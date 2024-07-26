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

__all__ = ['NotificationRecipientEmailArgs', 'NotificationRecipientEmail']

@pulumi.input_type
class NotificationRecipientEmailArgs:
    def __init__(__self__, *,
                 api_management_id: pulumi.Input[str],
                 email: pulumi.Input[str],
                 notification_type: pulumi.Input[str]):
        """
        The set of arguments for constructing a NotificationRecipientEmail resource.
        :param pulumi.Input[str] api_management_id: The ID of the API Management Service from which to create this Notification Recipient Email. Changing this forces a new API Management Notification Recipient Email to be created.
        :param pulumi.Input[str] email: The recipient email address. Changing this forces a new API Management Notification Recipient Email to be created.
        :param pulumi.Input[str] notification_type: The Notification Name to be received. Changing this forces a new API Management Notification Recipient Email to be created. Possible values are `AccountClosedPublisher`, `BCC`, `NewApplicationNotificationMessage`, `NewIssuePublisherNotificationMessage`, `PurchasePublisherNotificationMessage`, `QuotaLimitApproachingPublisherNotificationMessage`, and `RequestPublisherNotificationMessage`.
        """
        pulumi.set(__self__, "api_management_id", api_management_id)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "notification_type", notification_type)

    @property
    @pulumi.getter(name="apiManagementId")
    def api_management_id(self) -> pulumi.Input[str]:
        """
        The ID of the API Management Service from which to create this Notification Recipient Email. Changing this forces a new API Management Notification Recipient Email to be created.
        """
        return pulumi.get(self, "api_management_id")

    @api_management_id.setter
    def api_management_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_management_id", value)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        The recipient email address. Changing this forces a new API Management Notification Recipient Email to be created.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Input[str]:
        """
        The Notification Name to be received. Changing this forces a new API Management Notification Recipient Email to be created. Possible values are `AccountClosedPublisher`, `BCC`, `NewApplicationNotificationMessage`, `NewIssuePublisherNotificationMessage`, `PurchasePublisherNotificationMessage`, `QuotaLimitApproachingPublisherNotificationMessage`, and `RequestPublisherNotificationMessage`.
        """
        return pulumi.get(self, "notification_type")

    @notification_type.setter
    def notification_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "notification_type", value)


@pulumi.input_type
class _NotificationRecipientEmailState:
    def __init__(__self__, *,
                 api_management_id: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 notification_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NotificationRecipientEmail resources.
        :param pulumi.Input[str] api_management_id: The ID of the API Management Service from which to create this Notification Recipient Email. Changing this forces a new API Management Notification Recipient Email to be created.
        :param pulumi.Input[str] email: The recipient email address. Changing this forces a new API Management Notification Recipient Email to be created.
        :param pulumi.Input[str] notification_type: The Notification Name to be received. Changing this forces a new API Management Notification Recipient Email to be created. Possible values are `AccountClosedPublisher`, `BCC`, `NewApplicationNotificationMessage`, `NewIssuePublisherNotificationMessage`, `PurchasePublisherNotificationMessage`, `QuotaLimitApproachingPublisherNotificationMessage`, and `RequestPublisherNotificationMessage`.
        """
        if api_management_id is not None:
            pulumi.set(__self__, "api_management_id", api_management_id)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if notification_type is not None:
            pulumi.set(__self__, "notification_type", notification_type)

    @property
    @pulumi.getter(name="apiManagementId")
    def api_management_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the API Management Service from which to create this Notification Recipient Email. Changing this forces a new API Management Notification Recipient Email to be created.
        """
        return pulumi.get(self, "api_management_id")

    @api_management_id.setter
    def api_management_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_management_id", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The recipient email address. Changing this forces a new API Management Notification Recipient Email to be created.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[pulumi.Input[str]]:
        """
        The Notification Name to be received. Changing this forces a new API Management Notification Recipient Email to be created. Possible values are `AccountClosedPublisher`, `BCC`, `NewApplicationNotificationMessage`, `NewIssuePublisherNotificationMessage`, `PurchasePublisherNotificationMessage`, `QuotaLimitApproachingPublisherNotificationMessage`, and `RequestPublisherNotificationMessage`.
        """
        return pulumi.get(self, "notification_type")

    @notification_type.setter
    def notification_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notification_type", value)


class NotificationRecipientEmail(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_management_id: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 notification_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a API Management Notification Recipient Email.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_service = azure.apimanagement.Service("example",
            name="example-apim",
            location=example.location,
            resource_group_name=example.name,
            publisher_name="My Company",
            publisher_email="company@terraform.io",
            sku_name="Developer_1")
        example_notification_recipient_email = azure.apimanagement.NotificationRecipientEmail("example",
            api_management_id=example_service.id,
            notification_type="AccountClosedPublisher",
            email="foo@bar.com")
        ```

        ## Import

        API Management Notification Recipient Emails can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:apimanagement/notificationRecipientEmail:NotificationRecipientEmail example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.ApiManagement/service/service1/notifications/notificationName1/recipientEmails/email1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_id: The ID of the API Management Service from which to create this Notification Recipient Email. Changing this forces a new API Management Notification Recipient Email to be created.
        :param pulumi.Input[str] email: The recipient email address. Changing this forces a new API Management Notification Recipient Email to be created.
        :param pulumi.Input[str] notification_type: The Notification Name to be received. Changing this forces a new API Management Notification Recipient Email to be created. Possible values are `AccountClosedPublisher`, `BCC`, `NewApplicationNotificationMessage`, `NewIssuePublisherNotificationMessage`, `PurchasePublisherNotificationMessage`, `QuotaLimitApproachingPublisherNotificationMessage`, and `RequestPublisherNotificationMessage`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationRecipientEmailArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a API Management Notification Recipient Email.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_service = azure.apimanagement.Service("example",
            name="example-apim",
            location=example.location,
            resource_group_name=example.name,
            publisher_name="My Company",
            publisher_email="company@terraform.io",
            sku_name="Developer_1")
        example_notification_recipient_email = azure.apimanagement.NotificationRecipientEmail("example",
            api_management_id=example_service.id,
            notification_type="AccountClosedPublisher",
            email="foo@bar.com")
        ```

        ## Import

        API Management Notification Recipient Emails can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:apimanagement/notificationRecipientEmail:NotificationRecipientEmail example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.ApiManagement/service/service1/notifications/notificationName1/recipientEmails/email1
        ```

        :param str resource_name: The name of the resource.
        :param NotificationRecipientEmailArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationRecipientEmailArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_management_id: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 notification_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NotificationRecipientEmailArgs.__new__(NotificationRecipientEmailArgs)

            if api_management_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_management_id'")
            __props__.__dict__["api_management_id"] = api_management_id
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            if notification_type is None and not opts.urn:
                raise TypeError("Missing required property 'notification_type'")
            __props__.__dict__["notification_type"] = notification_type
        super(NotificationRecipientEmail, __self__).__init__(
            'azure:apimanagement/notificationRecipientEmail:NotificationRecipientEmail',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_management_id: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            notification_type: Optional[pulumi.Input[str]] = None) -> 'NotificationRecipientEmail':
        """
        Get an existing NotificationRecipientEmail resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_id: The ID of the API Management Service from which to create this Notification Recipient Email. Changing this forces a new API Management Notification Recipient Email to be created.
        :param pulumi.Input[str] email: The recipient email address. Changing this forces a new API Management Notification Recipient Email to be created.
        :param pulumi.Input[str] notification_type: The Notification Name to be received. Changing this forces a new API Management Notification Recipient Email to be created. Possible values are `AccountClosedPublisher`, `BCC`, `NewApplicationNotificationMessage`, `NewIssuePublisherNotificationMessage`, `PurchasePublisherNotificationMessage`, `QuotaLimitApproachingPublisherNotificationMessage`, and `RequestPublisherNotificationMessage`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NotificationRecipientEmailState.__new__(_NotificationRecipientEmailState)

        __props__.__dict__["api_management_id"] = api_management_id
        __props__.__dict__["email"] = email
        __props__.__dict__["notification_type"] = notification_type
        return NotificationRecipientEmail(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiManagementId")
    def api_management_id(self) -> pulumi.Output[str]:
        """
        The ID of the API Management Service from which to create this Notification Recipient Email. Changing this forces a new API Management Notification Recipient Email to be created.
        """
        return pulumi.get(self, "api_management_id")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The recipient email address. Changing this forces a new API Management Notification Recipient Email to be created.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> pulumi.Output[str]:
        """
        The Notification Name to be received. Changing this forces a new API Management Notification Recipient Email to be created. Possible values are `AccountClosedPublisher`, `BCC`, `NewApplicationNotificationMessage`, `NewIssuePublisherNotificationMessage`, `PurchasePublisherNotificationMessage`, `QuotaLimitApproachingPublisherNotificationMessage`, and `RequestPublisherNotificationMessage`.
        """
        return pulumi.get(self, "notification_type")

