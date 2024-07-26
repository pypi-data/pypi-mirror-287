# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GitopsAppProjectMappingArgs', 'GitopsAppProjectMapping']

@pulumi.input_type
class GitopsAppProjectMappingArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 agent_id: pulumi.Input[str],
                 argo_project_name: pulumi.Input[str],
                 org_id: pulumi.Input[str],
                 project_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a GitopsAppProjectMapping resource.
        :param pulumi.Input[str] account_id: Account identifier of the GitOps agent's Application Project.
        :param pulumi.Input[str] agent_id: Agent identifier for which the ArgoCD and Harness project mapping is to be created.
        :param pulumi.Input[str] argo_project_name: ArgoCD Project name which is to be mapped to the Harness project.
        :param pulumi.Input[str] org_id: Organization identifier of the GitOps agent's Application Project.
        :param pulumi.Input[str] project_id: Project identifier of the GitOps agent's Application Project.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "agent_id", agent_id)
        pulumi.set(__self__, "argo_project_name", argo_project_name)
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        Account identifier of the GitOps agent's Application Project.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[str]:
        """
        Agent identifier for which the ArgoCD and Harness project mapping is to be created.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="argoProjectName")
    def argo_project_name(self) -> pulumi.Input[str]:
        """
        ArgoCD Project name which is to be mapped to the Harness project.
        """
        return pulumi.get(self, "argo_project_name")

    @argo_project_name.setter
    def argo_project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "argo_project_name", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[str]:
        """
        Organization identifier of the GitOps agent's Application Project.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        Project identifier of the GitOps agent's Application Project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)


@pulumi.input_type
class _GitopsAppProjectMappingState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 argo_project_name: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GitopsAppProjectMapping resources.
        :param pulumi.Input[str] account_id: Account identifier of the GitOps agent's Application Project.
        :param pulumi.Input[str] agent_id: Agent identifier for which the ArgoCD and Harness project mapping is to be created.
        :param pulumi.Input[str] argo_project_name: ArgoCD Project name which is to be mapped to the Harness project.
        :param pulumi.Input[str] identifier: Identifier of the GitOps Application Project.
        :param pulumi.Input[str] org_id: Organization identifier of the GitOps agent's Application Project.
        :param pulumi.Input[str] project_id: Project identifier of the GitOps agent's Application Project.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if agent_id is not None:
            pulumi.set(__self__, "agent_id", agent_id)
        if argo_project_name is not None:
            pulumi.set(__self__, "argo_project_name", argo_project_name)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Account identifier of the GitOps agent's Application Project.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[str]]:
        """
        Agent identifier for which the ArgoCD and Harness project mapping is to be created.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="argoProjectName")
    def argo_project_name(self) -> Optional[pulumi.Input[str]]:
        """
        ArgoCD Project name which is to be mapped to the Harness project.
        """
        return pulumi.get(self, "argo_project_name")

    @argo_project_name.setter
    def argo_project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "argo_project_name", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the GitOps Application Project.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        Organization identifier of the GitOps agent's Application Project.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project identifier of the GitOps agent's Application Project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


class GitopsAppProjectMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 argo_project_name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for managing Harness GitOps Application Project Mappings.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        example = harness.platform.GitopsAppProjectMapping("example",
            account_id="account_id",
            org_id="organization_id",
            project_id="project_id",
            agent_id="agent_id",
            argo_project_name="argoProjectName")
        ```

        ## Import

        Import a GitOps agent app project mapping

        ```sh
        $ pulumi import harness:platform/gitopsAppProjectMapping:GitopsAppProjectMapping example <organization_id>/<project_id>/<agent_id>/<appproject_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account identifier of the GitOps agent's Application Project.
        :param pulumi.Input[str] agent_id: Agent identifier for which the ArgoCD and Harness project mapping is to be created.
        :param pulumi.Input[str] argo_project_name: ArgoCD Project name which is to be mapped to the Harness project.
        :param pulumi.Input[str] org_id: Organization identifier of the GitOps agent's Application Project.
        :param pulumi.Input[str] project_id: Project identifier of the GitOps agent's Application Project.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GitopsAppProjectMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing Harness GitOps Application Project Mappings.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        example = harness.platform.GitopsAppProjectMapping("example",
            account_id="account_id",
            org_id="organization_id",
            project_id="project_id",
            agent_id="agent_id",
            argo_project_name="argoProjectName")
        ```

        ## Import

        Import a GitOps agent app project mapping

        ```sh
        $ pulumi import harness:platform/gitopsAppProjectMapping:GitopsAppProjectMapping example <organization_id>/<project_id>/<agent_id>/<appproject_id>
        ```

        :param str resource_name: The name of the resource.
        :param GitopsAppProjectMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GitopsAppProjectMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 argo_project_name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GitopsAppProjectMappingArgs.__new__(GitopsAppProjectMappingArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            if agent_id is None and not opts.urn:
                raise TypeError("Missing required property 'agent_id'")
            __props__.__dict__["agent_id"] = agent_id
            if argo_project_name is None and not opts.urn:
                raise TypeError("Missing required property 'argo_project_name'")
            __props__.__dict__["argo_project_name"] = argo_project_name
            if org_id is None and not opts.urn:
                raise TypeError("Missing required property 'org_id'")
            __props__.__dict__["org_id"] = org_id
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["identifier"] = None
        super(GitopsAppProjectMapping, __self__).__init__(
            'harness:platform/gitopsAppProjectMapping:GitopsAppProjectMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            agent_id: Optional[pulumi.Input[str]] = None,
            argo_project_name: Optional[pulumi.Input[str]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None) -> 'GitopsAppProjectMapping':
        """
        Get an existing GitopsAppProjectMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account identifier of the GitOps agent's Application Project.
        :param pulumi.Input[str] agent_id: Agent identifier for which the ArgoCD and Harness project mapping is to be created.
        :param pulumi.Input[str] argo_project_name: ArgoCD Project name which is to be mapped to the Harness project.
        :param pulumi.Input[str] identifier: Identifier of the GitOps Application Project.
        :param pulumi.Input[str] org_id: Organization identifier of the GitOps agent's Application Project.
        :param pulumi.Input[str] project_id: Project identifier of the GitOps agent's Application Project.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GitopsAppProjectMappingState.__new__(_GitopsAppProjectMappingState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["agent_id"] = agent_id
        __props__.__dict__["argo_project_name"] = argo_project_name
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["project_id"] = project_id
        return GitopsAppProjectMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Account identifier of the GitOps agent's Application Project.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[str]:
        """
        Agent identifier for which the ArgoCD and Harness project mapping is to be created.
        """
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter(name="argoProjectName")
    def argo_project_name(self) -> pulumi.Output[str]:
        """
        ArgoCD Project name which is to be mapped to the Harness project.
        """
        return pulumi.get(self, "argo_project_name")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        Identifier of the GitOps Application Project.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[str]:
        """
        Organization identifier of the GitOps agent's Application Project.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        Project identifier of the GitOps agent's Application Project.
        """
        return pulumi.get(self, "project_id")

