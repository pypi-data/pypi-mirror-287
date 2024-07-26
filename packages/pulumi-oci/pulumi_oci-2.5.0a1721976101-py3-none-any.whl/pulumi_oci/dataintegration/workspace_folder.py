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

__all__ = ['WorkspaceFolderArgs', 'WorkspaceFolder']

@pulumi.input_type
class WorkspaceFolderArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str],
                 registry_metadata: pulumi.Input['WorkspaceFolderRegistryMetadataArgs'],
                 workspace_id: pulumi.Input[str],
                 category_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder_key: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 model_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_status: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a WorkspaceFolder resource.
        :param pulumi.Input[str] identifier: (Updatable) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.
        :param pulumi.Input['WorkspaceFolderRegistryMetadataArgs'] registry_metadata: (Updatable) Information about the object and its parent.
        :param pulumi.Input[str] workspace_id: The workspace ID.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] category_name: (Updatable) The category name.
        :param pulumi.Input[str] description: (Updatable) A user defined description for the folder.
        :param pulumi.Input[str] key: (Updatable) Currently not used on folder creation. Reserved for future.
        :param pulumi.Input[str] model_version: (Updatable) The model version of an object.
        :param pulumi.Input[str] name: (Updatable) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.
        :param pulumi.Input[int] object_status: (Updatable) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
        """
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "registry_metadata", registry_metadata)
        pulumi.set(__self__, "workspace_id", workspace_id)
        if category_name is not None:
            pulumi.set(__self__, "category_name", category_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if folder_key is not None:
            pulumi.set(__self__, "folder_key", folder_key)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if model_version is not None:
            pulumi.set(__self__, "model_version", model_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if object_status is not None:
            pulumi.set(__self__, "object_status", object_status)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        """
        (Updatable) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="registryMetadata")
    def registry_metadata(self) -> pulumi.Input['WorkspaceFolderRegistryMetadataArgs']:
        """
        (Updatable) Information about the object and its parent.
        """
        return pulumi.get(self, "registry_metadata")

    @registry_metadata.setter
    def registry_metadata(self, value: pulumi.Input['WorkspaceFolderRegistryMetadataArgs']):
        pulumi.set(self, "registry_metadata", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        The workspace ID.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)

    @property
    @pulumi.getter(name="categoryName")
    def category_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The category name.
        """
        return pulumi.get(self, "category_name")

    @category_name.setter
    def category_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user defined description for the folder.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="folderKey")
    def folder_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "folder_key")

    @folder_key.setter
    def folder_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_key", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Currently not used on folder creation. Reserved for future.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="modelVersion")
    def model_version(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The model version of an object.
        """
        return pulumi.get(self, "model_version")

    @model_version.setter
    def model_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="objectStatus")
    def object_status(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
        """
        return pulumi.get(self, "object_status")

    @object_status.setter
    def object_status(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "object_status", value)


@pulumi.input_type
class _WorkspaceFolderState:
    def __init__(__self__, *,
                 category_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder_key: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 key_map: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 metadatas: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceFolderMetadataArgs']]]] = None,
                 model_type: Optional[pulumi.Input[str]] = None,
                 model_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_status: Optional[pulumi.Input[int]] = None,
                 object_version: Optional[pulumi.Input[int]] = None,
                 parent_reves: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceFolderParentRefArgs']]]] = None,
                 registry_metadata: Optional[pulumi.Input['WorkspaceFolderRegistryMetadataArgs']] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WorkspaceFolder resources.
        :param pulumi.Input[str] category_name: (Updatable) The category name.
        :param pulumi.Input[str] description: (Updatable) A user defined description for the folder.
        :param pulumi.Input[str] identifier: (Updatable) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.
        :param pulumi.Input[str] key: (Updatable) Currently not used on folder creation. Reserved for future.
        :param pulumi.Input[Mapping[str, Any]] key_map: A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.
        :param pulumi.Input[Sequence[pulumi.Input['WorkspaceFolderMetadataArgs']]] metadatas: A summary type containing information about the object including its key, name and when/who created/updated it.
        :param pulumi.Input[str] model_type: The type of the object.
        :param pulumi.Input[str] model_version: (Updatable) The model version of an object.
        :param pulumi.Input[str] name: (Updatable) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.
        :param pulumi.Input[int] object_status: (Updatable) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
        :param pulumi.Input[int] object_version: The version of the object that is used to track changes in the object instance.
        :param pulumi.Input[Sequence[pulumi.Input['WorkspaceFolderParentRefArgs']]] parent_reves: A reference to the object's parent.
        :param pulumi.Input['WorkspaceFolderRegistryMetadataArgs'] registry_metadata: (Updatable) Information about the object and its parent.
        :param pulumi.Input[str] workspace_id: The workspace ID.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if category_name is not None:
            pulumi.set(__self__, "category_name", category_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if folder_key is not None:
            pulumi.set(__self__, "folder_key", folder_key)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if key_map is not None:
            pulumi.set(__self__, "key_map", key_map)
        if metadatas is not None:
            pulumi.set(__self__, "metadatas", metadatas)
        if model_type is not None:
            pulumi.set(__self__, "model_type", model_type)
        if model_version is not None:
            pulumi.set(__self__, "model_version", model_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if object_status is not None:
            pulumi.set(__self__, "object_status", object_status)
        if object_version is not None:
            pulumi.set(__self__, "object_version", object_version)
        if parent_reves is not None:
            pulumi.set(__self__, "parent_reves", parent_reves)
        if registry_metadata is not None:
            pulumi.set(__self__, "registry_metadata", registry_metadata)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="categoryName")
    def category_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The category name.
        """
        return pulumi.get(self, "category_name")

    @category_name.setter
    def category_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user defined description for the folder.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="folderKey")
    def folder_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "folder_key")

    @folder_key.setter
    def folder_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_key", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Currently not used on folder creation. Reserved for future.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="keyMap")
    def key_map(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.
        """
        return pulumi.get(self, "key_map")

    @key_map.setter
    def key_map(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "key_map", value)

    @property
    @pulumi.getter
    def metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceFolderMetadataArgs']]]]:
        """
        A summary type containing information about the object including its key, name and when/who created/updated it.
        """
        return pulumi.get(self, "metadatas")

    @metadatas.setter
    def metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceFolderMetadataArgs']]]]):
        pulumi.set(self, "metadatas", value)

    @property
    @pulumi.getter(name="modelType")
    def model_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the object.
        """
        return pulumi.get(self, "model_type")

    @model_type.setter
    def model_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_type", value)

    @property
    @pulumi.getter(name="modelVersion")
    def model_version(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The model version of an object.
        """
        return pulumi.get(self, "model_version")

    @model_version.setter
    def model_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="objectStatus")
    def object_status(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
        """
        return pulumi.get(self, "object_status")

    @object_status.setter
    def object_status(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "object_status", value)

    @property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[pulumi.Input[int]]:
        """
        The version of the object that is used to track changes in the object instance.
        """
        return pulumi.get(self, "object_version")

    @object_version.setter
    def object_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "object_version", value)

    @property
    @pulumi.getter(name="parentReves")
    def parent_reves(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceFolderParentRefArgs']]]]:
        """
        A reference to the object's parent.
        """
        return pulumi.get(self, "parent_reves")

    @parent_reves.setter
    def parent_reves(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceFolderParentRefArgs']]]]):
        pulumi.set(self, "parent_reves", value)

    @property
    @pulumi.getter(name="registryMetadata")
    def registry_metadata(self) -> Optional[pulumi.Input['WorkspaceFolderRegistryMetadataArgs']]:
        """
        (Updatable) Information about the object and its parent.
        """
        return pulumi.get(self, "registry_metadata")

    @registry_metadata.setter
    def registry_metadata(self, value: Optional[pulumi.Input['WorkspaceFolderRegistryMetadataArgs']]):
        pulumi.set(self, "registry_metadata", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The workspace ID.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_id", value)


class WorkspaceFolder(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder_key: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 model_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_status: Optional[pulumi.Input[int]] = None,
                 registry_metadata: Optional[pulumi.Input[pulumi.InputType['WorkspaceFolderRegistryMetadataArgs']]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Workspace Folder resource in Oracle Cloud Infrastructure Data Integration service.

        Creates a folder in a project or in another folder, limited to two levels of folders. |
        Folders are used to organize your design-time resources, such as tasks or data flows.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_workspace_folder = oci.data_integration.WorkspaceFolder("test_workspace_folder",
            identifier=workspace_folder_identifier,
            name=workspace_folder_name,
            registry_metadata=oci.data_integration.WorkspaceFolderRegistryMetadataArgs(
                aggregator_key=workspace_folder_registry_metadata_aggregator_key,
                is_favorite=workspace_folder_registry_metadata_is_favorite,
                key=workspace_folder_registry_metadata_key,
                labels=workspace_folder_registry_metadata_labels,
                registry_version=workspace_folder_registry_metadata_registry_version,
            ),
            workspace_id=test_workspace["id"],
            category_name=test_category["name"],
            description=workspace_folder_description,
            key=workspace_folder_key,
            model_version=workspace_folder_model_version,
            object_status=workspace_folder_object_status)
        ```

        ## Import

        WorkspaceFolders can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:DataIntegration/workspaceFolder:WorkspaceFolder test_workspace_folder "workspaces/{workspaceId}/folders/{folderKey}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category_name: (Updatable) The category name.
        :param pulumi.Input[str] description: (Updatable) A user defined description for the folder.
        :param pulumi.Input[str] identifier: (Updatable) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.
        :param pulumi.Input[str] key: (Updatable) Currently not used on folder creation. Reserved for future.
        :param pulumi.Input[str] model_version: (Updatable) The model version of an object.
        :param pulumi.Input[str] name: (Updatable) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.
        :param pulumi.Input[int] object_status: (Updatable) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
        :param pulumi.Input[pulumi.InputType['WorkspaceFolderRegistryMetadataArgs']] registry_metadata: (Updatable) Information about the object and its parent.
        :param pulumi.Input[str] workspace_id: The workspace ID.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceFolderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Workspace Folder resource in Oracle Cloud Infrastructure Data Integration service.

        Creates a folder in a project or in another folder, limited to two levels of folders. |
        Folders are used to organize your design-time resources, such as tasks or data flows.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_workspace_folder = oci.data_integration.WorkspaceFolder("test_workspace_folder",
            identifier=workspace_folder_identifier,
            name=workspace_folder_name,
            registry_metadata=oci.data_integration.WorkspaceFolderRegistryMetadataArgs(
                aggregator_key=workspace_folder_registry_metadata_aggregator_key,
                is_favorite=workspace_folder_registry_metadata_is_favorite,
                key=workspace_folder_registry_metadata_key,
                labels=workspace_folder_registry_metadata_labels,
                registry_version=workspace_folder_registry_metadata_registry_version,
            ),
            workspace_id=test_workspace["id"],
            category_name=test_category["name"],
            description=workspace_folder_description,
            key=workspace_folder_key,
            model_version=workspace_folder_model_version,
            object_status=workspace_folder_object_status)
        ```

        ## Import

        WorkspaceFolders can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:DataIntegration/workspaceFolder:WorkspaceFolder test_workspace_folder "workspaces/{workspaceId}/folders/{folderKey}"
        ```

        :param str resource_name: The name of the resource.
        :param WorkspaceFolderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceFolderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder_key: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 model_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 object_status: Optional[pulumi.Input[int]] = None,
                 registry_metadata: Optional[pulumi.Input[pulumi.InputType['WorkspaceFolderRegistryMetadataArgs']]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceFolderArgs.__new__(WorkspaceFolderArgs)

            __props__.__dict__["category_name"] = category_name
            __props__.__dict__["description"] = description
            __props__.__dict__["folder_key"] = folder_key
            if identifier is None and not opts.urn:
                raise TypeError("Missing required property 'identifier'")
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["key"] = key
            __props__.__dict__["model_version"] = model_version
            __props__.__dict__["name"] = name
            __props__.__dict__["object_status"] = object_status
            if registry_metadata is None and not opts.urn:
                raise TypeError("Missing required property 'registry_metadata'")
            __props__.__dict__["registry_metadata"] = registry_metadata
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["key_map"] = None
            __props__.__dict__["metadatas"] = None
            __props__.__dict__["model_type"] = None
            __props__.__dict__["object_version"] = None
            __props__.__dict__["parent_reves"] = None
        super(WorkspaceFolder, __self__).__init__(
            'oci:DataIntegration/workspaceFolder:WorkspaceFolder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            category_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            folder_key: Optional[pulumi.Input[str]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            key_map: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkspaceFolderMetadataArgs']]]]] = None,
            model_type: Optional[pulumi.Input[str]] = None,
            model_version: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            object_status: Optional[pulumi.Input[int]] = None,
            object_version: Optional[pulumi.Input[int]] = None,
            parent_reves: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkspaceFolderParentRefArgs']]]]] = None,
            registry_metadata: Optional[pulumi.Input[pulumi.InputType['WorkspaceFolderRegistryMetadataArgs']]] = None,
            workspace_id: Optional[pulumi.Input[str]] = None) -> 'WorkspaceFolder':
        """
        Get an existing WorkspaceFolder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category_name: (Updatable) The category name.
        :param pulumi.Input[str] description: (Updatable) A user defined description for the folder.
        :param pulumi.Input[str] identifier: (Updatable) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.
        :param pulumi.Input[str] key: (Updatable) Currently not used on folder creation. Reserved for future.
        :param pulumi.Input[Mapping[str, Any]] key_map: A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkspaceFolderMetadataArgs']]]] metadatas: A summary type containing information about the object including its key, name and when/who created/updated it.
        :param pulumi.Input[str] model_type: The type of the object.
        :param pulumi.Input[str] model_version: (Updatable) The model version of an object.
        :param pulumi.Input[str] name: (Updatable) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.
        :param pulumi.Input[int] object_status: (Updatable) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
        :param pulumi.Input[int] object_version: The version of the object that is used to track changes in the object instance.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkspaceFolderParentRefArgs']]]] parent_reves: A reference to the object's parent.
        :param pulumi.Input[pulumi.InputType['WorkspaceFolderRegistryMetadataArgs']] registry_metadata: (Updatable) Information about the object and its parent.
        :param pulumi.Input[str] workspace_id: The workspace ID.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceFolderState.__new__(_WorkspaceFolderState)

        __props__.__dict__["category_name"] = category_name
        __props__.__dict__["description"] = description
        __props__.__dict__["folder_key"] = folder_key
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["key"] = key
        __props__.__dict__["key_map"] = key_map
        __props__.__dict__["metadatas"] = metadatas
        __props__.__dict__["model_type"] = model_type
        __props__.__dict__["model_version"] = model_version
        __props__.__dict__["name"] = name
        __props__.__dict__["object_status"] = object_status
        __props__.__dict__["object_version"] = object_version
        __props__.__dict__["parent_reves"] = parent_reves
        __props__.__dict__["registry_metadata"] = registry_metadata
        __props__.__dict__["workspace_id"] = workspace_id
        return WorkspaceFolder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="categoryName")
    def category_name(self) -> pulumi.Output[str]:
        """
        (Updatable) The category name.
        """
        return pulumi.get(self, "category_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        (Updatable) A user defined description for the folder.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="folderKey")
    def folder_key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "folder_key")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        (Updatable) Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        (Updatable) Currently not used on folder creation. Reserved for future.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="keyMap")
    def key_map(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        A key map. If provided, the key is replaced with generated key. This structure provides mapping between user provided key and generated key.
        """
        return pulumi.get(self, "key_map")

    @property
    @pulumi.getter
    def metadatas(self) -> pulumi.Output[Sequence['outputs.WorkspaceFolderMetadata']]:
        """
        A summary type containing information about the object including its key, name and when/who created/updated it.
        """
        return pulumi.get(self, "metadatas")

    @property
    @pulumi.getter(name="modelType")
    def model_type(self) -> pulumi.Output[str]:
        """
        The type of the object.
        """
        return pulumi.get(self, "model_type")

    @property
    @pulumi.getter(name="modelVersion")
    def model_version(self) -> pulumi.Output[str]:
        """
        (Updatable) The model version of an object.
        """
        return pulumi.get(self, "model_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        (Updatable) Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectStatus")
    def object_status(self) -> pulumi.Output[int]:
        """
        (Updatable) The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
        """
        return pulumi.get(self, "object_status")

    @property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> pulumi.Output[int]:
        """
        The version of the object that is used to track changes in the object instance.
        """
        return pulumi.get(self, "object_version")

    @property
    @pulumi.getter(name="parentReves")
    def parent_reves(self) -> pulumi.Output[Sequence['outputs.WorkspaceFolderParentRef']]:
        """
        A reference to the object's parent.
        """
        return pulumi.get(self, "parent_reves")

    @property
    @pulumi.getter(name="registryMetadata")
    def registry_metadata(self) -> pulumi.Output['outputs.WorkspaceFolderRegistryMetadata']:
        """
        (Updatable) Information about the object and its parent.
        """
        return pulumi.get(self, "registry_metadata")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[str]:
        """
        The workspace ID.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "workspace_id")

