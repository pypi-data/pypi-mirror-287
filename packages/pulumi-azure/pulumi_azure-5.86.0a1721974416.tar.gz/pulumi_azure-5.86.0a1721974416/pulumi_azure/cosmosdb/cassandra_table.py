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

__all__ = ['CassandraTableArgs', 'CassandraTable']

@pulumi.input_type
class CassandraTableArgs:
    def __init__(__self__, *,
                 cassandra_keyspace_id: pulumi.Input[str],
                 schema: pulumi.Input['CassandraTableSchemaArgs'],
                 analytical_storage_ttl: Optional[pulumi.Input[int]] = None,
                 autoscale_settings: Optional[pulumi.Input['CassandraTableAutoscaleSettingsArgs']] = None,
                 default_ttl: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 throughput: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a CassandraTable resource.
        :param pulumi.Input[str] cassandra_keyspace_id: The ID of the Cosmos DB Cassandra Keyspace to create the table within. Changing this forces a new resource to be created.
        :param pulumi.Input['CassandraTableSchemaArgs'] schema: A `schema` block as defined below.
        :param pulumi.Input[int] analytical_storage_ttl: Time to live of the Analytical Storage. Possible values are between `-1` and `2147483647` except `0`. `-1` means the Analytical Storage never expires. Changing this forces a new resource to be created.
               
               > **Note:** throughput has a maximum value of `1000000` unless a higher limit is requested via Azure Support
        :param pulumi.Input[int] default_ttl: Time to live of the Cosmos DB Cassandra table. Possible values are at least `-1`. `-1` means the Cassandra table never expires.
        :param pulumi.Input[str] name: Specifies the name of the Cosmos DB Cassandra Table. Changing this forces a new resource to be created.
        """
        pulumi.set(__self__, "cassandra_keyspace_id", cassandra_keyspace_id)
        pulumi.set(__self__, "schema", schema)
        if analytical_storage_ttl is not None:
            pulumi.set(__self__, "analytical_storage_ttl", analytical_storage_ttl)
        if autoscale_settings is not None:
            pulumi.set(__self__, "autoscale_settings", autoscale_settings)
        if default_ttl is not None:
            pulumi.set(__self__, "default_ttl", default_ttl)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if throughput is not None:
            pulumi.set(__self__, "throughput", throughput)

    @property
    @pulumi.getter(name="cassandraKeyspaceId")
    def cassandra_keyspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the Cosmos DB Cassandra Keyspace to create the table within. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cassandra_keyspace_id")

    @cassandra_keyspace_id.setter
    def cassandra_keyspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cassandra_keyspace_id", value)

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Input['CassandraTableSchemaArgs']:
        """
        A `schema` block as defined below.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: pulumi.Input['CassandraTableSchemaArgs']):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Time to live of the Analytical Storage. Possible values are between `-1` and `2147483647` except `0`. `-1` means the Analytical Storage never expires. Changing this forces a new resource to be created.

        > **Note:** throughput has a maximum value of `1000000` unless a higher limit is requested via Azure Support
        """
        return pulumi.get(self, "analytical_storage_ttl")

    @analytical_storage_ttl.setter
    def analytical_storage_ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "analytical_storage_ttl", value)

    @property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[pulumi.Input['CassandraTableAutoscaleSettingsArgs']]:
        return pulumi.get(self, "autoscale_settings")

    @autoscale_settings.setter
    def autoscale_settings(self, value: Optional[pulumi.Input['CassandraTableAutoscaleSettingsArgs']]):
        pulumi.set(self, "autoscale_settings", value)

    @property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Time to live of the Cosmos DB Cassandra table. Possible values are at least `-1`. `-1` means the Cassandra table never expires.
        """
        return pulumi.get(self, "default_ttl")

    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_ttl", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Cosmos DB Cassandra Table. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "throughput")

    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "throughput", value)


@pulumi.input_type
class _CassandraTableState:
    def __init__(__self__, *,
                 analytical_storage_ttl: Optional[pulumi.Input[int]] = None,
                 autoscale_settings: Optional[pulumi.Input['CassandraTableAutoscaleSettingsArgs']] = None,
                 cassandra_keyspace_id: Optional[pulumi.Input[str]] = None,
                 default_ttl: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input['CassandraTableSchemaArgs']] = None,
                 throughput: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering CassandraTable resources.
        :param pulumi.Input[int] analytical_storage_ttl: Time to live of the Analytical Storage. Possible values are between `-1` and `2147483647` except `0`. `-1` means the Analytical Storage never expires. Changing this forces a new resource to be created.
               
               > **Note:** throughput has a maximum value of `1000000` unless a higher limit is requested via Azure Support
        :param pulumi.Input[str] cassandra_keyspace_id: The ID of the Cosmos DB Cassandra Keyspace to create the table within. Changing this forces a new resource to be created.
        :param pulumi.Input[int] default_ttl: Time to live of the Cosmos DB Cassandra table. Possible values are at least `-1`. `-1` means the Cassandra table never expires.
        :param pulumi.Input[str] name: Specifies the name of the Cosmos DB Cassandra Table. Changing this forces a new resource to be created.
        :param pulumi.Input['CassandraTableSchemaArgs'] schema: A `schema` block as defined below.
        """
        if analytical_storage_ttl is not None:
            pulumi.set(__self__, "analytical_storage_ttl", analytical_storage_ttl)
        if autoscale_settings is not None:
            pulumi.set(__self__, "autoscale_settings", autoscale_settings)
        if cassandra_keyspace_id is not None:
            pulumi.set(__self__, "cassandra_keyspace_id", cassandra_keyspace_id)
        if default_ttl is not None:
            pulumi.set(__self__, "default_ttl", default_ttl)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if throughput is not None:
            pulumi.set(__self__, "throughput", throughput)

    @property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Time to live of the Analytical Storage. Possible values are between `-1` and `2147483647` except `0`. `-1` means the Analytical Storage never expires. Changing this forces a new resource to be created.

        > **Note:** throughput has a maximum value of `1000000` unless a higher limit is requested via Azure Support
        """
        return pulumi.get(self, "analytical_storage_ttl")

    @analytical_storage_ttl.setter
    def analytical_storage_ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "analytical_storage_ttl", value)

    @property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> Optional[pulumi.Input['CassandraTableAutoscaleSettingsArgs']]:
        return pulumi.get(self, "autoscale_settings")

    @autoscale_settings.setter
    def autoscale_settings(self, value: Optional[pulumi.Input['CassandraTableAutoscaleSettingsArgs']]):
        pulumi.set(self, "autoscale_settings", value)

    @property
    @pulumi.getter(name="cassandraKeyspaceId")
    def cassandra_keyspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Cosmos DB Cassandra Keyspace to create the table within. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cassandra_keyspace_id")

    @cassandra_keyspace_id.setter
    def cassandra_keyspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cassandra_keyspace_id", value)

    @property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Time to live of the Cosmos DB Cassandra table. Possible values are at least `-1`. `-1` means the Cassandra table never expires.
        """
        return pulumi.get(self, "default_ttl")

    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_ttl", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the Cosmos DB Cassandra Table. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input['CassandraTableSchemaArgs']]:
        """
        A `schema` block as defined below.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input['CassandraTableSchemaArgs']]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter
    def throughput(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "throughput")

    @throughput.setter
    def throughput(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "throughput", value)


class CassandraTable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 analytical_storage_ttl: Optional[pulumi.Input[int]] = None,
                 autoscale_settings: Optional[pulumi.Input[Union['CassandraTableAutoscaleSettingsArgs', 'CassandraTableAutoscaleSettingsArgsDict']]] = None,
                 cassandra_keyspace_id: Optional[pulumi.Input[str]] = None,
                 default_ttl: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[Union['CassandraTableSchemaArgs', 'CassandraTableSchemaArgsDict']]] = None,
                 throughput: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Manages a Cassandra Table within a Cosmos DB Cassandra Keyspace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="tflex-cosmosdb-account-rg",
            location="West Europe")
        example_account = azure.cosmosdb.Account("example",
            name="tfex-cosmosdb-account",
            resource_group_name=example.name,
            location=example.location,
            offer_type="Standard",
            capabilities=[{
                "name": "EnableCassandra",
            }],
            consistency_policy={
                "consistency_level": "Strong",
            },
            geo_locations=[{
                "location": example.location,
                "failover_priority": 0,
            }])
        example_cassandra_keyspace = azure.cosmosdb.CassandraKeyspace("example",
            name="tfex-cosmos-cassandra-keyspace",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            throughput=400)
        example_cassandra_table = azure.cosmosdb.CassandraTable("example",
            name="testtable",
            cassandra_keyspace_id=example_cassandra_keyspace.id,
            schema={
                "columns": [
                    {
                        "name": "test1",
                        "type": "ascii",
                    },
                    {
                        "name": "test2",
                        "type": "int",
                    },
                ],
                "partition_keys": [{
                    "name": "test1",
                }],
            })
        ```

        ## Import

        Cosmos Cassandra Table can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:cosmosdb/cassandraTable:CassandraTable ks1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.DocumentDB/databaseAccounts/account1/cassandraKeyspaces/ks1/tables/table1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] analytical_storage_ttl: Time to live of the Analytical Storage. Possible values are between `-1` and `2147483647` except `0`. `-1` means the Analytical Storage never expires. Changing this forces a new resource to be created.
               
               > **Note:** throughput has a maximum value of `1000000` unless a higher limit is requested via Azure Support
        :param pulumi.Input[str] cassandra_keyspace_id: The ID of the Cosmos DB Cassandra Keyspace to create the table within. Changing this forces a new resource to be created.
        :param pulumi.Input[int] default_ttl: Time to live of the Cosmos DB Cassandra table. Possible values are at least `-1`. `-1` means the Cassandra table never expires.
        :param pulumi.Input[str] name: Specifies the name of the Cosmos DB Cassandra Table. Changing this forces a new resource to be created.
        :param pulumi.Input[Union['CassandraTableSchemaArgs', 'CassandraTableSchemaArgsDict']] schema: A `schema` block as defined below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CassandraTableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Cassandra Table within a Cosmos DB Cassandra Keyspace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example = azure.core.ResourceGroup("example",
            name="tflex-cosmosdb-account-rg",
            location="West Europe")
        example_account = azure.cosmosdb.Account("example",
            name="tfex-cosmosdb-account",
            resource_group_name=example.name,
            location=example.location,
            offer_type="Standard",
            capabilities=[{
                "name": "EnableCassandra",
            }],
            consistency_policy={
                "consistency_level": "Strong",
            },
            geo_locations=[{
                "location": example.location,
                "failover_priority": 0,
            }])
        example_cassandra_keyspace = azure.cosmosdb.CassandraKeyspace("example",
            name="tfex-cosmos-cassandra-keyspace",
            resource_group_name=example_account.resource_group_name,
            account_name=example_account.name,
            throughput=400)
        example_cassandra_table = azure.cosmosdb.CassandraTable("example",
            name="testtable",
            cassandra_keyspace_id=example_cassandra_keyspace.id,
            schema={
                "columns": [
                    {
                        "name": "test1",
                        "type": "ascii",
                    },
                    {
                        "name": "test2",
                        "type": "int",
                    },
                ],
                "partition_keys": [{
                    "name": "test1",
                }],
            })
        ```

        ## Import

        Cosmos Cassandra Table can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:cosmosdb/cassandraTable:CassandraTable ks1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.DocumentDB/databaseAccounts/account1/cassandraKeyspaces/ks1/tables/table1
        ```

        :param str resource_name: The name of the resource.
        :param CassandraTableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CassandraTableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 analytical_storage_ttl: Optional[pulumi.Input[int]] = None,
                 autoscale_settings: Optional[pulumi.Input[Union['CassandraTableAutoscaleSettingsArgs', 'CassandraTableAutoscaleSettingsArgsDict']]] = None,
                 cassandra_keyspace_id: Optional[pulumi.Input[str]] = None,
                 default_ttl: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[Union['CassandraTableSchemaArgs', 'CassandraTableSchemaArgsDict']]] = None,
                 throughput: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CassandraTableArgs.__new__(CassandraTableArgs)

            __props__.__dict__["analytical_storage_ttl"] = analytical_storage_ttl
            __props__.__dict__["autoscale_settings"] = autoscale_settings
            if cassandra_keyspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'cassandra_keyspace_id'")
            __props__.__dict__["cassandra_keyspace_id"] = cassandra_keyspace_id
            __props__.__dict__["default_ttl"] = default_ttl
            __props__.__dict__["name"] = name
            if schema is None and not opts.urn:
                raise TypeError("Missing required property 'schema'")
            __props__.__dict__["schema"] = schema
            __props__.__dict__["throughput"] = throughput
        super(CassandraTable, __self__).__init__(
            'azure:cosmosdb/cassandraTable:CassandraTable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            analytical_storage_ttl: Optional[pulumi.Input[int]] = None,
            autoscale_settings: Optional[pulumi.Input[Union['CassandraTableAutoscaleSettingsArgs', 'CassandraTableAutoscaleSettingsArgsDict']]] = None,
            cassandra_keyspace_id: Optional[pulumi.Input[str]] = None,
            default_ttl: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            schema: Optional[pulumi.Input[Union['CassandraTableSchemaArgs', 'CassandraTableSchemaArgsDict']]] = None,
            throughput: Optional[pulumi.Input[int]] = None) -> 'CassandraTable':
        """
        Get an existing CassandraTable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] analytical_storage_ttl: Time to live of the Analytical Storage. Possible values are between `-1` and `2147483647` except `0`. `-1` means the Analytical Storage never expires. Changing this forces a new resource to be created.
               
               > **Note:** throughput has a maximum value of `1000000` unless a higher limit is requested via Azure Support
        :param pulumi.Input[str] cassandra_keyspace_id: The ID of the Cosmos DB Cassandra Keyspace to create the table within. Changing this forces a new resource to be created.
        :param pulumi.Input[int] default_ttl: Time to live of the Cosmos DB Cassandra table. Possible values are at least `-1`. `-1` means the Cassandra table never expires.
        :param pulumi.Input[str] name: Specifies the name of the Cosmos DB Cassandra Table. Changing this forces a new resource to be created.
        :param pulumi.Input[Union['CassandraTableSchemaArgs', 'CassandraTableSchemaArgsDict']] schema: A `schema` block as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CassandraTableState.__new__(_CassandraTableState)

        __props__.__dict__["analytical_storage_ttl"] = analytical_storage_ttl
        __props__.__dict__["autoscale_settings"] = autoscale_settings
        __props__.__dict__["cassandra_keyspace_id"] = cassandra_keyspace_id
        __props__.__dict__["default_ttl"] = default_ttl
        __props__.__dict__["name"] = name
        __props__.__dict__["schema"] = schema
        __props__.__dict__["throughput"] = throughput
        return CassandraTable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="analyticalStorageTtl")
    def analytical_storage_ttl(self) -> pulumi.Output[Optional[int]]:
        """
        Time to live of the Analytical Storage. Possible values are between `-1` and `2147483647` except `0`. `-1` means the Analytical Storage never expires. Changing this forces a new resource to be created.

        > **Note:** throughput has a maximum value of `1000000` unless a higher limit is requested via Azure Support
        """
        return pulumi.get(self, "analytical_storage_ttl")

    @property
    @pulumi.getter(name="autoscaleSettings")
    def autoscale_settings(self) -> pulumi.Output[Optional['outputs.CassandraTableAutoscaleSettings']]:
        return pulumi.get(self, "autoscale_settings")

    @property
    @pulumi.getter(name="cassandraKeyspaceId")
    def cassandra_keyspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the Cosmos DB Cassandra Keyspace to create the table within. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "cassandra_keyspace_id")

    @property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> pulumi.Output[Optional[int]]:
        """
        Time to live of the Cosmos DB Cassandra table. Possible values are at least `-1`. `-1` means the Cassandra table never expires.
        """
        return pulumi.get(self, "default_ttl")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Cosmos DB Cassandra Table. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output['outputs.CassandraTableSchema']:
        """
        A `schema` block as defined below.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter
    def throughput(self) -> pulumi.Output[int]:
        return pulumi.get(self, "throughput")

