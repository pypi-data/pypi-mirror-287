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

__all__ = ['UserGroupArgs', 'UserGroup']

@pulumi.input_type
class UserGroupArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 ldap_settings: Optional[pulumi.Input['UserGroupLdapSettingsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input['UserGroupNotificationSettingsArgs']] = None,
                 permissions: Optional[pulumi.Input['UserGroupPermissionsArgs']] = None,
                 saml_settings: Optional[pulumi.Input['UserGroupSamlSettingsArgs']] = None):
        """
        The set of arguments for constructing a UserGroup resource.
        :param pulumi.Input[str] description: The description of the user group.
        :param pulumi.Input['UserGroupLdapSettingsArgs'] ldap_settings: The LDAP settings for the user group.
        :param pulumi.Input[str] name: The name of the user group.
        :param pulumi.Input['UserGroupNotificationSettingsArgs'] notification_settings: The notification settings of the user group.
        :param pulumi.Input['UserGroupPermissionsArgs'] permissions: The permissions of the user group.
        :param pulumi.Input['UserGroupSamlSettingsArgs'] saml_settings: The SAML settings for the user group.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ldap_settings is not None:
            pulumi.set(__self__, "ldap_settings", ldap_settings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_settings is not None:
            pulumi.set(__self__, "notification_settings", notification_settings)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if saml_settings is not None:
            pulumi.set(__self__, "saml_settings", saml_settings)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the user group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ldapSettings")
    def ldap_settings(self) -> Optional[pulumi.Input['UserGroupLdapSettingsArgs']]:
        """
        The LDAP settings for the user group.
        """
        return pulumi.get(self, "ldap_settings")

    @ldap_settings.setter
    def ldap_settings(self, value: Optional[pulumi.Input['UserGroupLdapSettingsArgs']]):
        pulumi.set(self, "ldap_settings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> Optional[pulumi.Input['UserGroupNotificationSettingsArgs']]:
        """
        The notification settings of the user group.
        """
        return pulumi.get(self, "notification_settings")

    @notification_settings.setter
    def notification_settings(self, value: Optional[pulumi.Input['UserGroupNotificationSettingsArgs']]):
        pulumi.set(self, "notification_settings", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input['UserGroupPermissionsArgs']]:
        """
        The permissions of the user group.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input['UserGroupPermissionsArgs']]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="samlSettings")
    def saml_settings(self) -> Optional[pulumi.Input['UserGroupSamlSettingsArgs']]:
        """
        The SAML settings for the user group.
        """
        return pulumi.get(self, "saml_settings")

    @saml_settings.setter
    def saml_settings(self, value: Optional[pulumi.Input['UserGroupSamlSettingsArgs']]):
        pulumi.set(self, "saml_settings", value)


@pulumi.input_type
class _UserGroupState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 imported_by_scim: Optional[pulumi.Input[bool]] = None,
                 is_sso_linked: Optional[pulumi.Input[bool]] = None,
                 ldap_settings: Optional[pulumi.Input['UserGroupLdapSettingsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input['UserGroupNotificationSettingsArgs']] = None,
                 permissions: Optional[pulumi.Input['UserGroupPermissionsArgs']] = None,
                 saml_settings: Optional[pulumi.Input['UserGroupSamlSettingsArgs']] = None):
        """
        Input properties used for looking up and filtering UserGroup resources.
        :param pulumi.Input[str] description: The description of the user group.
        :param pulumi.Input[bool] imported_by_scim: Indicates whether the user group was imported by SCIM.
        :param pulumi.Input[bool] is_sso_linked: Indicates whether the user group is linked to an SSO provider.
        :param pulumi.Input['UserGroupLdapSettingsArgs'] ldap_settings: The LDAP settings for the user group.
        :param pulumi.Input[str] name: The name of the user group.
        :param pulumi.Input['UserGroupNotificationSettingsArgs'] notification_settings: The notification settings of the user group.
        :param pulumi.Input['UserGroupPermissionsArgs'] permissions: The permissions of the user group.
        :param pulumi.Input['UserGroupSamlSettingsArgs'] saml_settings: The SAML settings for the user group.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if imported_by_scim is not None:
            pulumi.set(__self__, "imported_by_scim", imported_by_scim)
        if is_sso_linked is not None:
            pulumi.set(__self__, "is_sso_linked", is_sso_linked)
        if ldap_settings is not None:
            pulumi.set(__self__, "ldap_settings", ldap_settings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_settings is not None:
            pulumi.set(__self__, "notification_settings", notification_settings)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if saml_settings is not None:
            pulumi.set(__self__, "saml_settings", saml_settings)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the user group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="importedByScim")
    def imported_by_scim(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the user group was imported by SCIM.
        """
        return pulumi.get(self, "imported_by_scim")

    @imported_by_scim.setter
    def imported_by_scim(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "imported_by_scim", value)

    @property
    @pulumi.getter(name="isSsoLinked")
    def is_sso_linked(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the user group is linked to an SSO provider.
        """
        return pulumi.get(self, "is_sso_linked")

    @is_sso_linked.setter
    def is_sso_linked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_sso_linked", value)

    @property
    @pulumi.getter(name="ldapSettings")
    def ldap_settings(self) -> Optional[pulumi.Input['UserGroupLdapSettingsArgs']]:
        """
        The LDAP settings for the user group.
        """
        return pulumi.get(self, "ldap_settings")

    @ldap_settings.setter
    def ldap_settings(self, value: Optional[pulumi.Input['UserGroupLdapSettingsArgs']]):
        pulumi.set(self, "ldap_settings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> Optional[pulumi.Input['UserGroupNotificationSettingsArgs']]:
        """
        The notification settings of the user group.
        """
        return pulumi.get(self, "notification_settings")

    @notification_settings.setter
    def notification_settings(self, value: Optional[pulumi.Input['UserGroupNotificationSettingsArgs']]):
        pulumi.set(self, "notification_settings", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input['UserGroupPermissionsArgs']]:
        """
        The permissions of the user group.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input['UserGroupPermissionsArgs']]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="samlSettings")
    def saml_settings(self) -> Optional[pulumi.Input['UserGroupSamlSettingsArgs']]:
        """
        The SAML settings for the user group.
        """
        return pulumi.get(self, "saml_settings")

    @saml_settings.setter
    def saml_settings(self, value: Optional[pulumi.Input['UserGroupSamlSettingsArgs']]):
        pulumi.set(self, "saml_settings", value)


class UserGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ldap_settings: Optional[pulumi.Input[pulumi.InputType['UserGroupLdapSettingsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input[pulumi.InputType['UserGroupNotificationSettingsArgs']]] = None,
                 permissions: Optional[pulumi.Input[pulumi.InputType['UserGroupPermissionsArgs']]] = None,
                 saml_settings: Optional[pulumi.Input[pulumi.InputType['UserGroupSamlSettingsArgs']]] = None,
                 __props__=None):
        """
        Resource for creating a Harness user group

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        example = harness.UserGroup("example",
            name="example-group",
            description="This group demonstrates account level and resource level permissions.",
            permissions=harness.UserGroupPermissionsArgs(
                account_permissions=[
                    "ADMINISTER_OTHER_ACCOUNT_FUNCTIONS",
                    "MANAGE_API_KEYS",
                ],
                app_permissions=harness.UserGroupPermissionsAppPermissionsArgs(
                    alls=[harness.UserGroupPermissionsAppPermissionsAllArgs(
                        actions=[
                            "CREATE",
                            "READ",
                            "UPDATE",
                            "DELETE",
                        ],
                    )],
                    deployments=[
                        harness.UserGroupPermissionsAppPermissionsDeploymentArgs(
                            actions=[
                                "READ",
                                "ROLLBACK_WORKFLOW",
                                "EXECUTE_PIPELINE",
                                "EXECUTE_WORKFLOW",
                            ],
                            filters=["NON_PRODUCTION_ENVIRONMENTS"],
                        ),
                        harness.UserGroupPermissionsAppPermissionsDeploymentArgs(
                            actions=["READ"],
                            filters=["PRODUCTION_ENVIRONMENTS"],
                        ),
                    ],
                    environments=[
                        harness.UserGroupPermissionsAppPermissionsEnvironmentArgs(
                            actions=[
                                "CREATE",
                                "READ",
                                "UPDATE",
                                "DELETE",
                            ],
                            filters=["NON_PRODUCTION_ENVIRONMENTS"],
                        ),
                        harness.UserGroupPermissionsAppPermissionsEnvironmentArgs(
                            actions=["READ"],
                            filters=["PRODUCTION_ENVIRONMENTS"],
                        ),
                    ],
                    pipelines=[
                        harness.UserGroupPermissionsAppPermissionsPipelineArgs(
                            actions=[
                                "CREATE",
                                "READ",
                                "UPDATE",
                                "DELETE",
                            ],
                            filters=["NON_PRODUCTION_PIPELINES"],
                        ),
                        harness.UserGroupPermissionsAppPermissionsPipelineArgs(
                            actions=["READ"],
                            filters=["PRODUCTION_PIPELINES"],
                        ),
                    ],
                    provisioners=[
                        harness.UserGroupPermissionsAppPermissionsProvisionerArgs(
                            actions=[
                                "UPDATE",
                                "DELETE",
                            ],
                        ),
                        harness.UserGroupPermissionsAppPermissionsProvisionerArgs(
                            actions=[
                                "CREATE",
                                "READ",
                            ],
                        ),
                    ],
                    services=[
                        harness.UserGroupPermissionsAppPermissionsServiceArgs(
                            actions=[
                                "UPDATE",
                                "DELETE",
                            ],
                        ),
                        harness.UserGroupPermissionsAppPermissionsServiceArgs(
                            actions=[
                                "UPDATE",
                                "DELETE",
                            ],
                        ),
                    ],
                    templates=[harness.UserGroupPermissionsAppPermissionsTemplateArgs(
                        actions=[
                            "CREATE",
                            "READ",
                            "UPDATE",
                            "DELETE",
                        ],
                    )],
                    workflows=[
                        harness.UserGroupPermissionsAppPermissionsWorkflowArgs(
                            actions=[
                                "UPDATE",
                                "DELETE",
                            ],
                            filters=["NON_PRODUCTION_WORKFLOWS"],
                        ),
                        harness.UserGroupPermissionsAppPermissionsWorkflowArgs(
                            actions=[
                                "CREATE",
                                "READ",
                            ],
                            filters=[
                                "PRODUCTION_WORKFLOWS",
                                "WORKFLOW_TEMPLATES",
                            ],
                        ),
                    ],
                ),
            ))
        ```

        ## Import

        Import using the id of the user group

        ```sh
        $ pulumi import harness:index/userGroup:UserGroup example <USER_GROUP_ID>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the user group.
        :param pulumi.Input[pulumi.InputType['UserGroupLdapSettingsArgs']] ldap_settings: The LDAP settings for the user group.
        :param pulumi.Input[str] name: The name of the user group.
        :param pulumi.Input[pulumi.InputType['UserGroupNotificationSettingsArgs']] notification_settings: The notification settings of the user group.
        :param pulumi.Input[pulumi.InputType['UserGroupPermissionsArgs']] permissions: The permissions of the user group.
        :param pulumi.Input[pulumi.InputType['UserGroupSamlSettingsArgs']] saml_settings: The SAML settings for the user group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[UserGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for creating a Harness user group

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        example = harness.UserGroup("example",
            name="example-group",
            description="This group demonstrates account level and resource level permissions.",
            permissions=harness.UserGroupPermissionsArgs(
                account_permissions=[
                    "ADMINISTER_OTHER_ACCOUNT_FUNCTIONS",
                    "MANAGE_API_KEYS",
                ],
                app_permissions=harness.UserGroupPermissionsAppPermissionsArgs(
                    alls=[harness.UserGroupPermissionsAppPermissionsAllArgs(
                        actions=[
                            "CREATE",
                            "READ",
                            "UPDATE",
                            "DELETE",
                        ],
                    )],
                    deployments=[
                        harness.UserGroupPermissionsAppPermissionsDeploymentArgs(
                            actions=[
                                "READ",
                                "ROLLBACK_WORKFLOW",
                                "EXECUTE_PIPELINE",
                                "EXECUTE_WORKFLOW",
                            ],
                            filters=["NON_PRODUCTION_ENVIRONMENTS"],
                        ),
                        harness.UserGroupPermissionsAppPermissionsDeploymentArgs(
                            actions=["READ"],
                            filters=["PRODUCTION_ENVIRONMENTS"],
                        ),
                    ],
                    environments=[
                        harness.UserGroupPermissionsAppPermissionsEnvironmentArgs(
                            actions=[
                                "CREATE",
                                "READ",
                                "UPDATE",
                                "DELETE",
                            ],
                            filters=["NON_PRODUCTION_ENVIRONMENTS"],
                        ),
                        harness.UserGroupPermissionsAppPermissionsEnvironmentArgs(
                            actions=["READ"],
                            filters=["PRODUCTION_ENVIRONMENTS"],
                        ),
                    ],
                    pipelines=[
                        harness.UserGroupPermissionsAppPermissionsPipelineArgs(
                            actions=[
                                "CREATE",
                                "READ",
                                "UPDATE",
                                "DELETE",
                            ],
                            filters=["NON_PRODUCTION_PIPELINES"],
                        ),
                        harness.UserGroupPermissionsAppPermissionsPipelineArgs(
                            actions=["READ"],
                            filters=["PRODUCTION_PIPELINES"],
                        ),
                    ],
                    provisioners=[
                        harness.UserGroupPermissionsAppPermissionsProvisionerArgs(
                            actions=[
                                "UPDATE",
                                "DELETE",
                            ],
                        ),
                        harness.UserGroupPermissionsAppPermissionsProvisionerArgs(
                            actions=[
                                "CREATE",
                                "READ",
                            ],
                        ),
                    ],
                    services=[
                        harness.UserGroupPermissionsAppPermissionsServiceArgs(
                            actions=[
                                "UPDATE",
                                "DELETE",
                            ],
                        ),
                        harness.UserGroupPermissionsAppPermissionsServiceArgs(
                            actions=[
                                "UPDATE",
                                "DELETE",
                            ],
                        ),
                    ],
                    templates=[harness.UserGroupPermissionsAppPermissionsTemplateArgs(
                        actions=[
                            "CREATE",
                            "READ",
                            "UPDATE",
                            "DELETE",
                        ],
                    )],
                    workflows=[
                        harness.UserGroupPermissionsAppPermissionsWorkflowArgs(
                            actions=[
                                "UPDATE",
                                "DELETE",
                            ],
                            filters=["NON_PRODUCTION_WORKFLOWS"],
                        ),
                        harness.UserGroupPermissionsAppPermissionsWorkflowArgs(
                            actions=[
                                "CREATE",
                                "READ",
                            ],
                            filters=[
                                "PRODUCTION_WORKFLOWS",
                                "WORKFLOW_TEMPLATES",
                            ],
                        ),
                    ],
                ),
            ))
        ```

        ## Import

        Import using the id of the user group

        ```sh
        $ pulumi import harness:index/userGroup:UserGroup example <USER_GROUP_ID>
        ```

        :param str resource_name: The name of the resource.
        :param UserGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ldap_settings: Optional[pulumi.Input[pulumi.InputType['UserGroupLdapSettingsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_settings: Optional[pulumi.Input[pulumi.InputType['UserGroupNotificationSettingsArgs']]] = None,
                 permissions: Optional[pulumi.Input[pulumi.InputType['UserGroupPermissionsArgs']]] = None,
                 saml_settings: Optional[pulumi.Input[pulumi.InputType['UserGroupSamlSettingsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserGroupArgs.__new__(UserGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["ldap_settings"] = ldap_settings
            __props__.__dict__["name"] = name
            __props__.__dict__["notification_settings"] = notification_settings
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["saml_settings"] = saml_settings
            __props__.__dict__["imported_by_scim"] = None
            __props__.__dict__["is_sso_linked"] = None
        super(UserGroup, __self__).__init__(
            'harness:index/userGroup:UserGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            imported_by_scim: Optional[pulumi.Input[bool]] = None,
            is_sso_linked: Optional[pulumi.Input[bool]] = None,
            ldap_settings: Optional[pulumi.Input[pulumi.InputType['UserGroupLdapSettingsArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            notification_settings: Optional[pulumi.Input[pulumi.InputType['UserGroupNotificationSettingsArgs']]] = None,
            permissions: Optional[pulumi.Input[pulumi.InputType['UserGroupPermissionsArgs']]] = None,
            saml_settings: Optional[pulumi.Input[pulumi.InputType['UserGroupSamlSettingsArgs']]] = None) -> 'UserGroup':
        """
        Get an existing UserGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the user group.
        :param pulumi.Input[bool] imported_by_scim: Indicates whether the user group was imported by SCIM.
        :param pulumi.Input[bool] is_sso_linked: Indicates whether the user group is linked to an SSO provider.
        :param pulumi.Input[pulumi.InputType['UserGroupLdapSettingsArgs']] ldap_settings: The LDAP settings for the user group.
        :param pulumi.Input[str] name: The name of the user group.
        :param pulumi.Input[pulumi.InputType['UserGroupNotificationSettingsArgs']] notification_settings: The notification settings of the user group.
        :param pulumi.Input[pulumi.InputType['UserGroupPermissionsArgs']] permissions: The permissions of the user group.
        :param pulumi.Input[pulumi.InputType['UserGroupSamlSettingsArgs']] saml_settings: The SAML settings for the user group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserGroupState.__new__(_UserGroupState)

        __props__.__dict__["description"] = description
        __props__.__dict__["imported_by_scim"] = imported_by_scim
        __props__.__dict__["is_sso_linked"] = is_sso_linked
        __props__.__dict__["ldap_settings"] = ldap_settings
        __props__.__dict__["name"] = name
        __props__.__dict__["notification_settings"] = notification_settings
        __props__.__dict__["permissions"] = permissions
        __props__.__dict__["saml_settings"] = saml_settings
        return UserGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the user group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="importedByScim")
    def imported_by_scim(self) -> pulumi.Output[bool]:
        """
        Indicates whether the user group was imported by SCIM.
        """
        return pulumi.get(self, "imported_by_scim")

    @property
    @pulumi.getter(name="isSsoLinked")
    def is_sso_linked(self) -> pulumi.Output[bool]:
        """
        Indicates whether the user group is linked to an SSO provider.
        """
        return pulumi.get(self, "is_sso_linked")

    @property
    @pulumi.getter(name="ldapSettings")
    def ldap_settings(self) -> pulumi.Output[Optional['outputs.UserGroupLdapSettings']]:
        """
        The LDAP settings for the user group.
        """
        return pulumi.get(self, "ldap_settings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the user group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> pulumi.Output[Optional['outputs.UserGroupNotificationSettings']]:
        """
        The notification settings of the user group.
        """
        return pulumi.get(self, "notification_settings")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional['outputs.UserGroupPermissions']]:
        """
        The permissions of the user group.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="samlSettings")
    def saml_settings(self) -> pulumi.Output[Optional['outputs.UserGroupSamlSettings']]:
        """
        The SAML settings for the user group.
        """
        return pulumi.get(self, "saml_settings")

