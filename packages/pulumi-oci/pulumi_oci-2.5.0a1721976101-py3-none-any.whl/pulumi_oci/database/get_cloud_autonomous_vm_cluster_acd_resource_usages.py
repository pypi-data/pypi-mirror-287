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
    'GetCloudAutonomousVmClusterAcdResourceUsagesResult',
    'AwaitableGetCloudAutonomousVmClusterAcdResourceUsagesResult',
    'get_cloud_autonomous_vm_cluster_acd_resource_usages',
    'get_cloud_autonomous_vm_cluster_acd_resource_usages_output',
]

@pulumi.output_type
class GetCloudAutonomousVmClusterAcdResourceUsagesResult:
    """
    A collection of values returned by getCloudAutonomousVmClusterAcdResourceUsages.
    """
    def __init__(__self__, autonomous_container_database_resource_usages=None, cloud_autonomous_vm_cluster_id=None, compartment_id=None, filters=None, id=None):
        if autonomous_container_database_resource_usages and not isinstance(autonomous_container_database_resource_usages, list):
            raise TypeError("Expected argument 'autonomous_container_database_resource_usages' to be a list")
        pulumi.set(__self__, "autonomous_container_database_resource_usages", autonomous_container_database_resource_usages)
        if cloud_autonomous_vm_cluster_id and not isinstance(cloud_autonomous_vm_cluster_id, str):
            raise TypeError("Expected argument 'cloud_autonomous_vm_cluster_id' to be a str")
        pulumi.set(__self__, "cloud_autonomous_vm_cluster_id", cloud_autonomous_vm_cluster_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="autonomousContainerDatabaseResourceUsages")
    def autonomous_container_database_resource_usages(self) -> Sequence['outputs.GetCloudAutonomousVmClusterAcdResourceUsagesAutonomousContainerDatabaseResourceUsageResult']:
        """
        The list of autonomous_container_database_resource_usages.
        """
        return pulumi.get(self, "autonomous_container_database_resource_usages")

    @property
    @pulumi.getter(name="cloudAutonomousVmClusterId")
    def cloud_autonomous_vm_cluster_id(self) -> str:
        return pulumi.get(self, "cloud_autonomous_vm_cluster_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetCloudAutonomousVmClusterAcdResourceUsagesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetCloudAutonomousVmClusterAcdResourceUsagesResult(GetCloudAutonomousVmClusterAcdResourceUsagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudAutonomousVmClusterAcdResourceUsagesResult(
            autonomous_container_database_resource_usages=self.autonomous_container_database_resource_usages,
            cloud_autonomous_vm_cluster_id=self.cloud_autonomous_vm_cluster_id,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id)


def get_cloud_autonomous_vm_cluster_acd_resource_usages(cloud_autonomous_vm_cluster_id: Optional[str] = None,
                                                        compartment_id: Optional[str] = None,
                                                        filters: Optional[Sequence[pulumi.InputType['GetCloudAutonomousVmClusterAcdResourceUsagesFilterArgs']]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudAutonomousVmClusterAcdResourceUsagesResult:
    """
    This data source provides the list of Cloud Autonomous Vm Cluster Acd Resource Usages in Oracle Cloud Infrastructure Database service.

    Gets the list of resource usage details for all the Cloud Autonomous Container Database
    in the specified Cloud Autonomous Exadata VM cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cloud_autonomous_vm_cluster_acd_resource_usages = oci.Database.get_cloud_autonomous_vm_cluster_acd_resource_usages(cloud_autonomous_vm_cluster_id=test_cloud_autonomous_vm_cluster["id"],
        compartment_id=compartment_id)
    ```


    :param str cloud_autonomous_vm_cluster_id: The Cloud VM cluster [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    __args__ = dict()
    __args__['cloudAutonomousVmClusterId'] = cloud_autonomous_vm_cluster_id
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getCloudAutonomousVmClusterAcdResourceUsages:getCloudAutonomousVmClusterAcdResourceUsages', __args__, opts=opts, typ=GetCloudAutonomousVmClusterAcdResourceUsagesResult).value

    return AwaitableGetCloudAutonomousVmClusterAcdResourceUsagesResult(
        autonomous_container_database_resource_usages=pulumi.get(__ret__, 'autonomous_container_database_resource_usages'),
        cloud_autonomous_vm_cluster_id=pulumi.get(__ret__, 'cloud_autonomous_vm_cluster_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_cloud_autonomous_vm_cluster_acd_resource_usages)
def get_cloud_autonomous_vm_cluster_acd_resource_usages_output(cloud_autonomous_vm_cluster_id: Optional[pulumi.Input[str]] = None,
                                                               compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                               filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetCloudAutonomousVmClusterAcdResourceUsagesFilterArgs']]]]] = None,
                                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudAutonomousVmClusterAcdResourceUsagesResult]:
    """
    This data source provides the list of Cloud Autonomous Vm Cluster Acd Resource Usages in Oracle Cloud Infrastructure Database service.

    Gets the list of resource usage details for all the Cloud Autonomous Container Database
    in the specified Cloud Autonomous Exadata VM cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cloud_autonomous_vm_cluster_acd_resource_usages = oci.Database.get_cloud_autonomous_vm_cluster_acd_resource_usages(cloud_autonomous_vm_cluster_id=test_cloud_autonomous_vm_cluster["id"],
        compartment_id=compartment_id)
    ```


    :param str cloud_autonomous_vm_cluster_id: The Cloud VM cluster [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str compartment_id: The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    """
    ...
