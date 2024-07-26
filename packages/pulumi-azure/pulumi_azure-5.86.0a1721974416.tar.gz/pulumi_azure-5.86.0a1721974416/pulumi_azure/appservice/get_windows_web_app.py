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
    'GetWindowsWebAppResult',
    'AwaitableGetWindowsWebAppResult',
    'get_windows_web_app',
    'get_windows_web_app_output',
]

@pulumi.output_type
class GetWindowsWebAppResult:
    """
    A collection of values returned by getWindowsWebApp.
    """
    def __init__(__self__, app_settings=None, auth_settings=None, auth_settings_v2s=None, backups=None, client_affinity_enabled=None, client_certificate_enabled=None, client_certificate_exclusion_paths=None, client_certificate_mode=None, connection_strings=None, custom_domain_verification_id=None, default_hostname=None, enabled=None, ftp_publish_basic_authentication_enabled=None, hosting_environment_id=None, https_only=None, id=None, identities=None, kind=None, location=None, logs=None, name=None, outbound_ip_address_lists=None, outbound_ip_addresses=None, possible_outbound_ip_address_lists=None, possible_outbound_ip_addresses=None, public_network_access_enabled=None, resource_group_name=None, service_plan_id=None, site_configs=None, site_credentials=None, sticky_settings=None, storage_accounts=None, tags=None, virtual_network_subnet_id=None, webdeploy_publish_basic_authentication_enabled=None):
        if app_settings and not isinstance(app_settings, dict):
            raise TypeError("Expected argument 'app_settings' to be a dict")
        pulumi.set(__self__, "app_settings", app_settings)
        if auth_settings and not isinstance(auth_settings, list):
            raise TypeError("Expected argument 'auth_settings' to be a list")
        pulumi.set(__self__, "auth_settings", auth_settings)
        if auth_settings_v2s and not isinstance(auth_settings_v2s, list):
            raise TypeError("Expected argument 'auth_settings_v2s' to be a list")
        pulumi.set(__self__, "auth_settings_v2s", auth_settings_v2s)
        if backups and not isinstance(backups, list):
            raise TypeError("Expected argument 'backups' to be a list")
        pulumi.set(__self__, "backups", backups)
        if client_affinity_enabled and not isinstance(client_affinity_enabled, bool):
            raise TypeError("Expected argument 'client_affinity_enabled' to be a bool")
        pulumi.set(__self__, "client_affinity_enabled", client_affinity_enabled)
        if client_certificate_enabled and not isinstance(client_certificate_enabled, bool):
            raise TypeError("Expected argument 'client_certificate_enabled' to be a bool")
        pulumi.set(__self__, "client_certificate_enabled", client_certificate_enabled)
        if client_certificate_exclusion_paths and not isinstance(client_certificate_exclusion_paths, str):
            raise TypeError("Expected argument 'client_certificate_exclusion_paths' to be a str")
        pulumi.set(__self__, "client_certificate_exclusion_paths", client_certificate_exclusion_paths)
        if client_certificate_mode and not isinstance(client_certificate_mode, str):
            raise TypeError("Expected argument 'client_certificate_mode' to be a str")
        pulumi.set(__self__, "client_certificate_mode", client_certificate_mode)
        if connection_strings and not isinstance(connection_strings, list):
            raise TypeError("Expected argument 'connection_strings' to be a list")
        pulumi.set(__self__, "connection_strings", connection_strings)
        if custom_domain_verification_id and not isinstance(custom_domain_verification_id, str):
            raise TypeError("Expected argument 'custom_domain_verification_id' to be a str")
        pulumi.set(__self__, "custom_domain_verification_id", custom_domain_verification_id)
        if default_hostname and not isinstance(default_hostname, str):
            raise TypeError("Expected argument 'default_hostname' to be a str")
        pulumi.set(__self__, "default_hostname", default_hostname)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if ftp_publish_basic_authentication_enabled and not isinstance(ftp_publish_basic_authentication_enabled, bool):
            raise TypeError("Expected argument 'ftp_publish_basic_authentication_enabled' to be a bool")
        pulumi.set(__self__, "ftp_publish_basic_authentication_enabled", ftp_publish_basic_authentication_enabled)
        if hosting_environment_id and not isinstance(hosting_environment_id, str):
            raise TypeError("Expected argument 'hosting_environment_id' to be a str")
        pulumi.set(__self__, "hosting_environment_id", hosting_environment_id)
        if https_only and not isinstance(https_only, bool):
            raise TypeError("Expected argument 'https_only' to be a bool")
        pulumi.set(__self__, "https_only", https_only)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identities and not isinstance(identities, list):
            raise TypeError("Expected argument 'identities' to be a list")
        pulumi.set(__self__, "identities", identities)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if logs and not isinstance(logs, list):
            raise TypeError("Expected argument 'logs' to be a list")
        pulumi.set(__self__, "logs", logs)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outbound_ip_address_lists and not isinstance(outbound_ip_address_lists, list):
            raise TypeError("Expected argument 'outbound_ip_address_lists' to be a list")
        pulumi.set(__self__, "outbound_ip_address_lists", outbound_ip_address_lists)
        if outbound_ip_addresses and not isinstance(outbound_ip_addresses, str):
            raise TypeError("Expected argument 'outbound_ip_addresses' to be a str")
        pulumi.set(__self__, "outbound_ip_addresses", outbound_ip_addresses)
        if possible_outbound_ip_address_lists and not isinstance(possible_outbound_ip_address_lists, list):
            raise TypeError("Expected argument 'possible_outbound_ip_address_lists' to be a list")
        pulumi.set(__self__, "possible_outbound_ip_address_lists", possible_outbound_ip_address_lists)
        if possible_outbound_ip_addresses and not isinstance(possible_outbound_ip_addresses, str):
            raise TypeError("Expected argument 'possible_outbound_ip_addresses' to be a str")
        pulumi.set(__self__, "possible_outbound_ip_addresses", possible_outbound_ip_addresses)
        if public_network_access_enabled and not isinstance(public_network_access_enabled, bool):
            raise TypeError("Expected argument 'public_network_access_enabled' to be a bool")
        pulumi.set(__self__, "public_network_access_enabled", public_network_access_enabled)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if service_plan_id and not isinstance(service_plan_id, str):
            raise TypeError("Expected argument 'service_plan_id' to be a str")
        pulumi.set(__self__, "service_plan_id", service_plan_id)
        if site_configs and not isinstance(site_configs, list):
            raise TypeError("Expected argument 'site_configs' to be a list")
        pulumi.set(__self__, "site_configs", site_configs)
        if site_credentials and not isinstance(site_credentials, list):
            raise TypeError("Expected argument 'site_credentials' to be a list")
        pulumi.set(__self__, "site_credentials", site_credentials)
        if sticky_settings and not isinstance(sticky_settings, list):
            raise TypeError("Expected argument 'sticky_settings' to be a list")
        pulumi.set(__self__, "sticky_settings", sticky_settings)
        if storage_accounts and not isinstance(storage_accounts, list):
            raise TypeError("Expected argument 'storage_accounts' to be a list")
        pulumi.set(__self__, "storage_accounts", storage_accounts)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if virtual_network_subnet_id and not isinstance(virtual_network_subnet_id, str):
            raise TypeError("Expected argument 'virtual_network_subnet_id' to be a str")
        pulumi.set(__self__, "virtual_network_subnet_id", virtual_network_subnet_id)
        if webdeploy_publish_basic_authentication_enabled and not isinstance(webdeploy_publish_basic_authentication_enabled, bool):
            raise TypeError("Expected argument 'webdeploy_publish_basic_authentication_enabled' to be a bool")
        pulumi.set(__self__, "webdeploy_publish_basic_authentication_enabled", webdeploy_publish_basic_authentication_enabled)

    @property
    @pulumi.getter(name="appSettings")
    def app_settings(self) -> Mapping[str, str]:
        """
        A map of key-value pairs of App Settings.
        """
        return pulumi.get(self, "app_settings")

    @property
    @pulumi.getter(name="authSettings")
    def auth_settings(self) -> Sequence['outputs.GetWindowsWebAppAuthSettingResult']:
        """
        A `auth_settings` block as defined below.
        """
        return pulumi.get(self, "auth_settings")

    @property
    @pulumi.getter(name="authSettingsV2s")
    def auth_settings_v2s(self) -> Sequence['outputs.GetWindowsWebAppAuthSettingsV2Result']:
        """
        An `auth_settings_v2` block as defined below.
        """
        return pulumi.get(self, "auth_settings_v2s")

    @property
    @pulumi.getter
    def backups(self) -> Sequence['outputs.GetWindowsWebAppBackupResult']:
        """
        A `backup` block as defined below.
        """
        return pulumi.get(self, "backups")

    @property
    @pulumi.getter(name="clientAffinityEnabled")
    def client_affinity_enabled(self) -> bool:
        """
        Is Client Affinity enabled?
        """
        return pulumi.get(self, "client_affinity_enabled")

    @property
    @pulumi.getter(name="clientCertificateEnabled")
    def client_certificate_enabled(self) -> bool:
        """
        Are Client Certificates enabled?
        """
        return pulumi.get(self, "client_certificate_enabled")

    @property
    @pulumi.getter(name="clientCertificateExclusionPaths")
    def client_certificate_exclusion_paths(self) -> str:
        """
        Paths to exclude when using client certificates, separated by ;
        """
        return pulumi.get(self, "client_certificate_exclusion_paths")

    @property
    @pulumi.getter(name="clientCertificateMode")
    def client_certificate_mode(self) -> str:
        """
        The Client Certificate mode.
        """
        return pulumi.get(self, "client_certificate_mode")

    @property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(self) -> Sequence['outputs.GetWindowsWebAppConnectionStringResult']:
        """
        A `connection_string` block as defined below.
        """
        return pulumi.get(self, "connection_strings")

    @property
    @pulumi.getter(name="customDomainVerificationId")
    def custom_domain_verification_id(self) -> str:
        """
        The identifier used by App Service to perform domain ownership verification via DNS TXT record.
        """
        return pulumi.get(self, "custom_domain_verification_id")

    @property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> str:
        """
        The Default Hostname of the Windows Web App.
        """
        return pulumi.get(self, "default_hostname")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Is the Backup enabled?
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="ftpPublishBasicAuthenticationEnabled")
    def ftp_publish_basic_authentication_enabled(self) -> bool:
        """
        Are the default FTP Basic Authentication publishing credentials enabled.
        """
        return pulumi.get(self, "ftp_publish_basic_authentication_enabled")

    @property
    @pulumi.getter(name="hostingEnvironmentId")
    def hosting_environment_id(self) -> str:
        """
        The ID of the App Service Environment used by App Service.
        """
        return pulumi.get(self, "hosting_environment_id")

    @property
    @pulumi.getter(name="httpsOnly")
    def https_only(self) -> bool:
        """
        Does the Windows Web App require HTTPS connections.
        """
        return pulumi.get(self, "https_only")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identities(self) -> Sequence['outputs.GetWindowsWebAppIdentityResult']:
        """
        A `identity` block as defined below.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The string representation of the Windows Web App Kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region where the Windows Web App exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def logs(self) -> Sequence['outputs.GetWindowsWebAppLogResult']:
        """
        A `logs` block as defined below.
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this Storage Account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outboundIpAddressLists")
    def outbound_ip_address_lists(self) -> Sequence[str]:
        """
        The list of Outbound IP Addresses for this Windows Web App.
        """
        return pulumi.get(self, "outbound_ip_address_lists")

    @property
    @pulumi.getter(name="outboundIpAddresses")
    def outbound_ip_addresses(self) -> str:
        """
        A string representation of the list of Outbound IP Addresses for this Windows Web App.
        """
        return pulumi.get(self, "outbound_ip_addresses")

    @property
    @pulumi.getter(name="possibleOutboundIpAddressLists")
    def possible_outbound_ip_address_lists(self) -> Sequence[str]:
        """
        The list of Possible Outbound IP Addresses that could be used by this Windows Web App.
        """
        return pulumi.get(self, "possible_outbound_ip_address_lists")

    @property
    @pulumi.getter(name="possibleOutboundIpAddresses")
    def possible_outbound_ip_addresses(self) -> str:
        """
        The string representation of the list of Possible Outbound IP Addresses that could be used by this Windows Web App.
        """
        return pulumi.get(self, "possible_outbound_ip_addresses")

    @property
    @pulumi.getter(name="publicNetworkAccessEnabled")
    def public_network_access_enabled(self) -> bool:
        """
        Is Public Network Access enabled for the Windows Web App.
        """
        return pulumi.get(self, "public_network_access_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="servicePlanId")
    def service_plan_id(self) -> str:
        """
        The ID of the Service Plan in which this Windows Web App resides.
        """
        return pulumi.get(self, "service_plan_id")

    @property
    @pulumi.getter(name="siteConfigs")
    def site_configs(self) -> Sequence['outputs.GetWindowsWebAppSiteConfigResult']:
        """
        A `site_config` block as defined below.
        """
        return pulumi.get(self, "site_configs")

    @property
    @pulumi.getter(name="siteCredentials")
    def site_credentials(self) -> Sequence['outputs.GetWindowsWebAppSiteCredentialResult']:
        """
        A `site_credential` block as defined below.
        """
        return pulumi.get(self, "site_credentials")

    @property
    @pulumi.getter(name="stickySettings")
    def sticky_settings(self) -> Sequence['outputs.GetWindowsWebAppStickySettingResult']:
        """
        A `sticky_settings` block as defined below.
        """
        return pulumi.get(self, "sticky_settings")

    @property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> Sequence['outputs.GetWindowsWebAppStorageAccountResult']:
        """
        A `storage_account` block as defined below.
        """
        return pulumi.get(self, "storage_accounts")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the Windows Web App.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> str:
        """
        The subnet id which the Windows Web App is vNet Integrated with.
        """
        return pulumi.get(self, "virtual_network_subnet_id")

    @property
    @pulumi.getter(name="webdeployPublishBasicAuthenticationEnabled")
    def webdeploy_publish_basic_authentication_enabled(self) -> bool:
        """
        Are the default WebDeploy Basic Authentication publishing credentials enabled.
        """
        return pulumi.get(self, "webdeploy_publish_basic_authentication_enabled")


class AwaitableGetWindowsWebAppResult(GetWindowsWebAppResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWindowsWebAppResult(
            app_settings=self.app_settings,
            auth_settings=self.auth_settings,
            auth_settings_v2s=self.auth_settings_v2s,
            backups=self.backups,
            client_affinity_enabled=self.client_affinity_enabled,
            client_certificate_enabled=self.client_certificate_enabled,
            client_certificate_exclusion_paths=self.client_certificate_exclusion_paths,
            client_certificate_mode=self.client_certificate_mode,
            connection_strings=self.connection_strings,
            custom_domain_verification_id=self.custom_domain_verification_id,
            default_hostname=self.default_hostname,
            enabled=self.enabled,
            ftp_publish_basic_authentication_enabled=self.ftp_publish_basic_authentication_enabled,
            hosting_environment_id=self.hosting_environment_id,
            https_only=self.https_only,
            id=self.id,
            identities=self.identities,
            kind=self.kind,
            location=self.location,
            logs=self.logs,
            name=self.name,
            outbound_ip_address_lists=self.outbound_ip_address_lists,
            outbound_ip_addresses=self.outbound_ip_addresses,
            possible_outbound_ip_address_lists=self.possible_outbound_ip_address_lists,
            possible_outbound_ip_addresses=self.possible_outbound_ip_addresses,
            public_network_access_enabled=self.public_network_access_enabled,
            resource_group_name=self.resource_group_name,
            service_plan_id=self.service_plan_id,
            site_configs=self.site_configs,
            site_credentials=self.site_credentials,
            sticky_settings=self.sticky_settings,
            storage_accounts=self.storage_accounts,
            tags=self.tags,
            virtual_network_subnet_id=self.virtual_network_subnet_id,
            webdeploy_publish_basic_authentication_enabled=self.webdeploy_publish_basic_authentication_enabled)


def get_windows_web_app(name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWindowsWebAppResult:
    """
    Use this data source to access information about an existing Windows Web App.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_windows_web_app(name="existing",
        resource_group_name="existing")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this Windows Web App.
    :param str resource_group_name: The name of the Resource Group where the Windows Web App exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:appservice/getWindowsWebApp:getWindowsWebApp', __args__, opts=opts, typ=GetWindowsWebAppResult).value

    return AwaitableGetWindowsWebAppResult(
        app_settings=pulumi.get(__ret__, 'app_settings'),
        auth_settings=pulumi.get(__ret__, 'auth_settings'),
        auth_settings_v2s=pulumi.get(__ret__, 'auth_settings_v2s'),
        backups=pulumi.get(__ret__, 'backups'),
        client_affinity_enabled=pulumi.get(__ret__, 'client_affinity_enabled'),
        client_certificate_enabled=pulumi.get(__ret__, 'client_certificate_enabled'),
        client_certificate_exclusion_paths=pulumi.get(__ret__, 'client_certificate_exclusion_paths'),
        client_certificate_mode=pulumi.get(__ret__, 'client_certificate_mode'),
        connection_strings=pulumi.get(__ret__, 'connection_strings'),
        custom_domain_verification_id=pulumi.get(__ret__, 'custom_domain_verification_id'),
        default_hostname=pulumi.get(__ret__, 'default_hostname'),
        enabled=pulumi.get(__ret__, 'enabled'),
        ftp_publish_basic_authentication_enabled=pulumi.get(__ret__, 'ftp_publish_basic_authentication_enabled'),
        hosting_environment_id=pulumi.get(__ret__, 'hosting_environment_id'),
        https_only=pulumi.get(__ret__, 'https_only'),
        id=pulumi.get(__ret__, 'id'),
        identities=pulumi.get(__ret__, 'identities'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        logs=pulumi.get(__ret__, 'logs'),
        name=pulumi.get(__ret__, 'name'),
        outbound_ip_address_lists=pulumi.get(__ret__, 'outbound_ip_address_lists'),
        outbound_ip_addresses=pulumi.get(__ret__, 'outbound_ip_addresses'),
        possible_outbound_ip_address_lists=pulumi.get(__ret__, 'possible_outbound_ip_address_lists'),
        possible_outbound_ip_addresses=pulumi.get(__ret__, 'possible_outbound_ip_addresses'),
        public_network_access_enabled=pulumi.get(__ret__, 'public_network_access_enabled'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        service_plan_id=pulumi.get(__ret__, 'service_plan_id'),
        site_configs=pulumi.get(__ret__, 'site_configs'),
        site_credentials=pulumi.get(__ret__, 'site_credentials'),
        sticky_settings=pulumi.get(__ret__, 'sticky_settings'),
        storage_accounts=pulumi.get(__ret__, 'storage_accounts'),
        tags=pulumi.get(__ret__, 'tags'),
        virtual_network_subnet_id=pulumi.get(__ret__, 'virtual_network_subnet_id'),
        webdeploy_publish_basic_authentication_enabled=pulumi.get(__ret__, 'webdeploy_publish_basic_authentication_enabled'))


@_utilities.lift_output_func(get_windows_web_app)
def get_windows_web_app_output(name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWindowsWebAppResult]:
    """
    Use this data source to access information about an existing Windows Web App.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_windows_web_app(name="existing",
        resource_group_name="existing")
    pulumi.export("id", example.id)
    ```


    :param str name: The name of this Windows Web App.
    :param str resource_group_name: The name of the Resource Group where the Windows Web App exists.
    """
    ...
