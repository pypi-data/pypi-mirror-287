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
    'GetFusionEnvironmentScheduledActivitiesResult',
    'AwaitableGetFusionEnvironmentScheduledActivitiesResult',
    'get_fusion_environment_scheduled_activities',
    'get_fusion_environment_scheduled_activities_output',
]

@pulumi.output_type
class GetFusionEnvironmentScheduledActivitiesResult:
    """
    A collection of values returned by getFusionEnvironmentScheduledActivities.
    """
    def __init__(__self__, display_name=None, filters=None, fusion_environment_id=None, id=None, run_cycle=None, scheduled_activity_collections=None, state=None, time_expected_finish_less_than_or_equal_to=None, time_scheduled_start_greater_than_or_equal_to=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if fusion_environment_id and not isinstance(fusion_environment_id, str):
            raise TypeError("Expected argument 'fusion_environment_id' to be a str")
        pulumi.set(__self__, "fusion_environment_id", fusion_environment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if run_cycle and not isinstance(run_cycle, str):
            raise TypeError("Expected argument 'run_cycle' to be a str")
        pulumi.set(__self__, "run_cycle", run_cycle)
        if scheduled_activity_collections and not isinstance(scheduled_activity_collections, list):
            raise TypeError("Expected argument 'scheduled_activity_collections' to be a list")
        pulumi.set(__self__, "scheduled_activity_collections", scheduled_activity_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_expected_finish_less_than_or_equal_to and not isinstance(time_expected_finish_less_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_expected_finish_less_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_expected_finish_less_than_or_equal_to", time_expected_finish_less_than_or_equal_to)
        if time_scheduled_start_greater_than_or_equal_to and not isinstance(time_scheduled_start_greater_than_or_equal_to, str):
            raise TypeError("Expected argument 'time_scheduled_start_greater_than_or_equal_to' to be a str")
        pulumi.set(__self__, "time_scheduled_start_greater_than_or_equal_to", time_scheduled_start_greater_than_or_equal_to)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        scheduled activity display name, can be renamed.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetFusionEnvironmentScheduledActivitiesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="fusionEnvironmentId")
    def fusion_environment_id(self) -> str:
        """
        FAaaS Environment Identifier.
        """
        return pulumi.get(self, "fusion_environment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="runCycle")
    def run_cycle(self) -> Optional[str]:
        """
        run cadence.
        """
        return pulumi.get(self, "run_cycle")

    @property
    @pulumi.getter(name="scheduledActivityCollections")
    def scheduled_activity_collections(self) -> Sequence['outputs.GetFusionEnvironmentScheduledActivitiesScheduledActivityCollectionResult']:
        """
        The list of scheduled_activity_collection.
        """
        return pulumi.get(self, "scheduled_activity_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the scheduledActivity.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeExpectedFinishLessThanOrEqualTo")
    def time_expected_finish_less_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_expected_finish_less_than_or_equal_to")

    @property
    @pulumi.getter(name="timeScheduledStartGreaterThanOrEqualTo")
    def time_scheduled_start_greater_than_or_equal_to(self) -> Optional[str]:
        return pulumi.get(self, "time_scheduled_start_greater_than_or_equal_to")


class AwaitableGetFusionEnvironmentScheduledActivitiesResult(GetFusionEnvironmentScheduledActivitiesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFusionEnvironmentScheduledActivitiesResult(
            display_name=self.display_name,
            filters=self.filters,
            fusion_environment_id=self.fusion_environment_id,
            id=self.id,
            run_cycle=self.run_cycle,
            scheduled_activity_collections=self.scheduled_activity_collections,
            state=self.state,
            time_expected_finish_less_than_or_equal_to=self.time_expected_finish_less_than_or_equal_to,
            time_scheduled_start_greater_than_or_equal_to=self.time_scheduled_start_greater_than_or_equal_to)


def get_fusion_environment_scheduled_activities(display_name: Optional[str] = None,
                                                filters: Optional[Sequence[pulumi.InputType['GetFusionEnvironmentScheduledActivitiesFilterArgs']]] = None,
                                                fusion_environment_id: Optional[str] = None,
                                                run_cycle: Optional[str] = None,
                                                state: Optional[str] = None,
                                                time_expected_finish_less_than_or_equal_to: Optional[str] = None,
                                                time_scheduled_start_greater_than_or_equal_to: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFusionEnvironmentScheduledActivitiesResult:
    """
    This data source provides the list of Fusion Environment Scheduled Activities in Oracle Cloud Infrastructure Fusion Apps service.

    Returns a list of ScheduledActivities.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fusion_environment_scheduled_activities = oci.Functions.get_fusion_environment_scheduled_activities(fusion_environment_id=test_fusion_environment["id"],
        display_name=fusion_environment_scheduled_activity_display_name,
        run_cycle=fusion_environment_scheduled_activity_run_cycle,
        state=fusion_environment_scheduled_activity_state,
        time_expected_finish_less_than_or_equal_to=fusion_environment_scheduled_activity_time_expected_finish_less_than_or_equal_to,
        time_scheduled_start_greater_than_or_equal_to=fusion_environment_scheduled_activity_time_scheduled_start_greater_than_or_equal_to)
    ```


    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str fusion_environment_id: unique FusionEnvironment identifier
    :param str run_cycle: A filter that returns all resources that match the specified run cycle.
    :param str state: A filter that returns all resources that match the specified status
    :param str time_expected_finish_less_than_or_equal_to: A filter that returns all resources that end before this date
    :param str time_scheduled_start_greater_than_or_equal_to: A filter that returns all resources that are scheduled after this date
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['fusionEnvironmentId'] = fusion_environment_id
    __args__['runCycle'] = run_cycle
    __args__['state'] = state
    __args__['timeExpectedFinishLessThanOrEqualTo'] = time_expected_finish_less_than_or_equal_to
    __args__['timeScheduledStartGreaterThanOrEqualTo'] = time_scheduled_start_greater_than_or_equal_to
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Functions/getFusionEnvironmentScheduledActivities:getFusionEnvironmentScheduledActivities', __args__, opts=opts, typ=GetFusionEnvironmentScheduledActivitiesResult).value

    return AwaitableGetFusionEnvironmentScheduledActivitiesResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        fusion_environment_id=pulumi.get(__ret__, 'fusion_environment_id'),
        id=pulumi.get(__ret__, 'id'),
        run_cycle=pulumi.get(__ret__, 'run_cycle'),
        scheduled_activity_collections=pulumi.get(__ret__, 'scheduled_activity_collections'),
        state=pulumi.get(__ret__, 'state'),
        time_expected_finish_less_than_or_equal_to=pulumi.get(__ret__, 'time_expected_finish_less_than_or_equal_to'),
        time_scheduled_start_greater_than_or_equal_to=pulumi.get(__ret__, 'time_scheduled_start_greater_than_or_equal_to'))


@_utilities.lift_output_func(get_fusion_environment_scheduled_activities)
def get_fusion_environment_scheduled_activities_output(display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetFusionEnvironmentScheduledActivitiesFilterArgs']]]]] = None,
                                                       fusion_environment_id: Optional[pulumi.Input[str]] = None,
                                                       run_cycle: Optional[pulumi.Input[Optional[str]]] = None,
                                                       state: Optional[pulumi.Input[Optional[str]]] = None,
                                                       time_expected_finish_less_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                                       time_scheduled_start_greater_than_or_equal_to: Optional[pulumi.Input[Optional[str]]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFusionEnvironmentScheduledActivitiesResult]:
    """
    This data source provides the list of Fusion Environment Scheduled Activities in Oracle Cloud Infrastructure Fusion Apps service.

    Returns a list of ScheduledActivities.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_fusion_environment_scheduled_activities = oci.Functions.get_fusion_environment_scheduled_activities(fusion_environment_id=test_fusion_environment["id"],
        display_name=fusion_environment_scheduled_activity_display_name,
        run_cycle=fusion_environment_scheduled_activity_run_cycle,
        state=fusion_environment_scheduled_activity_state,
        time_expected_finish_less_than_or_equal_to=fusion_environment_scheduled_activity_time_expected_finish_less_than_or_equal_to,
        time_scheduled_start_greater_than_or_equal_to=fusion_environment_scheduled_activity_time_scheduled_start_greater_than_or_equal_to)
    ```


    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str fusion_environment_id: unique FusionEnvironment identifier
    :param str run_cycle: A filter that returns all resources that match the specified run cycle.
    :param str state: A filter that returns all resources that match the specified status
    :param str time_expected_finish_less_than_or_equal_to: A filter that returns all resources that end before this date
    :param str time_scheduled_start_greater_than_or_equal_to: A filter that returns all resources that are scheduled after this date
    """
    ...
