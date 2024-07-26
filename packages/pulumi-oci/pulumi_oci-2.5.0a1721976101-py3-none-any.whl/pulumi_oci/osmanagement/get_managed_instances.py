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
    'GetManagedInstancesResult',
    'AwaitableGetManagedInstancesResult',
    'get_managed_instances',
    'get_managed_instances_output',
]

@pulumi.output_type
class GetManagedInstancesResult:
    """
    A collection of values returned by getManagedInstances.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, managed_instances=None, os_family=None):
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
        if managed_instances and not isinstance(managed_instances, list):
            raise TypeError("Expected argument 'managed_instances' to be a list")
        pulumi.set(__self__, "managed_instances", managed_instances)
        if os_family and not isinstance(os_family, str):
            raise TypeError("Expected argument 'os_family' to be a str")
        pulumi.set(__self__, "os_family", os_family)

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
    def filters(self) -> Optional[Sequence['outputs.GetManagedInstancesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedInstances")
    def managed_instances(self) -> Sequence['outputs.GetManagedInstancesManagedInstanceResult']:
        """
        The list of managed_instances.
        """
        return pulumi.get(self, "managed_instances")

    @property
    @pulumi.getter(name="osFamily")
    def os_family(self) -> Optional[str]:
        """
        The Operating System type of the managed instance.
        """
        return pulumi.get(self, "os_family")


class AwaitableGetManagedInstancesResult(GetManagedInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstancesResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            managed_instances=self.managed_instances,
            os_family=self.os_family)


def get_managed_instances(compartment_id: Optional[str] = None,
                          display_name: Optional[str] = None,
                          filters: Optional[Sequence[pulumi.InputType['GetManagedInstancesFilterArgs']]] = None,
                          os_family: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstancesResult:
    """
    This data source provides the list of Managed Instances in Oracle Cloud Infrastructure OS Management service.

    Returns a list of all Managed Instances.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instances = oci.OsManagement.get_managed_instances(compartment_id=compartment_id,
        display_name=managed_instance_display_name,
        os_family=managed_instance_os_family)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str os_family: The OS family for which to list resources.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['osFamily'] = os_family
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsManagement/getManagedInstances:getManagedInstances', __args__, opts=opts, typ=GetManagedInstancesResult).value

    return AwaitableGetManagedInstancesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_instances=pulumi.get(__ret__, 'managed_instances'),
        os_family=pulumi.get(__ret__, 'os_family'))


@_utilities.lift_output_func(get_managed_instances)
def get_managed_instances_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                 display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedInstancesFilterArgs']]]]] = None,
                                 os_family: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstancesResult]:
    """
    This data source provides the list of Managed Instances in Oracle Cloud Infrastructure OS Management service.

    Returns a list of all Managed Instances.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instances = oci.OsManagement.get_managed_instances(compartment_id=compartment_id,
        display_name=managed_instance_display_name,
        os_family=managed_instance_os_family)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str os_family: The OS family for which to list resources.
    """
    ...
