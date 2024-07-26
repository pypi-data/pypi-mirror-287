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
    'GetOceInstancesResult',
    'AwaitableGetOceInstancesResult',
    'get_oce_instances',
    'get_oce_instances_output',
]

@pulumi.output_type
class GetOceInstancesResult:
    """
    A collection of values returned by getOceInstances.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, oce_instances=None, state=None, tenancy_id=None):
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
        if oce_instances and not isinstance(oce_instances, list):
            raise TypeError("Expected argument 'oce_instances' to be a list")
        pulumi.set(__self__, "oce_instances", oce_instances)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tenancy_id and not isinstance(tenancy_id, str):
            raise TypeError("Expected argument 'tenancy_id' to be a str")
        pulumi.set(__self__, "tenancy_id", tenancy_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetOceInstancesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="oceInstances")
    def oce_instances(self) -> Sequence['outputs.GetOceInstancesOceInstanceResult']:
        """
        The list of oce_instances.
        """
        return pulumi.get(self, "oce_instances")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the instance lifecycle.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tenancyId")
    def tenancy_id(self) -> Optional[str]:
        """
        Tenancy Identifier
        """
        return pulumi.get(self, "tenancy_id")


class AwaitableGetOceInstancesResult(GetOceInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOceInstancesResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            oce_instances=self.oce_instances,
            state=self.state,
            tenancy_id=self.tenancy_id)


def get_oce_instances(compartment_id: Optional[str] = None,
                      display_name: Optional[str] = None,
                      filters: Optional[Sequence[pulumi.InputType['GetOceInstancesFilterArgs']]] = None,
                      state: Optional[str] = None,
                      tenancy_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOceInstancesResult:
    """
    This data source provides the list of Oce Instances in Oracle Cloud Infrastructure Content and Experience service.

    Returns a list of OceInstances.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_oce_instances = oci.Oce.get_oce_instances(compartment_id=compartment_id,
        display_name=oce_instance_display_name,
        state=oce_instance_state,
        tenancy_id=test_tenancy["id"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str state: Filter results on lifecycleState.
    :param str tenancy_id: The ID of the tenancy in which to list resources.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    __args__['tenancyId'] = tenancy_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Oce/getOceInstances:getOceInstances', __args__, opts=opts, typ=GetOceInstancesResult).value

    return AwaitableGetOceInstancesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        oce_instances=pulumi.get(__ret__, 'oce_instances'),
        state=pulumi.get(__ret__, 'state'),
        tenancy_id=pulumi.get(__ret__, 'tenancy_id'))


@_utilities.lift_output_func(get_oce_instances)
def get_oce_instances_output(compartment_id: Optional[pulumi.Input[str]] = None,
                             display_name: Optional[pulumi.Input[Optional[str]]] = None,
                             filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetOceInstancesFilterArgs']]]]] = None,
                             state: Optional[pulumi.Input[Optional[str]]] = None,
                             tenancy_id: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOceInstancesResult]:
    """
    This data source provides the list of Oce Instances in Oracle Cloud Infrastructure Content and Experience service.

    Returns a list of OceInstances.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_oce_instances = oci.Oce.get_oce_instances(compartment_id=compartment_id,
        display_name=oce_instance_display_name,
        state=oce_instance_state,
        tenancy_id=test_tenancy["id"])
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable.  Example: `My new resource`
    :param str state: Filter results on lifecycleState.
    :param str tenancy_id: The ID of the tenancy in which to list resources.
    """
    ...
