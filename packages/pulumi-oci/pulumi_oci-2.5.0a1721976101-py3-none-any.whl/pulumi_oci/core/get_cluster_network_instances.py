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
    'GetClusterNetworkInstancesResult',
    'AwaitableGetClusterNetworkInstancesResult',
    'get_cluster_network_instances',
    'get_cluster_network_instances_output',
]

@pulumi.output_type
class GetClusterNetworkInstancesResult:
    """
    A collection of values returned by getClusterNetworkInstances.
    """
    def __init__(__self__, cluster_network_id=None, compartment_id=None, display_name=None, filters=None, id=None, instances=None):
        if cluster_network_id and not isinstance(cluster_network_id, str):
            raise TypeError("Expected argument 'cluster_network_id' to be a str")
        pulumi.set(__self__, "cluster_network_id", cluster_network_id)
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
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        pulumi.set(__self__, "instances", instances)

    @property
    @pulumi.getter(name="clusterNetworkId")
    def cluster_network_id(self) -> str:
        return pulumi.get(self, "cluster_network_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the instance.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetClusterNetworkInstancesFilterResult']]:
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
    def instances(self) -> Sequence['outputs.GetClusterNetworkInstancesInstanceResult']:
        """
        The list of instances.
        """
        return pulumi.get(self, "instances")


class AwaitableGetClusterNetworkInstancesResult(GetClusterNetworkInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterNetworkInstancesResult(
            cluster_network_id=self.cluster_network_id,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            instances=self.instances)


def get_cluster_network_instances(cluster_network_id: Optional[str] = None,
                                  compartment_id: Optional[str] = None,
                                  display_name: Optional[str] = None,
                                  filters: Optional[Sequence[pulumi.InputType['GetClusterNetworkInstancesFilterArgs']]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterNetworkInstancesResult:
    """
    This data source provides the list of Cluster Network Instances in Oracle Cloud Infrastructure Core service.

    Lists the instances in a [cluster network with instance pools](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/managingclusternetworks.htm).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cluster_network_instances = oci.Core.get_cluster_network_instances(cluster_network_id=test_cluster_network["id"],
        compartment_id=compartment_id,
        display_name=cluster_network_instance_display_name)
    ```


    :param str cluster_network_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    """
    __args__ = dict()
    __args__['clusterNetworkId'] = cluster_network_id
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getClusterNetworkInstances:getClusterNetworkInstances', __args__, opts=opts, typ=GetClusterNetworkInstancesResult).value

    return AwaitableGetClusterNetworkInstancesResult(
        cluster_network_id=pulumi.get(__ret__, 'cluster_network_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        instances=pulumi.get(__ret__, 'instances'))


@_utilities.lift_output_func(get_cluster_network_instances)
def get_cluster_network_instances_output(cluster_network_id: Optional[pulumi.Input[str]] = None,
                                         compartment_id: Optional[pulumi.Input[str]] = None,
                                         display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                         filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetClusterNetworkInstancesFilterArgs']]]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterNetworkInstancesResult]:
    """
    This data source provides the list of Cluster Network Instances in Oracle Cloud Infrastructure Core service.

    Lists the instances in a [cluster network with instance pools](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/managingclusternetworks.htm).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cluster_network_instances = oci.Core.get_cluster_network_instances(cluster_network_id=test_cluster_network["id"],
        compartment_id=compartment_id,
        display_name=cluster_network_instance_display_name)
    ```


    :param str cluster_network_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cluster network.
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    """
    ...
