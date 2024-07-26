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
    'GetManagedInstanceGroupsResult',
    'AwaitableGetManagedInstanceGroupsResult',
    'get_managed_instance_groups',
    'get_managed_instance_groups_output',
]

@pulumi.output_type
class GetManagedInstanceGroupsResult:
    """
    A collection of values returned by getManagedInstanceGroups.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, managed_instance_groups=None, os_family=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_instance_groups and not isinstance(managed_instance_groups, list):
            raise TypeError("Expected argument 'managed_instance_groups' to be a list")
        pulumi.set(__self__, "managed_instance_groups", managed_instance_groups)
        if os_family and not isinstance(os_family, str):
            raise TypeError("Expected argument 'os_family' to be a str")
        pulumi.set(__self__, "os_family", os_family)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        OCID for the Compartment
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        User friendly name
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedInstanceGroupsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedInstanceGroups")
    def managed_instance_groups(self) -> Sequence['outputs.GetManagedInstanceGroupsManagedInstanceGroupResult']:
        """
        The list of managed_instance_groups.
        """
        return pulumi.get(self, "managed_instance_groups")

    @property
    @pulumi.getter(name="osFamily")
    def os_family(self) -> Optional[str]:
        """
        The Operating System type of the managed instance.
        """
        return pulumi.get(self, "os_family")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the Software Source.
        """
        return pulumi.get(self, "state")


class AwaitableGetManagedInstanceGroupsResult(GetManagedInstanceGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstanceGroupsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            managed_instance_groups=self.managed_instance_groups,
            os_family=self.os_family,
            state=self.state)


def get_managed_instance_groups(compartment_id: Optional[str] = None,
                                display_name: Optional[str] = None,
                                filters: Optional[Sequence[pulumi.InputType['GetManagedInstanceGroupsFilterArgs']]] = None,
                                os_family: Optional[str] = None,
                                state: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstanceGroupsResult:
    """
    This data source provides the list of Managed Instance Groups in Oracle Cloud Infrastructure OS Management service.

    Returns a list of all Managed Instance Groups.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_groups = oci.OsManagement.get_managed_instance_groups(compartment_id=compartment_id,
        display_name=managed_instance_group_display_name,
        os_family=managed_instance_group_os_family,
        state=managed_instance_group_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str os_family: The OS family for which to list resources.
    :param str state: The current lifecycle state for the object.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['osFamily'] = os_family
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsManagement/getManagedInstanceGroups:getManagedInstanceGroups', __args__, opts=opts, typ=GetManagedInstanceGroupsResult).value

    return AwaitableGetManagedInstanceGroupsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_instance_groups=pulumi.get(__ret__, 'managed_instance_groups'),
        os_family=pulumi.get(__ret__, 'os_family'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_managed_instance_groups)
def get_managed_instance_groups_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                       display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedInstanceGroupsFilterArgs']]]]] = None,
                                       os_family: Optional[pulumi.Input[Optional[str]]] = None,
                                       state: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstanceGroupsResult]:
    """
    This data source provides the list of Managed Instance Groups in Oracle Cloud Infrastructure OS Management service.

    Returns a list of all Managed Instance Groups.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_groups = oci.OsManagement.get_managed_instance_groups(compartment_id=compartment_id,
        display_name=managed_instance_group_display_name,
        os_family=managed_instance_group_os_family,
        state=managed_instance_group_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str os_family: The OS family for which to list resources.
    :param str state: The current lifecycle state for the object.
    """
    ...
