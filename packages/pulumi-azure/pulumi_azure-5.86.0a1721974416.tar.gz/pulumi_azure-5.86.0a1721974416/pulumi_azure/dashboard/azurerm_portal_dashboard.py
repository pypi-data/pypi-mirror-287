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
    'Azurerm_portal_dashboardResult',
    'AwaitableAzurerm_portal_dashboardResult',
    'azurerm_portal_dashboard',
    'azurerm_portal_dashboard_output',
]

warnings.warn("""azure.dashboard.azurerm_portal_dashboard has been deprecated in favor of azure.portal.getDashboard""", DeprecationWarning)

@pulumi.output_type
class Azurerm_portal_dashboardResult:
    """
    A collection of values returned by azurerm_portal_dashboard.
    """
    def __init__(__self__, dashboard_properties=None, display_name=None, id=None, location=None, name=None, resource_group_name=None, tags=None):
        if dashboard_properties and not isinstance(dashboard_properties, str):
            raise TypeError("Expected argument 'dashboard_properties' to be a str")
        pulumi.set(__self__, "dashboard_properties", dashboard_properties)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dashboardProperties")
    def dashboard_properties(self) -> str:
        """
        JSON data representing dashboard body.
        """
        return pulumi.get(self, "dashboard_properties")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region where the shared Azure Portal dashboard exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the shared Azure Portal dashboard.
        """
        return pulumi.get(self, "tags")


class AwaitableAzurerm_portal_dashboardResult(Azurerm_portal_dashboardResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return Azurerm_portal_dashboardResult(
            dashboard_properties=self.dashboard_properties,
            display_name=self.display_name,
            id=self.id,
            location=self.location,
            name=self.name,
            resource_group_name=self.resource_group_name,
            tags=self.tags)


def azurerm_portal_dashboard(dashboard_properties: Optional[str] = None,
                             display_name: Optional[str] = None,
                             name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableAzurerm_portal_dashboardResult:
    """
    Use this data source to access information about an existing shared dashboard in the Azure Portal. This is the data source of the `portal.Dashboard` resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.portal.get_dashboard(name="existing-dashboard",
        resource_group_name="dashboard-rg")
    pulumi.export("id", example_azurerm_dashboard["id"])
    ```


    :param str dashboard_properties: JSON data representing dashboard body.
    :param str display_name: Specifies the display name of the shared Azure Portal Dashboard.
    :param str name: Specifies the name of the shared Azure Portal Dashboard.
    :param str resource_group_name: Specifies the name of the resource group the shared Azure Portal Dashboard is located in.
    """
    pulumi.log.warn("""azurerm_portal_dashboard is deprecated: azure.dashboard.azurerm_portal_dashboard has been deprecated in favor of azure.portal.getDashboard""")
    __args__ = dict()
    __args__['dashboardProperties'] = dashboard_properties
    __args__['displayName'] = display_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:dashboard/azurerm_portal_dashboard:azurerm_portal_dashboard', __args__, opts=opts, typ=Azurerm_portal_dashboardResult).value

    return AwaitableAzurerm_portal_dashboardResult(
        dashboard_properties=pulumi.get(__ret__, 'dashboard_properties'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        resource_group_name=pulumi.get(__ret__, 'resource_group_name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(azurerm_portal_dashboard)
def azurerm_portal_dashboard_output(dashboard_properties: Optional[pulumi.Input[Optional[str]]] = None,
                                    display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                    name: Optional[pulumi.Input[Optional[str]]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[Azurerm_portal_dashboardResult]:
    """
    Use this data source to access information about an existing shared dashboard in the Azure Portal. This is the data source of the `portal.Dashboard` resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.portal.get_dashboard(name="existing-dashboard",
        resource_group_name="dashboard-rg")
    pulumi.export("id", example_azurerm_dashboard["id"])
    ```


    :param str dashboard_properties: JSON data representing dashboard body.
    :param str display_name: Specifies the display name of the shared Azure Portal Dashboard.
    :param str name: Specifies the name of the shared Azure Portal Dashboard.
    :param str resource_group_name: Specifies the name of the resource group the shared Azure Portal Dashboard is located in.
    """
    pulumi.log.warn("""azurerm_portal_dashboard is deprecated: azure.dashboard.azurerm_portal_dashboard has been deprecated in favor of azure.portal.getDashboard""")
    ...
