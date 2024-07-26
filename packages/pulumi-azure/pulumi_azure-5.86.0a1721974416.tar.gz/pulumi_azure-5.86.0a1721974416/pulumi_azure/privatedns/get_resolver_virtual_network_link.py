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
    'GetResolverVirtualNetworkLinkResult',
    'AwaitableGetResolverVirtualNetworkLinkResult',
    'get_resolver_virtual_network_link',
    'get_resolver_virtual_network_link_output',
]

@pulumi.output_type
class GetResolverVirtualNetworkLinkResult:
    """
    A collection of values returned by getResolverVirtualNetworkLink.
    """
    def __init__(__self__, dns_forwarding_ruleset_id=None, id=None, metadata=None, name=None, virtual_network_id=None):
        if dns_forwarding_ruleset_id and not isinstance(dns_forwarding_ruleset_id, str):
            raise TypeError("Expected argument 'dns_forwarding_ruleset_id' to be a str")
        pulumi.set(__self__, "dns_forwarding_ruleset_id", dns_forwarding_ruleset_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if virtual_network_id and not isinstance(virtual_network_id, str):
            raise TypeError("Expected argument 'virtual_network_id' to be a str")
        pulumi.set(__self__, "virtual_network_id", virtual_network_id)

    @property
    @pulumi.getter(name="dnsForwardingRulesetId")
    def dns_forwarding_ruleset_id(self) -> str:
        return pulumi.get(self, "dns_forwarding_ruleset_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, str]:
        """
        The metadata attached to the Private DNS Resolver Virtual Network Link.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="virtualNetworkId")
    def virtual_network_id(self) -> str:
        """
        The ID of the Virtual Network that is linked to the Private DNS Resolver Virtual Network Link.
        """
        return pulumi.get(self, "virtual_network_id")


class AwaitableGetResolverVirtualNetworkLinkResult(GetResolverVirtualNetworkLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResolverVirtualNetworkLinkResult(
            dns_forwarding_ruleset_id=self.dns_forwarding_ruleset_id,
            id=self.id,
            metadata=self.metadata,
            name=self.name,
            virtual_network_id=self.virtual_network_id)


def get_resolver_virtual_network_link(dns_forwarding_ruleset_id: Optional[str] = None,
                                      name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResolverVirtualNetworkLinkResult:
    """
    Gets information about an existing Private DNS Resolver Virtual Network Link.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.privatedns.get_resolver_virtual_network_link(name="example-link",
        dns_forwarding_ruleset_id="example-dns-forwarding-ruleset-id")
    ```


    :param str dns_forwarding_ruleset_id: ID of the Private DNS Resolver DNS Forwarding Ruleset.
    :param str name: Name of the Private DNS Resolver Virtual Network Link.
    """
    __args__ = dict()
    __args__['dnsForwardingRulesetId'] = dns_forwarding_ruleset_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:privatedns/getResolverVirtualNetworkLink:getResolverVirtualNetworkLink', __args__, opts=opts, typ=GetResolverVirtualNetworkLinkResult).value

    return AwaitableGetResolverVirtualNetworkLinkResult(
        dns_forwarding_ruleset_id=pulumi.get(__ret__, 'dns_forwarding_ruleset_id'),
        id=pulumi.get(__ret__, 'id'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        virtual_network_id=pulumi.get(__ret__, 'virtual_network_id'))


@_utilities.lift_output_func(get_resolver_virtual_network_link)
def get_resolver_virtual_network_link_output(dns_forwarding_ruleset_id: Optional[pulumi.Input[str]] = None,
                                             name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResolverVirtualNetworkLinkResult]:
    """
    Gets information about an existing Private DNS Resolver Virtual Network Link.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.privatedns.get_resolver_virtual_network_link(name="example-link",
        dns_forwarding_ruleset_id="example-dns-forwarding-ruleset-id")
    ```


    :param str dns_forwarding_ruleset_id: ID of the Private DNS Resolver DNS Forwarding Ruleset.
    :param str name: Name of the Private DNS Resolver Virtual Network Link.
    """
    ...
