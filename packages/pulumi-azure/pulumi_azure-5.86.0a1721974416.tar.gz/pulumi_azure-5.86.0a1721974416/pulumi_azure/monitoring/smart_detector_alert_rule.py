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

__all__ = ['SmartDetectorAlertRuleArgs', 'SmartDetectorAlertRule']

@pulumi.input_type
class SmartDetectorAlertRuleArgs:
    def __init__(__self__, *,
                 action_group: pulumi.Input['SmartDetectorAlertRuleActionGroupArgs'],
                 detector_type: pulumi.Input[str],
                 frequency: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 scope_resource_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 severity: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 throttling_duration: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SmartDetectorAlertRule resource.
        :param pulumi.Input['SmartDetectorAlertRuleActionGroupArgs'] action_group: An `action_group` block as defined below.
        :param pulumi.Input[str] detector_type: Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible values are `FailureAnomaliesDetector`, `RequestPerformanceDegradationDetector`, `DependencyPerformanceDegradationDetector`, `ExceptionVolumeChangedDetector`, `TraceSeverityDetector`, `MemoryLeakDetector`.
        :param pulumi.Input[str] frequency: Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_resource_ids: Specifies the scopes of this Smart Detector Alert Rule.
        :param pulumi.Input[str] severity: Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
        :param pulumi.Input[str] description: Specifies a description for the Smart Detector Alert Rule.
        :param pulumi.Input[bool] enabled: Is the Smart Detector Alert Rule enabled? Defaults to `true`.
        :param pulumi.Input[str] name: Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] throttling_duration: Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
        """
        pulumi.set(__self__, "action_group", action_group)
        pulumi.set(__self__, "detector_type", detector_type)
        pulumi.set(__self__, "frequency", frequency)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "scope_resource_ids", scope_resource_ids)
        pulumi.set(__self__, "severity", severity)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if throttling_duration is not None:
            pulumi.set(__self__, "throttling_duration", throttling_duration)

    @property
    @pulumi.getter(name="actionGroup")
    def action_group(self) -> pulumi.Input['SmartDetectorAlertRuleActionGroupArgs']:
        """
        An `action_group` block as defined below.
        """
        return pulumi.get(self, "action_group")

    @action_group.setter
    def action_group(self, value: pulumi.Input['SmartDetectorAlertRuleActionGroupArgs']):
        pulumi.set(self, "action_group", value)

    @property
    @pulumi.getter(name="detectorType")
    def detector_type(self) -> pulumi.Input[str]:
        """
        Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible values are `FailureAnomaliesDetector`, `RequestPerformanceDegradationDetector`, `DependencyPerformanceDegradationDetector`, `ExceptionVolumeChangedDetector`, `TraceSeverityDetector`, `MemoryLeakDetector`.
        """
        return pulumi.get(self, "detector_type")

    @detector_type.setter
    def detector_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "detector_type", value)

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[str]:
        """
        Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: pulumi.Input[str]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="scopeResourceIds")
    def scope_resource_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Specifies the scopes of this Smart Detector Alert Rule.
        """
        return pulumi.get(self, "scope_resource_ids")

    @scope_resource_ids.setter
    def scope_resource_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "scope_resource_ids", value)

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Input[str]:
        """
        Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: pulumi.Input[str]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies a description for the Smart Detector Alert Rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Is the Smart Detector Alert Rule enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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

    @property
    @pulumi.getter(name="throttlingDuration")
    def throttling_duration(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
        """
        return pulumi.get(self, "throttling_duration")

    @throttling_duration.setter
    def throttling_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "throttling_duration", value)


@pulumi.input_type
class _SmartDetectorAlertRuleState:
    def __init__(__self__, *,
                 action_group: Optional[pulumi.Input['SmartDetectorAlertRuleActionGroupArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detector_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 severity: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 throttling_duration: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SmartDetectorAlertRule resources.
        :param pulumi.Input['SmartDetectorAlertRuleActionGroupArgs'] action_group: An `action_group` block as defined below.
        :param pulumi.Input[str] description: Specifies a description for the Smart Detector Alert Rule.
        :param pulumi.Input[str] detector_type: Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible values are `FailureAnomaliesDetector`, `RequestPerformanceDegradationDetector`, `DependencyPerformanceDegradationDetector`, `ExceptionVolumeChangedDetector`, `TraceSeverityDetector`, `MemoryLeakDetector`.
        :param pulumi.Input[bool] enabled: Is the Smart Detector Alert Rule enabled? Defaults to `true`.
        :param pulumi.Input[str] frequency: Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
        :param pulumi.Input[str] name: Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_resource_ids: Specifies the scopes of this Smart Detector Alert Rule.
        :param pulumi.Input[str] severity: Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] throttling_duration: Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
        """
        if action_group is not None:
            pulumi.set(__self__, "action_group", action_group)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if detector_type is not None:
            pulumi.set(__self__, "detector_type", detector_type)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if frequency is not None:
            pulumi.set(__self__, "frequency", frequency)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if scope_resource_ids is not None:
            pulumi.set(__self__, "scope_resource_ids", scope_resource_ids)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if throttling_duration is not None:
            pulumi.set(__self__, "throttling_duration", throttling_duration)

    @property
    @pulumi.getter(name="actionGroup")
    def action_group(self) -> Optional[pulumi.Input['SmartDetectorAlertRuleActionGroupArgs']]:
        """
        An `action_group` block as defined below.
        """
        return pulumi.get(self, "action_group")

    @action_group.setter
    def action_group(self, value: Optional[pulumi.Input['SmartDetectorAlertRuleActionGroupArgs']]):
        pulumi.set(self, "action_group", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies a description for the Smart Detector Alert Rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="detectorType")
    def detector_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible values are `FailureAnomaliesDetector`, `RequestPerformanceDegradationDetector`, `DependencyPerformanceDegradationDetector`, `ExceptionVolumeChangedDetector`, `TraceSeverityDetector`, `MemoryLeakDetector`.
        """
        return pulumi.get(self, "detector_type")

    @detector_type.setter
    def detector_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "detector_type", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Is the Smart Detector Alert Rule enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="scopeResourceIds")
    def scope_resource_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the scopes of this Smart Detector Alert Rule.
        """
        return pulumi.get(self, "scope_resource_ids")

    @scope_resource_ids.setter
    def scope_resource_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scope_resource_ids", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "severity", value)

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

    @property
    @pulumi.getter(name="throttlingDuration")
    def throttling_duration(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
        """
        return pulumi.get(self, "throttling_duration")

    @throttling_duration.setter
    def throttling_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "throttling_duration", value)


class SmartDetectorAlertRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_group: Optional[pulumi.Input[Union['SmartDetectorAlertRuleActionGroupArgs', 'SmartDetectorAlertRuleActionGroupArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detector_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 severity: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 throttling_duration: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Monitor Smart Detector Alert Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_insights = azure.appinsights.Insights("example",
            name="example-appinsights",
            location=example.location,
            resource_group_name=example.name,
            application_type="web")
        example_action_group = azure.monitoring.ActionGroup("example",
            name="example-action-group",
            resource_group_name=example.name,
            short_name="example")
        example_smart_detector_alert_rule = azure.monitoring.SmartDetectorAlertRule("example",
            name="example-smart-detector-alert-rule",
            resource_group_name=example.name,
            severity="Sev0",
            scope_resource_ids=[example_insights.id],
            frequency="PT1M",
            detector_type="FailureAnomaliesDetector",
            action_group={
                "ids": [example_action_group.id],
            })
        ```

        ## Import

        Monitor Smart Detector Alert Rule can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:monitoring/smartDetectorAlertRule:SmartDetectorAlertRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.AlertsManagement/smartDetectorAlertRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['SmartDetectorAlertRuleActionGroupArgs', 'SmartDetectorAlertRuleActionGroupArgsDict']] action_group: An `action_group` block as defined below.
        :param pulumi.Input[str] description: Specifies a description for the Smart Detector Alert Rule.
        :param pulumi.Input[str] detector_type: Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible values are `FailureAnomaliesDetector`, `RequestPerformanceDegradationDetector`, `DependencyPerformanceDegradationDetector`, `ExceptionVolumeChangedDetector`, `TraceSeverityDetector`, `MemoryLeakDetector`.
        :param pulumi.Input[bool] enabled: Is the Smart Detector Alert Rule enabled? Defaults to `true`.
        :param pulumi.Input[str] frequency: Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
        :param pulumi.Input[str] name: Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_resource_ids: Specifies the scopes of this Smart Detector Alert Rule.
        :param pulumi.Input[str] severity: Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] throttling_duration: Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SmartDetectorAlertRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Monitor Smart Detector Alert Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_insights = azure.appinsights.Insights("example",
            name="example-appinsights",
            location=example.location,
            resource_group_name=example.name,
            application_type="web")
        example_action_group = azure.monitoring.ActionGroup("example",
            name="example-action-group",
            resource_group_name=example.name,
            short_name="example")
        example_smart_detector_alert_rule = azure.monitoring.SmartDetectorAlertRule("example",
            name="example-smart-detector-alert-rule",
            resource_group_name=example.name,
            severity="Sev0",
            scope_resource_ids=[example_insights.id],
            frequency="PT1M",
            detector_type="FailureAnomaliesDetector",
            action_group={
                "ids": [example_action_group.id],
            })
        ```

        ## Import

        Monitor Smart Detector Alert Rule can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:monitoring/smartDetectorAlertRule:SmartDetectorAlertRule example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.AlertsManagement/smartDetectorAlertRules/rule1
        ```

        :param str resource_name: The name of the resource.
        :param SmartDetectorAlertRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SmartDetectorAlertRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_group: Optional[pulumi.Input[Union['SmartDetectorAlertRuleActionGroupArgs', 'SmartDetectorAlertRuleActionGroupArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detector_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 severity: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 throttling_duration: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SmartDetectorAlertRuleArgs.__new__(SmartDetectorAlertRuleArgs)

            if action_group is None and not opts.urn:
                raise TypeError("Missing required property 'action_group'")
            __props__.__dict__["action_group"] = action_group
            __props__.__dict__["description"] = description
            if detector_type is None and not opts.urn:
                raise TypeError("Missing required property 'detector_type'")
            __props__.__dict__["detector_type"] = detector_type
            __props__.__dict__["enabled"] = enabled
            if frequency is None and not opts.urn:
                raise TypeError("Missing required property 'frequency'")
            __props__.__dict__["frequency"] = frequency
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if scope_resource_ids is None and not opts.urn:
                raise TypeError("Missing required property 'scope_resource_ids'")
            __props__.__dict__["scope_resource_ids"] = scope_resource_ids
            if severity is None and not opts.urn:
                raise TypeError("Missing required property 'severity'")
            __props__.__dict__["severity"] = severity
            __props__.__dict__["tags"] = tags
            __props__.__dict__["throttling_duration"] = throttling_duration
        super(SmartDetectorAlertRule, __self__).__init__(
            'azure:monitoring/smartDetectorAlertRule:SmartDetectorAlertRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action_group: Optional[pulumi.Input[Union['SmartDetectorAlertRuleActionGroupArgs', 'SmartDetectorAlertRuleActionGroupArgsDict']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            detector_type: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            frequency: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            scope_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            severity: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            throttling_duration: Optional[pulumi.Input[str]] = None) -> 'SmartDetectorAlertRule':
        """
        Get an existing SmartDetectorAlertRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['SmartDetectorAlertRuleActionGroupArgs', 'SmartDetectorAlertRuleActionGroupArgsDict']] action_group: An `action_group` block as defined below.
        :param pulumi.Input[str] description: Specifies a description for the Smart Detector Alert Rule.
        :param pulumi.Input[str] detector_type: Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible values are `FailureAnomaliesDetector`, `RequestPerformanceDegradationDetector`, `DependencyPerformanceDegradationDetector`, `ExceptionVolumeChangedDetector`, `TraceSeverityDetector`, `MemoryLeakDetector`.
        :param pulumi.Input[bool] enabled: Is the Smart Detector Alert Rule enabled? Defaults to `true`.
        :param pulumi.Input[str] frequency: Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
        :param pulumi.Input[str] name: Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_resource_ids: Specifies the scopes of this Smart Detector Alert Rule.
        :param pulumi.Input[str] severity: Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] throttling_duration: Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SmartDetectorAlertRuleState.__new__(_SmartDetectorAlertRuleState)

        __props__.__dict__["action_group"] = action_group
        __props__.__dict__["description"] = description
        __props__.__dict__["detector_type"] = detector_type
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["frequency"] = frequency
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["scope_resource_ids"] = scope_resource_ids
        __props__.__dict__["severity"] = severity
        __props__.__dict__["tags"] = tags
        __props__.__dict__["throttling_duration"] = throttling_duration
        return SmartDetectorAlertRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionGroup")
    def action_group(self) -> pulumi.Output['outputs.SmartDetectorAlertRuleActionGroup']:
        """
        An `action_group` block as defined below.
        """
        return pulumi.get(self, "action_group")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies a description for the Smart Detector Alert Rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="detectorType")
    def detector_type(self) -> pulumi.Output[str]:
        """
        Specifies the Built-In Smart Detector type that this alert rule will use. Currently the only possible values are `FailureAnomaliesDetector`, `RequestPerformanceDegradationDetector`, `DependencyPerformanceDegradationDetector`, `ExceptionVolumeChangedDetector`, `TraceSeverityDetector`, `MemoryLeakDetector`.
        """
        return pulumi.get(self, "detector_type")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Is the Smart Detector Alert Rule enabled? Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[str]:
        """
        Specifies the frequency of this Smart Detector Alert Rule in ISO8601 format.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Monitor Smart Detector Alert Rule. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the resource group in which the Monitor Smart Detector Alert Rule should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="scopeResourceIds")
    def scope_resource_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Specifies the scopes of this Smart Detector Alert Rule.
        """
        return pulumi.get(self, "scope_resource_ids")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[str]:
        """
        Specifies the severity of this Smart Detector Alert Rule. Possible values are `Sev0`, `Sev1`, `Sev2`, `Sev3` or `Sev4`.
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="throttlingDuration")
    def throttling_duration(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the duration (in ISO8601 format) to wait before notifying on the alert rule again.
        """
        return pulumi.get(self, "throttling_duration")

