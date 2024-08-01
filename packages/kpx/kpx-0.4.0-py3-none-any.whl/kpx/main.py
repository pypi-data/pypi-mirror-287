#!/usr/bin/env python3

import typer
import boto3

from typing import Optional

from .aws_config import AwsConfigManager
from .aws_ec2 import AwsResourceQuery
from .aws_ecr import ContainerRegistry
from .aws_vpc import VpcManager
from .aws_route53 import Route53
from .aws_lb import AwsLb
from .eks_nodes import list_nodes_info

app = typer.Typer(help="KPX application for aws profiles", no_args_is_help=True)


@app.command()
def cfg(
    aws_profile: Optional[str] = typer.Argument('default'),
    region: Optional[str] = typer.Argument("us-east-1"),
    output: Optional[str] = typer.Argument("json")
):
    """
    Configure ~/.aws/config file with profiles settings
    """
    AwsConfigManager.generate_config(aws_profile, region, output)


@app.command()
def cred(
    aws_profile: Optional[str] = typer.Argument('default'),
    key: Optional[str] = typer.Argument(""),
    secret: Optional[str] = typer.Argument("")
):
    """
    Configure ~/.aws/credentials file with aws credentials
    """
    AwsConfigManager.generate_credentials(aws_profile, key, secret)


@app.command()
def r53(zone_id: Optional[str] = typer.Argument('')):
    """
    List Route53 hosted zones
    """
    client = boto3.client('route53')
    Route53.list_r53(client, zone_id)


@app.command()
def ecr(repo_name: Optional[str] = typer.Argument('')):
    """
    List ECR repositories
    """
    client = boto3.client('ecr')

    ecr = ContainerRegistry(client)

    if repo_name != '':
        ecr.get_images(repo_name, AwsConfigManager.account_id)
    else:
        ecr.get_repositories()


@app.command()
def ec2():
    """
    List EC2 instances
    """
    client = boto3.client('ec2')
    arq = AwsResourceQuery(client)
    arq.list_ec2()


@app.command()
def lb():
    """
    List Load Balancers
    """
    client = boto3.client('elbv2')
    awslb = AwsLb(client)
    awslb.get_load_balancers()


@app.command()
def vpc(vpc_id: Optional[str] = typer.Argument('')):
    """
    List VPCs and show Cidr blocks or subnets for provided VPC ID
    """
    session = boto3.Session(region_name=str(AwsConfigManager.aws_region()))
    vm = VpcManager(session)
    if vpc_id != '':
        print(f'Showing item: {vpc_id}')
        vm.get_vpc_subnets(vpc_id)
    else:
        print(f'List all available VPCs in {AwsConfigManager.aws_region()}')
        client = boto3.client('ec2', region_name=AwsConfigManager.aws_region())
        vm.get_vpc_list(client)


@app.command()
def nodes():
    """
    List EKS nodes and show some information about them
    """
    from kubernetes import client, config
    config.load_kube_config()

    k8sapi = client.CoreV1Api()

    list_nodes_info(k8sapi)


if __name__ == '__main__':  # pragma: no cover
    app()
