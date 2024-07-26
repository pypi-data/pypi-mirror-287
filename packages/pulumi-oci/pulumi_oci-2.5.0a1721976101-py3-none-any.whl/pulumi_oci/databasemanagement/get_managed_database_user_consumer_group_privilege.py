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

__all__ = [
    'GetManagedDatabaseUserConsumerGroupPrivilegeResult',
    'AwaitableGetManagedDatabaseUserConsumerGroupPrivilegeResult',
    'get_managed_database_user_consumer_group_privilege',
    'get_managed_database_user_consumer_group_privilege_output',
]

@pulumi.output_type
class GetManagedDatabaseUserConsumerGroupPrivilegeResult:
    """
    A collection of values returned by getManagedDatabaseUserConsumerGroupPrivilege.
    """
    def __init__(__self__, id=None, items=None, managed_database_id=None, name=None, user_name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if managed_database_id and not isinstance(managed_database_id, str):
            raise TypeError("Expected argument 'managed_database_id' to be a str")
        pulumi.set(__self__, "managed_database_id", managed_database_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetManagedDatabaseUserConsumerGroupPrivilegeItemResult']:
        """
        An array of consumer group privileges.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="managedDatabaseId")
    def managed_database_id(self) -> str:
        return pulumi.get(self, "managed_database_id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the granted consumer group privilege.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        return pulumi.get(self, "user_name")


class AwaitableGetManagedDatabaseUserConsumerGroupPrivilegeResult(GetManagedDatabaseUserConsumerGroupPrivilegeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedDatabaseUserConsumerGroupPrivilegeResult(
            id=self.id,
            items=self.items,
            managed_database_id=self.managed_database_id,
            name=self.name,
            user_name=self.user_name)


def get_managed_database_user_consumer_group_privilege(managed_database_id: Optional[str] = None,
                                                       name: Optional[str] = None,
                                                       user_name: Optional[str] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedDatabaseUserConsumerGroupPrivilegeResult:
    """
    This data source provides details about a specific Managed Database User Consumer Group Privilege resource in Oracle Cloud Infrastructure Database Management service.

    Gets the list of consumer group privileges granted to a specific user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_user_consumer_group_privilege = oci.DatabaseManagement.get_managed_database_user_consumer_group_privilege(managed_database_id=test_managed_database["id"],
        user_name=test_user["name"],
        name=managed_database_user_consumer_group_privilege_name)
    ```


    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str name: A filter to return only resources that match the entire name.
    :param str user_name: The name of the user whose details are to be viewed.
    """
    __args__ = dict()
    __args__['managedDatabaseId'] = managed_database_id
    __args__['name'] = name
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getManagedDatabaseUserConsumerGroupPrivilege:getManagedDatabaseUserConsumerGroupPrivilege', __args__, opts=opts, typ=GetManagedDatabaseUserConsumerGroupPrivilegeResult).value

    return AwaitableGetManagedDatabaseUserConsumerGroupPrivilegeResult(
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        managed_database_id=pulumi.get(__ret__, 'managed_database_id'),
        name=pulumi.get(__ret__, 'name'),
        user_name=pulumi.get(__ret__, 'user_name'))


@_utilities.lift_output_func(get_managed_database_user_consumer_group_privilege)
def get_managed_database_user_consumer_group_privilege_output(managed_database_id: Optional[pulumi.Input[str]] = None,
                                                              name: Optional[pulumi.Input[Optional[str]]] = None,
                                                              user_name: Optional[pulumi.Input[str]] = None,
                                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedDatabaseUserConsumerGroupPrivilegeResult]:
    """
    This data source provides details about a specific Managed Database User Consumer Group Privilege resource in Oracle Cloud Infrastructure Database Management service.

    Gets the list of consumer group privileges granted to a specific user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_database_user_consumer_group_privilege = oci.DatabaseManagement.get_managed_database_user_consumer_group_privilege(managed_database_id=test_managed_database["id"],
        user_name=test_user["name"],
        name=managed_database_user_consumer_group_privilege_name)
    ```


    :param str managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
    :param str name: A filter to return only resources that match the entire name.
    :param str user_name: The name of the user whose details are to be viewed.
    """
    ...
