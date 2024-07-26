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

__all__ = ['WorkspaceCustomerManagedKeyArgs', 'WorkspaceCustomerManagedKey']

@pulumi.input_type
class WorkspaceCustomerManagedKeyArgs:
    def __init__(__self__, *,
                 key_vault_key_id: pulumi.Input[str],
                 workspace_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a WorkspaceCustomerManagedKey resource.
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault.
        :param pulumi.Input[str] workspace_id: The ID of the Databricks Workspace..
        """
        pulumi.set(__self__, "key_vault_key_id", key_vault_key_id)
        pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> pulumi.Input[str]:
        """
        The ID of the Key Vault.
        """
        return pulumi.get(self, "key_vault_key_id")

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_key_id", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the Databricks Workspace..
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)


@pulumi.input_type
class _WorkspaceCustomerManagedKeyState:
    def __init__(__self__, *,
                 key_vault_key_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WorkspaceCustomerManagedKey resources.
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault.
        :param pulumi.Input[str] workspace_id: The ID of the Databricks Workspace..
        """
        if key_vault_key_id is not None:
            pulumi.set(__self__, "key_vault_key_id", key_vault_key_id)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Key Vault.
        """
        return pulumi.get(self, "key_vault_key_id")

    @key_vault_key_id.setter
    def key_vault_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_key_id", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Databricks Workspace..
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_id", value)


class WorkspaceCustomerManagedKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_vault_key_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Customer Managed Key for a Databricks Workspace root DBFS

        !>**IMPORTANT:** This resource has been deprecated and will be removed from the 4.0 Azure provider. Please use the `databricks.WorkspaceRootDbfsCustomerManagedKey` resource instead.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_client_config()
        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_workspace = azure.databricks.Workspace("example",
            name="databricks-test",
            resource_group_name=example.name,
            location=example.location,
            sku="premium",
            customer_managed_key_enabled=True,
            tags={
                "Environment": "Production",
            })
        example_key_vault = azure.keyvault.KeyVault("example",
            name="examplekeyvault",
            location=example.location,
            resource_group_name=example.name,
            tenant_id=current.tenant_id,
            sku_name="premium",
            purge_protection_enabled=True,
            soft_delete_retention_days=7)
        terraform = azure.keyvault.AccessPolicy("terraform",
            key_vault_id=example_key_vault.id,
            tenant_id=example_key_vault.tenant_id,
            object_id=current.object_id,
            key_permissions=[
                "Create",
                "Delete",
                "Get",
                "Purge",
                "Recover",
                "Update",
                "List",
                "Decrypt",
                "Sign",
                "GetRotationPolicy",
            ])
        example_key = azure.keyvault.Key("example",
            name="example-certificate",
            key_vault_id=example_key_vault.id,
            key_type="RSA",
            key_size=2048,
            key_opts=[
                "decrypt",
                "encrypt",
                "sign",
                "unwrapKey",
                "verify",
                "wrapKey",
            ],
            opts = pulumi.ResourceOptions(depends_on=[terraform]))
        databricks = azure.keyvault.AccessPolicy("databricks",
            key_vault_id=example_key_vault.id,
            tenant_id=example_workspace.storage_account_identities[0].tenant_id,
            object_id=example_workspace.storage_account_identities[0].principal_id,
            key_permissions=[
                "Create",
                "Delete",
                "Get",
                "Purge",
                "Recover",
                "Update",
                "List",
                "Decrypt",
                "Sign",
            ],
            opts = pulumi.ResourceOptions(depends_on=[example_workspace]))
        example_workspace_root_dbfs_customer_managed_key = azure.databricks.WorkspaceRootDbfsCustomerManagedKey("example",
            workspace_id=example_workspace.id,
            key_vault_key_id=example_key.id,
            opts = pulumi.ResourceOptions(depends_on=[databricks]))
        ```

        ## Example HCL Configurations

        * Databricks Workspace with Root Databricks File System Customer Managed Keys
        * Databricks Workspace with Customer Managed Keys for Managed Services
        * Databricks Workspace with Private Endpoint, Customer Managed Keys for Managed Services and Root Databricks File System Customer Managed Keys

        ## Import

        Databricks Workspace Customer Managed Key can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:databricks/workspaceCustomerManagedKey:WorkspaceCustomerManagedKey workspace1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Databricks/workspaces/workspace1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault.
        :param pulumi.Input[str] workspace_id: The ID of the Databricks Workspace..
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceCustomerManagedKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Customer Managed Key for a Databricks Workspace root DBFS

        !>**IMPORTANT:** This resource has been deprecated and will be removed from the 4.0 Azure provider. Please use the `databricks.WorkspaceRootDbfsCustomerManagedKey` resource instead.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        current = azure.core.get_client_config()
        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_workspace = azure.databricks.Workspace("example",
            name="databricks-test",
            resource_group_name=example.name,
            location=example.location,
            sku="premium",
            customer_managed_key_enabled=True,
            tags={
                "Environment": "Production",
            })
        example_key_vault = azure.keyvault.KeyVault("example",
            name="examplekeyvault",
            location=example.location,
            resource_group_name=example.name,
            tenant_id=current.tenant_id,
            sku_name="premium",
            purge_protection_enabled=True,
            soft_delete_retention_days=7)
        terraform = azure.keyvault.AccessPolicy("terraform",
            key_vault_id=example_key_vault.id,
            tenant_id=example_key_vault.tenant_id,
            object_id=current.object_id,
            key_permissions=[
                "Create",
                "Delete",
                "Get",
                "Purge",
                "Recover",
                "Update",
                "List",
                "Decrypt",
                "Sign",
                "GetRotationPolicy",
            ])
        example_key = azure.keyvault.Key("example",
            name="example-certificate",
            key_vault_id=example_key_vault.id,
            key_type="RSA",
            key_size=2048,
            key_opts=[
                "decrypt",
                "encrypt",
                "sign",
                "unwrapKey",
                "verify",
                "wrapKey",
            ],
            opts = pulumi.ResourceOptions(depends_on=[terraform]))
        databricks = azure.keyvault.AccessPolicy("databricks",
            key_vault_id=example_key_vault.id,
            tenant_id=example_workspace.storage_account_identities[0].tenant_id,
            object_id=example_workspace.storage_account_identities[0].principal_id,
            key_permissions=[
                "Create",
                "Delete",
                "Get",
                "Purge",
                "Recover",
                "Update",
                "List",
                "Decrypt",
                "Sign",
            ],
            opts = pulumi.ResourceOptions(depends_on=[example_workspace]))
        example_workspace_root_dbfs_customer_managed_key = azure.databricks.WorkspaceRootDbfsCustomerManagedKey("example",
            workspace_id=example_workspace.id,
            key_vault_key_id=example_key.id,
            opts = pulumi.ResourceOptions(depends_on=[databricks]))
        ```

        ## Example HCL Configurations

        * Databricks Workspace with Root Databricks File System Customer Managed Keys
        * Databricks Workspace with Customer Managed Keys for Managed Services
        * Databricks Workspace with Private Endpoint, Customer Managed Keys for Managed Services and Root Databricks File System Customer Managed Keys

        ## Import

        Databricks Workspace Customer Managed Key can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:databricks/workspaceCustomerManagedKey:WorkspaceCustomerManagedKey workspace1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Databricks/workspaces/workspace1
        ```

        :param str resource_name: The name of the resource.
        :param WorkspaceCustomerManagedKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceCustomerManagedKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_vault_key_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceCustomerManagedKeyArgs.__new__(WorkspaceCustomerManagedKeyArgs)

            if key_vault_key_id is None and not opts.urn:
                raise TypeError("Missing required property 'key_vault_key_id'")
            __props__.__dict__["key_vault_key_id"] = key_vault_key_id
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
        super(WorkspaceCustomerManagedKey, __self__).__init__(
            'azure:databricks/workspaceCustomerManagedKey:WorkspaceCustomerManagedKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key_vault_key_id: Optional[pulumi.Input[str]] = None,
            workspace_id: Optional[pulumi.Input[str]] = None) -> 'WorkspaceCustomerManagedKey':
        """
        Get an existing WorkspaceCustomerManagedKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_vault_key_id: The ID of the Key Vault.
        :param pulumi.Input[str] workspace_id: The ID of the Databricks Workspace..
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceCustomerManagedKeyState.__new__(_WorkspaceCustomerManagedKeyState)

        __props__.__dict__["key_vault_key_id"] = key_vault_key_id
        __props__.__dict__["workspace_id"] = workspace_id
        return WorkspaceCustomerManagedKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> pulumi.Output[str]:
        """
        The ID of the Key Vault.
        """
        return pulumi.get(self, "key_vault_key_id")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Databricks Workspace..
        """
        return pulumi.get(self, "workspace_id")

