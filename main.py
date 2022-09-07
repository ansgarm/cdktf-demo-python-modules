#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace
from eks_deployment import EksDeployment
from imports.vpc import Vpc
import cdktf_cdktf_provider_aws as aws

REGION = 'us-west-2'
AZS = [f'{REGION}{a}' for a in ["a", "b", "c"]]


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        aws.AwsProvider(self, 'aws', region=REGION)

        Vpc(self, "vpc",
            name=ns,
            cidr="10.99.0.0/18",

            enable_nat_gateway=False,

            azs=AZS,
            public_subnets=["10.99.0.0/24", "10.99.1.0/24", "10.99.2.0/24"],
            private_subnets=["10.99.3.0/24", "10.99.4.0/24", "10.99.5.0/24"],
            database_subnets=["10.99.7.0/24", "10.99.8.0/24", "10.99.9.0/24"],
            )

        deployment = EksDeployment(self, "deployment",
                                   deployment_name="my-web-app",
                                   container="nginx",
                                   )

        deployment.add_sidecar(container="fluent/fluentd")


app = App()
stack = MyStack(app, "demo-python-modules")
CloudBackend(stack,
             hostname='app.terraform.io',
             organization='cdktf-team',
             workspaces=NamedCloudWorkspace('demo-python-modules')
             )

app.synth()
