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
from . import outputs

__all__ = [
    'GetEnvironmentV3Result',
    'AwaitableGetEnvironmentV3Result',
    'get_environment_v3',
    'get_environment_v3_output',
]

@pulumi.output_type
class GetEnvironmentV3Result:
    """
    A collection of values returned by getEnvironmentV3.
    """
    def __init__(__self__, allow_new_private_endpoint_connections=None, cluster_settings=None, dedicated_host_count=None, dns_suffix=None, external_inbound_ip_addresses=None, id=None, inbound_network_dependencies=None, internal_inbound_ip_addresses=None, internal_load_balancing_mode=None, ip_ssl_address_count=None, linux_outbound_ip_addresses=None, location=None, name=None, pricing_tier=None, remote_debugging_enabled=None, resource_group_name=None, subnet_id=None, tags=None, windows_outbound_ip_addresses=None, zone_redundant=None):
        if allow_new_private_endpoint_connections and not isinstance(allow_new_private_endpoint_connections, bool):
            raise TypeError("Expected argument 'allow_new_private_endpoint_connections' to be a bool")
        pulumi.set(__self__, "allow_new_private_endpoint_connections", allow_new_private_endpoint_connections)
        if cluster_settings and not isinstance(cluster_settings, list):
            raise TypeError("Expected argument 'cluster_settings' to be a list")
        pulumi.set(__self__, "cluster_settings", cluster_settings)
        if dedicated_host_count and not isinstance(dedicated_host_count, int):
            raise TypeError("Expected argument 'dedicated_host_count' to be a int")
        pulumi.set(__self__, "dedicated_host_count", dedicated_host_count)
        if dns_suffix and not isinstance(dns_suffix, str):
            raise TypeError("Expected argument 'dns_suffix' to be a str")
        pulumi.set(__self__, "dns_suffix", dns_suffix)
        if external_inbound_ip_addresses and not isinstance(external_inbound_ip_addresses, list):
            raise TypeError("Expected argument 'external_inbound_ip_addresses' to be a list")
        pulumi.set(__self__, "external_inbound_ip_addresses", external_inbound_ip_addresses)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inbound_network_dependencies and not isinstance(inbound_network_dependencies, list):
            raise TypeError("Expected argument 'inbound_network_dependencies' to be a list")
        pulumi.set(__self__, "inbound_network_dependencies", inbound_network_dependencies)
        if internal_inbound_ip_addresses and not isinstance(internal_inbound_ip_addresses, list):
            raise TypeError("Expected argument 'internal_inbound_ip_addresses' to be a list")
        pulumi.set(__self__, "internal_inbound_ip_addresses", internal_inbound_ip_addresses)
        if internal_load_balancing_mode and not isinstance(internal_load_balancing_mode, str):
            raise TypeError("Expected argument 'internal_load_balancing_mode' to be a str")
        pulumi.set(__self__, "internal_load_balancing_mode", internal_load_balancing_mode)
        if ip_ssl_address_count and not isinstance(ip_ssl_address_count, int):
            raise TypeError("Expected argument 'ip_ssl_address_count' to be a int")
        pulumi.set(__self__, "ip_ssl_address_count", ip_ssl_address_count)
        if linux_outbound_ip_addresses and not isinstance(linux_outbound_ip_addresses, list):
            raise TypeError("Expected argument 'linux_outbound_ip_addresses' to be a list")
        pulumi.set(__self__, "linux_outbound_ip_addresses", linux_outbound_ip_addresses)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pricing_tier and not isinstance(pricing_tier, str):
            raise TypeError("Expected argument 'pricing_tier' to be a str")
        pulumi.set(__self__, "pricing_tier", pricing_tier)
        if remote_debugging_enabled and not isinstance(remote_debugging_enabled, bool):
            raise TypeError("Expected argument 'remote_debugging_enabled' to be a bool")
        pulumi.set(__self__, "remote_debugging_enabled", remote_debugging_enabled)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if windows_outbound_ip_addresses and not isinstance(windows_outbound_ip_addresses, list):
            raise TypeError("Expected argument 'windows_outbound_ip_addresses' to be a list")
        pulumi.set(__self__, "windows_outbound_ip_addresses", windows_outbound_ip_addresses)
        if zone_redundant and not isinstance(zone_redundant, bool):
            raise TypeError("Expected argument 'zone_redundant' to be a bool")
        pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="allowNewPrivateEndpointConnections")
    def allow_new_private_endpoint_connections(self) -> bool:
        """
        Are new Private Endpoint Connections allowed.
        """
        return pulumi.get(self, "allow_new_private_endpoint_connections")

    @property
    @pulumi.getter(name="clusterSettings")
    def cluster_settings(self) -> Sequence['outputs.GetEnvironmentV3ClusterSettingResult']:
        """
        A `cluster_setting` block as defined below.
        """
        return pulumi.get(self, "cluster_settings")

    @property
    @pulumi.getter(name="dedicatedHostCount")
    def dedicated_host_count(self) -> int:
        """
        The number of Dedicated Hosts used by this ASEv3.
        """
        return pulumi.get(self, "dedicated_host_count")

    @property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> str:
        """
        the DNS suffix for this App Service Environment V3.
        """
        return pulumi.get(self, "dns_suffix")

    @property
    @pulumi.getter(name="externalInboundIpAddresses")
    def external_inbound_ip_addresses(self) -> Sequence[str]:
        """
        The external inbound IP addresses of the App Service Environment V3.
        """
        return pulumi.get(self, "external_inbound_ip_addresses")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inboundNetworkDependencies")
    def inbound_network_dependencies(self) -> Sequence['outputs.GetEnvironmentV3InboundNetworkDependencyResult']:
        """
        An Inbound Network Dependencies block as defined below.
        """
        return pulumi.get(self, "inbound_network_dependencies")

    @property
    @pulumi.getter(name="internalInboundIpAddresses")
    def internal_inbound_ip_addresses(self) -> Sequence[str]:
        """
        The internal inbound IP addresses of the App Service Environment V3.
        """
        return pulumi.get(self, "internal_inbound_ip_addresses")

    @property
    @pulumi.getter(name="internalLoadBalancingMode")
    def internal_load_balancing_mode(self) -> str:
        """
        The Internal Load Balancing Mode of this ASEv3.
        """
        return pulumi.get(self, "internal_load_balancing_mode")

    @property
    @pulumi.getter(name="ipSslAddressCount")
    def ip_ssl_address_count(self) -> int:
        """
        The number of IP SSL addresses reserved for the App Service Environment V3.
        """
        return pulumi.get(self, "ip_ssl_address_count")

    @property
    @pulumi.getter(name="linuxOutboundIpAddresses")
    def linux_outbound_ip_addresses(self) -> Sequence[str]:
        """
        The list of Outbound IP Addresses of Linux based Apps in this App Service Environment V3.
        """
        return pulumi.get(self, "linux_outbound_ip_addresses")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location where the App Service Environment exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Cluster Setting.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pricingTier")
    def pricing_tier(self) -> str:
        """
        Pricing tier for the front end instances.
        """
        return pulumi.get(self, "pricing_tier")

    @property
    @pulumi.getter(name="remoteDebuggingEnabled")
    def remote_debugging_enabled(self) -> bool:
        return pulumi.get(self, "remote_debugging_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The ID of the v3 App Service Environment Subnet.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the v3 App Service Environment.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="windowsOutboundIpAddresses")
    def windows_outbound_ip_addresses(self) -> Sequence[str]:
        """
        Outbound addresses of Windows based Apps in this App Service Environment V3.
        """
        return pulumi.get(self, "windows_outbound_ip_addresses")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> bool:
        return pulumi.get(self, "zone_redundant")


class AwaitableGetEnvironmentV3Result(GetEnvironmentV3Result):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentV3Result(
            allow_new_private_endpoint_connections=self.allow_new_private_endpoint_connections,
            cluster_settings=self.cluster_settings,
            dedicated_host_count=self.dedicated_host_count,
            dns_suffix=self.dns_suffix,
            external_inbound_ip_addresses=self.external_inbound_ip_addresses,
            id=self.id,
            inbound_network_dependencies=self.inbound_network_dependencies,
            internal_inbound_ip_addresses=self.internal_inbound_ip_addresses,
            internal_load_balancing_mode=self.internal_load_balancing_mode,
            ip_ssl_address_count=self.ip_ssl_address_count,
            linux_outbound_ip_addresses=self.linux_outbound_ip_addresses,
            location=self.location,
            name=self.name,
            pricing_tier=self.pricing_tier,
            remote_debugging_enabled=self.remote_debugging_enabled,
            resource_group_name=self.resource_group_name,
            subnet_id=self.subnet_id,
            tags=self.tags,
            windows_outbound_ip_addresses=self.windows_outbound_ip_addresses,
            zone_redundant=self.zone_redundant)


def get_environment_v3(name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentV3Result:
    """
    Use this data source to access information about an existing 3rd Generation (v3) App Service Environment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_environment_v3(name="example-ASE",
        resource_group_name="example-resource-group")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this v3 App Service Environment.
    :param str resource_group_name: The name of the Resource Group where the v3 App Service Environment exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:appservice/getEnvironmentV3:getEnvironmentV3', __args__, opts=opts, typ=GetEnvironmentV3Result).value

    return AwaitableGetEnvironmentV3Result(
        allow_new_private_endpoint_connections=pulumi.get(__ret__, 'allow_new_private_endpoint_connections'),
        cluster_settings=pulumi.get(__ret__, 'cluster_settings'),
        dedicated_host_count=pulumi.get(__ret__, 'dedicated_host_count'),
        dns_suffix=pulumi.get(__ret__, 'dns_suffix'),
        external_inbound_ip_addresses=pulumi.get(__ret__, 'external_inbound_ip_addresses'),
        id=pulumi.get(__ret__, 'id'),
        inbound_network_dependencies=pulumi.get(__ret__, 'inbound_network_dependencies'),
        internal_inbound_ip_addresses=pulumi.get(__ret__, 'internal_inbound_ip_addresses'),
        internal_load_balancing_mode=pulumi.get(__ret__, 'internal_load_balancing_mode'),
        ip_ssl_address_count=pulumi.get(__ret__, 'ip_ssl_address_count'),
        linux_outbound_ip_addresses=pulumi.get(__ret__, 'linux_outbound_ip_addresses'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        pricing_tier=pulumi.get(__ret__, 'pricing_tier'),
        remote_debugging_enabled=pulumi.get(__ret__, 'remote_debugging_enabled'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        tags=pulumi.get(__ret__, 'tags'),
        windows_outbound_ip_addresses=pulumi.get(__ret__, 'windows_outbound_ip_addresses'),
        zone_redundant=pulumi.get(__ret__, 'zone_redundant'))


@_utilities.lift_output_func(get_environment_v3)
def get_environment_v3_output(name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvironmentV3Result]:
    """
    Use this data source to access information about an existing 3rd Generation (v3) App Service Environment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_environment_v3(name="example-ASE",
        resource_group_name="example-resource-group")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this v3 App Service Environment.
    :param str resource_group_name: The name of the Resource Group where the v3 App Service Environment exists.
    """
    ...
