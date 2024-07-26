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

__all__ = ['CapabilityArgs', 'Capability']

@pulumi.input_type
class CapabilityArgs:
    def __init__(__self__, *,
                 capability_type: pulumi.Input[str],
                 chaos_studio_target_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a Capability resource.
        :param pulumi.Input[str] capability_type: The capability that should be applied to the Chaos Studio Target. For supported values please see this Chaos Studio [Fault Library](https://learn.microsoft.com/azure/chaos-studio/chaos-studio-fault-library). Changing this forces a new Chaos Studio Capability to be created.
        :param pulumi.Input[str] chaos_studio_target_id: The Chaos Studio Target that the capability should be applied to. Changing this forces a new Chaos Studio Capability to be created.
        """
        pulumi.set(__self__, "capability_type", capability_type)
        pulumi.set(__self__, "chaos_studio_target_id", chaos_studio_target_id)

    @property
    @pulumi.getter(name="capabilityType")
    def capability_type(self) -> pulumi.Input[str]:
        """
        The capability that should be applied to the Chaos Studio Target. For supported values please see this Chaos Studio [Fault Library](https://learn.microsoft.com/azure/chaos-studio/chaos-studio-fault-library). Changing this forces a new Chaos Studio Capability to be created.
        """
        return pulumi.get(self, "capability_type")

    @capability_type.setter
    def capability_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "capability_type", value)

    @property
    @pulumi.getter(name="chaosStudioTargetId")
    def chaos_studio_target_id(self) -> pulumi.Input[str]:
        """
        The Chaos Studio Target that the capability should be applied to. Changing this forces a new Chaos Studio Capability to be created.
        """
        return pulumi.get(self, "chaos_studio_target_id")

    @chaos_studio_target_id.setter
    def chaos_studio_target_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "chaos_studio_target_id", value)


@pulumi.input_type
class _CapabilityState:
    def __init__(__self__, *,
                 capability_type: Optional[pulumi.Input[str]] = None,
                 capability_urn: Optional[pulumi.Input[str]] = None,
                 chaos_studio_target_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Capability resources.
        :param pulumi.Input[str] capability_type: The capability that should be applied to the Chaos Studio Target. For supported values please see this Chaos Studio [Fault Library](https://learn.microsoft.com/azure/chaos-studio/chaos-studio-fault-library). Changing this forces a new Chaos Studio Capability to be created.
        :param pulumi.Input[str] capability_urn: The Unique Resource Name of the Capability.
        :param pulumi.Input[str] chaos_studio_target_id: The Chaos Studio Target that the capability should be applied to. Changing this forces a new Chaos Studio Capability to be created.
        """
        if capability_type is not None:
            pulumi.set(__self__, "capability_type", capability_type)
        if capability_urn is not None:
            pulumi.set(__self__, "capability_urn", capability_urn)
        if chaos_studio_target_id is not None:
            pulumi.set(__self__, "chaos_studio_target_id", chaos_studio_target_id)

    @property
    @pulumi.getter(name="capabilityType")
    def capability_type(self) -> Optional[pulumi.Input[str]]:
        """
        The capability that should be applied to the Chaos Studio Target. For supported values please see this Chaos Studio [Fault Library](https://learn.microsoft.com/azure/chaos-studio/chaos-studio-fault-library). Changing this forces a new Chaos Studio Capability to be created.
        """
        return pulumi.get(self, "capability_type")

    @capability_type.setter
    def capability_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capability_type", value)

    @property
    @pulumi.getter(name="capabilityUrn")
    def capability_urn(self) -> Optional[pulumi.Input[str]]:
        """
        The Unique Resource Name of the Capability.
        """
        return pulumi.get(self, "capability_urn")

    @capability_urn.setter
    def capability_urn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capability_urn", value)

    @property
    @pulumi.getter(name="chaosStudioTargetId")
    def chaos_studio_target_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Chaos Studio Target that the capability should be applied to. Changing this forces a new Chaos Studio Capability to be created.
        """
        return pulumi.get(self, "chaos_studio_target_id")

    @chaos_studio_target_id.setter
    def chaos_studio_target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "chaos_studio_target_id", value)


class Capability(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capability_type: Optional[pulumi.Input[str]] = None,
                 chaos_studio_target_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Chaos Studio Capability.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example = azure.containerservice.KubernetesCluster("example",
            name="example",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            dns_prefix="acctestaksexample",
            default_node_pool={
                "name": "example-value",
                "node_count": "example-value",
                "vm_size": "example-value",
            },
            identity={
                "type": "example-value",
            })
        example_target = azure.chaosstudio.Target("example",
            location=example_resource_group.location,
            target_resource_id=example.id,
            target_type="example-value")
        example_capability = azure.chaosstudio.Capability("example",
            capability_type="example-value",
            chaos_studio_target_id=example_target.id)
        ```

        ## Import

        An existing Chaos Studio Target can be imported into Terraform using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:chaosstudio/capability:Capability example /{scope}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}
        ```

        * Where `{scope}` is the ID of the Azure Resource under which the Chaos Studio Target exists. For example `/subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/some-resource-group`.

        * Where `{targetName}` is the name of the Target. For example `targetValue`.

        * Where `{capabilityName}` is the name of the Capability. For example `capabilityName`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capability_type: The capability that should be applied to the Chaos Studio Target. For supported values please see this Chaos Studio [Fault Library](https://learn.microsoft.com/azure/chaos-studio/chaos-studio-fault-library). Changing this forces a new Chaos Studio Capability to be created.
        :param pulumi.Input[str] chaos_studio_target_id: The Chaos Studio Target that the capability should be applied to. Changing this forces a new Chaos Studio Capability to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CapabilityArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Chaos Studio Capability.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example = azure.containerservice.KubernetesCluster("example",
            name="example",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            dns_prefix="acctestaksexample",
            default_node_pool={
                "name": "example-value",
                "node_count": "example-value",
                "vm_size": "example-value",
            },
            identity={
                "type": "example-value",
            })
        example_target = azure.chaosstudio.Target("example",
            location=example_resource_group.location,
            target_resource_id=example.id,
            target_type="example-value")
        example_capability = azure.chaosstudio.Capability("example",
            capability_type="example-value",
            chaos_studio_target_id=example_target.id)
        ```

        ## Import

        An existing Chaos Studio Target can be imported into Terraform using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:chaosstudio/capability:Capability example /{scope}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}
        ```

        * Where `{scope}` is the ID of the Azure Resource under which the Chaos Studio Target exists. For example `/subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/some-resource-group`.

        * Where `{targetName}` is the name of the Target. For example `targetValue`.

        * Where `{capabilityName}` is the name of the Capability. For example `capabilityName`.

        :param str resource_name: The name of the resource.
        :param CapabilityArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CapabilityArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capability_type: Optional[pulumi.Input[str]] = None,
                 chaos_studio_target_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CapabilityArgs.__new__(CapabilityArgs)

            if capability_type is None and not opts.urn:
                raise TypeError("Missing required property 'capability_type'")
            __props__.__dict__["capability_type"] = capability_type
            if chaos_studio_target_id is None and not opts.urn:
                raise TypeError("Missing required property 'chaos_studio_target_id'")
            __props__.__dict__["chaos_studio_target_id"] = chaos_studio_target_id
            __props__.__dict__["capability_urn"] = None
        super(Capability, __self__).__init__(
            'azure:chaosstudio/capability:Capability',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            capability_type: Optional[pulumi.Input[str]] = None,
            capability_urn: Optional[pulumi.Input[str]] = None,
            chaos_studio_target_id: Optional[pulumi.Input[str]] = None) -> 'Capability':
        """
        Get an existing Capability resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capability_type: The capability that should be applied to the Chaos Studio Target. For supported values please see this Chaos Studio [Fault Library](https://learn.microsoft.com/azure/chaos-studio/chaos-studio-fault-library). Changing this forces a new Chaos Studio Capability to be created.
        :param pulumi.Input[str] capability_urn: The Unique Resource Name of the Capability.
        :param pulumi.Input[str] chaos_studio_target_id: The Chaos Studio Target that the capability should be applied to. Changing this forces a new Chaos Studio Capability to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CapabilityState.__new__(_CapabilityState)

        __props__.__dict__["capability_type"] = capability_type
        __props__.__dict__["capability_urn"] = capability_urn
        __props__.__dict__["chaos_studio_target_id"] = chaos_studio_target_id
        return Capability(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="capabilityType")
    def capability_type(self) -> pulumi.Output[str]:
        """
        The capability that should be applied to the Chaos Studio Target. For supported values please see this Chaos Studio [Fault Library](https://learn.microsoft.com/azure/chaos-studio/chaos-studio-fault-library). Changing this forces a new Chaos Studio Capability to be created.
        """
        return pulumi.get(self, "capability_type")

    @property
    @pulumi.getter(name="capabilityUrn")
    def capability_urn(self) -> pulumi.Output[str]:
        """
        The Unique Resource Name of the Capability.
        """
        return pulumi.get(self, "capability_urn")

    @property
    @pulumi.getter(name="chaosStudioTargetId")
    def chaos_studio_target_id(self) -> pulumi.Output[str]:
        """
        The Chaos Studio Target that the capability should be applied to. Changing this forces a new Chaos Studio Capability to be created.
        """
        return pulumi.get(self, "chaos_studio_target_id")

