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

__all__ = ['GitOpsRepoCertArgs', 'GitOpsRepoCert']

@pulumi.input_type
class GitOpsRepoCertArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 agent_id: pulumi.Input[str],
                 requests: pulumi.Input[Sequence[pulumi.Input['GitOpsRepoCertRequestArgs']]],
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GitOpsRepoCert resource.
        :param pulumi.Input[str] account_id: Account identifier of the GitOps repository certificate.
        :param pulumi.Input[str] agent_id: Agent identifier of the GitOps repository certificate.
        :param pulumi.Input[Sequence[pulumi.Input['GitOpsRepoCertRequestArgs']]] requests: Repository Certificate create/update request.
        :param pulumi.Input[str] org_id: Organization identifier of the GitOps repository certificate.
        :param pulumi.Input[str] project_id: Project identifier of the GitOps repository certificate.
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
        Account identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[str]:
        """
        Agent identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter
    def requests(self) -> pulumi.Input[Sequence[pulumi.Input['GitOpsRepoCertRequestArgs']]]:
        """
        Repository Certificate create/update request.
        """
        return pulumi.get(self, "requests")

    @requests.setter
    def requests(self, value: pulumi.Input[Sequence[pulumi.Input['GitOpsRepoCertRequestArgs']]]):
        pulumi.set(self, "requests", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        Organization identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


@pulumi.input_type
class _GitOpsRepoCertState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 requests: Optional[pulumi.Input[Sequence[pulumi.Input['GitOpsRepoCertRequestArgs']]]] = None):
        """
        Input properties used for looking up and filtering GitOpsRepoCert resources.
        :param pulumi.Input[str] account_id: Account identifier of the GitOps repository certificate.
        :param pulumi.Input[str] agent_id: Agent identifier of the GitOps repository certificate.
        :param pulumi.Input[str] org_id: Organization identifier of the GitOps repository certificate.
        :param pulumi.Input[str] project_id: Project identifier of the GitOps repository certificate.
        :param pulumi.Input[Sequence[pulumi.Input['GitOpsRepoCertRequestArgs']]] requests: Repository Certificate create/update request.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if agent_id is not None:
            pulumi.set(__self__, "agent_id", agent_id)
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
        Account identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[str]]:
        """
        Agent identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        Organization identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GitOpsRepoCertRequestArgs']]]]:
        """
        Repository Certificate create/update request.
        """
        return pulumi.get(self, "requests")

    @requests.setter
    def requests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GitOpsRepoCertRequestArgs']]]]):
        pulumi.set(self, "requests", value)


class GitOpsRepoCert(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 requests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsRepoCertRequestArgs']]]]] = None,
                 __props__=None):
        """
        Resource for managing a Harness Gitops Repository Certificate. You can only create 1 instance per agent which has all the certificates of this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        example = harness.platform.GitOpsRepoCert("example",
            requests=[harness.platform.GitOpsRepoCertRequestArgs(
                certificates=[harness.platform.GitOpsRepoCertRequestCertificateArgs(
                    metadatas=[harness.platform.GitOpsRepoCertRequestCertificateMetadataArgs()],
                    items=[harness.platform.GitOpsRepoCertRequestCertificateItemArgs(
                        server_name="github.com",
                        cert_type="ssh",
                        cert_sub_type="ecdsa-sha2-nistp256",
                        cert_data="QUFBQUUyVmpaSE5oTFhOb1lUSXRibWx6ZEhBeU5UWUFBQUFJYm1semRIQXlOVFlBQUFCQkJFbUtTRU5qUUVlek9teGtaTXk3b3BLZ3dGQjlua3Q1WVJyWU1qTnVHNU44N3VSZ2c2Q0xyYm81d0FkVC95NnYwbUtWMFUydzBXWjJZQi8rK1Rwb2NrZz0=",
                    )],
                )],
                upsert=True,
            )],
            account_id="account_id",
            agent_id="agent_id")
        ```

        ## Import

        Import an Account level Gitops Repository Certificate

        ```sh
        $ pulumi import harness:platform/gitOpsRepoCert:GitOpsRepoCert example <repocert_id>
        ```

        Import an Org level Gitops Repository Certificate

        ```sh
        $ pulumi import harness:platform/gitOpsRepoCert:GitOpsRepoCert example <organization_id>/<repocert_id>
        ```

        Import a Project level Gitops Repository Certificate

        ```sh
        $ pulumi import harness:platform/gitOpsRepoCert:GitOpsRepoCert example <organization_id>/<project_id>/<repocert_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account identifier of the GitOps repository certificate.
        :param pulumi.Input[str] agent_id: Agent identifier of the GitOps repository certificate.
        :param pulumi.Input[str] org_id: Organization identifier of the GitOps repository certificate.
        :param pulumi.Input[str] project_id: Project identifier of the GitOps repository certificate.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsRepoCertRequestArgs']]]] requests: Repository Certificate create/update request.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GitOpsRepoCertArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing a Harness Gitops Repository Certificate. You can only create 1 instance per agent which has all the certificates of this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        example = harness.platform.GitOpsRepoCert("example",
            requests=[harness.platform.GitOpsRepoCertRequestArgs(
                certificates=[harness.platform.GitOpsRepoCertRequestCertificateArgs(
                    metadatas=[harness.platform.GitOpsRepoCertRequestCertificateMetadataArgs()],
                    items=[harness.platform.GitOpsRepoCertRequestCertificateItemArgs(
                        server_name="github.com",
                        cert_type="ssh",
                        cert_sub_type="ecdsa-sha2-nistp256",
                        cert_data="QUFBQUUyVmpaSE5oTFhOb1lUSXRibWx6ZEhBeU5UWUFBQUFJYm1semRIQXlOVFlBQUFCQkJFbUtTRU5qUUVlek9teGtaTXk3b3BLZ3dGQjlua3Q1WVJyWU1qTnVHNU44N3VSZ2c2Q0xyYm81d0FkVC95NnYwbUtWMFUydzBXWjJZQi8rK1Rwb2NrZz0=",
                    )],
                )],
                upsert=True,
            )],
            account_id="account_id",
            agent_id="agent_id")
        ```

        ## Import

        Import an Account level Gitops Repository Certificate

        ```sh
        $ pulumi import harness:platform/gitOpsRepoCert:GitOpsRepoCert example <repocert_id>
        ```

        Import an Org level Gitops Repository Certificate

        ```sh
        $ pulumi import harness:platform/gitOpsRepoCert:GitOpsRepoCert example <organization_id>/<repocert_id>
        ```

        Import a Project level Gitops Repository Certificate

        ```sh
        $ pulumi import harness:platform/gitOpsRepoCert:GitOpsRepoCert example <organization_id>/<project_id>/<repocert_id>
        ```

        :param str resource_name: The name of the resource.
        :param GitOpsRepoCertArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GitOpsRepoCertArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 requests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsRepoCertRequestArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GitOpsRepoCertArgs.__new__(GitOpsRepoCertArgs)

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
        super(GitOpsRepoCert, __self__).__init__(
            'harness:platform/gitOpsRepoCert:GitOpsRepoCert',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            agent_id: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            requests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsRepoCertRequestArgs']]]]] = None) -> 'GitOpsRepoCert':
        """
        Get an existing GitOpsRepoCert resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account identifier of the GitOps repository certificate.
        :param pulumi.Input[str] agent_id: Agent identifier of the GitOps repository certificate.
        :param pulumi.Input[str] org_id: Organization identifier of the GitOps repository certificate.
        :param pulumi.Input[str] project_id: Project identifier of the GitOps repository certificate.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GitOpsRepoCertRequestArgs']]]] requests: Repository Certificate create/update request.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GitOpsRepoCertState.__new__(_GitOpsRepoCertState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["agent_id"] = agent_id
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["requests"] = requests
        return GitOpsRepoCert(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Account identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[str]:
        """
        Agent identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[Optional[str]]:
        """
        Organization identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[Optional[str]]:
        """
        Project identifier of the GitOps repository certificate.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def requests(self) -> pulumi.Output[Sequence['outputs.GitOpsRepoCertRequest']]:
        """
        Repository Certificate create/update request.
        """
        return pulumi.get(self, "requests")

