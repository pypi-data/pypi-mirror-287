# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetExternalClusterInstanceResult',
    'AwaitableGetExternalClusterInstanceResult',
    'get_external_cluster_instance',
    'get_external_cluster_instance_output',
]

@pulumi.output_type
class GetExternalClusterInstanceResult:
    """
    A collection of values returned by getExternalClusterInstance.
    """
    def __init__(__self__, adr_home_directory=None, compartment_id=None, component_name=None, crs_base_directory=None, defined_tags=None, display_name=None, external_cluster_id=None, external_cluster_instance_id=None, external_connector_id=None, external_db_node_id=None, external_db_system_id=None, freeform_tags=None, host_name=None, id=None, lifecycle_details=None, node_role=None, state=None, system_tags=None, time_created=None, time_updated=None):
        if adr_home_directory and not isinstance(adr_home_directory, str):
            raise TypeError("Expected argument 'adr_home_directory' to be a str")
        pulumi.set(__self__, "adr_home_directory", adr_home_directory)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if component_name and not isinstance(component_name, str):
            raise TypeError("Expected argument 'component_name' to be a str")
        pulumi.set(__self__, "component_name", component_name)
        if crs_base_directory and not isinstance(crs_base_directory, str):
            raise TypeError("Expected argument 'crs_base_directory' to be a str")
        pulumi.set(__self__, "crs_base_directory", crs_base_directory)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_cluster_id and not isinstance(external_cluster_id, str):
            raise TypeError("Expected argument 'external_cluster_id' to be a str")
        pulumi.set(__self__, "external_cluster_id", external_cluster_id)
        if external_cluster_instance_id and not isinstance(external_cluster_instance_id, str):
            raise TypeError("Expected argument 'external_cluster_instance_id' to be a str")
        pulumi.set(__self__, "external_cluster_instance_id", external_cluster_instance_id)
        if external_connector_id and not isinstance(external_connector_id, str):
            raise TypeError("Expected argument 'external_connector_id' to be a str")
        pulumi.set(__self__, "external_connector_id", external_connector_id)
        if external_db_node_id and not isinstance(external_db_node_id, str):
            raise TypeError("Expected argument 'external_db_node_id' to be a str")
        pulumi.set(__self__, "external_db_node_id", external_db_node_id)
        if external_db_system_id and not isinstance(external_db_system_id, str):
            raise TypeError("Expected argument 'external_db_system_id' to be a str")
        pulumi.set(__self__, "external_db_system_id", external_db_system_id)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if host_name and not isinstance(host_name, str):
            raise TypeError("Expected argument 'host_name' to be a str")
        pulumi.set(__self__, "host_name", host_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if node_role and not isinstance(node_role, str):
            raise TypeError("Expected argument 'node_role' to be a str")
        pulumi.set(__self__, "node_role", node_role)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="adrHomeDirectory")
    def adr_home_directory(self) -> str:
        """
        The Automatic Diagnostic Repository (ADR) home directory for the cluster instance.
        """
        return pulumi.get(self, "adr_home_directory")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="componentName")
    def component_name(self) -> str:
        """
        The name of the external cluster instance.
        """
        return pulumi.get(self, "component_name")

    @property
    @pulumi.getter(name="crsBaseDirectory")
    def crs_base_directory(self) -> str:
        """
        The Oracle base location of Cluster Ready Services (CRS).
        """
        return pulumi.get(self, "crs_base_directory")

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
        The user-friendly name for the cluster instance. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalClusterId")
    def external_cluster_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster that the cluster instance belongs to.
        """
        return pulumi.get(self, "external_cluster_id")

    @property
    @pulumi.getter(name="externalClusterInstanceId")
    def external_cluster_instance_id(self) -> str:
        return pulumi.get(self, "external_cluster_instance_id")

    @property
    @pulumi.getter(name="externalConnectorId")
    def external_connector_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external connector.
        """
        return pulumi.get(self, "external_connector_id")

    @property
    @pulumi.getter(name="externalDbNodeId")
    def external_db_node_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB node.
        """
        return pulumi.get(self, "external_db_node_id")

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the cluster instance is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        The name of the host on which the cluster instance is running.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Additional information about the current lifecycle state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="nodeRole")
    def node_role(self) -> str:
        """
        The role of the cluster node.
        """
        return pulumi.get(self, "node_role")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current lifecycle state of the external cluster instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the external cluster instance was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time the external cluster instance was last updated.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetExternalClusterInstanceResult(GetExternalClusterInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalClusterInstanceResult(
            adr_home_directory=self.adr_home_directory,
            compartment_id=self.compartment_id,
            component_name=self.component_name,
            crs_base_directory=self.crs_base_directory,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            external_cluster_id=self.external_cluster_id,
            external_cluster_instance_id=self.external_cluster_instance_id,
            external_connector_id=self.external_connector_id,
            external_db_node_id=self.external_db_node_id,
            external_db_system_id=self.external_db_system_id,
            freeform_tags=self.freeform_tags,
            host_name=self.host_name,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            node_role=self.node_role,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_external_cluster_instance(external_cluster_instance_id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalClusterInstanceResult:
    """
    This data source provides details about a specific External Cluster Instance resource in Oracle Cloud Infrastructure Database Management service.

    Gets the details for the external cluster instance specified by `externalClusterInstanceId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_cluster_instance = oci.DatabaseManagement.get_external_cluster_instance(external_cluster_instance_id=test_external_cluster_instance_oci_database_management_external_cluster_instance["id"])
    ```


    :param str external_cluster_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
    """
    __args__ = dict()
    __args__['externalClusterInstanceId'] = external_cluster_instance_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getExternalClusterInstance:getExternalClusterInstance', __args__, opts=opts, typ=GetExternalClusterInstanceResult).value

    return AwaitableGetExternalClusterInstanceResult(
        adr_home_directory=pulumi.get(__ret__, 'adr_home_directory'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        component_name=pulumi.get(__ret__, 'component_name'),
        crs_base_directory=pulumi.get(__ret__, 'crs_base_directory'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_cluster_id=pulumi.get(__ret__, 'external_cluster_id'),
        external_cluster_instance_id=pulumi.get(__ret__, 'external_cluster_instance_id'),
        external_connector_id=pulumi.get(__ret__, 'external_connector_id'),
        external_db_node_id=pulumi.get(__ret__, 'external_db_node_id'),
        external_db_system_id=pulumi.get(__ret__, 'external_db_system_id'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        host_name=pulumi.get(__ret__, 'host_name'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        node_role=pulumi.get(__ret__, 'node_role'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_external_cluster_instance)
def get_external_cluster_instance_output(external_cluster_instance_id: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalClusterInstanceResult]:
    """
    This data source provides details about a specific External Cluster Instance resource in Oracle Cloud Infrastructure Database Management service.

    Gets the details for the external cluster instance specified by `externalClusterInstanceId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_cluster_instance = oci.DatabaseManagement.get_external_cluster_instance(external_cluster_instance_id=test_external_cluster_instance_oci_database_management_external_cluster_instance["id"])
    ```


    :param str external_cluster_instance_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external cluster instance.
    """
    ...
