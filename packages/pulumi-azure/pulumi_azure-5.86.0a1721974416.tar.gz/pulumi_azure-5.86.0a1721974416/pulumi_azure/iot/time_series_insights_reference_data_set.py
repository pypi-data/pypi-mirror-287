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

__all__ = ['TimeSeriesInsightsReferenceDataSetArgs', 'TimeSeriesInsightsReferenceDataSet']

@pulumi.input_type
class TimeSeriesInsightsReferenceDataSetArgs:
    def __init__(__self__, *,
                 key_properties: pulumi.Input[Sequence[pulumi.Input['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs']]],
                 time_series_insights_environment_id: pulumi.Input[str],
                 data_string_comparison_behavior: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a TimeSeriesInsightsReferenceDataSet resource.
        :param pulumi.Input[Sequence[pulumi.Input['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs']]] key_properties: A `key_property` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] time_series_insights_environment_id: The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        :param pulumi.Input[str] data_string_comparison_behavior: The comparison behavior that will be used to compare keys. Valid values include `Ordinal` and `OrdinalIgnoreCase`. Defaults to `Ordinal`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created. Must be globally unique.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        pulumi.set(__self__, "key_properties", key_properties)
        pulumi.set(__self__, "time_series_insights_environment_id", time_series_insights_environment_id)
        if data_string_comparison_behavior is not None:
            pulumi.set(__self__, "data_string_comparison_behavior", data_string_comparison_behavior)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="keyProperties")
    def key_properties(self) -> pulumi.Input[Sequence[pulumi.Input['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs']]]:
        """
        A `key_property` block as defined below. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "key_properties")

    @key_properties.setter
    def key_properties(self, value: pulumi.Input[Sequence[pulumi.Input['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs']]]):
        pulumi.set(self, "key_properties", value)

    @property
    @pulumi.getter(name="timeSeriesInsightsEnvironmentId")
    def time_series_insights_environment_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "time_series_insights_environment_id")

    @time_series_insights_environment_id.setter
    def time_series_insights_environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_series_insights_environment_id", value)

    @property
    @pulumi.getter(name="dataStringComparisonBehavior")
    def data_string_comparison_behavior(self) -> Optional[pulumi.Input[str]]:
        """
        The comparison behavior that will be used to compare keys. Valid values include `Ordinal` and `OrdinalIgnoreCase`. Defaults to `Ordinal`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "data_string_comparison_behavior")

    @data_string_comparison_behavior.setter
    def data_string_comparison_behavior(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_string_comparison_behavior", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created. Must be globally unique.
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


@pulumi.input_type
class _TimeSeriesInsightsReferenceDataSetState:
    def __init__(__self__, *,
                 data_string_comparison_behavior: Optional[pulumi.Input[str]] = None,
                 key_properties: Optional[pulumi.Input[Sequence[pulumi.Input['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_series_insights_environment_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TimeSeriesInsightsReferenceDataSet resources.
        :param pulumi.Input[str] data_string_comparison_behavior: The comparison behavior that will be used to compare keys. Valid values include `Ordinal` and `OrdinalIgnoreCase`. Defaults to `Ordinal`. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs']]] key_properties: A `key_property` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created. Must be globally unique.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] time_series_insights_environment_id: The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        if data_string_comparison_behavior is not None:
            pulumi.set(__self__, "data_string_comparison_behavior", data_string_comparison_behavior)
        if key_properties is not None:
            pulumi.set(__self__, "key_properties", key_properties)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if time_series_insights_environment_id is not None:
            pulumi.set(__self__, "time_series_insights_environment_id", time_series_insights_environment_id)

    @property
    @pulumi.getter(name="dataStringComparisonBehavior")
    def data_string_comparison_behavior(self) -> Optional[pulumi.Input[str]]:
        """
        The comparison behavior that will be used to compare keys. Valid values include `Ordinal` and `OrdinalIgnoreCase`. Defaults to `Ordinal`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "data_string_comparison_behavior")

    @data_string_comparison_behavior.setter
    def data_string_comparison_behavior(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_string_comparison_behavior", value)

    @property
    @pulumi.getter(name="keyProperties")
    def key_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs']]]]:
        """
        A `key_property` block as defined below. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "key_properties")

    @key_properties.setter
    def key_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs']]]]):
        pulumi.set(self, "key_properties", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created. Must be globally unique.
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
    @pulumi.getter(name="timeSeriesInsightsEnvironmentId")
    def time_series_insights_environment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "time_series_insights_environment_id")

    @time_series_insights_environment_id.setter
    def time_series_insights_environment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_series_insights_environment_id", value)


class TimeSeriesInsightsReferenceDataSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_string_comparison_behavior: Optional[pulumi.Input[str]] = None,
                 key_properties: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs', 'TimeSeriesInsightsReferenceDataSetKeyPropertyArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_series_insights_environment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Azure IoT Time Series Insights Reference Data Set.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_time_series_insights_standard_environment = azure.iot.TimeSeriesInsightsStandardEnvironment("example",
            name="example",
            location=example.location,
            resource_group_name=example.name,
            sku_name="S1_1",
            data_retention_time="P30D")
        example_time_series_insights_reference_data_set = azure.iot.TimeSeriesInsightsReferenceDataSet("example",
            name="example",
            time_series_insights_environment_id=example_time_series_insights_standard_environment.id,
            location=example.location,
            key_properties=[{
                "name": "keyProperty1",
                "type": "String",
            }])
        ```

        ## Import

        Azure IoT Time Series Insights Reference Data Set can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:iot/timeSeriesInsightsReferenceDataSet:TimeSeriesInsightsReferenceDataSet example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.TimeSeriesInsights/environments/example/referenceDataSets/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_string_comparison_behavior: The comparison behavior that will be used to compare keys. Valid values include `Ordinal` and `OrdinalIgnoreCase`. Defaults to `Ordinal`. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[Union['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs', 'TimeSeriesInsightsReferenceDataSetKeyPropertyArgsDict']]]] key_properties: A `key_property` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created. Must be globally unique.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] time_series_insights_environment_id: The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TimeSeriesInsightsReferenceDataSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Azure IoT Time Series Insights Reference Data Set.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_time_series_insights_standard_environment = azure.iot.TimeSeriesInsightsStandardEnvironment("example",
            name="example",
            location=example.location,
            resource_group_name=example.name,
            sku_name="S1_1",
            data_retention_time="P30D")
        example_time_series_insights_reference_data_set = azure.iot.TimeSeriesInsightsReferenceDataSet("example",
            name="example",
            time_series_insights_environment_id=example_time_series_insights_standard_environment.id,
            location=example.location,
            key_properties=[{
                "name": "keyProperty1",
                "type": "String",
            }])
        ```

        ## Import

        Azure IoT Time Series Insights Reference Data Set can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:iot/timeSeriesInsightsReferenceDataSet:TimeSeriesInsightsReferenceDataSet example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.TimeSeriesInsights/environments/example/referenceDataSets/example
        ```

        :param str resource_name: The name of the resource.
        :param TimeSeriesInsightsReferenceDataSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TimeSeriesInsightsReferenceDataSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_string_comparison_behavior: Optional[pulumi.Input[str]] = None,
                 key_properties: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs', 'TimeSeriesInsightsReferenceDataSetKeyPropertyArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_series_insights_environment_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TimeSeriesInsightsReferenceDataSetArgs.__new__(TimeSeriesInsightsReferenceDataSetArgs)

            __props__.__dict__["data_string_comparison_behavior"] = data_string_comparison_behavior
            if key_properties is None and not opts.urn:
                raise TypeError("Missing required property 'key_properties'")
            __props__.__dict__["key_properties"] = key_properties
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            if time_series_insights_environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'time_series_insights_environment_id'")
            __props__.__dict__["time_series_insights_environment_id"] = time_series_insights_environment_id
        super(TimeSeriesInsightsReferenceDataSet, __self__).__init__(
            'azure:iot/timeSeriesInsightsReferenceDataSet:TimeSeriesInsightsReferenceDataSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            data_string_comparison_behavior: Optional[pulumi.Input[str]] = None,
            key_properties: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs', 'TimeSeriesInsightsReferenceDataSetKeyPropertyArgsDict']]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            time_series_insights_environment_id: Optional[pulumi.Input[str]] = None) -> 'TimeSeriesInsightsReferenceDataSet':
        """
        Get an existing TimeSeriesInsightsReferenceDataSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_string_comparison_behavior: The comparison behavior that will be used to compare keys. Valid values include `Ordinal` and `OrdinalIgnoreCase`. Defaults to `Ordinal`. Changing this forces a new resource to be created.
        :param pulumi.Input[Sequence[pulumi.Input[Union['TimeSeriesInsightsReferenceDataSetKeyPropertyArgs', 'TimeSeriesInsightsReferenceDataSetKeyPropertyArgsDict']]]] key_properties: A `key_property` block as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created. Must be globally unique.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] time_series_insights_environment_id: The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TimeSeriesInsightsReferenceDataSetState.__new__(_TimeSeriesInsightsReferenceDataSetState)

        __props__.__dict__["data_string_comparison_behavior"] = data_string_comparison_behavior
        __props__.__dict__["key_properties"] = key_properties
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["time_series_insights_environment_id"] = time_series_insights_environment_id
        return TimeSeriesInsightsReferenceDataSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataStringComparisonBehavior")
    def data_string_comparison_behavior(self) -> pulumi.Output[Optional[str]]:
        """
        The comparison behavior that will be used to compare keys. Valid values include `Ordinal` and `OrdinalIgnoreCase`. Defaults to `Ordinal`. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "data_string_comparison_behavior")

    @property
    @pulumi.getter(name="keyProperties")
    def key_properties(self) -> pulumi.Output[Sequence['outputs.TimeSeriesInsightsReferenceDataSetKeyProperty']]:
        """
        A `key_property` block as defined below. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "key_properties")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created. Must be globally unique.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeSeriesInsightsEnvironmentId")
    def time_series_insights_environment_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Azure IoT Time Series Insights Environment in which to create the Azure IoT Time Series Insights Reference Data Set. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "time_series_insights_environment_id")

