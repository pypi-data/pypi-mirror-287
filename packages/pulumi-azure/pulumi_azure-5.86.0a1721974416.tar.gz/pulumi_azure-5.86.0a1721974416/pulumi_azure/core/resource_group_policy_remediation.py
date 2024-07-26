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

__all__ = ['ResourceGroupPolicyRemediationArgs', 'ResourceGroupPolicyRemediation']

@pulumi.input_type
class ResourceGroupPolicyRemediationArgs:
    def __init__(__self__, *,
                 policy_assignment_id: pulumi.Input[str],
                 resource_group_id: pulumi.Input[str],
                 failure_percentage: Optional[pulumi.Input[float]] = None,
                 location_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parallel_deployments: Optional[pulumi.Input[int]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 resource_count: Optional[pulumi.Input[int]] = None,
                 resource_discovery_mode: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ResourceGroupPolicyRemediation resource.
        :param pulumi.Input[str] policy_assignment_id: The ID of the Policy Assignment that should be remediated.
        :param pulumi.Input[str] resource_group_id: The Resource Group ID at which the Policy Remediation should be applied. Changing this forces a new resource to be created.
        :param pulumi.Input[float] failure_percentage: A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] location_filters: A list of the resource locations that will be remediated.
        :param pulumi.Input[str] name: The name of the Policy Remediation. Changing this forces a new resource to be created.
        :param pulumi.Input[int] parallel_deployments: Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        :param pulumi.Input[str] policy_definition_id: The unique ID for the policy definition within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
               
               > **Note:** This property has been deprecated and will be removed in version 4.0 of the provider in favour of `policy_definition_reference_id`.
        :param pulumi.Input[str] policy_definition_reference_id: The unique ID for the policy definition reference within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        :param pulumi.Input[int] resource_count: Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        :param pulumi.Input[str] resource_discovery_mode: The way that resources to remediate are discovered. Possible values are `ExistingNonCompliant`, `ReEvaluateCompliance`. Defaults to `ExistingNonCompliant`.
        """
        pulumi.set(__self__, "policy_assignment_id", policy_assignment_id)
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if failure_percentage is not None:
            pulumi.set(__self__, "failure_percentage", failure_percentage)
        if location_filters is not None:
            pulumi.set(__self__, "location_filters", location_filters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parallel_deployments is not None:
            pulumi.set(__self__, "parallel_deployments", parallel_deployments)
        if policy_definition_id is not None:
            warnings.warn("""`policy_definition_id` will be removed in version 4.0 of the AzureRM Provider in favour of `policy_definition_reference_id`.""", DeprecationWarning)
            pulumi.log.warn("""policy_definition_id is deprecated: `policy_definition_id` will be removed in version 4.0 of the AzureRM Provider in favour of `policy_definition_reference_id`.""")
        if policy_definition_id is not None:
            pulumi.set(__self__, "policy_definition_id", policy_definition_id)
        if policy_definition_reference_id is not None:
            pulumi.set(__self__, "policy_definition_reference_id", policy_definition_reference_id)
        if resource_count is not None:
            pulumi.set(__self__, "resource_count", resource_count)
        if resource_discovery_mode is not None:
            pulumi.set(__self__, "resource_discovery_mode", resource_discovery_mode)

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Input[str]:
        """
        The ID of the Policy Assignment that should be remediated.
        """
        return pulumi.get(self, "policy_assignment_id")

    @policy_assignment_id.setter
    def policy_assignment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_assignment_id", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Input[str]:
        """
        The Resource Group ID at which the Policy Remediation should be applied. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter(name="failurePercentage")
    def failure_percentage(self) -> Optional[pulumi.Input[float]]:
        """
        A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        """
        return pulumi.get(self, "failure_percentage")

    @failure_percentage.setter
    def failure_percentage(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "failure_percentage", value)

    @property
    @pulumi.getter(name="locationFilters")
    def location_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of the resource locations that will be remediated.
        """
        return pulumi.get(self, "location_filters")

    @location_filters.setter
    def location_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "location_filters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Policy Remediation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parallelDeployments")
    def parallel_deployments(self) -> Optional[pulumi.Input[int]]:
        """
        Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        """
        return pulumi.get(self, "parallel_deployments")

    @parallel_deployments.setter
    def parallel_deployments(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "parallel_deployments", value)

    @property
    @pulumi.getter(name="policyDefinitionId")
    @_utilities.deprecated("""`policy_definition_id` will be removed in version 4.0 of the AzureRM Provider in favour of `policy_definition_reference_id`.""")
    def policy_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID for the policy definition within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.

        > **Note:** This property has been deprecated and will be removed in version 4.0 of the provider in favour of `policy_definition_reference_id`.
        """
        return pulumi.get(self, "policy_definition_id")

    @policy_definition_id.setter
    def policy_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_id", value)

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID for the policy definition reference within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @policy_definition_reference_id.setter
    def policy_definition_reference_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_reference_id", value)

    @property
    @pulumi.getter(name="resourceCount")
    def resource_count(self) -> Optional[pulumi.Input[int]]:
        """
        Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        """
        return pulumi.get(self, "resource_count")

    @resource_count.setter
    def resource_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "resource_count", value)

    @property
    @pulumi.getter(name="resourceDiscoveryMode")
    def resource_discovery_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The way that resources to remediate are discovered. Possible values are `ExistingNonCompliant`, `ReEvaluateCompliance`. Defaults to `ExistingNonCompliant`.
        """
        return pulumi.get(self, "resource_discovery_mode")

    @resource_discovery_mode.setter
    def resource_discovery_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_discovery_mode", value)


@pulumi.input_type
class _ResourceGroupPolicyRemediationState:
    def __init__(__self__, *,
                 failure_percentage: Optional[pulumi.Input[float]] = None,
                 location_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parallel_deployments: Optional[pulumi.Input[int]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 resource_count: Optional[pulumi.Input[int]] = None,
                 resource_discovery_mode: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ResourceGroupPolicyRemediation resources.
        :param pulumi.Input[float] failure_percentage: A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] location_filters: A list of the resource locations that will be remediated.
        :param pulumi.Input[str] name: The name of the Policy Remediation. Changing this forces a new resource to be created.
        :param pulumi.Input[int] parallel_deployments: Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        :param pulumi.Input[str] policy_assignment_id: The ID of the Policy Assignment that should be remediated.
        :param pulumi.Input[str] policy_definition_id: The unique ID for the policy definition within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
               
               > **Note:** This property has been deprecated and will be removed in version 4.0 of the provider in favour of `policy_definition_reference_id`.
        :param pulumi.Input[str] policy_definition_reference_id: The unique ID for the policy definition reference within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        :param pulumi.Input[int] resource_count: Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        :param pulumi.Input[str] resource_discovery_mode: The way that resources to remediate are discovered. Possible values are `ExistingNonCompliant`, `ReEvaluateCompliance`. Defaults to `ExistingNonCompliant`.
        :param pulumi.Input[str] resource_group_id: The Resource Group ID at which the Policy Remediation should be applied. Changing this forces a new resource to be created.
        """
        if failure_percentage is not None:
            pulumi.set(__self__, "failure_percentage", failure_percentage)
        if location_filters is not None:
            pulumi.set(__self__, "location_filters", location_filters)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parallel_deployments is not None:
            pulumi.set(__self__, "parallel_deployments", parallel_deployments)
        if policy_assignment_id is not None:
            pulumi.set(__self__, "policy_assignment_id", policy_assignment_id)
        if policy_definition_id is not None:
            warnings.warn("""`policy_definition_id` will be removed in version 4.0 of the AzureRM Provider in favour of `policy_definition_reference_id`.""", DeprecationWarning)
            pulumi.log.warn("""policy_definition_id is deprecated: `policy_definition_id` will be removed in version 4.0 of the AzureRM Provider in favour of `policy_definition_reference_id`.""")
        if policy_definition_id is not None:
            pulumi.set(__self__, "policy_definition_id", policy_definition_id)
        if policy_definition_reference_id is not None:
            pulumi.set(__self__, "policy_definition_reference_id", policy_definition_reference_id)
        if resource_count is not None:
            pulumi.set(__self__, "resource_count", resource_count)
        if resource_discovery_mode is not None:
            pulumi.set(__self__, "resource_discovery_mode", resource_discovery_mode)
        if resource_group_id is not None:
            pulumi.set(__self__, "resource_group_id", resource_group_id)

    @property
    @pulumi.getter(name="failurePercentage")
    def failure_percentage(self) -> Optional[pulumi.Input[float]]:
        """
        A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        """
        return pulumi.get(self, "failure_percentage")

    @failure_percentage.setter
    def failure_percentage(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "failure_percentage", value)

    @property
    @pulumi.getter(name="locationFilters")
    def location_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of the resource locations that will be remediated.
        """
        return pulumi.get(self, "location_filters")

    @location_filters.setter
    def location_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "location_filters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Policy Remediation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parallelDeployments")
    def parallel_deployments(self) -> Optional[pulumi.Input[int]]:
        """
        Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        """
        return pulumi.get(self, "parallel_deployments")

    @parallel_deployments.setter
    def parallel_deployments(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "parallel_deployments", value)

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Policy Assignment that should be remediated.
        """
        return pulumi.get(self, "policy_assignment_id")

    @policy_assignment_id.setter
    def policy_assignment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_assignment_id", value)

    @property
    @pulumi.getter(name="policyDefinitionId")
    @_utilities.deprecated("""`policy_definition_id` will be removed in version 4.0 of the AzureRM Provider in favour of `policy_definition_reference_id`.""")
    def policy_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID for the policy definition within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.

        > **Note:** This property has been deprecated and will be removed in version 4.0 of the provider in favour of `policy_definition_reference_id`.
        """
        return pulumi.get(self, "policy_definition_id")

    @policy_definition_id.setter
    def policy_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_id", value)

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID for the policy definition reference within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @policy_definition_reference_id.setter
    def policy_definition_reference_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_reference_id", value)

    @property
    @pulumi.getter(name="resourceCount")
    def resource_count(self) -> Optional[pulumi.Input[int]]:
        """
        Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        """
        return pulumi.get(self, "resource_count")

    @resource_count.setter
    def resource_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "resource_count", value)

    @property
    @pulumi.getter(name="resourceDiscoveryMode")
    def resource_discovery_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The way that resources to remediate are discovered. Possible values are `ExistingNonCompliant`, `ReEvaluateCompliance`. Defaults to `ExistingNonCompliant`.
        """
        return pulumi.get(self, "resource_discovery_mode")

    @resource_discovery_mode.setter
    def resource_discovery_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_discovery_mode", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Resource Group ID at which the Policy Remediation should be applied. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)


class ResourceGroupPolicyRemediation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 failure_percentage: Optional[pulumi.Input[float]] = None,
                 location_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parallel_deployments: Optional[pulumi.Input[int]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 resource_count: Optional[pulumi.Input[int]] = None,
                 resource_discovery_mode: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Azure Resource Group Policy Remediation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_definition = azure.policy.Definition("example",
            name="my-policy-definition",
            policy_type="Custom",
            mode="All",
            display_name="my-policy-definition",
            policy_rule=\"\"\"    {
            "if": {
              "not": {
                "field": "location",
                "in": "[parameters('allowedLocations')]"
              }
            },
            "then": {
              "effect": "audit"
            }
          }
        \"\"\",
            parameters=\"\"\"    {
            "allowedLocations": {
              "type": "Array",
              "metadata": {
                "description": "The list of allowed locations for resources.",
                "displayName": "Allowed locations",
                "strongType": "location"
              }
            }
          }
        \"\"\")
        example_resource_group_policy_assignment = azure.core.ResourceGroupPolicyAssignment("example",
            name="example",
            resource_group_id=example.id,
            policy_definition_id=example_definition.id)
        example_resource_group_policy_remediation = azure.core.ResourceGroupPolicyRemediation("example",
            name="example-policy-remediation",
            resource_group_id=example.id,
            policy_assignment_id=example_resource_group_policy_assignment.id,
            location_filters=["West Europe"])
        ```

        ## Import

        Policy Remediations can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:core/resourceGroupPolicyRemediation:ResourceGroupPolicyRemediation example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.PolicyInsights/remediations/remediation1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] failure_percentage: A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] location_filters: A list of the resource locations that will be remediated.
        :param pulumi.Input[str] name: The name of the Policy Remediation. Changing this forces a new resource to be created.
        :param pulumi.Input[int] parallel_deployments: Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        :param pulumi.Input[str] policy_assignment_id: The ID of the Policy Assignment that should be remediated.
        :param pulumi.Input[str] policy_definition_id: The unique ID for the policy definition within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
               
               > **Note:** This property has been deprecated and will be removed in version 4.0 of the provider in favour of `policy_definition_reference_id`.
        :param pulumi.Input[str] policy_definition_reference_id: The unique ID for the policy definition reference within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        :param pulumi.Input[int] resource_count: Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        :param pulumi.Input[str] resource_discovery_mode: The way that resources to remediate are discovered. Possible values are `ExistingNonCompliant`, `ReEvaluateCompliance`. Defaults to `ExistingNonCompliant`.
        :param pulumi.Input[str] resource_group_id: The Resource Group ID at which the Policy Remediation should be applied. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceGroupPolicyRemediationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Azure Resource Group Policy Remediation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_definition = azure.policy.Definition("example",
            name="my-policy-definition",
            policy_type="Custom",
            mode="All",
            display_name="my-policy-definition",
            policy_rule=\"\"\"    {
            "if": {
              "not": {
                "field": "location",
                "in": "[parameters('allowedLocations')]"
              }
            },
            "then": {
              "effect": "audit"
            }
          }
        \"\"\",
            parameters=\"\"\"    {
            "allowedLocations": {
              "type": "Array",
              "metadata": {
                "description": "The list of allowed locations for resources.",
                "displayName": "Allowed locations",
                "strongType": "location"
              }
            }
          }
        \"\"\")
        example_resource_group_policy_assignment = azure.core.ResourceGroupPolicyAssignment("example",
            name="example",
            resource_group_id=example.id,
            policy_definition_id=example_definition.id)
        example_resource_group_policy_remediation = azure.core.ResourceGroupPolicyRemediation("example",
            name="example-policy-remediation",
            resource_group_id=example.id,
            policy_assignment_id=example_resource_group_policy_assignment.id,
            location_filters=["West Europe"])
        ```

        ## Import

        Policy Remediations can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:core/resourceGroupPolicyRemediation:ResourceGroupPolicyRemediation example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.PolicyInsights/remediations/remediation1
        ```

        :param str resource_name: The name of the resource.
        :param ResourceGroupPolicyRemediationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceGroupPolicyRemediationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 failure_percentage: Optional[pulumi.Input[float]] = None,
                 location_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parallel_deployments: Optional[pulumi.Input[int]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 resource_count: Optional[pulumi.Input[int]] = None,
                 resource_discovery_mode: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceGroupPolicyRemediationArgs.__new__(ResourceGroupPolicyRemediationArgs)

            __props__.__dict__["failure_percentage"] = failure_percentage
            __props__.__dict__["location_filters"] = location_filters
            __props__.__dict__["name"] = name
            __props__.__dict__["parallel_deployments"] = parallel_deployments
            if policy_assignment_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_assignment_id'")
            __props__.__dict__["policy_assignment_id"] = policy_assignment_id
            __props__.__dict__["policy_definition_id"] = policy_definition_id
            __props__.__dict__["policy_definition_reference_id"] = policy_definition_reference_id
            __props__.__dict__["resource_count"] = resource_count
            __props__.__dict__["resource_discovery_mode"] = resource_discovery_mode
            if resource_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_id'")
            __props__.__dict__["resource_group_id"] = resource_group_id
        super(ResourceGroupPolicyRemediation, __self__).__init__(
            'azure:core/resourceGroupPolicyRemediation:ResourceGroupPolicyRemediation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            failure_percentage: Optional[pulumi.Input[float]] = None,
            location_filters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parallel_deployments: Optional[pulumi.Input[int]] = None,
            policy_assignment_id: Optional[pulumi.Input[str]] = None,
            policy_definition_id: Optional[pulumi.Input[str]] = None,
            policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
            resource_count: Optional[pulumi.Input[int]] = None,
            resource_discovery_mode: Optional[pulumi.Input[str]] = None,
            resource_group_id: Optional[pulumi.Input[str]] = None) -> 'ResourceGroupPolicyRemediation':
        """
        Get an existing ResourceGroupPolicyRemediation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] failure_percentage: A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] location_filters: A list of the resource locations that will be remediated.
        :param pulumi.Input[str] name: The name of the Policy Remediation. Changing this forces a new resource to be created.
        :param pulumi.Input[int] parallel_deployments: Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        :param pulumi.Input[str] policy_assignment_id: The ID of the Policy Assignment that should be remediated.
        :param pulumi.Input[str] policy_definition_id: The unique ID for the policy definition within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
               
               > **Note:** This property has been deprecated and will be removed in version 4.0 of the provider in favour of `policy_definition_reference_id`.
        :param pulumi.Input[str] policy_definition_reference_id: The unique ID for the policy definition reference within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        :param pulumi.Input[int] resource_count: Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        :param pulumi.Input[str] resource_discovery_mode: The way that resources to remediate are discovered. Possible values are `ExistingNonCompliant`, `ReEvaluateCompliance`. Defaults to `ExistingNonCompliant`.
        :param pulumi.Input[str] resource_group_id: The Resource Group ID at which the Policy Remediation should be applied. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResourceGroupPolicyRemediationState.__new__(_ResourceGroupPolicyRemediationState)

        __props__.__dict__["failure_percentage"] = failure_percentage
        __props__.__dict__["location_filters"] = location_filters
        __props__.__dict__["name"] = name
        __props__.__dict__["parallel_deployments"] = parallel_deployments
        __props__.__dict__["policy_assignment_id"] = policy_assignment_id
        __props__.__dict__["policy_definition_id"] = policy_definition_id
        __props__.__dict__["policy_definition_reference_id"] = policy_definition_reference_id
        __props__.__dict__["resource_count"] = resource_count
        __props__.__dict__["resource_discovery_mode"] = resource_discovery_mode
        __props__.__dict__["resource_group_id"] = resource_group_id
        return ResourceGroupPolicyRemediation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="failurePercentage")
    def failure_percentage(self) -> pulumi.Output[Optional[float]]:
        """
        A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        """
        return pulumi.get(self, "failure_percentage")

    @property
    @pulumi.getter(name="locationFilters")
    def location_filters(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of the resource locations that will be remediated.
        """
        return pulumi.get(self, "location_filters")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Policy Remediation. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parallelDeployments")
    def parallel_deployments(self) -> pulumi.Output[Optional[int]]:
        """
        Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        """
        return pulumi.get(self, "parallel_deployments")

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Output[str]:
        """
        The ID of the Policy Assignment that should be remediated.
        """
        return pulumi.get(self, "policy_assignment_id")

    @property
    @pulumi.getter(name="policyDefinitionId")
    @_utilities.deprecated("""`policy_definition_id` will be removed in version 4.0 of the AzureRM Provider in favour of `policy_definition_reference_id`.""")
    def policy_definition_id(self) -> pulumi.Output[Optional[str]]:
        """
        The unique ID for the policy definition within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.

        > **Note:** This property has been deprecated and will be removed in version 4.0 of the provider in favour of `policy_definition_reference_id`.
        """
        return pulumi.get(self, "policy_definition_id")

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> pulumi.Output[Optional[str]]:
        """
        The unique ID for the policy definition reference within the policy set definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @property
    @pulumi.getter(name="resourceCount")
    def resource_count(self) -> pulumi.Output[Optional[int]]:
        """
        Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        """
        return pulumi.get(self, "resource_count")

    @property
    @pulumi.getter(name="resourceDiscoveryMode")
    def resource_discovery_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The way that resources to remediate are discovered. Possible values are `ExistingNonCompliant`, `ReEvaluateCompliance`. Defaults to `ExistingNonCompliant`.
        """
        return pulumi.get(self, "resource_discovery_mode")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Output[str]:
        """
        The Resource Group ID at which the Policy Remediation should be applied. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_id")

