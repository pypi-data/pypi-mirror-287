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

__all__ = ['ApiTagArgs', 'ApiTag']

@pulumi.input_type
class ApiTagArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApiTag resource.
        :param pulumi.Input[str] api_id: The ID of the API Management API. Changing this forces a new API Management API Tag to be created.
        :param pulumi.Input[str] name: The name of the tag. It must be known in the API Management instance. Changing this forces a new API Management API Tag to be created.
        """
        pulumi.set(__self__, "api_id", api_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        The ID of the API Management API. Changing this forces a new API Management API Tag to be created.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the tag. It must be known in the API Management instance. Changing this forces a new API Management API Tag to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ApiTagState:
    def __init__(__self__, *,
                 api_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApiTag resources.
        :param pulumi.Input[str] api_id: The ID of the API Management API. Changing this forces a new API Management API Tag to be created.
        :param pulumi.Input[str] name: The name of the tag. It must be known in the API Management instance. Changing this forces a new API Management API Tag to be created.
        """
        if api_id is not None:
            pulumi.set(__self__, "api_id", api_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the API Management API. Changing this forces a new API Management API Tag to be created.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the tag. It must be known in the API Management instance. Changing this forces a new API Management API Tag to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ApiTag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages the Assignment of an API Management API Tag to an API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example = azure.apimanagement.get_service_output(name="example-apim",
            resource_group_name=example_resource_group.name)
        example_api = azure.apimanagement.Api("example",
            name="example-api",
            resource_group_name=example_resource_group.name,
            api_management_name=example.name,
            revision="1")
        example_tag = azure.apimanagement.Tag("example",
            api_management_id=example.id,
            name="example-tag")
        example_api_tag = azure.apimanagement.ApiTag("example",
            api_id=example_api.id,
            name=example_tag.name)
        ```

        ## Import

        API Management API Tags can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:apimanagement/apiTag:ApiTag example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.ApiManagement/service/service1/apis/api1/tags/tag1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The ID of the API Management API. Changing this forces a new API Management API Tag to be created.
        :param pulumi.Input[str] name: The name of the tag. It must be known in the API Management instance. Changing this forces a new API Management API Tag to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiTagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages the Assignment of an API Management API Tag to an API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example = azure.apimanagement.get_service_output(name="example-apim",
            resource_group_name=example_resource_group.name)
        example_api = azure.apimanagement.Api("example",
            name="example-api",
            resource_group_name=example_resource_group.name,
            api_management_name=example.name,
            revision="1")
        example_tag = azure.apimanagement.Tag("example",
            api_management_id=example.id,
            name="example-tag")
        example_api_tag = azure.apimanagement.ApiTag("example",
            api_id=example_api.id,
            name=example_tag.name)
        ```

        ## Import

        API Management API Tags can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:apimanagement/apiTag:ApiTag example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.ApiManagement/service/service1/apis/api1/tags/tag1
        ```

        :param str resource_name: The name of the resource.
        :param ApiTagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiTagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiTagArgs.__new__(ApiTagArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["name"] = name
        super(ApiTag, __self__).__init__(
            'azure:apimanagement/apiTag:ApiTag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ApiTag':
        """
        Get an existing ApiTag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The ID of the API Management API. Changing this forces a new API Management API Tag to be created.
        :param pulumi.Input[str] name: The name of the tag. It must be known in the API Management instance. Changing this forces a new API Management API Tag to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApiTagState.__new__(_ApiTagState)

        __props__.__dict__["api_id"] = api_id
        __props__.__dict__["name"] = name
        return ApiTag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        """
        The ID of the API Management API. Changing this forces a new API Management API Tag to be created.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the tag. It must be known in the API Management instance. Changing this forces a new API Management API Tag to be created.
        """
        return pulumi.get(self, "name")

