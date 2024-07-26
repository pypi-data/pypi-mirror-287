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
    'GetNetworkSliceResult',
    'AwaitableGetNetworkSliceResult',
    'get_network_slice',
    'get_network_slice_output',
]

@pulumi.output_type
class GetNetworkSliceResult:
    """
    A collection of values returned by getNetworkSlice.
    """
    def __init__(__self__, description=None, id=None, location=None, mobile_network_id=None, name=None, single_network_slice_selection_assistance_informations=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mobile_network_id and not isinstance(mobile_network_id, str):
            raise TypeError("Expected argument 'mobile_network_id' to be a str")
        pulumi.set(__self__, "mobile_network_id", mobile_network_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if single_network_slice_selection_assistance_informations and not isinstance(single_network_slice_selection_assistance_informations, list):
            raise TypeError("Expected argument 'single_network_slice_selection_assistance_informations' to be a list")
        pulumi.set(__self__, "single_network_slice_selection_assistance_informations", single_network_slice_selection_assistance_informations)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description of this Mobile Network Slice.
        """
        return pulumi.get(self, "description")

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
        The Azure Region where the Mobile Network Slice exists.
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
    @pulumi.getter(name="singleNetworkSliceSelectionAssistanceInformations")
    def single_network_slice_selection_assistance_informations(self) -> Sequence['outputs.GetNetworkSliceSingleNetworkSliceSelectionAssistanceInformationResult']:
        """
        A `single_network_slice_selection_assistance_information` block as defined below. Single-network slice selection assistance information (S-NSSAI).
        """
        return pulumi.get(self, "single_network_slice_selection_assistance_informations")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags which are assigned to the Mobile Network Slice.
        """
        return pulumi.get(self, "tags")


class AwaitableGetNetworkSliceResult(GetNetworkSliceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkSliceResult(
            description=self.description,
            id=self.id,
            location=self.location,
            mobile_network_id=self.mobile_network_id,
            name=self.name,
            single_network_slice_selection_assistance_informations=self.single_network_slice_selection_assistance_informations,
            tags=self.tags)


def get_network_slice(mobile_network_id: Optional[str] = None,
                      name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkSliceResult:
    """
    Get information about a Mobile Network Slice.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.mobile.get_network(name="example-mn",
        resource_group_name="example-rg")
    example_get_network_slice = azure.mobile.get_network_slice(name="example-mns",
        mobile_network_id=test["id"])
    ```


    :param str mobile_network_id: The ID of Mobile Network which the Mobile Network Slice belongs to.
    :param str name: Specifies the name which should be used for this Mobile Network Slice.
    """
    __args__ = dict()
    __args__['mobileNetworkId'] = mobile_network_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:mobile/getNetworkSlice:getNetworkSlice', __args__, opts=opts, typ=GetNetworkSliceResult).value

    return AwaitableGetNetworkSliceResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        mobile_network_id=pulumi.get(__ret__, 'mobile_network_id'),
        name=pulumi.get(__ret__, 'name'),
        single_network_slice_selection_assistance_informations=pulumi.get(__ret__, 'single_network_slice_selection_assistance_informations'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_network_slice)
def get_network_slice_output(mobile_network_id: Optional[pulumi.Input[str]] = None,
                             name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkSliceResult]:
    """
    Get information about a Mobile Network Slice.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.mobile.get_network(name="example-mn",
        resource_group_name="example-rg")
    example_get_network_slice = azure.mobile.get_network_slice(name="example-mns",
        mobile_network_id=test["id"])
    ```


    :param str mobile_network_id: The ID of Mobile Network which the Mobile Network Slice belongs to.
    :param str name: Specifies the name which should be used for this Mobile Network Slice.
    """
    ...
