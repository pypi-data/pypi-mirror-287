# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

__all__ = [
    'GetResourceGroupTemplateDeploymentResult',
    'AwaitableGetResourceGroupTemplateDeploymentResult',
    'get_resource_group_template_deployment',
    'get_resource_group_template_deployment_output',
]

@pulumi.output_type
class GetResourceGroupTemplateDeploymentResult:
    """
    A collection of values returned by getResourceGroupTemplateDeployment.
    """
    def __init__(__self__, id=None, name=None, output_content=None, resource_group_name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if output_content and not isinstance(output_content, str):
            raise TypeError("Expected argument 'output_content' to be a str")
        pulumi.set(__self__, "output_content", output_content)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputContent")
    def output_content(self) -> str:
        """
        The JSON Content of the Outputs of the ARM Template Deployment.
        """
        return pulumi.get(self, "output_content")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")


class AwaitableGetResourceGroupTemplateDeploymentResult(GetResourceGroupTemplateDeploymentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceGroupTemplateDeploymentResult(
            id=self.id,
            name=self.name,
            output_content=self.output_content,
            resource_group_name=self.resource_group_name)


def get_resource_group_template_deployment(name: Optional[str] = None,
                                           resource_group_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceGroupTemplateDeploymentResult:
    """
    Use this data source to access information about an existing Resource Group Template Deployment.


    :param str name: The name of this Resource Group Template Deployment.
    :param str resource_group_name: The name of the Resource Group to which the Resource Group Template Deployment was applied.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:core/getResourceGroupTemplateDeployment:getResourceGroupTemplateDeployment', __args__, opts=opts, typ=GetResourceGroupTemplateDeploymentResult).value

    return AwaitableGetResourceGroupTemplateDeploymentResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        output_content=pulumi.get(__ret__, 'output_content'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'))


@_utilities.lift_output_func(get_resource_group_template_deployment)
def get_resource_group_template_deployment_output(name: Optional[pulumi.Input[str]] = None,
                                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceGroupTemplateDeploymentResult]:
    """
    Use this data source to access information about an existing Resource Group Template Deployment.


    :param str name: The name of this Resource Group Template Deployment.
    :param str resource_group_name: The name of the Resource Group to which the Resource Group Template Deployment was applied.
    """
    ...
