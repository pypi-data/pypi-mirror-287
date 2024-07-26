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

__all__ = ['LogzMonitorArgs', 'LogzMonitor']

@pulumi.input_type
class LogzMonitorArgs:
    def __init__(__self__, *,
                 plan: pulumi.Input['LogzMonitorPlanArgs'],
                 resource_group_name: pulumi.Input[str],
                 user: pulumi.Input['LogzMonitorUserArgs'],
                 company_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 enterprise_app_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LogzMonitor resource.
        :param pulumi.Input['LogzMonitorPlanArgs'] plan: A `plan` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input['LogzMonitorUserArgs'] user: A `user` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] company_name: Name of the Logz organization. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[bool] enabled: Whether the resource monitoring is enabled? Defaults to `true`.
        :param pulumi.Input[str] enterprise_app_id: The ID of the Enterprise App. Changing this forces a new logz Monitor to be created.
               
               > **NOTE** Please follow [Set up Logz.io single sign-on](https://docs.microsoft.com/azure/partner-solutions/logzio/setup-sso) to create the ID of the Enterprise App.
        :param pulumi.Input[str] location: The Azure Region where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[str] name: The name which should be used for this logz Monitor. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the logz Monitor.
        """
        pulumi.set(__self__, "plan", plan)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "user", user)
        if company_name is not None:
            pulumi.set(__self__, "company_name", company_name)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if enterprise_app_id is not None:
            pulumi.set(__self__, "enterprise_app_id", enterprise_app_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Input['LogzMonitorPlanArgs']:
        """
        A `plan` block as defined below. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: pulumi.Input['LogzMonitorPlanArgs']):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input['LogzMonitorUserArgs']:
        """
        A `user` block as defined below. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input['LogzMonitorUserArgs']):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Logz organization. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "company_name")

    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "company_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the resource monitoring is enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="enterpriseAppId")
    def enterprise_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Enterprise App. Changing this forces a new logz Monitor to be created.

        > **NOTE** Please follow [Set up Logz.io single sign-on](https://docs.microsoft.com/azure/partner-solutions/logzio/setup-sso) to create the ID of the Enterprise App.
        """
        return pulumi.get(self, "enterprise_app_id")

    @enterprise_app_id.setter
    def enterprise_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enterprise_app_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this logz Monitor. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the logz Monitor.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _LogzMonitorState:
    def __init__(__self__, *,
                 company_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 enterprise_app_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logz_organization_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input['LogzMonitorPlanArgs']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 single_sign_on_url: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user: Optional[pulumi.Input['LogzMonitorUserArgs']] = None):
        """
        Input properties used for looking up and filtering LogzMonitor resources.
        :param pulumi.Input[str] company_name: Name of the Logz organization. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[bool] enabled: Whether the resource monitoring is enabled? Defaults to `true`.
        :param pulumi.Input[str] enterprise_app_id: The ID of the Enterprise App. Changing this forces a new logz Monitor to be created.
               
               > **NOTE** Please follow [Set up Logz.io single sign-on](https://docs.microsoft.com/azure/partner-solutions/logzio/setup-sso) to create the ID of the Enterprise App.
        :param pulumi.Input[str] location: The Azure Region where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[str] logz_organization_id: The ID associated with the logz organization of this logz Monitor.
        :param pulumi.Input[str] name: The name which should be used for this logz Monitor. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input['LogzMonitorPlanArgs'] plan: A `plan` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[str] single_sign_on_url: The single sign on url associated with the logz organization of this logz Monitor.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the logz Monitor.
        :param pulumi.Input['LogzMonitorUserArgs'] user: A `user` block as defined below. Changing this forces a new resource to be created.
        """
        if company_name is not None:
            pulumi.set(__self__, "company_name", company_name)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if enterprise_app_id is not None:
            pulumi.set(__self__, "enterprise_app_id", enterprise_app_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if logz_organization_id is not None:
            pulumi.set(__self__, "logz_organization_id", logz_organization_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if single_sign_on_url is not None:
            pulumi.set(__self__, "single_sign_on_url", single_sign_on_url)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Logz organization. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "company_name")

    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "company_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the resource monitoring is enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="enterpriseAppId")
    def enterprise_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Enterprise App. Changing this forces a new logz Monitor to be created.

        > **NOTE** Please follow [Set up Logz.io single sign-on](https://docs.microsoft.com/azure/partner-solutions/logzio/setup-sso) to create the ID of the Enterprise App.
        """
        return pulumi.get(self, "enterprise_app_id")

    @enterprise_app_id.setter
    def enterprise_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enterprise_app_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="logzOrganizationId")
    def logz_organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID associated with the logz organization of this logz Monitor.
        """
        return pulumi.get(self, "logz_organization_id")

    @logz_organization_id.setter
    def logz_organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logz_organization_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this logz Monitor. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['LogzMonitorPlanArgs']]:
        """
        A `plan` block as defined below. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['LogzMonitorPlanArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="singleSignOnUrl")
    def single_sign_on_url(self) -> Optional[pulumi.Input[str]]:
        """
        The single sign on url associated with the logz organization of this logz Monitor.
        """
        return pulumi.get(self, "single_sign_on_url")

    @single_sign_on_url.setter
    def single_sign_on_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "single_sign_on_url", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the logz Monitor.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input['LogzMonitorUserArgs']]:
        """
        A `user` block as defined below. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input['LogzMonitorUserArgs']]):
        pulumi.set(self, "user", value)


class LogzMonitor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 company_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 enterprise_app_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[Union['LogzMonitorPlanArgs', 'LogzMonitorPlanArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user: Optional[pulumi.Input[Union['LogzMonitorUserArgs', 'LogzMonitorUserArgsDict']]] = None,
                 __props__=None):
        """
        Manages a logz Monitor.

        !> **Note:** Logz REST API is being deprecated by Azure and new resources cannot be created. This resource will be removed in version 4.0 of the provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-logz",
            location="West Europe")
        example_logz_monitor = azure.monitoring.LogzMonitor("example",
            name="example-monitor",
            resource_group_name=example.name,
            location=example.location,
            plan={
                "billing_cycle": "MONTHLY",
                "effective_date": "2022-06-06T00:00:00Z",
                "usage_type": "COMMITTED",
            },
            user={
                "email": "user@example.com",
                "first_name": "Example",
                "last_name": "User",
                "phone_number": "+12313803556",
            })
        ```

        ## Import

        logz Monitors can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:monitoring/logzMonitor:LogzMonitor example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Logz/monitors/monitor1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] company_name: Name of the Logz organization. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[bool] enabled: Whether the resource monitoring is enabled? Defaults to `true`.
        :param pulumi.Input[str] enterprise_app_id: The ID of the Enterprise App. Changing this forces a new logz Monitor to be created.
               
               > **NOTE** Please follow [Set up Logz.io single sign-on](https://docs.microsoft.com/azure/partner-solutions/logzio/setup-sso) to create the ID of the Enterprise App.
        :param pulumi.Input[str] location: The Azure Region where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[str] name: The name which should be used for this logz Monitor. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[Union['LogzMonitorPlanArgs', 'LogzMonitorPlanArgsDict']] plan: A `plan` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the logz Monitor.
        :param pulumi.Input[Union['LogzMonitorUserArgs', 'LogzMonitorUserArgsDict']] user: A `user` block as defined below. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LogzMonitorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a logz Monitor.

        !> **Note:** Logz REST API is being deprecated by Azure and new resources cannot be created. This resource will be removed in version 4.0 of the provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-logz",
            location="West Europe")
        example_logz_monitor = azure.monitoring.LogzMonitor("example",
            name="example-monitor",
            resource_group_name=example.name,
            location=example.location,
            plan={
                "billing_cycle": "MONTHLY",
                "effective_date": "2022-06-06T00:00:00Z",
                "usage_type": "COMMITTED",
            },
            user={
                "email": "user@example.com",
                "first_name": "Example",
                "last_name": "User",
                "phone_number": "+12313803556",
            })
        ```

        ## Import

        logz Monitors can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:monitoring/logzMonitor:LogzMonitor example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Logz/monitors/monitor1
        ```

        :param str resource_name: The name of the resource.
        :param LogzMonitorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogzMonitorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 company_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 enterprise_app_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[Union['LogzMonitorPlanArgs', 'LogzMonitorPlanArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user: Optional[pulumi.Input[Union['LogzMonitorUserArgs', 'LogzMonitorUserArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogzMonitorArgs.__new__(LogzMonitorArgs)

            __props__.__dict__["company_name"] = company_name
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["enterprise_app_id"] = enterprise_app_id
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if plan is None and not opts.urn:
                raise TypeError("Missing required property 'plan'")
            __props__.__dict__["plan"] = plan
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if user is None and not opts.urn:
                raise TypeError("Missing required property 'user'")
            __props__.__dict__["user"] = user
            __props__.__dict__["logz_organization_id"] = None
            __props__.__dict__["single_sign_on_url"] = None
        super(LogzMonitor, __self__).__init__(
            'azure:monitoring/logzMonitor:LogzMonitor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            company_name: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            enterprise_app_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            logz_organization_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            plan: Optional[pulumi.Input[Union['LogzMonitorPlanArgs', 'LogzMonitorPlanArgsDict']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            single_sign_on_url: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            user: Optional[pulumi.Input[Union['LogzMonitorUserArgs', 'LogzMonitorUserArgsDict']]] = None) -> 'LogzMonitor':
        """
        Get an existing LogzMonitor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] company_name: Name of the Logz organization. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[bool] enabled: Whether the resource monitoring is enabled? Defaults to `true`.
        :param pulumi.Input[str] enterprise_app_id: The ID of the Enterprise App. Changing this forces a new logz Monitor to be created.
               
               > **NOTE** Please follow [Set up Logz.io single sign-on](https://docs.microsoft.com/azure/partner-solutions/logzio/setup-sso) to create the ID of the Enterprise App.
        :param pulumi.Input[str] location: The Azure Region where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[str] logz_organization_id: The ID associated with the logz organization of this logz Monitor.
        :param pulumi.Input[str] name: The name which should be used for this logz Monitor. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[Union['LogzMonitorPlanArgs', 'LogzMonitorPlanArgsDict']] plan: A `plan` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        :param pulumi.Input[str] single_sign_on_url: The single sign on url associated with the logz organization of this logz Monitor.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the logz Monitor.
        :param pulumi.Input[Union['LogzMonitorUserArgs', 'LogzMonitorUserArgsDict']] user: A `user` block as defined below. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LogzMonitorState.__new__(_LogzMonitorState)

        __props__.__dict__["company_name"] = company_name
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["enterprise_app_id"] = enterprise_app_id
        __props__.__dict__["location"] = location
        __props__.__dict__["logz_organization_id"] = logz_organization_id
        __props__.__dict__["name"] = name
        __props__.__dict__["plan"] = plan
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["single_sign_on_url"] = single_sign_on_url
        __props__.__dict__["tags"] = tags
        __props__.__dict__["user"] = user
        return LogzMonitor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the Logz organization. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "company_name")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the resource monitoring is enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="enterpriseAppId")
    def enterprise_app_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Enterprise App. Changing this forces a new logz Monitor to be created.

        > **NOTE** Please follow [Set up Logz.io single sign-on](https://docs.microsoft.com/azure/partner-solutions/logzio/setup-sso) to create the ID of the Enterprise App.
        """
        return pulumi.get(self, "enterprise_app_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logzOrganizationId")
    def logz_organization_id(self) -> pulumi.Output[str]:
        """
        The ID associated with the logz organization of this logz Monitor.
        """
        return pulumi.get(self, "logz_organization_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this logz Monitor. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output['outputs.LogzMonitorPlan']:
        """
        A `plan` block as defined below. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the logz Monitor should exist. Changing this forces a new logz Monitor to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="singleSignOnUrl")
    def single_sign_on_url(self) -> pulumi.Output[str]:
        """
        The single sign on url associated with the logz organization of this logz Monitor.
        """
        return pulumi.get(self, "single_sign_on_url")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the logz Monitor.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output['outputs.LogzMonitorUser']:
        """
        A `user` block as defined below. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "user")

