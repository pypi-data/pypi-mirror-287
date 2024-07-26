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
    'AccountCustomerManagedKeyArgs',
    'AccountCustomerManagedKeyArgsDict',
    'AccountIdentityArgs',
    'AccountIdentityArgsDict',
    'AccountNetworkAclsArgs',
    'AccountNetworkAclsArgsDict',
    'AccountNetworkAclsVirtualNetworkRuleArgs',
    'AccountNetworkAclsVirtualNetworkRuleArgsDict',
    'AccountStorageArgs',
    'AccountStorageArgsDict',
    'DeploymentModelArgs',
    'DeploymentModelArgsDict',
    'DeploymentScaleArgs',
    'DeploymentScaleArgsDict',
]

MYPY = False

if not MYPY:
    class AccountCustomerManagedKeyArgsDict(TypedDict):
        key_vault_key_id: pulumi.Input[str]
        """
        The ID of the Key Vault Key which should be used to Encrypt the data in this Cognitive Account.
        """
        identity_client_id: NotRequired[pulumi.Input[str]]
        """
        The Client ID of the User Assigned Identity that has access to the key. This property only needs to be specified when there're multiple identities attached to the Cognitive Account.
        """
elif False:
    AccountCustomerManagedKeyArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AccountCustomerManagedKeyArgs:
    def __init__(__self__, *,
                 key_vault_key_id: pulumi.Input[str],
                 identity_client_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault Key which should be used to Encrypt the data in this Cognitive Account.
        :param pulumi.Input[str] identity_client_id: The Client ID of the User Assigned Identity that has access to the key. This property only needs to be specified when there're multiple identities attached to the Cognitive Account.
        """
        pulumi.set(__self__, "key_vault_key_id", key_vault_key_id)
        if identity_client_id is not None:
            pulumi.set(__self__, "identity_client_id", identity_client_id)

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> pulumi.Input[str]:
        """
        The ID of the Key Vault Key which should be used to Encrypt the data in this Cognitive Account.
        """
        return pulumi.get(self, "key_vault_key_id")

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_key_id", value)

    @property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Client ID of the User Assigned Identity that has access to the key. This property only needs to be specified when there're multiple identities attached to the Cognitive Account.
        """
        return pulumi.get(self, "identity_client_id")

    @identity_client_id.setter
    def identity_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_client_id", value)


if not MYPY:
    class AccountIdentityArgsDict(TypedDict):
        type: pulumi.Input[str]
        """
        Specifies the type of Managed Service Identity that should be configured on this Cognitive Account. Possible values are `SystemAssigned`, `UserAssigned`, `SystemAssigned, UserAssigned` (to enable both).
        """
        identity_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        Specifies a list of User Assigned Managed Identity IDs to be assigned to this Cognitive Account.

        > **NOTE:** This is required when `type` is set to `UserAssigned` or `SystemAssigned, UserAssigned`.
        """
        principal_id: NotRequired[pulumi.Input[str]]
        """
        The Principal ID associated with this Managed Service Identity.
        """
        tenant_id: NotRequired[pulumi.Input[str]]
        """
        The Tenant ID associated with this Managed Service Identity.
        """
elif False:
    AccountIdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AccountIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 identity_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: Specifies the type of Managed Service Identity that should be configured on this Cognitive Account. Possible values are `SystemAssigned`, `UserAssigned`, `SystemAssigned, UserAssigned` (to enable both).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identity_ids: Specifies a list of User Assigned Managed Identity IDs to be assigned to this Cognitive Account.
               
               > **NOTE:** This is required when `type` is set to `UserAssigned` or `SystemAssigned, UserAssigned`.
        :param pulumi.Input[str] principal_id: The Principal ID associated with this Managed Service Identity.
        :param pulumi.Input[str] tenant_id: The Tenant ID associated with this Managed Service Identity.
        """
        pulumi.set(__self__, "type", type)
        if identity_ids is not None:
            pulumi.set(__self__, "identity_ids", identity_ids)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Specifies the type of Managed Service Identity that should be configured on this Cognitive Account. Possible values are `SystemAssigned`, `UserAssigned`, `SystemAssigned, UserAssigned` (to enable both).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of User Assigned Managed Identity IDs to be assigned to this Cognitive Account.

        > **NOTE:** This is required when `type` is set to `UserAssigned` or `SystemAssigned, UserAssigned`.
        """
        return pulumi.get(self, "identity_ids")

    @identity_ids.setter
    def identity_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "identity_ids", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Principal ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Tenant ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


if not MYPY:
    class AccountNetworkAclsArgsDict(TypedDict):
        default_action: pulumi.Input[str]
        """
        The Default Action to use when no rules match from `ip_rules` / `virtual_network_rules`. Possible values are `Allow` and `Deny`.
        """
        ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        One or more IP Addresses, or CIDR Blocks which should be able to access the Cognitive Account.
        """
        virtual_network_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input['AccountNetworkAclsVirtualNetworkRuleArgsDict']]]]
        """
        A `virtual_network_rules` block as defined below.
        """
elif False:
    AccountNetworkAclsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AccountNetworkAclsArgs:
    def __init__(__self__, *,
                 default_action: pulumi.Input[str],
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkAclsVirtualNetworkRuleArgs']]]] = None):
        """
        :param pulumi.Input[str] default_action: The Default Action to use when no rules match from `ip_rules` / `virtual_network_rules`. Possible values are `Allow` and `Deny`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_rules: One or more IP Addresses, or CIDR Blocks which should be able to access the Cognitive Account.
        :param pulumi.Input[Sequence[pulumi.Input['AccountNetworkAclsVirtualNetworkRuleArgs']]] virtual_network_rules: A `virtual_network_rules` block as defined below.
        """
        pulumi.set(__self__, "default_action", default_action)
        if ip_rules is not None:
            pulumi.set(__self__, "ip_rules", ip_rules)
        if virtual_network_rules is not None:
            pulumi.set(__self__, "virtual_network_rules", virtual_network_rules)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input[str]:
        """
        The Default Action to use when no rules match from `ip_rules` / `virtual_network_rules`. Possible values are `Allow` and `Deny`.
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        One or more IP Addresses, or CIDR Blocks which should be able to access the Cognitive Account.
        """
        return pulumi.get(self, "ip_rules")

    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_rules", value)

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkAclsVirtualNetworkRuleArgs']]]]:
        """
        A `virtual_network_rules` block as defined below.
        """
        return pulumi.get(self, "virtual_network_rules")

    @virtual_network_rules.setter
    def virtual_network_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccountNetworkAclsVirtualNetworkRuleArgs']]]]):
        pulumi.set(self, "virtual_network_rules", value)


if not MYPY:
    class AccountNetworkAclsVirtualNetworkRuleArgsDict(TypedDict):
        subnet_id: pulumi.Input[str]
        """
        The ID of the subnet which should be able to access this Cognitive Account.
        """
        ignore_missing_vnet_service_endpoint: NotRequired[pulumi.Input[bool]]
        """
        Whether ignore missing vnet service endpoint or not. Default to `false`.
        """
elif False:
    AccountNetworkAclsVirtualNetworkRuleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AccountNetworkAclsVirtualNetworkRuleArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str],
                 ignore_missing_vnet_service_endpoint: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] subnet_id: The ID of the subnet which should be able to access this Cognitive Account.
        :param pulumi.Input[bool] ignore_missing_vnet_service_endpoint: Whether ignore missing vnet service endpoint or not. Default to `false`.
        """
        pulumi.set(__self__, "subnet_id", subnet_id)
        if ignore_missing_vnet_service_endpoint is not None:
            pulumi.set(__self__, "ignore_missing_vnet_service_endpoint", ignore_missing_vnet_service_endpoint)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The ID of the subnet which should be able to access this Cognitive Account.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether ignore missing vnet service endpoint or not. Default to `false`.
        """
        return pulumi.get(self, "ignore_missing_vnet_service_endpoint")

    @ignore_missing_vnet_service_endpoint.setter
    def ignore_missing_vnet_service_endpoint(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_missing_vnet_service_endpoint", value)


if not MYPY:
    class AccountStorageArgsDict(TypedDict):
        storage_account_id: pulumi.Input[str]
        """
        Full resource id of a Microsoft.Storage resource.
        """
        identity_client_id: NotRequired[pulumi.Input[str]]
        """
        The client ID of the managed identity associated with the storage resource.

        > **NOTE:** Not all `kind` support a `storage` block. For example the `kind` `OpenAI` does not support it.
        """
elif False:
    AccountStorageArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AccountStorageArgs:
    def __init__(__self__, *,
                 storage_account_id: pulumi.Input[str],
                 identity_client_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] storage_account_id: Full resource id of a Microsoft.Storage resource.
        :param pulumi.Input[str] identity_client_id: The client ID of the managed identity associated with the storage resource.
               
               > **NOTE:** Not all `kind` support a `storage` block. For example the `kind` `OpenAI` does not support it.
        """
        pulumi.set(__self__, "storage_account_id", storage_account_id)
        if identity_client_id is not None:
            pulumi.set(__self__, "identity_client_id", identity_client_id)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Input[str]:
        """
        Full resource id of a Microsoft.Storage resource.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The client ID of the managed identity associated with the storage resource.

        > **NOTE:** Not all `kind` support a `storage` block. For example the `kind` `OpenAI` does not support it.
        """
        return pulumi.get(self, "identity_client_id")

    @identity_client_id.setter
    def identity_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_client_id", value)


if not MYPY:
    class DeploymentModelArgsDict(TypedDict):
        format: pulumi.Input[str]
        """
        The format of the Cognitive Services Account Deployment model. Changing this forces a new resource to be created. Possible value is `OpenAI`.
        """
        name: pulumi.Input[str]
        """
        The name of the Cognitive Services Account Deployment model. Changing this forces a new resource to be created.
        """
        version: NotRequired[pulumi.Input[str]]
        """
        The version of Cognitive Services Account Deployment model. If `version` is not specified, the default version of the model at the time will be assigned.
        """
elif False:
    DeploymentModelArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DeploymentModelArgs:
    def __init__(__self__, *,
                 format: pulumi.Input[str],
                 name: pulumi.Input[str],
                 version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] format: The format of the Cognitive Services Account Deployment model. Changing this forces a new resource to be created. Possible value is `OpenAI`.
        :param pulumi.Input[str] name: The name of the Cognitive Services Account Deployment model. Changing this forces a new resource to be created.
        :param pulumi.Input[str] version: The version of Cognitive Services Account Deployment model. If `version` is not specified, the default version of the model at the time will be assigned.
        """
        pulumi.set(__self__, "format", format)
        pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def format(self) -> pulumi.Input[str]:
        """
        The format of the Cognitive Services Account Deployment model. Changing this forces a new resource to be created. Possible value is `OpenAI`.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: pulumi.Input[str]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the Cognitive Services Account Deployment model. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of Cognitive Services Account Deployment model. If `version` is not specified, the default version of the model at the time will be assigned.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


if not MYPY:
    class DeploymentScaleArgsDict(TypedDict):
        type: pulumi.Input[str]
        """
        The name of the SKU. Ex - `Standard` or `P3`. It is typically a letter+number code. Changing this forces a new resource to be created.
        """
        capacity: NotRequired[pulumi.Input[int]]
        """
        Tokens-per-Minute (TPM). The unit of measure for this field is in the thousands of Tokens-per-Minute. Defaults to `1` which means that the limitation is `1000` tokens per minute. If the resources SKU supports scale in/out then the capacity field should be included in the resources' configuration. If the scale in/out is not supported by the resources SKU then this field can be safely omitted. For more information about TPM please see the [product documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/quota?tabs=rest).
        """
        family: NotRequired[pulumi.Input[str]]
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here. Changing this forces a new resource to be created.
        """
        size: NotRequired[pulumi.Input[str]]
        """
        The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. Changing this forces a new resource to be created.
        """
        tier: NotRequired[pulumi.Input[str]]
        """
        Possible values are `Free`, `Basic`, `Standard`, `Premium`, `Enterprise`. Changing this forces a new resource to be created.
        """
elif False:
    DeploymentScaleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DeploymentScaleArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 capacity: Optional[pulumi.Input[int]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The name of the SKU. Ex - `Standard` or `P3`. It is typically a letter+number code. Changing this forces a new resource to be created.
        :param pulumi.Input[int] capacity: Tokens-per-Minute (TPM). The unit of measure for this field is in the thousands of Tokens-per-Minute. Defaults to `1` which means that the limitation is `1000` tokens per minute. If the resources SKU supports scale in/out then the capacity field should be included in the resources' configuration. If the scale in/out is not supported by the resources SKU then this field can be safely omitted. For more information about TPM please see the [product documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/quota?tabs=rest).
        :param pulumi.Input[str] family: If the service has different generations of hardware, for the same SKU, then that can be captured here. Changing this forces a new resource to be created.
        :param pulumi.Input[str] size: The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. Changing this forces a new resource to be created.
        :param pulumi.Input[str] tier: Possible values are `Free`, `Basic`, `Standard`, `Premium`, `Enterprise`. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "type", type)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The name of the SKU. Ex - `Standard` or `P3`. It is typically a letter+number code. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        Tokens-per-Minute (TPM). The unit of measure for this field is in the thousands of Tokens-per-Minute. Defaults to `1` which means that the limitation is `1000` tokens per minute. If the resources SKU supports scale in/out then the capacity field should be included in the resources' configuration. If the scale in/out is not supported by the resources SKU then this field can be safely omitted. For more information about TPM please see the [product documentation](https://learn.microsoft.com/azure/ai-services/openai/how-to/quota?tabs=rest).
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[str]]:
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        Possible values are `Free`, `Basic`, `Standard`, `Premium`, `Enterprise`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


