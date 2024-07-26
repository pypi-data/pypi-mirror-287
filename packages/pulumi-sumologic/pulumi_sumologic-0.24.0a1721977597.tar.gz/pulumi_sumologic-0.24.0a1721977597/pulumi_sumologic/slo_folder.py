# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SloFolderArgs', 'SloFolder']

@pulumi.input_type
class SloFolderArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 content_type: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 is_locked: Optional[pulumi.Input[bool]] = None,
                 is_mutable: Optional[pulumi.Input[bool]] = None,
                 is_system: Optional[pulumi.Input[bool]] = None,
                 modified_at: Optional[pulumi.Input[str]] = None,
                 modified_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 post_request_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a SloFolder resource.
        :param pulumi.Input[str] description: The description of the SLO folder.
        :param pulumi.Input[str] name: The name of the SLO folder. The name must be alphanumeric.
        :param pulumi.Input[str] parent_id: The identifier of the SLO Folder that contains this SLO Folder. Defaults to the root folder.
               
               Additional data provided in state:
        """
        pulumi.set(__self__, "description", description)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if is_locked is not None:
            pulumi.set(__self__, "is_locked", is_locked)
        if is_mutable is not None:
            pulumi.set(__self__, "is_mutable", is_mutable)
        if is_system is not None:
            pulumi.set(__self__, "is_system", is_system)
        if modified_at is not None:
            pulumi.set(__self__, "modified_at", modified_at)
        if modified_by is not None:
            pulumi.set(__self__, "modified_by", modified_by)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if post_request_map is not None:
            pulumi.set(__self__, "post_request_map", post_request_map)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the SLO folder.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="isLocked")
    def is_locked(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_locked")

    @is_locked.setter
    def is_locked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_locked", value)

    @property
    @pulumi.getter(name="isMutable")
    def is_mutable(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_mutable")

    @is_mutable.setter
    def is_mutable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_mutable", value)

    @property
    @pulumi.getter(name="isSystem")
    def is_system(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_system")

    @is_system.setter
    def is_system(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_system", value)

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "modified_at")

    @modified_at.setter
    def modified_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_at", value)

    @property
    @pulumi.getter(name="modifiedBy")
    def modified_by(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "modified_by")

    @modified_by.setter
    def modified_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_by", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SLO folder. The name must be alphanumeric.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the SLO Folder that contains this SLO Folder. Defaults to the root folder.

        Additional data provided in state:
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="postRequestMap")
    def post_request_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "post_request_map")

    @post_request_map.setter
    def post_request_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "post_request_map", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class _SloFolderState:
    def __init__(__self__, *,
                 content_type: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_locked: Optional[pulumi.Input[bool]] = None,
                 is_mutable: Optional[pulumi.Input[bool]] = None,
                 is_system: Optional[pulumi.Input[bool]] = None,
                 modified_at: Optional[pulumi.Input[str]] = None,
                 modified_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 post_request_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering SloFolder resources.
        :param pulumi.Input[str] description: The description of the SLO folder.
        :param pulumi.Input[str] name: The name of the SLO folder. The name must be alphanumeric.
        :param pulumi.Input[str] parent_id: The identifier of the SLO Folder that contains this SLO Folder. Defaults to the root folder.
               
               Additional data provided in state:
        """
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if is_locked is not None:
            pulumi.set(__self__, "is_locked", is_locked)
        if is_mutable is not None:
            pulumi.set(__self__, "is_mutable", is_mutable)
        if is_system is not None:
            pulumi.set(__self__, "is_system", is_system)
        if modified_at is not None:
            pulumi.set(__self__, "modified_at", modified_at)
        if modified_by is not None:
            pulumi.set(__self__, "modified_by", modified_by)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if post_request_map is not None:
            pulumi.set(__self__, "post_request_map", post_request_map)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the SLO folder.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="isLocked")
    def is_locked(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_locked")

    @is_locked.setter
    def is_locked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_locked", value)

    @property
    @pulumi.getter(name="isMutable")
    def is_mutable(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_mutable")

    @is_mutable.setter
    def is_mutable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_mutable", value)

    @property
    @pulumi.getter(name="isSystem")
    def is_system(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_system")

    @is_system.setter
    def is_system(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_system", value)

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "modified_at")

    @modified_at.setter
    def modified_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_at", value)

    @property
    @pulumi.getter(name="modifiedBy")
    def modified_by(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "modified_by")

    @modified_by.setter
    def modified_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_by", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SLO folder. The name must be alphanumeric.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the SLO Folder that contains this SLO Folder. Defaults to the root folder.

        Additional data provided in state:
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="postRequestMap")
    def post_request_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "post_request_map")

    @post_request_map.setter
    def post_request_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "post_request_map", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class SloFolder(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_locked: Optional[pulumi.Input[bool]] = None,
                 is_mutable: Optional[pulumi.Input[bool]] = None,
                 is_system: Optional[pulumi.Input[bool]] = None,
                 modified_at: Optional[pulumi.Input[str]] = None,
                 modified_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 post_request_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides the ability to create, read, delete, and update folders for SLO's.

        ## Example SLO Folder

        NOTE: SLO folders are considered a different resource from Library content and monitor folders.

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        tf_slo_folder = sumologic.SloFolder("tf_slo_folder",
            name="Terraform Managed SLO's",
            description="A folder for SLO's managed by terraform.")
        ```

        ## Example Nested SLO Folders

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        tf_payments_team_root_folder = sumologic.SloFolder("tf_payments_team_root_folder",
            name="Security Team SLOs",
            description="SLO's payments services.")
        tf_payments_team_prod_folder = sumologic.SloFolder("tf_payments_team_prod_folder",
            name="Production SLOs",
            description="SLOs for the Payments service on Production Environment.",
            parent_id=tf_payments_team_root_folder.id)
        tf_payments_team_stag_folder = sumologic.SloFolder("tf_payments_team_stag_folder",
            name="Staging SLOs",
            description="SLOs for the payments service on Staging Environment.",
            parent_id=tf_payments_team_root_folder.id)
        ```

        ## Import

        SLO folders can be imported using the SLO folder identifier, such as:

         shell

        ```sh
        $ pulumi import sumologic:index/sloFolder:SloFolder tf_slo_folder_1 0000000000ABC123
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the SLO folder.
        :param pulumi.Input[str] name: The name of the SLO folder. The name must be alphanumeric.
        :param pulumi.Input[str] parent_id: The identifier of the SLO Folder that contains this SLO Folder. Defaults to the root folder.
               
               Additional data provided in state:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SloFolderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides the ability to create, read, delete, and update folders for SLO's.

        ## Example SLO Folder

        NOTE: SLO folders are considered a different resource from Library content and monitor folders.

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        tf_slo_folder = sumologic.SloFolder("tf_slo_folder",
            name="Terraform Managed SLO's",
            description="A folder for SLO's managed by terraform.")
        ```

        ## Example Nested SLO Folders

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        tf_payments_team_root_folder = sumologic.SloFolder("tf_payments_team_root_folder",
            name="Security Team SLOs",
            description="SLO's payments services.")
        tf_payments_team_prod_folder = sumologic.SloFolder("tf_payments_team_prod_folder",
            name="Production SLOs",
            description="SLOs for the Payments service on Production Environment.",
            parent_id=tf_payments_team_root_folder.id)
        tf_payments_team_stag_folder = sumologic.SloFolder("tf_payments_team_stag_folder",
            name="Staging SLOs",
            description="SLOs for the payments service on Staging Environment.",
            parent_id=tf_payments_team_root_folder.id)
        ```

        ## Import

        SLO folders can be imported using the SLO folder identifier, such as:

         shell

        ```sh
        $ pulumi import sumologic:index/sloFolder:SloFolder tf_slo_folder_1 0000000000ABC123
        ```

        :param str resource_name: The name of the resource.
        :param SloFolderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SloFolderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_locked: Optional[pulumi.Input[bool]] = None,
                 is_mutable: Optional[pulumi.Input[bool]] = None,
                 is_system: Optional[pulumi.Input[bool]] = None,
                 modified_at: Optional[pulumi.Input[str]] = None,
                 modified_by: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 post_request_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SloFolderArgs.__new__(SloFolderArgs)

            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["created_by"] = created_by
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["is_locked"] = is_locked
            __props__.__dict__["is_mutable"] = is_mutable
            __props__.__dict__["is_system"] = is_system
            __props__.__dict__["modified_at"] = modified_at
            __props__.__dict__["modified_by"] = modified_by
            __props__.__dict__["name"] = name
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["post_request_map"] = post_request_map
            __props__.__dict__["type"] = type
            __props__.__dict__["version"] = version
        super(SloFolder, __self__).__init__(
            'sumologic:index/sloFolder:SloFolder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            content_type: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            created_by: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            is_locked: Optional[pulumi.Input[bool]] = None,
            is_mutable: Optional[pulumi.Input[bool]] = None,
            is_system: Optional[pulumi.Input[bool]] = None,
            modified_at: Optional[pulumi.Input[str]] = None,
            modified_by: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            post_request_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'SloFolder':
        """
        Get an existing SloFolder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the SLO folder.
        :param pulumi.Input[str] name: The name of the SLO folder. The name must be alphanumeric.
        :param pulumi.Input[str] parent_id: The identifier of the SLO Folder that contains this SLO Folder. Defaults to the root folder.
               
               Additional data provided in state:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SloFolderState.__new__(_SloFolderState)

        __props__.__dict__["content_type"] = content_type
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["created_by"] = created_by
        __props__.__dict__["description"] = description
        __props__.__dict__["is_locked"] = is_locked
        __props__.__dict__["is_mutable"] = is_mutable
        __props__.__dict__["is_system"] = is_system
        __props__.__dict__["modified_at"] = modified_at
        __props__.__dict__["modified_by"] = modified_by
        __props__.__dict__["name"] = name
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["post_request_map"] = post_request_map
        __props__.__dict__["type"] = type
        __props__.__dict__["version"] = version
        return SloFolder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the SLO folder.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="isLocked")
    def is_locked(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "is_locked")

    @property
    @pulumi.getter(name="isMutable")
    def is_mutable(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_mutable")

    @property
    @pulumi.getter(name="isSystem")
    def is_system(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_system")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter(name="modifiedBy")
    def modified_by(self) -> pulumi.Output[str]:
        return pulumi.get(self, "modified_by")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the SLO folder. The name must be alphanumeric.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        The identifier of the SLO Folder that contains this SLO Folder. Defaults to the root folder.

        Additional data provided in state:
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="postRequestMap")
    def post_request_map(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "post_request_map")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        return pulumi.get(self, "version")

