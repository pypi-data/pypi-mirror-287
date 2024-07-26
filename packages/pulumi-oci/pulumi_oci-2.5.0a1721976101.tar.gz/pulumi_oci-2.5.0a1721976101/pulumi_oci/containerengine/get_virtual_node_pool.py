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
    'GetVirtualNodePoolResult',
    'AwaitableGetVirtualNodePoolResult',
    'get_virtual_node_pool',
    'get_virtual_node_pool_output',
]

@pulumi.output_type
class GetVirtualNodePoolResult:
    """
    A collection of values returned by getVirtualNodePool.
    """
    def __init__(__self__, cluster_id=None, compartment_id=None, defined_tags=None, display_name=None, freeform_tags=None, id=None, initial_virtual_node_labels=None, kubernetes_version=None, lifecycle_details=None, nsg_ids=None, placement_configurations=None, pod_configurations=None, size=None, state=None, system_tags=None, taints=None, time_created=None, time_updated=None, virtual_node_pool_id=None, virtual_node_tags=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if initial_virtual_node_labels and not isinstance(initial_virtual_node_labels, list):
            raise TypeError("Expected argument 'initial_virtual_node_labels' to be a list")
        pulumi.set(__self__, "initial_virtual_node_labels", initial_virtual_node_labels)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if nsg_ids and not isinstance(nsg_ids, list):
            raise TypeError("Expected argument 'nsg_ids' to be a list")
        pulumi.set(__self__, "nsg_ids", nsg_ids)
        if placement_configurations and not isinstance(placement_configurations, list):
            raise TypeError("Expected argument 'placement_configurations' to be a list")
        pulumi.set(__self__, "placement_configurations", placement_configurations)
        if pod_configurations and not isinstance(pod_configurations, list):
            raise TypeError("Expected argument 'pod_configurations' to be a list")
        pulumi.set(__self__, "pod_configurations", pod_configurations)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if taints and not isinstance(taints, list):
            raise TypeError("Expected argument 'taints' to be a list")
        pulumi.set(__self__, "taints", taints)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if virtual_node_pool_id and not isinstance(virtual_node_pool_id, str):
            raise TypeError("Expected argument 'virtual_node_pool_id' to be a str")
        pulumi.set(__self__, "virtual_node_pool_id", virtual_node_pool_id)
        if virtual_node_tags and not isinstance(virtual_node_tags, list):
            raise TypeError("Expected argument 'virtual_node_tags' to be a list")
        pulumi.set(__self__, "virtual_node_tags", virtual_node_tags)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The cluster the virtual node pool is associated with. A virtual node pool can only be associated with one cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment of the virtual node pool.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name of the virtual node pool. This is a non-unique value.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the virtual node pool.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="initialVirtualNodeLabels")
    def initial_virtual_node_labels(self) -> Sequence['outputs.GetVirtualNodePoolInitialVirtualNodeLabelResult']:
        """
        Initial labels that will be added to the Kubernetes Virtual Node object when it registers. This is the same as virtualNodePool resources.
        """
        return pulumi.get(self, "initial_virtual_node_labels")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> str:
        """
        The version of Kubernetes running on the nodes in the node pool.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Details about the state of the Virtual Node Pool.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="nsgIds")
    def nsg_ids(self) -> Sequence[str]:
        """
        List of network security group IDs applied to the Pod VNIC.
        """
        return pulumi.get(self, "nsg_ids")

    @property
    @pulumi.getter(name="placementConfigurations")
    def placement_configurations(self) -> Sequence['outputs.GetVirtualNodePoolPlacementConfigurationResult']:
        """
        The list of placement configurations which determines where Virtual Nodes will be provisioned across as it relates to the subnet and availability domains. The size attribute determines how many we evenly spread across these placement configurations
        """
        return pulumi.get(self, "placement_configurations")

    @property
    @pulumi.getter(name="podConfigurations")
    def pod_configurations(self) -> Sequence['outputs.GetVirtualNodePoolPodConfigurationResult']:
        """
        The pod configuration for pods run on virtual nodes of this virtual node pool.
        """
        return pulumi.get(self, "pod_configurations")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The number of Virtual Nodes that should be in the Virtual Node Pool. The placement configurations determine where these virtual nodes are placed.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the Virtual Node Pool.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter
    def taints(self) -> Sequence['outputs.GetVirtualNodePoolTaintResult']:
        """
        A taint is a collection of <key, value, effect>. These taints will be applied to the Virtual Nodes of this Virtual Node Pool for Kubernetes scheduling.
        """
        return pulumi.get(self, "taints")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the virtual node pool was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the virtual node pool was updated.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="virtualNodePoolId")
    def virtual_node_pool_id(self) -> str:
        return pulumi.get(self, "virtual_node_pool_id")

    @property
    @pulumi.getter(name="virtualNodeTags")
    def virtual_node_tags(self) -> Sequence['outputs.GetVirtualNodePoolVirtualNodeTagResult']:
        """
        The tags associated to the virtual nodes in this virtual node pool.
        """
        return pulumi.get(self, "virtual_node_tags")


class AwaitableGetVirtualNodePoolResult(GetVirtualNodePoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNodePoolResult(
            cluster_id=self.cluster_id,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            initial_virtual_node_labels=self.initial_virtual_node_labels,
            kubernetes_version=self.kubernetes_version,
            lifecycle_details=self.lifecycle_details,
            nsg_ids=self.nsg_ids,
            placement_configurations=self.placement_configurations,
            pod_configurations=self.pod_configurations,
            size=self.size,
            state=self.state,
            system_tags=self.system_tags,
            taints=self.taints,
            time_created=self.time_created,
            time_updated=self.time_updated,
            virtual_node_pool_id=self.virtual_node_pool_id,
            virtual_node_tags=self.virtual_node_tags)


def get_virtual_node_pool(virtual_node_pool_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNodePoolResult:
    """
    This data source provides details about a specific Virtual Node Pool resource in Oracle Cloud Infrastructure Container Engine service.

    Get the details of a virtual node pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_virtual_node_pool = oci.ContainerEngine.get_virtual_node_pool(virtual_node_pool_id=test_virtual_node_pool_oci_containerengine_virtual_node_pool["id"])
    ```


    :param str virtual_node_pool_id: The OCID of the virtual node pool.
    """
    __args__ = dict()
    __args__['virtualNodePoolId'] = virtual_node_pool_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ContainerEngine/getVirtualNodePool:getVirtualNodePool', __args__, opts=opts, typ=GetVirtualNodePoolResult).value

    return AwaitableGetVirtualNodePoolResult(
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        initial_virtual_node_labels=pulumi.get(__ret__, 'initial_virtual_node_labels'),
        kubernetes_version=pulumi.get(__ret__, 'kubernetes_version'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        nsg_ids=pulumi.get(__ret__, 'nsg_ids'),
        placement_configurations=pulumi.get(__ret__, 'placement_configurations'),
        pod_configurations=pulumi.get(__ret__, 'pod_configurations'),
        size=pulumi.get(__ret__, 'size'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        taints=pulumi.get(__ret__, 'taints'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        virtual_node_pool_id=pulumi.get(__ret__, 'virtual_node_pool_id'),
        virtual_node_tags=pulumi.get(__ret__, 'virtual_node_tags'))


@_utilities.lift_output_func(get_virtual_node_pool)
def get_virtual_node_pool_output(virtual_node_pool_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNodePoolResult]:
    """
    This data source provides details about a specific Virtual Node Pool resource in Oracle Cloud Infrastructure Container Engine service.

    Get the details of a virtual node pool.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_virtual_node_pool = oci.ContainerEngine.get_virtual_node_pool(virtual_node_pool_id=test_virtual_node_pool_oci_containerengine_virtual_node_pool["id"])
    ```


    :param str virtual_node_pool_id: The OCID of the virtual node pool.
    """
    ...
