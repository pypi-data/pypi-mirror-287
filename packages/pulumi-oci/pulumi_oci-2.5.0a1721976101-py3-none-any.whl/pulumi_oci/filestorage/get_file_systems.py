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

__all__ = [
    'GetFileSystemsResult',
    'AwaitableGetFileSystemsResult',
    'get_file_systems',
    'get_file_systems_output',
]

@pulumi.output_type
class GetFileSystemsResult:
    """
    A collection of values returned by getFileSystems.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, display_name=None, file_systems=None, filesystem_snapshot_policy_id=None, filters=None, id=None, parent_file_system_id=None, source_snapshot_id=None, state=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if file_systems and not isinstance(file_systems, list):
            raise TypeError("Expected argument 'file_systems' to be a list")
        pulumi.set(__self__, "file_systems", file_systems)
        if filesystem_snapshot_policy_id and not isinstance(filesystem_snapshot_policy_id, str):
            raise TypeError("Expected argument 'filesystem_snapshot_policy_id' to be a str")
        pulumi.set(__self__, "filesystem_snapshot_policy_id", filesystem_snapshot_policy_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if parent_file_system_id and not isinstance(parent_file_system_id, str):
            raise TypeError("Expected argument 'parent_file_system_id' to be a str")
        pulumi.set(__self__, "parent_file_system_id", parent_file_system_id)
        if source_snapshot_id and not isinstance(source_snapshot_id, str):
            raise TypeError("Expected argument 'source_snapshot_id' to be a str")
        pulumi.set(__self__, "source_snapshot_id", source_snapshot_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The availability domain the file system is in. May be unset as a blank or NULL value.  Example: `Uocm:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the file system.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.  Example: `My file system`
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="fileSystems")
    def file_systems(self) -> Sequence['outputs.GetFileSystemsFileSystemResult']:
        """
        The list of file_systems.
        """
        return pulumi.get(self, "file_systems")

    @property
    @pulumi.getter(name="filesystemSnapshotPolicyId")
    def filesystem_snapshot_policy_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated file system snapshot policy, which controls the frequency of snapshot creation and retention period of the taken snapshots.
        """
        return pulumi.get(self, "filesystem_snapshot_policy_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetFileSystemsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="parentFileSystemId")
    def parent_file_system_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system that contains the source snapshot of a cloned file system. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        """
        return pulumi.get(self, "parent_file_system_id")

    @property
    @pulumi.getter(name="sourceSnapshotId")
    def source_snapshot_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source snapshot used to create a cloned file system. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        """
        return pulumi.get(self, "source_snapshot_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the file system.
        """
        return pulumi.get(self, "state")


class AwaitableGetFileSystemsResult(GetFileSystemsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFileSystemsResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            file_systems=self.file_systems,
            filesystem_snapshot_policy_id=self.filesystem_snapshot_policy_id,
            filters=self.filters,
            id=self.id,
            parent_file_system_id=self.parent_file_system_id,
            source_snapshot_id=self.source_snapshot_id,
            state=self.state)


def get_file_systems(availability_domain: Optional[str] = None,
                     compartment_id: Optional[str] = None,
                     display_name: Optional[str] = None,
                     filesystem_snapshot_policy_id: Optional[str] = None,
                     filters: Optional[Sequence[pulumi.InputType['GetFileSystemsFilterArgs']]] = None,
                     id: Optional[str] = None,
                     parent_file_system_id: Optional[str] = None,
                     source_snapshot_id: Optional[str] = None,
                     state: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFileSystemsResult:
    """
    This data source provides the list of File Systems in Oracle Cloud Infrastructure File Storage service.

    Lists the file system resources in the specified compartment, or by the specified compartment and
    file system snapshot policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_file_systems = oci.FileStorage.get_file_systems(availability_domain=file_system_availability_domain,
        compartment_id=compartment_id,
        display_name=file_system_display_name,
        filesystem_snapshot_policy_id=test_filesystem_snapshot_policy["id"],
        id=file_system_id,
        parent_file_system_id=test_file_system["id"],
        source_snapshot_id=test_snapshot["id"],
        state=file_system_state)
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A user-friendly name. It does not have to be unique, and it is changeable.  Example: `My resource`
    :param str filesystem_snapshot_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system snapshot policy that is associated with the file systems.
    :param str id: Filter results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.
    :param str parent_file_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system that contains the source snapshot of a cloned file system. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
    :param str source_snapshot_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the snapshot used to create a cloned file system. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
    :param str state: Filter results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    __args__ = dict()
    __args__['availabilityDomain'] = availability_domain
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filesystemSnapshotPolicyId'] = filesystem_snapshot_policy_id
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['parentFileSystemId'] = parent_file_system_id
    __args__['sourceSnapshotId'] = source_snapshot_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:FileStorage/getFileSystems:getFileSystems', __args__, opts=opts, typ=GetFileSystemsResult).value

    return AwaitableGetFileSystemsResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        file_systems=pulumi.get(__ret__, 'file_systems'),
        filesystem_snapshot_policy_id=pulumi.get(__ret__, 'filesystem_snapshot_policy_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        parent_file_system_id=pulumi.get(__ret__, 'parent_file_system_id'),
        source_snapshot_id=pulumi.get(__ret__, 'source_snapshot_id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_file_systems)
def get_file_systems_output(availability_domain: Optional[pulumi.Input[str]] = None,
                            compartment_id: Optional[pulumi.Input[str]] = None,
                            display_name: Optional[pulumi.Input[Optional[str]]] = None,
                            filesystem_snapshot_policy_id: Optional[pulumi.Input[Optional[str]]] = None,
                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetFileSystemsFilterArgs']]]]] = None,
                            id: Optional[pulumi.Input[Optional[str]]] = None,
                            parent_file_system_id: Optional[pulumi.Input[Optional[str]]] = None,
                            source_snapshot_id: Optional[pulumi.Input[Optional[str]]] = None,
                            state: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFileSystemsResult]:
    """
    This data source provides the list of File Systems in Oracle Cloud Infrastructure File Storage service.

    Lists the file system resources in the specified compartment, or by the specified compartment and
    file system snapshot policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_file_systems = oci.FileStorage.get_file_systems(availability_domain=file_system_availability_domain,
        compartment_id=compartment_id,
        display_name=file_system_display_name,
        filesystem_snapshot_policy_id=test_filesystem_snapshot_policy["id"],
        id=file_system_id,
        parent_file_system_id=test_file_system["id"],
        source_snapshot_id=test_snapshot["id"],
        state=file_system_state)
    ```


    :param str availability_domain: The name of the availability domain.  Example: `Uocm:PHX-AD-1`
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A user-friendly name. It does not have to be unique, and it is changeable.  Example: `My resource`
    :param str filesystem_snapshot_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system snapshot policy that is associated with the file systems.
    :param str id: Filter results by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Must be an OCID of the correct type for the resouce type.
    :param str parent_file_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the file system that contains the source snapshot of a cloned file system. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
    :param str source_snapshot_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the snapshot used to create a cloned file system. See [Cloning a File System](https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
    :param str state: Filter results by the specified lifecycle state. Must be a valid state for the resource type.
    """
    ...
