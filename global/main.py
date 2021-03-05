#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput, S3Backend

# for terraform provider
from imports.aws import AwsProvider, DataAwsCallerIdentity

# for terraform module
from imports.terraform_aws_modules.vpc.aws import Vpc

# get this from the ENV or passed into the app, hard-coding it for now
# env = 'production'


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        S3Backend(self,
                  bucket=f"fr-personal-account-config",
                  encrypt=True,
                  key=f"cdktf-test/{ns}.tfstate")

        AwsProvider(self, 'Aws', region='us-west-2')

        my_vpc = Vpc(self, f"{ns}-vpc",
                     name=f"{ns}-vpc",
                     cidr='10.9.0.0/16',
                     azs=['us-west-2a', 'us-west-2b', 'us-west-2c'],
                     private_subnets=['10.9.1.0/24', '10.9.2.0/24', '10.9.3.0/24'],
                     public_subnets=['10.9.101.0/24', '10.9.102.0/24', '10.9.103.0/24'],
                     enable_nat_gateway=True
                     )

        TerraformOutput(self, 'vpc_arn',
                        value=my_vpc.vpc_arn_output
                        )

app = App()
env = 'production'
MyStack(app, f"{env}-global")
app.synth()
