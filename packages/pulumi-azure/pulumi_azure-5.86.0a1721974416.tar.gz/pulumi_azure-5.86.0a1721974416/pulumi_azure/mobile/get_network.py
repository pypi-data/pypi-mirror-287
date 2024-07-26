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
    'GetNetworkResult',
    'AwaitableGetNetworkResult',
    'get_network',
    'get_network_output',
]

@pulumi.output_type
class GetNetworkResult:
    """
    A collection of values returned by getNetwork.
    """
    def __init__(__self__, id=None, location=None, mobile_country_code=None, mobile_network_code=None, name=None, resource_group_name=None, service_key=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mobile_country_code and not isinstance(mobile_country_code, str):
            raise TypeError("Expected argument 'mobile_country_code' to be a str")
        pulumi.set(__self__, "mobile_country_code", mobile_country_code)
        if mobile_network_code and not isinstance(mobile_network_code, str):
            raise TypeError("Expected argument 'mobile_network_code' to be a str")
        pulumi.set(__self__, "mobile_network_code", mobile_network_code)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if service_key and not isinstance(service_key, str):
            raise TypeError("Expected argument 'service_key' to be a str")
        pulumi.set(__self__, "service_key", service_key)
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
        The Azure Region where the Mobile Network should exist. Changing this forces a new Mobile Network to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mobileCountryCode")
    def mobile_country_code(self) -> str:
        """
        Mobile country code (MCC), defined in https://www.itu.int/rec/T-REC-E.212 .
        """
        return pulumi.get(self, "mobile_country_code")

    @property
    @pulumi.getter(name="mobileNetworkCode")
    def mobile_network_code(self) -> str:
        """
        Mobile network code (MNC), defined in https://www.itu.int/rec/T-REC-E.212 .
        """
        return pulumi.get(self, "mobile_network_code")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> str:
        """
        The mobile network resource identifier.
        """
        return pulumi.get(self, "service_key")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags which should be assigned to the Mobile Network.
        """
        return pulumi.get(self, "tags")


class AwaitableGetNetworkResult(GetNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkResult(
            id=self.id,
            location=self.location,
            mobile_country_code=self.mobile_country_code,
            mobile_network_code=self.mobile_network_code,
            name=self.name,
            resource_group_name=self.resource_group_name,
            service_key=self.service_key,
            tags=self.tags)


def get_network(name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkResult:
    """
    Get information about an Azure Mobile Network.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.mobile.get_network(name="example-mn",
        resource_group_name=example_azurerm_resource_group["name"])
    ```


    :param str name: Specifies the name which should be used for this Mobile Network.
    :param str resource_group_name: Specifies the name of the Resource Group where the Mobile Network should exist.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:mobile/getNetwork:getNetwork', __args__, opts=opts, typ=GetNetworkResult).value

    return AwaitableGetNetworkResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        mobile_country_code=pulumi.get(__ret__, 'mobile_country_code'),
        mobile_network_code=pulumi.get(__ret__, 'mobile_network_code'),
        name=pulumi.get(__ret__, 'name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        service_key=pulumi.get(__ret__, 'service_key'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_network)
def get_network_output(name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkResult]:
    """
    Get information about an Azure Mobile Network.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.mobile.get_network(name="example-mn",
        resource_group_name=example_azurerm_resource_group["name"])
    ```


    :param str name: Specifies the name which should be used for this Mobile Network.
    :param str resource_group_name: Specifies the name of the Resource Group where the Mobile Network should exist.
    """
    ...
