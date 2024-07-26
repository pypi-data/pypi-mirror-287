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
    'GetAvailabilitySetResult',
    'AwaitableGetAvailabilitySetResult',
    'get_availability_set',
    'get_availability_set_output',
]

@pulumi.output_type
class GetAvailabilitySetResult:
    """
    A collection of values returned by getAvailabilitySet.
    """
    def __init__(__self__, id=None, location=None, managed=None, name=None, platform_fault_domain_count=None, platform_update_domain_count=None, resource_group_name=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed and not isinstance(managed, bool):
            raise TypeError("Expected argument 'managed' to be a bool")
        pulumi.set(__self__, "managed", managed)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if platform_fault_domain_count and not isinstance(platform_fault_domain_count, str):
            raise TypeError("Expected argument 'platform_fault_domain_count' to be a str")
        pulumi.set(__self__, "platform_fault_domain_count", platform_fault_domain_count)
        if platform_update_domain_count and not isinstance(platform_update_domain_count, str):
            raise TypeError("Expected argument 'platform_update_domain_count' to be a str")
        pulumi.set(__self__, "platform_update_domain_count", platform_update_domain_count)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
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
        The supported Azure location where the Availability Set exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def managed(self) -> bool:
        """
        Whether the availability set is managed or not.
        """
        return pulumi.get(self, "managed")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> str:
        """
        The number of fault domains that are used.
        """
        return pulumi.get(self, "platform_fault_domain_count")

    @property
    @pulumi.getter(name="platformUpdateDomainCount")
    def platform_update_domain_count(self) -> str:
        """
        The number of update domains that are used.
        """
        return pulumi.get(self, "platform_update_domain_count")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetAvailabilitySetResult(GetAvailabilitySetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAvailabilitySetResult(
            id=self.id,
            location=self.location,
            managed=self.managed,
            name=self.name,
            platform_fault_domain_count=self.platform_fault_domain_count,
            platform_update_domain_count=self.platform_update_domain_count,
            resource_group_name=self.resource_group_name,
            tags=self.tags)


def get_availability_set(name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAvailabilitySetResult:
    """
    Use this data source to access information about an existing Availability Set.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.compute.get_availability_set(name="tf-appsecuritygroup",
        resource_group_name="my-resource-group")
    pulumi.export("availabilitySetId", example.id)
    ```


    :param str name: The name of the Availability Set.
    :param str resource_group_name: The name of the resource group in which the Availability Set exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:compute/getAvailabilitySet:getAvailabilitySet', __args__, opts=opts, typ=GetAvailabilitySetResult).value

    return AwaitableGetAvailabilitySetResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        managed=pulumi.get(__ret__, 'managed'),
        name=pulumi.get(__ret__, 'name'),
        platform_fault_domain_count=pulumi.get(__ret__, 'platform_fault_domain_count'),
        platform_update_domain_count=pulumi.get(__ret__, 'platform_update_domain_count'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_availability_set)
def get_availability_set_output(name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAvailabilitySetResult]:
    """
    Use this data source to access information about an existing Availability Set.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.compute.get_availability_set(name="tf-appsecuritygroup",
        resource_group_name="my-resource-group")
    pulumi.export("availabilitySetId", example.id)
    ```


    :param str name: The name of the Availability Set.
    :param str resource_group_name: The name of the resource group in which the Availability Set exists.
    """
    ...
