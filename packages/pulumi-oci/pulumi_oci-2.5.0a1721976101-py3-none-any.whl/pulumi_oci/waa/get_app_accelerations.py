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
    'GetAppAccelerationsResult',
    'AwaitableGetAppAccelerationsResult',
    'get_app_accelerations',
    'get_app_accelerations_output',
]

@pulumi.output_type
class GetAppAccelerationsResult:
    """
    A collection of values returned by getAppAccelerations.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, states=None, web_app_acceleration_collections=None, web_app_acceleration_policy_id=None):
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
        if states and not isinstance(states, list):
            raise TypeError("Expected argument 'states' to be a list")
        pulumi.set(__self__, "states", states)
        if web_app_acceleration_collections and not isinstance(web_app_acceleration_collections, list):
            raise TypeError("Expected argument 'web_app_acceleration_collections' to be a list")
        pulumi.set(__self__, "web_app_acceleration_collections", web_app_acceleration_collections)
        if web_app_acceleration_policy_id and not isinstance(web_app_acceleration_policy_id, str):
            raise TypeError("Expected argument 'web_app_acceleration_policy_id' to be a str")
        pulumi.set(__self__, "web_app_acceleration_policy_id", web_app_acceleration_policy_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        WebAppAcceleration display name, can be renamed.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAppAccelerationsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WebAppAcceleration.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def states(self) -> Optional[Sequence[str]]:
        """
        The current state of the WebAppAcceleration.
        """
        return pulumi.get(self, "states")

    @property
    @pulumi.getter(name="webAppAccelerationCollections")
    def web_app_acceleration_collections(self) -> Sequence['outputs.GetAppAccelerationsWebAppAccelerationCollectionResult']:
        """
        The list of web_app_acceleration_collection.
        """
        return pulumi.get(self, "web_app_acceleration_collections")

    @property
    @pulumi.getter(name="webAppAccelerationPolicyId")
    def web_app_acceleration_policy_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of WebAppAccelerationPolicy, which is attached to the resource.
        """
        return pulumi.get(self, "web_app_acceleration_policy_id")


class AwaitableGetAppAccelerationsResult(GetAppAccelerationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppAccelerationsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            states=self.states,
            web_app_acceleration_collections=self.web_app_acceleration_collections,
            web_app_acceleration_policy_id=self.web_app_acceleration_policy_id)


def get_app_accelerations(compartment_id: Optional[str] = None,
                          display_name: Optional[str] = None,
                          filters: Optional[Sequence[pulumi.InputType['GetAppAccelerationsFilterArgs']]] = None,
                          id: Optional[str] = None,
                          states: Optional[Sequence[str]] = None,
                          web_app_acceleration_policy_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppAccelerationsResult:
    """
    This data source provides the list of Web App Accelerations in Oracle Cloud Infrastructure Waa service.

    Gets a list of all WebAppAccelerations in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_web_app_accelerations = oci.Waa.get_app_accelerations(compartment_id=compartment_id,
        display_name=web_app_acceleration_display_name,
        id=web_app_acceleration_id,
        states=web_app_acceleration_state,
        web_app_acceleration_policy_id=test_web_app_acceleration_policy["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str id: A filter to return only the WebAppAcceleration with the given [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param Sequence[str] states: A filter to return only resources that match the given lifecycleState.
    :param str web_app_acceleration_policy_id: A filter to return only the WebAppAcceleration with the given [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of related WebAppAccelerationPolicy.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['states'] = states
    __args__['webAppAccelerationPolicyId'] = web_app_acceleration_policy_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Waa/getAppAccelerations:getAppAccelerations', __args__, opts=opts, typ=GetAppAccelerationsResult).value

    return AwaitableGetAppAccelerationsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        states=pulumi.get(__ret__, 'states'),
        web_app_acceleration_collections=pulumi.get(__ret__, 'web_app_acceleration_collections'),
        web_app_acceleration_policy_id=pulumi.get(__ret__, 'web_app_acceleration_policy_id'))


@_utilities.lift_output_func(get_app_accelerations)
def get_app_accelerations_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                 display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAppAccelerationsFilterArgs']]]]] = None,
                                 id: Optional[pulumi.Input[Optional[str]]] = None,
                                 states: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                 web_app_acceleration_policy_id: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppAccelerationsResult]:
    """
    This data source provides the list of Web App Accelerations in Oracle Cloud Infrastructure Waa service.

    Gets a list of all WebAppAccelerations in a compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_web_app_accelerations = oci.Waa.get_app_accelerations(compartment_id=compartment_id,
        display_name=web_app_acceleration_display_name,
        id=web_app_acceleration_id,
        states=web_app_acceleration_state,
        web_app_acceleration_policy_id=test_web_app_acceleration_policy["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str id: A filter to return only the WebAppAcceleration with the given [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param Sequence[str] states: A filter to return only resources that match the given lifecycleState.
    :param str web_app_acceleration_policy_id: A filter to return only the WebAppAcceleration with the given [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of related WebAppAccelerationPolicy.
    """
    ...
