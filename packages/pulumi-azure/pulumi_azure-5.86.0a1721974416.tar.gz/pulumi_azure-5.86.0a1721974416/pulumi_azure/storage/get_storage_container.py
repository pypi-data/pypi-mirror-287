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
    'GetStorageContainerResult',
    'AwaitableGetStorageContainerResult',
    'get_storage_container',
    'get_storage_container_output',
]

@pulumi.output_type
class GetStorageContainerResult:
    """
    A collection of values returned by getStorageContainer.
    """
    def __init__(__self__, container_access_type=None, default_encryption_scope=None, encryption_scope_override_enabled=None, has_immutability_policy=None, has_legal_hold=None, id=None, metadata=None, name=None, resource_manager_id=None, storage_account_name=None):
        if container_access_type and not isinstance(container_access_type, str):
            raise TypeError("Expected argument 'container_access_type' to be a str")
        pulumi.set(__self__, "container_access_type", container_access_type)
        if default_encryption_scope and not isinstance(default_encryption_scope, str):
            raise TypeError("Expected argument 'default_encryption_scope' to be a str")
        pulumi.set(__self__, "default_encryption_scope", default_encryption_scope)
        if encryption_scope_override_enabled and not isinstance(encryption_scope_override_enabled, bool):
            raise TypeError("Expected argument 'encryption_scope_override_enabled' to be a bool")
        pulumi.set(__self__, "encryption_scope_override_enabled", encryption_scope_override_enabled)
        if has_immutability_policy and not isinstance(has_immutability_policy, bool):
            raise TypeError("Expected argument 'has_immutability_policy' to be a bool")
        pulumi.set(__self__, "has_immutability_policy", has_immutability_policy)
        if has_legal_hold and not isinstance(has_legal_hold, bool):
            raise TypeError("Expected argument 'has_legal_hold' to be a bool")
        pulumi.set(__self__, "has_legal_hold", has_legal_hold)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_manager_id and not isinstance(resource_manager_id, str):
            raise TypeError("Expected argument 'resource_manager_id' to be a str")
        pulumi.set(__self__, "resource_manager_id", resource_manager_id)
        if storage_account_name and not isinstance(storage_account_name, str):
            raise TypeError("Expected argument 'storage_account_name' to be a str")
        pulumi.set(__self__, "storage_account_name", storage_account_name)

    @property
    @pulumi.getter(name="containerAccessType")
    def container_access_type(self) -> str:
        """
        The Access Level configured for this Container.
        """
        return pulumi.get(self, "container_access_type")

    @property
    @pulumi.getter(name="defaultEncryptionScope")
    def default_encryption_scope(self) -> str:
        """
        The default encryption scope in use for blobs uploaded to this container.
        """
        return pulumi.get(self, "default_encryption_scope")

    @property
    @pulumi.getter(name="encryptionScopeOverrideEnabled")
    def encryption_scope_override_enabled(self) -> bool:
        """
        Whether blobs are allowed to override the default encryption scope for this container.
        """
        return pulumi.get(self, "encryption_scope_override_enabled")

    @property
    @pulumi.getter(name="hasImmutabilityPolicy")
    def has_immutability_policy(self) -> bool:
        """
        Is there an Immutability Policy configured on this Storage Container?
        """
        return pulumi.get(self, "has_immutability_policy")

    @property
    @pulumi.getter(name="hasLegalHold")
    def has_legal_hold(self) -> bool:
        """
        Is there a Legal Hold configured on this Storage Container?
        """
        return pulumi.get(self, "has_legal_hold")

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
        A mapping of MetaData for this Container.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceManagerId")
    def resource_manager_id(self) -> str:
        """
        The Resource Manager ID of this Storage Container.
        """
        return pulumi.get(self, "resource_manager_id")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> str:
        return pulumi.get(self, "storage_account_name")


class AwaitableGetStorageContainerResult(GetStorageContainerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStorageContainerResult(
            container_access_type=self.container_access_type,
            default_encryption_scope=self.default_encryption_scope,
            encryption_scope_override_enabled=self.encryption_scope_override_enabled,
            has_immutability_policy=self.has_immutability_policy,
            has_legal_hold=self.has_legal_hold,
            id=self.id,
            metadata=self.metadata,
            name=self.name,
            resource_manager_id=self.resource_manager_id,
            storage_account_name=self.storage_account_name)


def get_storage_container(metadata: Optional[Mapping[str, str]] = None,
                          name: Optional[str] = None,
                          storage_account_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStorageContainerResult:
    """
    Use this data source to access information about an existing Storage Container.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.storage.get_storage_container(name="example-container-name",
        storage_account_name="example-storage-account-name")
    ```


    :param Mapping[str, str] metadata: A mapping of MetaData for this Container.
    :param str name: The name of the Container.
    :param str storage_account_name: The name of the Storage Account where the Container exists.
    """
    __args__ = dict()
    __args__['metadata'] = metadata
    __args__['name'] = name
    __args__['storageAccountName'] = storage_account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:storage/getStorageContainer:getStorageContainer', __args__, opts=opts, typ=GetStorageContainerResult).value

    return AwaitableGetStorageContainerResult(
        container_access_type=pulumi.get(__ret__, 'container_access_type'),
        default_encryption_scope=pulumi.get(__ret__, 'default_encryption_scope'),
        encryption_scope_override_enabled=pulumi.get(__ret__, 'encryption_scope_override_enabled'),
        has_immutability_policy=pulumi.get(__ret__, 'has_immutability_policy'),
        has_legal_hold=pulumi.get(__ret__, 'has_legal_hold'),
        id=pulumi.get(__ret__, 'id'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        resource_manager_id=pulumi.get(__ret__, 'resource_manager_id'),
        storage_account_name=pulumi.get(__ret__, 'storage_account_name'))


@_utilities.lift_output_func(get_storage_container)
def get_storage_container_output(metadata: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                 name: Optional[pulumi.Input[str]] = None,
                                 storage_account_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStorageContainerResult]:
    """
    Use this data source to access information about an existing Storage Container.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.storage.get_storage_container(name="example-container-name",
        storage_account_name="example-storage-account-name")
    ```


    :param Mapping[str, str] metadata: A mapping of MetaData for this Container.
    :param str name: The name of the Container.
    :param str storage_account_name: The name of the Storage Account where the Container exists.
    """
    ...
