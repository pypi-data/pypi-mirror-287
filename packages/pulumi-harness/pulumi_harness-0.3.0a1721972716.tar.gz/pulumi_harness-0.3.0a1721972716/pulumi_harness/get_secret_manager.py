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
    'GetSecretManagerResult',
    'AwaitableGetSecretManagerResult',
    'get_secret_manager',
    'get_secret_manager_output',
]

@pulumi.output_type
class GetSecretManagerResult:
    """
    A collection of values returned by getSecretManager.
    """
    def __init__(__self__, default=None, id=None, name=None, usage_scopes=None):
        if default and not isinstance(default, bool):
            raise TypeError("Expected argument 'default' to be a bool")
        pulumi.set(__self__, "default", default)
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
    def default(self) -> Optional[bool]:
        """
        True to lookup the id of the default secret manager
        """
        return pulumi.get(self, "default")

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
    def usage_scopes(self) -> Optional[Sequence['outputs.GetSecretManagerUsageScopeResult']]:
        """
        This block is used for scoping the resource to a specific set of applications or environments.
        """
        return pulumi.get(self, "usage_scopes")


class AwaitableGetSecretManagerResult(GetSecretManagerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretManagerResult(
            default=self.default,
            id=self.id,
            name=self.name,
            usage_scopes=self.usage_scopes)


def get_secret_manager(default: Optional[bool] = None,
                       id: Optional[str] = None,
                       name: Optional[str] = None,
                       usage_scopes: Optional[Sequence[pulumi.InputType['GetSecretManagerUsageScopeArgs']]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretManagerResult:
    """
    Data source for retrieving a Harness secret manager


    :param bool default: True to lookup the id of the default secret manager
    :param str id: Unique identifier of the secret manager
    :param str name: The name of the secret manager
    :param Sequence[pulumi.InputType['GetSecretManagerUsageScopeArgs']] usage_scopes: This block is used for scoping the resource to a specific set of applications or environments.
    """
    __args__ = dict()
    __args__['default'] = default
    __args__['id'] = id
    __args__['name'] = name
    __args__['usageScopes'] = usage_scopes
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('harness:index/getSecretManager:getSecretManager', __args__, opts=opts, typ=GetSecretManagerResult).value

    return AwaitableGetSecretManagerResult(
        default=pulumi.get(__ret__, 'default'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        usage_scopes=pulumi.get(__ret__, 'usage_scopes'))


@_utilities.lift_output_func(get_secret_manager)
def get_secret_manager_output(default: Optional[pulumi.Input[Optional[bool]]] = None,
                              id: Optional[pulumi.Input[Optional[str]]] = None,
                              name: Optional[pulumi.Input[Optional[str]]] = None,
                              usage_scopes: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSecretManagerUsageScopeArgs']]]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretManagerResult]:
    """
    Data source for retrieving a Harness secret manager


    :param bool default: True to lookup the id of the default secret manager
    :param str id: Unique identifier of the secret manager
    :param str name: The name of the secret manager
    :param Sequence[pulumi.InputType['GetSecretManagerUsageScopeArgs']] usage_scopes: This block is used for scoping the resource to a specific set of applications or environments.
    """
    ...
