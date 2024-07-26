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

__all__ = ['ApplicationSecurityGroupAssociationArgs', 'ApplicationSecurityGroupAssociation']

@pulumi.input_type
class ApplicationSecurityGroupAssociationArgs:
    def __init__(__self__, *,
                 application_security_group_id: pulumi.Input[str],
                 private_endpoint_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ApplicationSecurityGroupAssociation resource.
        :param pulumi.Input[str] application_security_group_id: The id of application security group to associate. Changing this forces a new resource to be created.
        :param pulumi.Input[str] private_endpoint_id: The id of private endpoint to associate. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "application_security_group_id", application_security_group_id)
        pulumi.set(__self__, "private_endpoint_id", private_endpoint_id)

    @property
    @pulumi.getter(name="applicationSecurityGroupId")
    def application_security_group_id(self) -> pulumi.Input[str]:
        """
        The id of application security group to associate. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_security_group_id")

    @application_security_group_id.setter
    def application_security_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_security_group_id", value)

    @property
    @pulumi.getter(name="privateEndpointId")
    def private_endpoint_id(self) -> pulumi.Input[str]:
        """
        The id of private endpoint to associate. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "private_endpoint_id")

    @private_endpoint_id.setter
    def private_endpoint_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_endpoint_id", value)


@pulumi.input_type
class _ApplicationSecurityGroupAssociationState:
    def __init__(__self__, *,
                 application_security_group_id: Optional[pulumi.Input[str]] = None,
                 private_endpoint_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApplicationSecurityGroupAssociation resources.
        :param pulumi.Input[str] application_security_group_id: The id of application security group to associate. Changing this forces a new resource to be created.
        :param pulumi.Input[str] private_endpoint_id: The id of private endpoint to associate. Changing this forces a new resource to be created.
        """
        if application_security_group_id is not None:
            pulumi.set(__self__, "application_security_group_id", application_security_group_id)
        if private_endpoint_id is not None:
            pulumi.set(__self__, "private_endpoint_id", private_endpoint_id)

    @property
    @pulumi.getter(name="applicationSecurityGroupId")
    def application_security_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of application security group to associate. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_security_group_id")

    @application_security_group_id.setter
    def application_security_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_security_group_id", value)

    @property
    @pulumi.getter(name="privateEndpointId")
    def private_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of private endpoint to associate. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "private_endpoint_id")

    @private_endpoint_id.setter
    def private_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_endpoint_id", value)


class ApplicationSecurityGroupAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_security_group_id: Optional[pulumi.Input[str]] = None,
                 private_endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an association between Private Endpoint and Application Security Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_subscription()
        example = azure.core.ResourceGroup("example",
            name="example-PEASGAsso",
            location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("example",
            name="examplevnet",
            resource_group_name=example.name,
            location=example.location,
            address_spaces=["10.5.0.0/16"])
        service = azure.network.Subnet("service",
            name="examplenetservice",
            resource_group_name=example.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.5.1.0/24"],
            enforce_private_link_service_network_policies=True)
        endpoint = azure.network.Subnet("endpoint",
            name="examplenetendpoint",
            resource_group_name=example.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.5.2.0/24"],
            enforce_private_link_endpoint_network_policies=True)
        example_public_ip = azure.network.PublicIp("example",
            name="examplepip",
            sku="Standard",
            location=example.location,
            resource_group_name=example.name,
            allocation_method="Static")
        example_load_balancer = azure.lb.LoadBalancer("example",
            name="examplelb",
            sku="Standard",
            location=example.location,
            resource_group_name=example.name,
            frontend_ip_configurations=[{
                "name": example_public_ip.name,
                "public_ip_address_id": example_public_ip.id,
            }])
        example_link_service = azure.privatedns.LinkService("example",
            name="examplePLS",
            location=example.location,
            resource_group_name=example.name,
            auto_approval_subscription_ids=[current.subscription_id],
            visibility_subscription_ids=[current.subscription_id],
            nat_ip_configurations=[{
                "name": "primaryIpConfiguration",
                "primary": True,
                "subnet_id": service.id,
            }],
            load_balancer_frontend_ip_configuration_ids=[example_load_balancer.frontend_ip_configurations[0].id])
        example_endpoint = azure.privatelink.Endpoint("example",
            name="example-privatelink",
            resource_group_name=example.name,
            location=example.location,
            subnet_id=endpoint.id,
            private_service_connection={
                "name": example_link_service.name,
                "is_manual_connection": False,
                "private_connection_resource_id": example_link_service.id,
            })
        example_application_security_group = azure.network.ApplicationSecurityGroup("example",
            name="example",
            location=example.location,
            resource_group_name=example.name)
        example_application_security_group_association = azure.privatelink.ApplicationSecurityGroupAssociation("example",
            private_endpoint_id=example_endpoint.id,
            application_security_group_id=example_application_security_group.id)
        ```

        ## Import

        Associations between Private Endpoint and Application Security Group can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:privatelink/applicationSecurityGroupAssociation:ApplicationSecurityGroupAssociation association1 "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/privateEndpoints/endpoints1|/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/applicationSecurityGroups/securityGroup1",
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_security_group_id: The id of application security group to associate. Changing this forces a new resource to be created.
        :param pulumi.Input[str] private_endpoint_id: The id of private endpoint to associate. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationSecurityGroupAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an association between Private Endpoint and Application Security Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_subscription()
        example = azure.core.ResourceGroup("example",
            name="example-PEASGAsso",
            location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("example",
            name="examplevnet",
            resource_group_name=example.name,
            location=example.location,
            address_spaces=["10.5.0.0/16"])
        service = azure.network.Subnet("service",
            name="examplenetservice",
            resource_group_name=example.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.5.1.0/24"],
            enforce_private_link_service_network_policies=True)
        endpoint = azure.network.Subnet("endpoint",
            name="examplenetendpoint",
            resource_group_name=example.name,
            virtual_network_name=example_virtual_network.name,
            address_prefixes=["10.5.2.0/24"],
            enforce_private_link_endpoint_network_policies=True)
        example_public_ip = azure.network.PublicIp("example",
            name="examplepip",
            sku="Standard",
            location=example.location,
            resource_group_name=example.name,
            allocation_method="Static")
        example_load_balancer = azure.lb.LoadBalancer("example",
            name="examplelb",
            sku="Standard",
            location=example.location,
            resource_group_name=example.name,
            frontend_ip_configurations=[{
                "name": example_public_ip.name,
                "public_ip_address_id": example_public_ip.id,
            }])
        example_link_service = azure.privatedns.LinkService("example",
            name="examplePLS",
            location=example.location,
            resource_group_name=example.name,
            auto_approval_subscription_ids=[current.subscription_id],
            visibility_subscription_ids=[current.subscription_id],
            nat_ip_configurations=[{
                "name": "primaryIpConfiguration",
                "primary": True,
                "subnet_id": service.id,
            }],
            load_balancer_frontend_ip_configuration_ids=[example_load_balancer.frontend_ip_configurations[0].id])
        example_endpoint = azure.privatelink.Endpoint("example",
            name="example-privatelink",
            resource_group_name=example.name,
            location=example.location,
            subnet_id=endpoint.id,
            private_service_connection={
                "name": example_link_service.name,
                "is_manual_connection": False,
                "private_connection_resource_id": example_link_service.id,
            })
        example_application_security_group = azure.network.ApplicationSecurityGroup("example",
            name="example",
            location=example.location,
            resource_group_name=example.name)
        example_application_security_group_association = azure.privatelink.ApplicationSecurityGroupAssociation("example",
            private_endpoint_id=example_endpoint.id,
            application_security_group_id=example_application_security_group.id)
        ```

        ## Import

        Associations between Private Endpoint and Application Security Group can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:privatelink/applicationSecurityGroupAssociation:ApplicationSecurityGroupAssociation association1 "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/privateEndpoints/endpoints1|/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/applicationSecurityGroups/securityGroup1",
        ```

        :param str resource_name: The name of the resource.
        :param ApplicationSecurityGroupAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationSecurityGroupAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_security_group_id: Optional[pulumi.Input[str]] = None,
                 private_endpoint_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationSecurityGroupAssociationArgs.__new__(ApplicationSecurityGroupAssociationArgs)

            if application_security_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_security_group_id'")
            __props__.__dict__["application_security_group_id"] = application_security_group_id
            if private_endpoint_id is None and not opts.urn:
                raise TypeError("Missing required property 'private_endpoint_id'")
            __props__.__dict__["private_endpoint_id"] = private_endpoint_id
        super(ApplicationSecurityGroupAssociation, __self__).__init__(
            'azure:privatelink/applicationSecurityGroupAssociation:ApplicationSecurityGroupAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_security_group_id: Optional[pulumi.Input[str]] = None,
            private_endpoint_id: Optional[pulumi.Input[str]] = None) -> 'ApplicationSecurityGroupAssociation':
        """
        Get an existing ApplicationSecurityGroupAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_security_group_id: The id of application security group to associate. Changing this forces a new resource to be created.
        :param pulumi.Input[str] private_endpoint_id: The id of private endpoint to associate. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApplicationSecurityGroupAssociationState.__new__(_ApplicationSecurityGroupAssociationState)

        __props__.__dict__["application_security_group_id"] = application_security_group_id
        __props__.__dict__["private_endpoint_id"] = private_endpoint_id
        return ApplicationSecurityGroupAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationSecurityGroupId")
    def application_security_group_id(self) -> pulumi.Output[str]:
        """
        The id of application security group to associate. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "application_security_group_id")

    @property
    @pulumi.getter(name="privateEndpointId")
    def private_endpoint_id(self) -> pulumi.Output[str]:
        """
        The id of private endpoint to associate. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "private_endpoint_id")

