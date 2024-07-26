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

__all__ = ['RepoRuleBranchArgs', 'RepoRuleBranch']

@pulumi.input_type
class RepoRuleBranchArgs:
    def __init__(__self__, *,
                 bypasses: pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchBypassArgs']]],
                 identifier: pulumi.Input[str],
                 policies: pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPolicyArgs']]],
                 repo_identifier: pulumi.Input[str],
                 state: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 patterns: Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPatternArgs']]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RepoRuleBranch resource.
        :param pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchBypassArgs']]] bypasses: List of users who can bypass this rule.
        :param pulumi.Input[str] identifier: Identifier of the rule.
        :param pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPolicyArgs']]] policies: Policies to be applied for this rule.
        :param pulumi.Input[str] repo_identifier: Repo identifier of the repository.
        :param pulumi.Input[str] state: State of the rule (active, disable, monitor).
        :param pulumi.Input[str] description: Description of the rule.
        :param pulumi.Input[str] org_id: Unique identifier of the organization.
        :param pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPatternArgs']]] patterns: Pattern of branch to which rule will apply.
        :param pulumi.Input[str] project_id: Unique identifier of the project.
        """
        pulumi.set(__self__, "bypasses", bypasses)
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "policies", policies)
        pulumi.set(__self__, "repo_identifier", repo_identifier)
        pulumi.set(__self__, "state", state)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if patterns is not None:
            pulumi.set(__self__, "patterns", patterns)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter
    def bypasses(self) -> pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchBypassArgs']]]:
        """
        List of users who can bypass this rule.
        """
        return pulumi.get(self, "bypasses")

    @bypasses.setter
    def bypasses(self, value: pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchBypassArgs']]]):
        pulumi.set(self, "bypasses", value)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        """
        Identifier of the rule.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPolicyArgs']]]:
        """
        Policies to be applied for this rule.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPolicyArgs']]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter(name="repoIdentifier")
    def repo_identifier(self) -> pulumi.Input[str]:
        """
        Repo identifier of the repository.
        """
        return pulumi.get(self, "repo_identifier")

    @repo_identifier.setter
    def repo_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "repo_identifier", value)

    @property
    @pulumi.getter
    def state(self) -> pulumi.Input[str]:
        """
        State of the rule (active, disable, monitor).
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: pulumi.Input[str]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the organization.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter
    def patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPatternArgs']]]]:
        """
        Pattern of branch to which rule will apply.
        """
        return pulumi.get(self, "patterns")

    @patterns.setter
    def patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPatternArgs']]]]):
        pulumi.set(self, "patterns", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


@pulumi.input_type
class _RepoRuleBranchState:
    def __init__(__self__, *,
                 bypasses: Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchBypassArgs']]]] = None,
                 created: Optional[pulumi.Input[int]] = None,
                 created_by: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 patterns: Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPatternArgs']]]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPolicyArgs']]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 repo_identifier: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 updated: Optional[pulumi.Input[int]] = None,
                 updated_by: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering RepoRuleBranch resources.
        :param pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchBypassArgs']]] bypasses: List of users who can bypass this rule.
        :param pulumi.Input[int] created: Timestamp when the rule was created.
        :param pulumi.Input[int] created_by: ID of the user who created the rule.
        :param pulumi.Input[str] description: Description of the rule.
        :param pulumi.Input[str] identifier: Identifier of the rule.
        :param pulumi.Input[str] org_id: Unique identifier of the organization.
        :param pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPatternArgs']]] patterns: Pattern of branch to which rule will apply.
        :param pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPolicyArgs']]] policies: Policies to be applied for this rule.
        :param pulumi.Input[str] project_id: Unique identifier of the project.
        :param pulumi.Input[str] repo_identifier: Repo identifier of the repository.
        :param pulumi.Input[str] state: State of the rule (active, disable, monitor).
        :param pulumi.Input[int] updated: Timestamp when the rule was updated.
        :param pulumi.Input[int] updated_by: ID of the user who updated the rule.
        """
        if bypasses is not None:
            pulumi.set(__self__, "bypasses", bypasses)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if patterns is not None:
            pulumi.set(__self__, "patterns", patterns)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if repo_identifier is not None:
            pulumi.set(__self__, "repo_identifier", repo_identifier)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if updated is not None:
            pulumi.set(__self__, "updated", updated)
        if updated_by is not None:
            pulumi.set(__self__, "updated_by", updated_by)

    @property
    @pulumi.getter
    def bypasses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchBypassArgs']]]]:
        """
        List of users who can bypass this rule.
        """
        return pulumi.get(self, "bypasses")

    @bypasses.setter
    def bypasses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchBypassArgs']]]]):
        pulumi.set(self, "bypasses", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[int]]:
        """
        Timestamp when the rule was created.
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the user who created the rule.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the rule.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the organization.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter
    def patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPatternArgs']]]]:
        """
        Pattern of branch to which rule will apply.
        """
        return pulumi.get(self, "patterns")

    @patterns.setter
    def patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPatternArgs']]]]):
        pulumi.set(self, "patterns", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPolicyArgs']]]]:
        """
        Policies to be applied for this rule.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RepoRuleBranchPolicyArgs']]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="repoIdentifier")
    def repo_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Repo identifier of the repository.
        """
        return pulumi.get(self, "repo_identifier")

    @repo_identifier.setter
    def repo_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_identifier", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of the rule (active, disable, monitor).
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def updated(self) -> Optional[pulumi.Input[int]]:
        """
        Timestamp when the rule was updated.
        """
        return pulumi.get(self, "updated")

    @updated.setter
    def updated(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "updated", value)

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the user who updated the rule.
        """
        return pulumi.get(self, "updated_by")

    @updated_by.setter
    def updated_by(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "updated_by", value)


class RepoRuleBranch(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchBypassArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 patterns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPatternArgs']]]]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPolicyArgs']]]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 repo_identifier: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for creating a Harness Repo Branch Rule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchBypassArgs']]]] bypasses: List of users who can bypass this rule.
        :param pulumi.Input[str] description: Description of the rule.
        :param pulumi.Input[str] identifier: Identifier of the rule.
        :param pulumi.Input[str] org_id: Unique identifier of the organization.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPatternArgs']]]] patterns: Pattern of branch to which rule will apply.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPolicyArgs']]]] policies: Policies to be applied for this rule.
        :param pulumi.Input[str] project_id: Unique identifier of the project.
        :param pulumi.Input[str] repo_identifier: Repo identifier of the repository.
        :param pulumi.Input[str] state: State of the rule (active, disable, monitor).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepoRuleBranchArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for creating a Harness Repo Branch Rule.

        :param str resource_name: The name of the resource.
        :param RepoRuleBranchArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepoRuleBranchArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchBypassArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 patterns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPatternArgs']]]]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPolicyArgs']]]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 repo_identifier: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RepoRuleBranchArgs.__new__(RepoRuleBranchArgs)

            if bypasses is None and not opts.urn:
                raise TypeError("Missing required property 'bypasses'")
            __props__.__dict__["bypasses"] = bypasses
            __props__.__dict__["description"] = description
            if identifier is None and not opts.urn:
                raise TypeError("Missing required property 'identifier'")
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["patterns"] = patterns
            if policies is None and not opts.urn:
                raise TypeError("Missing required property 'policies'")
            __props__.__dict__["policies"] = policies
            __props__.__dict__["project_id"] = project_id
            if repo_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'repo_identifier'")
            __props__.__dict__["repo_identifier"] = repo_identifier
            if state is None and not opts.urn:
                raise TypeError("Missing required property 'state'")
            __props__.__dict__["state"] = state
            __props__.__dict__["created"] = None
            __props__.__dict__["created_by"] = None
            __props__.__dict__["updated"] = None
            __props__.__dict__["updated_by"] = None
        super(RepoRuleBranch, __self__).__init__(
            'harness:platform/repoRuleBranch:RepoRuleBranch',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bypasses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchBypassArgs']]]]] = None,
            created: Optional[pulumi.Input[int]] = None,
            created_by: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            patterns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPatternArgs']]]]] = None,
            policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPolicyArgs']]]]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            repo_identifier: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            updated: Optional[pulumi.Input[int]] = None,
            updated_by: Optional[pulumi.Input[int]] = None) -> 'RepoRuleBranch':
        """
        Get an existing RepoRuleBranch resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchBypassArgs']]]] bypasses: List of users who can bypass this rule.
        :param pulumi.Input[int] created: Timestamp when the rule was created.
        :param pulumi.Input[int] created_by: ID of the user who created the rule.
        :param pulumi.Input[str] description: Description of the rule.
        :param pulumi.Input[str] identifier: Identifier of the rule.
        :param pulumi.Input[str] org_id: Unique identifier of the organization.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPatternArgs']]]] patterns: Pattern of branch to which rule will apply.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RepoRuleBranchPolicyArgs']]]] policies: Policies to be applied for this rule.
        :param pulumi.Input[str] project_id: Unique identifier of the project.
        :param pulumi.Input[str] repo_identifier: Repo identifier of the repository.
        :param pulumi.Input[str] state: State of the rule (active, disable, monitor).
        :param pulumi.Input[int] updated: Timestamp when the rule was updated.
        :param pulumi.Input[int] updated_by: ID of the user who updated the rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RepoRuleBranchState.__new__(_RepoRuleBranchState)

        __props__.__dict__["bypasses"] = bypasses
        __props__.__dict__["created"] = created
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["description"] = description
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["patterns"] = patterns
        __props__.__dict__["policies"] = policies
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["repo_identifier"] = repo_identifier
        __props__.__dict__["state"] = state
        __props__.__dict__["updated"] = updated
        __props__.__dict__["updated_by"] = updated_by
        return RepoRuleBranch(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bypasses(self) -> pulumi.Output[Sequence['outputs.RepoRuleBranchBypass']]:
        """
        List of users who can bypass this rule.
        """
        return pulumi.get(self, "bypasses")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[int]:
        """
        Timestamp when the rule was created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[int]:
        """
        ID of the user who created the rule.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        Identifier of the rule.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[Optional[str]]:
        """
        Unique identifier of the organization.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def patterns(self) -> pulumi.Output[Optional[Sequence['outputs.RepoRuleBranchPattern']]]:
        """
        Pattern of branch to which rule will apply.
        """
        return pulumi.get(self, "patterns")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Sequence['outputs.RepoRuleBranchPolicy']]:
        """
        Policies to be applied for this rule.
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[Optional[str]]:
        """
        Unique identifier of the project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="repoIdentifier")
    def repo_identifier(self) -> pulumi.Output[str]:
        """
        Repo identifier of the repository.
        """
        return pulumi.get(self, "repo_identifier")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the rule (active, disable, monitor).
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def updated(self) -> pulumi.Output[int]:
        """
        Timestamp when the rule was updated.
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[int]:
        """
        ID of the user who updated the rule.
        """
        return pulumi.get(self, "updated_by")

