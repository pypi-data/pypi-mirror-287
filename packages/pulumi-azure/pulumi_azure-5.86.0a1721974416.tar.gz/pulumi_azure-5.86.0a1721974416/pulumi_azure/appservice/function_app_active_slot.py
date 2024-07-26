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

__all__ = ['FunctionAppActiveSlotArgs', 'FunctionAppActiveSlot']

@pulumi.input_type
class FunctionAppActiveSlotArgs:
    def __init__(__self__, *,
                 slot_id: pulumi.Input[str],
                 overwrite_network_config: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a FunctionAppActiveSlot resource.
        :param pulumi.Input[str] slot_id: The ID of the Slot to swap with `Production`.
        :param pulumi.Input[bool] overwrite_network_config: The swap action should overwrite the Production slot's network configuration with the configuration from this slot. Defaults to `true`. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "slot_id", slot_id)
        if overwrite_network_config is not None:
            pulumi.set(__self__, "overwrite_network_config", overwrite_network_config)

    @property
    @pulumi.getter(name="slotId")
    def slot_id(self) -> pulumi.Input[str]:
        """
        The ID of the Slot to swap with `Production`.
        """
        return pulumi.get(self, "slot_id")

    @slot_id.setter
    def slot_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "slot_id", value)

    @property
    @pulumi.getter(name="overwriteNetworkConfig")
    def overwrite_network_config(self) -> Optional[pulumi.Input[bool]]:
        """
        The swap action should overwrite the Production slot's network configuration with the configuration from this slot. Defaults to `true`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "overwrite_network_config")

    @overwrite_network_config.setter
    def overwrite_network_config(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "overwrite_network_config", value)


@pulumi.input_type
class _FunctionAppActiveSlotState:
    def __init__(__self__, *,
                 last_successful_swap: Optional[pulumi.Input[str]] = None,
                 overwrite_network_config: Optional[pulumi.Input[bool]] = None,
                 slot_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FunctionAppActiveSlot resources.
        :param pulumi.Input[str] last_successful_swap: The timestamp of the last successful swap with `Production`
        :param pulumi.Input[bool] overwrite_network_config: The swap action should overwrite the Production slot's network configuration with the configuration from this slot. Defaults to `true`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] slot_id: The ID of the Slot to swap with `Production`.
        """
        if last_successful_swap is not None:
            pulumi.set(__self__, "last_successful_swap", last_successful_swap)
        if overwrite_network_config is not None:
            pulumi.set(__self__, "overwrite_network_config", overwrite_network_config)
        if slot_id is not None:
            pulumi.set(__self__, "slot_id", slot_id)

    @property
    @pulumi.getter(name="lastSuccessfulSwap")
    def last_successful_swap(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of the last successful swap with `Production`
        """
        return pulumi.get(self, "last_successful_swap")

    @last_successful_swap.setter
    def last_successful_swap(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_successful_swap", value)

    @property
    @pulumi.getter(name="overwriteNetworkConfig")
    def overwrite_network_config(self) -> Optional[pulumi.Input[bool]]:
        """
        The swap action should overwrite the Production slot's network configuration with the configuration from this slot. Defaults to `true`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "overwrite_network_config")

    @overwrite_network_config.setter
    def overwrite_network_config(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "overwrite_network_config", value)

    @property
    @pulumi.getter(name="slotId")
    def slot_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Slot to swap with `Production`.
        """
        return pulumi.get(self, "slot_id")

    @slot_id.setter
    def slot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slot_id", value)


class FunctionAppActiveSlot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 overwrite_network_config: Optional[pulumi.Input[bool]] = None,
                 slot_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Function App Active Slot.

        ## Example Usage

        ### Windows Function App

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_account = azure.storage.Account("example",
            name="windowsfunctionappsa",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_service_plan = azure.appservice.ServicePlan("example",
            name="example-app-service-plan",
            resource_group_name=example.name,
            location=example.location,
            os_type="Windows",
            sku_name="Y1")
        example_windows_function_app = azure.appservice.WindowsFunctionApp("example",
            name="example-windows-function-app",
            resource_group_name=example.name,
            location=example.location,
            storage_account_name=example_account.name,
            service_plan_id=example_service_plan.id,
            site_config={})
        example_windows_function_app_slot = azure.appservice.WindowsFunctionAppSlot("example",
            name="example-windows-function-app-slot",
            function_app_id=example_windows_function_app.id,
            storage_account_name=example_account.name,
            site_config={})
        example_function_app_active_slot = azure.appservice.FunctionAppActiveSlot("example", slot_id=example_windows_function_app_slot.id)
        ```

        ### Linux Function App

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_account = azure.storage.Account("example",
            name="linuxfunctionappsa",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_service_plan = azure.appservice.ServicePlan("example",
            name="example-app-service-plan",
            resource_group_name=example.name,
            location=example.location,
            os_type="Linux",
            sku_name="Y1")
        example_linux_function_app = azure.appservice.LinuxFunctionApp("example",
            name="example-linux-function-app",
            resource_group_name=example.name,
            location=example.location,
            service_plan_id=example_service_plan.id,
            storage_account_name=example_account.name,
            site_config={})
        example_linux_function_app_slot = azure.appservice.LinuxFunctionAppSlot("example",
            name="example-linux-function-app-slot",
            function_app_id=example_linux_function_app.name,
            storage_account_name=example_account.name,
            site_config={})
        example_function_app_active_slot = azure.appservice.FunctionAppActiveSlot("example", slot_id=example_linux_function_app_slot.id)
        ```

        ## Import

        a Function App Active Slot can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:appservice/functionAppActiveSlot:FunctionAppActiveSlot example "/subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Web/sites/site1"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] overwrite_network_config: The swap action should overwrite the Production slot's network configuration with the configuration from this slot. Defaults to `true`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] slot_id: The ID of the Slot to swap with `Production`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FunctionAppActiveSlotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Function App Active Slot.

        ## Example Usage

        ### Windows Function App

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_account = azure.storage.Account("example",
            name="windowsfunctionappsa",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_service_plan = azure.appservice.ServicePlan("example",
            name="example-app-service-plan",
            resource_group_name=example.name,
            location=example.location,
            os_type="Windows",
            sku_name="Y1")
        example_windows_function_app = azure.appservice.WindowsFunctionApp("example",
            name="example-windows-function-app",
            resource_group_name=example.name,
            location=example.location,
            storage_account_name=example_account.name,
            service_plan_id=example_service_plan.id,
            site_config={})
        example_windows_function_app_slot = azure.appservice.WindowsFunctionAppSlot("example",
            name="example-windows-function-app-slot",
            function_app_id=example_windows_function_app.id,
            storage_account_name=example_account.name,
            site_config={})
        example_function_app_active_slot = azure.appservice.FunctionAppActiveSlot("example", slot_id=example_windows_function_app_slot.id)
        ```

        ### Linux Function App

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_account = azure.storage.Account("example",
            name="linuxfunctionappsa",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_service_plan = azure.appservice.ServicePlan("example",
            name="example-app-service-plan",
            resource_group_name=example.name,
            location=example.location,
            os_type="Linux",
            sku_name="Y1")
        example_linux_function_app = azure.appservice.LinuxFunctionApp("example",
            name="example-linux-function-app",
            resource_group_name=example.name,
            location=example.location,
            service_plan_id=example_service_plan.id,
            storage_account_name=example_account.name,
            site_config={})
        example_linux_function_app_slot = azure.appservice.LinuxFunctionAppSlot("example",
            name="example-linux-function-app-slot",
            function_app_id=example_linux_function_app.name,
            storage_account_name=example_account.name,
            site_config={})
        example_function_app_active_slot = azure.appservice.FunctionAppActiveSlot("example", slot_id=example_linux_function_app_slot.id)
        ```

        ## Import

        a Function App Active Slot can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:appservice/functionAppActiveSlot:FunctionAppActiveSlot example "/subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Web/sites/site1"
        ```

        :param str resource_name: The name of the resource.
        :param FunctionAppActiveSlotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FunctionAppActiveSlotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 overwrite_network_config: Optional[pulumi.Input[bool]] = None,
                 slot_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FunctionAppActiveSlotArgs.__new__(FunctionAppActiveSlotArgs)

            __props__.__dict__["overwrite_network_config"] = overwrite_network_config
            if slot_id is None and not opts.urn:
                raise TypeError("Missing required property 'slot_id'")
            __props__.__dict__["slot_id"] = slot_id
            __props__.__dict__["last_successful_swap"] = None
        super(FunctionAppActiveSlot, __self__).__init__(
            'azure:appservice/functionAppActiveSlot:FunctionAppActiveSlot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            last_successful_swap: Optional[pulumi.Input[str]] = None,
            overwrite_network_config: Optional[pulumi.Input[bool]] = None,
            slot_id: Optional[pulumi.Input[str]] = None) -> 'FunctionAppActiveSlot':
        """
        Get an existing FunctionAppActiveSlot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] last_successful_swap: The timestamp of the last successful swap with `Production`
        :param pulumi.Input[bool] overwrite_network_config: The swap action should overwrite the Production slot's network configuration with the configuration from this slot. Defaults to `true`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] slot_id: The ID of the Slot to swap with `Production`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FunctionAppActiveSlotState.__new__(_FunctionAppActiveSlotState)

        __props__.__dict__["last_successful_swap"] = last_successful_swap
        __props__.__dict__["overwrite_network_config"] = overwrite_network_config
        __props__.__dict__["slot_id"] = slot_id
        return FunctionAppActiveSlot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="lastSuccessfulSwap")
    def last_successful_swap(self) -> pulumi.Output[str]:
        """
        The timestamp of the last successful swap with `Production`
        """
        return pulumi.get(self, "last_successful_swap")

    @property
    @pulumi.getter(name="overwriteNetworkConfig")
    def overwrite_network_config(self) -> pulumi.Output[Optional[bool]]:
        """
        The swap action should overwrite the Production slot's network configuration with the configuration from this slot. Defaults to `true`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "overwrite_network_config")

    @property
    @pulumi.getter(name="slotId")
    def slot_id(self) -> pulumi.Output[str]:
        """
        The ID of the Slot to swap with `Production`.
        """
        return pulumi.get(self, "slot_id")

