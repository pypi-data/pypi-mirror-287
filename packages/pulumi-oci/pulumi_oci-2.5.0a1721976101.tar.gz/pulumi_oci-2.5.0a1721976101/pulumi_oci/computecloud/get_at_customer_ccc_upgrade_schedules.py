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
    'GetAtCustomerCccUpgradeSchedulesResult',
    'AwaitableGetAtCustomerCccUpgradeSchedulesResult',
    'get_at_customer_ccc_upgrade_schedules',
    'get_at_customer_ccc_upgrade_schedules_output',
]

@pulumi.output_type
class GetAtCustomerCccUpgradeSchedulesResult:
    """
    A collection of values returned by getAtCustomerCccUpgradeSchedules.
    """
    def __init__(__self__, access_level=None, ccc_upgrade_schedule_collections=None, ccc_upgrade_schedule_id=None, compartment_id=None, compartment_id_in_subtree=None, display_name=None, display_name_contains=None, filters=None, id=None, state=None):
        if access_level and not isinstance(access_level, str):
            raise TypeError("Expected argument 'access_level' to be a str")
        pulumi.set(__self__, "access_level", access_level)
        if ccc_upgrade_schedule_collections and not isinstance(ccc_upgrade_schedule_collections, list):
            raise TypeError("Expected argument 'ccc_upgrade_schedule_collections' to be a list")
        pulumi.set(__self__, "ccc_upgrade_schedule_collections", ccc_upgrade_schedule_collections)
        if ccc_upgrade_schedule_id and not isinstance(ccc_upgrade_schedule_id, str):
            raise TypeError("Expected argument 'ccc_upgrade_schedule_id' to be a str")
        pulumi.set(__self__, "ccc_upgrade_schedule_id", ccc_upgrade_schedule_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if display_name_contains and not isinstance(display_name_contains, str):
            raise TypeError("Expected argument 'display_name_contains' to be a str")
        pulumi.set(__self__, "display_name_contains", display_name_contains)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[str]:
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter(name="cccUpgradeScheduleCollections")
    def ccc_upgrade_schedule_collections(self) -> Sequence['outputs.GetAtCustomerCccUpgradeSchedulesCccUpgradeScheduleCollectionResult']:
        """
        The list of ccc_upgrade_schedule_collection.
        """
        return pulumi.get(self, "ccc_upgrade_schedule_collections")

    @property
    @pulumi.getter(name="cccUpgradeScheduleId")
    def ccc_upgrade_schedule_id(self) -> Optional[str]:
        return pulumi.get(self, "ccc_upgrade_schedule_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        Compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the Compute Cloud@Customer upgrade schedule.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> Optional[bool]:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Compute Cloud@Customer upgrade schedule display name. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="displayNameContains")
    def display_name_contains(self) -> Optional[str]:
        return pulumi.get(self, "display_name_contains")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAtCustomerCccUpgradeSchedulesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Lifecycle state of the resource.
        """
        return pulumi.get(self, "state")


class AwaitableGetAtCustomerCccUpgradeSchedulesResult(GetAtCustomerCccUpgradeSchedulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAtCustomerCccUpgradeSchedulesResult(
            access_level=self.access_level,
            ccc_upgrade_schedule_collections=self.ccc_upgrade_schedule_collections,
            ccc_upgrade_schedule_id=self.ccc_upgrade_schedule_id,
            compartment_id=self.compartment_id,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            display_name=self.display_name,
            display_name_contains=self.display_name_contains,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_at_customer_ccc_upgrade_schedules(access_level: Optional[str] = None,
                                          ccc_upgrade_schedule_id: Optional[str] = None,
                                          compartment_id: Optional[str] = None,
                                          compartment_id_in_subtree: Optional[bool] = None,
                                          display_name: Optional[str] = None,
                                          display_name_contains: Optional[str] = None,
                                          filters: Optional[Sequence[pulumi.InputType['GetAtCustomerCccUpgradeSchedulesFilterArgs']]] = None,
                                          state: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAtCustomerCccUpgradeSchedulesResult:
    """
    This data source provides the list of Ccc Upgrade Schedules in Oracle Cloud Infrastructure Compute Cloud At Customer service.

    Returns a list of Compute Cloud@Customer upgrade schedules.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_ccc_upgrade_schedules = oci.ComputeCloud.get_at_customer_ccc_upgrade_schedules(access_level=ccc_upgrade_schedule_access_level,
        ccc_upgrade_schedule_id=test_ccc_upgrade_schedule["id"],
        compartment_id=compartment_id,
        compartment_id_in_subtree=ccc_upgrade_schedule_compartment_id_in_subtree,
        display_name=ccc_upgrade_schedule_display_name,
        display_name_contains=ccc_upgrade_schedule_display_name_contains,
        state=ccc_upgrade_schedule_state)
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str ccc_upgrade_schedule_id: Compute Cloud@Customer upgrade schedule [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and sub-compartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str display_name_contains: A filter to return only resources whose display name contains the substring.
    :param str state: A filter to return resources only when their lifecycleState matches the given lifecycleState.
    """
    __args__ = dict()
    __args__['accessLevel'] = access_level
    __args__['cccUpgradeScheduleId'] = ccc_upgrade_schedule_id
    __args__['compartmentId'] = compartment_id
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['displayName'] = display_name
    __args__['displayNameContains'] = display_name_contains
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ComputeCloud/getAtCustomerCccUpgradeSchedules:getAtCustomerCccUpgradeSchedules', __args__, opts=opts, typ=GetAtCustomerCccUpgradeSchedulesResult).value

    return AwaitableGetAtCustomerCccUpgradeSchedulesResult(
        access_level=pulumi.get(__ret__, 'access_level'),
        ccc_upgrade_schedule_collections=pulumi.get(__ret__, 'ccc_upgrade_schedule_collections'),
        ccc_upgrade_schedule_id=pulumi.get(__ret__, 'ccc_upgrade_schedule_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        display_name=pulumi.get(__ret__, 'display_name'),
        display_name_contains=pulumi.get(__ret__, 'display_name_contains'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_at_customer_ccc_upgrade_schedules)
def get_at_customer_ccc_upgrade_schedules_output(access_level: Optional[pulumi.Input[Optional[str]]] = None,
                                                 ccc_upgrade_schedule_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                 compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                 compartment_id_in_subtree: Optional[pulumi.Input[Optional[bool]]] = None,
                                                 display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                                 display_name_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAtCustomerCccUpgradeSchedulesFilterArgs']]]]] = None,
                                                 state: Optional[pulumi.Input[Optional[str]]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAtCustomerCccUpgradeSchedulesResult]:
    """
    This data source provides the list of Ccc Upgrade Schedules in Oracle Cloud Infrastructure Compute Cloud At Customer service.

    Returns a list of Compute Cloud@Customer upgrade schedules.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_ccc_upgrade_schedules = oci.ComputeCloud.get_at_customer_ccc_upgrade_schedules(access_level=ccc_upgrade_schedule_access_level,
        ccc_upgrade_schedule_id=test_ccc_upgrade_schedule["id"],
        compartment_id=compartment_id,
        compartment_id_in_subtree=ccc_upgrade_schedule_compartment_id_in_subtree,
        display_name=ccc_upgrade_schedule_display_name,
        display_name_contains=ccc_upgrade_schedule_display_name_contains,
        state=ccc_upgrade_schedule_state)
    ```


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param str ccc_upgrade_schedule_id: Compute Cloud@Customer upgrade schedule [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and sub-compartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str display_name_contains: A filter to return only resources whose display name contains the substring.
    :param str state: A filter to return resources only when their lifecycleState matches the given lifecycleState.
    """
    ...
