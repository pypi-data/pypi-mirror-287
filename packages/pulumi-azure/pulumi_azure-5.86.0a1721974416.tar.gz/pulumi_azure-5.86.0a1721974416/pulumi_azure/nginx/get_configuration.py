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

__all__ = [
    'GetConfigurationResult',
    'AwaitableGetConfigurationResult',
    'get_configuration',
    'get_configuration_output',
]

@pulumi.output_type
class GetConfigurationResult:
    """
    A collection of values returned by getConfiguration.
    """
    def __init__(__self__, config_files=None, id=None, nginx_deployment_id=None, package_data=None, protected_files=None, root_file=None):
        if config_files and not isinstance(config_files, list):
            raise TypeError("Expected argument 'config_files' to be a list")
        pulumi.set(__self__, "config_files", config_files)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if nginx_deployment_id and not isinstance(nginx_deployment_id, str):
            raise TypeError("Expected argument 'nginx_deployment_id' to be a str")
        pulumi.set(__self__, "nginx_deployment_id", nginx_deployment_id)
        if package_data and not isinstance(package_data, str):
            raise TypeError("Expected argument 'package_data' to be a str")
        pulumi.set(__self__, "package_data", package_data)
        if protected_files and not isinstance(protected_files, list):
            raise TypeError("Expected argument 'protected_files' to be a list")
        pulumi.set(__self__, "protected_files", protected_files)
        if root_file and not isinstance(root_file, str):
            raise TypeError("Expected argument 'root_file' to be a str")
        pulumi.set(__self__, "root_file", root_file)

    @property
    @pulumi.getter(name="configFiles")
    def config_files(self) -> Sequence['outputs.GetConfigurationConfigFileResult']:
        """
        A `config_file` block as defined below.
        """
        return pulumi.get(self, "config_files")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nginxDeploymentId")
    def nginx_deployment_id(self) -> str:
        return pulumi.get(self, "nginx_deployment_id")

    @property
    @pulumi.getter(name="packageData")
    def package_data(self) -> str:
        """
        The package data for this configuration.
        """
        return pulumi.get(self, "package_data")

    @property
    @pulumi.getter(name="protectedFiles")
    def protected_files(self) -> Sequence['outputs.GetConfigurationProtectedFileResult']:
        return pulumi.get(self, "protected_files")

    @property
    @pulumi.getter(name="rootFile")
    def root_file(self) -> str:
        """
        The root file path of this Nginx Configuration.
        """
        return pulumi.get(self, "root_file")


class AwaitableGetConfigurationResult(GetConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationResult(
            config_files=self.config_files,
            id=self.id,
            nginx_deployment_id=self.nginx_deployment_id,
            package_data=self.package_data,
            protected_files=self.protected_files,
            root_file=self.root_file)


def get_configuration(nginx_deployment_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationResult:
    """
    Use this data source to access information about an existing Nginx Configuration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.nginx.get_configuration(nginx_deployment_id=example_azurerm_nginx_deployment["id"])
    pulumi.export("id", example.id)
    ```


    :param str nginx_deployment_id: The ID of the Nginx Deployment.
    """
    __args__ = dict()
    __args__['nginxDeploymentId'] = nginx_deployment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:nginx/getConfiguration:getConfiguration', __args__, opts=opts, typ=GetConfigurationResult).value

    return AwaitableGetConfigurationResult(
        config_files=pulumi.get(__ret__, 'config_files'),
        id=pulumi.get(__ret__, 'id'),
        nginx_deployment_id=pulumi.get(__ret__, 'nginx_deployment_id'),
        package_data=pulumi.get(__ret__, 'package_data'),
        protected_files=pulumi.get(__ret__, 'protected_files'),
        root_file=pulumi.get(__ret__, 'root_file'))


@_utilities.lift_output_func(get_configuration)
def get_configuration_output(nginx_deployment_id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationResult]:
    """
    Use this data source to access information about an existing Nginx Configuration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.nginx.get_configuration(nginx_deployment_id=example_azurerm_nginx_deployment["id"])
    pulumi.export("id", example.id)
    ```


    :param str nginx_deployment_id: The ID of the Nginx Deployment.
    """
    ...
