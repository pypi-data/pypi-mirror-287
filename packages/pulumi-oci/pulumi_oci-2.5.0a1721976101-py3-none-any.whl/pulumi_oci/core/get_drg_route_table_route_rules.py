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
    'GetDrgRouteTableRouteRulesResult',
    'AwaitableGetDrgRouteTableRouteRulesResult',
    'get_drg_route_table_route_rules',
    'get_drg_route_table_route_rules_output',
]

@pulumi.output_type
class GetDrgRouteTableRouteRulesResult:
    """
    A collection of values returned by getDrgRouteTableRouteRules.
    """
    def __init__(__self__, drg_route_rules=None, drg_route_table_id=None, filters=None, id=None, route_type=None):
        if drg_route_rules and not isinstance(drg_route_rules, list):
            raise TypeError("Expected argument 'drg_route_rules' to be a list")
        pulumi.set(__self__, "drg_route_rules", drg_route_rules)
        if drg_route_table_id and not isinstance(drg_route_table_id, str):
            raise TypeError("Expected argument 'drg_route_table_id' to be a str")
        pulumi.set(__self__, "drg_route_table_id", drg_route_table_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if route_type and not isinstance(route_type, str):
            raise TypeError("Expected argument 'route_type' to be a str")
        pulumi.set(__self__, "route_type", route_type)

    @property
    @pulumi.getter(name="drgRouteRules")
    def drg_route_rules(self) -> Sequence['outputs.GetDrgRouteTableRouteRulesDrgRouteRuleResult']:
        """
        The list of drg_route_rules.
        """
        return pulumi.get(self, "drg_route_rules")

    @property
    @pulumi.getter(name="drgRouteTableId")
    def drg_route_table_id(self) -> str:
        return pulumi.get(self, "drg_route_table_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDrgRouteTableRouteRulesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="routeType")
    def route_type(self) -> Optional[str]:
        """
        You can specify static routes for the DRG route table using the API. The DRG learns dynamic routes from the DRG attachments using various routing protocols.
        """
        return pulumi.get(self, "route_type")


class AwaitableGetDrgRouteTableRouteRulesResult(GetDrgRouteTableRouteRulesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDrgRouteTableRouteRulesResult(
            drg_route_rules=self.drg_route_rules,
            drg_route_table_id=self.drg_route_table_id,
            filters=self.filters,
            id=self.id,
            route_type=self.route_type)


def get_drg_route_table_route_rules(drg_route_table_id: Optional[str] = None,
                                    filters: Optional[Sequence[pulumi.InputType['GetDrgRouteTableRouteRulesFilterArgs']]] = None,
                                    route_type: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDrgRouteTableRouteRulesResult:
    """
    This data source provides the list of Drg Route Table Route Rules in Oracle Cloud Infrastructure Core service.

    Lists the route rules in the specified DRG route table.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_drg_route_table_route_rules = oci.Core.get_drg_route_table_route_rules(drg_route_table_id=test_drg_route_table["id"],
        route_type=drg_route_table_route_rule_route_type)
    ```


    :param str drg_route_table_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
    :param str route_type: Static routes are specified through the DRG route table API. Dynamic routes are learned by the DRG from the DRG attachments through various routing protocols.
    """
    __args__ = dict()
    __args__['drgRouteTableId'] = drg_route_table_id
    __args__['filters'] = filters
    __args__['routeType'] = route_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getDrgRouteTableRouteRules:getDrgRouteTableRouteRules', __args__, opts=opts, typ=GetDrgRouteTableRouteRulesResult).value

    return AwaitableGetDrgRouteTableRouteRulesResult(
        drg_route_rules=pulumi.get(__ret__, 'drg_route_rules'),
        drg_route_table_id=pulumi.get(__ret__, 'drg_route_table_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        route_type=pulumi.get(__ret__, 'route_type'))


@_utilities.lift_output_func(get_drg_route_table_route_rules)
def get_drg_route_table_route_rules_output(drg_route_table_id: Optional[pulumi.Input[str]] = None,
                                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDrgRouteTableRouteRulesFilterArgs']]]]] = None,
                                           route_type: Optional[pulumi.Input[Optional[str]]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDrgRouteTableRouteRulesResult]:
    """
    This data source provides the list of Drg Route Table Route Rules in Oracle Cloud Infrastructure Core service.

    Lists the route rules in the specified DRG route table.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_drg_route_table_route_rules = oci.Core.get_drg_route_table_route_rules(drg_route_table_id=test_drg_route_table["id"],
        route_type=drg_route_table_route_rule_route_type)
    ```


    :param str drg_route_table_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
    :param str route_type: Static routes are specified through the DRG route table API. Dynamic routes are learned by the DRG from the DRG attachments through various routing protocols.
    """
    ...
