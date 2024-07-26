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
    'GetSecretResult',
    'AwaitableGetSecretResult',
    'get_secret',
    'get_secret_output',
]

@pulumi.output_type
class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, content_type=None, expiration_date=None, id=None, key_vault_id=None, name=None, not_before_date=None, resource_id=None, resource_versionless_id=None, tags=None, value=None, version=None, versionless_id=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if expiration_date and not isinstance(expiration_date, str):
            raise TypeError("Expected argument 'expiration_date' to be a str")
        pulumi.set(__self__, "expiration_date", expiration_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_vault_id and not isinstance(key_vault_id, str):
            raise TypeError("Expected argument 'key_vault_id' to be a str")
        pulumi.set(__self__, "key_vault_id", key_vault_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if not_before_date and not isinstance(not_before_date, str):
            raise TypeError("Expected argument 'not_before_date' to be a str")
        pulumi.set(__self__, "not_before_date", not_before_date)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if resource_versionless_id and not isinstance(resource_versionless_id, str):
            raise TypeError("Expected argument 'resource_versionless_id' to be a str")
        pulumi.set(__self__, "resource_versionless_id", resource_versionless_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if versionless_id and not isinstance(versionless_id, str):
            raise TypeError("Expected argument 'versionless_id' to be a str")
        pulumi.set(__self__, "versionless_id", versionless_id)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        """
        The content type for the Key Vault Secret.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> str:
        """
        The date and time at which the Key Vault Secret expires and is no longer valid.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> str:
        return pulumi.get(self, "key_vault_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notBeforeDate")
    def not_before_date(self) -> str:
        """
        The earliest date at which the Key Vault Secret can be used.
        """
        return pulumi.get(self, "not_before_date")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        The (Versioned) ID for this Key Vault Secret. This property points to a specific version of a Key Vault Secret, as such using this won't auto-rotate values if used in other Azure Services.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceVersionlessId")
    def resource_versionless_id(self) -> str:
        """
        The Versionless ID of the Key Vault Secret. This property allows other Azure Services (that support it) to auto-rotate their value when the Key Vault Secret is updated.
        """
        return pulumi.get(self, "resource_versionless_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Any tags assigned to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the Key Vault Secret.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="versionlessId")
    def versionless_id(self) -> str:
        """
        The Versionless ID of the Key Vault Secret. This can be used to always get latest secret value, and enable fetching automatically rotating secrets.
        """
        return pulumi.get(self, "versionless_id")


class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            content_type=self.content_type,
            expiration_date=self.expiration_date,
            id=self.id,
            key_vault_id=self.key_vault_id,
            name=self.name,
            not_before_date=self.not_before_date,
            resource_id=self.resource_id,
            resource_versionless_id=self.resource_versionless_id,
            tags=self.tags,
            value=self.value,
            version=self.version,
            versionless_id=self.versionless_id)


def get_secret(key_vault_id: Optional[str] = None,
               name: Optional[str] = None,
               version: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretResult:
    """
    Use this data source to access information about an existing Key Vault Secret.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.keyvault.get_secret(name="secret-sauce",
        key_vault_id=existing["id"])
    pulumi.export("secretValue", example.value)
    ```


    :param str key_vault_id: Specifies the ID of the Key Vault instance to fetch secret names from, available on the `keyvault.KeyVault` Data Source / Resource.
    :param str name: Specifies the name of the Key Vault Secret.
    :param str version: Specifies the version of the Key Vault Secret. Defaults to the current version of the Key Vault Secret.
           
           **NOTE:** The vault must be in the same subscription as the provider. If the vault is in another subscription, you must create an aliased provider for that subscription.
    """
    __args__ = dict()
    __args__['keyVaultId'] = key_vault_id
    __args__['name'] = name
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:keyvault/getSecret:getSecret', __args__, opts=opts, typ=GetSecretResult).value

    return AwaitableGetSecretResult(
        content_type=pulumi.get(__ret__, 'content_type'),
        expiration_date=pulumi.get(__ret__, 'expiration_date'),
        id=pulumi.get(__ret__, 'id'),
        key_vault_id=pulumi.get(__ret__, 'key_vault_id'),
        name=pulumi.get(__ret__, 'name'),
        not_before_date=pulumi.get(__ret__, 'not_before_date'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        resource_versionless_id=pulumi.get(__ret__, 'resource_versionless_id'),
        tags=pulumi.get(__ret__, 'tags'),
        value=pulumi.get(__ret__, 'value'),
        version=pulumi.get(__ret__, 'version'),
        versionless_id=pulumi.get(__ret__, 'versionless_id'))


@_utilities.lift_output_func(get_secret)
def get_secret_output(key_vault_id: Optional[pulumi.Input[str]] = None,
                      name: Optional[pulumi.Input[str]] = None,
                      version: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretResult]:
    """
    Use this data source to access information about an existing Key Vault Secret.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.keyvault.get_secret(name="secret-sauce",
        key_vault_id=existing["id"])
    pulumi.export("secretValue", example.value)
    ```


    :param str key_vault_id: Specifies the ID of the Key Vault instance to fetch secret names from, available on the `keyvault.KeyVault` Data Source / Resource.
    :param str name: Specifies the name of the Key Vault Secret.
    :param str version: Specifies the version of the Key Vault Secret. Defaults to the current version of the Key Vault Secret.
           
           **NOTE:** The vault must be in the same subscription as the provider. If the vault is in another subscription, you must create an aliased provider for that subscription.
    """
    ...
