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

__all__ = ['ProfileArgs', 'Profile']

@pulumi.input_type
class ProfileArgs:
    def __init__(__self__, *,
                 dns_config: pulumi.Input['ProfileDnsConfigArgs'],
                 monitor_config: pulumi.Input['ProfileMonitorConfigArgs'],
                 resource_group_name: pulumi.Input[str],
                 traffic_routing_method: pulumi.Input[str],
                 max_return: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 profile_status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 traffic_view_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Profile resource.
        :param pulumi.Input['ProfileDnsConfigArgs'] dns_config: This block specifies the DNS configuration of the Profile. One `dns_config` block as defined below.
        :param pulumi.Input['ProfileMonitorConfigArgs'] monitor_config: This block specifies the Endpoint monitoring configuration for the Profile. One `monitor_config` block as defined below.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Traffic Manager profile. Changing this forces a new resource to be created.
        :param pulumi.Input[str] traffic_routing_method: Specifies the algorithm used to route traffic. Possible values are `Geographic`, `Weighted`, `Performance`, `Priority`, `Subnet` and `MultiValue`.
               * `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
               * `MultiValue` - All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type `External` and are specified as IPv4 or IPv6 addresses.
               * `Performance` - Traffic is routed via the User's closest Endpoint
               * `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
               * `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
               * `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
        :param pulumi.Input[int] max_return: The amount of endpoints to return for DNS queries to this Profile. Possible values range from `1` to `8`.
               
               > **NOTE:** `max_return` must be set when the `traffic_routing_method` is `MultiValue`.
        :param pulumi.Input[str] name: The name of the Traffic Manager profile. Changing this forces a new resource to be created.
        :param pulumi.Input[str] profile_status: The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] traffic_view_enabled: Indicates whether Traffic View is enabled for the Traffic Manager profile.
        """
        pulumi.set(__self__, "dns_config", dns_config)
        pulumi.set(__self__, "monitor_config", monitor_config)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "traffic_routing_method", traffic_routing_method)
        if max_return is not None:
            pulumi.set(__self__, "max_return", max_return)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if profile_status is not None:
            pulumi.set(__self__, "profile_status", profile_status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if traffic_view_enabled is not None:
            pulumi.set(__self__, "traffic_view_enabled", traffic_view_enabled)

    @property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> pulumi.Input['ProfileDnsConfigArgs']:
        """
        This block specifies the DNS configuration of the Profile. One `dns_config` block as defined below.
        """
        return pulumi.get(self, "dns_config")

    @dns_config.setter
    def dns_config(self, value: pulumi.Input['ProfileDnsConfigArgs']):
        pulumi.set(self, "dns_config", value)

    @property
    @pulumi.getter(name="monitorConfig")
    def monitor_config(self) -> pulumi.Input['ProfileMonitorConfigArgs']:
        """
        This block specifies the Endpoint monitoring configuration for the Profile. One `monitor_config` block as defined below.
        """
        return pulumi.get(self, "monitor_config")

    @monitor_config.setter
    def monitor_config(self, value: pulumi.Input['ProfileMonitorConfigArgs']):
        pulumi.set(self, "monitor_config", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which to create the Traffic Manager profile. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="trafficRoutingMethod")
    def traffic_routing_method(self) -> pulumi.Input[str]:
        """
        Specifies the algorithm used to route traffic. Possible values are `Geographic`, `Weighted`, `Performance`, `Priority`, `Subnet` and `MultiValue`.
        * `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
        * `MultiValue` - All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type `External` and are specified as IPv4 or IPv6 addresses.
        * `Performance` - Traffic is routed via the User's closest Endpoint
        * `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
        * `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
        * `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
        """
        return pulumi.get(self, "traffic_routing_method")

    @traffic_routing_method.setter
    def traffic_routing_method(self, value: pulumi.Input[str]):
        pulumi.set(self, "traffic_routing_method", value)

    @property
    @pulumi.getter(name="maxReturn")
    def max_return(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of endpoints to return for DNS queries to this Profile. Possible values range from `1` to `8`.

        > **NOTE:** `max_return` must be set when the `traffic_routing_method` is `MultiValue`.
        """
        return pulumi.get(self, "max_return")

    @max_return.setter
    def max_return(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_return", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Traffic Manager profile. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="profileStatus")
    def profile_status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
        """
        return pulumi.get(self, "profile_status")

    @profile_status.setter
    def profile_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_status", value)

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
    @pulumi.getter(name="trafficViewEnabled")
    def traffic_view_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether Traffic View is enabled for the Traffic Manager profile.
        """
        return pulumi.get(self, "traffic_view_enabled")

    @traffic_view_enabled.setter
    def traffic_view_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "traffic_view_enabled", value)


@pulumi.input_type
class _ProfileState:
    def __init__(__self__, *,
                 dns_config: Optional[pulumi.Input['ProfileDnsConfigArgs']] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 max_return: Optional[pulumi.Input[int]] = None,
                 monitor_config: Optional[pulumi.Input['ProfileMonitorConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 profile_status: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 traffic_routing_method: Optional[pulumi.Input[str]] = None,
                 traffic_view_enabled: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Profile resources.
        :param pulumi.Input['ProfileDnsConfigArgs'] dns_config: This block specifies the DNS configuration of the Profile. One `dns_config` block as defined below.
        :param pulumi.Input[str] fqdn: The FQDN of the created Profile.
        :param pulumi.Input[int] max_return: The amount of endpoints to return for DNS queries to this Profile. Possible values range from `1` to `8`.
               
               > **NOTE:** `max_return` must be set when the `traffic_routing_method` is `MultiValue`.
        :param pulumi.Input['ProfileMonitorConfigArgs'] monitor_config: This block specifies the Endpoint monitoring configuration for the Profile. One `monitor_config` block as defined below.
        :param pulumi.Input[str] name: The name of the Traffic Manager profile. Changing this forces a new resource to be created.
        :param pulumi.Input[str] profile_status: The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Traffic Manager profile. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] traffic_routing_method: Specifies the algorithm used to route traffic. Possible values are `Geographic`, `Weighted`, `Performance`, `Priority`, `Subnet` and `MultiValue`.
               * `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
               * `MultiValue` - All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type `External` and are specified as IPv4 or IPv6 addresses.
               * `Performance` - Traffic is routed via the User's closest Endpoint
               * `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
               * `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
               * `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
        :param pulumi.Input[bool] traffic_view_enabled: Indicates whether Traffic View is enabled for the Traffic Manager profile.
        """
        if dns_config is not None:
            pulumi.set(__self__, "dns_config", dns_config)
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if max_return is not None:
            pulumi.set(__self__, "max_return", max_return)
        if monitor_config is not None:
            pulumi.set(__self__, "monitor_config", monitor_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if profile_status is not None:
            pulumi.set(__self__, "profile_status", profile_status)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if traffic_routing_method is not None:
            pulumi.set(__self__, "traffic_routing_method", traffic_routing_method)
        if traffic_view_enabled is not None:
            pulumi.set(__self__, "traffic_view_enabled", traffic_view_enabled)

    @property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> Optional[pulumi.Input['ProfileDnsConfigArgs']]:
        """
        This block specifies the DNS configuration of the Profile. One `dns_config` block as defined below.
        """
        return pulumi.get(self, "dns_config")

    @dns_config.setter
    def dns_config(self, value: Optional[pulumi.Input['ProfileDnsConfigArgs']]):
        pulumi.set(self, "dns_config", value)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        The FQDN of the created Profile.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter(name="maxReturn")
    def max_return(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of endpoints to return for DNS queries to this Profile. Possible values range from `1` to `8`.

        > **NOTE:** `max_return` must be set when the `traffic_routing_method` is `MultiValue`.
        """
        return pulumi.get(self, "max_return")

    @max_return.setter
    def max_return(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_return", value)

    @property
    @pulumi.getter(name="monitorConfig")
    def monitor_config(self) -> Optional[pulumi.Input['ProfileMonitorConfigArgs']]:
        """
        This block specifies the Endpoint monitoring configuration for the Profile. One `monitor_config` block as defined below.
        """
        return pulumi.get(self, "monitor_config")

    @monitor_config.setter
    def monitor_config(self, value: Optional[pulumi.Input['ProfileMonitorConfigArgs']]):
        pulumi.set(self, "monitor_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Traffic Manager profile. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="profileStatus")
    def profile_status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
        """
        return pulumi.get(self, "profile_status")

    @profile_status.setter
    def profile_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_status", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which to create the Traffic Manager profile. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

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
    @pulumi.getter(name="trafficRoutingMethod")
    def traffic_routing_method(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the algorithm used to route traffic. Possible values are `Geographic`, `Weighted`, `Performance`, `Priority`, `Subnet` and `MultiValue`.
        * `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
        * `MultiValue` - All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type `External` and are specified as IPv4 or IPv6 addresses.
        * `Performance` - Traffic is routed via the User's closest Endpoint
        * `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
        * `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
        * `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
        """
        return pulumi.get(self, "traffic_routing_method")

    @traffic_routing_method.setter
    def traffic_routing_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "traffic_routing_method", value)

    @property
    @pulumi.getter(name="trafficViewEnabled")
    def traffic_view_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether Traffic View is enabled for the Traffic Manager profile.
        """
        return pulumi.get(self, "traffic_view_enabled")

    @traffic_view_enabled.setter
    def traffic_view_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "traffic_view_enabled", value)


warnings.warn("""azure.trafficmanager.Profile has been deprecated in favor of azure.network.TrafficManagerProfile""", DeprecationWarning)


class Profile(pulumi.CustomResource):
    warnings.warn("""azure.trafficmanager.Profile has been deprecated in favor of azure.network.TrafficManagerProfile""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_config: Optional[pulumi.Input[Union['ProfileDnsConfigArgs', 'ProfileDnsConfigArgsDict']]] = None,
                 max_return: Optional[pulumi.Input[int]] = None,
                 monitor_config: Optional[pulumi.Input[Union['ProfileMonitorConfigArgs', 'ProfileMonitorConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 profile_status: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 traffic_routing_method: Optional[pulumi.Input[str]] = None,
                 traffic_view_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages a Traffic Manager Profile to which multiple endpoints can be attached.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        server = random.RandomId("server",
            keepers={
                "azi_id": "1",
            },
            byte_length=8)
        example = azure.core.ResourceGroup("example",
            name="trafficmanagerProfile",
            location="West Europe")
        example_traffic_manager_profile = azure.network.TrafficManagerProfile("example",
            name=server.hex,
            resource_group_name=example.name,
            traffic_routing_method="Weighted",
            dns_config={
                "relative_name": server.hex,
                "ttl": 100,
            },
            monitor_config={
                "protocol": "HTTP",
                "port": 80,
                "path": "/",
                "interval_in_seconds": 30,
                "timeout_in_seconds": 9,
                "tolerated_number_of_failures": 3,
            },
            tags={
                "environment": "Production",
            })
        ```

        ## Import

        Traffic Manager Profiles can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:trafficmanager/profile:Profile exampleProfile /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/trafficManagerProfiles/mytrafficmanagerprofile1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ProfileDnsConfigArgs', 'ProfileDnsConfigArgsDict']] dns_config: This block specifies the DNS configuration of the Profile. One `dns_config` block as defined below.
        :param pulumi.Input[int] max_return: The amount of endpoints to return for DNS queries to this Profile. Possible values range from `1` to `8`.
               
               > **NOTE:** `max_return` must be set when the `traffic_routing_method` is `MultiValue`.
        :param pulumi.Input[Union['ProfileMonitorConfigArgs', 'ProfileMonitorConfigArgsDict']] monitor_config: This block specifies the Endpoint monitoring configuration for the Profile. One `monitor_config` block as defined below.
        :param pulumi.Input[str] name: The name of the Traffic Manager profile. Changing this forces a new resource to be created.
        :param pulumi.Input[str] profile_status: The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Traffic Manager profile. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] traffic_routing_method: Specifies the algorithm used to route traffic. Possible values are `Geographic`, `Weighted`, `Performance`, `Priority`, `Subnet` and `MultiValue`.
               * `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
               * `MultiValue` - All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type `External` and are specified as IPv4 or IPv6 addresses.
               * `Performance` - Traffic is routed via the User's closest Endpoint
               * `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
               * `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
               * `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
        :param pulumi.Input[bool] traffic_view_enabled: Indicates whether Traffic View is enabled for the Traffic Manager profile.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Traffic Manager Profile to which multiple endpoints can be attached.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_random as random

        server = random.RandomId("server",
            keepers={
                "azi_id": "1",
            },
            byte_length=8)
        example = azure.core.ResourceGroup("example",
            name="trafficmanagerProfile",
            location="West Europe")
        example_traffic_manager_profile = azure.network.TrafficManagerProfile("example",
            name=server.hex,
            resource_group_name=example.name,
            traffic_routing_method="Weighted",
            dns_config={
                "relative_name": server.hex,
                "ttl": 100,
            },
            monitor_config={
                "protocol": "HTTP",
                "port": 80,
                "path": "/",
                "interval_in_seconds": 30,
                "timeout_in_seconds": 9,
                "tolerated_number_of_failures": 3,
            },
            tags={
                "environment": "Production",
            })
        ```

        ## Import

        Traffic Manager Profiles can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:trafficmanager/profile:Profile exampleProfile /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/trafficManagerProfiles/mytrafficmanagerprofile1
        ```

        :param str resource_name: The name of the resource.
        :param ProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_config: Optional[pulumi.Input[Union['ProfileDnsConfigArgs', 'ProfileDnsConfigArgsDict']]] = None,
                 max_return: Optional[pulumi.Input[int]] = None,
                 monitor_config: Optional[pulumi.Input[Union['ProfileMonitorConfigArgs', 'ProfileMonitorConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 profile_status: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 traffic_routing_method: Optional[pulumi.Input[str]] = None,
                 traffic_view_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        pulumi.log.warn("""Profile is deprecated: azure.trafficmanager.Profile has been deprecated in favor of azure.network.TrafficManagerProfile""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProfileArgs.__new__(ProfileArgs)

            if dns_config is None and not opts.urn:
                raise TypeError("Missing required property 'dns_config'")
            __props__.__dict__["dns_config"] = dns_config
            __props__.__dict__["max_return"] = max_return
            if monitor_config is None and not opts.urn:
                raise TypeError("Missing required property 'monitor_config'")
            __props__.__dict__["monitor_config"] = monitor_config
            __props__.__dict__["name"] = name
            __props__.__dict__["profile_status"] = profile_status
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if traffic_routing_method is None and not opts.urn:
                raise TypeError("Missing required property 'traffic_routing_method'")
            __props__.__dict__["traffic_routing_method"] = traffic_routing_method
            __props__.__dict__["traffic_view_enabled"] = traffic_view_enabled
            __props__.__dict__["fqdn"] = None
        super(Profile, __self__).__init__(
            'azure:trafficmanager/profile:Profile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dns_config: Optional[pulumi.Input[Union['ProfileDnsConfigArgs', 'ProfileDnsConfigArgsDict']]] = None,
            fqdn: Optional[pulumi.Input[str]] = None,
            max_return: Optional[pulumi.Input[int]] = None,
            monitor_config: Optional[pulumi.Input[Union['ProfileMonitorConfigArgs', 'ProfileMonitorConfigArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            profile_status: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            traffic_routing_method: Optional[pulumi.Input[str]] = None,
            traffic_view_enabled: Optional[pulumi.Input[bool]] = None) -> 'Profile':
        """
        Get an existing Profile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ProfileDnsConfigArgs', 'ProfileDnsConfigArgsDict']] dns_config: This block specifies the DNS configuration of the Profile. One `dns_config` block as defined below.
        :param pulumi.Input[str] fqdn: The FQDN of the created Profile.
        :param pulumi.Input[int] max_return: The amount of endpoints to return for DNS queries to this Profile. Possible values range from `1` to `8`.
               
               > **NOTE:** `max_return` must be set when the `traffic_routing_method` is `MultiValue`.
        :param pulumi.Input[Union['ProfileMonitorConfigArgs', 'ProfileMonitorConfigArgsDict']] monitor_config: This block specifies the Endpoint monitoring configuration for the Profile. One `monitor_config` block as defined below.
        :param pulumi.Input[str] name: The name of the Traffic Manager profile. Changing this forces a new resource to be created.
        :param pulumi.Input[str] profile_status: The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Traffic Manager profile. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] traffic_routing_method: Specifies the algorithm used to route traffic. Possible values are `Geographic`, `Weighted`, `Performance`, `Priority`, `Subnet` and `MultiValue`.
               * `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
               * `MultiValue` - All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type `External` and are specified as IPv4 or IPv6 addresses.
               * `Performance` - Traffic is routed via the User's closest Endpoint
               * `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
               * `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
               * `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
        :param pulumi.Input[bool] traffic_view_enabled: Indicates whether Traffic View is enabled for the Traffic Manager profile.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProfileState.__new__(_ProfileState)

        __props__.__dict__["dns_config"] = dns_config
        __props__.__dict__["fqdn"] = fqdn
        __props__.__dict__["max_return"] = max_return
        __props__.__dict__["monitor_config"] = monitor_config
        __props__.__dict__["name"] = name
        __props__.__dict__["profile_status"] = profile_status
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["traffic_routing_method"] = traffic_routing_method
        __props__.__dict__["traffic_view_enabled"] = traffic_view_enabled
        return Profile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dnsConfig")
    def dns_config(self) -> pulumi.Output['outputs.ProfileDnsConfig']:
        """
        This block specifies the DNS configuration of the Profile. One `dns_config` block as defined below.
        """
        return pulumi.get(self, "dns_config")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        The FQDN of the created Profile.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="maxReturn")
    def max_return(self) -> pulumi.Output[Optional[int]]:
        """
        The amount of endpoints to return for DNS queries to this Profile. Possible values range from `1` to `8`.

        > **NOTE:** `max_return` must be set when the `traffic_routing_method` is `MultiValue`.
        """
        return pulumi.get(self, "max_return")

    @property
    @pulumi.getter(name="monitorConfig")
    def monitor_config(self) -> pulumi.Output['outputs.ProfileMonitorConfig']:
        """
        This block specifies the Endpoint monitoring configuration for the Profile. One `monitor_config` block as defined below.
        """
        return pulumi.get(self, "monitor_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Traffic Manager profile. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileStatus")
    def profile_status(self) -> pulumi.Output[str]:
        """
        The status of the profile, can be set to either `Enabled` or `Disabled`. Defaults to `Enabled`.
        """
        return pulumi.get(self, "profile_status")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the Traffic Manager profile. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trafficRoutingMethod")
    def traffic_routing_method(self) -> pulumi.Output[str]:
        """
        Specifies the algorithm used to route traffic. Possible values are `Geographic`, `Weighted`, `Performance`, `Priority`, `Subnet` and `MultiValue`.
        * `Geographic` - Traffic is routed based on Geographic regions specified in the Endpoint.
        * `MultiValue` - All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type `External` and are specified as IPv4 or IPv6 addresses.
        * `Performance` - Traffic is routed via the User's closest Endpoint
        * `Priority` - Traffic is routed to the Endpoint with the lowest `priority` value.
        * `Subnet` - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.
        * `Weighted` - Traffic is spread across Endpoints proportional to their `weight` value.
        """
        return pulumi.get(self, "traffic_routing_method")

    @property
    @pulumi.getter(name="trafficViewEnabled")
    def traffic_view_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether Traffic View is enabled for the Traffic Manager profile.
        """
        return pulumi.get(self, "traffic_view_enabled")

