from kubernetes import client, config
from prettytable import PrettyTable

def get_allocatable_gpus(nod):
    if 'nvidia.com/gpu' in nod.status.allocatable:
        return nod.status.allocatable['nvidia.com/gpu']

    return ''


def format_bytes(size):
    # 2**10 = 1024
    if 'Ki' in size:
        size = int(str(size).replace('Ki', '')) * 1024

    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return '{0} {1}'.format(round(size, 2), power_labels[n]+'B')


def get_instance_type(metadata):
    if 'node.kubernetes.io/instance-type' in metadata.labels.keys():
        return metadata.labels['node.kubernetes.io/instance-type']

    return ''


def get_node_group_name(metadata):
    if 'node.kubernetes.io/nodegroup' in metadata.labels.keys():
        return metadata.labels['node.kubernetes.io/nodegroup']

    return ''


def get_node_taints(node_spec):
    taints = []
    if node_spec.taints is None:
        return ''

    for taint in node_spec.taints:
        taints.append('{0}={1}:{2}'.format(taint.key, taint.value, taint.effect))

    return ','.join(taints)


def list_nodes_info():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    ret = v1.list_node()

    table = PrettyTable()
    table.field_names = ['Name', 'Type', 'Group Name', 'GPUs', 'CPUs', 'Memory', 'SSD', 'Taints']
    table.align['Name'] = 'l'
    table.align['Group Name'] = 'l'
    table.align['Memory'] = 'r'
    table.align['SSD'] = 'r'
    table.align['GPUs'] = 'r'
    table.align['CPUs'] = 'r'
    table.align['Taints'] = 'l'

    for nod in ret.items:
        table.add_row([
            nod.metadata.name,
            get_instance_type(nod.metadata),
            get_node_group_name(nod.metadata),
            get_allocatable_gpus(nod),
            nod.status.capacity['cpu'],
            format_bytes(nod.status.capacity['memory']),
            format_bytes(nod.status.capacity['ephemeral-storage']),
            get_node_taints(nod.spec)
        ])
        # exit(0)

    print(table.get_string())
