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

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['ProviderPolicyArgs']]]] = None,
                 policy_signing_certificate_data: Optional[pulumi.Input[str]] = None,
                 sev_snp_policy_base64: Optional[pulumi.Input[str]] = None,
                 sgx_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tpm_policy_base64: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the attestation provider should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: The Azure Region where the Attestation Provider should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Attestation Provider. Changing this forces a new resource to be created.
        :param pulumi.Input[str] open_enclave_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[str] policy_signing_certificate_data: A valid X.509 certificate (Section 4 of [RFC4648](https://tools.ietf.org/html/rfc4648)). Changing this forces a new resource to be created.
               
               > **NOTE:** If the `policy_signing_certificate_data` argument contains more than one valid X.509 certificate only the first certificate will be used.
        :param pulumi.Input[str] sev_snp_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
               
               > [More information on the JWT Policies can be found in this article on `learn.microsoft.com`](https://learn.microsoft.com/azure/attestation/author-sign-policy).
        :param pulumi.Input[str] sgx_enclave_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Attestation Provider.
        :param pulumi.Input[str] tpm_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if open_enclave_policy_base64 is not None:
            pulumi.set(__self__, "open_enclave_policy_base64", open_enclave_policy_base64)
        if policies is not None:
            warnings.warn("""This field is no longer used and will be removed in v4.0 of the Azure Provider - use `open_enclave_policy_base64`, `sgx_enclave_policy_base64`, `tpm_policy_base64` and `sev_snp_policy_base64` instead.""", DeprecationWarning)
            pulumi.log.warn("""policies is deprecated: This field is no longer used and will be removed in v4.0 of the Azure Provider - use `open_enclave_policy_base64`, `sgx_enclave_policy_base64`, `tpm_policy_base64` and `sev_snp_policy_base64` instead.""")
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if policy_signing_certificate_data is not None:
            pulumi.set(__self__, "policy_signing_certificate_data", policy_signing_certificate_data)
        if sev_snp_policy_base64 is not None:
            pulumi.set(__self__, "sev_snp_policy_base64", sev_snp_policy_base64)
        if sgx_enclave_policy_base64 is not None:
            pulumi.set(__self__, "sgx_enclave_policy_base64", sgx_enclave_policy_base64)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tpm_policy_base64 is not None:
            pulumi.set(__self__, "tpm_policy_base64", tpm_policy_base64)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the attestation provider should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Attestation Provider should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Attestation Provider. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="openEnclavePolicyBase64")
    def open_enclave_policy_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        return pulumi.get(self, "open_enclave_policy_base64")

    @open_enclave_policy_base64.setter
    def open_enclave_policy_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "open_enclave_policy_base64", value)

    @property
    @pulumi.getter
    @_utilities.deprecated("""This field is no longer used and will be removed in v4.0 of the Azure Provider - use `open_enclave_policy_base64`, `sgx_enclave_policy_base64`, `tpm_policy_base64` and `sev_snp_policy_base64` instead.""")
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProviderPolicyArgs']]]]:
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProviderPolicyArgs']]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter(name="policySigningCertificateData")
    def policy_signing_certificate_data(self) -> Optional[pulumi.Input[str]]:
        """
        A valid X.509 certificate (Section 4 of [RFC4648](https://tools.ietf.org/html/rfc4648)). Changing this forces a new resource to be created.

        > **NOTE:** If the `policy_signing_certificate_data` argument contains more than one valid X.509 certificate only the first certificate will be used.
        """
        return pulumi.get(self, "policy_signing_certificate_data")

    @policy_signing_certificate_data.setter
    def policy_signing_certificate_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_signing_certificate_data", value)

    @property
    @pulumi.getter(name="sevSnpPolicyBase64")
    def sev_snp_policy_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.

        > [More information on the JWT Policies can be found in this article on `learn.microsoft.com`](https://learn.microsoft.com/azure/attestation/author-sign-policy).
        """
        return pulumi.get(self, "sev_snp_policy_base64")

    @sev_snp_policy_base64.setter
    def sev_snp_policy_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sev_snp_policy_base64", value)

    @property
    @pulumi.getter(name="sgxEnclavePolicyBase64")
    def sgx_enclave_policy_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        return pulumi.get(self, "sgx_enclave_policy_base64")

    @sgx_enclave_policy_base64.setter
    def sgx_enclave_policy_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sgx_enclave_policy_base64", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Attestation Provider.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tpmPolicyBase64")
    def tpm_policy_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        return pulumi.get(self, "tpm_policy_base64")

    @tpm_policy_base64.setter
    def tpm_policy_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tpm_policy_base64", value)


@pulumi.input_type
class _ProviderState:
    def __init__(__self__, *,
                 attestation_uri: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['ProviderPolicyArgs']]]] = None,
                 policy_signing_certificate_data: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sev_snp_policy_base64: Optional[pulumi.Input[str]] = None,
                 sgx_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tpm_policy_base64: Optional[pulumi.Input[str]] = None,
                 trust_model: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Provider resources.
        :param pulumi.Input[str] attestation_uri: The URI of the Attestation Service.
        :param pulumi.Input[str] location: The Azure Region where the Attestation Provider should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Attestation Provider. Changing this forces a new resource to be created.
        :param pulumi.Input[str] open_enclave_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[str] policy_signing_certificate_data: A valid X.509 certificate (Section 4 of [RFC4648](https://tools.ietf.org/html/rfc4648)). Changing this forces a new resource to be created.
               
               > **NOTE:** If the `policy_signing_certificate_data` argument contains more than one valid X.509 certificate only the first certificate will be used.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the attestation provider should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sev_snp_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
               
               > [More information on the JWT Policies can be found in this article on `learn.microsoft.com`](https://learn.microsoft.com/azure/attestation/author-sign-policy).
        :param pulumi.Input[str] sgx_enclave_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Attestation Provider.
        :param pulumi.Input[str] tpm_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[str] trust_model: Trust model used for the Attestation Service.
        """
        if attestation_uri is not None:
            pulumi.set(__self__, "attestation_uri", attestation_uri)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if open_enclave_policy_base64 is not None:
            pulumi.set(__self__, "open_enclave_policy_base64", open_enclave_policy_base64)
        if policies is not None:
            warnings.warn("""This field is no longer used and will be removed in v4.0 of the Azure Provider - use `open_enclave_policy_base64`, `sgx_enclave_policy_base64`, `tpm_policy_base64` and `sev_snp_policy_base64` instead.""", DeprecationWarning)
            pulumi.log.warn("""policies is deprecated: This field is no longer used and will be removed in v4.0 of the Azure Provider - use `open_enclave_policy_base64`, `sgx_enclave_policy_base64`, `tpm_policy_base64` and `sev_snp_policy_base64` instead.""")
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if policy_signing_certificate_data is not None:
            pulumi.set(__self__, "policy_signing_certificate_data", policy_signing_certificate_data)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sev_snp_policy_base64 is not None:
            pulumi.set(__self__, "sev_snp_policy_base64", sev_snp_policy_base64)
        if sgx_enclave_policy_base64 is not None:
            pulumi.set(__self__, "sgx_enclave_policy_base64", sgx_enclave_policy_base64)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tpm_policy_base64 is not None:
            pulumi.set(__self__, "tpm_policy_base64", tpm_policy_base64)
        if trust_model is not None:
            pulumi.set(__self__, "trust_model", trust_model)

    @property
    @pulumi.getter(name="attestationUri")
    def attestation_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the Attestation Service.
        """
        return pulumi.get(self, "attestation_uri")

    @attestation_uri.setter
    def attestation_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attestation_uri", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Attestation Provider should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Attestation Provider. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="openEnclavePolicyBase64")
    def open_enclave_policy_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        return pulumi.get(self, "open_enclave_policy_base64")

    @open_enclave_policy_base64.setter
    def open_enclave_policy_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "open_enclave_policy_base64", value)

    @property
    @pulumi.getter
    @_utilities.deprecated("""This field is no longer used and will be removed in v4.0 of the Azure Provider - use `open_enclave_policy_base64`, `sgx_enclave_policy_base64`, `tpm_policy_base64` and `sev_snp_policy_base64` instead.""")
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProviderPolicyArgs']]]]:
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProviderPolicyArgs']]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter(name="policySigningCertificateData")
    def policy_signing_certificate_data(self) -> Optional[pulumi.Input[str]]:
        """
        A valid X.509 certificate (Section 4 of [RFC4648](https://tools.ietf.org/html/rfc4648)). Changing this forces a new resource to be created.

        > **NOTE:** If the `policy_signing_certificate_data` argument contains more than one valid X.509 certificate only the first certificate will be used.
        """
        return pulumi.get(self, "policy_signing_certificate_data")

    @policy_signing_certificate_data.setter
    def policy_signing_certificate_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_signing_certificate_data", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the attestation provider should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sevSnpPolicyBase64")
    def sev_snp_policy_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.

        > [More information on the JWT Policies can be found in this article on `learn.microsoft.com`](https://learn.microsoft.com/azure/attestation/author-sign-policy).
        """
        return pulumi.get(self, "sev_snp_policy_base64")

    @sev_snp_policy_base64.setter
    def sev_snp_policy_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sev_snp_policy_base64", value)

    @property
    @pulumi.getter(name="sgxEnclavePolicyBase64")
    def sgx_enclave_policy_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        return pulumi.get(self, "sgx_enclave_policy_base64")

    @sgx_enclave_policy_base64.setter
    def sgx_enclave_policy_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sgx_enclave_policy_base64", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Attestation Provider.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tpmPolicyBase64")
    def tpm_policy_base64(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        return pulumi.get(self, "tpm_policy_base64")

    @tpm_policy_base64.setter
    def tpm_policy_base64(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tpm_policy_base64", value)

    @property
    @pulumi.getter(name="trustModel")
    def trust_model(self) -> Optional[pulumi.Input[str]]:
        """
        Trust model used for the Attestation Service.
        """
        return pulumi.get(self, "trust_model")

    @trust_model.setter
    def trust_model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trust_model", value)


class Provider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ProviderPolicyArgs', 'ProviderPolicyArgsDict']]]]] = None,
                 policy_signing_certificate_data: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sev_snp_policy_base64: Optional[pulumi.Input[str]] = None,
                 sgx_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tpm_policy_base64: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an Attestation Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_std as std

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_provider = azure.attestation.Provider("example",
            name="exampleprovider",
            resource_group_name=example.name,
            location=example.location,
            policy_signing_certificate_data=std.file(input="./example/cert.pem").result)
        ```

        ## Import

        Attestation Providers can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:attestation/provider:Provider example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Attestation/attestationProviders/provider1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The Azure Region where the Attestation Provider should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Attestation Provider. Changing this forces a new resource to be created.
        :param pulumi.Input[str] open_enclave_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[str] policy_signing_certificate_data: A valid X.509 certificate (Section 4 of [RFC4648](https://tools.ietf.org/html/rfc4648)). Changing this forces a new resource to be created.
               
               > **NOTE:** If the `policy_signing_certificate_data` argument contains more than one valid X.509 certificate only the first certificate will be used.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the attestation provider should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sev_snp_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
               
               > [More information on the JWT Policies can be found in this article on `learn.microsoft.com`](https://learn.microsoft.com/azure/attestation/author-sign-policy).
        :param pulumi.Input[str] sgx_enclave_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Attestation Provider.
        :param pulumi.Input[str] tpm_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Attestation Provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_std as std

        example = azure.core.ResourceGroup("example",
            name="example-resources",
            location="West Europe")
        example_provider = azure.attestation.Provider("example",
            name="exampleprovider",
            resource_group_name=example.name,
            location=example.location,
            policy_signing_certificate_data=std.file(input="./example/cert.pem").result)
        ```

        ## Import

        Attestation Providers can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import azure:attestation/provider:Provider example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Attestation/attestationProviders/provider1
        ```

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 open_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ProviderPolicyArgs', 'ProviderPolicyArgsDict']]]]] = None,
                 policy_signing_certificate_data: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sev_snp_policy_base64: Optional[pulumi.Input[str]] = None,
                 sgx_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tpm_policy_base64: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["open_enclave_policy_base64"] = open_enclave_policy_base64
            __props__.__dict__["policies"] = policies
            __props__.__dict__["policy_signing_certificate_data"] = policy_signing_certificate_data
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sev_snp_policy_base64"] = sev_snp_policy_base64
            __props__.__dict__["sgx_enclave_policy_base64"] = sgx_enclave_policy_base64
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tpm_policy_base64"] = tpm_policy_base64
            __props__.__dict__["attestation_uri"] = None
            __props__.__dict__["trust_model"] = None
        super(Provider, __self__).__init__(
            'azure:attestation/provider:Provider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attestation_uri: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            open_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
            policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ProviderPolicyArgs', 'ProviderPolicyArgsDict']]]]] = None,
            policy_signing_certificate_data: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            sev_snp_policy_base64: Optional[pulumi.Input[str]] = None,
            sgx_enclave_policy_base64: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tpm_policy_base64: Optional[pulumi.Input[str]] = None,
            trust_model: Optional[pulumi.Input[str]] = None) -> 'Provider':
        """
        Get an existing Provider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] attestation_uri: The URI of the Attestation Service.
        :param pulumi.Input[str] location: The Azure Region where the Attestation Provider should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name which should be used for this Attestation Provider. Changing this forces a new resource to be created.
        :param pulumi.Input[str] open_enclave_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[str] policy_signing_certificate_data: A valid X.509 certificate (Section 4 of [RFC4648](https://tools.ietf.org/html/rfc4648)). Changing this forces a new resource to be created.
               
               > **NOTE:** If the `policy_signing_certificate_data` argument contains more than one valid X.509 certificate only the first certificate will be used.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the attestation provider should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sev_snp_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
               
               > [More information on the JWT Policies can be found in this article on `learn.microsoft.com`](https://learn.microsoft.com/azure/attestation/author-sign-policy).
        :param pulumi.Input[str] sgx_enclave_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Attestation Provider.
        :param pulumi.Input[str] tpm_policy_base64: Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        :param pulumi.Input[str] trust_model: Trust model used for the Attestation Service.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProviderState.__new__(_ProviderState)

        __props__.__dict__["attestation_uri"] = attestation_uri
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["open_enclave_policy_base64"] = open_enclave_policy_base64
        __props__.__dict__["policies"] = policies
        __props__.__dict__["policy_signing_certificate_data"] = policy_signing_certificate_data
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["sev_snp_policy_base64"] = sev_snp_policy_base64
        __props__.__dict__["sgx_enclave_policy_base64"] = sgx_enclave_policy_base64
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tpm_policy_base64"] = tpm_policy_base64
        __props__.__dict__["trust_model"] = trust_model
        return Provider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attestationUri")
    def attestation_uri(self) -> pulumi.Output[str]:
        """
        The URI of the Attestation Service.
        """
        return pulumi.get(self, "attestation_uri")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Attestation Provider should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Attestation Provider. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="openEnclavePolicyBase64")
    def open_enclave_policy_base64(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        return pulumi.get(self, "open_enclave_policy_base64")

    @property
    @pulumi.getter
    @_utilities.deprecated("""This field is no longer used and will be removed in v4.0 of the Azure Provider - use `open_enclave_policy_base64`, `sgx_enclave_policy_base64`, `tpm_policy_base64` and `sev_snp_policy_base64` instead.""")
    def policies(self) -> pulumi.Output[Optional[Sequence['outputs.ProviderPolicy']]]:
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter(name="policySigningCertificateData")
    def policy_signing_certificate_data(self) -> pulumi.Output[Optional[str]]:
        """
        A valid X.509 certificate (Section 4 of [RFC4648](https://tools.ietf.org/html/rfc4648)). Changing this forces a new resource to be created.

        > **NOTE:** If the `policy_signing_certificate_data` argument contains more than one valid X.509 certificate only the first certificate will be used.
        """
        return pulumi.get(self, "policy_signing_certificate_data")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the attestation provider should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="sevSnpPolicyBase64")
    def sev_snp_policy_base64(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.

        > [More information on the JWT Policies can be found in this article on `learn.microsoft.com`](https://learn.microsoft.com/azure/attestation/author-sign-policy).
        """
        return pulumi.get(self, "sev_snp_policy_base64")

    @property
    @pulumi.getter(name="sgxEnclavePolicyBase64")
    def sgx_enclave_policy_base64(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        return pulumi.get(self, "sgx_enclave_policy_base64")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Attestation Provider.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tpmPolicyBase64")
    def tpm_policy_base64(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the base64 URI Encoded RFC 7519 JWT that should be used for the Attestation Policy.
        """
        return pulumi.get(self, "tpm_policy_base64")

    @property
    @pulumi.getter(name="trustModel")
    def trust_model(self) -> pulumi.Output[str]:
        """
        Trust model used for the Attestation Service.
        """
        return pulumi.get(self, "trust_model")

