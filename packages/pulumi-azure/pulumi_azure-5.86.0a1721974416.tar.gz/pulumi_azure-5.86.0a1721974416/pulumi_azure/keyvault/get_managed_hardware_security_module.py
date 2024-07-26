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
    'GetManagedHardwareSecurityModuleResult',
    'AwaitableGetManagedHardwareSecurityModuleResult',
    'get_managed_hardware_security_module',
    'get_managed_hardware_security_module_output',
]

@pulumi.output_type
class GetManagedHardwareSecurityModuleResult:
    """
    A collection of values returned by getManagedHardwareSecurityModule.
    """
    def __init__(__self__, admin_object_ids=None, hsm_uri=None, id=None, location=None, name=None, purge_protection_enabled=None, resource_group_name=None, sku_name=None, soft_delete_retention_days=None, tags=None, tenant_id=None):
        if admin_object_ids and not isinstance(admin_object_ids, list):
            raise TypeError("Expected argument 'admin_object_ids' to be a list")
        pulumi.set(__self__, "admin_object_ids", admin_object_ids)
        if hsm_uri and not isinstance(hsm_uri, str):
            raise TypeError("Expected argument 'hsm_uri' to be a str")
        pulumi.set(__self__, "hsm_uri", hsm_uri)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if purge_protection_enabled and not isinstance(purge_protection_enabled, bool):
            raise TypeError("Expected argument 'purge_protection_enabled' to be a bool")
        pulumi.set(__self__, "purge_protection_enabled", purge_protection_enabled)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sku_name and not isinstance(sku_name, str):
            raise TypeError("Expected argument 'sku_name' to be a str")
        pulumi.set(__self__, "sku_name", sku_name)
        if soft_delete_retention_days and not isinstance(soft_delete_retention_days, int):
            raise TypeError("Expected argument 'soft_delete_retention_days' to be a int")
        pulumi.set(__self__, "soft_delete_retention_days", soft_delete_retention_days)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="adminObjectIds")
    def admin_object_ids(self) -> Sequence[str]:
        """
        Specifies a list of administrators object IDs for the key vault Managed Hardware Security Module.
        """
        return pulumi.get(self, "admin_object_ids")

    @property
    @pulumi.getter(name="hsmUri")
    def hsm_uri(self) -> str:
        """
        The URI of the Hardware Security Module for performing operations on keys and secrets.
        """
        return pulumi.get(self, "hsm_uri")

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
        The Azure Region in which the Key Vault managed Hardware Security Module exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="purgeProtectionEnabled")
    def purge_protection_enabled(self) -> bool:
        """
        Is purge protection enabled on this Key Vault Managed Hardware Security Module?
        """
        return pulumi.get(self, "purge_protection_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> str:
        """
        The Name of the SKU used for this Key Vault Managed Hardware Security Module.
        """
        return pulumi.get(self, "sku_name")

    @property
    @pulumi.getter(name="softDeleteRetentionDays")
    def soft_delete_retention_days(self) -> int:
        """
        The number of days that items should be retained for soft-deleted.
        """
        return pulumi.get(self, "soft_delete_retention_days")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the Key Vault Managed Hardware Security Module.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The Azure Active Directory Tenant ID used for authenticating requests to the Key Vault Managed Hardware Security Module.
        """
        return pulumi.get(self, "tenant_id")


class AwaitableGetManagedHardwareSecurityModuleResult(GetManagedHardwareSecurityModuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedHardwareSecurityModuleResult(
            admin_object_ids=self.admin_object_ids,
            hsm_uri=self.hsm_uri,
            id=self.id,
            location=self.location,
            name=self.name,
            purge_protection_enabled=self.purge_protection_enabled,
            resource_group_name=self.resource_group_name,
            sku_name=self.sku_name,
            soft_delete_retention_days=self.soft_delete_retention_days,
            tags=self.tags,
            tenant_id=self.tenant_id)


def get_managed_hardware_security_module(name: Optional[str] = None,
                                         resource_group_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedHardwareSecurityModuleResult:
    """
    Use this data source to access information about an existing Key Vault Managed Hardware Security Module.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.keyvault.get_managed_hardware_security_module(name="mykeyvaultHsm",
        resource_group_name="some-resource-group")
    pulumi.export("hsmUri", example.hsm_uri)
    ```


    :param str name: The name of the Key Vault Managed Hardware Security Module.
    :param str resource_group_name: The name of the Resource Group in which the Key Vault Managed Hardware Security Module exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:keyvault/getManagedHardwareSecurityModule:getManagedHardwareSecurityModule', __args__, opts=opts, typ=GetManagedHardwareSecurityModuleResult).value

    return AwaitableGetManagedHardwareSecurityModuleResult(
        admin_object_ids=pulumi.get(__ret__, 'admin_object_ids'),
        hsm_uri=pulumi.get(__ret__, 'hsm_uri'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        purge_protection_enabled=pulumi.get(__ret__, 'purge_protection_enabled'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        sku_name=pulumi.get(__ret__, 'sku_name'),
        soft_delete_retention_days=pulumi.get(__ret__, 'soft_delete_retention_days'),
        tags=pulumi.get(__ret__, 'tags'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'))


@_utilities.lift_output_func(get_managed_hardware_security_module)
def get_managed_hardware_security_module_output(name: Optional[pulumi.Input[str]] = None,
                                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedHardwareSecurityModuleResult]:
    """
    Use this data source to access information about an existing Key Vault Managed Hardware Security Module.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.keyvault.get_managed_hardware_security_module(name="mykeyvaultHsm",
        resource_group_name="some-resource-group")
    pulumi.export("hsmUri", example.hsm_uri)
    ```


    :param str name: The name of the Key Vault Managed Hardware Security Module.
    :param str resource_group_name: The name of the Resource Group in which the Key Vault Managed Hardware Security Module exists.
    """
    ...
