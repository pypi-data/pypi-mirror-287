# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetSshCredentialResult',
    'AwaitableGetSshCredentialResult',
    'get_ssh_credential',
    'get_ssh_credential_output',
]

@pulumi.output_type
class GetSshCredentialResult:
    """
    A collection of values returned by getSshCredential.
    """
    def __init__(__self__, id=None, name=None, usage_scopes=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if usage_scopes and not isinstance(usage_scopes, list):
            raise TypeError("Expected argument 'usage_scopes' to be a list")
        pulumi.set(__self__, "usage_scopes", usage_scopes)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier of the secret manager
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the secret manager
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="usageScopes")
    def usage_scopes(self) -> Optional[Sequence['outputs.GetSshCredentialUsageScopeResult']]:
        """
        This block is used for scoping the resource to a specific set of applications or environments.
        """
        return pulumi.get(self, "usage_scopes")


class AwaitableGetSshCredentialResult(GetSshCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSshCredentialResult(
            id=self.id,
            name=self.name,
            usage_scopes=self.usage_scopes)


def get_ssh_credential(id: Optional[str] = None,
                       name: Optional[str] = None,
                       usage_scopes: Optional[Sequence[pulumi.InputType['GetSshCredentialUsageScopeArgs']]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSshCredentialResult:
    """
    Data source for retrieving an SSH credential.


    :param str id: Unique identifier of the secret manager
    :param str name: The name of the secret manager
    :param Sequence[pulumi.InputType['GetSshCredentialUsageScopeArgs']] usage_scopes: This block is used for scoping the resource to a specific set of applications or environments.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['usageScopes'] = usage_scopes
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('harness:index/getSshCredential:getSshCredential', __args__, opts=opts, typ=GetSshCredentialResult).value

    return AwaitableGetSshCredentialResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        usage_scopes=pulumi.get(__ret__, 'usage_scopes'))


@_utilities.lift_output_func(get_ssh_credential)
def get_ssh_credential_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                              name: Optional[pulumi.Input[Optional[str]]] = None,
                              usage_scopes: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSshCredentialUsageScopeArgs']]]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSshCredentialResult]:
    """
    Data source for retrieving an SSH credential.


    :param str id: Unique identifier of the secret manager
    :param str name: The name of the secret manager
    :param Sequence[pulumi.InputType['GetSshCredentialUsageScopeArgs']] usage_scopes: This block is used for scoping the resource to a specific set of applications or environments.
    """
    ...
