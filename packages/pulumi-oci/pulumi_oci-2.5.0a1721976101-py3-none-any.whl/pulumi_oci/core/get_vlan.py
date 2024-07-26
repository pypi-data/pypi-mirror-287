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
    'GetVlanResult',
    'AwaitableGetVlanResult',
    'get_vlan',
    'get_vlan_output',
]

@pulumi.output_type
class GetVlanResult:
    """
    A collection of values returned by getVlan.
    """
    def __init__(__self__, availability_domain=None, cidr_block=None, compartment_id=None, defined_tags=None, display_name=None, freeform_tags=None, id=None, nsg_ids=None, route_table_id=None, state=None, time_created=None, vcn_id=None, vlan_id=None, vlan_tag=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if cidr_block and not isinstance(cidr_block, str):
            raise TypeError("Expected argument 'cidr_block' to be a str")
        pulumi.set(__self__, "cidr_block", cidr_block)
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
        if nsg_ids and not isinstance(nsg_ids, list):
            raise TypeError("Expected argument 'nsg_ids' to be a list")
        pulumi.set(__self__, "nsg_ids", nsg_ids)
        if route_table_id and not isinstance(route_table_id, str):
            raise TypeError("Expected argument 'route_table_id' to be a str")
        pulumi.set(__self__, "route_table_id", route_table_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)
        if vlan_id and not isinstance(vlan_id, str):
            raise TypeError("Expected argument 'vlan_id' to be a str")
        pulumi.set(__self__, "vlan_id", vlan_id)
        if vlan_tag and not isinstance(vlan_tag, int):
            raise TypeError("Expected argument 'vlan_tag' to be a int")
        pulumi.set(__self__, "vlan_tag", vlan_tag)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The VLAN's availability domain. This attribute will be null if this is a regional VLAN rather than an AD-specific VLAN.  Example: `Uocm:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> str:
        """
        The range of IPv4 addresses that will be used for layer 3 communication with hosts outside the VLAN.  Example: `192.168.1.0/24`
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the VLAN.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The VLAN's Oracle ID ([OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nsgIds")
    def nsg_ids(self) -> Sequence[str]:
        """
        A list of the OCIDs of the network security groups (NSGs) to use with this VLAN. All VNICs in the VLAN belong to these NSGs. For more information about NSGs, see [NetworkSecurityGroup](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
        """
        return pulumi.get(self, "nsg_ids")

    @property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table that the VLAN uses.
        """
        return pulumi.get(self, "route_table_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The VLAN's current state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the VLAN was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the VLAN is in.
        """
        return pulumi.get(self, "vcn_id")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> str:
        return pulumi.get(self, "vlan_id")

    @property
    @pulumi.getter(name="vlanTag")
    def vlan_tag(self) -> int:
        """
        The IEEE 802.1Q VLAN tag of this VLAN.  Example: `100`
        """
        return pulumi.get(self, "vlan_tag")


class AwaitableGetVlanResult(GetVlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVlanResult(
            availability_domain=self.availability_domain,
            cidr_block=self.cidr_block,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            nsg_ids=self.nsg_ids,
            route_table_id=self.route_table_id,
            state=self.state,
            time_created=self.time_created,
            vcn_id=self.vcn_id,
            vlan_id=self.vlan_id,
            vlan_tag=self.vlan_tag)


def get_vlan(vlan_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVlanResult:
    """
    This data source provides details about a specific Vlan resource in Oracle Cloud Infrastructure Core service.

    Gets the specified VLAN's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vlan = oci.Core.get_vlan(vlan_id=test_vlan_oci_core_vlan["id"])
    ```


    :param str vlan_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
    """
    __args__ = dict()
    __args__['vlanId'] = vlan_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getVlan:getVlan', __args__, opts=opts, typ=GetVlanResult).value

    return AwaitableGetVlanResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        cidr_block=pulumi.get(__ret__, 'cidr_block'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        nsg_ids=pulumi.get(__ret__, 'nsg_ids'),
        route_table_id=pulumi.get(__ret__, 'route_table_id'),
        state=pulumi.get(__ret__, 'state'),
        time_created=pulumi.get(__ret__, 'time_created'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'),
        vlan_id=pulumi.get(__ret__, 'vlan_id'),
        vlan_tag=pulumi.get(__ret__, 'vlan_tag'))


@_utilities.lift_output_func(get_vlan)
def get_vlan_output(vlan_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVlanResult]:
    """
    This data source provides details about a specific Vlan resource in Oracle Cloud Infrastructure Core service.

    Gets the specified VLAN's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_vlan = oci.Core.get_vlan(vlan_id=test_vlan_oci_core_vlan["id"])
    ```


    :param str vlan_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
    """
    ...
