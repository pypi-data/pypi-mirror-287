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

__all__ = ['EncryptedTextArgs', 'EncryptedText']

@pulumi.input_type
class EncryptedTextArgs:
    def __init__(__self__, *,
                 secret_manager_id: pulumi.Input[str],
                 inherit_scopes_from_secret_manager: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scoped_to_account: Optional[pulumi.Input[bool]] = None,
                 secret_reference: Optional[pulumi.Input[str]] = None,
                 usage_scopes: Optional[pulumi.Input[Sequence[pulumi.Input['EncryptedTextUsageScopeArgs']]]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EncryptedText resource.
        :param pulumi.Input[str] secret_manager_id: The id of the secret manager to associate the secret with. Once set, this field cannot be changed.
        :param pulumi.Input[bool] inherit_scopes_from_secret_manager: Boolean that indicates whether or not to inherit the usage scopes from the secret manager
        :param pulumi.Input[str] name: Name of the encrypted text secret
        :param pulumi.Input[bool] scoped_to_account: Boolean that indicates whether or not the secret is scoped to the account
        :param pulumi.Input[str] secret_reference: Name of the existing secret. If you already have secrets created in a secrets manager such as HashiCorp Vault or AWS Secrets Manager, you do not need to re-create the existing secrets in Harness.
        :param pulumi.Input[Sequence[pulumi.Input['EncryptedTextUsageScopeArgs']]] usage_scopes: This block is used for scoping the resource to a specific set of applications or environments.
        :param pulumi.Input[str] value: The value of the secret.
        """
        pulumi.set(__self__, "secret_manager_id", secret_manager_id)
        if inherit_scopes_from_secret_manager is not None:
            pulumi.set(__self__, "inherit_scopes_from_secret_manager", inherit_scopes_from_secret_manager)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scoped_to_account is not None:
            pulumi.set(__self__, "scoped_to_account", scoped_to_account)
        if secret_reference is not None:
            pulumi.set(__self__, "secret_reference", secret_reference)
        if usage_scopes is not None:
            pulumi.set(__self__, "usage_scopes", usage_scopes)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="secretManagerId")
    def secret_manager_id(self) -> pulumi.Input[str]:
        """
        The id of the secret manager to associate the secret with. Once set, this field cannot be changed.
        """
        return pulumi.get(self, "secret_manager_id")

    @secret_manager_id.setter
    def secret_manager_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret_manager_id", value)

    @property
    @pulumi.getter(name="inheritScopesFromSecretManager")
    def inherit_scopes_from_secret_manager(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean that indicates whether or not to inherit the usage scopes from the secret manager
        """
        return pulumi.get(self, "inherit_scopes_from_secret_manager")

    @inherit_scopes_from_secret_manager.setter
    def inherit_scopes_from_secret_manager(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "inherit_scopes_from_secret_manager", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the encrypted text secret
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="scopedToAccount")
    def scoped_to_account(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean that indicates whether or not the secret is scoped to the account
        """
        return pulumi.get(self, "scoped_to_account")

    @scoped_to_account.setter
    def scoped_to_account(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "scoped_to_account", value)

    @property
    @pulumi.getter(name="secretReference")
    def secret_reference(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the existing secret. If you already have secrets created in a secrets manager such as HashiCorp Vault or AWS Secrets Manager, you do not need to re-create the existing secrets in Harness.
        """
        return pulumi.get(self, "secret_reference")

    @secret_reference.setter
    def secret_reference(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_reference", value)

    @property
    @pulumi.getter(name="usageScopes")
    def usage_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EncryptedTextUsageScopeArgs']]]]:
        """
        This block is used for scoping the resource to a specific set of applications or environments.
        """
        return pulumi.get(self, "usage_scopes")

    @usage_scopes.setter
    def usage_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EncryptedTextUsageScopeArgs']]]]):
        pulumi.set(self, "usage_scopes", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the secret.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class _EncryptedTextState:
    def __init__(__self__, *,
                 inherit_scopes_from_secret_manager: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scoped_to_account: Optional[pulumi.Input[bool]] = None,
                 secret_manager_id: Optional[pulumi.Input[str]] = None,
                 secret_reference: Optional[pulumi.Input[str]] = None,
                 usage_scopes: Optional[pulumi.Input[Sequence[pulumi.Input['EncryptedTextUsageScopeArgs']]]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EncryptedText resources.
        :param pulumi.Input[bool] inherit_scopes_from_secret_manager: Boolean that indicates whether or not to inherit the usage scopes from the secret manager
        :param pulumi.Input[str] name: Name of the encrypted text secret
        :param pulumi.Input[bool] scoped_to_account: Boolean that indicates whether or not the secret is scoped to the account
        :param pulumi.Input[str] secret_manager_id: The id of the secret manager to associate the secret with. Once set, this field cannot be changed.
        :param pulumi.Input[str] secret_reference: Name of the existing secret. If you already have secrets created in a secrets manager such as HashiCorp Vault or AWS Secrets Manager, you do not need to re-create the existing secrets in Harness.
        :param pulumi.Input[Sequence[pulumi.Input['EncryptedTextUsageScopeArgs']]] usage_scopes: This block is used for scoping the resource to a specific set of applications or environments.
        :param pulumi.Input[str] value: The value of the secret.
        """
        if inherit_scopes_from_secret_manager is not None:
            pulumi.set(__self__, "inherit_scopes_from_secret_manager", inherit_scopes_from_secret_manager)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scoped_to_account is not None:
            pulumi.set(__self__, "scoped_to_account", scoped_to_account)
        if secret_manager_id is not None:
            pulumi.set(__self__, "secret_manager_id", secret_manager_id)
        if secret_reference is not None:
            pulumi.set(__self__, "secret_reference", secret_reference)
        if usage_scopes is not None:
            pulumi.set(__self__, "usage_scopes", usage_scopes)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="inheritScopesFromSecretManager")
    def inherit_scopes_from_secret_manager(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean that indicates whether or not to inherit the usage scopes from the secret manager
        """
        return pulumi.get(self, "inherit_scopes_from_secret_manager")

    @inherit_scopes_from_secret_manager.setter
    def inherit_scopes_from_secret_manager(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "inherit_scopes_from_secret_manager", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the encrypted text secret
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="scopedToAccount")
    def scoped_to_account(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean that indicates whether or not the secret is scoped to the account
        """
        return pulumi.get(self, "scoped_to_account")

    @scoped_to_account.setter
    def scoped_to_account(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "scoped_to_account", value)

    @property
    @pulumi.getter(name="secretManagerId")
    def secret_manager_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the secret manager to associate the secret with. Once set, this field cannot be changed.
        """
        return pulumi.get(self, "secret_manager_id")

    @secret_manager_id.setter
    def secret_manager_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_manager_id", value)

    @property
    @pulumi.getter(name="secretReference")
    def secret_reference(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the existing secret. If you already have secrets created in a secrets manager such as HashiCorp Vault or AWS Secrets Manager, you do not need to re-create the existing secrets in Harness.
        """
        return pulumi.get(self, "secret_reference")

    @secret_reference.setter
    def secret_reference(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_reference", value)

    @property
    @pulumi.getter(name="usageScopes")
    def usage_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EncryptedTextUsageScopeArgs']]]]:
        """
        This block is used for scoping the resource to a specific set of applications or environments.
        """
        return pulumi.get(self, "usage_scopes")

    @usage_scopes.setter
    def usage_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EncryptedTextUsageScopeArgs']]]]):
        pulumi.set(self, "usage_scopes", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the secret.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class EncryptedText(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 inherit_scopes_from_secret_manager: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scoped_to_account: Optional[pulumi.Input[bool]] = None,
                 secret_manager_id: Optional[pulumi.Input[str]] = None,
                 secret_reference: Optional[pulumi.Input[str]] = None,
                 usage_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EncryptedTextUsageScopeArgs']]]]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for creating an encrypted text secret

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        default = harness.get_secret_manager(default=True)
        example = harness.EncryptedText("example",
            name="example-secret",
            value="someval",
            secret_manager_id=default.id,
            usage_scopes=[
                harness.EncryptedTextUsageScopeArgs(
                    environment_filter_type="PRODUCTION_ENVIRONMENTS",
                ),
                harness.EncryptedTextUsageScopeArgs(
                    environment_filter_type="NON_PRODUCTION_ENVIRONMENTS",
                ),
            ])
        ```

        ## Import

        Import using the Harness encrypted text format.

        NOTE: The secret value cannot be decrypted and imported.

        ```sh
        $ pulumi import harness:index/encryptedText:EncryptedText example <secret_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] inherit_scopes_from_secret_manager: Boolean that indicates whether or not to inherit the usage scopes from the secret manager
        :param pulumi.Input[str] name: Name of the encrypted text secret
        :param pulumi.Input[bool] scoped_to_account: Boolean that indicates whether or not the secret is scoped to the account
        :param pulumi.Input[str] secret_manager_id: The id of the secret manager to associate the secret with. Once set, this field cannot be changed.
        :param pulumi.Input[str] secret_reference: Name of the existing secret. If you already have secrets created in a secrets manager such as HashiCorp Vault or AWS Secrets Manager, you do not need to re-create the existing secrets in Harness.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EncryptedTextUsageScopeArgs']]]] usage_scopes: This block is used for scoping the resource to a specific set of applications or environments.
        :param pulumi.Input[str] value: The value of the secret.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EncryptedTextArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for creating an encrypted text secret

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        default = harness.get_secret_manager(default=True)
        example = harness.EncryptedText("example",
            name="example-secret",
            value="someval",
            secret_manager_id=default.id,
            usage_scopes=[
                harness.EncryptedTextUsageScopeArgs(
                    environment_filter_type="PRODUCTION_ENVIRONMENTS",
                ),
                harness.EncryptedTextUsageScopeArgs(
                    environment_filter_type="NON_PRODUCTION_ENVIRONMENTS",
                ),
            ])
        ```

        ## Import

        Import using the Harness encrypted text format.

        NOTE: The secret value cannot be decrypted and imported.

        ```sh
        $ pulumi import harness:index/encryptedText:EncryptedText example <secret_id>
        ```

        :param str resource_name: The name of the resource.
        :param EncryptedTextArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EncryptedTextArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 inherit_scopes_from_secret_manager: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scoped_to_account: Optional[pulumi.Input[bool]] = None,
                 secret_manager_id: Optional[pulumi.Input[str]] = None,
                 secret_reference: Optional[pulumi.Input[str]] = None,
                 usage_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EncryptedTextUsageScopeArgs']]]]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EncryptedTextArgs.__new__(EncryptedTextArgs)

            __props__.__dict__["inherit_scopes_from_secret_manager"] = inherit_scopes_from_secret_manager
            __props__.__dict__["name"] = name
            __props__.__dict__["scoped_to_account"] = scoped_to_account
            if secret_manager_id is None and not opts.urn:
                raise TypeError("Missing required property 'secret_manager_id'")
            __props__.__dict__["secret_manager_id"] = secret_manager_id
            __props__.__dict__["secret_reference"] = secret_reference
            __props__.__dict__["usage_scopes"] = usage_scopes
            __props__.__dict__["value"] = None if value is None else pulumi.Output.secret(value)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["value"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(EncryptedText, __self__).__init__(
            'harness:index/encryptedText:EncryptedText',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            inherit_scopes_from_secret_manager: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            scoped_to_account: Optional[pulumi.Input[bool]] = None,
            secret_manager_id: Optional[pulumi.Input[str]] = None,
            secret_reference: Optional[pulumi.Input[str]] = None,
            usage_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EncryptedTextUsageScopeArgs']]]]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'EncryptedText':
        """
        Get an existing EncryptedText resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] inherit_scopes_from_secret_manager: Boolean that indicates whether or not to inherit the usage scopes from the secret manager
        :param pulumi.Input[str] name: Name of the encrypted text secret
        :param pulumi.Input[bool] scoped_to_account: Boolean that indicates whether or not the secret is scoped to the account
        :param pulumi.Input[str] secret_manager_id: The id of the secret manager to associate the secret with. Once set, this field cannot be changed.
        :param pulumi.Input[str] secret_reference: Name of the existing secret. If you already have secrets created in a secrets manager such as HashiCorp Vault or AWS Secrets Manager, you do not need to re-create the existing secrets in Harness.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EncryptedTextUsageScopeArgs']]]] usage_scopes: This block is used for scoping the resource to a specific set of applications or environments.
        :param pulumi.Input[str] value: The value of the secret.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EncryptedTextState.__new__(_EncryptedTextState)

        __props__.__dict__["inherit_scopes_from_secret_manager"] = inherit_scopes_from_secret_manager
        __props__.__dict__["name"] = name
        __props__.__dict__["scoped_to_account"] = scoped_to_account
        __props__.__dict__["secret_manager_id"] = secret_manager_id
        __props__.__dict__["secret_reference"] = secret_reference
        __props__.__dict__["usage_scopes"] = usage_scopes
        __props__.__dict__["value"] = value
        return EncryptedText(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="inheritScopesFromSecretManager")
    def inherit_scopes_from_secret_manager(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean that indicates whether or not to inherit the usage scopes from the secret manager
        """
        return pulumi.get(self, "inherit_scopes_from_secret_manager")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the encrypted text secret
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scopedToAccount")
    def scoped_to_account(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean that indicates whether or not the secret is scoped to the account
        """
        return pulumi.get(self, "scoped_to_account")

    @property
    @pulumi.getter(name="secretManagerId")
    def secret_manager_id(self) -> pulumi.Output[str]:
        """
        The id of the secret manager to associate the secret with. Once set, this field cannot be changed.
        """
        return pulumi.get(self, "secret_manager_id")

    @property
    @pulumi.getter(name="secretReference")
    def secret_reference(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the existing secret. If you already have secrets created in a secrets manager such as HashiCorp Vault or AWS Secrets Manager, you do not need to re-create the existing secrets in Harness.
        """
        return pulumi.get(self, "secret_reference")

    @property
    @pulumi.getter(name="usageScopes")
    def usage_scopes(self) -> pulumi.Output[Optional[Sequence['outputs.EncryptedTextUsageScope']]]:
        """
        This block is used for scoping the resource to a specific set of applications or environments.
        """
        return pulumi.get(self, "usage_scopes")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[str]]:
        """
        The value of the secret.
        """
        return pulumi.get(self, "value")

