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
    'GetPrivateEndpointResult',
    'AwaitableGetPrivateEndpointResult',
    'get_private_endpoint',
    'get_private_endpoint_output',
]

@pulumi.output_type
class GetPrivateEndpointResult:
    """
    A collection of values returned by getPrivateEndpoint.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, description=None, display_name=None, freeform_tags=None, id=None, lifecycle_state_details=None, nsg_ids=None, private_endpoint_id=None, private_ip=None, sharded_databases=None, state=None, subnet_id=None, system_tags=None, time_created=None, time_updated=None, vcn_id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_state_details and not isinstance(lifecycle_state_details, str):
            raise TypeError("Expected argument 'lifecycle_state_details' to be a str")
        pulumi.set(__self__, "lifecycle_state_details", lifecycle_state_details)
        if nsg_ids and not isinstance(nsg_ids, list):
            raise TypeError("Expected argument 'nsg_ids' to be a list")
        pulumi.set(__self__, "nsg_ids", nsg_ids)
        if private_endpoint_id and not isinstance(private_endpoint_id, str):
            raise TypeError("Expected argument 'private_endpoint_id' to be a str")
        pulumi.set(__self__, "private_endpoint_id", private_endpoint_id)
        if private_ip and not isinstance(private_ip, str):
            raise TypeError("Expected argument 'private_ip' to be a str")
        pulumi.set(__self__, "private_ip", private_ip)
        if sharded_databases and not isinstance(sharded_databases, list):
            raise TypeError("Expected argument 'sharded_databases' to be a list")
        pulumi.set(__self__, "sharded_databases", sharded_databases)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Identifier of the compartment in which private endpoint exists.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        PrivateEndpoint description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        PrivateEndpoint display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier of the Private Endpoint.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleStateDetails")
    def lifecycle_state_details(self) -> str:
        """
        Detailed message for the lifecycle state.
        """
        return pulumi.get(self, "lifecycle_state_details")

    @property
    @pulumi.getter(name="nsgIds")
    def nsg_ids(self) -> Sequence[str]:
        """
        The OCIDs of the network security groups that the private endpoint belongs to.
        """
        return pulumi.get(self, "nsg_ids")

    @property
    @pulumi.getter(name="privateEndpointId")
    def private_endpoint_id(self) -> str:
        return pulumi.get(self, "private_endpoint_id")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> str:
        """
        IP address of the Private Endpoint.
        """
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="shardedDatabases")
    def sharded_databases(self) -> Sequence[str]:
        """
        The OCIDs of sharded databases that consumes the given private endpoint.
        """
        return pulumi.get(self, "sharded_databases")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Lifecycle states for private endpoint.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        Identifier of the subnet in which private endpoint exists.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the PrivateEndpoint was first created. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the Private Endpoint was last updated. An RFC3339 formatted datetime string
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> str:
        """
        Identifier of the VCN in which subnet exists.
        """
        return pulumi.get(self, "vcn_id")


class AwaitableGetPrivateEndpointResult(GetPrivateEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateEndpointResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            lifecycle_state_details=self.lifecycle_state_details,
            nsg_ids=self.nsg_ids,
            private_endpoint_id=self.private_endpoint_id,
            private_ip=self.private_ip,
            sharded_databases=self.sharded_databases,
            state=self.state,
            subnet_id=self.subnet_id,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated,
            vcn_id=self.vcn_id)


def get_private_endpoint(private_endpoint_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateEndpointResult:
    """
    This data source provides details about a specific Private Endpoint resource in Oracle Cloud Infrastructure Globally Distributed Database service.

    Get the PrivateEndpoint resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_private_endpoint = oci.GloballyDistributedDatabase.get_private_endpoint(private_endpoint_id=test_private_endpoint_oci_globally_distributed_database_private_endpoint["id"])
    ```


    :param str private_endpoint_id: Oracle Sharded Database PrivateEndpoint identifier
    """
    __args__ = dict()
    __args__['privateEndpointId'] = private_endpoint_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:GloballyDistributedDatabase/getPrivateEndpoint:getPrivateEndpoint', __args__, opts=opts, typ=GetPrivateEndpointResult).value

    return AwaitableGetPrivateEndpointResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_state_details=pulumi.get(__ret__, 'lifecycle_state_details'),
        nsg_ids=pulumi.get(__ret__, 'nsg_ids'),
        private_endpoint_id=pulumi.get(__ret__, 'private_endpoint_id'),
        private_ip=pulumi.get(__ret__, 'private_ip'),
        sharded_databases=pulumi.get(__ret__, 'sharded_databases'),
        state=pulumi.get(__ret__, 'state'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'))


@_utilities.lift_output_func(get_private_endpoint)
def get_private_endpoint_output(private_endpoint_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateEndpointResult]:
    """
    This data source provides details about a specific Private Endpoint resource in Oracle Cloud Infrastructure Globally Distributed Database service.

    Get the PrivateEndpoint resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_private_endpoint = oci.GloballyDistributedDatabase.get_private_endpoint(private_endpoint_id=test_private_endpoint_oci_globally_distributed_database_private_endpoint["id"])
    ```


    :param str private_endpoint_id: Oracle Sharded Database PrivateEndpoint identifier
    """
    ...
