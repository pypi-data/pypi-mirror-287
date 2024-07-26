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

__all__ = ['HybridRunbookWorkerGroupArgs', 'HybridRunbookWorkerGroup']

@pulumi.input_type
class HybridRunbookWorkerGroupArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 credential_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HybridRunbookWorkerGroup resource.
        :param pulumi.Input[str] automation_account_name: The name of the Automation Account in which the Runbook Worker Group is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        :param pulumi.Input[str] credential_name: The name of resource type `automation.Credential` to use for hybrid worker.
        :param pulumi.Input[str] name: The name which should be used for this Automation Account Runbook Worker Group. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if credential_name is not None:
            pulumi.set(__self__, "credential_name", credential_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the Automation Account in which the Runbook Worker Group is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="credentialName")
    def credential_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of resource type `automation.Credential` to use for hybrid worker.
        """
        return pulumi.get(self, "credential_name")

    @credential_name.setter
    def credential_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credential_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Automation Account Runbook Worker Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _HybridRunbookWorkerGroupState:
    def __init__(__self__, *,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 credential_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HybridRunbookWorkerGroup resources.
        :param pulumi.Input[str] automation_account_name: The name of the Automation Account in which the Runbook Worker Group is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] credential_name: The name of resource type `automation.Credential` to use for hybrid worker.
        :param pulumi.Input[str] name: The name which should be used for this Automation Account Runbook Worker Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        if automation_account_name is not None:
            pulumi.set(__self__, "automation_account_name", automation_account_name)
        if credential_name is not None:
            pulumi.set(__self__, "credential_name", credential_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Automation Account in which the Runbook Worker Group is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter(name="credentialName")
    def credential_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of resource type `automation.Credential` to use for hybrid worker.
        """
        return pulumi.get(self, "credential_name")

    @credential_name.setter
    def credential_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credential_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Automation Account Runbook Worker Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


class HybridRunbookWorkerGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 credential_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Automation Hybrid Runbook Worker Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_account = azure.automation.Account("example",
            name="example-account",
            location=example.location,
            resource_group_name=example.name,
            sku_name="Basic")
        example_hybrid_runbook_worker_group = azure.automation.HybridRunbookWorkerGroup("example",
            name="example",
            resource_group_name=example.name,
            automation_account_name=example_account.name)
        ```

        ## Import

        Automations can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:automation/hybridRunbookWorkerGroup:HybridRunbookWorkerGroup example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.Automation/automationAccounts/account1/hybridRunbookWorkerGroups/grp1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the Automation Account in which the Runbook Worker Group is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] credential_name: The name of resource type `automation.Credential` to use for hybrid worker.
        :param pulumi.Input[str] name: The name which should be used for this Automation Account Runbook Worker Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HybridRunbookWorkerGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Automation Hybrid Runbook Worker Group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_account = azure.automation.Account("example",
            name="example-account",
            location=example.location,
            resource_group_name=example.name,
            sku_name="Basic")
        example_hybrid_runbook_worker_group = azure.automation.HybridRunbookWorkerGroup("example",
            name="example",
            resource_group_name=example.name,
            automation_account_name=example_account.name)
        ```

        ## Import

        Automations can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:automation/hybridRunbookWorkerGroup:HybridRunbookWorkerGroup example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.Automation/automationAccounts/account1/hybridRunbookWorkerGroups/grp1
        ```

        :param str resource_name: The name of the resource.
        :param HybridRunbookWorkerGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HybridRunbookWorkerGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 credential_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HybridRunbookWorkerGroupArgs.__new__(HybridRunbookWorkerGroupArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            __props__.__dict__["credential_name"] = credential_name
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
        super(HybridRunbookWorkerGroup, __self__).__init__(
            'azure:automation/hybridRunbookWorkerGroup:HybridRunbookWorkerGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            automation_account_name: Optional[pulumi.Input[str]] = None,
            credential_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'HybridRunbookWorkerGroup':
        """
        Get an existing HybridRunbookWorkerGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the Automation Account in which the Runbook Worker Group is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] credential_name: The name of resource type `automation.Credential` to use for hybrid worker.
        :param pulumi.Input[str] name: The name which should be used for this Automation Account Runbook Worker Group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HybridRunbookWorkerGroupState.__new__(_HybridRunbookWorkerGroupState)

        __props__.__dict__["automation_account_name"] = automation_account_name
        __props__.__dict__["credential_name"] = credential_name
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        return HybridRunbookWorkerGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Output[str]:
        """
        The name of the Automation Account in which the Runbook Worker Group is created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "automation_account_name")

    @property
    @pulumi.getter(name="credentialName")
    def credential_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of resource type `automation.Credential` to use for hybrid worker.
        """
        return pulumi.get(self, "credential_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Automation Account Runbook Worker Group. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Automation should exist. Changing this forces a new Automation to be created.
        """
        return pulumi.get(self, "resource_group_name")

