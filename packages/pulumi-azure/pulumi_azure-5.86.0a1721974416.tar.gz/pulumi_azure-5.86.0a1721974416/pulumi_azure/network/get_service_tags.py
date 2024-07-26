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
    'GetServiceTagsResult',
    'AwaitableGetServiceTagsResult',
    'get_service_tags',
    'get_service_tags_output',
]

@pulumi.output_type
class GetServiceTagsResult:
    """
    A collection of values returned by getServiceTags.
    """
    def __init__(__self__, address_prefixes=None, id=None, ipv4_cidrs=None, ipv6_cidrs=None, location=None, location_filter=None, name=None, service=None):
        if address_prefixes and not isinstance(address_prefixes, list):
            raise TypeError("Expected argument 'address_prefixes' to be a list")
        pulumi.set(__self__, "address_prefixes", address_prefixes)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv4_cidrs and not isinstance(ipv4_cidrs, list):
            raise TypeError("Expected argument 'ipv4_cidrs' to be a list")
        pulumi.set(__self__, "ipv4_cidrs", ipv4_cidrs)
        if ipv6_cidrs and not isinstance(ipv6_cidrs, list):
            raise TypeError("Expected argument 'ipv6_cidrs' to be a list")
        pulumi.set(__self__, "ipv6_cidrs", ipv6_cidrs)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if location_filter and not isinstance(location_filter, str):
            raise TypeError("Expected argument 'location_filter' to be a str")
        pulumi.set(__self__, "location_filter", location_filter)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if service and not isinstance(service, str):
            raise TypeError("Expected argument 'service' to be a str")
        pulumi.set(__self__, "service", service)

    @property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> Sequence[str]:
        """
        List of address prefixes for the service type (and optionally a specific region).
        """
        return pulumi.get(self, "address_prefixes")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv4Cidrs")
    def ipv4_cidrs(self) -> Sequence[str]:
        """
        List of IPv4 addresses for the service type (and optionally a specific region)
        """
        return pulumi.get(self, "ipv4_cidrs")

    @property
    @pulumi.getter(name="ipv6Cidrs")
    def ipv6_cidrs(self) -> Sequence[str]:
        """
        List of IPv6 addresses for the service type (and optionally a specific region)
        """
        return pulumi.get(self, "ipv6_cidrs")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="locationFilter")
    def location_filter(self) -> Optional[str]:
        return pulumi.get(self, "location_filter")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this Service Tags block.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def service(self) -> str:
        return pulumi.get(self, "service")


class AwaitableGetServiceTagsResult(GetServiceTagsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceTagsResult(
            address_prefixes=self.address_prefixes,
            id=self.id,
            ipv4_cidrs=self.ipv4_cidrs,
            ipv6_cidrs=self.ipv6_cidrs,
            location=self.location,
            location_filter=self.location_filter,
            name=self.name,
            service=self.service)


def get_service_tags(location: Optional[str] = None,
                     location_filter: Optional[str] = None,
                     service: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceTagsResult:
    """
    Use this data source to access information about Service Tags.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_service_tags(location="westcentralus",
        service="AzureKeyVault",
        location_filter="northeurope")
    pulumi.export("addressPrefixes", example.address_prefixes)
    pulumi.export("ipv4Cidrs", example.ipv4_cidrs)
    ```


    :param str location: The Azure Region where the Service Tags exists. This value is not used to filter the results but for specifying the region to request. For filtering by region use `location_filter` instead.  More information can be found here: [Service Tags URL parameters](https://docs.microsoft.com/rest/api/virtualnetwork/servicetags/list#uri-parameters).
    :param str location_filter: Changes the scope of the service tags. Can be any value that is also valid for `location`. If this field is empty then all address prefixes are considered instead of only location specific ones.
    :param str service: The type of the service for which address prefixes will be fetched. Available service tags can be found here: [Available service tags](https://docs.microsoft.com/azure/virtual-network/service-tags-overview#available-service-tags).
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['locationFilter'] = location_filter
    __args__['service'] = service
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:network/getServiceTags:getServiceTags', __args__, opts=opts, typ=GetServiceTagsResult).value

    return AwaitableGetServiceTagsResult(
        address_prefixes=pulumi.get(__ret__, 'address_prefixes'),
        id=pulumi.get(__ret__, 'id'),
        ipv4_cidrs=pulumi.get(__ret__, 'ipv4_cidrs'),
        ipv6_cidrs=pulumi.get(__ret__, 'ipv6_cidrs'),
        location=pulumi.get(__ret__, 'location'),
        location_filter=pulumi.get(__ret__, 'location_filter'),
        name=pulumi.get(__ret__, 'name'),
        service=pulumi.get(__ret__, 'service'))


@_utilities.lift_output_func(get_service_tags)
def get_service_tags_output(location: Optional[pulumi.Input[str]] = None,
                            location_filter: Optional[pulumi.Input[Optional[str]]] = None,
                            service: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceTagsResult]:
    """
    Use this data source to access information about Service Tags.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.network.get_service_tags(location="westcentralus",
        service="AzureKeyVault",
        location_filter="northeurope")
    pulumi.export("addressPrefixes", example.address_prefixes)
    pulumi.export("ipv4Cidrs", example.ipv4_cidrs)
    ```


    :param str location: The Azure Region where the Service Tags exists. This value is not used to filter the results but for specifying the region to request. For filtering by region use `location_filter` instead.  More information can be found here: [Service Tags URL parameters](https://docs.microsoft.com/rest/api/virtualnetwork/servicetags/list#uri-parameters).
    :param str location_filter: Changes the scope of the service tags. Can be any value that is also valid for `location`. If this field is empty then all address prefixes are considered instead of only location specific ones.
    :param str service: The type of the service for which address prefixes will be fetched. Available service tags can be found here: [Available service tags](https://docs.microsoft.com/azure/virtual-network/service-tags-overview#available-service-tags).
    """
    ...
