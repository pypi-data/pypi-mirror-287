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

__all__ = ['IntegrationAccountBatchConfigurationArgs', 'IntegrationAccountBatchConfiguration']

@pulumi.input_type
class IntegrationAccountBatchConfigurationArgs:
    def __init__(__self__, *,
                 batch_group_name: pulumi.Input[str],
                 integration_account_name: pulumi.Input[str],
                 release_criteria: pulumi.Input['IntegrationAccountBatchConfigurationReleaseCriteriaArgs'],
                 resource_group_name: pulumi.Input[str],
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IntegrationAccountBatchConfiguration resource.
        :param pulumi.Input[str] batch_group_name: The batch group name of the Logic App Integration Batch Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[str] integration_account_name: The name of the Logic App Integration Account. Changing this forces a new resource to be created.
        :param pulumi.Input['IntegrationAccountBatchConfigurationReleaseCriteriaArgs'] release_criteria: A `release_criteria` block as documented below, which is used to select the criteria to meet before processing each batch.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Logic App Integration Account Batch Configuration should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A JSON mapping of any Metadata for this Logic App Integration Account Batch Configuration.
        :param pulumi.Input[str] name: The name which should be used for this Logic App Integration Account Batch Configuration. Only Alphanumeric characters allowed. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "batch_group_name", batch_group_name)
        pulumi.set(__self__, "integration_account_name", integration_account_name)
        pulumi.set(__self__, "release_criteria", release_criteria)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="batchGroupName")
    def batch_group_name(self) -> pulumi.Input[str]:
        """
        The batch group name of the Logic App Integration Batch Configuration. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "batch_group_name")

    @batch_group_name.setter
    def batch_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "batch_group_name", value)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[str]:
        """
        The name of the Logic App Integration Account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter(name="releaseCriteria")
    def release_criteria(self) -> pulumi.Input['IntegrationAccountBatchConfigurationReleaseCriteriaArgs']:
        """
        A `release_criteria` block as documented below, which is used to select the criteria to meet before processing each batch.
        """
        return pulumi.get(self, "release_criteria")

    @release_criteria.setter
    def release_criteria(self, value: pulumi.Input['IntegrationAccountBatchConfigurationReleaseCriteriaArgs']):
        pulumi.set(self, "release_criteria", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Logic App Integration Account Batch Configuration should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A JSON mapping of any Metadata for this Logic App Integration Account Batch Configuration.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Logic App Integration Account Batch Configuration. Only Alphanumeric characters allowed. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _IntegrationAccountBatchConfigurationState:
    def __init__(__self__, *,
                 batch_group_name: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 release_criteria: Optional[pulumi.Input['IntegrationAccountBatchConfigurationReleaseCriteriaArgs']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IntegrationAccountBatchConfiguration resources.
        :param pulumi.Input[str] batch_group_name: The batch group name of the Logic App Integration Batch Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[str] integration_account_name: The name of the Logic App Integration Account. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A JSON mapping of any Metadata for this Logic App Integration Account Batch Configuration.
        :param pulumi.Input[str] name: The name which should be used for this Logic App Integration Account Batch Configuration. Only Alphanumeric characters allowed. Changing this forces a new resource to be created.
        :param pulumi.Input['IntegrationAccountBatchConfigurationReleaseCriteriaArgs'] release_criteria: A `release_criteria` block as documented below, which is used to select the criteria to meet before processing each batch.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Logic App Integration Account Batch Configuration should exist. Changing this forces a new resource to be created.
        """
        if batch_group_name is not None:
            pulumi.set(__self__, "batch_group_name", batch_group_name)
        if integration_account_name is not None:
            pulumi.set(__self__, "integration_account_name", integration_account_name)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if release_criteria is not None:
            pulumi.set(__self__, "release_criteria", release_criteria)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)

    @property
    @pulumi.getter(name="batchGroupName")
    def batch_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The batch group name of the Logic App Integration Batch Configuration. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "batch_group_name")

    @batch_group_name.setter
    def batch_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "batch_group_name", value)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Logic App Integration Account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A JSON mapping of any Metadata for this Logic App Integration Account Batch Configuration.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Logic App Integration Account Batch Configuration. Only Alphanumeric characters allowed. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="releaseCriteria")
    def release_criteria(self) -> Optional[pulumi.Input['IntegrationAccountBatchConfigurationReleaseCriteriaArgs']]:
        """
        A `release_criteria` block as documented below, which is used to select the criteria to meet before processing each batch.
        """
        return pulumi.get(self, "release_criteria")

    @release_criteria.setter
    def release_criteria(self, value: Optional[pulumi.Input['IntegrationAccountBatchConfigurationReleaseCriteriaArgs']]):
        pulumi.set(self, "release_criteria", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Logic App Integration Account Batch Configuration should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


class IntegrationAccountBatchConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 batch_group_name: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 release_criteria: Optional[pulumi.Input[Union['IntegrationAccountBatchConfigurationReleaseCriteriaArgs', 'IntegrationAccountBatchConfigurationReleaseCriteriaArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Logic App Integration Account Batch Configuration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_integration_account = azure.logicapps.IntegrationAccount("example",
            name="example-ia",
            location=example.location,
            resource_group_name=example.name,
            sku_name="Standard")
        example_integration_account_batch_configuration = azure.logicapps.IntegrationAccountBatchConfiguration("example",
            name="exampleiabc",
            resource_group_name=example.name,
            integration_account_name=example_integration_account.name,
            batch_group_name="TestBatchGroup",
            release_criteria={
                "message_count": 80,
            })
        ```

        ## Import

        Logic App Integration Account Batch Configurations can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:logicapps/integrationAccountBatchConfiguration:IntegrationAccountBatchConfiguration example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Logic/integrationAccounts/account1/batchConfigurations/batchConfiguration1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] batch_group_name: The batch group name of the Logic App Integration Batch Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[str] integration_account_name: The name of the Logic App Integration Account. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A JSON mapping of any Metadata for this Logic App Integration Account Batch Configuration.
        :param pulumi.Input[str] name: The name which should be used for this Logic App Integration Account Batch Configuration. Only Alphanumeric characters allowed. Changing this forces a new resource to be created.
        :param pulumi.Input[Union['IntegrationAccountBatchConfigurationReleaseCriteriaArgs', 'IntegrationAccountBatchConfigurationReleaseCriteriaArgsDict']] release_criteria: A `release_criteria` block as documented below, which is used to select the criteria to meet before processing each batch.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Logic App Integration Account Batch Configuration should exist. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationAccountBatchConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Logic App Integration Account Batch Configuration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_integration_account = azure.logicapps.IntegrationAccount("example",
            name="example-ia",
            location=example.location,
            resource_group_name=example.name,
            sku_name="Standard")
        example_integration_account_batch_configuration = azure.logicapps.IntegrationAccountBatchConfiguration("example",
            name="exampleiabc",
            resource_group_name=example.name,
            integration_account_name=example_integration_account.name,
            batch_group_name="TestBatchGroup",
            release_criteria={
                "message_count": 80,
            })
        ```

        ## Import

        Logic App Integration Account Batch Configurations can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:logicapps/integrationAccountBatchConfiguration:IntegrationAccountBatchConfiguration example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Logic/integrationAccounts/account1/batchConfigurations/batchConfiguration1
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationAccountBatchConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationAccountBatchConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 batch_group_name: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 release_criteria: Optional[pulumi.Input[Union['IntegrationAccountBatchConfigurationReleaseCriteriaArgs', 'IntegrationAccountBatchConfigurationReleaseCriteriaArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationAccountBatchConfigurationArgs.__new__(IntegrationAccountBatchConfigurationArgs)

            if batch_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'batch_group_name'")
            __props__.__dict__["batch_group_name"] = batch_group_name
            if integration_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_account_name'")
            __props__.__dict__["integration_account_name"] = integration_account_name
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            if release_criteria is None and not opts.urn:
                raise TypeError("Missing required property 'release_criteria'")
            __props__.__dict__["release_criteria"] = release_criteria
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
        super(IntegrationAccountBatchConfiguration, __self__).__init__(
            'azure:logicapps/integrationAccountBatchConfiguration:IntegrationAccountBatchConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            batch_group_name: Optional[pulumi.Input[str]] = None,
            integration_account_name: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            release_criteria: Optional[pulumi.Input[Union['IntegrationAccountBatchConfigurationReleaseCriteriaArgs', 'IntegrationAccountBatchConfigurationReleaseCriteriaArgsDict']]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'IntegrationAccountBatchConfiguration':
        """
        Get an existing IntegrationAccountBatchConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] batch_group_name: The batch group name of the Logic App Integration Batch Configuration. Changing this forces a new resource to be created.
        :param pulumi.Input[str] integration_account_name: The name of the Logic App Integration Account. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: A JSON mapping of any Metadata for this Logic App Integration Account Batch Configuration.
        :param pulumi.Input[str] name: The name which should be used for this Logic App Integration Account Batch Configuration. Only Alphanumeric characters allowed. Changing this forces a new resource to be created.
        :param pulumi.Input[Union['IntegrationAccountBatchConfigurationReleaseCriteriaArgs', 'IntegrationAccountBatchConfigurationReleaseCriteriaArgsDict']] release_criteria: A `release_criteria` block as documented below, which is used to select the criteria to meet before processing each batch.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Logic App Integration Account Batch Configuration should exist. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationAccountBatchConfigurationState.__new__(_IntegrationAccountBatchConfigurationState)

        __props__.__dict__["batch_group_name"] = batch_group_name
        __props__.__dict__["integration_account_name"] = integration_account_name
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["release_criteria"] = release_criteria
        __props__.__dict__["resource_group_name"] = resource_group_name
        return IntegrationAccountBatchConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="batchGroupName")
    def batch_group_name(self) -> pulumi.Output[str]:
        """
        The batch group name of the Logic App Integration Batch Configuration. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "batch_group_name")

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Output[str]:
        """
        The name of the Logic App Integration Account. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "integration_account_name")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A JSON mapping of any Metadata for this Logic App Integration Account Batch Configuration.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Logic App Integration Account Batch Configuration. Only Alphanumeric characters allowed. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="releaseCriteria")
    def release_criteria(self) -> pulumi.Output['outputs.IntegrationAccountBatchConfigurationReleaseCriteria']:
        """
        A `release_criteria` block as documented below, which is used to select the criteria to meet before processing each batch.
        """
        return pulumi.get(self, "release_criteria")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Logic App Integration Account Batch Configuration should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

