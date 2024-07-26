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
    'GetResourceGroupResult',
    'AwaitableGetResourceGroupResult',
    'get_resource_group',
    'get_resource_group_output',
]

@pulumi.output_type
class GetResourceGroupResult:
    """
    A collection of values returned by getResourceGroup.
    """
    def __init__(__self__, id=None, location=None, managed_by=None, name=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region where the Resource Group exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> str:
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the Resource Group.
        """
        return pulumi.get(self, "tags")


class AwaitableGetResourceGroupResult(GetResourceGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceGroupResult(
            id=self.id,
            location=self.location,
            managed_by=self.managed_by,
            name=self.name,
            tags=self.tags)


def get_resource_group(name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceGroupResult:
    """
    Use this data source to access information about an existing Resource Group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.core.get_resource_group(name="existing")
    pulumi.export("id", example.id)
    ```


    :param str name: The Name of this Resource Group.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:core/getResourceGroup:getResourceGroup', __args__, opts=opts, typ=GetResourceGroupResult).value

    return AwaitableGetResourceGroupResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        managed_by=pulumi.get(__ret__, 'managed_by'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_resource_group)
def get_resource_group_output(name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceGroupResult]:
    """
    Use this data source to access information about an existing Resource Group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.core.get_resource_group(name="existing")
    pulumi.export("id", example.id)
    ```


    :param str name: The Name of this Resource Group.
    """
    ...
