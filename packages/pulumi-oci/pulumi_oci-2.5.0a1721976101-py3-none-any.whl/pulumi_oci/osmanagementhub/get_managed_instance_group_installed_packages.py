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
    'GetManagedInstanceGroupInstalledPackagesResult',
    'AwaitableGetManagedInstanceGroupInstalledPackagesResult',
    'get_managed_instance_group_installed_packages',
    'get_managed_instance_group_installed_packages_output',
]

@pulumi.output_type
class GetManagedInstanceGroupInstalledPackagesResult:
    """
    A collection of values returned by getManagedInstanceGroupInstalledPackages.
    """
    def __init__(__self__, compartment_id=None, display_name_contains=None, display_names=None, filters=None, id=None, managed_instance_group_id=None, managed_instance_group_installed_package_collections=None, time_install_date_end=None, time_install_date_start=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name_contains and not isinstance(display_name_contains, str):
            raise TypeError("Expected argument 'display_name_contains' to be a str")
        pulumi.set(__self__, "display_name_contains", display_name_contains)
        if display_names and not isinstance(display_names, list):
            raise TypeError("Expected argument 'display_names' to be a list")
        pulumi.set(__self__, "display_names", display_names)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_instance_group_id and not isinstance(managed_instance_group_id, str):
            raise TypeError("Expected argument 'managed_instance_group_id' to be a str")
        pulumi.set(__self__, "managed_instance_group_id", managed_instance_group_id)
        if managed_instance_group_installed_package_collections and not isinstance(managed_instance_group_installed_package_collections, list):
            raise TypeError("Expected argument 'managed_instance_group_installed_package_collections' to be a list")
        pulumi.set(__self__, "managed_instance_group_installed_package_collections", managed_instance_group_installed_package_collections)
        if time_install_date_end and not isinstance(time_install_date_end, str):
            raise TypeError("Expected argument 'time_install_date_end' to be a str")
        pulumi.set(__self__, "time_install_date_end", time_install_date_end)
        if time_install_date_start and not isinstance(time_install_date_start, str):
            raise TypeError("Expected argument 'time_install_date_start' to be a str")
        pulumi.set(__self__, "time_install_date_start", time_install_date_start)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayNameContains")
    def display_name_contains(self) -> Optional[str]:
        return pulumi.get(self, "display_name_contains")

    @property
    @pulumi.getter(name="displayNames")
    def display_names(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "display_names")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetManagedInstanceGroupInstalledPackagesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedInstanceGroupId")
    def managed_instance_group_id(self) -> str:
        return pulumi.get(self, "managed_instance_group_id")

    @property
    @pulumi.getter(name="managedInstanceGroupInstalledPackageCollections")
    def managed_instance_group_installed_package_collections(self) -> Sequence['outputs.GetManagedInstanceGroupInstalledPackagesManagedInstanceGroupInstalledPackageCollectionResult']:
        """
        The list of managed_instance_group_installed_package_collection.
        """
        return pulumi.get(self, "managed_instance_group_installed_package_collections")

    @property
    @pulumi.getter(name="timeInstallDateEnd")
    def time_install_date_end(self) -> Optional[str]:
        return pulumi.get(self, "time_install_date_end")

    @property
    @pulumi.getter(name="timeInstallDateStart")
    def time_install_date_start(self) -> Optional[str]:
        return pulumi.get(self, "time_install_date_start")


class AwaitableGetManagedInstanceGroupInstalledPackagesResult(GetManagedInstanceGroupInstalledPackagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstanceGroupInstalledPackagesResult(
            compartment_id=self.compartment_id,
            display_name_contains=self.display_name_contains,
            display_names=self.display_names,
            filters=self.filters,
            id=self.id,
            managed_instance_group_id=self.managed_instance_group_id,
            managed_instance_group_installed_package_collections=self.managed_instance_group_installed_package_collections,
            time_install_date_end=self.time_install_date_end,
            time_install_date_start=self.time_install_date_start)


def get_managed_instance_group_installed_packages(compartment_id: Optional[str] = None,
                                                  display_name_contains: Optional[str] = None,
                                                  display_names: Optional[Sequence[str]] = None,
                                                  filters: Optional[Sequence[pulumi.InputType['GetManagedInstanceGroupInstalledPackagesFilterArgs']]] = None,
                                                  managed_instance_group_id: Optional[str] = None,
                                                  time_install_date_end: Optional[str] = None,
                                                  time_install_date_start: Optional[str] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstanceGroupInstalledPackagesResult:
    """
    This data source provides the list of Managed Instance Group Installed Packages in Oracle Cloud Infrastructure Os Management Hub service.

    Lists installed packages on the specified managed instances group. Filter the list against a variety
    of criteria including but not limited to the package name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_group_installed_packages = oci.OsManagementHub.get_managed_instance_group_installed_packages(managed_instance_group_id=test_managed_instance_group["id"],
        compartment_id=compartment_id,
        display_names=managed_instance_group_installed_package_display_name,
        display_name_contains=managed_instance_group_installed_package_display_name_contains,
        time_install_date_end=managed_instance_group_installed_package_time_install_date_end,
        time_install_date_start=managed_instance_group_installed_package_time_install_date_start)
    ```


    :param str compartment_id: The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
    :param str display_name_contains: A filter to return resources that may partially match the given display name.
    :param Sequence[str] display_names: A filter to return resources that match the given display names.
    :param str managed_instance_group_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
    :param str time_install_date_end: A filter to return only packages that were installed on or before the date provided, in ISO 8601 format.  Example: 2017-07-14T02:40:00.000Z
    :param str time_install_date_start: The install date after which to list all packages, in ISO 8601 format  Example: 2017-07-14T02:40:00.000Z
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayNameContains'] = display_name_contains
    __args__['displayNames'] = display_names
    __args__['filters'] = filters
    __args__['managedInstanceGroupId'] = managed_instance_group_id
    __args__['timeInstallDateEnd'] = time_install_date_end
    __args__['timeInstallDateStart'] = time_install_date_start
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsManagementHub/getManagedInstanceGroupInstalledPackages:getManagedInstanceGroupInstalledPackages', __args__, opts=opts, typ=GetManagedInstanceGroupInstalledPackagesResult).value

    return AwaitableGetManagedInstanceGroupInstalledPackagesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name_contains=pulumi.get(__ret__, 'display_name_contains'),
        display_names=pulumi.get(__ret__, 'display_names'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        managed_instance_group_id=pulumi.get(__ret__, 'managed_instance_group_id'),
        managed_instance_group_installed_package_collections=pulumi.get(__ret__, 'managed_instance_group_installed_package_collections'),
        time_install_date_end=pulumi.get(__ret__, 'time_install_date_end'),
        time_install_date_start=pulumi.get(__ret__, 'time_install_date_start'))


@_utilities.lift_output_func(get_managed_instance_group_installed_packages)
def get_managed_instance_group_installed_packages_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                         display_name_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                                         display_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                         filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetManagedInstanceGroupInstalledPackagesFilterArgs']]]]] = None,
                                                         managed_instance_group_id: Optional[pulumi.Input[str]] = None,
                                                         time_install_date_end: Optional[pulumi.Input[Optional[str]]] = None,
                                                         time_install_date_start: Optional[pulumi.Input[Optional[str]]] = None,
                                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstanceGroupInstalledPackagesResult]:
    """
    This data source provides the list of Managed Instance Group Installed Packages in Oracle Cloud Infrastructure Os Management Hub service.

    Lists installed packages on the specified managed instances group. Filter the list against a variety
    of criteria including but not limited to the package name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_instance_group_installed_packages = oci.OsManagementHub.get_managed_instance_group_installed_packages(managed_instance_group_id=test_managed_instance_group["id"],
        compartment_id=compartment_id,
        display_names=managed_instance_group_installed_package_display_name,
        display_name_contains=managed_instance_group_installed_package_display_name_contains,
        time_install_date_end=managed_instance_group_installed_package_time_install_date_end,
        time_install_date_start=managed_instance_group_installed_package_time_install_date_start)
    ```


    :param str compartment_id: The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
    :param str display_name_contains: A filter to return resources that may partially match the given display name.
    :param Sequence[str] display_names: A filter to return resources that match the given display names.
    :param str managed_instance_group_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
    :param str time_install_date_end: A filter to return only packages that were installed on or before the date provided, in ISO 8601 format.  Example: 2017-07-14T02:40:00.000Z
    :param str time_install_date_start: The install date after which to list all packages, in ISO 8601 format  Example: 2017-07-14T02:40:00.000Z
    """
    ...
