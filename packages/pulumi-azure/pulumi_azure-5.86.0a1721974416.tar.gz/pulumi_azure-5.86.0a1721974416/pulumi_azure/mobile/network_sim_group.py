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

__all__ = ['NetworkSimGroupArgs', 'NetworkSimGroup']

@pulumi.input_type
class NetworkSimGroupArgs:
    def __init__(__self__, *,
                 mobile_network_id: pulumi.Input[str],
                 encryption_key_url: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['NetworkSimGroupIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkSimGroup resource.
        :param pulumi.Input[str] mobile_network_id: The ID of Mobile Network which the Mobile Network Sim Group belongs to. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] encryption_key_url: A key to encrypt the SIM data that belongs to this SIM group.
        :param pulumi.Input['NetworkSimGroupIdentityArgs'] identity: An `identity` block as defined below.
               
               > **NOTE:** A `UserAssigned` identity must be specified when `encryption_key_url` is specified.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Mobile Network Sim Groups should exist. Changing this forces a new Mobile Network Sim Group to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Mobile Network Sim Groups. Changing this forces a new Mobile Network Sim Group to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Mobile Network Sim Groups.
        """
        pulumi.set(__self__, "mobile_network_id", mobile_network_id)
        if encryption_key_url is not None:
            pulumi.set(__self__, "encryption_key_url", encryption_key_url)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="mobileNetworkId")
    def mobile_network_id(self) -> pulumi.Input[str]:
        """
        The ID of Mobile Network which the Mobile Network Sim Group belongs to. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "mobile_network_id")

    @mobile_network_id.setter
    def mobile_network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "mobile_network_id", value)

    @property
    @pulumi.getter(name="encryptionKeyUrl")
    def encryption_key_url(self) -> Optional[pulumi.Input[str]]:
        """
        A key to encrypt the SIM data that belongs to this SIM group.
        """
        return pulumi.get(self, "encryption_key_url")

    @encryption_key_url.setter
    def encryption_key_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_key_url", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['NetworkSimGroupIdentityArgs']]:
        """
        An `identity` block as defined below.

        > **NOTE:** A `UserAssigned` identity must be specified when `encryption_key_url` is specified.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['NetworkSimGroupIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Mobile Network Sim Groups should exist. Changing this forces a new Mobile Network Sim Group to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name which should be used for this Mobile Network Sim Groups. Changing this forces a new Mobile Network Sim Group to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Mobile Network Sim Groups.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _NetworkSimGroupState:
    def __init__(__self__, *,
                 encryption_key_url: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['NetworkSimGroupIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering NetworkSimGroup resources.
        :param pulumi.Input[str] encryption_key_url: A key to encrypt the SIM data that belongs to this SIM group.
        :param pulumi.Input['NetworkSimGroupIdentityArgs'] identity: An `identity` block as defined below.
               
               > **NOTE:** A `UserAssigned` identity must be specified when `encryption_key_url` is specified.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Mobile Network Sim Groups should exist. Changing this forces a new Mobile Network Sim Group to be created.
        :param pulumi.Input[str] mobile_network_id: The ID of Mobile Network which the Mobile Network Sim Group belongs to. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Mobile Network Sim Groups. Changing this forces a new Mobile Network Sim Group to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Mobile Network Sim Groups.
        """
        if encryption_key_url is not None:
            pulumi.set(__self__, "encryption_key_url", encryption_key_url)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mobile_network_id is not None:
            pulumi.set(__self__, "mobile_network_id", mobile_network_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="encryptionKeyUrl")
    def encryption_key_url(self) -> Optional[pulumi.Input[str]]:
        """
        A key to encrypt the SIM data that belongs to this SIM group.
        """
        return pulumi.get(self, "encryption_key_url")

    @encryption_key_url.setter
    def encryption_key_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_key_url", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['NetworkSimGroupIdentityArgs']]:
        """
        An `identity` block as defined below.

        > **NOTE:** A `UserAssigned` identity must be specified when `encryption_key_url` is specified.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['NetworkSimGroupIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Mobile Network Sim Groups should exist. Changing this forces a new Mobile Network Sim Group to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mobileNetworkId")
    def mobile_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of Mobile Network which the Mobile Network Sim Group belongs to. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "mobile_network_id")

    @mobile_network_id.setter
    def mobile_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mobile_network_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name which should be used for this Mobile Network Sim Groups. Changing this forces a new Mobile Network Sim Group to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Mobile Network Sim Groups.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class NetworkSimGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_key_url: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['NetworkSimGroupIdentityArgs', 'NetworkSimGroupIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Mobile Network Sim Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_network = azure.mobile.Network("example",
            name="example-mn",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            mobile_country_code="001",
            mobile_network_code="01")
        example = azure.authorization.get_user_assigned_identity(name="name_of_user_assigned_identity",
            resource_group_name="name_of_resource_group")
        example_get_key_vault = azure.keyvault.get_key_vault(name="example-kv",
            resource_group_name="some-resource-group")
        example_get_key = azure.keyvault.get_key(name="example-key",
            key_vault_id=example_get_key_vault.id)
        example_network_sim_group = azure.mobile.NetworkSimGroup("example",
            name="example-mnsg",
            location=example_resource_group.location,
            mobile_network_id=example_network.id,
            encryption_key_url=example_get_key.id,
            identity={
                "type": "SystemAssigned, UserAssigned",
                "identity_ids": [example.id],
            },
            tags={
                "key": "value",
            })
        ```

        ## Import

        Mobile Network Sim Groups can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:mobile/networkSimGroup:NetworkSimGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.MobileNetwork/simGroups/simGroup1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] encryption_key_url: A key to encrypt the SIM data that belongs to this SIM group.
        :param pulumi.Input[Union['NetworkSimGroupIdentityArgs', 'NetworkSimGroupIdentityArgsDict']] identity: An `identity` block as defined below.
               
               > **NOTE:** A `UserAssigned` identity must be specified when `encryption_key_url` is specified.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Mobile Network Sim Groups should exist. Changing this forces a new Mobile Network Sim Group to be created.
        :param pulumi.Input[str] mobile_network_id: The ID of Mobile Network which the Mobile Network Sim Group belongs to. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Mobile Network Sim Groups. Changing this forces a new Mobile Network Sim Group to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Mobile Network Sim Groups.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkSimGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Mobile Network Sim Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_network = azure.mobile.Network("example",
            name="example-mn",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            mobile_country_code="001",
            mobile_network_code="01")
        example = azure.authorization.get_user_assigned_identity(name="name_of_user_assigned_identity",
            resource_group_name="name_of_resource_group")
        example_get_key_vault = azure.keyvault.get_key_vault(name="example-kv",
            resource_group_name="some-resource-group")
        example_get_key = azure.keyvault.get_key(name="example-key",
            key_vault_id=example_get_key_vault.id)
        example_network_sim_group = azure.mobile.NetworkSimGroup("example",
            name="example-mnsg",
            location=example_resource_group.location,
            mobile_network_id=example_network.id,
            encryption_key_url=example_get_key.id,
            identity={
                "type": "SystemAssigned, UserAssigned",
                "identity_ids": [example.id],
            },
            tags={
                "key": "value",
            })
        ```

        ## Import

        Mobile Network Sim Groups can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:mobile/networkSimGroup:NetworkSimGroup example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resourceGroup1/providers/Microsoft.MobileNetwork/simGroups/simGroup1
        ```

        :param str resource_name: The name of the resource.
        :param NetworkSimGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkSimGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_key_url: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['NetworkSimGroupIdentityArgs', 'NetworkSimGroupIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkSimGroupArgs.__new__(NetworkSimGroupArgs)

            __props__.__dict__["encryption_key_url"] = encryption_key_url
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if mobile_network_id is None and not opts.urn:
                raise TypeError("Missing required property 'mobile_network_id'")
            __props__.__dict__["mobile_network_id"] = mobile_network_id
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
        super(NetworkSimGroup, __self__).__init__(
            'azure:mobile/networkSimGroup:NetworkSimGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            encryption_key_url: Optional[pulumi.Input[str]] = None,
            identity: Optional[pulumi.Input[Union['NetworkSimGroupIdentityArgs', 'NetworkSimGroupIdentityArgsDict']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            mobile_network_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'NetworkSimGroup':
        """
        Get an existing NetworkSimGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] encryption_key_url: A key to encrypt the SIM data that belongs to this SIM group.
        :param pulumi.Input[Union['NetworkSimGroupIdentityArgs', 'NetworkSimGroupIdentityArgsDict']] identity: An `identity` block as defined below.
               
               > **NOTE:** A `UserAssigned` identity must be specified when `encryption_key_url` is specified.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Mobile Network Sim Groups should exist. Changing this forces a new Mobile Network Sim Group to be created.
        :param pulumi.Input[str] mobile_network_id: The ID of Mobile Network which the Mobile Network Sim Group belongs to. Changing this forces a new Mobile Network Slice to be created.
        :param pulumi.Input[str] name: Specifies the name which should be used for this Mobile Network Sim Groups. Changing this forces a new Mobile Network Sim Group to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Mobile Network Sim Groups.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkSimGroupState.__new__(_NetworkSimGroupState)

        __props__.__dict__["encryption_key_url"] = encryption_key_url
        __props__.__dict__["identity"] = identity
        __props__.__dict__["location"] = location
        __props__.__dict__["mobile_network_id"] = mobile_network_id
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        return NetworkSimGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="encryptionKeyUrl")
    def encryption_key_url(self) -> pulumi.Output[Optional[str]]:
        """
        A key to encrypt the SIM data that belongs to this SIM group.
        """
        return pulumi.get(self, "encryption_key_url")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.NetworkSimGroupIdentity']]:
        """
        An `identity` block as defined below.

        > **NOTE:** A `UserAssigned` identity must be specified when `encryption_key_url` is specified.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region where the Mobile Network Sim Groups should exist. Changing this forces a new Mobile Network Sim Group to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mobileNetworkId")
    def mobile_network_id(self) -> pulumi.Output[str]:
        """
        The ID of Mobile Network which the Mobile Network Sim Group belongs to. Changing this forces a new Mobile Network Slice to be created.
        """
        return pulumi.get(self, "mobile_network_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name which should be used for this Mobile Network Sim Groups. Changing this forces a new Mobile Network Sim Group to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Mobile Network Sim Groups.
        """
        return pulumi.get(self, "tags")

