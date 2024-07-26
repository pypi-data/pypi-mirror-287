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
    'GetEncryptedValueResult',
    'AwaitableGetEncryptedValueResult',
    'get_encrypted_value',
    'get_encrypted_value_output',
]

@pulumi.output_type
class GetEncryptedValueResult:
    """
    A collection of values returned by getEncryptedValue.
    """
    def __init__(__self__, algorithm=None, decoded_plain_text_value=None, encrypted_data=None, id=None, key_vault_key_id=None, plain_text_value=None):
        if algorithm and not isinstance(algorithm, str):
            raise TypeError("Expected argument 'algorithm' to be a str")
        pulumi.set(__self__, "algorithm", algorithm)
        if decoded_plain_text_value and not isinstance(decoded_plain_text_value, str):
            raise TypeError("Expected argument 'decoded_plain_text_value' to be a str")
        pulumi.set(__self__, "decoded_plain_text_value", decoded_plain_text_value)
        if encrypted_data and not isinstance(encrypted_data, str):
            raise TypeError("Expected argument 'encrypted_data' to be a str")
        pulumi.set(__self__, "encrypted_data", encrypted_data)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_vault_key_id and not isinstance(key_vault_key_id, str):
            raise TypeError("Expected argument 'key_vault_key_id' to be a str")
        pulumi.set(__self__, "key_vault_key_id", key_vault_key_id)
        if plain_text_value and not isinstance(plain_text_value, str):
            raise TypeError("Expected argument 'plain_text_value' to be a str")
        pulumi.set(__self__, "plain_text_value", plain_text_value)

    @property
    @pulumi.getter
    def algorithm(self) -> str:
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="decodedPlainTextValue")
    def decoded_plain_text_value(self) -> str:
        """
        The Base64URL decoded string of `plain_text_value`. Because the API would remove padding characters of `plain_text_value` when encrypting, this attribute is useful to get the original value.
        """
        return pulumi.get(self, "decoded_plain_text_value")

    @property
    @pulumi.getter(name="encryptedData")
    def encrypted_data(self) -> Optional[str]:
        return pulumi.get(self, "encrypted_data")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyVaultKeyId")
    def key_vault_key_id(self) -> str:
        return pulumi.get(self, "key_vault_key_id")

    @property
    @pulumi.getter(name="plainTextValue")
    def plain_text_value(self) -> Optional[str]:
        return pulumi.get(self, "plain_text_value")


class AwaitableGetEncryptedValueResult(GetEncryptedValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEncryptedValueResult(
            algorithm=self.algorithm,
            decoded_plain_text_value=self.decoded_plain_text_value,
            encrypted_data=self.encrypted_data,
            id=self.id,
            key_vault_key_id=self.key_vault_key_id,
            plain_text_value=self.plain_text_value)


def get_encrypted_value(algorithm: Optional[str] = None,
                        encrypted_data: Optional[str] = None,
                        key_vault_key_id: Optional[str] = None,
                        plain_text_value: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEncryptedValueResult:
    """
    Encrypts or Decrypts a value using a Key Vault Key.


    :param str algorithm: The Algorithm which should be used to Decrypt/Encrypt this Value. Possible values are `RSA1_5`, `RSA-OAEP` and `RSA-OAEP-256`.
    :param str encrypted_data: The Base64 URL Encoded Encrypted Data which should be decrypted into `plain_text_value`.
    :param str key_vault_key_id: The ID of the Key Vault Key which should be used to Decrypt/Encrypt this Value.
    :param str plain_text_value: The plain-text value which should be Encrypted into `encrypted_data`.
           
           > **Note:** One of either `encrypted_data` or `plain_text_value` must be specified and is used to populate the encrypted/decrypted value for the other field.
    """
    __args__ = dict()
    __args__['algorithm'] = algorithm
    __args__['encryptedData'] = encrypted_data
    __args__['keyVaultKeyId'] = key_vault_key_id
    __args__['plainTextValue'] = plain_text_value
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure:keyvault/getEncryptedValue:getEncryptedValue', __args__, opts=opts, typ=GetEncryptedValueResult).value

    return AwaitableGetEncryptedValueResult(
        algorithm=pulumi.get(__ret__, 'algorithm'),
        decoded_plain_text_value=pulumi.get(__ret__, 'decoded_plain_text_value'),
        encrypted_data=pulumi.get(__ret__, 'encrypted_data'),
        id=pulumi.get(__ret__, 'id'),
        key_vault_key_id=pulumi.get(__ret__, 'key_vault_key_id'),
        plain_text_value=pulumi.get(__ret__, 'plain_text_value'))


@_utilities.lift_output_func(get_encrypted_value)
def get_encrypted_value_output(algorithm: Optional[pulumi.Input[str]] = None,
                               encrypted_data: Optional[pulumi.Input[Optional[str]]] = None,
                               key_vault_key_id: Optional[pulumi.Input[str]] = None,
                               plain_text_value: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEncryptedValueResult]:
    """
    Encrypts or Decrypts a value using a Key Vault Key.


    :param str algorithm: The Algorithm which should be used to Decrypt/Encrypt this Value. Possible values are `RSA1_5`, `RSA-OAEP` and `RSA-OAEP-256`.
    :param str encrypted_data: The Base64 URL Encoded Encrypted Data which should be decrypted into `plain_text_value`.
    :param str key_vault_key_id: The ID of the Key Vault Key which should be used to Decrypt/Encrypt this Value.
    :param str plain_text_value: The plain-text value which should be Encrypted into `encrypted_data`.
           
           > **Note:** One of either `encrypted_data` or `plain_text_value` must be specified and is used to populate the encrypted/decrypted value for the other field.
    """
    ...
