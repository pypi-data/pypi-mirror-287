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
    'GetNetworkFirewallPolicySecurityRulesResult',
    'AwaitableGetNetworkFirewallPolicySecurityRulesResult',
    'get_network_firewall_policy_security_rules',
    'get_network_firewall_policy_security_rules_output',
]

@pulumi.output_type
class GetNetworkFirewallPolicySecurityRulesResult:
    """
    A collection of values returned by getNetworkFirewallPolicySecurityRules.
    """
    def __init__(__self__, display_name=None, filters=None, id=None, network_firewall_policy_id=None, security_rule_priority_order=None, security_rule_summary_collections=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if network_firewall_policy_id and not isinstance(network_firewall_policy_id, str):
            raise TypeError("Expected argument 'network_firewall_policy_id' to be a str")
        pulumi.set(__self__, "network_firewall_policy_id", network_firewall_policy_id)
        if security_rule_priority_order and not isinstance(security_rule_priority_order, int):
            raise TypeError("Expected argument 'security_rule_priority_order' to be a int")
        pulumi.set(__self__, "security_rule_priority_order", security_rule_priority_order)
        if security_rule_summary_collections and not isinstance(security_rule_summary_collections, list):
            raise TypeError("Expected argument 'security_rule_summary_collections' to be a list")
        pulumi.set(__self__, "security_rule_summary_collections", security_rule_summary_collections)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetNetworkFirewallPolicySecurityRulesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="networkFirewallPolicyId")
    def network_firewall_policy_id(self) -> str:
        return pulumi.get(self, "network_firewall_policy_id")

    @property
    @pulumi.getter(name="securityRulePriorityOrder")
    def security_rule_priority_order(self) -> Optional[int]:
        return pulumi.get(self, "security_rule_priority_order")

    @property
    @pulumi.getter(name="securityRuleSummaryCollections")
    def security_rule_summary_collections(self) -> Sequence['outputs.GetNetworkFirewallPolicySecurityRulesSecurityRuleSummaryCollectionResult']:
        """
        The list of security_rule_summary_collection.
        """
        return pulumi.get(self, "security_rule_summary_collections")


class AwaitableGetNetworkFirewallPolicySecurityRulesResult(GetNetworkFirewallPolicySecurityRulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkFirewallPolicySecurityRulesResult(
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            network_firewall_policy_id=self.network_firewall_policy_id,
            security_rule_priority_order=self.security_rule_priority_order,
            security_rule_summary_collections=self.security_rule_summary_collections)


def get_network_firewall_policy_security_rules(display_name: Optional[str] = None,
                                               filters: Optional[Sequence[pulumi.InputType['GetNetworkFirewallPolicySecurityRulesFilterArgs']]] = None,
                                               network_firewall_policy_id: Optional[str] = None,
                                               security_rule_priority_order: Optional[int] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkFirewallPolicySecurityRulesResult:
    """
    This data source provides the list of Network Firewall Policy Security Rules in Oracle Cloud Infrastructure Network Firewall service.

    Returns a list of Security Rule for the Network Firewall Policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_network_firewall_policy_security_rules = oci.NetworkFirewall.get_network_firewall_policy_security_rules(network_firewall_policy_id=test_network_firewall_policy["id"],
        display_name=network_firewall_policy_security_rule_display_name,
        security_rule_priority_order=network_firewall_policy_security_rule_security_rule_priority_order)
    ```


    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str network_firewall_policy_id: Unique Network Firewall Policy identifier
    :param int security_rule_priority_order: Unique priority order for Security Rules in the network firewall policy.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['networkFirewallPolicyId'] = network_firewall_policy_id
    __args__['securityRulePriorityOrder'] = security_rule_priority_order
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:NetworkFirewall/getNetworkFirewallPolicySecurityRules:getNetworkFirewallPolicySecurityRules', __args__, opts=opts, typ=GetNetworkFirewallPolicySecurityRulesResult).value

    return AwaitableGetNetworkFirewallPolicySecurityRulesResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        network_firewall_policy_id=pulumi.get(__ret__, 'network_firewall_policy_id'),
        security_rule_priority_order=pulumi.get(__ret__, 'security_rule_priority_order'),
        security_rule_summary_collections=pulumi.get(__ret__, 'security_rule_summary_collections'))


@_utilities.lift_output_func(get_network_firewall_policy_security_rules)
def get_network_firewall_policy_security_rules_output(display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetNetworkFirewallPolicySecurityRulesFilterArgs']]]]] = None,
                                                      network_firewall_policy_id: Optional[pulumi.Input[str]] = None,
                                                      security_rule_priority_order: Optional[pulumi.Input[Optional[int]]] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkFirewallPolicySecurityRulesResult]:
    """
    This data source provides the list of Network Firewall Policy Security Rules in Oracle Cloud Infrastructure Network Firewall service.

    Returns a list of Security Rule for the Network Firewall Policy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_network_firewall_policy_security_rules = oci.NetworkFirewall.get_network_firewall_policy_security_rules(network_firewall_policy_id=test_network_firewall_policy["id"],
        display_name=network_firewall_policy_security_rule_display_name,
        security_rule_priority_order=network_firewall_policy_security_rule_security_rule_priority_order)
    ```


    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str network_firewall_policy_id: Unique Network Firewall Policy identifier
    :param int security_rule_priority_order: Unique priority order for Security Rules in the network firewall policy.
    """
    ...
