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

__all__ = ['FileStoreFileArgs', 'FileStoreFile']

@pulumi.input_type
class FileStoreFileArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str],
                 parent_identifier: pulumi.Input[str],
                 content: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_content_path: Optional[pulumi.Input[str]] = None,
                 file_usage: Optional[pulumi.Input[str]] = None,
                 mime_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a FileStoreFile resource.
        :param pulumi.Input[str] identifier: Unique identifier of the resource.
        :param pulumi.Input[str] parent_identifier: File parent identifier on Harness File Store
        :param pulumi.Input[str] content: File content stored on Harness File Store
        :param pulumi.Input[str] description: Description of the resource.
        :param pulumi.Input[str] file_content_path: File content path to be upladed on Harness File Store
        :param pulumi.Input[str] file_usage: File usage. Valid options are ManifestFile, Config, Script
        :param pulumi.Input[str] mime_type: File mime type
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[str] org_id: Unique identifier of the organization.
        :param pulumi.Input[str] project_id: Unique identifier of the project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags to associate with the resource.
        """
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "parent_identifier", parent_identifier)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if file_content_path is not None:
            pulumi.set(__self__, "file_content_path", file_content_path)
        if file_usage is not None:
            pulumi.set(__self__, "file_usage", file_usage)
        if mime_type is not None:
            pulumi.set(__self__, "mime_type", mime_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        """
        Unique identifier of the resource.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="parentIdentifier")
    def parent_identifier(self) -> pulumi.Input[str]:
        """
        File parent identifier on Harness File Store
        """
        return pulumi.get(self, "parent_identifier")

    @parent_identifier.setter
    def parent_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_identifier", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        File content stored on Harness File Store
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="fileContentPath")
    def file_content_path(self) -> Optional[pulumi.Input[str]]:
        """
        File content path to be upladed on Harness File Store
        """
        return pulumi.get(self, "file_content_path")

    @file_content_path.setter
    def file_content_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_content_path", value)

    @property
    @pulumi.getter(name="fileUsage")
    def file_usage(self) -> Optional[pulumi.Input[str]]:
        """
        File usage. Valid options are ManifestFile, Config, Script
        """
        return pulumi.get(self, "file_usage")

    @file_usage.setter
    def file_usage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_usage", value)

    @property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[pulumi.Input[str]]:
        """
        File mime type
        """
        return pulumi.get(self, "mime_type")

    @mime_type.setter
    def mime_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mime_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Tags to associate with the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _FileStoreFileState:
    def __init__(__self__, *,
                 content: Optional[pulumi.Input[str]] = None,
                 created_bies: Optional[pulumi.Input[Sequence[pulumi.Input['FileStoreFileCreatedByArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_content_path: Optional[pulumi.Input[str]] = None,
                 file_usage: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 last_modified_at: Optional[pulumi.Input[int]] = None,
                 last_modified_bies: Optional[pulumi.Input[Sequence[pulumi.Input['FileStoreFileLastModifiedByArgs']]]] = None,
                 mime_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 parent_identifier: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering FileStoreFile resources.
        :param pulumi.Input[str] content: File content stored on Harness File Store
        :param pulumi.Input[Sequence[pulumi.Input['FileStoreFileCreatedByArgs']]] created_bies: Created by
        :param pulumi.Input[str] description: Description of the resource.
        :param pulumi.Input[str] file_content_path: File content path to be upladed on Harness File Store
        :param pulumi.Input[str] file_usage: File usage. Valid options are ManifestFile, Config, Script
        :param pulumi.Input[str] identifier: Unique identifier of the resource.
        :param pulumi.Input[int] last_modified_at: Last modified at
        :param pulumi.Input[Sequence[pulumi.Input['FileStoreFileLastModifiedByArgs']]] last_modified_bies: Last modified by
        :param pulumi.Input[str] mime_type: File mime type
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[str] org_id: Unique identifier of the organization.
        :param pulumi.Input[str] parent_identifier: File parent identifier on Harness File Store
        :param pulumi.Input[str] path: Harness File Store file path
        :param pulumi.Input[str] project_id: Unique identifier of the project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags to associate with the resource.
        """
        if content is not None:
            pulumi.set(__self__, "content", content)
        if created_bies is not None:
            pulumi.set(__self__, "created_bies", created_bies)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if file_content_path is not None:
            pulumi.set(__self__, "file_content_path", file_content_path)
        if file_usage is not None:
            pulumi.set(__self__, "file_usage", file_usage)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_bies is not None:
            pulumi.set(__self__, "last_modified_bies", last_modified_bies)
        if mime_type is not None:
            pulumi.set(__self__, "mime_type", mime_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if parent_identifier is not None:
            pulumi.set(__self__, "parent_identifier", parent_identifier)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        File content stored on Harness File Store
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="createdBies")
    def created_bies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FileStoreFileCreatedByArgs']]]]:
        """
        Created by
        """
        return pulumi.get(self, "created_bies")

    @created_bies.setter
    def created_bies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FileStoreFileCreatedByArgs']]]]):
        pulumi.set(self, "created_bies", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="fileContentPath")
    def file_content_path(self) -> Optional[pulumi.Input[str]]:
        """
        File content path to be upladed on Harness File Store
        """
        return pulumi.get(self, "file_content_path")

    @file_content_path.setter
    def file_content_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_content_path", value)

    @property
    @pulumi.getter(name="fileUsage")
    def file_usage(self) -> Optional[pulumi.Input[str]]:
        """
        File usage. Valid options are ManifestFile, Config, Script
        """
        return pulumi.get(self, "file_usage")

    @file_usage.setter
    def file_usage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_usage", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the resource.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[int]]:
        """
        Last modified at
        """
        return pulumi.get(self, "last_modified_at")

    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "last_modified_at", value)

    @property
    @pulumi.getter(name="lastModifiedBies")
    def last_modified_bies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FileStoreFileLastModifiedByArgs']]]]:
        """
        Last modified by
        """
        return pulumi.get(self, "last_modified_bies")

    @last_modified_bies.setter
    def last_modified_bies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FileStoreFileLastModifiedByArgs']]]]):
        pulumi.set(self, "last_modified_bies", value)

    @property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[pulumi.Input[str]]:
        """
        File mime type
        """
        return pulumi.get(self, "mime_type")

    @mime_type.setter
    def mime_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mime_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="parentIdentifier")
    def parent_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        File parent identifier on Harness File Store
        """
        return pulumi.get(self, "parent_identifier")

    @parent_identifier.setter
    def parent_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_identifier", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Harness File Store file path
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Tags to associate with the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class FileStoreFile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_content_path: Optional[pulumi.Input[str]] = None,
                 file_usage: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 mime_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 parent_identifier: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource for creating files in Harness.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        # Create file
        example = harness.platform.FileStoreFile("example",
            org_id="org_id",
            project_id="project_id",
            identifier="identifier",
            name="name",
            description="description",
            tags=[
                "foo:bar",
                "baz:qux",
            ],
            parent_identifier="parent_identifier",
            file_content_path="file_content_path",
            mime_type="mime_type",
            file_usage="MANIFEST_FILE|CONFIG|SCRIPT")
        ```

        ## Import

        Import account level file

        ```sh
        $ pulumi import harness:platform/fileStoreFile:FileStoreFile example <identifier>
        ```

        Import org level file

        ```sh
        $ pulumi import harness:platform/fileStoreFile:FileStoreFile example <org_id><identifier>
        ```

        Import org level file

        ```sh
        $ pulumi import harness:platform/fileStoreFile:FileStoreFile example <org_id><project_id><identifier>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: File content stored on Harness File Store
        :param pulumi.Input[str] description: Description of the resource.
        :param pulumi.Input[str] file_content_path: File content path to be upladed on Harness File Store
        :param pulumi.Input[str] file_usage: File usage. Valid options are ManifestFile, Config, Script
        :param pulumi.Input[str] identifier: Unique identifier of the resource.
        :param pulumi.Input[str] mime_type: File mime type
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[str] org_id: Unique identifier of the organization.
        :param pulumi.Input[str] parent_identifier: File parent identifier on Harness File Store
        :param pulumi.Input[str] project_id: Unique identifier of the project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags to associate with the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FileStoreFileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for creating files in Harness.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_harness as harness

        # Create file
        example = harness.platform.FileStoreFile("example",
            org_id="org_id",
            project_id="project_id",
            identifier="identifier",
            name="name",
            description="description",
            tags=[
                "foo:bar",
                "baz:qux",
            ],
            parent_identifier="parent_identifier",
            file_content_path="file_content_path",
            mime_type="mime_type",
            file_usage="MANIFEST_FILE|CONFIG|SCRIPT")
        ```

        ## Import

        Import account level file

        ```sh
        $ pulumi import harness:platform/fileStoreFile:FileStoreFile example <identifier>
        ```

        Import org level file

        ```sh
        $ pulumi import harness:platform/fileStoreFile:FileStoreFile example <org_id><identifier>
        ```

        Import org level file

        ```sh
        $ pulumi import harness:platform/fileStoreFile:FileStoreFile example <org_id><project_id><identifier>
        ```

        :param str resource_name: The name of the resource.
        :param FileStoreFileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FileStoreFileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_content_path: Optional[pulumi.Input[str]] = None,
                 file_usage: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 mime_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 parent_identifier: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FileStoreFileArgs.__new__(FileStoreFileArgs)

            __props__.__dict__["content"] = content
            __props__.__dict__["description"] = description
            __props__.__dict__["file_content_path"] = file_content_path
            __props__.__dict__["file_usage"] = file_usage
            if identifier is None and not opts.urn:
                raise TypeError("Missing required property 'identifier'")
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["mime_type"] = mime_type
            __props__.__dict__["name"] = name
            __props__.__dict__["org_id"] = org_id
            if parent_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'parent_identifier'")
            __props__.__dict__["parent_identifier"] = parent_identifier
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_bies"] = None
            __props__.__dict__["last_modified_at"] = None
            __props__.__dict__["last_modified_bies"] = None
            __props__.__dict__["path"] = None
        super(FileStoreFile, __self__).__init__(
            'harness:platform/fileStoreFile:FileStoreFile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            content: Optional[pulumi.Input[str]] = None,
            created_bies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileStoreFileCreatedByArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            file_content_path: Optional[pulumi.Input[str]] = None,
            file_usage: Optional[pulumi.Input[str]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            last_modified_at: Optional[pulumi.Input[int]] = None,
            last_modified_bies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileStoreFileLastModifiedByArgs']]]]] = None,
            mime_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            parent_identifier: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'FileStoreFile':
        """
        Get an existing FileStoreFile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: File content stored on Harness File Store
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileStoreFileCreatedByArgs']]]] created_bies: Created by
        :param pulumi.Input[str] description: Description of the resource.
        :param pulumi.Input[str] file_content_path: File content path to be upladed on Harness File Store
        :param pulumi.Input[str] file_usage: File usage. Valid options are ManifestFile, Config, Script
        :param pulumi.Input[str] identifier: Unique identifier of the resource.
        :param pulumi.Input[int] last_modified_at: Last modified at
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FileStoreFileLastModifiedByArgs']]]] last_modified_bies: Last modified by
        :param pulumi.Input[str] mime_type: File mime type
        :param pulumi.Input[str] name: Name of the resource.
        :param pulumi.Input[str] org_id: Unique identifier of the organization.
        :param pulumi.Input[str] parent_identifier: File parent identifier on Harness File Store
        :param pulumi.Input[str] path: Harness File Store file path
        :param pulumi.Input[str] project_id: Unique identifier of the project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags to associate with the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FileStoreFileState.__new__(_FileStoreFileState)

        __props__.__dict__["content"] = content
        __props__.__dict__["created_bies"] = created_bies
        __props__.__dict__["description"] = description
        __props__.__dict__["file_content_path"] = file_content_path
        __props__.__dict__["file_usage"] = file_usage
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["last_modified_at"] = last_modified_at
        __props__.__dict__["last_modified_bies"] = last_modified_bies
        __props__.__dict__["mime_type"] = mime_type
        __props__.__dict__["name"] = name
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["parent_identifier"] = parent_identifier
        __props__.__dict__["path"] = path
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["tags"] = tags
        return FileStoreFile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional[str]]:
        """
        File content stored on Harness File Store
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createdBies")
    def created_bies(self) -> pulumi.Output[Sequence['outputs.FileStoreFileCreatedBy']]:
        """
        Created by
        """
        return pulumi.get(self, "created_bies")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="fileContentPath")
    def file_content_path(self) -> pulumi.Output[Optional[str]]:
        """
        File content path to be upladed on Harness File Store
        """
        return pulumi.get(self, "file_content_path")

    @property
    @pulumi.getter(name="fileUsage")
    def file_usage(self) -> pulumi.Output[str]:
        """
        File usage. Valid options are ManifestFile, Config, Script
        """
        return pulumi.get(self, "file_usage")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        Unique identifier of the resource.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[int]:
        """
        Last modified at
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBies")
    def last_modified_bies(self) -> pulumi.Output[Sequence['outputs.FileStoreFileLastModifiedBy']]:
        """
        Last modified by
        """
        return pulumi.get(self, "last_modified_bies")

    @property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> pulumi.Output[str]:
        """
        File mime type
        """
        return pulumi.get(self, "mime_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[Optional[str]]:
        """
        Unique identifier of the organization.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="parentIdentifier")
    def parent_identifier(self) -> pulumi.Output[str]:
        """
        File parent identifier on Harness File Store
        """
        return pulumi.get(self, "parent_identifier")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        Harness File Store file path
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[Optional[str]]:
        """
        Unique identifier of the project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Tags to associate with the resource.
        """
        return pulumi.get(self, "tags")

