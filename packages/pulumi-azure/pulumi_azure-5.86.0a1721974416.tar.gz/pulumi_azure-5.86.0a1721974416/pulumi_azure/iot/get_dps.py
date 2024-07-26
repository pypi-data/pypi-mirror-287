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
    'GetDpsResult',
    'AwaitableGetDpsResult',
    'get_dps',
    'get_dps_output',
]

@pulumi.output_type
class GetDpsResult:
    """
    A collection of values returned by getDps.
    """
    def __init__(__self__, allocation_policy=None, device_provisioning_host_name=None, id=None, id_scope=None, location=None, name=None, resource_group_name=None, service_operations_host_name=None, tags=None):
        if allocation_policy and not isinstance(allocation_policy, str):
            raise TypeError("Expected argument 'allocation_policy' to be a str")
        pulumi.set(__self__, "allocation_policy", allocation_policy)
        if device_provisioning_host_name and not isinstance(device_provisioning_host_name, str):
            raise TypeError("Expected argument 'device_provisioning_host_name' to be a str")
        pulumi.set(__self__, "device_provisioning_host_name", device_provisioning_host_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if id_scope and not isinstance(id_scope, str):
            raise TypeError("Expected argument 'id_scope' to be a str")
        pulumi.set(__self__, "id_scope", id_scope)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if service_operations_host_name and not isinstance(service_operations_host_name, str):
            raise TypeError("Expected argument 'service_operations_host_name' to be a str")
        pulumi.set(__self__, "service_operations_host_name", service_operations_host_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="allocationPolicy")
    def allocation_policy(self) -> str:
        """
        The allocation policy of the IoT Device Provisioning Service.
        """
        return pulumi.get(self, "allocation_policy")

    @property
    @pulumi.getter(name="deviceProvisioningHostName")
    def device_provisioning_host_name(self) -> str:
        """
        The device endpoint of the IoT Device Provisioning Service.
        """
        return pulumi.get(self, "device_provisioning_host_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idScope")
    def id_scope(self) -> str:
        """
        The unique identifier of the IoT Device Provisioning Service.
        """
        return pulumi.get(self, "id_scope")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Specifies the supported Azure location where the IoT Device Provisioning Service exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="serviceOperationsHostName")
    def service_operations_host_name(self) -> str:
        """
        The service endpoint of the IoT Device Provisioning Service.
        """
        return pulumi.get(self, "service_operations_host_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "tags")


class AwaitableGetDpsResult(GetDpsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDpsResult(
            allocation_policy=self.allocation_policy,
            device_provisioning_host_name=self.device_provisioning_host_name,
            id=self.id,
            id_scope=self.id_scope,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            service_operations_host_name=self.service_operations_host_name,
            tags=self.tags)


def get_dps(name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            tags: Optional[Mapping[str, str]] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDpsResult:
    """
    Use this data source to access information about an existing IotHub Device Provisioning Service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.iot.get_dps(name="iot_hub_dps_test",
        resource_group_name="iothub_dps_rg")
    ```


    :param str name: Specifies the name of the Iot Device Provisioning Service resource.
    :param str resource_group_name: The name of the resource group under which the Iot Device Provisioning Service is located in.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['tags'] = tags
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:iot/getDps:getDps', __args__, opts=opts, typ=GetDpsResult).value

    return AwaitableGetDpsResult(
        allocation_policy=pulumi.get(__ret__, 'allocation_policy'),
        device_provisioning_host_name=pulumi.get(__ret__, 'device_provisioning_host_name'),
        id=pulumi.get(__ret__, 'id'),
        id_scope=pulumi.get(__ret__, 'id_scope'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        service_operations_host_name=pulumi.get(__ret__, 'service_operations_host_name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_dps)
def get_dps_output(name: Optional[pulumi.Input[str]] = None,
                   resource_group_name: Optional[pulumi.Input[str]] = None,
                   tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDpsResult]:
    """
    Use this data source to access information about an existing IotHub Device Provisioning Service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.iot.get_dps(name="iot_hub_dps_test",
        resource_group_name="iothub_dps_rg")
    ```


    :param str name: Specifies the name of the Iot Device Provisioning Service resource.
    :param str resource_group_name: The name of the resource group under which the Iot Device Provisioning Service is located in.
    """
    ...
