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
    'PolicySetDefinitionPolicyDefinitionGroupArgs',
    'PolicySetDefinitionPolicyDefinitionGroupArgsDict',
    'PolicySetDefinitionPolicyDefinitionReferenceArgs',
    'PolicySetDefinitionPolicyDefinitionReferenceArgsDict',
    'VirtualMachineConfigurationAssignmentConfigurationArgs',
    'VirtualMachineConfigurationAssignmentConfigurationArgsDict',
    'VirtualMachineConfigurationAssignmentConfigurationParameterArgs',
    'VirtualMachineConfigurationAssignmentConfigurationParameterArgsDict',
]

MYPY = False

if not MYPY:
    class PolicySetDefinitionPolicyDefinitionGroupArgsDict(TypedDict):
        name: pulumi.Input[str]
        """
        The name of this policy definition group.
        """
        additional_metadata_resource_id: NotRequired[pulumi.Input[str]]
        """
        The ID of a resource that contains additional metadata about this policy definition group.
        """
        category: NotRequired[pulumi.Input[str]]
        """
        The category of this policy definition group.
        """
        description: NotRequired[pulumi.Input[str]]
        """
        The description of this policy definition group.
        """
        display_name: NotRequired[pulumi.Input[str]]
        """
        The display name of this policy definition group.
        """
elif False:
    PolicySetDefinitionPolicyDefinitionGroupArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PolicySetDefinitionPolicyDefinitionGroupArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 additional_metadata_resource_id: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: The name of this policy definition group.
        :param pulumi.Input[str] additional_metadata_resource_id: The ID of a resource that contains additional metadata about this policy definition group.
        :param pulumi.Input[str] category: The category of this policy definition group.
        :param pulumi.Input[str] description: The description of this policy definition group.
        :param pulumi.Input[str] display_name: The display name of this policy definition group.
        """
        pulumi.set(__self__, "name", name)
        if additional_metadata_resource_id is not None:
            pulumi.set(__self__, "additional_metadata_resource_id", additional_metadata_resource_id)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of this policy definition group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="additionalMetadataResourceId")
    def additional_metadata_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a resource that contains additional metadata about this policy definition group.
        """
        return pulumi.get(self, "additional_metadata_resource_id")

    @additional_metadata_resource_id.setter
    def additional_metadata_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "additional_metadata_resource_id", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        The category of this policy definition group.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of this policy definition group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of this policy definition group.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


if not MYPY:
    class PolicySetDefinitionPolicyDefinitionReferenceArgsDict(TypedDict):
        policy_definition_id: pulumi.Input[str]
        """
        The ID of the policy definition that will be included in this policy set definition.
        """
        parameter_values: NotRequired[pulumi.Input[str]]
        """
        Parameter values for the referenced policy rule. This field is a JSON string that allows you to assign parameters to this policy rule.
        """
        policy_group_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        A list of names of the policy definition groups that this policy definition reference belongs to.
        """
        reference_id: NotRequired[pulumi.Input[str]]
        """
        A unique ID within this policy set definition for this policy definition reference.
        """
elif False:
    PolicySetDefinitionPolicyDefinitionReferenceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PolicySetDefinitionPolicyDefinitionReferenceArgs:
    def __init__(__self__, *,
                 policy_definition_id: pulumi.Input[str],
                 parameter_values: Optional[pulumi.Input[str]] = None,
                 policy_group_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 reference_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] policy_definition_id: The ID of the policy definition that will be included in this policy set definition.
        :param pulumi.Input[str] parameter_values: Parameter values for the referenced policy rule. This field is a JSON string that allows you to assign parameters to this policy rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policy_group_names: A list of names of the policy definition groups that this policy definition reference belongs to.
        :param pulumi.Input[str] reference_id: A unique ID within this policy set definition for this policy definition reference.
        """
        pulumi.set(__self__, "policy_definition_id", policy_definition_id)
        if parameter_values is not None:
            pulumi.set(__self__, "parameter_values", parameter_values)
        if policy_group_names is not None:
            pulumi.set(__self__, "policy_group_names", policy_group_names)
        if reference_id is not None:
            pulumi.set(__self__, "reference_id", reference_id)

    @property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> pulumi.Input[str]:
        """
        The ID of the policy definition that will be included in this policy set definition.
        """
        return pulumi.get(self, "policy_definition_id")

    @policy_definition_id.setter
    def policy_definition_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_definition_id", value)

    @property
    @pulumi.getter(name="parameterValues")
    def parameter_values(self) -> Optional[pulumi.Input[str]]:
        """
        Parameter values for the referenced policy rule. This field is a JSON string that allows you to assign parameters to this policy rule.
        """
        return pulumi.get(self, "parameter_values")

    @parameter_values.setter
    def parameter_values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_values", value)

    @property
    @pulumi.getter(name="policyGroupNames")
    def policy_group_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of names of the policy definition groups that this policy definition reference belongs to.
        """
        return pulumi.get(self, "policy_group_names")

    @policy_group_names.setter
    def policy_group_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policy_group_names", value)

    @property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[pulumi.Input[str]]:
        """
        A unique ID within this policy set definition for this policy definition reference.
        """
        return pulumi.get(self, "reference_id")

    @reference_id.setter
    def reference_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reference_id", value)


if not MYPY:
    class VirtualMachineConfigurationAssignmentConfigurationArgsDict(TypedDict):
        assignment_type: NotRequired[pulumi.Input[str]]
        """
        The assignment type for the Guest Configuration Assignment. Possible values are `Audit`, `ApplyAndAutoCorrect`, `ApplyAndMonitor` and `DeployAndAutoCorrect`.
        """
        content_hash: NotRequired[pulumi.Input[str]]
        """
        The content hash for the Guest Configuration package.
        """
        content_uri: NotRequired[pulumi.Input[str]]
        """
        The content URI where the Guest Configuration package is stored.

        > **NOTE:** When deploying a Custom Guest Configuration package the `content_hash` and `content_uri` fields must be defined. For Built-in Guest Configuration packages, such as the `AzureWindowsBaseline` package, the `content_hash` and `content_uri` should not be defined, rather these fields will be returned after the Built-in Guest Configuration package has been provisioned. For more information on guest configuration assignments please see the [product documentation](https://docs.microsoft.com/azure/governance/policy/concepts/guest-configuration-assignments).
        """
        parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input['VirtualMachineConfigurationAssignmentConfigurationParameterArgsDict']]]]
        """
        One or more `parameter` blocks as defined below which define what configuration parameters and values against.
        """
        version: NotRequired[pulumi.Input[str]]
        """
        The version of the Guest Configuration that will be assigned in this Guest Configuration Assignment.
        """
elif False:
    VirtualMachineConfigurationAssignmentConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VirtualMachineConfigurationAssignmentConfigurationArgs:
    def __init__(__self__, *,
                 assignment_type: Optional[pulumi.Input[str]] = None,
                 content_hash: Optional[pulumi.Input[str]] = None,
                 content_uri: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualMachineConfigurationAssignmentConfigurationParameterArgs']]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] assignment_type: The assignment type for the Guest Configuration Assignment. Possible values are `Audit`, `ApplyAndAutoCorrect`, `ApplyAndMonitor` and `DeployAndAutoCorrect`.
        :param pulumi.Input[str] content_hash: The content hash for the Guest Configuration package.
        :param pulumi.Input[str] content_uri: The content URI where the Guest Configuration package is stored.
               
               > **NOTE:** When deploying a Custom Guest Configuration package the `content_hash` and `content_uri` fields must be defined. For Built-in Guest Configuration packages, such as the `AzureWindowsBaseline` package, the `content_hash` and `content_uri` should not be defined, rather these fields will be returned after the Built-in Guest Configuration package has been provisioned. For more information on guest configuration assignments please see the [product documentation](https://docs.microsoft.com/azure/governance/policy/concepts/guest-configuration-assignments).
        :param pulumi.Input[Sequence[pulumi.Input['VirtualMachineConfigurationAssignmentConfigurationParameterArgs']]] parameters: One or more `parameter` blocks as defined below which define what configuration parameters and values against.
        :param pulumi.Input[str] version: The version of the Guest Configuration that will be assigned in this Guest Configuration Assignment.
        """
        if assignment_type is not None:
            pulumi.set(__self__, "assignment_type", assignment_type)
        if content_hash is not None:
            pulumi.set(__self__, "content_hash", content_hash)
        if content_uri is not None:
            pulumi.set(__self__, "content_uri", content_uri)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="assignmentType")
    def assignment_type(self) -> Optional[pulumi.Input[str]]:
        """
        The assignment type for the Guest Configuration Assignment. Possible values are `Audit`, `ApplyAndAutoCorrect`, `ApplyAndMonitor` and `DeployAndAutoCorrect`.
        """
        return pulumi.get(self, "assignment_type")

    @assignment_type.setter
    def assignment_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assignment_type", value)

    @property
    @pulumi.getter(name="contentHash")
    def content_hash(self) -> Optional[pulumi.Input[str]]:
        """
        The content hash for the Guest Configuration package.
        """
        return pulumi.get(self, "content_hash")

    @content_hash.setter
    def content_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_hash", value)

    @property
    @pulumi.getter(name="contentUri")
    def content_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The content URI where the Guest Configuration package is stored.

        > **NOTE:** When deploying a Custom Guest Configuration package the `content_hash` and `content_uri` fields must be defined. For Built-in Guest Configuration packages, such as the `AzureWindowsBaseline` package, the `content_hash` and `content_uri` should not be defined, rather these fields will be returned after the Built-in Guest Configuration package has been provisioned. For more information on guest configuration assignments please see the [product documentation](https://docs.microsoft.com/azure/governance/policy/concepts/guest-configuration-assignments).
        """
        return pulumi.get(self, "content_uri")

    @content_uri.setter
    def content_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_uri", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VirtualMachineConfigurationAssignmentConfigurationParameterArgs']]]]:
        """
        One or more `parameter` blocks as defined below which define what configuration parameters and values against.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualMachineConfigurationAssignmentConfigurationParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the Guest Configuration that will be assigned in this Guest Configuration Assignment.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


if not MYPY:
    class VirtualMachineConfigurationAssignmentConfigurationParameterArgsDict(TypedDict):
        name: pulumi.Input[str]
        """
        The name of the configuration parameter to check.
        """
        value: pulumi.Input[str]
        """
        The value to check the configuration parameter with.
        """
elif False:
    VirtualMachineConfigurationAssignmentConfigurationParameterArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VirtualMachineConfigurationAssignmentConfigurationParameterArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the configuration parameter to check.
        :param pulumi.Input[str] value: The value to check the configuration parameter with.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the configuration parameter to check.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value to check the configuration parameter with.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


