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
    'GetCloudAutonomousVmClusterResourceUsageResult',
    'AwaitableGetCloudAutonomousVmClusterResourceUsageResult',
    'get_cloud_autonomous_vm_cluster_resource_usage',
    'get_cloud_autonomous_vm_cluster_resource_usage_output',
]

@pulumi.output_type
class GetCloudAutonomousVmClusterResourceUsageResult:
    """
    A collection of values returned by getCloudAutonomousVmClusterResourceUsage.
    """
    def __init__(__self__, autonomous_data_storage_size_in_tbs=None, autonomous_vm_resource_usages=None, available_autonomous_data_storage_size_in_tbs=None, available_cpus=None, cloud_autonomous_vm_cluster_id=None, db_node_storage_size_in_gbs=None, display_name=None, exadata_storage_in_tbs=None, id=None, memory_per_oracle_compute_unit_in_gbs=None, memory_size_in_gbs=None, non_provisionable_autonomous_container_databases=None, provisionable_autonomous_container_databases=None, provisioned_autonomous_container_databases=None, provisioned_cpus=None, reclaimable_cpus=None, reserved_cpus=None, total_container_databases=None, total_cpus=None, used_autonomous_data_storage_size_in_tbs=None, used_cpus=None):
        if autonomous_data_storage_size_in_tbs and not isinstance(autonomous_data_storage_size_in_tbs, float):
            raise TypeError("Expected argument 'autonomous_data_storage_size_in_tbs' to be a float")
        pulumi.set(__self__, "autonomous_data_storage_size_in_tbs", autonomous_data_storage_size_in_tbs)
        if autonomous_vm_resource_usages and not isinstance(autonomous_vm_resource_usages, list):
            raise TypeError("Expected argument 'autonomous_vm_resource_usages' to be a list")
        pulumi.set(__self__, "autonomous_vm_resource_usages", autonomous_vm_resource_usages)
        if available_autonomous_data_storage_size_in_tbs and not isinstance(available_autonomous_data_storage_size_in_tbs, float):
            raise TypeError("Expected argument 'available_autonomous_data_storage_size_in_tbs' to be a float")
        pulumi.set(__self__, "available_autonomous_data_storage_size_in_tbs", available_autonomous_data_storage_size_in_tbs)
        if available_cpus and not isinstance(available_cpus, float):
            raise TypeError("Expected argument 'available_cpus' to be a float")
        pulumi.set(__self__, "available_cpus", available_cpus)
        if cloud_autonomous_vm_cluster_id and not isinstance(cloud_autonomous_vm_cluster_id, str):
            raise TypeError("Expected argument 'cloud_autonomous_vm_cluster_id' to be a str")
        pulumi.set(__self__, "cloud_autonomous_vm_cluster_id", cloud_autonomous_vm_cluster_id)
        if db_node_storage_size_in_gbs and not isinstance(db_node_storage_size_in_gbs, int):
            raise TypeError("Expected argument 'db_node_storage_size_in_gbs' to be a int")
        pulumi.set(__self__, "db_node_storage_size_in_gbs", db_node_storage_size_in_gbs)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if exadata_storage_in_tbs and not isinstance(exadata_storage_in_tbs, float):
            raise TypeError("Expected argument 'exadata_storage_in_tbs' to be a float")
        pulumi.set(__self__, "exadata_storage_in_tbs", exadata_storage_in_tbs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if memory_per_oracle_compute_unit_in_gbs and not isinstance(memory_per_oracle_compute_unit_in_gbs, int):
            raise TypeError("Expected argument 'memory_per_oracle_compute_unit_in_gbs' to be a int")
        pulumi.set(__self__, "memory_per_oracle_compute_unit_in_gbs", memory_per_oracle_compute_unit_in_gbs)
        if memory_size_in_gbs and not isinstance(memory_size_in_gbs, int):
            raise TypeError("Expected argument 'memory_size_in_gbs' to be a int")
        pulumi.set(__self__, "memory_size_in_gbs", memory_size_in_gbs)
        if non_provisionable_autonomous_container_databases and not isinstance(non_provisionable_autonomous_container_databases, int):
            raise TypeError("Expected argument 'non_provisionable_autonomous_container_databases' to be a int")
        pulumi.set(__self__, "non_provisionable_autonomous_container_databases", non_provisionable_autonomous_container_databases)
        if provisionable_autonomous_container_databases and not isinstance(provisionable_autonomous_container_databases, int):
            raise TypeError("Expected argument 'provisionable_autonomous_container_databases' to be a int")
        pulumi.set(__self__, "provisionable_autonomous_container_databases", provisionable_autonomous_container_databases)
        if provisioned_autonomous_container_databases and not isinstance(provisioned_autonomous_container_databases, int):
            raise TypeError("Expected argument 'provisioned_autonomous_container_databases' to be a int")
        pulumi.set(__self__, "provisioned_autonomous_container_databases", provisioned_autonomous_container_databases)
        if provisioned_cpus and not isinstance(provisioned_cpus, float):
            raise TypeError("Expected argument 'provisioned_cpus' to be a float")
        pulumi.set(__self__, "provisioned_cpus", provisioned_cpus)
        if reclaimable_cpus and not isinstance(reclaimable_cpus, float):
            raise TypeError("Expected argument 'reclaimable_cpus' to be a float")
        pulumi.set(__self__, "reclaimable_cpus", reclaimable_cpus)
        if reserved_cpus and not isinstance(reserved_cpus, float):
            raise TypeError("Expected argument 'reserved_cpus' to be a float")
        pulumi.set(__self__, "reserved_cpus", reserved_cpus)
        if total_container_databases and not isinstance(total_container_databases, int):
            raise TypeError("Expected argument 'total_container_databases' to be a int")
        pulumi.set(__self__, "total_container_databases", total_container_databases)
        if total_cpus and not isinstance(total_cpus, float):
            raise TypeError("Expected argument 'total_cpus' to be a float")
        pulumi.set(__self__, "total_cpus", total_cpus)
        if used_autonomous_data_storage_size_in_tbs and not isinstance(used_autonomous_data_storage_size_in_tbs, float):
            raise TypeError("Expected argument 'used_autonomous_data_storage_size_in_tbs' to be a float")
        pulumi.set(__self__, "used_autonomous_data_storage_size_in_tbs", used_autonomous_data_storage_size_in_tbs)
        if used_cpus and not isinstance(used_cpus, float):
            raise TypeError("Expected argument 'used_cpus' to be a float")
        pulumi.set(__self__, "used_cpus", used_cpus)

    @property
    @pulumi.getter(name="autonomousDataStorageSizeInTbs")
    def autonomous_data_storage_size_in_tbs(self) -> float:
        """
        The data disk group size allocated for Autonomous Databases, in TBs.
        """
        return pulumi.get(self, "autonomous_data_storage_size_in_tbs")

    @property
    @pulumi.getter(name="autonomousVmResourceUsages")
    def autonomous_vm_resource_usages(self) -> Sequence['outputs.GetCloudAutonomousVmClusterResourceUsageAutonomousVmResourceUsageResult']:
        """
        List of Autonomous VM resource usages.
        """
        return pulumi.get(self, "autonomous_vm_resource_usages")

    @property
    @pulumi.getter(name="availableAutonomousDataStorageSizeInTbs")
    def available_autonomous_data_storage_size_in_tbs(self) -> float:
        """
        The data disk group size available for Autonomous Databases, in TBs.
        """
        return pulumi.get(self, "available_autonomous_data_storage_size_in_tbs")

    @property
    @pulumi.getter(name="availableCpus")
    def available_cpus(self) -> float:
        """
        The number of CPU cores available.
        """
        return pulumi.get(self, "available_cpus")

    @property
    @pulumi.getter(name="cloudAutonomousVmClusterId")
    def cloud_autonomous_vm_cluster_id(self) -> str:
        return pulumi.get(self, "cloud_autonomous_vm_cluster_id")

    @property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> int:
        """
        The local node storage allocated in GBs.
        """
        return pulumi.get(self, "db_node_storage_size_in_gbs")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-friendly name for the Autonomous VM cluster. The name does not need to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="exadataStorageInTbs")
    def exadata_storage_in_tbs(self) -> float:
        """
        Total exadata storage allocated for the Autonomous VM Cluster. DATA + RECOVERY + SPARSE + any overhead in TBs.
        """
        return pulumi.get(self, "exadata_storage_in_tbs")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memoryPerOracleComputeUnitInGbs")
    def memory_per_oracle_compute_unit_in_gbs(self) -> int:
        """
        The amount of memory (in GBs) to be enabled per each CPU core.
        """
        return pulumi.get(self, "memory_per_oracle_compute_unit_in_gbs")

    @property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> int:
        """
        The memory allocated in GBs.
        """
        return pulumi.get(self, "memory_size_in_gbs")

    @property
    @pulumi.getter(name="nonProvisionableAutonomousContainerDatabases")
    def non_provisionable_autonomous_container_databases(self) -> int:
        """
        The number of non-provisionable Autonomous Container Databases in an Autonomous VM Cluster.
        """
        return pulumi.get(self, "non_provisionable_autonomous_container_databases")

    @property
    @pulumi.getter(name="provisionableAutonomousContainerDatabases")
    def provisionable_autonomous_container_databases(self) -> int:
        """
        The number of provisionable Autonomous Container Databases in an Autonomous VM Cluster.
        """
        return pulumi.get(self, "provisionable_autonomous_container_databases")

    @property
    @pulumi.getter(name="provisionedAutonomousContainerDatabases")
    def provisioned_autonomous_container_databases(self) -> int:
        """
        The number of provisioned Autonomous Container Databases in an Autonomous VM Cluster.
        """
        return pulumi.get(self, "provisioned_autonomous_container_databases")

    @property
    @pulumi.getter(name="provisionedCpus")
    def provisioned_cpus(self) -> float:
        """
        The number of CPUs provisioned in an Autonomous VM Cluster.
        """
        return pulumi.get(self, "provisioned_cpus")

    @property
    @pulumi.getter(name="reclaimableCpus")
    def reclaimable_cpus(self) -> float:
        """
        CPU cores that continue to be included in the count of OCPUs available to the Autonomous Container Database even after one of its Autonomous Database is terminated or scaled down. You can release them to the available OCPUs at its parent AVMC level by restarting the Autonomous Container Database.
        """
        return pulumi.get(self, "reclaimable_cpus")

    @property
    @pulumi.getter(name="reservedCpus")
    def reserved_cpus(self) -> float:
        """
        The number of CPUs reserved in an Autonomous VM Cluster.
        """
        return pulumi.get(self, "reserved_cpus")

    @property
    @pulumi.getter(name="totalContainerDatabases")
    def total_container_databases(self) -> int:
        """
        The total number of Autonomous Container Databases that can be created.
        """
        return pulumi.get(self, "total_container_databases")

    @property
    @pulumi.getter(name="totalCpus")
    def total_cpus(self) -> float:
        """
        The number of CPU cores enabled on the Cloud Autonomous VM cluster.
        """
        return pulumi.get(self, "total_cpus")

    @property
    @pulumi.getter(name="usedAutonomousDataStorageSizeInTbs")
    def used_autonomous_data_storage_size_in_tbs(self) -> float:
        """
        The data disk group size used for Autonomous Databases, in TBs.
        """
        return pulumi.get(self, "used_autonomous_data_storage_size_in_tbs")

    @property
    @pulumi.getter(name="usedCpus")
    def used_cpus(self) -> float:
        """
        The number of CPU cores alloted to the Autonomous Container Databases in an Cloud Autonomous VM cluster.
        """
        return pulumi.get(self, "used_cpus")


class AwaitableGetCloudAutonomousVmClusterResourceUsageResult(GetCloudAutonomousVmClusterResourceUsageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudAutonomousVmClusterResourceUsageResult(
            autonomous_data_storage_size_in_tbs=self.autonomous_data_storage_size_in_tbs,
            autonomous_vm_resource_usages=self.autonomous_vm_resource_usages,
            available_autonomous_data_storage_size_in_tbs=self.available_autonomous_data_storage_size_in_tbs,
            available_cpus=self.available_cpus,
            cloud_autonomous_vm_cluster_id=self.cloud_autonomous_vm_cluster_id,
            db_node_storage_size_in_gbs=self.db_node_storage_size_in_gbs,
            display_name=self.display_name,
            exadata_storage_in_tbs=self.exadata_storage_in_tbs,
            id=self.id,
            memory_per_oracle_compute_unit_in_gbs=self.memory_per_oracle_compute_unit_in_gbs,
            memory_size_in_gbs=self.memory_size_in_gbs,
            non_provisionable_autonomous_container_databases=self.non_provisionable_autonomous_container_databases,
            provisionable_autonomous_container_databases=self.provisionable_autonomous_container_databases,
            provisioned_autonomous_container_databases=self.provisioned_autonomous_container_databases,
            provisioned_cpus=self.provisioned_cpus,
            reclaimable_cpus=self.reclaimable_cpus,
            reserved_cpus=self.reserved_cpus,
            total_container_databases=self.total_container_databases,
            total_cpus=self.total_cpus,
            used_autonomous_data_storage_size_in_tbs=self.used_autonomous_data_storage_size_in_tbs,
            used_cpus=self.used_cpus)


def get_cloud_autonomous_vm_cluster_resource_usage(cloud_autonomous_vm_cluster_id: Optional[str] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudAutonomousVmClusterResourceUsageResult:
    """
    This data source provides details about a specific Cloud Autonomous Vm Cluster Resource Usage resource in Oracle Cloud Infrastructure Database service.

    Get the resource usage details for the specified Cloud Autonomous Exadata VM cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cloud_autonomous_vm_cluster_resource_usage = oci.Database.get_cloud_autonomous_vm_cluster_resource_usage(cloud_autonomous_vm_cluster_id=test_cloud_autonomous_vm_cluster["id"])
    ```


    :param str cloud_autonomous_vm_cluster_id: The Cloud VM cluster [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    __args__ = dict()
    __args__['cloudAutonomousVmClusterId'] = cloud_autonomous_vm_cluster_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getCloudAutonomousVmClusterResourceUsage:getCloudAutonomousVmClusterResourceUsage', __args__, opts=opts, typ=GetCloudAutonomousVmClusterResourceUsageResult).value

    return AwaitableGetCloudAutonomousVmClusterResourceUsageResult(
        autonomous_data_storage_size_in_tbs=pulumi.get(__ret__, 'autonomous_data_storage_size_in_tbs'),
        autonomous_vm_resource_usages=pulumi.get(__ret__, 'autonomous_vm_resource_usages'),
        available_autonomous_data_storage_size_in_tbs=pulumi.get(__ret__, 'available_autonomous_data_storage_size_in_tbs'),
        available_cpus=pulumi.get(__ret__, 'available_cpus'),
        cloud_autonomous_vm_cluster_id=pulumi.get(__ret__, 'cloud_autonomous_vm_cluster_id'),
        db_node_storage_size_in_gbs=pulumi.get(__ret__, 'db_node_storage_size_in_gbs'),
        display_name=pulumi.get(__ret__, 'display_name'),
        exadata_storage_in_tbs=pulumi.get(__ret__, 'exadata_storage_in_tbs'),
        id=pulumi.get(__ret__, 'id'),
        memory_per_oracle_compute_unit_in_gbs=pulumi.get(__ret__, 'memory_per_oracle_compute_unit_in_gbs'),
        memory_size_in_gbs=pulumi.get(__ret__, 'memory_size_in_gbs'),
        non_provisionable_autonomous_container_databases=pulumi.get(__ret__, 'non_provisionable_autonomous_container_databases'),
        provisionable_autonomous_container_databases=pulumi.get(__ret__, 'provisionable_autonomous_container_databases'),
        provisioned_autonomous_container_databases=pulumi.get(__ret__, 'provisioned_autonomous_container_databases'),
        provisioned_cpus=pulumi.get(__ret__, 'provisioned_cpus'),
        reclaimable_cpus=pulumi.get(__ret__, 'reclaimable_cpus'),
        reserved_cpus=pulumi.get(__ret__, 'reserved_cpus'),
        total_container_databases=pulumi.get(__ret__, 'total_container_databases'),
        total_cpus=pulumi.get(__ret__, 'total_cpus'),
        used_autonomous_data_storage_size_in_tbs=pulumi.get(__ret__, 'used_autonomous_data_storage_size_in_tbs'),
        used_cpus=pulumi.get(__ret__, 'used_cpus'))


@_utilities.lift_output_func(get_cloud_autonomous_vm_cluster_resource_usage)
def get_cloud_autonomous_vm_cluster_resource_usage_output(cloud_autonomous_vm_cluster_id: Optional[pulumi.Input[str]] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudAutonomousVmClusterResourceUsageResult]:
    """
    This data source provides details about a specific Cloud Autonomous Vm Cluster Resource Usage resource in Oracle Cloud Infrastructure Database service.

    Get the resource usage details for the specified Cloud Autonomous Exadata VM cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cloud_autonomous_vm_cluster_resource_usage = oci.Database.get_cloud_autonomous_vm_cluster_resource_usage(cloud_autonomous_vm_cluster_id=test_cloud_autonomous_vm_cluster["id"])
    ```


    :param str cloud_autonomous_vm_cluster_id: The Cloud VM cluster [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    ...
