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
    'GetManagedMySqlDatabaseResult',
    'AwaitableGetManagedMySqlDatabaseResult',
    'get_managed_my_sql_database',
    'get_managed_my_sql_database_output',
]

@pulumi.output_type
class GetManagedMySqlDatabaseResult:
    """
    A collection of values returned by getManagedMySqlDatabase.
    """
    def __init__(__self__, compartment_id=None, db_name=None, db_version=None, heat_wave_cluster_display_name=None, heat_wave_memory_size=None, heat_wave_node_shape=None, heat_wave_nodes=None, id=None, is_heat_wave_active=None, is_heat_wave_enabled=None, is_lakehouse_enabled=None, managed_my_sql_database_id=None, name=None, time_created=None, time_created_heat_wave=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if db_name and not isinstance(db_name, str):
            raise TypeError("Expected argument 'db_name' to be a str")
        pulumi.set(__self__, "db_name", db_name)
        if db_version and not isinstance(db_version, str):
            raise TypeError("Expected argument 'db_version' to be a str")
        pulumi.set(__self__, "db_version", db_version)
        if heat_wave_cluster_display_name and not isinstance(heat_wave_cluster_display_name, str):
            raise TypeError("Expected argument 'heat_wave_cluster_display_name' to be a str")
        pulumi.set(__self__, "heat_wave_cluster_display_name", heat_wave_cluster_display_name)
        if heat_wave_memory_size and not isinstance(heat_wave_memory_size, int):
            raise TypeError("Expected argument 'heat_wave_memory_size' to be a int")
        pulumi.set(__self__, "heat_wave_memory_size", heat_wave_memory_size)
        if heat_wave_node_shape and not isinstance(heat_wave_node_shape, str):
            raise TypeError("Expected argument 'heat_wave_node_shape' to be a str")
        pulumi.set(__self__, "heat_wave_node_shape", heat_wave_node_shape)
        if heat_wave_nodes and not isinstance(heat_wave_nodes, list):
            raise TypeError("Expected argument 'heat_wave_nodes' to be a list")
        pulumi.set(__self__, "heat_wave_nodes", heat_wave_nodes)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_heat_wave_active and not isinstance(is_heat_wave_active, bool):
            raise TypeError("Expected argument 'is_heat_wave_active' to be a bool")
        pulumi.set(__self__, "is_heat_wave_active", is_heat_wave_active)
        if is_heat_wave_enabled and not isinstance(is_heat_wave_enabled, bool):
            raise TypeError("Expected argument 'is_heat_wave_enabled' to be a bool")
        pulumi.set(__self__, "is_heat_wave_enabled", is_heat_wave_enabled)
        if is_lakehouse_enabled and not isinstance(is_lakehouse_enabled, bool):
            raise TypeError("Expected argument 'is_lakehouse_enabled' to be a bool")
        pulumi.set(__self__, "is_lakehouse_enabled", is_lakehouse_enabled)
        if managed_my_sql_database_id and not isinstance(managed_my_sql_database_id, str):
            raise TypeError("Expected argument 'managed_my_sql_database_id' to be a str")
        pulumi.set(__self__, "managed_my_sql_database_id", managed_my_sql_database_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_created_heat_wave and not isinstance(time_created_heat_wave, str):
            raise TypeError("Expected argument 'time_created_heat_wave' to be a str")
        pulumi.set(__self__, "time_created_heat_wave", time_created_heat_wave)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dbName")
    def db_name(self) -> str:
        """
        The name of the MySQL Database.
        """
        return pulumi.get(self, "db_name")

    @property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> str:
        """
        The version of the MySQL Database.
        """
        return pulumi.get(self, "db_version")

    @property
    @pulumi.getter(name="heatWaveClusterDisplayName")
    def heat_wave_cluster_display_name(self) -> str:
        """
        The name of the HeatWave cluster.
        """
        return pulumi.get(self, "heat_wave_cluster_display_name")

    @property
    @pulumi.getter(name="heatWaveMemorySize")
    def heat_wave_memory_size(self) -> int:
        """
        The total memory belonging to the HeatWave cluster in GBs.
        """
        return pulumi.get(self, "heat_wave_memory_size")

    @property
    @pulumi.getter(name="heatWaveNodeShape")
    def heat_wave_node_shape(self) -> str:
        """
        The shape of the nodes in the HeatWave cluster.
        """
        return pulumi.get(self, "heat_wave_node_shape")

    @property
    @pulumi.getter(name="heatWaveNodes")
    def heat_wave_nodes(self) -> Sequence['outputs.GetManagedMySqlDatabaseHeatWaveNodeResult']:
        """
        The information about individual HeatWave nodes in the cluster.
        """
        return pulumi.get(self, "heat_wave_nodes")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isHeatWaveActive")
    def is_heat_wave_active(self) -> bool:
        """
        Indicates whether the HeatWave cluster is active or not.
        """
        return pulumi.get(self, "is_heat_wave_active")

    @property
    @pulumi.getter(name="isHeatWaveEnabled")
    def is_heat_wave_enabled(self) -> bool:
        """
        Indicates whether HeatWave is enabled for the MySQL Database System or not.
        """
        return pulumi.get(self, "is_heat_wave_enabled")

    @property
    @pulumi.getter(name="isLakehouseEnabled")
    def is_lakehouse_enabled(self) -> bool:
        """
        Indicates whether HeatWave Lakehouse is enabled for the MySQL Database System or not.
        """
        return pulumi.get(self, "is_lakehouse_enabled")

    @property
    @pulumi.getter(name="managedMySqlDatabaseId")
    def managed_my_sql_database_id(self) -> str:
        return pulumi.get(self, "managed_my_sql_database_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Managed MySQL Database.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the HeatWave node was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeCreatedHeatWave")
    def time_created_heat_wave(self) -> str:
        """
        The date and time the Managed MySQL Database was created.
        """
        return pulumi.get(self, "time_created_heat_wave")


class AwaitableGetManagedMySqlDatabaseResult(GetManagedMySqlDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedMySqlDatabaseResult(
            compartment_id=self.compartment_id,
            db_name=self.db_name,
            db_version=self.db_version,
            heat_wave_cluster_display_name=self.heat_wave_cluster_display_name,
            heat_wave_memory_size=self.heat_wave_memory_size,
            heat_wave_node_shape=self.heat_wave_node_shape,
            heat_wave_nodes=self.heat_wave_nodes,
            id=self.id,
            is_heat_wave_active=self.is_heat_wave_active,
            is_heat_wave_enabled=self.is_heat_wave_enabled,
            is_lakehouse_enabled=self.is_lakehouse_enabled,
            managed_my_sql_database_id=self.managed_my_sql_database_id,
            name=self.name,
            time_created=self.time_created,
            time_created_heat_wave=self.time_created_heat_wave)


def get_managed_my_sql_database(managed_my_sql_database_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedMySqlDatabaseResult:
    """
    This data source provides details about a specific Managed My Sql Database resource in Oracle Cloud Infrastructure Database Management service.

    Retrieves General Information for given MySQL Instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_my_sql_database = oci.DatabaseManagement.get_managed_my_sql_database(managed_my_sql_database_id=test_managed_my_sql_database_oci_database_management_managed_my_sql_database["id"])
    ```


    :param str managed_my_sql_database_id: The OCID of ManagedMySqlDatabase.
    """
    __args__ = dict()
    __args__['managedMySqlDatabaseId'] = managed_my_sql_database_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getManagedMySqlDatabase:getManagedMySqlDatabase', __args__, opts=opts, typ=GetManagedMySqlDatabaseResult).value

    return AwaitableGetManagedMySqlDatabaseResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        db_name=pulumi.get(__ret__, 'db_name'),
        db_version=pulumi.get(__ret__, 'db_version'),
        heat_wave_cluster_display_name=pulumi.get(__ret__, 'heat_wave_cluster_display_name'),
        heat_wave_memory_size=pulumi.get(__ret__, 'heat_wave_memory_size'),
        heat_wave_node_shape=pulumi.get(__ret__, 'heat_wave_node_shape'),
        heat_wave_nodes=pulumi.get(__ret__, 'heat_wave_nodes'),
        id=pulumi.get(__ret__, 'id'),
        is_heat_wave_active=pulumi.get(__ret__, 'is_heat_wave_active'),
        is_heat_wave_enabled=pulumi.get(__ret__, 'is_heat_wave_enabled'),
        is_lakehouse_enabled=pulumi.get(__ret__, 'is_lakehouse_enabled'),
        managed_my_sql_database_id=pulumi.get(__ret__, 'managed_my_sql_database_id'),
        name=pulumi.get(__ret__, 'name'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_created_heat_wave=pulumi.get(__ret__, 'time_created_heat_wave'))


@_utilities.lift_output_func(get_managed_my_sql_database)
def get_managed_my_sql_database_output(managed_my_sql_database_id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedMySqlDatabaseResult]:
    """
    This data source provides details about a specific Managed My Sql Database resource in Oracle Cloud Infrastructure Database Management service.

    Retrieves General Information for given MySQL Instance.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_managed_my_sql_database = oci.DatabaseManagement.get_managed_my_sql_database(managed_my_sql_database_id=test_managed_my_sql_database_oci_database_management_managed_my_sql_database["id"])
    ```


    :param str managed_my_sql_database_id: The OCID of ManagedMySqlDatabase.
    """
    ...
