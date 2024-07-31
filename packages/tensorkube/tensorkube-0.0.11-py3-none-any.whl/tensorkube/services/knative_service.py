import subprocess
import time
from datetime import datetime
from typing import Optional

import click
import yaml
from kubernetes import config, client
from kubernetes.client import ApiException

from tensorkube.constants import KNATIVE_SERVING_NAMESPACE, CONFIG_FEATURES, TENSORFUSE_NAMESPACES, DEFAULT_NAMESPACE
from tensorkube.services.k8s_service import get_efs_claim_name


def get_instance_family_from_gpu_type(gpu_type):
    gpu_type = gpu_type.lower()
    if gpu_type == 'v100':
        return 'p3'
    elif gpu_type == 'a10g':
        return 'g5'
    elif gpu_type == 't4':
        return 'g4dn'
    elif gpu_type == 't4g':
        return 'g5g'
    elif gpu_type == 'l4':
        return 'g6'
    else:
        raise ValueError(f"Unsupported GPU type: {gpu_type}")


def get_supported_gpu_families():
    return ['p3', 'g5', 'g4dn', 'g5g', 'g6']


def apply_anti_affinity_for_gpus(yaml_dict):
    # this function assumes that already there are anti affinity terms
    existing_terms = \
    yaml_dict['spec']['template']['spec']['affinity']['nodeAffinity']['requiredDuringSchedulingIgnoredDuringExecution'][
        'nodeSelectorTerms']
    for term in existing_terms:
        for expression in term.get('matchExpressions', []):
            if expression['key'] == 'karpenter.k8s.aws/instance-family' and expression['operator'] == 'NotIn':
                expression['values'] = list(set(expression['values'] + get_supported_gpu_families()))
    return yaml_dict


def apply_knative_service_with_podman(service_name: str, yaml_file_path: str, sanitised_project_name: str,
                                      image_tag: str, workdir: str, command: str, gpus: int, gpu_type: str,
                                      env: Optional[str] = None, cpu: float = 100, memory: int = 200,
                                      min_scale: int = 0, max_scale: int = 3):
    # Load kube config
    config.load_kube_config()

    # Read the YAML file
    with open(yaml_file_path, 'r') as f:
        yaml_content = f.read()

    click.echo(f"Applying Knative service {service_name} for project {sanitised_project_name} and {gpus} GPUs.")
    yaml_content = yaml_content.replace('${SERVICE_NAME}', service_name)
    yaml_content = yaml_content.replace('${GPUS}', str(gpus))

    # Load the YAML content    
    yaml_dict = yaml.safe_load(yaml_content)

    for volume in yaml_dict['spec']['template']['spec']['volumes']:
        if volume['name'] == 'efs-storage':
            volume['persistentVolumeClaim']['claimName'] = get_efs_claim_name(env_name=env)

    if gpus > 0:
        yaml_dict['spec']['template']['spec']['containers'][0]['image'] = "tensorfuse/podman-nvidia:v1"
        config_nvidia_ctk_commands = """sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
               nvidia-ctk cdi list
            """
        podman_gpu_tags = "--gpus all --env NVIDIA_VISIBLE_DEVICES=all --env NVIDIA_DRIVER_CAPABILITIES=compute,utility"
    else:
        config_nvidia_ctk_commands = ""
        yaml_dict['spec']['template']['spec']['containers'][0]['image'] = "quay.io/podman/stable"
        podman_gpu_tags = ""

    if workdir:
        final_command = f"cd {workdir} && {command}"
    else:
        final_command = command

    yaml_dict['spec']['template']['spec']['containers'][0]['command'] = ["/bin/sh", "-c",
                                                                         f"""{config_nvidia_ctk_commands}
        sed -i 's|mount_program = "/usr/bin/fuse-overlayfs"|mount_program = ""|' /etc/containers/storage.conf
        sudo podman run --name mycontainer {podman_gpu_tags} --network=host \
         --rootfs /mnt/efs/images/{sanitised_project_name}/{image_tag}/rootfs:O sh -c "{final_command}" """]
    if gpus > 0:
        yaml_dict['spec']['template']['spec']['nodeSelector'] = {
            'karpenter.k8s.aws/instance-family': get_instance_family_from_gpu_type(gpu_type)}
    else:
        yaml_dict['spec']['template']['spec']['containers'][0]['resources']['requests'][
            'memory'] = f'{str(int(memory))}M'
        yaml_dict['spec']['template']['spec']['containers'][0]['resources']['requests']['cpu'] = f'{str(int(cpu))}m'
        apply_anti_affinity_for_gpus(yaml_dict)
    # apply min scale and max scale arguements
    yaml_dict['spec']['template']['metadata']['annotations']['autoscaling.knative.dev/min-scale'] = str(min_scale)
    yaml_dict['spec']['template']['metadata']['annotations']['autoscaling.knative.dev/max-scale'] = str(max_scale)

    yaml_dict['spec']['template']['metadata']['annotations']['image_tag'] = image_tag
    yaml_dict['spec']['template']['metadata']['annotations']['deploy_time'] = datetime.now().isoformat()

    # Create a Kubernetes API client
    k8s_client = client.CustomObjectsApi()

    # Apply the configuration
    group = "serving.knative.dev"
    version = "v1"
    namespace = env if env else DEFAULT_NAMESPACE
    plural = "services"

    # check if the custom object exists if yes then update else create
    try:
        existing_service = k8s_client.get_namespaced_custom_object(group, version, namespace, plural, service_name)
        resource_version = existing_service['metadata']['resourceVersion']
        # add the resource_version to the yaml dict
        yaml_dict['metadata']['resourceVersion'] = resource_version
        click.echo(f'Resource version is {resource_version}')
        # Remove immutable fields
        if 'metadata' in yaml_dict:
            if 'annotations' in yaml_dict['metadata']:
                if 'serving.knative.dev/creator' in yaml_dict['metadata']['annotations']:
                    del yaml_dict['metadata']['annotations']['serving.knative.dev/creator']
            if 'annotations' in yaml_dict['metadata']:
                if 'serving.knative.dev/lastModifier' in yaml_dict['metadata']['annotations']:
                    del yaml_dict['metadata']['annotations']['serving.knative.dev/lastModifier']
        k8s_client.patch_namespaced_custom_object(group, version, namespace, plural, service_name, yaml_dict)
        click.echo(f"Updated Knative service {service_name}.")
    except client.exceptions.ApiException as e:
        if e.status == 404:
            k8s_client.create_namespaced_custom_object(group, version, namespace, plural, yaml_dict)
            click.echo(f"Created Knative service {service_name}.")
        else:
            click.echo(f"Error applying Knative service: {e}")
            raise e


def enable_knative_selectors_pv_pvc_capabilities(namespace=KNATIVE_SERVING_NAMESPACE):
    """
    Enable the nodeSelector feature in the config-features ConfigMap.

    Args:
        namespace (str): The namespace where the ConfigMap is located. Defaults to 'knative-serving'.
    """
    # Load the kubeconfig
    config.load_kube_config()

    # Create an instance of the API class
    v1 = client.CoreV1Api()

    try:
        # Get the existing config-features ConfigMap
        config_map = v1.read_namespaced_config_map(name=CONFIG_FEATURES, namespace=namespace)

        # Update the ConfigMap data
        if config_map.data is None:
            config_map.data = {}
        config_map.data['kubernetes.podspec-nodeselector'] = 'enabled'
        config_map.data['kubernetes.podspec-affinity'] = 'enabled'
        config_map.data["kubernetes.podspec-persistent-volume-claim"] = "enabled"
        config_map.data["kubernetes.podspec-persistent-volume-write"] = "enabled"
        config_map.data["kubernetes.containerspec-addcapabilities"] = "enabled"
        config_map.data["kubernetes.podspec-security-context"] = "enabled"

        # Update the ConfigMap
        v1.patch_namespaced_config_map(name=CONFIG_FEATURES, namespace=namespace, body=config_map)
        print(
            f"Successfully enabled node selector, affinity, pv-claim, pv-write and add-capabilities features in {CONFIG_FEATURES} ConfigMap.")
    except client.exceptions.ApiException as e:
        print(f"Exception when updating ConfigMap: {e}")
        raise

def list_deployed_services(env_name: Optional[str] = None, all: bool = False):
    config.load_kube_config()
    api = client.CustomObjectsApi()
    if all:
        ksvc_list = api.list_cluster_custom_object(
            group="serving.knative.dev",
            version="v1",
            plural="services",
        )
    else:
        namespace = env_name if env_name else DEFAULT_NAMESPACE
        ksvc_list = api.list_namespaced_custom_object(
            group="serving.knative.dev",
            version="v1",
            plural="services",
            namespace=namespace,
        )

    return ksvc_list


def get_knative_service(service_name: str, namespace: str = "default"):
    config.load_kube_config()
    api = client.CustomObjectsApi()
    ksvc = api.get_namespaced_custom_object(
        group="serving.knative.dev",
        version="v1",
        plural="services",
        name=service_name,
        namespace=namespace,
    )
    return ksvc


def get_ready_condition(service):
    ready_condition = [condition for condition in service['status']['conditions'] if condition['type'] == 'Ready']
    if ready_condition:
        return ready_condition[0]
    return None


def get_latest_running_revision(service_name: str, namespace: str = "default"):
    service = get_knative_service(service_name, namespace)
    latest_revision_name = service['status']['latestReadyRevisionName']
    return latest_revision_name


def get_pods_for_service(service_name: str, namespace: str = "default"):
    config.load_kube_config()
    api = client.CoreV1Api()
    latest_revision = get_latest_running_revision(service_name, namespace)
    pods = api.list_namespaced_pod(namespace=namespace, 
                                   label_selector=f"serving.knative.dev/service={service_name},serving.knative.dev/revision={latest_revision}")
    return pods


def delete_knative_services():
    # kubectl delete ksvc --all -n <your-namespace>
    command = ["kubectl", "delete", "ksvc", "--all", "-n", "default"]
    subprocess.run(command, check=True)  # TODO maybe wait for pods to scale down before returning


def cleanup_knative_resources():
    try:
        # kubectl delete gateway --all -n istio-system
        command = ["kubectl", "delete", "gateway", "--all", "-n", "istio-system"]
        subprocess.run(command, check=True)
        #  kubectl delete gateway --all -n knative-serving
        command = ["kubectl", "delete", "gateway", "--all", "-n", "knative-serving"]
        subprocess.run(command, check=True)
    except Exception as e:
        click.echo(f"Error while cleaning up Istio gateways: {e}")


def list_ksvc_in_namespace(namespace: str):
    # Load the Kubernetes configuration
    config.load_kube_config()

    # Create an instance of the CustomObjectsApi
    api_instance = client.CustomObjectsApi()

    # Define the group, version, and plural for the Knative service
    group = 'serving.knative.dev'
    version = 'v1'
    plural = 'services'

    try:
        # List all Knative services in the specified namespace
        services = api_instance.list_namespaced_custom_object(group=group, version=version, namespace=namespace,
                                                              plural=plural)
        return services
    except ApiException as e:
        print(f"Failed to list Knative services in namespace {namespace}: {e}")
        raise e


def delete_ksvc_from_namespace(service_name: str, namespace: str):
    # Load the Kubernetes configuration
    config.load_kube_config()

    # Create an instance of the CustomObjectsApi
    api_instance = client.CustomObjectsApi()

    # Define the group, version, and plural for the Knative service
    group = 'serving.knative.dev'
    version = 'v1'
    plural = 'services'

    try:
        # Delete the Knative service
        api_instance.delete_namespaced_custom_object(group=group, version=version, namespace=namespace, plural=plural,
                                                     name=service_name, body=client.V1DeleteOptions())
        print(f"Knative service {service_name} deletion initiated.")
        # Wait for the service to be deleted
        while True:
            try:
                api_instance.get_namespaced_custom_object(group, version, namespace, plural, service_name)
                time.sleep(1)  # Wait for 1 second before checking again
            except ApiException as e:
                if e.status == 404:
                    print(f"Knative service {service_name} deleted successfully.")
                    break
                else:
                    print(f"Error while waiting for deletion of Knative service {service_name}: {e}")
                    raise e
        print(f"Knative service {service_name} deleted successfully.")
    except ApiException as e:
        print(f"Failed to delete Knative service {service_name}: {e}")


def delete_all_ksvc_from_namespace(namespace: str):
    if namespace in TENSORFUSE_NAMESPACES:
        click.echo(f"Namespace {namespace} is a system namespace. Skipping deletion of Knative services.")
        return False
    services = list_ksvc_in_namespace(namespace)
    for service in services['items']:
        service_name = service['metadata']['name']
        delete_ksvc_from_namespace(service_name, namespace)
