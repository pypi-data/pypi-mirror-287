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

__all__ = ['EdgeModuleArgs', 'EdgeModule']

@pulumi.input_type
class EdgeModuleArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 video_analyzer_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EdgeModule resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        :param pulumi.Input[str] video_analyzer_name: The name of the Video Analyzer in which to create the Edge Module. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "video_analyzer_name", video_analyzer_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which to create the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="videoAnalyzerName")
    def video_analyzer_name(self) -> pulumi.Input[str]:
        """
        The name of the Video Analyzer in which to create the Edge Module. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "video_analyzer_name")

    @video_analyzer_name.setter
    def video_analyzer_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "video_analyzer_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _EdgeModuleState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 video_analyzer_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EdgeModule resources.
        :param pulumi.Input[str] name: Specifies the name of the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        :param pulumi.Input[str] video_analyzer_name: The name of the Video Analyzer in which to create the Edge Module. Changing this forces a new resource to be created.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if video_analyzer_name is not None:
            pulumi.set(__self__, "video_analyzer_name", video_analyzer_name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which to create the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="videoAnalyzerName")
    def video_analyzer_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Video Analyzer in which to create the Edge Module. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "video_analyzer_name")

    @video_analyzer_name.setter
    def video_analyzer_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "video_analyzer_name", value)


class EdgeModule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 video_analyzer_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Video Analyzer Edge Module.

        !> Video Analyzer (Preview) is now Deprecated and will be Retired on 2022-11-30 - as such the `videoanalyzer.EdgeModule` resource is deprecated and will be removed in v4.0 of the AzureRM Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="video-analyzer-resources",
            location="West Europe")
        example_account = azure.storage.Account("example",
            name="examplestoracc",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_user_assigned_identity = azure.authorization.UserAssignedIdentity("example",
            name="exampleidentity",
            resource_group_name=example.name,
            location=example.location)
        contributor = azure.authorization.Assignment("contributor",
            scope=example_account.id,
            role_definition_name="Storage Blob Data Contributor",
            principal_id=example_user_assigned_identity.principal_id)
        reader = azure.authorization.Assignment("reader",
            scope=example_account.id,
            role_definition_name="Reader",
            principal_id=example_user_assigned_identity.principal_id)
        example_analyzer = azure.videoanalyzer.Analyzer("example",
            name="exampleanalyzer",
            location=example.location,
            resource_group_name=example.name,
            storage_account={
                "id": example_account.id,
                "user_assigned_identity_id": example_user_assigned_identity.id,
            },
            identity={
                "type": "UserAssigned",
                "identity_ids": [example_user_assigned_identity.id],
            },
            tags={
                "environment": "staging",
            },
            opts = pulumi.ResourceOptions(depends_on=[
                    example_user_assigned_identity,
                    contributor,
                    reader,
                ]))
        example_edge_module = azure.videoanalyzer.EdgeModule("example",
            name="example-edge-module",
            resource_group_name=example.name,
            video_analyzer_name=example_analyzer.name)
        ```

        ## Import

        Video Analyzer Edge Module can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:videoanalyzer/edgeModule:EdgeModule edge /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Media/videoAnalyzers/analyzer1/edgeModules/edge1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Specifies the name of the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        :param pulumi.Input[str] video_analyzer_name: The name of the Video Analyzer in which to create the Edge Module. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EdgeModuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Video Analyzer Edge Module.

        !> Video Analyzer (Preview) is now Deprecated and will be Retired on 2022-11-30 - as such the `videoanalyzer.EdgeModule` resource is deprecated and will be removed in v4.0 of the AzureRM Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="video-analyzer-resources",
            location="West Europe")
        example_account = azure.storage.Account("example",
            name="examplestoracc",
            resource_group_name=example.name,
            location=example.location,
            account_tier="Standard",
            account_replication_type="GRS")
        example_user_assigned_identity = azure.authorization.UserAssignedIdentity("example",
            name="exampleidentity",
            resource_group_name=example.name,
            location=example.location)
        contributor = azure.authorization.Assignment("contributor",
            scope=example_account.id,
            role_definition_name="Storage Blob Data Contributor",
            principal_id=example_user_assigned_identity.principal_id)
        reader = azure.authorization.Assignment("reader",
            scope=example_account.id,
            role_definition_name="Reader",
            principal_id=example_user_assigned_identity.principal_id)
        example_analyzer = azure.videoanalyzer.Analyzer("example",
            name="exampleanalyzer",
            location=example.location,
            resource_group_name=example.name,
            storage_account={
                "id": example_account.id,
                "user_assigned_identity_id": example_user_assigned_identity.id,
            },
            identity={
                "type": "UserAssigned",
                "identity_ids": [example_user_assigned_identity.id],
            },
            tags={
                "environment": "staging",
            },
            opts = pulumi.ResourceOptions(depends_on=[
                    example_user_assigned_identity,
                    contributor,
                    reader,
                ]))
        example_edge_module = azure.videoanalyzer.EdgeModule("example",
            name="example-edge-module",
            resource_group_name=example.name,
            video_analyzer_name=example_analyzer.name)
        ```

        ## Import

        Video Analyzer Edge Module can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:videoanalyzer/edgeModule:EdgeModule edge /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Media/videoAnalyzers/analyzer1/edgeModules/edge1
        ```

        :param str resource_name: The name of the resource.
        :param EdgeModuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EdgeModuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 video_analyzer_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EdgeModuleArgs.__new__(EdgeModuleArgs)

            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if video_analyzer_name is None and not opts.urn:
                raise TypeError("Missing required property 'video_analyzer_name'")
            __props__.__dict__["video_analyzer_name"] = video_analyzer_name
        super(EdgeModule, __self__).__init__(
            'azure:videoanalyzer/edgeModule:EdgeModule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            video_analyzer_name: Optional[pulumi.Input[str]] = None) -> 'EdgeModule':
        """
        Get an existing EdgeModule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Specifies the name of the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        :param pulumi.Input[str] video_analyzer_name: The name of the Video Analyzer in which to create the Edge Module. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EdgeModuleState.__new__(_EdgeModuleState)

        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["video_analyzer_name"] = video_analyzer_name
        return EdgeModule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the Video Analyzer Edge Module. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="videoAnalyzerName")
    def video_analyzer_name(self) -> pulumi.Output[str]:
        """
        The name of the Video Analyzer in which to create the Edge Module. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "video_analyzer_name")

