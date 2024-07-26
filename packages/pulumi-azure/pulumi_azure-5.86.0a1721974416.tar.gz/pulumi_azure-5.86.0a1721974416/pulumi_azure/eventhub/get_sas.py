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
    'GetSasResult',
    'AwaitableGetSasResult',
    'get_sas',
    'get_sas_output',
]

@pulumi.output_type
class GetSasResult:
    """
    A collection of values returned by getSas.
    """
    def __init__(__self__, connection_string=None, expiry=None, id=None, sas=None):
        if connection_string and not isinstance(connection_string, str):
            raise TypeError("Expected argument 'connection_string' to be a str")
        pulumi.set(__self__, "connection_string", connection_string)
        if expiry and not isinstance(expiry, str):
            raise TypeError("Expected argument 'expiry' to be a str")
        pulumi.set(__self__, "expiry", expiry)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sas and not isinstance(sas, str):
            raise TypeError("Expected argument 'sas' to be a str")
        pulumi.set(__self__, "sas", sas)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def expiry(self) -> str:
        return pulumi.get(self, "expiry")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def sas(self) -> str:
        """
        The computed Event Hub Shared Access Signature (SAS).
        """
        return pulumi.get(self, "sas")


class AwaitableGetSasResult(GetSasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSasResult(
            connection_string=self.connection_string,
            expiry=self.expiry,
            id=self.id,
            sas=self.sas)


def get_sas(connection_string: Optional[str] = None,
            expiry: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSasResult:
    """
    Use this data source to obtain a Shared Access Signature (SAS Token) for an existing Event Hub.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example_resource_group = azure.core.ResourceGroup("example",
        name="example-resources",
        location="West Europe")
    example_event_hub_namespace = azure.eventhub.EventHubNamespace("example",
        name="example-ehn",
        location=example_resource_group.location,
        resource_group_name=example_resource_group.name,
        sku="Basic")
    example_event_hub = azure.eventhub.EventHub("example",
        name="example-eh",
        namespace_name=example_event_hub_namespace.name,
        resource_group_name=example_resource_group.name,
        partition_count=1,
        message_retention=1)
    example_authorization_rule = azure.eventhub.AuthorizationRule("example",
        name="example-ehar",
        namespace_name=example_event_hub_namespace.name,
        eventhub_name=example_event_hub.name,
        resource_group_name=example_resource_group.name,
        listen=True,
        send=True,
        manage=True)
    example = azure.eventhub.get_authorization_rule_output(name=example_authorization_rule.name,
        namespace_name=example_event_hub_namespace.name,
        eventhub_name=example_event_hub.name,
        resource_group_name=example_resource_group.name)
    example_get_sas = example.apply(lambda example: azure.eventhub.get_sas_output(connection_string=example.primary_connection_string,
        expiry="2023-06-23T00:00:00Z"))
    ```


    :param str connection_string: The connection string for the Event Hub to which this SAS applies.
    :param str expiry: The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.
    """
    __args__ = dict()
    __args__['connectionString'] = connection_string
    __args__['expiry'] = expiry
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:eventhub/getSas:getSas', __args__, opts=opts, typ=GetSasResult).value

    return AwaitableGetSasResult(
        connection_string=pulumi.get(__ret__, 'connection_string'),
        expiry=pulumi.get(__ret__, 'expiry'),
        id=pulumi.get(__ret__, 'id'),
        sas=pulumi.get(__ret__, 'sas'))


@_utilities.lift_output_func(get_sas)
def get_sas_output(connection_string: Optional[pulumi.Input[str]] = None,
                   expiry: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSasResult]:
    """
    Use this data source to obtain a Shared Access Signature (SAS Token) for an existing Event Hub.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example_resource_group = azure.core.ResourceGroup("example",
        name="example-resources",
        location="West Europe")
    example_event_hub_namespace = azure.eventhub.EventHubNamespace("example",
        name="example-ehn",
        location=example_resource_group.location,
        resource_group_name=example_resource_group.name,
        sku="Basic")
    example_event_hub = azure.eventhub.EventHub("example",
        name="example-eh",
        namespace_name=example_event_hub_namespace.name,
        resource_group_name=example_resource_group.name,
        partition_count=1,
        message_retention=1)
    example_authorization_rule = azure.eventhub.AuthorizationRule("example",
        name="example-ehar",
        namespace_name=example_event_hub_namespace.name,
        eventhub_name=example_event_hub.name,
        resource_group_name=example_resource_group.name,
        listen=True,
        send=True,
        manage=True)
    example = azure.eventhub.get_authorization_rule_output(name=example_authorization_rule.name,
        namespace_name=example_event_hub_namespace.name,
        eventhub_name=example_event_hub.name,
        resource_group_name=example_resource_group.name)
    example_get_sas = example.apply(lambda example: azure.eventhub.get_sas_output(connection_string=example.primary_connection_string,
        expiry="2023-06-23T00:00:00Z"))
    ```


    :param str connection_string: The connection string for the Event Hub to which this SAS applies.
    :param str expiry: The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.
    """
    ...
