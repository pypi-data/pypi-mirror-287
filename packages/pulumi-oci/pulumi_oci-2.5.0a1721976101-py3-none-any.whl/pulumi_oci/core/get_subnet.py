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
    'GetSubnetResult',
    'AwaitableGetSubnetResult',
    'get_subnet',
    'get_subnet_output',
]

@pulumi.output_type
class GetSubnetResult:
    """
    A collection of values returned by getSubnet.
    """
    def __init__(__self__, availability_domain=None, cidr_block=None, compartment_id=None, defined_tags=None, dhcp_options_id=None, display_name=None, dns_label=None, freeform_tags=None, id=None, ipv6cidr_block=None, ipv6cidr_blocks=None, ipv6virtual_router_ip=None, prohibit_internet_ingress=None, prohibit_public_ip_on_vnic=None, route_table_id=None, security_list_ids=None, state=None, subnet_domain_name=None, subnet_id=None, time_created=None, vcn_id=None, virtual_router_ip=None, virtual_router_mac=None):
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
        if dhcp_options_id and not isinstance(dhcp_options_id, str):
            raise TypeError("Expected argument 'dhcp_options_id' to be a str")
        pulumi.set(__self__, "dhcp_options_id", dhcp_options_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if dns_label and not isinstance(dns_label, str):
            raise TypeError("Expected argument 'dns_label' to be a str")
        pulumi.set(__self__, "dns_label", dns_label)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv6cidr_block and not isinstance(ipv6cidr_block, str):
            raise TypeError("Expected argument 'ipv6cidr_block' to be a str")
        pulumi.set(__self__, "ipv6cidr_block", ipv6cidr_block)
        if ipv6cidr_blocks and not isinstance(ipv6cidr_blocks, list):
            raise TypeError("Expected argument 'ipv6cidr_blocks' to be a list")
        pulumi.set(__self__, "ipv6cidr_blocks", ipv6cidr_blocks)
        if ipv6virtual_router_ip and not isinstance(ipv6virtual_router_ip, str):
            raise TypeError("Expected argument 'ipv6virtual_router_ip' to be a str")
        pulumi.set(__self__, "ipv6virtual_router_ip", ipv6virtual_router_ip)
        if prohibit_internet_ingress and not isinstance(prohibit_internet_ingress, bool):
            raise TypeError("Expected argument 'prohibit_internet_ingress' to be a bool")
        pulumi.set(__self__, "prohibit_internet_ingress", prohibit_internet_ingress)
        if prohibit_public_ip_on_vnic and not isinstance(prohibit_public_ip_on_vnic, bool):
            raise TypeError("Expected argument 'prohibit_public_ip_on_vnic' to be a bool")
        pulumi.set(__self__, "prohibit_public_ip_on_vnic", prohibit_public_ip_on_vnic)
        if route_table_id and not isinstance(route_table_id, str):
            raise TypeError("Expected argument 'route_table_id' to be a str")
        pulumi.set(__self__, "route_table_id", route_table_id)
        if security_list_ids and not isinstance(security_list_ids, list):
            raise TypeError("Expected argument 'security_list_ids' to be a list")
        pulumi.set(__self__, "security_list_ids", security_list_ids)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subnet_domain_name and not isinstance(subnet_domain_name, str):
            raise TypeError("Expected argument 'subnet_domain_name' to be a str")
        pulumi.set(__self__, "subnet_domain_name", subnet_domain_name)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)
        if virtual_router_ip and not isinstance(virtual_router_ip, str):
            raise TypeError("Expected argument 'virtual_router_ip' to be a str")
        pulumi.set(__self__, "virtual_router_ip", virtual_router_ip)
        if virtual_router_mac and not isinstance(virtual_router_mac, str):
            raise TypeError("Expected argument 'virtual_router_mac' to be a str")
        pulumi.set(__self__, "virtual_router_mac", virtual_router_mac)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The subnet's availability domain. This attribute will be null if this is a regional subnet instead of an AD-specific subnet. Oracle recommends creating regional subnets.  Example: `Uocm:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> str:
        """
        The subnet's CIDR block.  Example: `10.0.1.0/24`
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the subnet.
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
    @pulumi.getter(name="dhcpOptionsId")
    def dhcp_options_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the set of DHCP options that the subnet uses.
        """
        return pulumi.get(self, "dhcp_options_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dnsLabel")
    def dns_label(self) -> str:
        """
        A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed.
        """
        return pulumi.get(self, "dns_label")

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
        The subnet's Oracle ID ([OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv6cidrBlock")
    def ipv6cidr_block(self) -> str:
        """
        For an IPv6-enabled subnet, this is the IPv6 prefix for the subnet's IP address space. The subnet size is always /64. See [IPv6 Addresses](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).  Example: `2001:0db8:0123:1111::/64`
        """
        return pulumi.get(self, "ipv6cidr_block")

    @property
    @pulumi.getter(name="ipv6cidrBlocks")
    def ipv6cidr_blocks(self) -> Sequence[str]:
        """
        The list of all IPv6 prefixes (Oracle allocated IPv6 GUA, ULA or private IPv6 prefixes, BYOIPv6 prefixes) for the subnet.
        """
        return pulumi.get(self, "ipv6cidr_blocks")

    @property
    @pulumi.getter(name="ipv6virtualRouterIp")
    def ipv6virtual_router_ip(self) -> str:
        """
        For an IPv6-enabled subnet, this is the IPv6 address of the virtual router.  Example: `2001:0db8:0123:1111:89ab:cdef:1234:5678`
        """
        return pulumi.get(self, "ipv6virtual_router_ip")

    @property
    @pulumi.getter(name="prohibitInternetIngress")
    def prohibit_internet_ingress(self) -> bool:
        """
        Whether to disallow ingress internet traffic to VNICs within this subnet. Defaults to false.
        """
        return pulumi.get(self, "prohibit_internet_ingress")

    @property
    @pulumi.getter(name="prohibitPublicIpOnVnic")
    def prohibit_public_ip_on_vnic(self) -> bool:
        """
        Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/latest/CreateVnicDetails/)). If `prohibitPublicIpOnVnic` is set to true, VNICs created in this subnet cannot have public IP addresses (that is, it's a private subnet).  Example: `true`
        """
        return pulumi.get(self, "prohibit_public_ip_on_vnic")

    @property
    @pulumi.getter(name="routeTableId")
    def route_table_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table that the subnet uses.
        """
        return pulumi.get(self, "route_table_id")

    @property
    @pulumi.getter(name="securityListIds")
    def security_list_ids(self) -> Sequence[str]:
        """
        The OCIDs of the security list or lists that the subnet uses. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.
        """
        return pulumi.get(self, "security_list_ids")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The subnet's current state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subnetDomainName")
    def subnet_domain_name(self) -> str:
        """
        The subnet's domain name, which consists of the subnet's DNS label, the VCN's DNS label, and the `oraclevcn.com` domain.
        """
        return pulumi.get(self, "subnet_domain_name")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the subnet was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).  Example: `2016-08-25T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the subnet is in.
        """
        return pulumi.get(self, "vcn_id")

    @property
    @pulumi.getter(name="virtualRouterIp")
    def virtual_router_ip(self) -> str:
        """
        The IP address of the virtual router.  Example: `10.0.14.1`
        """
        return pulumi.get(self, "virtual_router_ip")

    @property
    @pulumi.getter(name="virtualRouterMac")
    def virtual_router_mac(self) -> str:
        """
        The MAC address of the virtual router.  Example: `00:00:00:00:00:01`
        """
        return pulumi.get(self, "virtual_router_mac")


class AwaitableGetSubnetResult(GetSubnetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubnetResult(
            availability_domain=self.availability_domain,
            cidr_block=self.cidr_block,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            dhcp_options_id=self.dhcp_options_id,
            display_name=self.display_name,
            dns_label=self.dns_label,
            freeform_tags=self.freeform_tags,
            id=self.id,
            ipv6cidr_block=self.ipv6cidr_block,
            ipv6cidr_blocks=self.ipv6cidr_blocks,
            ipv6virtual_router_ip=self.ipv6virtual_router_ip,
            prohibit_internet_ingress=self.prohibit_internet_ingress,
            prohibit_public_ip_on_vnic=self.prohibit_public_ip_on_vnic,
            route_table_id=self.route_table_id,
            security_list_ids=self.security_list_ids,
            state=self.state,
            subnet_domain_name=self.subnet_domain_name,
            subnet_id=self.subnet_id,
            time_created=self.time_created,
            vcn_id=self.vcn_id,
            virtual_router_ip=self.virtual_router_ip,
            virtual_router_mac=self.virtual_router_mac)


def get_subnet(subnet_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubnetResult:
    """
    This data source provides details about a specific Subnet resource in Oracle Cloud Infrastructure Core service.

    Gets the specified subnet's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_subnet = oci.Core.get_subnet(subnet_id=test_subnet_oci_core_subnet["id"])
    ```


    :param str subnet_id: Specify the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet.
    """
    __args__ = dict()
    __args__['subnetId'] = subnet_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getSubnet:getSubnet', __args__, opts=opts, typ=GetSubnetResult).value

    return AwaitableGetSubnetResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        cidr_block=pulumi.get(__ret__, 'cidr_block'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        dhcp_options_id=pulumi.get(__ret__, 'dhcp_options_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        dns_label=pulumi.get(__ret__, 'dns_label'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        ipv6cidr_block=pulumi.get(__ret__, 'ipv6cidr_block'),
        ipv6cidr_blocks=pulumi.get(__ret__, 'ipv6cidr_blocks'),
        ipv6virtual_router_ip=pulumi.get(__ret__, 'ipv6virtual_router_ip'),
        prohibit_internet_ingress=pulumi.get(__ret__, 'prohibit_internet_ingress'),
        prohibit_public_ip_on_vnic=pulumi.get(__ret__, 'prohibit_public_ip_on_vnic'),
        route_table_id=pulumi.get(__ret__, 'route_table_id'),
        security_list_ids=pulumi.get(__ret__, 'security_list_ids'),
        state=pulumi.get(__ret__, 'state'),
        subnet_domain_name=pulumi.get(__ret__, 'subnet_domain_name'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        time_created=pulumi.get(__ret__, 'time_created'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'),
        virtual_router_ip=pulumi.get(__ret__, 'virtual_router_ip'),
        virtual_router_mac=pulumi.get(__ret__, 'virtual_router_mac'))


@_utilities.lift_output_func(get_subnet)
def get_subnet_output(subnet_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSubnetResult]:
    """
    This data source provides details about a specific Subnet resource in Oracle Cloud Infrastructure Core service.

    Gets the specified subnet's information.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_subnet = oci.Core.get_subnet(subnet_id=test_subnet_oci_core_subnet["id"])
    ```


    :param str subnet_id: Specify the [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet.
    """
    ...
