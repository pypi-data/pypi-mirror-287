# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetGitopsAppProjectResult',
    'AwaitableGetGitopsAppProjectResult',
    'get_gitops_app_project',
    'get_gitops_app_project_output',
]

@pulumi.output_type
class GetGitopsAppProjectResult:
    """
    A collection of values returned by getGitopsAppProject.
    """
    def __init__(__self__, account_id=None, agent_id=None, id=None, org_id=None, project_id=None, query_name=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if agent_id and not isinstance(agent_id, str):
            raise TypeError("Expected argument 'agent_id' to be a str")
        pulumi.set(__self__, "agent_id", agent_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if org_id and not isinstance(org_id, str):
            raise TypeError("Expected argument 'org_id' to be a str")
        pulumi.set(__self__, "org_id", org_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if query_name and not isinstance(query_name, str):
            raise TypeError("Expected argument 'query_name' to be a str")
        pulumi.set(__self__, "query_name", query_name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> str:
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[str]:
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="queryName")
    def query_name(self) -> str:
        return pulumi.get(self, "query_name")


class AwaitableGetGitopsAppProjectResult(GetGitopsAppProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGitopsAppProjectResult(
            account_id=self.account_id,
            agent_id=self.agent_id,
            id=self.id,
            org_id=self.org_id,
            project_id=self.project_id,
            query_name=self.query_name)


def get_gitops_app_project(account_id: Optional[str] = None,
                           agent_id: Optional[str] = None,
                           org_id: Optional[str] = None,
                           project_id: Optional[str] = None,
                           query_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGitopsAppProjectResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['agentId'] = agent_id
    __args__['orgId'] = org_id
    __args__['projectId'] = project_id
    __args__['queryName'] = query_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('harness:platform/getGitopsAppProject:getGitopsAppProject', __args__, opts=opts, typ=GetGitopsAppProjectResult).value

    return AwaitableGetGitopsAppProjectResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        agent_id=pulumi.get(__ret__, 'agent_id'),
        id=pulumi.get(__ret__, 'id'),
        org_id=pulumi.get(__ret__, 'org_id'),
        project_id=pulumi.get(__ret__, 'project_id'),
        query_name=pulumi.get(__ret__, 'query_name'))


@_utilities.lift_output_func(get_gitops_app_project)
def get_gitops_app_project_output(account_id: Optional[pulumi.Input[str]] = None,
                                  agent_id: Optional[pulumi.Input[str]] = None,
                                  org_id: Optional[pulumi.Input[Optional[str]]] = None,
                                  project_id: Optional[pulumi.Input[Optional[str]]] = None,
                                  query_name: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGitopsAppProjectResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
