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
    'GetNetworkSimGroupResult',
    'AwaitableGetNetworkSimGroupResult',
    'get_network_sim_group',
    'get_network_sim_group_output',
]

@pulumi.output_type
class GetNetworkSimGroupResult:
    """
    A collection of values returned by getNetworkSimGroup.
    """
    def __init__(__self__, encryption_key_url=None, id=None, identities=None, location=None, mobile_network_id=None, name=None, tags=None):
        if encryption_key_url and not isinstance(encryption_key_url, str):
            raise TypeError("Expected argument 'encryption_key_url' to be a str")
        pulumi.set(__self__, "encryption_key_url", encryption_key_url)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identities and not isinstance(identities, list):
            raise TypeError("Expected argument 'identities' to be a list")
        pulumi.set(__self__, "identities", identities)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mobile_network_id and not isinstance(mobile_network_id, str):
            raise TypeError("Expected argument 'mobile_network_id' to be a str")
        pulumi.set(__self__, "mobile_network_id", mobile_network_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="encryptionKeyUrl")
    def encryption_key_url(self) -> str:
        """
        A key to encrypt the SIM data that belongs to this SIM group.
        """
        return pulumi.get(self, "encryption_key_url")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identities(self) -> Sequence['outputs.GetNetworkSimGroupIdentityResult']:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region where the Mobile Network Sim Groups should exist.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mobileNetworkId")
    def mobile_network_id(self) -> str:
        return pulumi.get(self, "mobile_network_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags which should be assigned to the Mobile Network Sim Groups.
        """
        return pulumi.get(self, "tags")


class AwaitableGetNetworkSimGroupResult(GetNetworkSimGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkSimGroupResult(
            encryption_key_url=self.encryption_key_url,
            id=self.id,
            identities=self.identities,
            location=self.location,
            mobile_network_id=self.mobile_network_id,
            name=self.name,
            tags=self.tags)


def get_network_sim_group(mobile_network_id: Optional[str] = None,
                          name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkSimGroupResult:
    """
    Get information about a Mobile Network Sim Group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.mobile.get_network(name="example-mn",
        resource_group_name=example_azurerm_resource_group["name"])
    example_get_network_sim_group = azure.mobile.get_network_sim_group(name="example-mnsg",
        mobile_network_id=example.id)
    ```


    :param str mobile_network_id: The ID of Mobile Network which the Mobile Network Sim Group belongs to.
    :param str name: Specifies the name which should be used for this Mobile Network Sim Groups.
    """
    __args__ = dict()
    __args__['mobileNetworkId'] = mobile_network_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:mobile/getNetworkSimGroup:getNetworkSimGroup', __args__, opts=opts, typ=GetNetworkSimGroupResult).value

    return AwaitableGetNetworkSimGroupResult(
        encryption_key_url=pulumi.get(__ret__, 'encryption_key_url'),
        id=pulumi.get(__ret__, 'id'),
        identities=pulumi.get(__ret__, 'identities'),
        location=pulumi.get(__ret__, 'location'),
        mobile_network_id=pulumi.get(__ret__, 'mobile_network_id'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_network_sim_group)
def get_network_sim_group_output(mobile_network_id: Optional[pulumi.Input[str]] = None,
                                 name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkSimGroupResult]:
    """
    Get information about a Mobile Network Sim Group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.mobile.get_network(name="example-mn",
        resource_group_name=example_azurerm_resource_group["name"])
    example_get_network_sim_group = azure.mobile.get_network_sim_group(name="example-mnsg",
        mobile_network_id=example.id)
    ```


    :param str mobile_network_id: The ID of Mobile Network which the Mobile Network Sim Group belongs to.
    :param str name: Specifies the name which should be used for this Mobile Network Sim Groups.
    """
    ...
