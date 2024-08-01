from prettytable import PrettyTable
from .utils import Output
from .aws_config import AwsConfigManager


class Route53():
    @staticmethod
    def list_r53(client, zone_id=''):
        if zone_id != '':
            Output.header(f'List Records for ZoneID: {zone_id}')
            resp = client.list_resource_record_sets(
                HostedZoneId=zone_id
            )

            table = PrettyTable()
            table.field_names = ["Name", "Type", "Targets"]
            table.align['Name'] = 'r'
            table.align['Targets'] = 'l'

            for rec in resp['ResourceRecordSets']:
                if 'AliasTarget' in rec:
                    table.add_row([
                        rec['Name'].strip('.'),
                        rec['Type'],
                        '(alias) ' + rec['AliasTarget']['DNSName'].strip('.')[:128]
                    ])

                if 'ResourceRecords' in rec:
                    table.add_row([
                        rec['Name'].strip('.'),
                        rec['Type'],
                        '\n'.join([d['Value'][:128] for d in rec['ResourceRecords']])
                    ])

            print(table.get_string())
            return None
        try:
            resp = client.list_hosted_zones()

            table = PrettyTable()
            table.field_names = ["Domain", "Id", "Records"]
            table.align['Domain'] = 'r'
            table.align['Records'] = 'r'

            if len(resp['HostedZones']) > 0:
                for zone in resp['HostedZones']:
                    table.add_row([
                        zone['Name'].strip('.'),
                        zone['Id'].replace('/hostedzone/', ''),
                        zone['ResourceRecordSetCount']
                    ])
                print(f'\nAccount id: {AwsConfigManager.account_id}')
                print(table.get_string())
            else:
                Output.error(f'No hosted zones in account: {AwsConfigManager.account_id}')
        except Exception as e:
            Output.error(e)
