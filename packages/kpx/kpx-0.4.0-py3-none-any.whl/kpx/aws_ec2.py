from .utils import Output
from prettytable import PrettyTable


class AwsResourceQuery:
    def __init__(self, client):
        self.client = client

    def list_ec2(self):
        table = PrettyTable()
        table.field_names = self.get_table_header()
        table.align['PrivateIP'] = 'r'
        table.align['PublicIP'] = 'r'
        table.align['Name'] = 'r'

        ec2_instances = self.list_ec2_instances()
        if len(ec2_instances) > 0:
            table.add_rows(ec2_instances)
            print(table.get_string())

    @staticmethod
    def get_table_header():
        return ["ID", "Name", "Type", "PrivateIP", "PublicIP", "State"]

    @staticmethod
    def get_instance_name_from_tags(tags):
        for item in tags:
            if item['Key'] == 'Name':
                return item['Value']

        return '---'

    def list_ec2_instances(self):
        instances = []
        try:
            resp = self.client.describe_instances()
        except Exception as e:
            Output.error(e)
            return []

        for reservation in resp['Reservations']:
            for instance in reservation['Instances']:
                # print(instance)
                data = {
                    'id': instance['InstanceId'],
                    'name': self.get_instance_name_from_tags(instance['Tags']),
                    'type': instance['InstanceType'],
                    'PrivateIp': instance['PrivateIpAddress'] if 'PrivateIpAddress' in instance else '-',
                    'PublicIp': instance['PublicIpAddress'] if 'PublicIpAddress' in instance else '-',
                    'state': instance['State']['Name'],
                }

                instances.append(data.values())

        return instances
