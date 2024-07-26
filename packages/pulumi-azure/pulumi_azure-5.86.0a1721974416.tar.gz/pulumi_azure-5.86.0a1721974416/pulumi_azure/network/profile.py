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
from ._inputs import *

__all__ = ['ProfileArgs', 'Profile']

@pulumi.input_type
class ProfileArgs:
    def __init__(__self__, *,
                 container_network_interface: pulumi.Input['ProfileContainerNetworkInterfaceArgs'],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Profile resource.
        :param pulumi.Input['ProfileContainerNetworkInterfaceArgs'] container_network_interface: A `container_network_interface` block as documented below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Network Profile. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        """
        pulumi.set(__self__, "container_network_interface", container_network_interface)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="containerNetworkInterface")
    def container_network_interface(self) -> pulumi.Input['ProfileContainerNetworkInterfaceArgs']:
        """
        A `container_network_interface` block as documented below.
        """
        return pulumi.get(self, "container_network_interface")

    @container_network_interface.setter
    def container_network_interface(self, value: pulumi.Input['ProfileContainerNetworkInterfaceArgs']):
        pulumi.set(self, "container_network_interface", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Network Profile. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ProfileState:
    def __init__(__self__, *,
                 container_network_interface: Optional[pulumi.Input['ProfileContainerNetworkInterfaceArgs']] = None,
                 container_network_interface_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Profile resources.
        :param pulumi.Input['ProfileContainerNetworkInterfaceArgs'] container_network_interface: A `container_network_interface` block as documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] container_network_interface_ids: A list of Container Network Interface IDs.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Network Profile. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        """
        if container_network_interface is not None:
            pulumi.set(__self__, "container_network_interface", container_network_interface)
        if container_network_interface_ids is not None:
            pulumi.set(__self__, "container_network_interface_ids", container_network_interface_ids)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="containerNetworkInterface")
    def container_network_interface(self) -> Optional[pulumi.Input['ProfileContainerNetworkInterfaceArgs']]:
        """
        A `container_network_interface` block as documented below.
        """
        return pulumi.get(self, "container_network_interface")

    @container_network_interface.setter
    def container_network_interface(self, value: Optional[pulumi.Input['ProfileContainerNetworkInterfaceArgs']]):
        pulumi.set(self, "container_network_interface", value)

    @property
    @pulumi.getter(name="containerNetworkInterfaceIds")
    def container_network_interface_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of Container Network Interface IDs.
        """
        return pulumi.get(self, "container_network_interface_ids")

    @container_network_interface_ids.setter
    def container_network_interface_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "container_network_interface_ids", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Network Profile. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Profile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_network_interface: Optional[pulumi.Input[Union['ProfileContainerNetworkInterfaceArgs', 'ProfileContainerNetworkInterfaceArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Network Profile.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="examplegroup",
            location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("example",
            name="examplevnet",
            location=example.location,
            resource_group_name=example.name,
            address_spaces=["10.1.0.0/16"])
        example_subnet = azure.network.Subnet("example",
            name="examplesubnet",
            resource_group_name=example.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.1.0.0/24"],
            delegations=[{
                "name": "delegation",
                "service_delegation": {
                    "name": "Microsoft.ContainerInstance/containerGroups",
                    "actions": ["Microsoft.Network/virtualNetworks/subnets/action"],
                },
            }])
        example_profile = azure.network.Profile("example",
            name="examplenetprofile",
            location=example.location,
            resource_group_name=example.name,
            container_network_interface={
                "name": "examplecnic",
                "ip_configurations": [{
                    "name": "exampleipconfig",
                    "subnet_id": example_subnet.id,
                }],
            })
        ```

        ## Import

        Network Profile can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:network/profile:Profile example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/networkProfiles/examplenetprofile
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ProfileContainerNetworkInterfaceArgs', 'ProfileContainerNetworkInterfaceArgsDict']] container_network_interface: A `container_network_interface` block as documented below.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Network Profile. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Network Profile.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="examplegroup",
            location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("example",
            name="examplevnet",
            location=example.location,
            resource_group_name=example.name,
            address_spaces=["10.1.0.0/16"])
        example_subnet = azure.network.Subnet("example",
            name="examplesubnet",
            resource_group_name=example.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.1.0.0/24"],
            delegations=[{
                "name": "delegation",
                "service_delegation": {
                    "name": "Microsoft.ContainerInstance/containerGroups",
                    "actions": ["Microsoft.Network/virtualNetworks/subnets/action"],
                },
            }])
        example_profile = azure.network.Profile("example",
            name="examplenetprofile",
            location=example.location,
            resource_group_name=example.name,
            container_network_interface={
                "name": "examplecnic",
                "ip_configurations": [{
                    "name": "exampleipconfig",
                    "subnet_id": example_subnet.id,
                }],
            })
        ```

        ## Import

        Network Profile can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:network/profile:Profile example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/networkProfiles/examplenetprofile
        ```

        :param str resource_name: The name of the resource.
        :param ProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_network_interface: Optional[pulumi.Input[Union['ProfileContainerNetworkInterfaceArgs', 'ProfileContainerNetworkInterfaceArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProfileArgs.__new__(ProfileArgs)

            if container_network_interface is None and not opts.urn:
                raise TypeError("Missing required property 'container_network_interface'")
            __props__.__dict__["container_network_interface"] = container_network_interface
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["container_network_interface_ids"] = None
        super(Profile, __self__).__init__(
            'azure:network/profile:Profile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            container_network_interface: Optional[pulumi.Input[Union['ProfileContainerNetworkInterfaceArgs', 'ProfileContainerNetworkInterfaceArgsDict']]] = None,
            container_network_interface_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Profile':
        """
        Get an existing Profile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ProfileContainerNetworkInterfaceArgs', 'ProfileContainerNetworkInterfaceArgsDict']] container_network_interface: A `container_network_interface` block as documented below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] container_network_interface_ids: A list of Container Network Interface IDs.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Network Profile. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags assigned to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProfileState.__new__(_ProfileState)

        __props__.__dict__["container_network_interface"] = container_network_interface
        __props__.__dict__["container_network_interface_ids"] = container_network_interface_ids
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["tags"] = tags
        return Profile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerNetworkInterface")
    def container_network_interface(self) -> pulumi.Output['outputs.ProfileContainerNetworkInterface']:
        """
        A `container_network_interface` block as documented below.
        """
        return pulumi.get(self, "container_network_interface")

    @property
    @pulumi.getter(name="containerNetworkInterfaceIds")
    def container_network_interface_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of Container Network Interface IDs.
        """
        return pulumi.get(self, "container_network_interface_ids")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Network Profile. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")

