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
from ._inputs import *

__all__ = ['StaticWebAppArgs', 'StaticWebApp']

@pulumi.input_type
class StaticWebAppArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 app_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 basic_auth: Optional[pulumi.Input['StaticWebAppBasicAuthArgs']] = None,
                 configuration_file_changes_enabled: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input['StaticWebAppIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preview_environments_enabled: Optional[pulumi.Input[bool]] = None,
                 sku_size: Optional[pulumi.Input[str]] = None,
                 sku_tier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StaticWebApp resource.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] app_settings: A key-value pair of App Settings.
        :param pulumi.Input['StaticWebAppBasicAuthArgs'] basic_auth: A `basic_auth` block as defined below.
        :param pulumi.Input[bool] configuration_file_changes_enabled: Should changes to the configuration file be permitted. Defaults to `true`.
        :param pulumi.Input['StaticWebAppIdentityArgs'] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[str] name: The name which should be used for this Static Web App. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[bool] preview_environments_enabled: Are Preview (Staging) environments enabled. Defaults to `true`.
        :param pulumi.Input[str] sku_size: Specifies the SKU size of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        :param pulumi.Input[str] sku_tier: Specifies the SKU tier of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if app_settings is not None:
            pulumi.set(__self__, "app_settings", app_settings)
        if basic_auth is not None:
            pulumi.set(__self__, "basic_auth", basic_auth)
        if configuration_file_changes_enabled is not None:
            pulumi.set(__self__, "configuration_file_changes_enabled", configuration_file_changes_enabled)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if preview_environments_enabled is not None:
            pulumi.set(__self__, "preview_environments_enabled", preview_environments_enabled)
        if sku_size is not None:
            pulumi.set(__self__, "sku_size", sku_size)
        if sku_tier is not None:
            pulumi.set(__self__, "sku_tier", sku_tier)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="appSettings")
    def app_settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value pair of App Settings.
        """
        return pulumi.get(self, "app_settings")

    @app_settings.setter
    def app_settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "app_settings", value)

    @property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> Optional[pulumi.Input['StaticWebAppBasicAuthArgs']]:
        """
        A `basic_auth` block as defined below.
        """
        return pulumi.get(self, "basic_auth")

    @basic_auth.setter
    def basic_auth(self, value: Optional[pulumi.Input['StaticWebAppBasicAuthArgs']]):
        pulumi.set(self, "basic_auth", value)

    @property
    @pulumi.getter(name="configurationFileChangesEnabled")
    def configuration_file_changes_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should changes to the configuration file be permitted. Defaults to `true`.
        """
        return pulumi.get(self, "configuration_file_changes_enabled")

    @configuration_file_changes_enabled.setter
    def configuration_file_changes_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "configuration_file_changes_enabled", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['StaticWebAppIdentityArgs']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['StaticWebAppIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Static Web App. Changing this forces a new Static Web App to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="previewEnvironmentsEnabled")
    def preview_environments_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Are Preview (Staging) environments enabled. Defaults to `true`.
        """
        return pulumi.get(self, "preview_environments_enabled")

    @preview_environments_enabled.setter
    def preview_environments_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "preview_environments_enabled", value)

    @property
    @pulumi.getter(name="skuSize")
    def sku_size(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the SKU size of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        """
        return pulumi.get(self, "sku_size")

    @sku_size.setter
    def sku_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku_size", value)

    @property
    @pulumi.getter(name="skuTier")
    def sku_tier(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the SKU tier of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        """
        return pulumi.get(self, "sku_tier")

    @sku_tier.setter
    def sku_tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku_tier", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _StaticWebAppState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 app_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 basic_auth: Optional[pulumi.Input['StaticWebAppBasicAuthArgs']] = None,
                 configuration_file_changes_enabled: Optional[pulumi.Input[bool]] = None,
                 default_host_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['StaticWebAppIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preview_environments_enabled: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku_size: Optional[pulumi.Input[str]] = None,
                 sku_tier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering StaticWebApp resources.
        :param pulumi.Input[str] api_key: The API key of this Static Web App, which is used for later interacting with this Static Web App from other clients, e.g. GitHub Action.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] app_settings: A key-value pair of App Settings.
        :param pulumi.Input['StaticWebAppBasicAuthArgs'] basic_auth: A `basic_auth` block as defined below.
        :param pulumi.Input[bool] configuration_file_changes_enabled: Should changes to the configuration file be permitted. Defaults to `true`.
        :param pulumi.Input[str] default_host_name: The default host name of the Static Web App.
        :param pulumi.Input['StaticWebAppIdentityArgs'] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[str] name: The name which should be used for this Static Web App. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[bool] preview_environments_enabled: Are Preview (Staging) environments enabled. Defaults to `true`.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[str] sku_size: Specifies the SKU size of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        :param pulumi.Input[str] sku_tier: Specifies the SKU tier of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if app_settings is not None:
            pulumi.set(__self__, "app_settings", app_settings)
        if basic_auth is not None:
            pulumi.set(__self__, "basic_auth", basic_auth)
        if configuration_file_changes_enabled is not None:
            pulumi.set(__self__, "configuration_file_changes_enabled", configuration_file_changes_enabled)
        if default_host_name is not None:
            pulumi.set(__self__, "default_host_name", default_host_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if preview_environments_enabled is not None:
            pulumi.set(__self__, "preview_environments_enabled", preview_environments_enabled)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sku_size is not None:
            pulumi.set(__self__, "sku_size", sku_size)
        if sku_tier is not None:
            pulumi.set(__self__, "sku_tier", sku_tier)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API key of this Static Web App, which is used for later interacting with this Static Web App from other clients, e.g. GitHub Action.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="appSettings")
    def app_settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value pair of App Settings.
        """
        return pulumi.get(self, "app_settings")

    @app_settings.setter
    def app_settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "app_settings", value)

    @property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> Optional[pulumi.Input['StaticWebAppBasicAuthArgs']]:
        """
        A `basic_auth` block as defined below.
        """
        return pulumi.get(self, "basic_auth")

    @basic_auth.setter
    def basic_auth(self, value: Optional[pulumi.Input['StaticWebAppBasicAuthArgs']]):
        pulumi.set(self, "basic_auth", value)

    @property
    @pulumi.getter(name="configurationFileChangesEnabled")
    def configuration_file_changes_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should changes to the configuration file be permitted. Defaults to `true`.
        """
        return pulumi.get(self, "configuration_file_changes_enabled")

    @configuration_file_changes_enabled.setter
    def configuration_file_changes_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "configuration_file_changes_enabled", value)

    @property
    @pulumi.getter(name="defaultHostName")
    def default_host_name(self) -> Optional[pulumi.Input[str]]:
        """
        The default host name of the Static Web App.
        """
        return pulumi.get(self, "default_host_name")

    @default_host_name.setter
    def default_host_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_host_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['StaticWebAppIdentityArgs']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['StaticWebAppIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Static Web App. Changing this forces a new Static Web App to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="previewEnvironmentsEnabled")
    def preview_environments_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Are Preview (Staging) environments enabled. Defaults to `true`.
        """
        return pulumi.get(self, "preview_environments_enabled")

    @preview_environments_enabled.setter
    def preview_environments_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "preview_environments_enabled", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="skuSize")
    def sku_size(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the SKU size of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        """
        return pulumi.get(self, "sku_size")

    @sku_size.setter
    def sku_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku_size", value)

    @property
    @pulumi.getter(name="skuTier")
    def sku_tier(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the SKU tier of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        """
        return pulumi.get(self, "sku_tier")

    @sku_tier.setter
    def sku_tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku_tier", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class StaticWebApp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 basic_auth: Optional[pulumi.Input[Union['StaticWebAppBasicAuthArgs', 'StaticWebAppBasicAuthArgsDict']]] = None,
                 configuration_file_changes_enabled: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input[Union['StaticWebAppIdentityArgs', 'StaticWebAppIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preview_environments_enabled: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku_size: Optional[pulumi.Input[str]] = None,
                 sku_tier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an App Service Static Web App.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_static_web_app = azure.appservice.StaticWebApp("example",
            name="example",
            resource_group_name=example.name,
            location=example.location)
        ```

        ## Import

        Static Web Apps can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:appservice/staticWebApp:StaticWebApp example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Web/staticSites/my-static-site1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] app_settings: A key-value pair of App Settings.
        :param pulumi.Input[Union['StaticWebAppBasicAuthArgs', 'StaticWebAppBasicAuthArgsDict']] basic_auth: A `basic_auth` block as defined below.
        :param pulumi.Input[bool] configuration_file_changes_enabled: Should changes to the configuration file be permitted. Defaults to `true`.
        :param pulumi.Input[Union['StaticWebAppIdentityArgs', 'StaticWebAppIdentityArgsDict']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[str] name: The name which should be used for this Static Web App. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[bool] preview_environments_enabled: Are Preview (Staging) environments enabled. Defaults to `true`.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[str] sku_size: Specifies the SKU size of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        :param pulumi.Input[str] sku_tier: Specifies the SKU tier of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StaticWebAppArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an App Service Static Web App.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_static_web_app = azure.appservice.StaticWebApp("example",
            name="example",
            resource_group_name=example.name,
            location=example.location)
        ```

        ## Import

        Static Web Apps can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:appservice/staticWebApp:StaticWebApp example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Web/staticSites/my-static-site1
        ```

        :param str resource_name: The name of the resource.
        :param StaticWebAppArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StaticWebAppArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 basic_auth: Optional[pulumi.Input[Union['StaticWebAppBasicAuthArgs', 'StaticWebAppBasicAuthArgsDict']]] = None,
                 configuration_file_changes_enabled: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input[Union['StaticWebAppIdentityArgs', 'StaticWebAppIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preview_environments_enabled: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku_size: Optional[pulumi.Input[str]] = None,
                 sku_tier: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StaticWebAppArgs.__new__(StaticWebAppArgs)

            __props__.__dict__["app_settings"] = app_settings
            __props__.__dict__["basic_auth"] = None if basic_auth is None else pulumi.Output.secret(basic_auth)
            __props__.__dict__["configuration_file_changes_enabled"] = configuration_file_changes_enabled
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["preview_environments_enabled"] = preview_environments_enabled
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku_size"] = sku_size
            __props__.__dict__["sku_tier"] = sku_tier
            __props__.__dict__["tags"] = tags
            __props__.__dict__["api_key"] = None
            __props__.__dict__["default_host_name"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey", "basicAuth"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(StaticWebApp, __self__).__init__(
            'azure:appservice/staticWebApp:StaticWebApp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            app_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            basic_auth: Optional[pulumi.Input[Union['StaticWebAppBasicAuthArgs', 'StaticWebAppBasicAuthArgsDict']]] = None,
            configuration_file_changes_enabled: Optional[pulumi.Input[bool]] = None,
            default_host_name: Optional[pulumi.Input[str]] = None,
            identity: Optional[pulumi.Input[Union['StaticWebAppIdentityArgs', 'StaticWebAppIdentityArgsDict']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            preview_environments_enabled: Optional[pulumi.Input[bool]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            sku_size: Optional[pulumi.Input[str]] = None,
            sku_tier: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'StaticWebApp':
        """
        Get an existing StaticWebApp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: The API key of this Static Web App, which is used for later interacting with this Static Web App from other clients, e.g. GitHub Action.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] app_settings: A key-value pair of App Settings.
        :param pulumi.Input[Union['StaticWebAppBasicAuthArgs', 'StaticWebAppBasicAuthArgsDict']] basic_auth: A `basic_auth` block as defined below.
        :param pulumi.Input[bool] configuration_file_changes_enabled: Should changes to the configuration file be permitted. Defaults to `true`.
        :param pulumi.Input[str] default_host_name: The default host name of the Static Web App.
        :param pulumi.Input[Union['StaticWebAppIdentityArgs', 'StaticWebAppIdentityArgsDict']] identity: An `identity` block as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[str] name: The name which should be used for this Static Web App. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[bool] preview_environments_enabled: Are Preview (Staging) environments enabled. Defaults to `true`.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        :param pulumi.Input[str] sku_size: Specifies the SKU size of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        :param pulumi.Input[str] sku_tier: Specifies the SKU tier of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StaticWebAppState.__new__(_StaticWebAppState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["app_settings"] = app_settings
        __props__.__dict__["basic_auth"] = basic_auth
        __props__.__dict__["configuration_file_changes_enabled"] = configuration_file_changes_enabled
        __props__.__dict__["default_host_name"] = default_host_name
        __props__.__dict__["identity"] = identity
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["preview_environments_enabled"] = preview_environments_enabled
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["sku_size"] = sku_size
        __props__.__dict__["sku_tier"] = sku_tier
        __props__.__dict__["tags"] = tags
        return StaticWebApp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        """
        The API key of this Static Web App, which is used for later interacting with this Static Web App from other clients, e.g. GitHub Action.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="appSettings")
    def app_settings(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A key-value pair of App Settings.
        """
        return pulumi.get(self, "app_settings")

    @property
    @pulumi.getter(name="basicAuth")
    def basic_auth(self) -> pulumi.Output[Optional['outputs.StaticWebAppBasicAuth']]:
        """
        A `basic_auth` block as defined below.
        """
        return pulumi.get(self, "basic_auth")

    @property
    @pulumi.getter(name="configurationFileChangesEnabled")
    def configuration_file_changes_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should changes to the configuration file be permitted. Defaults to `true`.
        """
        return pulumi.get(self, "configuration_file_changes_enabled")

    @property
    @pulumi.getter(name="defaultHostName")
    def default_host_name(self) -> pulumi.Output[str]:
        """
        The default host name of the Static Web App.
        """
        return pulumi.get(self, "default_host_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.StaticWebAppIdentity']]:
        """
        An `identity` block as defined below.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Static Web App. Changing this forces a new Static Web App to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="previewEnvironmentsEnabled")
    def preview_environments_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Are Preview (Staging) environments enabled. Defaults to `true`.
        """
        return pulumi.get(self, "preview_environments_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Static Web App should exist. Changing this forces a new Static Web App to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="skuSize")
    def sku_size(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the SKU size of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        """
        return pulumi.get(self, "sku_size")

    @property
    @pulumi.getter(name="skuTier")
    def sku_tier(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the SKU tier of the Static Web App. Possible values are `Free` or `Standard`. Defaults to `Free`.
        """
        return pulumi.get(self, "sku_tier")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

