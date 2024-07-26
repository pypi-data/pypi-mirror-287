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
    'HubApnsCredentialArgs',
    'HubApnsCredentialArgsDict',
    'HubGcmCredentialArgs',
    'HubGcmCredentialArgsDict',
]

MYPY = False

if not MYPY:
    class HubApnsCredentialArgsDict(TypedDict):
        application_mode: pulumi.Input[str]
        """
        The Application Mode which defines which server the APNS Messages should be sent to. Possible values are `Production` and `Sandbox`.
        """
        bundle_id: pulumi.Input[str]
        """
        The Bundle ID of the iOS/macOS application to send push notifications for, such as `com.org.example`.
        """
        key_id: pulumi.Input[str]
        """
        The Apple Push Notifications Service (APNS) Key.
        """
        team_id: pulumi.Input[str]
        """
        The ID of the team the Token.
        """
        token: pulumi.Input[str]
        """
        The Push Token associated with the Apple Developer Account. This is the contents of the `key` downloaded from [the Apple Developer Portal](https://developer.apple.com/account/ios/authkey/) between the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` blocks.
        """
elif False:
    HubApnsCredentialArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class HubApnsCredentialArgs:
    def __init__(__self__, *,
                 application_mode: pulumi.Input[str],
                 bundle_id: pulumi.Input[str],
                 key_id: pulumi.Input[str],
                 team_id: pulumi.Input[str],
                 token: pulumi.Input[str]):
        """
        :param pulumi.Input[str] application_mode: The Application Mode which defines which server the APNS Messages should be sent to. Possible values are `Production` and `Sandbox`.
        :param pulumi.Input[str] bundle_id: The Bundle ID of the iOS/macOS application to send push notifications for, such as `com.org.example`.
        :param pulumi.Input[str] key_id: The Apple Push Notifications Service (APNS) Key.
        :param pulumi.Input[str] team_id: The ID of the team the Token.
        :param pulumi.Input[str] token: The Push Token associated with the Apple Developer Account. This is the contents of the `key` downloaded from [the Apple Developer Portal](https://developer.apple.com/account/ios/authkey/) between the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` blocks.
        """
        pulumi.set(__self__, "application_mode", application_mode)
        pulumi.set(__self__, "bundle_id", bundle_id)
        pulumi.set(__self__, "key_id", key_id)
        pulumi.set(__self__, "team_id", team_id)
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="applicationMode")
    def application_mode(self) -> pulumi.Input[str]:
        """
        The Application Mode which defines which server the APNS Messages should be sent to. Possible values are `Production` and `Sandbox`.
        """
        return pulumi.get(self, "application_mode")

    @application_mode.setter
    def application_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_mode", value)

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Input[str]:
        """
        The Bundle ID of the iOS/macOS application to send push notifications for, such as `com.org.example`.
        """
        return pulumi.get(self, "bundle_id")

    @bundle_id.setter
    def bundle_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "bundle_id", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[str]:
        """
        The Apple Push Notifications Service (APNS) Key.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_id", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Input[str]:
        """
        The ID of the team the Token.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter
    def token(self) -> pulumi.Input[str]:
        """
        The Push Token associated with the Apple Developer Account. This is the contents of the `key` downloaded from [the Apple Developer Portal](https://developer.apple.com/account/ios/authkey/) between the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` blocks.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: pulumi.Input[str]):
        pulumi.set(self, "token", value)


if not MYPY:
    class HubGcmCredentialArgsDict(TypedDict):
        api_key: pulumi.Input[str]
        """
        The API Key associated with the Google Cloud Messaging service.
        """
elif False:
    HubGcmCredentialArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class HubGcmCredentialArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str]):
        """
        :param pulumi.Input[str] api_key: The API Key associated with the Google Cloud Messaging service.
        """
        pulumi.set(__self__, "api_key", api_key)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[str]:
        """
        The API Key associated with the Google Cloud Messaging service.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_key", value)


