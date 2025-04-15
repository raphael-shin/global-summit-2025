from aws_cdk import Stack, CustomResource
from aws_cdk import aws_sagemaker as sagemaker
from aws_cdk import aws_iam as iam
from constructs import Construct

class GfpganSageMakerEndpointStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, gfpgan_image_uri: str, codebuild_status_resource: CustomResource, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        gfpgan_sagemaker_endpoint_name = self.node.try_get_context("gfpgan_sagemaker_endpoint_name")
        gfpgan_sagemaker_endpoint_instance_count = self.node.try_get_context("gfpgan_sagemaker_endpoint_instance_count")
        gfpgan_sagemaker_endpoint_instance_type = self.node.try_get_context("gfpgan_sagemaker_endpoint_instance_type")

        # Add a dependency on the CodeBuild status resource
        self.node.add_dependency(codebuild_status_resource)
        
        # Create IAM Role for SageMaker
        sagemaker_role = iam.Role(self, "SageMakerExecutionRole",
            assumed_by=iam.ServicePrincipal("sagemaker.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSageMakerFullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess")
            ]
        )

        # Create SageMaker Model for GFPGAN
        gfpgan_model = sagemaker.CfnModel(self, "GfpganSageMakerModel",
            execution_role_arn=sagemaker_role.role_arn,
            primary_container={
                "image": gfpgan_image_uri,
                "mode": "SingleModel"
            },
            model_name="gfpgan-sagemaker-model"
        )

        # Create SageMaker Endpoint Configuration for GFPGAN
        gfpgan_sagemaker_endpoint_config = sagemaker.CfnEndpointConfig(self, "GfpganSageMakerEndpointConfig",
            production_variants=[
                {
                    "initialInstanceCount": gfpgan_sagemaker_endpoint_instance_count,
                    "instanceType": gfpgan_sagemaker_endpoint_instance_type,
                    "modelName": gfpgan_model.model_name,
                    "variantName": "GfpganVariant",
                    "initialVariantWeight": 1
                }
            ],
            endpoint_config_name="gfpgan-sagemaker-endpoint-config"
        )
        gfpgan_sagemaker_endpoint_config.add_dependency(gfpgan_model)

        # Create SageMaker Endpoint for GFPGAN
        gfpgan_endpoint = sagemaker.CfnEndpoint(self, "GfpganSageMakerEndpoint",
            endpoint_config_name=gfpgan_sagemaker_endpoint_config.endpoint_config_name,
            endpoint_name=gfpgan_sagemaker_endpoint_name
        )
        gfpgan_endpoint.add_dependency(gfpgan_sagemaker_endpoint_config)

        # Expose endpoint names as properties
        self.gfpgan_endpoint_name = gfpgan_endpoint.endpoint_name