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

__all__ = ['CustomDomainArgs', 'CustomDomain']

@pulumi.input_type
class CustomDomainArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 web_pubsub_custom_certificate_id: pulumi.Input[str],
                 web_pubsub_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CustomDomain resource.
        :param pulumi.Input[str] domain_name: Specifies the custom domain name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
               
               > **NOTE:** Please ensure the custom domain name is included in the Subject Alternative Names of the selected Web PubSub Custom Certificate.
        :param pulumi.Input[str] web_pubsub_custom_certificate_id: Specifies the Web PubSub Custom Certificate ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        :param pulumi.Input[str] web_pubsub_id: Specifies the Web PubSub ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "web_pubsub_custom_certificate_id", web_pubsub_custom_certificate_id)
        pulumi.set(__self__, "web_pubsub_id", web_pubsub_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        Specifies the custom domain name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.

        > **NOTE:** Please ensure the custom domain name is included in the Subject Alternative Names of the selected Web PubSub Custom Certificate.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="webPubsubCustomCertificateId")
    def web_pubsub_custom_certificate_id(self) -> pulumi.Input[str]:
        """
        Specifies the Web PubSub Custom Certificate ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "web_pubsub_custom_certificate_id")

    @web_pubsub_custom_certificate_id.setter
    def web_pubsub_custom_certificate_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "web_pubsub_custom_certificate_id", value)

    @property
    @pulumi.getter(name="webPubsubId")
    def web_pubsub_id(self) -> pulumi.Input[str]:
        """
        Specifies the Web PubSub ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "web_pubsub_id")

    @web_pubsub_id.setter
    def web_pubsub_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "web_pubsub_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CustomDomainState:
    def __init__(__self__, *,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 web_pubsub_custom_certificate_id: Optional[pulumi.Input[str]] = None,
                 web_pubsub_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CustomDomain resources.
        :param pulumi.Input[str] domain_name: Specifies the custom domain name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
               
               > **NOTE:** Please ensure the custom domain name is included in the Subject Alternative Names of the selected Web PubSub Custom Certificate.
        :param pulumi.Input[str] name: Specifies the name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        :param pulumi.Input[str] web_pubsub_custom_certificate_id: Specifies the Web PubSub Custom Certificate ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        :param pulumi.Input[str] web_pubsub_id: Specifies the Web PubSub ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if web_pubsub_custom_certificate_id is not None:
            pulumi.set(__self__, "web_pubsub_custom_certificate_id", web_pubsub_custom_certificate_id)
        if web_pubsub_id is not None:
            pulumi.set(__self__, "web_pubsub_id", web_pubsub_id)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the custom domain name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.

        > **NOTE:** Please ensure the custom domain name is included in the Subject Alternative Names of the selected Web PubSub Custom Certificate.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="webPubsubCustomCertificateId")
    def web_pubsub_custom_certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Web PubSub Custom Certificate ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "web_pubsub_custom_certificate_id")

    @web_pubsub_custom_certificate_id.setter
    def web_pubsub_custom_certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "web_pubsub_custom_certificate_id", value)

    @property
    @pulumi.getter(name="webPubsubId")
    def web_pubsub_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Web PubSub ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "web_pubsub_id")

    @web_pubsub_id.setter
    def web_pubsub_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "web_pubsub_id", value)


class CustomDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 web_pubsub_custom_certificate_id: Optional[pulumi.Input[str]] = None,
                 web_pubsub_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Azure Web PubSub Custom Domain.

        ## Import

        Custom Domain for a Web PubSub service can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:webpubsub/customDomain:CustomDomain example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.SignalRService/webPubSub/webpubsub1/customDomains/customDomain1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Specifies the custom domain name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
               
               > **NOTE:** Please ensure the custom domain name is included in the Subject Alternative Names of the selected Web PubSub Custom Certificate.
        :param pulumi.Input[str] name: Specifies the name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        :param pulumi.Input[str] web_pubsub_custom_certificate_id: Specifies the Web PubSub Custom Certificate ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        :param pulumi.Input[str] web_pubsub_id: Specifies the Web PubSub ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Azure Web PubSub Custom Domain.

        ## Import

        Custom Domain for a Web PubSub service can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:webpubsub/customDomain:CustomDomain example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.SignalRService/webPubSub/webpubsub1/customDomains/customDomain1
        ```

        :param str resource_name: The name of the resource.
        :param CustomDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 web_pubsub_custom_certificate_id: Optional[pulumi.Input[str]] = None,
                 web_pubsub_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomDomainArgs.__new__(CustomDomainArgs)

            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["name"] = name
            if web_pubsub_custom_certificate_id is None and not opts.urn:
                raise TypeError("Missing required property 'web_pubsub_custom_certificate_id'")
            __props__.__dict__["web_pubsub_custom_certificate_id"] = web_pubsub_custom_certificate_id
            if web_pubsub_id is None and not opts.urn:
                raise TypeError("Missing required property 'web_pubsub_id'")
            __props__.__dict__["web_pubsub_id"] = web_pubsub_id
        super(CustomDomain, __self__).__init__(
            'azure:webpubsub/customDomain:CustomDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            web_pubsub_custom_certificate_id: Optional[pulumi.Input[str]] = None,
            web_pubsub_id: Optional[pulumi.Input[str]] = None) -> 'CustomDomain':
        """
        Get an existing CustomDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Specifies the custom domain name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
               
               > **NOTE:** Please ensure the custom domain name is included in the Subject Alternative Names of the selected Web PubSub Custom Certificate.
        :param pulumi.Input[str] name: Specifies the name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        :param pulumi.Input[str] web_pubsub_custom_certificate_id: Specifies the Web PubSub Custom Certificate ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        :param pulumi.Input[str] web_pubsub_id: Specifies the Web PubSub ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomDomainState.__new__(_CustomDomainState)

        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["name"] = name
        __props__.__dict__["web_pubsub_custom_certificate_id"] = web_pubsub_custom_certificate_id
        __props__.__dict__["web_pubsub_id"] = web_pubsub_id
        return CustomDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        Specifies the custom domain name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.

        > **NOTE:** Please ensure the custom domain name is included in the Subject Alternative Names of the selected Web PubSub Custom Certificate.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="webPubsubCustomCertificateId")
    def web_pubsub_custom_certificate_id(self) -> pulumi.Output[str]:
        """
        Specifies the Web PubSub Custom Certificate ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "web_pubsub_custom_certificate_id")

    @property
    @pulumi.getter(name="webPubsubId")
    def web_pubsub_id(self) -> pulumi.Output[str]:
        """
        Specifies the Web PubSub ID of the Web PubSub Custom Domain. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "web_pubsub_id")

