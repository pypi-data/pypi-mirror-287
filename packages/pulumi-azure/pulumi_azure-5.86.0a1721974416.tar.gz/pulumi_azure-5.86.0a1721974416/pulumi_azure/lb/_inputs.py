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
    'BackendAddressPoolAddressInboundNatRulePortMappingArgs',
    'BackendAddressPoolAddressInboundNatRulePortMappingArgsDict',
    'BackendAddressPoolTunnelInterfaceArgs',
    'BackendAddressPoolTunnelInterfaceArgsDict',
    'LoadBalancerFrontendIpConfigurationArgs',
    'LoadBalancerFrontendIpConfigurationArgsDict',
    'OutboundRuleFrontendIpConfigurationArgs',
    'OutboundRuleFrontendIpConfigurationArgsDict',
]

MYPY = False

if not MYPY:
    class BackendAddressPoolAddressInboundNatRulePortMappingArgsDict(TypedDict):
        backend_port: NotRequired[pulumi.Input[int]]
        """
        The Backend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        frontend_port: NotRequired[pulumi.Input[int]]
        """
        The Frontend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        inbound_nat_rule_name: NotRequired[pulumi.Input[str]]
        """
        The name of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
elif False:
    BackendAddressPoolAddressInboundNatRulePortMappingArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class BackendAddressPoolAddressInboundNatRulePortMappingArgs:
    def __init__(__self__, *,
                 backend_port: Optional[pulumi.Input[int]] = None,
                 frontend_port: Optional[pulumi.Input[int]] = None,
                 inbound_nat_rule_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[int] backend_port: The Backend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        :param pulumi.Input[int] frontend_port: The Frontend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        :param pulumi.Input[str] inbound_nat_rule_name: The name of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        if backend_port is not None:
            pulumi.set(__self__, "backend_port", backend_port)
        if frontend_port is not None:
            pulumi.set(__self__, "frontend_port", frontend_port)
        if inbound_nat_rule_name is not None:
            pulumi.set(__self__, "inbound_nat_rule_name", inbound_nat_rule_name)

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[pulumi.Input[int]]:
        """
        The Backend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        return pulumi.get(self, "backend_port")

    @backend_port.setter
    def backend_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backend_port", value)

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> Optional[pulumi.Input[int]]:
        """
        The Frontend Port of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        return pulumi.get(self, "frontend_port")

    @frontend_port.setter
    def frontend_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frontend_port", value)

    @property
    @pulumi.getter(name="inboundNatRuleName")
    def inbound_nat_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Load Balancing Inbound NAT Rules associated with this Backend Address Pool Address.
        """
        return pulumi.get(self, "inbound_nat_rule_name")

    @inbound_nat_rule_name.setter
    def inbound_nat_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inbound_nat_rule_name", value)


if not MYPY:
    class BackendAddressPoolTunnelInterfaceArgsDict(TypedDict):
        identifier: pulumi.Input[int]
        """
        The unique identifier of this Gateway Load Balancer Tunnel Interface.
        """
        port: pulumi.Input[int]
        """
        The port number that this Gateway Load Balancer Tunnel Interface listens to.
        """
        protocol: pulumi.Input[str]
        """
        The protocol used for this Gateway Load Balancer Tunnel Interface. Possible values are `None`, `Native` and `VXLAN`.
        """
        type: pulumi.Input[str]
        """
        The traffic type of this Gateway Load Balancer Tunnel Interface. Possible values are `None`, `Internal` and `External`.
        """
elif False:
    BackendAddressPoolTunnelInterfaceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class BackendAddressPoolTunnelInterfaceArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[int],
                 port: pulumi.Input[int],
                 protocol: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[int] identifier: The unique identifier of this Gateway Load Balancer Tunnel Interface.
        :param pulumi.Input[int] port: The port number that this Gateway Load Balancer Tunnel Interface listens to.
        :param pulumi.Input[str] protocol: The protocol used for this Gateway Load Balancer Tunnel Interface. Possible values are `None`, `Native` and `VXLAN`.
        :param pulumi.Input[str] type: The traffic type of this Gateway Load Balancer Tunnel Interface. Possible values are `None`, `Internal` and `External`.
        """
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[int]:
        """
        The unique identifier of this Gateway Load Balancer Tunnel Interface.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[int]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        The port number that this Gateway Load Balancer Tunnel Interface listens to.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        The protocol used for this Gateway Load Balancer Tunnel Interface. Possible values are `None`, `Native` and `VXLAN`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The traffic type of this Gateway Load Balancer Tunnel Interface. Possible values are `None`, `Internal` and `External`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


if not MYPY:
    class LoadBalancerFrontendIpConfigurationArgsDict(TypedDict):
        name: pulumi.Input[str]
        """
        Specifies the name of the frontend IP configuration.
        """
        gateway_load_balancer_frontend_ip_configuration_id: NotRequired[pulumi.Input[str]]
        """
        The Frontend IP Configuration ID of a Gateway SKU Load Balancer.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        The id of the Frontend IP Configuration.
        """
        inbound_nat_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The list of IDs of inbound rules that use this frontend IP.
        """
        load_balancer_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The list of IDs of load balancing rules that use this frontend IP.
        """
        outbound_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The list of IDs outbound rules that use this frontend IP.
        """
        private_ip_address: NotRequired[pulumi.Input[str]]
        """
        Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.
        """
        private_ip_address_allocation: NotRequired[pulumi.Input[str]]
        """
        The allocation method for the Private IP Address used by this Load Balancer. Possible values as `Dynamic` and `Static`.
        """
        private_ip_address_version: NotRequired[pulumi.Input[str]]
        """
        The version of IP that the Private IP Address is. Possible values are `IPv4` or `IPv6`.
        """
        public_ip_address_id: NotRequired[pulumi.Input[str]]
        """
        The ID of a Public IP Address which should be associated with the Load Balancer.
        """
        public_ip_prefix_id: NotRequired[pulumi.Input[str]]
        """
        The ID of a Public IP Prefix which should be associated with the Load Balancer. Public IP Prefix can only be used with outbound rules.
        """
        subnet_id: NotRequired[pulumi.Input[str]]
        """
        The ID of the Subnet which should be associated with the IP Configuration.
        """
        zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        Specifies a list of Availability Zones in which the IP Address for this Load Balancer should be located.

        > **NOTE:** Availability Zones are only supported with a [Standard SKU](https://docs.microsoft.com/azure/load-balancer/load-balancer-standard-availability-zones) and [in select regions](https://docs.microsoft.com/azure/availability-zones/az-overview) at this time.
        """
elif False:
    LoadBalancerFrontendIpConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class LoadBalancerFrontendIpConfigurationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 gateway_load_balancer_frontend_ip_configuration_id: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 inbound_nat_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 load_balancer_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 outbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 private_ip_address_allocation: Optional[pulumi.Input[str]] = None,
                 private_ip_address_version: Optional[pulumi.Input[str]] = None,
                 public_ip_address_id: Optional[pulumi.Input[str]] = None,
                 public_ip_prefix_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] name: Specifies the name of the frontend IP configuration.
        :param pulumi.Input[str] gateway_load_balancer_frontend_ip_configuration_id: The Frontend IP Configuration ID of a Gateway SKU Load Balancer.
        :param pulumi.Input[str] id: The id of the Frontend IP Configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] inbound_nat_rules: The list of IDs of inbound rules that use this frontend IP.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] load_balancer_rules: The list of IDs of load balancing rules that use this frontend IP.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] outbound_rules: The list of IDs outbound rules that use this frontend IP.
        :param pulumi.Input[str] private_ip_address: Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.
        :param pulumi.Input[str] private_ip_address_allocation: The allocation method for the Private IP Address used by this Load Balancer. Possible values as `Dynamic` and `Static`.
        :param pulumi.Input[str] private_ip_address_version: The version of IP that the Private IP Address is. Possible values are `IPv4` or `IPv6`.
        :param pulumi.Input[str] public_ip_address_id: The ID of a Public IP Address which should be associated with the Load Balancer.
        :param pulumi.Input[str] public_ip_prefix_id: The ID of a Public IP Prefix which should be associated with the Load Balancer. Public IP Prefix can only be used with outbound rules.
        :param pulumi.Input[str] subnet_id: The ID of the Subnet which should be associated with the IP Configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: Specifies a list of Availability Zones in which the IP Address for this Load Balancer should be located.
               
               > **NOTE:** Availability Zones are only supported with a [Standard SKU](https://docs.microsoft.com/azure/load-balancer/load-balancer-standard-availability-zones) and [in select regions](https://docs.microsoft.com/azure/availability-zones/az-overview) at this time.
        """
        pulumi.set(__self__, "name", name)
        if gateway_load_balancer_frontend_ip_configuration_id is not None:
            pulumi.set(__self__, "gateway_load_balancer_frontend_ip_configuration_id", gateway_load_balancer_frontend_ip_configuration_id)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if inbound_nat_rules is not None:
            pulumi.set(__self__, "inbound_nat_rules", inbound_nat_rules)
        if load_balancer_rules is not None:
            pulumi.set(__self__, "load_balancer_rules", load_balancer_rules)
        if outbound_rules is not None:
            pulumi.set(__self__, "outbound_rules", outbound_rules)
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)
        if private_ip_address_allocation is not None:
            pulumi.set(__self__, "private_ip_address_allocation", private_ip_address_allocation)
        if private_ip_address_version is not None:
            pulumi.set(__self__, "private_ip_address_version", private_ip_address_version)
        if public_ip_address_id is not None:
            pulumi.set(__self__, "public_ip_address_id", public_ip_address_id)
        if public_ip_prefix_id is not None:
            pulumi.set(__self__, "public_ip_prefix_id", public_ip_prefix_id)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the frontend IP configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="gatewayLoadBalancerFrontendIpConfigurationId")
    def gateway_load_balancer_frontend_ip_configuration_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Frontend IP Configuration ID of a Gateway SKU Load Balancer.
        """
        return pulumi.get(self, "gateway_load_balancer_frontend_ip_configuration_id")

    @gateway_load_balancer_frontend_ip_configuration_id.setter
    def gateway_load_balancer_frontend_ip_configuration_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_load_balancer_frontend_ip_configuration_id", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the Frontend IP Configuration.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="inboundNatRules")
    def inbound_nat_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of IDs of inbound rules that use this frontend IP.
        """
        return pulumi.get(self, "inbound_nat_rules")

    @inbound_nat_rules.setter
    def inbound_nat_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "inbound_nat_rules", value)

    @property
    @pulumi.getter(name="loadBalancerRules")
    def load_balancer_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of IDs of load balancing rules that use this frontend IP.
        """
        return pulumi.get(self, "load_balancer_rules")

    @load_balancer_rules.setter
    def load_balancer_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "load_balancer_rules", value)

    @property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of IDs outbound rules that use this frontend IP.
        """
        return pulumi.get(self, "outbound_rules")

    @outbound_rules.setter
    def outbound_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "outbound_rules", value)

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.
        """
        return pulumi.get(self, "private_ip_address")

    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address", value)

    @property
    @pulumi.getter(name="privateIpAddressAllocation")
    def private_ip_address_allocation(self) -> Optional[pulumi.Input[str]]:
        """
        The allocation method for the Private IP Address used by this Load Balancer. Possible values as `Dynamic` and `Static`.
        """
        return pulumi.get(self, "private_ip_address_allocation")

    @private_ip_address_allocation.setter
    def private_ip_address_allocation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address_allocation", value)

    @property
    @pulumi.getter(name="privateIpAddressVersion")
    def private_ip_address_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of IP that the Private IP Address is. Possible values are `IPv4` or `IPv6`.
        """
        return pulumi.get(self, "private_ip_address_version")

    @private_ip_address_version.setter
    def private_ip_address_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address_version", value)

    @property
    @pulumi.getter(name="publicIpAddressId")
    def public_ip_address_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a Public IP Address which should be associated with the Load Balancer.
        """
        return pulumi.get(self, "public_ip_address_id")

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ip_address_id", value)

    @property
    @pulumi.getter(name="publicIpPrefixId")
    def public_ip_prefix_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a Public IP Prefix which should be associated with the Load Balancer. Public IP Prefix can only be used with outbound rules.
        """
        return pulumi.get(self, "public_ip_prefix_id")

    @public_ip_prefix_id.setter
    def public_ip_prefix_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ip_prefix_id", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Subnet which should be associated with the IP Configuration.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of Availability Zones in which the IP Address for this Load Balancer should be located.

        > **NOTE:** Availability Zones are only supported with a [Standard SKU](https://docs.microsoft.com/azure/load-balancer/load-balancer-standard-availability-zones) and [in select regions](https://docs.microsoft.com/azure/availability-zones/az-overview) at this time.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


if not MYPY:
    class OutboundRuleFrontendIpConfigurationArgsDict(TypedDict):
        name: pulumi.Input[str]
        """
        The name of the Frontend IP Configuration.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        The ID of the Load Balancer Outbound Rule.
        """
elif False:
    OutboundRuleFrontendIpConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OutboundRuleFrontendIpConfigurationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: The name of the Frontend IP Configuration.
        :param pulumi.Input[str] id: The ID of the Load Balancer Outbound Rule.
        """
        pulumi.set(__self__, "name", name)
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the Frontend IP Configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Load Balancer Outbound Rule.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


