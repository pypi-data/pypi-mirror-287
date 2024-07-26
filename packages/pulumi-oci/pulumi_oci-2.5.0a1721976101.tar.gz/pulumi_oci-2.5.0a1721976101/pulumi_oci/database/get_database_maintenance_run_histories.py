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
    'GetDatabaseMaintenanceRunHistoriesResult',
    'AwaitableGetDatabaseMaintenanceRunHistoriesResult',
    'get_database_maintenance_run_histories',
    'get_database_maintenance_run_histories_output',
]

@pulumi.output_type
class GetDatabaseMaintenanceRunHistoriesResult:
    """
    A collection of values returned by getDatabaseMaintenanceRunHistories.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, filters=None, id=None, maintenance_run_histories=None, maintenance_type=None, state=None, target_resource_id=None, target_resource_type=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if maintenance_run_histories and not isinstance(maintenance_run_histories, list):
            raise TypeError("Expected argument 'maintenance_run_histories' to be a list")
        pulumi.set(__self__, "maintenance_run_histories", maintenance_run_histories)
        if maintenance_type and not isinstance(maintenance_type, str):
            raise TypeError("Expected argument 'maintenance_type' to be a str")
        pulumi.set(__self__, "maintenance_type", maintenance_type)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if target_resource_id and not isinstance(target_resource_id, str):
            raise TypeError("Expected argument 'target_resource_id' to be a str")
        pulumi.set(__self__, "target_resource_id", target_resource_id)
        if target_resource_type and not isinstance(target_resource_type, str):
            raise TypeError("Expected argument 'target_resource_type' to be a str")
        pulumi.set(__self__, "target_resource_type", target_resource_type)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> Optional[str]:
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDatabaseMaintenanceRunHistoriesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maintenanceRunHistories")
    def maintenance_run_histories(self) -> Sequence['outputs.GetDatabaseMaintenanceRunHistoriesMaintenanceRunHistoryResult']:
        """
        The list of maintenance_run_histories.
        """
        return pulumi.get(self, "maintenance_run_histories")

    @property
    @pulumi.getter(name="maintenanceType")
    def maintenance_type(self) -> Optional[str]:
        """
        Maintenance type.
        """
        return pulumi.get(self, "maintenance_type")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the maintenance run. For Autonomous Database Serverless instances, valid states are IN_PROGRESS, SUCCEEDED, and FAILED.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[str]:
        """
        The ID of the target resource on which the maintenance run occurs.
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> Optional[str]:
        """
        The type of the target resource on which the maintenance run occurs.
        """
        return pulumi.get(self, "target_resource_type")


class AwaitableGetDatabaseMaintenanceRunHistoriesResult(GetDatabaseMaintenanceRunHistoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseMaintenanceRunHistoriesResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            maintenance_run_histories=self.maintenance_run_histories,
            maintenance_type=self.maintenance_type,
            state=self.state,
            target_resource_id=self.target_resource_id,
            target_resource_type=self.target_resource_type)


def get_database_maintenance_run_histories(availability_domain: Optional[str] = None,
                                           compartment_id: Optional[str] = None,
                                           filters: Optional[Sequence[pulumi.InputType['GetDatabaseMaintenanceRunHistoriesFilterArgs']]] = None,
                                           maintenance_type: Optional[str] = None,
                                           state: Optional[str] = None,
                                           target_resource_id: Optional[str] = None,
                                           target_resource_type: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseMaintenanceRunHistoriesResult:
    """
    This data source provides the list of Maintenance Run Histories in Oracle Cloud Infrastructure Database service.

    Gets a list of the maintenance run histories in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_maintenance_run_histories = oci.Database.get_database_maintenance_run_histories(compartment_id=compartment_id,
        availability_domain=maintenance_run_history_availability_domain,
        maintenance_type=maintenance_run_history_maintenance_type,
        state=maintenance_run_history_state,
        target_resource_id=test_target_resource["id"],
        target_resource_type=maintenance_run_history_target_resource_type)
    ```


    :param str availability_domain: A filter to return only resources that match the given availability domain exactly.
    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str maintenance_type: The maintenance type.
    :param str state: The state of the maintenance run history.
    :param str target_resource_id: The target resource ID.
    :param str target_resource_type: The type of the target resource.
    """
    __args__ = dict()
    __args__['availabilityDomain'] = availability_domain
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['maintenanceType'] = maintenance_type
    __args__['state'] = state
    __args__['targetResourceId'] = target_resource_id
    __args__['targetResourceType'] = target_resource_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getDatabaseMaintenanceRunHistories:getDatabaseMaintenanceRunHistories', __args__, opts=opts, typ=GetDatabaseMaintenanceRunHistoriesResult).value

    return AwaitableGetDatabaseMaintenanceRunHistoriesResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        maintenance_run_histories=pulumi.get(__ret__, 'maintenance_run_histories'),
        maintenance_type=pulumi.get(__ret__, 'maintenance_type'),
        state=pulumi.get(__ret__, 'state'),
        target_resource_id=pulumi.get(__ret__, 'target_resource_id'),
        target_resource_type=pulumi.get(__ret__, 'target_resource_type'))


@_utilities.lift_output_func(get_database_maintenance_run_histories)
def get_database_maintenance_run_histories_output(availability_domain: Optional[pulumi.Input[Optional[str]]] = None,
                                                  compartment_id: Optional[pulumi.Input[str]] = None,
                                                  filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDatabaseMaintenanceRunHistoriesFilterArgs']]]]] = None,
                                                  maintenance_type: Optional[pulumi.Input[Optional[str]]] = None,
                                                  state: Optional[pulumi.Input[Optional[str]]] = None,
                                                  target_resource_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                  target_resource_type: Optional[pulumi.Input[Optional[str]]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseMaintenanceRunHistoriesResult]:
    """
    This data source provides the list of Maintenance Run Histories in Oracle Cloud Infrastructure Database service.

    Gets a list of the maintenance run histories in the specified compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_maintenance_run_histories = oci.Database.get_database_maintenance_run_histories(compartment_id=compartment_id,
        availability_domain=maintenance_run_history_availability_domain,
        maintenance_type=maintenance_run_history_maintenance_type,
        state=maintenance_run_history_state,
        target_resource_id=test_target_resource["id"],
        target_resource_type=maintenance_run_history_target_resource_type)
    ```


    :param str availability_domain: A filter to return only resources that match the given availability domain exactly.
    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str maintenance_type: The maintenance type.
    :param str state: The state of the maintenance run history.
    :param str target_resource_id: The target resource ID.
    :param str target_resource_type: The type of the target resource.
    """
    ...
