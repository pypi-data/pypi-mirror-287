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
    'AttachedDatabaseConfigurationSharing',
    'ClusterIdentity',
    'ClusterOptimizedAutoScale',
    'ClusterSku',
    'ClusterVirtualNetworkConfiguration',
    'GetClusterIdentityResult',
]

@pulumi.output_type
class AttachedDatabaseConfigurationSharing(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "externalTablesToExcludes":
            suggest = "external_tables_to_excludes"
        elif key == "externalTablesToIncludes":
            suggest = "external_tables_to_includes"
        elif key == "materializedViewsToExcludes":
            suggest = "materialized_views_to_excludes"
        elif key == "materializedViewsToIncludes":
            suggest = "materialized_views_to_includes"
        elif key == "tablesToExcludes":
            suggest = "tables_to_excludes"
        elif key == "tablesToIncludes":
            suggest = "tables_to_includes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AttachedDatabaseConfigurationSharing. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AttachedDatabaseConfigurationSharing.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AttachedDatabaseConfigurationSharing.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 external_tables_to_excludes: Optional[Sequence[str]] = None,
                 external_tables_to_includes: Optional[Sequence[str]] = None,
                 materialized_views_to_excludes: Optional[Sequence[str]] = None,
                 materialized_views_to_includes: Optional[Sequence[str]] = None,
                 tables_to_excludes: Optional[Sequence[str]] = None,
                 tables_to_includes: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] external_tables_to_excludes: List of external tables exclude from the follower database.
        :param Sequence[str] external_tables_to_includes: List of external tables to include in the follower database.
        :param Sequence[str] materialized_views_to_excludes: List of materialized views exclude from the follower database.
        :param Sequence[str] materialized_views_to_includes: List of materialized views to include in the follower database.
        :param Sequence[str] tables_to_excludes: List of tables to exclude from the follower database.
        :param Sequence[str] tables_to_includes: List of tables to include in the follower database.
        """
        if external_tables_to_excludes is not None:
            pulumi.set(__self__, "external_tables_to_excludes", external_tables_to_excludes)
        if external_tables_to_includes is not None:
            pulumi.set(__self__, "external_tables_to_includes", external_tables_to_includes)
        if materialized_views_to_excludes is not None:
            pulumi.set(__self__, "materialized_views_to_excludes", materialized_views_to_excludes)
        if materialized_views_to_includes is not None:
            pulumi.set(__self__, "materialized_views_to_includes", materialized_views_to_includes)
        if tables_to_excludes is not None:
            pulumi.set(__self__, "tables_to_excludes", tables_to_excludes)
        if tables_to_includes is not None:
            pulumi.set(__self__, "tables_to_includes", tables_to_includes)

    @property
    @pulumi.getter(name="externalTablesToExcludes")
    def external_tables_to_excludes(self) -> Optional[Sequence[str]]:
        """
        List of external tables exclude from the follower database.
        """
        return pulumi.get(self, "external_tables_to_excludes")

    @property
    @pulumi.getter(name="externalTablesToIncludes")
    def external_tables_to_includes(self) -> Optional[Sequence[str]]:
        """
        List of external tables to include in the follower database.
        """
        return pulumi.get(self, "external_tables_to_includes")

    @property
    @pulumi.getter(name="materializedViewsToExcludes")
    def materialized_views_to_excludes(self) -> Optional[Sequence[str]]:
        """
        List of materialized views exclude from the follower database.
        """
        return pulumi.get(self, "materialized_views_to_excludes")

    @property
    @pulumi.getter(name="materializedViewsToIncludes")
    def materialized_views_to_includes(self) -> Optional[Sequence[str]]:
        """
        List of materialized views to include in the follower database.
        """
        return pulumi.get(self, "materialized_views_to_includes")

    @property
    @pulumi.getter(name="tablesToExcludes")
    def tables_to_excludes(self) -> Optional[Sequence[str]]:
        """
        List of tables to exclude from the follower database.
        """
        return pulumi.get(self, "tables_to_excludes")

    @property
    @pulumi.getter(name="tablesToIncludes")
    def tables_to_includes(self) -> Optional[Sequence[str]]:
        """
        List of tables to include in the follower database.
        """
        return pulumi.get(self, "tables_to_includes")


@pulumi.output_type
class ClusterIdentity(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "identityIds":
            suggest = "identity_ids"
        elif key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 identity_ids: Optional[Sequence[str]] = None,
                 principal_id: Optional[str] = None,
                 tenant_id: Optional[str] = None):
        """
        :param str type: Specifies the type of Managed Service Identity that is configured on this Kusto Cluster. Possible values are: `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
        :param Sequence[str] identity_ids: Specifies a list of User Assigned Managed Identity IDs to be assigned to this Kusto Cluster.
               
               > **NOTE:** This is required when `type` is set to `UserAssigned` or `SystemAssigned, UserAssigned`.
        :param str principal_id: The Principal ID associated with this System Assigned Managed Service Identity.
        :param str tenant_id: The Tenant ID associated with this System Assigned Managed Service Identity.
        """
        pulumi.set(__self__, "type", type)
        if identity_ids is not None:
            pulumi.set(__self__, "identity_ids", identity_ids)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Specifies the type of Managed Service Identity that is configured on this Kusto Cluster. Possible values are: `SystemAssigned`, `UserAssigned` and `SystemAssigned, UserAssigned`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Optional[Sequence[str]]:
        """
        Specifies a list of User Assigned Managed Identity IDs to be assigned to this Kusto Cluster.

        > **NOTE:** This is required when `type` is set to `UserAssigned` or `SystemAssigned, UserAssigned`.
        """
        return pulumi.get(self, "identity_ids")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[str]:
        """
        The Principal ID associated with this System Assigned Managed Service Identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The Tenant ID associated with this System Assigned Managed Service Identity.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class ClusterOptimizedAutoScale(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maximumInstances":
            suggest = "maximum_instances"
        elif key == "minimumInstances":
            suggest = "minimum_instances"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterOptimizedAutoScale. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterOptimizedAutoScale.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterOptimizedAutoScale.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 maximum_instances: int,
                 minimum_instances: int):
        """
        :param int maximum_instances: The maximum number of allowed instances. Must between `0` and `1000`.
        :param int minimum_instances: The minimum number of allowed instances. Must between `0` and `1000`.
        """
        pulumi.set(__self__, "maximum_instances", maximum_instances)
        pulumi.set(__self__, "minimum_instances", minimum_instances)

    @property
    @pulumi.getter(name="maximumInstances")
    def maximum_instances(self) -> int:
        """
        The maximum number of allowed instances. Must between `0` and `1000`.
        """
        return pulumi.get(self, "maximum_instances")

    @property
    @pulumi.getter(name="minimumInstances")
    def minimum_instances(self) -> int:
        """
        The minimum number of allowed instances. Must between `0` and `1000`.
        """
        return pulumi.get(self, "minimum_instances")


@pulumi.output_type
class ClusterSku(dict):
    def __init__(__self__, *,
                 name: str,
                 capacity: Optional[int] = None):
        """
        :param str name: The name of the SKU. Possible values are `Dev(No SLA)_Standard_D11_v2`, `Dev(No SLA)_Standard_E2a_v4`, `Standard_D14_v2`, `Standard_D11_v2`, `Standard_D16d_v5`, `Standard_D13_v2`, `Standard_D12_v2`, `Standard_DS14_v2+4TB_PS`, `Standard_DS14_v2+3TB_PS`, `Standard_DS13_v2+1TB_PS`, `Standard_DS13_v2+2TB_PS`, `Standard_D32d_v5`, `Standard_D32d_v4`, `Standard_EC8ads_v5`, `Standard_EC8as_v5+1TB_PS`, `Standard_EC8as_v5+2TB_PS`, `Standard_EC16ads_v5`, `Standard_EC16as_v5+4TB_PS`, `Standard_EC16as_v5+3TB_PS`, `Standard_E80ids_v4`, `Standard_E8a_v4`, `Standard_E8ads_v5`, `Standard_E8as_v5+1TB_PS`, `Standard_E8as_v5+2TB_PS`, `Standard_E8as_v4+1TB_PS`, `Standard_E8as_v4+2TB_PS`, `Standard_E8d_v5`, `Standard_E8d_v4`, `Standard_E8s_v5+1TB_PS`, `Standard_E8s_v5+2TB_PS`, `Standard_E8s_v4+1TB_PS`, `Standard_E8s_v4+2TB_PS`, `Standard_E4a_v4`, `Standard_E4ads_v5`, `Standard_E4d_v5`, `Standard_E4d_v4`, `Standard_E16a_v4`, `Standard_E16ads_v5`, `Standard_E16as_v5+4TB_PS`, `Standard_E16as_v5+3TB_PS`, `Standard_E16as_v4+4TB_PS`, `Standard_E16as_v4+3TB_PS`, `Standard_E16d_v5`, `Standard_E16d_v4`, `Standard_E16s_v5+4TB_PS`, `Standard_E16s_v5+3TB_PS`, `Standard_E16s_v4+4TB_PS`, `Standard_E16s_v4+3TB_PS`, `Standard_E64i_v3`, `Standard_E2a_v4`, `Standard_E2ads_v5`, `Standard_E2d_v5`, `Standard_E2d_v4`, `Standard_L8as_v3`, `Standard_L8s`, `Standard_L8s_v3`, `Standard_L8s_v2`, `Standard_L4s`, `Standard_L16as_v3`, `Standard_L16s`, `Standard_L16s_v3`, `Standard_L16s_v2`, `Standard_L32as_v3` and `Standard_L32s_v3`.
        :param int capacity: Specifies the node count for the cluster. Boundaries depend on the SKU name.
               
               > **NOTE:** If no `optimized_auto_scale` block is defined, then the capacity is required.
               > **NOTE:** If an `optimized_auto_scale` block is defined and no capacity is set, then the capacity is initially set to the value of `minimum_instances`.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU. Possible values are `Dev(No SLA)_Standard_D11_v2`, `Dev(No SLA)_Standard_E2a_v4`, `Standard_D14_v2`, `Standard_D11_v2`, `Standard_D16d_v5`, `Standard_D13_v2`, `Standard_D12_v2`, `Standard_DS14_v2+4TB_PS`, `Standard_DS14_v2+3TB_PS`, `Standard_DS13_v2+1TB_PS`, `Standard_DS13_v2+2TB_PS`, `Standard_D32d_v5`, `Standard_D32d_v4`, `Standard_EC8ads_v5`, `Standard_EC8as_v5+1TB_PS`, `Standard_EC8as_v5+2TB_PS`, `Standard_EC16ads_v5`, `Standard_EC16as_v5+4TB_PS`, `Standard_EC16as_v5+3TB_PS`, `Standard_E80ids_v4`, `Standard_E8a_v4`, `Standard_E8ads_v5`, `Standard_E8as_v5+1TB_PS`, `Standard_E8as_v5+2TB_PS`, `Standard_E8as_v4+1TB_PS`, `Standard_E8as_v4+2TB_PS`, `Standard_E8d_v5`, `Standard_E8d_v4`, `Standard_E8s_v5+1TB_PS`, `Standard_E8s_v5+2TB_PS`, `Standard_E8s_v4+1TB_PS`, `Standard_E8s_v4+2TB_PS`, `Standard_E4a_v4`, `Standard_E4ads_v5`, `Standard_E4d_v5`, `Standard_E4d_v4`, `Standard_E16a_v4`, `Standard_E16ads_v5`, `Standard_E16as_v5+4TB_PS`, `Standard_E16as_v5+3TB_PS`, `Standard_E16as_v4+4TB_PS`, `Standard_E16as_v4+3TB_PS`, `Standard_E16d_v5`, `Standard_E16d_v4`, `Standard_E16s_v5+4TB_PS`, `Standard_E16s_v5+3TB_PS`, `Standard_E16s_v4+4TB_PS`, `Standard_E16s_v4+3TB_PS`, `Standard_E64i_v3`, `Standard_E2a_v4`, `Standard_E2ads_v5`, `Standard_E2d_v5`, `Standard_E2d_v4`, `Standard_L8as_v3`, `Standard_L8s`, `Standard_L8s_v3`, `Standard_L8s_v2`, `Standard_L4s`, `Standard_L16as_v3`, `Standard_L16s`, `Standard_L16s_v3`, `Standard_L16s_v2`, `Standard_L32as_v3` and `Standard_L32s_v3`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        Specifies the node count for the cluster. Boundaries depend on the SKU name.

        > **NOTE:** If no `optimized_auto_scale` block is defined, then the capacity is required.
        > **NOTE:** If an `optimized_auto_scale` block is defined and no capacity is set, then the capacity is initially set to the value of `minimum_instances`.
        """
        return pulumi.get(self, "capacity")


@pulumi.output_type
class ClusterVirtualNetworkConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataManagementPublicIpId":
            suggest = "data_management_public_ip_id"
        elif key == "enginePublicIpId":
            suggest = "engine_public_ip_id"
        elif key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterVirtualNetworkConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterVirtualNetworkConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterVirtualNetworkConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_management_public_ip_id: str,
                 engine_public_ip_id: str,
                 subnet_id: str):
        """
        :param str data_management_public_ip_id: Data management's service public IP address resource id.
        :param str engine_public_ip_id: Engine service's public IP address resource id.
        :param str subnet_id: The subnet resource id.
        """
        pulumi.set(__self__, "data_management_public_ip_id", data_management_public_ip_id)
        pulumi.set(__self__, "engine_public_ip_id", engine_public_ip_id)
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="dataManagementPublicIpId")
    def data_management_public_ip_id(self) -> str:
        """
        Data management's service public IP address resource id.
        """
        return pulumi.get(self, "data_management_public_ip_id")

    @property
    @pulumi.getter(name="enginePublicIpId")
    def engine_public_ip_id(self) -> str:
        """
        Engine service's public IP address resource id.
        """
        return pulumi.get(self, "engine_public_ip_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The subnet resource id.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class GetClusterIdentityResult(dict):
    def __init__(__self__, *,
                 identity_ids: Sequence[str],
                 principal_id: str,
                 tenant_id: str,
                 type: str):
        """
        :param Sequence[str] identity_ids: A list of User Assigned Managed Identity IDs to be assigned to this Kusto Cluster.
        :param str principal_id: The Principal ID associated with this System Assigned Managed Service Identity.
        :param str tenant_id: The Tenant ID associated with this System Assigned Managed Service Identity.
        :param str type: The type of Managed Service Identity that is configured on this Kusto Cluster.
        """
        pulumi.set(__self__, "identity_ids", identity_ids)
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> Sequence[str]:
        """
        A list of User Assigned Managed Identity IDs to be assigned to this Kusto Cluster.
        """
        return pulumi.get(self, "identity_ids")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The Principal ID associated with this System Assigned Managed Service Identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The Tenant ID associated with this System Assigned Managed Service Identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Managed Service Identity that is configured on this Kusto Cluster.
        """
        return pulumi.get(self, "type")


