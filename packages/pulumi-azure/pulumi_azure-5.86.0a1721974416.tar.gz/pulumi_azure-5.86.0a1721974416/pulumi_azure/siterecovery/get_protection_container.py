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
    'GetProtectionContainerResult',
    'AwaitableGetProtectionContainerResult',
    'get_protection_container',
    'get_protection_container_output',
]

@pulumi.output_type
class GetProtectionContainerResult:
    """
    A collection of values returned by getProtectionContainer.
    """
    def __init__(__self__, id=None, name=None, recovery_fabric_name=None, recovery_vault_name=None, resource_group_name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if recovery_fabric_name and not isinstance(recovery_fabric_name, str):
            raise TypeError("Expected argument 'recovery_fabric_name' to be a str")
        pulumi.set(__self__, "recovery_fabric_name", recovery_fabric_name)
        if recovery_vault_name and not isinstance(recovery_vault_name, str):
            raise TypeError("Expected argument 'recovery_vault_name' to be a str")
        pulumi.set(__self__, "recovery_vault_name", recovery_vault_name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recoveryFabricName")
    def recovery_fabric_name(self) -> str:
        return pulumi.get(self, "recovery_fabric_name")

    @property
    @pulumi.getter(name="recoveryVaultName")
    def recovery_vault_name(self) -> str:
        return pulumi.get(self, "recovery_vault_name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")


class AwaitableGetProtectionContainerResult(GetProtectionContainerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProtectionContainerResult(
            id=self.id,
            name=self.name,
            recovery_fabric_name=self.recovery_fabric_name,
            recovery_vault_name=self.recovery_vault_name,
            resource_group_name=self.resource_group_name)


def get_protection_container(name: Optional[str] = None,
                             recovery_fabric_name: Optional[str] = None,
                             recovery_vault_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProtectionContainerResult:
    """
    Use this data source to access information about an existing site recovery services protection container.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    container = azure.siterecovery.get_protection_container(name="primary-container",
        recovery_vault_name="tfex-recovery_vault",
        resource_group_name="tfex-resource_group",
        recovery_fabric_name="primary-fabric")
    ```


    :param str name: Specifies the name of the protection container.
    :param str recovery_fabric_name: The name of the fabric that contains the protection container.
    :param str recovery_vault_name: The name of the Recovery Services Vault that the protection container is associated witth.
    :param str resource_group_name: The name of the resource group in which the associated protection container resides.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['recoveryFabricName'] = recovery_fabric_name
    __args__['recoveryVaultName'] = recovery_vault_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:siterecovery/getProtectionContainer:getProtectionContainer', __args__, opts=opts, typ=GetProtectionContainerResult).value

    return AwaitableGetProtectionContainerResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        recovery_fabric_name=pulumi.get(__ret__, 'recovery_fabric_name'),
        recovery_vault_name=pulumi.get(__ret__, 'recovery_vault_name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'))


@_utilities.lift_output_func(get_protection_container)
def get_protection_container_output(name: Optional[pulumi.Input[str]] = None,
                                    recovery_fabric_name: Optional[pulumi.Input[str]] = None,
                                    recovery_vault_name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProtectionContainerResult]:
    """
    Use this data source to access information about an existing site recovery services protection container.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    container = azure.siterecovery.get_protection_container(name="primary-container",
        recovery_vault_name="tfex-recovery_vault",
        resource_group_name="tfex-resource_group",
        recovery_fabric_name="primary-fabric")
    ```


    :param str name: Specifies the name of the protection container.
    :param str recovery_fabric_name: The name of the fabric that contains the protection container.
    :param str recovery_vault_name: The name of the Recovery Services Vault that the protection container is associated witth.
    :param str resource_group_name: The name of the resource group in which the associated protection container resides.
    """
    ...
