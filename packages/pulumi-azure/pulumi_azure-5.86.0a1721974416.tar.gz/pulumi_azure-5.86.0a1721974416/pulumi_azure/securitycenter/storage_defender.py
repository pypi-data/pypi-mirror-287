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

__all__ = ['StorageDefenderArgs', 'StorageDefender']

@pulumi.input_type
class StorageDefenderArgs:
    def __init__(__self__, *,
                 storage_account_id: pulumi.Input[str],
                 malware_scanning_on_upload_cap_gb_per_month: Optional[pulumi.Input[int]] = None,
                 malware_scanning_on_upload_enabled: Optional[pulumi.Input[bool]] = None,
                 override_subscription_settings_enabled: Optional[pulumi.Input[bool]] = None,
                 sensitive_data_discovery_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a StorageDefender resource.
        :param pulumi.Input[str] storage_account_id: The ID of the storage account the defender applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[int] malware_scanning_on_upload_cap_gb_per_month: The max GB to be scanned per Month. Must be `-1` or above `0`. Omit this property or set to `-1` if no capping is needed. Defaults to `-1`.
        :param pulumi.Input[bool] malware_scanning_on_upload_enabled: Whether On Upload malware scanning should be enabled. Defaults to `false`.
        :param pulumi.Input[bool] override_subscription_settings_enabled: Whether the settings defined for this storage account should override the settings defined for the subscription. Defaults to `false`.
        :param pulumi.Input[bool] sensitive_data_discovery_enabled: Whether Sensitive Data Discovery should be enabled. Defaults to `false`.
        """
        pulumi.set(__self__, "storage_account_id", storage_account_id)
        if malware_scanning_on_upload_cap_gb_per_month is not None:
            pulumi.set(__self__, "malware_scanning_on_upload_cap_gb_per_month", malware_scanning_on_upload_cap_gb_per_month)
        if malware_scanning_on_upload_enabled is not None:
            pulumi.set(__self__, "malware_scanning_on_upload_enabled", malware_scanning_on_upload_enabled)
        if override_subscription_settings_enabled is not None:
            pulumi.set(__self__, "override_subscription_settings_enabled", override_subscription_settings_enabled)
        if sensitive_data_discovery_enabled is not None:
            pulumi.set(__self__, "sensitive_data_discovery_enabled", sensitive_data_discovery_enabled)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[str]:
        """
        The ID of the storage account the defender applied to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter(name="malwareScanningOnUploadCapGbPerMonth")
    def malware_scanning_on_upload_cap_gb_per_month(self) -> Optional[pulumi.Input[int]]:
        """
        The max GB to be scanned per Month. Must be `-1` or above `0`. Omit this property or set to `-1` if no capping is needed. Defaults to `-1`.
        """
        return pulumi.get(self, "malware_scanning_on_upload_cap_gb_per_month")

    @malware_scanning_on_upload_cap_gb_per_month.setter
    def malware_scanning_on_upload_cap_gb_per_month(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "malware_scanning_on_upload_cap_gb_per_month", value)

    @property
    @pulumi.getter(name="malwareScanningOnUploadEnabled")
    def malware_scanning_on_upload_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether On Upload malware scanning should be enabled. Defaults to `false`.
        """
        return pulumi.get(self, "malware_scanning_on_upload_enabled")

    @malware_scanning_on_upload_enabled.setter
    def malware_scanning_on_upload_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "malware_scanning_on_upload_enabled", value)

    @property
    @pulumi.getter(name="overrideSubscriptionSettingsEnabled")
    def override_subscription_settings_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the settings defined for this storage account should override the settings defined for the subscription. Defaults to `false`.
        """
        return pulumi.get(self, "override_subscription_settings_enabled")

    @override_subscription_settings_enabled.setter
    def override_subscription_settings_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "override_subscription_settings_enabled", value)

    @property
    @pulumi.getter(name="sensitiveDataDiscoveryEnabled")
    def sensitive_data_discovery_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether Sensitive Data Discovery should be enabled. Defaults to `false`.
        """
        return pulumi.get(self, "sensitive_data_discovery_enabled")

    @sensitive_data_discovery_enabled.setter
    def sensitive_data_discovery_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sensitive_data_discovery_enabled", value)


@pulumi.input_type
class _StorageDefenderState:
    def __init__(__self__, *,
                 malware_scanning_on_upload_cap_gb_per_month: Optional[pulumi.Input[int]] = None,
                 malware_scanning_on_upload_enabled: Optional[pulumi.Input[bool]] = None,
                 override_subscription_settings_enabled: Optional[pulumi.Input[bool]] = None,
                 sensitive_data_discovery_enabled: Optional[pulumi.Input[bool]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StorageDefender resources.
        :param pulumi.Input[int] malware_scanning_on_upload_cap_gb_per_month: The max GB to be scanned per Month. Must be `-1` or above `0`. Omit this property or set to `-1` if no capping is needed. Defaults to `-1`.
        :param pulumi.Input[bool] malware_scanning_on_upload_enabled: Whether On Upload malware scanning should be enabled. Defaults to `false`.
        :param pulumi.Input[bool] override_subscription_settings_enabled: Whether the settings defined for this storage account should override the settings defined for the subscription. Defaults to `false`.
        :param pulumi.Input[bool] sensitive_data_discovery_enabled: Whether Sensitive Data Discovery should be enabled. Defaults to `false`.
        :param pulumi.Input[str] storage_account_id: The ID of the storage account the defender applied to. Changing this forces a new resource to be created.
        """
        if malware_scanning_on_upload_cap_gb_per_month is not None:
            pulumi.set(__self__, "malware_scanning_on_upload_cap_gb_per_month", malware_scanning_on_upload_cap_gb_per_month)
        if malware_scanning_on_upload_enabled is not None:
            pulumi.set(__self__, "malware_scanning_on_upload_enabled", malware_scanning_on_upload_enabled)
        if override_subscription_settings_enabled is not None:
            pulumi.set(__self__, "override_subscription_settings_enabled", override_subscription_settings_enabled)
        if sensitive_data_discovery_enabled is not None:
            pulumi.set(__self__, "sensitive_data_discovery_enabled", sensitive_data_discovery_enabled)
        if storage_account_id is not None:
            pulumi.set(__self__, "storage_account_id", storage_account_id)

    @property
    @pulumi.getter(name="malwareScanningOnUploadCapGbPerMonth")
    def malware_scanning_on_upload_cap_gb_per_month(self) -> Optional[pulumi.Input[int]]:
        """
        The max GB to be scanned per Month. Must be `-1` or above `0`. Omit this property or set to `-1` if no capping is needed. Defaults to `-1`.
        """
        return pulumi.get(self, "malware_scanning_on_upload_cap_gb_per_month")

    @malware_scanning_on_upload_cap_gb_per_month.setter
    def malware_scanning_on_upload_cap_gb_per_month(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "malware_scanning_on_upload_cap_gb_per_month", value)

    @property
    @pulumi.getter(name="malwareScanningOnUploadEnabled")
    def malware_scanning_on_upload_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether On Upload malware scanning should be enabled. Defaults to `false`.
        """
        return pulumi.get(self, "malware_scanning_on_upload_enabled")

    @malware_scanning_on_upload_enabled.setter
    def malware_scanning_on_upload_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "malware_scanning_on_upload_enabled", value)

    @property
    @pulumi.getter(name="overrideSubscriptionSettingsEnabled")
    def override_subscription_settings_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the settings defined for this storage account should override the settings defined for the subscription. Defaults to `false`.
        """
        return pulumi.get(self, "override_subscription_settings_enabled")

    @override_subscription_settings_enabled.setter
    def override_subscription_settings_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "override_subscription_settings_enabled", value)

    @property
    @pulumi.getter(name="sensitiveDataDiscoveryEnabled")
    def sensitive_data_discovery_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether Sensitive Data Discovery should be enabled. Defaults to `false`.
        """
        return pulumi.get(self, "sensitive_data_discovery_enabled")

    @sensitive_data_discovery_enabled.setter
    def sensitive_data_discovery_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sensitive_data_discovery_enabled", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the storage account the defender applied to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_id", value)


class StorageDefender(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 malware_scanning_on_upload_cap_gb_per_month: Optional[pulumi.Input[int]] = None,
                 malware_scanning_on_upload_enabled: Optional[pulumi.Input[bool]] = None,
                 override_subscription_settings_enabled: Optional[pulumi.Input[bool]] = None,
                 sensitive_data_discovery_enabled: Optional[pulumi.Input[bool]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages the Defender for Storage.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-rg",
            location="westus2")
        example_account = azure.storage.Account("example",
            name="exampleacc",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_storage_defender = azure.securitycenter.StorageDefender("example", storage_account_id=example_account.id)
        ```

        ## Import

        The setting can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:securitycenter/storageDefender:StorageDefender example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Storage/storageAccounts/storageacc
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] malware_scanning_on_upload_cap_gb_per_month: The max GB to be scanned per Month. Must be `-1` or above `0`. Omit this property or set to `-1` if no capping is needed. Defaults to `-1`.
        :param pulumi.Input[bool] malware_scanning_on_upload_enabled: Whether On Upload malware scanning should be enabled. Defaults to `false`.
        :param pulumi.Input[bool] override_subscription_settings_enabled: Whether the settings defined for this storage account should override the settings defined for the subscription. Defaults to `false`.
        :param pulumi.Input[bool] sensitive_data_discovery_enabled: Whether Sensitive Data Discovery should be enabled. Defaults to `false`.
        :param pulumi.Input[str] storage_account_id: The ID of the storage account the defender applied to. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageDefenderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages the Defender for Storage.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-rg",
            location="westus2")
        example_account = azure.storage.Account("example",
            name="exampleacc",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="LRS")
        example_storage_defender = azure.securitycenter.StorageDefender("example", storage_account_id=example_account.id)
        ```

        ## Import

        The setting can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:securitycenter/storageDefender:StorageDefender example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Storage/storageAccounts/storageacc
        ```

        :param str resource_name: The name of the resource.
        :param StorageDefenderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageDefenderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 malware_scanning_on_upload_cap_gb_per_month: Optional[pulumi.Input[int]] = None,
                 malware_scanning_on_upload_enabled: Optional[pulumi.Input[bool]] = None,
                 override_subscription_settings_enabled: Optional[pulumi.Input[bool]] = None,
                 sensitive_data_discovery_enabled: Optional[pulumi.Input[bool]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StorageDefenderArgs.__new__(StorageDefenderArgs)

            __props__.__dict__["malware_scanning_on_upload_cap_gb_per_month"] = malware_scanning_on_upload_cap_gb_per_month
            __props__.__dict__["malware_scanning_on_upload_enabled"] = malware_scanning_on_upload_enabled
            __props__.__dict__["override_subscription_settings_enabled"] = override_subscription_settings_enabled
            __props__.__dict__["sensitive_data_discovery_enabled"] = sensitive_data_discovery_enabled
            if storage_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_id'")
            __props__.__dict__["storage_account_id"] = storage_account_id
        super(StorageDefender, __self__).__init__(
            'azure:securitycenter/storageDefender:StorageDefender',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            malware_scanning_on_upload_cap_gb_per_month: Optional[pulumi.Input[int]] = None,
            malware_scanning_on_upload_enabled: Optional[pulumi.Input[bool]] = None,
            override_subscription_settings_enabled: Optional[pulumi.Input[bool]] = None,
            sensitive_data_discovery_enabled: Optional[pulumi.Input[bool]] = None,
            storage_account_id: Optional[pulumi.Input[str]] = None) -> 'StorageDefender':
        """
        Get an existing StorageDefender resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] malware_scanning_on_upload_cap_gb_per_month: The max GB to be scanned per Month. Must be `-1` or above `0`. Omit this property or set to `-1` if no capping is needed. Defaults to `-1`.
        :param pulumi.Input[bool] malware_scanning_on_upload_enabled: Whether On Upload malware scanning should be enabled. Defaults to `false`.
        :param pulumi.Input[bool] override_subscription_settings_enabled: Whether the settings defined for this storage account should override the settings defined for the subscription. Defaults to `false`.
        :param pulumi.Input[bool] sensitive_data_discovery_enabled: Whether Sensitive Data Discovery should be enabled. Defaults to `false`.
        :param pulumi.Input[str] storage_account_id: The ID of the storage account the defender applied to. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StorageDefenderState.__new__(_StorageDefenderState)

        __props__.__dict__["malware_scanning_on_upload_cap_gb_per_month"] = malware_scanning_on_upload_cap_gb_per_month
        __props__.__dict__["malware_scanning_on_upload_enabled"] = malware_scanning_on_upload_enabled
        __props__.__dict__["override_subscription_settings_enabled"] = override_subscription_settings_enabled
        __props__.__dict__["sensitive_data_discovery_enabled"] = sensitive_data_discovery_enabled
        __props__.__dict__["storage_account_id"] = storage_account_id
        return StorageDefender(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="malwareScanningOnUploadCapGbPerMonth")
    def malware_scanning_on_upload_cap_gb_per_month(self) -> pulumi.Output[Optional[int]]:
        """
        The max GB to be scanned per Month. Must be `-1` or above `0`. Omit this property or set to `-1` if no capping is needed. Defaults to `-1`.
        """
        return pulumi.get(self, "malware_scanning_on_upload_cap_gb_per_month")

    @property
    @pulumi.getter(name="malwareScanningOnUploadEnabled")
    def malware_scanning_on_upload_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether On Upload malware scanning should be enabled. Defaults to `false`.
        """
        return pulumi.get(self, "malware_scanning_on_upload_enabled")

    @property
    @pulumi.getter(name="overrideSubscriptionSettingsEnabled")
    def override_subscription_settings_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the settings defined for this storage account should override the settings defined for the subscription. Defaults to `false`.
        """
        return pulumi.get(self, "override_subscription_settings_enabled")

    @property
    @pulumi.getter(name="sensitiveDataDiscoveryEnabled")
    def sensitive_data_discovery_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether Sensitive Data Discovery should be enabled. Defaults to `false`.
        """
        return pulumi.get(self, "sensitive_data_discovery_enabled")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[str]:
        """
        The ID of the storage account the defender applied to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "storage_account_id")

