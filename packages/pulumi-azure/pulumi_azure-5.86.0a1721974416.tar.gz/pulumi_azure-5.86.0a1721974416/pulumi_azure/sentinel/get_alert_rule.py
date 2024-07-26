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
    'GetAlertRuleResult',
    'AwaitableGetAlertRuleResult',
    'get_alert_rule',
    'get_alert_rule_output',
]

@pulumi.output_type
class GetAlertRuleResult:
    """
    A collection of values returned by getAlertRule.
    """
    def __init__(__self__, id=None, log_analytics_workspace_id=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if log_analytics_workspace_id and not isinstance(log_analytics_workspace_id, str):
            raise TypeError("Expected argument 'log_analytics_workspace_id' to be a str")
        pulumi.set(__self__, "log_analytics_workspace_id", log_analytics_workspace_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> str:
        return pulumi.get(self, "log_analytics_workspace_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetAlertRuleResult(GetAlertRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAlertRuleResult(
            id=self.id,
            log_analytics_workspace_id=self.log_analytics_workspace_id,
            name=self.name)


def get_alert_rule(log_analytics_workspace_id: Optional[str] = None,
                   name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAlertRuleResult:
    """
    Use this data source to access information about an existing Sentinel Alert Rule.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.operationalinsights.get_analytics_workspace(name="example",
        resource_group_name="example-resources")
    example_get_alert_rule = azure.sentinel.get_alert_rule(name="existing",
        log_analytics_workspace_id=example.id)
    pulumi.export("id", example_get_alert_rule.id)
    ```


    :param str log_analytics_workspace_id: The ID of the Log Analytics Workspace this Sentinel Alert Rule belongs to.
    :param str name: The name which should be used for this Sentinel Alert Rule.
    """
    __args__ = dict()
    __args__['logAnalyticsWorkspaceId'] = log_analytics_workspace_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:sentinel/getAlertRule:getAlertRule', __args__, opts=opts, typ=GetAlertRuleResult).value

    return AwaitableGetAlertRuleResult(
        id=pulumi.get(__ret__, 'id'),
        log_analytics_workspace_id=pulumi.get(__ret__, 'log_analytics_workspace_id'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_alert_rule)
def get_alert_rule_output(log_analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                          name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAlertRuleResult]:
    """
    Use this data source to access information about an existing Sentinel Alert Rule.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.operationalinsights.get_analytics_workspace(name="example",
        resource_group_name="example-resources")
    example_get_alert_rule = azure.sentinel.get_alert_rule(name="existing",
        log_analytics_workspace_id=example.id)
    pulumi.export("id", example_get_alert_rule.id)
    ```


    :param str log_analytics_workspace_id: The ID of the Log Analytics Workspace this Sentinel Alert Rule belongs to.
    :param str name: The name which should be used for this Sentinel Alert Rule.
    """
    ...
