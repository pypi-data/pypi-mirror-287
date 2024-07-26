# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['GitOpsGnupgArgs', 'GitOpsGnupg']

@pulumi.input_type
class GitOpsGnupgArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 agent_id: pulumi.Input[str],
                 requests: pulumi.Input[Sequence[pulumi.Input['GitOpsGnupgRequestArgs']]],
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GitOpsGnupg resource.
        :param pulumi.Input[str] account_id: Account Identifier for the GnuPG Key.
        :param pulumi.Input[str] agent_id: Agent identifier for the GnuPG Key.
        :param pulumi.Input[Sequence[pulumi.Input['GitOpsGnupgRequestArgs']]] requests: GnuPGPublicKey is a representation of a GnuPG public key
        :param pulumi.Input[str] org_id: Organization Identifier for the GnuPG Key.
        :param pulumi.Input[str] project_id: Project Identifier for the GnuPG Key.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "agent_id", agent_id)
        pulumi.set(__self__, "requests", requests)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        Account Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[str]:
        """
        Agent identifier for the GnuPG Key.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter
    def requests(self) -> pulumi.Input[Sequence[pulumi.Input['GitOpsGnupgRequestArgs']]]:
        """
        GnuPGPublicKey is a representation of a GnuPG public key
        """
        return pulumi.get(self, "requests")

    @requests.setter
    def requests(self, value: pulumi.Input[Sequence[pulumi.Input['GitOpsGnupgRequestArgs']]]):
        pulumi.set(self, "requests", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        Organization Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


@pulumi.input_type
class _GitOpsGnupgState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 requests: Optional[pulumi.Input[Sequence[pulumi.Input['GitOpsGnupgRequestArgs']]]] = None):
        """
        Input properties used for looking up and filtering GitOpsGnupg resources.
        :param pulumi.Input[str] account_id: Account Identifier for the GnuPG Key.
        :param pulumi.Input[str] agent_id: Agent identifier for the GnuPG Key.
        :param pulumi.Input[str] identifier: Identifier for the GnuPG Key.
        :param pulumi.Input[str] org_id: Organization Identifier for the GnuPG Key.
        :param pulumi.Input[str] project_id: Project Identifier for the GnuPG Key.
        :param pulumi.Input[Sequence[pulumi.Input['GitOpsGnupgRequestArgs']]] requests: GnuPGPublicKey is a representation of a GnuPG public key
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if agent_id is not None:
            pulumi.set(__self__, "agent_id", agent_id)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if requests is not None:
            pulumi.set(__self__, "requests", requests)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Account Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[str]]:
        """
        Agent identifier for the GnuPG Key.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        Organization Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GitOpsGnupgRequestArgs']]]]:
        """
        GnuPGPublicKey is a representation of a GnuPG public key
        """
        return pulumi.get(self, "requests")

    @requests.setter
    def requests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GitOpsGnupgRequestArgs']]]]):
        pulumi.set(self, "requests", value)


class GitOpsGnupg(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 requests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsGnupgRequestArgs']]]]] = None,
                 __props__=None):
        """
        Resource for managing Harness GitOps GPG public key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        example = harness.platform.GitOpsGnupg("example",
            account_id="account_id",
            agent_id="agent_id",
            requests=[harness.platform.GitOpsGnupgRequestArgs(
                upsert=True,
                publickeys=[harness.platform.GitOpsGnupgRequestPublickeyArgs(
                    key_data="-----BEGIN PGP PUBLIC KEY BLOCK-----XXXXXX-----END PGP PUBLIC KEY BLOCK-----",
                )],
            )])
        ```

        ## Import

        Import an Account level Gitops GnuPG Key

        ```sh
        $ pulumi import harness:platform/gitOpsGnupg:GitOpsGnupg example <agent_id>/<key_id>
        ```

        Import an Org level Gitops GnuPG Key

        ```sh
        $ pulumi import harness:platform/gitOpsGnupg:GitOpsGnupg example <organization_id>/<agent_id>/<key_id>
        ```

        Import a Project level Gitops GnuPG Key

        ```sh
        $ pulumi import harness:platform/gitOpsGnupg:GitOpsGnupg example <organization_id>/<project_id>/<agent_id>/<key_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account Identifier for the GnuPG Key.
        :param pulumi.Input[str] agent_id: Agent identifier for the GnuPG Key.
        :param pulumi.Input[str] org_id: Organization Identifier for the GnuPG Key.
        :param pulumi.Input[str] project_id: Project Identifier for the GnuPG Key.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsGnupgRequestArgs']]]] requests: GnuPGPublicKey is a representation of a GnuPG public key
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GitOpsGnupgArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing Harness GitOps GPG public key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        example = harness.platform.GitOpsGnupg("example",
            account_id="account_id",
            agent_id="agent_id",
            requests=[harness.platform.GitOpsGnupgRequestArgs(
                upsert=True,
                publickeys=[harness.platform.GitOpsGnupgRequestPublickeyArgs(
                    key_data="-----BEGIN PGP PUBLIC KEY BLOCK-----XXXXXX-----END PGP PUBLIC KEY BLOCK-----",
                )],
            )])
        ```

        ## Import

        Import an Account level Gitops GnuPG Key

        ```sh
        $ pulumi import harness:platform/gitOpsGnupg:GitOpsGnupg example <agent_id>/<key_id>
        ```

        Import an Org level Gitops GnuPG Key

        ```sh
        $ pulumi import harness:platform/gitOpsGnupg:GitOpsGnupg example <organization_id>/<agent_id>/<key_id>
        ```

        Import a Project level Gitops GnuPG Key

        ```sh
        $ pulumi import harness:platform/gitOpsGnupg:GitOpsGnupg example <organization_id>/<project_id>/<agent_id>/<key_id>
        ```

        :param str resource_name: The name of the resource.
        :param GitOpsGnupgArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GitOpsGnupgArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 requests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsGnupgRequestArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GitOpsGnupgArgs.__new__(GitOpsGnupgArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            if agent_id is None and not opts.urn:
                raise TypeError("Missing required property 'agent_id'")
            __props__.__dict__["agent_id"] = agent_id
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["project_id"] = project_id
            if requests is None and not opts.urn:
                raise TypeError("Missing required property 'requests'")
            __props__.__dict__["requests"] = requests
            __props__.__dict__["identifier"] = None
        super(GitOpsGnupg, __self__).__init__(
            'harness:platform/gitOpsGnupg:GitOpsGnupg',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            agent_id: Optional[pulumi.Input[str]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            requests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsGnupgRequestArgs']]]]] = None) -> 'GitOpsGnupg':
        """
        Get an existing GitOpsGnupg resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account Identifier for the GnuPG Key.
        :param pulumi.Input[str] agent_id: Agent identifier for the GnuPG Key.
        :param pulumi.Input[str] identifier: Identifier for the GnuPG Key.
        :param pulumi.Input[str] org_id: Organization Identifier for the GnuPG Key.
        :param pulumi.Input[str] project_id: Project Identifier for the GnuPG Key.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsGnupgRequestArgs']]]] requests: GnuPGPublicKey is a representation of a GnuPG public key
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GitOpsGnupgState.__new__(_GitOpsGnupgState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["agent_id"] = agent_id
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["requests"] = requests
        return GitOpsGnupg(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Account Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[str]:
        """
        Agent identifier for the GnuPG Key.
        """
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[Optional[str]]:
        """
        Organization Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[Optional[str]]:
        """
        Project Identifier for the GnuPG Key.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def requests(self) -> pulumi.Output[Sequence['outputs.GitOpsGnupgRequest']]:
        """
        GnuPGPublicKey is a representation of a GnuPG public key
        """
        return pulumi.get(self, "requests")

