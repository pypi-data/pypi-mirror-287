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

__all__ = [
    'NamespaceCustomerManagedKey',
    'NamespaceIdentity',
    'NamespaceNetworkRuleSet',
    'NamespaceNetworkRuleSetNetworkRule',
    'SubscriptionClientScopedSubscription',
    'SubscriptionRuleCorrelationFilter',
]

@pulumi.output_type
class NamespaceCustomerManagedKey(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "identityId":
            suggest = "identity_id"
        elif key == "keyVaultKeyId":
            suggest = "key_vault_key_id"
        elif key == "infrastructureEncryptionEnabled":
            suggest = "infrastructure_encryption_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NamespaceCustomerManagedKey. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NamespaceCustomerManagedKey.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NamespaceCustomerManagedKey.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 identity_id: str,
                 key_vault_key_id: str,
                 infrastructure_encryption_enabled: Optional[bool] = None):
        """
        :param str identity_id: The ID of the User Assigned Identity that has access to the key.
        :param str key_vault_key_id: The ID of the Key Vault Key which should be used to Encrypt the data in this ServiceBus Namespace.
        :param bool infrastructure_encryption_enabled: Used to specify whether enable Infrastructure Encryption (Double Encryption). Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "identity_id", identity_id)
        pulumi.set(__self__, "key_vault_key_id", key_vault_key_id)
        if infrastructure_encryption_enabled is not None:
            pulumi.set(__self__, "infrastructure_encryption_enabled", infrastructure_encryption_enabled)

    @property
    @pulumi.getter(name="identityId")
    def identity_id(self) -> str:
        """
        The ID of the User Assigned Identity that has access to the key.
        """
        return pulumi.get(self, "identity_id")

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> str:
        """
        The ID of the Key Vault Key which should be used to Encrypt the data in this ServiceBus Namespace.
        """
        return pulumi.get(self, "key_vault_key_id")

    @property
    @pulumi.getter(name="infrastructureEncryptionEnabled")
    def infrastructure_encryption_enabled(self) -> Optional[bool]:
        """
        Used to specify whether enable Infrastructure Encryption (Double Encryption). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "infrastructure_encryption_enabled")


@pulumi.output_type
class NamespaceIdentity(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "identityIds":
            suggest = "identity_ids"
        elif key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NamespaceIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NamespaceIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NamespaceIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 identity_ids: Optional[Sequence[str]] = None,
                 principal_id: Optional[str] = None,
                 tenant_id: Optional[str] = None):
        """
        :param str type: Specifies the type of Managed Service Identity that should be configured on this ServiceBus Namespace. Possible values are `SystemAssigned`, `UserAssigned`, `SystemAssigned, UserAssigned` (to enable both).
        :param Sequence[str] identity_ids: Specifies a list of User Assigned Managed Identity IDs to be assigned to this ServiceBus namespace.
               
               > **NOTE:** This is required when `type` is set to `UserAssigned` or `SystemAssigned, UserAssigned`.
        :param str principal_id: The Principal ID for the Service Principal associated with the Managed Service Identity of this ServiceBus Namespace.
        :param str tenant_id: The Tenant ID for the Service Principal associated with the Managed Service Identity of this ServiceBus Namespace.
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
    def type(self) -> str:
        """
        Specifies the type of Managed Service Identity that should be configured on this ServiceBus Namespace. Possible values are `SystemAssigned`, `UserAssigned`, `SystemAssigned, UserAssigned` (to enable both).
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Optional[Sequence[str]]:
        """
        Specifies a list of User Assigned Managed Identity IDs to be assigned to this ServiceBus namespace.

        > **NOTE:** This is required when `type` is set to `UserAssigned` or `SystemAssigned, UserAssigned`.
        """
        return pulumi.get(self, "identity_ids")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[str]:
        """
        The Principal ID for the Service Principal associated with the Managed Service Identity of this ServiceBus Namespace.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The Tenant ID for the Service Principal associated with the Managed Service Identity of this ServiceBus Namespace.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class NamespaceNetworkRuleSet(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultAction":
            suggest = "default_action"
        elif key == "ipRules":
            suggest = "ip_rules"
        elif key == "networkRules":
            suggest = "network_rules"
        elif key == "publicNetworkAccessEnabled":
            suggest = "public_network_access_enabled"
        elif key == "trustedServicesAllowed":
            suggest = "trusted_services_allowed"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NamespaceNetworkRuleSet. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NamespaceNetworkRuleSet.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NamespaceNetworkRuleSet.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 default_action: Optional[str] = None,
                 ip_rules: Optional[Sequence[str]] = None,
                 network_rules: Optional[Sequence['outputs.NamespaceNetworkRuleSetNetworkRule']] = None,
                 public_network_access_enabled: Optional[bool] = None,
                 trusted_services_allowed: Optional[bool] = None):
        """
        :param str default_action: Specifies the default action for the Network Rule Set. Possible values are `Allow` and `Deny`. Defaults to `Allow`.
        :param Sequence[str] ip_rules: One or more IP Addresses, or CIDR Blocks which should be able to access the ServiceBus Namespace.
        :param Sequence['NamespaceNetworkRuleSetNetworkRuleArgs'] network_rules: One or more `network_rules` blocks as defined below.
        :param bool public_network_access_enabled: Whether to allow traffic over public network. Possible values are `true` and `false`. Defaults to `true`.
        :param bool trusted_services_allowed: Are Azure Services that are known and trusted for this resource type are allowed to bypass firewall configuration? See [Trusted Microsoft Services](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/service-bus-messaging/includes/service-bus-trusted-services.md)
        """
        if default_action is not None:
            pulumi.set(__self__, "default_action", default_action)
        if ip_rules is not None:
            pulumi.set(__self__, "ip_rules", ip_rules)
        if network_rules is not None:
            pulumi.set(__self__, "network_rules", network_rules)
        if public_network_access_enabled is not None:
            pulumi.set(__self__, "public_network_access_enabled", public_network_access_enabled)
        if trusted_services_allowed is not None:
            pulumi.set(__self__, "trusted_services_allowed", trusted_services_allowed)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[str]:
        """
        Specifies the default action for the Network Rule Set. Possible values are `Allow` and `Deny`. Defaults to `Allow`.
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[Sequence[str]]:
        """
        One or more IP Addresses, or CIDR Blocks which should be able to access the ServiceBus Namespace.
        """
        return pulumi.get(self, "ip_rules")

    @property
    @pulumi.getter(name="networkRules")
    def network_rules(self) -> Optional[Sequence['outputs.NamespaceNetworkRuleSetNetworkRule']]:
        """
        One or more `network_rules` blocks as defined below.
        """
        return pulumi.get(self, "network_rules")

    @property
    @pulumi.getter(name="publicNetworkAccessEnabled")
    def public_network_access_enabled(self) -> Optional[bool]:
        """
        Whether to allow traffic over public network. Possible values are `true` and `false`. Defaults to `true`.
        """
        return pulumi.get(self, "public_network_access_enabled")

    @property
    @pulumi.getter(name="trustedServicesAllowed")
    def trusted_services_allowed(self) -> Optional[bool]:
        """
        Are Azure Services that are known and trusted for this resource type are allowed to bypass firewall configuration? See [Trusted Microsoft Services](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/service-bus-messaging/includes/service-bus-trusted-services.md)
        """
        return pulumi.get(self, "trusted_services_allowed")


@pulumi.output_type
class NamespaceNetworkRuleSetNetworkRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetId":
            suggest = "subnet_id"
        elif key == "ignoreMissingVnetServiceEndpoint":
            suggest = "ignore_missing_vnet_service_endpoint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NamespaceNetworkRuleSetNetworkRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NamespaceNetworkRuleSetNetworkRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NamespaceNetworkRuleSetNetworkRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_id: str,
                 ignore_missing_vnet_service_endpoint: Optional[bool] = None):
        """
        :param str subnet_id: The Subnet ID which should be able to access this ServiceBus Namespace.
        :param bool ignore_missing_vnet_service_endpoint: Should the ServiceBus Namespace Network Rule Set ignore missing Virtual Network Service Endpoint option in the Subnet? Defaults to `false`.
        """
        pulumi.set(__self__, "subnet_id", subnet_id)
        if ignore_missing_vnet_service_endpoint is not None:
            pulumi.set(__self__, "ignore_missing_vnet_service_endpoint", ignore_missing_vnet_service_endpoint)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The Subnet ID which should be able to access this ServiceBus Namespace.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[bool]:
        """
        Should the ServiceBus Namespace Network Rule Set ignore missing Virtual Network Service Endpoint option in the Subnet? Defaults to `false`.
        """
        return pulumi.get(self, "ignore_missing_vnet_service_endpoint")


@pulumi.output_type
class SubscriptionClientScopedSubscription(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "isClientScopedSubscriptionDurable":
            suggest = "is_client_scoped_subscription_durable"
        elif key == "isClientScopedSubscriptionShareable":
            suggest = "is_client_scoped_subscription_shareable"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SubscriptionClientScopedSubscription. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SubscriptionClientScopedSubscription.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SubscriptionClientScopedSubscription.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: Optional[str] = None,
                 is_client_scoped_subscription_durable: Optional[bool] = None,
                 is_client_scoped_subscription_shareable: Optional[bool] = None):
        """
        :param str client_id: Specifies the Client ID of the application that created the client-scoped subscription. Changing this forces a new resource to be created.
               
               > **NOTE:** Client ID can be null or empty, but it must match the client ID set on the JMS client application. From the Azure Service Bus perspective, a null client ID and an empty client id have the same behavior. If the client ID is set to null or empty, it is only accessible to client applications whose client ID is also set to null or empty.
        :param bool is_client_scoped_subscription_durable: Whether the client scoped subscription is durable. This property can only be controlled from the application side.
        :param bool is_client_scoped_subscription_shareable: Whether the client scoped subscription is shareable. Defaults to `true` Changing this forces a new resource to be created.
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if is_client_scoped_subscription_durable is not None:
            pulumi.set(__self__, "is_client_scoped_subscription_durable", is_client_scoped_subscription_durable)
        if is_client_scoped_subscription_shareable is not None:
            pulumi.set(__self__, "is_client_scoped_subscription_shareable", is_client_scoped_subscription_shareable)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[str]:
        """
        Specifies the Client ID of the application that created the client-scoped subscription. Changing this forces a new resource to be created.

        > **NOTE:** Client ID can be null or empty, but it must match the client ID set on the JMS client application. From the Azure Service Bus perspective, a null client ID and an empty client id have the same behavior. If the client ID is set to null or empty, it is only accessible to client applications whose client ID is also set to null or empty.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="isClientScopedSubscriptionDurable")
    def is_client_scoped_subscription_durable(self) -> Optional[bool]:
        """
        Whether the client scoped subscription is durable. This property can only be controlled from the application side.
        """
        return pulumi.get(self, "is_client_scoped_subscription_durable")

    @property
    @pulumi.getter(name="isClientScopedSubscriptionShareable")
    def is_client_scoped_subscription_shareable(self) -> Optional[bool]:
        """
        Whether the client scoped subscription is shareable. Defaults to `true` Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "is_client_scoped_subscription_shareable")


@pulumi.output_type
class SubscriptionRuleCorrelationFilter(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "contentType":
            suggest = "content_type"
        elif key == "correlationId":
            suggest = "correlation_id"
        elif key == "messageId":
            suggest = "message_id"
        elif key == "replyTo":
            suggest = "reply_to"
        elif key == "replyToSessionId":
            suggest = "reply_to_session_id"
        elif key == "sessionId":
            suggest = "session_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SubscriptionRuleCorrelationFilter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SubscriptionRuleCorrelationFilter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SubscriptionRuleCorrelationFilter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 content_type: Optional[str] = None,
                 correlation_id: Optional[str] = None,
                 label: Optional[str] = None,
                 message_id: Optional[str] = None,
                 properties: Optional[Mapping[str, str]] = None,
                 reply_to: Optional[str] = None,
                 reply_to_session_id: Optional[str] = None,
                 session_id: Optional[str] = None,
                 to: Optional[str] = None):
        """
        :param str content_type: Content type of the message.
        :param str correlation_id: Identifier of the correlation.
        :param str label: Application specific label.
        :param str message_id: Identifier of the message.
        :param Mapping[str, str] properties: A list of user defined properties to be included in the filter. Specified as a map of name/value pairs.
               
               > **NOTE:** When creating a subscription rule of type `CorrelationFilter` at least one property must be set in the `correlation_filter` block.
        :param str reply_to: Address of the queue to reply to.
        :param str reply_to_session_id: Session identifier to reply to.
        :param str session_id: Session identifier.
        :param str to: Address to send to.
        """
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if correlation_id is not None:
            pulumi.set(__self__, "correlation_id", correlation_id)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if message_id is not None:
            pulumi.set(__self__, "message_id", message_id)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if reply_to is not None:
            pulumi.set(__self__, "reply_to", reply_to)
        if reply_to_session_id is not None:
            pulumi.set(__self__, "reply_to_session_id", reply_to_session_id)
        if session_id is not None:
            pulumi.set(__self__, "session_id", session_id)
        if to is not None:
            pulumi.set(__self__, "to", to)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[str]:
        """
        Content type of the message.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> Optional[str]:
        """
        Identifier of the correlation.
        """
        return pulumi.get(self, "correlation_id")

    @property
    @pulumi.getter
    def label(self) -> Optional[str]:
        """
        Application specific label.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[str]:
        """
        Identifier of the message.
        """
        return pulumi.get(self, "message_id")

    @property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, str]]:
        """
        A list of user defined properties to be included in the filter. Specified as a map of name/value pairs.

        > **NOTE:** When creating a subscription rule of type `CorrelationFilter` at least one property must be set in the `correlation_filter` block.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> Optional[str]:
        """
        Address of the queue to reply to.
        """
        return pulumi.get(self, "reply_to")

    @property
    @pulumi.getter(name="replyToSessionId")
    def reply_to_session_id(self) -> Optional[str]:
        """
        Session identifier to reply to.
        """
        return pulumi.get(self, "reply_to_session_id")

    @property
    @pulumi.getter(name="sessionId")
    def session_id(self) -> Optional[str]:
        """
        Session identifier.
        """
        return pulumi.get(self, "session_id")

    @property
    @pulumi.getter
    def to(self) -> Optional[str]:
        """
        Address to send to.
        """
        return pulumi.get(self, "to")


