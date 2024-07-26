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
    'GetStaticWebAppResult',
    'AwaitableGetStaticWebAppResult',
    'get_static_web_app',
    'get_static_web_app_output',
]

@pulumi.output_type
class GetStaticWebAppResult:
    """
    A collection of values returned by getStaticWebApp.
    """
    def __init__(__self__, api_key=None, app_settings=None, basic_auths=None, configuration_file_changes_enabled=None, default_host_name=None, id=None, identities=None, location=None, name=None, preview_environments_enabled=None, resource_group_name=None, sku_size=None, sku_tier=None, tags=None):
        if api_key and not isinstance(api_key, str):
            raise TypeError("Expected argument 'api_key' to be a str")
        pulumi.set(__self__, "api_key", api_key)
        if app_settings and not isinstance(app_settings, dict):
            raise TypeError("Expected argument 'app_settings' to be a dict")
        pulumi.set(__self__, "app_settings", app_settings)
        if basic_auths and not isinstance(basic_auths, list):
            raise TypeError("Expected argument 'basic_auths' to be a list")
        pulumi.set(__self__, "basic_auths", basic_auths)
        if configuration_file_changes_enabled and not isinstance(configuration_file_changes_enabled, bool):
            raise TypeError("Expected argument 'configuration_file_changes_enabled' to be a bool")
        pulumi.set(__self__, "configuration_file_changes_enabled", configuration_file_changes_enabled)
        if default_host_name and not isinstance(default_host_name, str):
            raise TypeError("Expected argument 'default_host_name' to be a str")
        pulumi.set(__self__, "default_host_name", default_host_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identities and not isinstance(identities, list):
            raise TypeError("Expected argument 'identities' to be a list")
        pulumi.set(__self__, "identities", identities)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if preview_environments_enabled and not isinstance(preview_environments_enabled, bool):
            raise TypeError("Expected argument 'preview_environments_enabled' to be a bool")
        pulumi.set(__self__, "preview_environments_enabled", preview_environments_enabled)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sku_size and not isinstance(sku_size, str):
            raise TypeError("Expected argument 'sku_size' to be a str")
        pulumi.set(__self__, "sku_size", sku_size)
        if sku_tier and not isinstance(sku_tier, str):
            raise TypeError("Expected argument 'sku_tier' to be a str")
        pulumi.set(__self__, "sku_tier", sku_tier)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> str:
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="appSettings")
    def app_settings(self) -> Mapping[str, str]:
        return pulumi.get(self, "app_settings")

    @property
    @pulumi.getter(name="basicAuths")
    def basic_auths(self) -> Sequence['outputs.GetStaticWebAppBasicAuthResult']:
        return pulumi.get(self, "basic_auths")

    @property
    @pulumi.getter(name="configurationFileChangesEnabled")
    def configuration_file_changes_enabled(self) -> bool:
        return pulumi.get(self, "configuration_file_changes_enabled")

    @property
    @pulumi.getter(name="defaultHostName")
    def default_host_name(self) -> str:
        return pulumi.get(self, "default_host_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identities(self) -> Sequence['outputs.GetStaticWebAppIdentityResult']:
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="previewEnvironmentsEnabled")
    def preview_environments_enabled(self) -> bool:
        return pulumi.get(self, "preview_environments_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="skuSize")
    def sku_size(self) -> str:
        return pulumi.get(self, "sku_size")

    @property
    @pulumi.getter(name="skuTier")
    def sku_tier(self) -> str:
        return pulumi.get(self, "sku_tier")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        return pulumi.get(self, "tags")


class AwaitableGetStaticWebAppResult(GetStaticWebAppResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStaticWebAppResult(
            api_key=self.api_key,
            app_settings=self.app_settings,
            basic_auths=self.basic_auths,
            configuration_file_changes_enabled=self.configuration_file_changes_enabled,
            default_host_name=self.default_host_name,
            id=self.id,
            identities=self.identities,
            location=self.location,
            name=self.name,
            preview_environments_enabled=self.preview_environments_enabled,
            resource_group_name=self.resource_group_name,
            sku_size=self.sku_size,
            sku_tier=self.sku_tier,
            tags=self.tags)


def get_static_web_app(name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStaticWebAppResult:
    """
    Use this data source to access information about an existing Static Web App.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_static_web_app(name="existing",
        resource_group_name="existing")
    ```


    :param str name: The name of this Static Web App.
    :param str resource_group_name: The name of the Resource Group where the Static Web App exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:appservice/getStaticWebApp:getStaticWebApp', __args__, opts=opts, typ=GetStaticWebAppResult).value

    return AwaitableGetStaticWebAppResult(
        api_key=pulumi.get(__ret__, 'api_key'),
        app_settings=pulumi.get(__ret__, 'app_settings'),
        basic_auths=pulumi.get(__ret__, 'basic_auths'),
        configuration_file_changes_enabled=pulumi.get(__ret__, 'configuration_file_changes_enabled'),
        default_host_name=pulumi.get(__ret__, 'default_host_name'),
        id=pulumi.get(__ret__, 'id'),
        identities=pulumi.get(__ret__, 'identities'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        preview_environments_enabled=pulumi.get(__ret__, 'preview_environments_enabled'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        sku_size=pulumi.get(__ret__, 'sku_size'),
        sku_tier=pulumi.get(__ret__, 'sku_tier'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_static_web_app)
def get_static_web_app_output(name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStaticWebAppResult]:
    """
    Use this data source to access information about an existing Static Web App.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.appservice.get_static_web_app(name="existing",
        resource_group_name="existing")
    ```


    :param str name: The name of this Static Web App.
    :param str resource_group_name: The name of the Resource Group where the Static Web App exists.
    """
    ...
