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
    'GetEnvironmentCertificateResult',
    'AwaitableGetEnvironmentCertificateResult',
    'get_environment_certificate',
    'get_environment_certificate_output',
]

@pulumi.output_type
class GetEnvironmentCertificateResult:
    """
    A collection of values returned by getEnvironmentCertificate.
    """
    def __init__(__self__, container_app_environment_id=None, expiration_date=None, id=None, issue_date=None, issuer=None, name=None, subject_name=None, tags=None, thumbprint=None):
        if container_app_environment_id and not isinstance(container_app_environment_id, str):
            raise TypeError("Expected argument 'container_app_environment_id' to be a str")
        pulumi.set(__self__, "container_app_environment_id", container_app_environment_id)
        if expiration_date and not isinstance(expiration_date, str):
            raise TypeError("Expected argument 'expiration_date' to be a str")
        pulumi.set(__self__, "expiration_date", expiration_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if issue_date and not isinstance(issue_date, str):
            raise TypeError("Expected argument 'issue_date' to be a str")
        pulumi.set(__self__, "issue_date", issue_date)
        if issuer and not isinstance(issuer, str):
            raise TypeError("Expected argument 'issuer' to be a str")
        pulumi.set(__self__, "issuer", issuer)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if subject_name and not isinstance(subject_name, str):
            raise TypeError("Expected argument 'subject_name' to be a str")
        pulumi.set(__self__, "subject_name", subject_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if thumbprint and not isinstance(thumbprint, str):
            raise TypeError("Expected argument 'thumbprint' to be a str")
        pulumi.set(__self__, "thumbprint", thumbprint)

    @property
    @pulumi.getter(name="containerAppEnvironmentId")
    def container_app_environment_id(self) -> str:
        return pulumi.get(self, "container_app_environment_id")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> str:
        """
        The expiration date for the Certificate.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="issueDate")
    def issue_date(self) -> str:
        """
        The date of issue for the Certificate.
        """
        return pulumi.get(self, "issue_date")

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        The Certificate Issuer.
        """
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> str:
        """
        The Subject Name for the Certificate.
        """
        return pulumi.get(self, "subject_name")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags assigned to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def thumbprint(self) -> str:
        """
        The Thumbprint of the Certificate.
        """
        return pulumi.get(self, "thumbprint")


class AwaitableGetEnvironmentCertificateResult(GetEnvironmentCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentCertificateResult(
            container_app_environment_id=self.container_app_environment_id,
            expiration_date=self.expiration_date,
            id=self.id,
            issue_date=self.issue_date,
            issuer=self.issuer,
            name=self.name,
            subject_name=self.subject_name,
            tags=self.tags,
            thumbprint=self.thumbprint)


def get_environment_certificate(container_app_environment_id: Optional[str] = None,
                                name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentCertificateResult:
    """
    Use this data source to access information about an existing Container App Environment Certificate.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.containerapp.get_environment(name="example-environment",
        resource_group_name="example-resources")
    example_get_environment_certificate = azure.containerapp.get_environment_certificate(name="mycertificate",
        container_app_environment_id=example.id)
    ```


    :param str container_app_environment_id: The ID of the Container App Environment to configure this Certificate on. Changing this forces a new resource to be created.
    :param str name: The name of the Container Apps Certificate. Changing this forces a new resource to be created.
    """
    __args__ = dict()
    __args__['containerAppEnvironmentId'] = container_app_environment_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:containerapp/getEnvironmentCertificate:getEnvironmentCertificate', __args__, opts=opts, typ=GetEnvironmentCertificateResult).value

    return AwaitableGetEnvironmentCertificateResult(
        container_app_environment_id=pulumi.get(__ret__, 'container_app_environment_id'),
        expiration_date=pulumi.get(__ret__, 'expiration_date'),
        id=pulumi.get(__ret__, 'id'),
        issue_date=pulumi.get(__ret__, 'issue_date'),
        issuer=pulumi.get(__ret__, 'issuer'),
        name=pulumi.get(__ret__, 'name'),
        subject_name=pulumi.get(__ret__, 'subject_name'),
        tags=pulumi.get(__ret__, 'tags'),
        thumbprint=pulumi.get(__ret__, 'thumbprint'))


@_utilities.lift_output_func(get_environment_certificate)
def get_environment_certificate_output(container_app_environment_id: Optional[pulumi.Input[str]] = None,
                                       name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvironmentCertificateResult]:
    """
    Use this data source to access information about an existing Container App Environment Certificate.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.containerapp.get_environment(name="example-environment",
        resource_group_name="example-resources")
    example_get_environment_certificate = azure.containerapp.get_environment_certificate(name="mycertificate",
        container_app_environment_id=example.id)
    ```


    :param str container_app_environment_id: The ID of the Container App Environment to configure this Certificate on. Changing this forces a new resource to be created.
    :param str name: The name of the Container Apps Certificate. Changing this forces a new resource to be created.
    """
    ...
