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
    'GetBuildRunsResult',
    'AwaitableGetBuildRunsResult',
    'get_build_runs',
    'get_build_runs_output',
]

@pulumi.output_type
class GetBuildRunsResult:
    """
    A collection of values returned by getBuildRuns.
    """
    def __init__(__self__, build_pipeline_id=None, build_run_summary_collections=None, compartment_id=None, display_name=None, filters=None, id=None, project_id=None, state=None):
        if build_pipeline_id and not isinstance(build_pipeline_id, str):
            raise TypeError("Expected argument 'build_pipeline_id' to be a str")
        pulumi.set(__self__, "build_pipeline_id", build_pipeline_id)
        if build_run_summary_collections and not isinstance(build_run_summary_collections, list):
            raise TypeError("Expected argument 'build_run_summary_collections' to be a list")
        pulumi.set(__self__, "build_run_summary_collections", build_run_summary_collections)
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
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="buildPipelineId")
    def build_pipeline_id(self) -> Optional[str]:
        """
        The OCID of the build pipeline to be triggered.
        """
        return pulumi.get(self, "build_pipeline_id")

    @property
    @pulumi.getter(name="buildRunSummaryCollections")
    def build_run_summary_collections(self) -> Sequence['outputs.GetBuildRunsBuildRunSummaryCollectionResult']:
        """
        The list of build_run_summary_collection.
        """
        return pulumi.get(self, "build_run_summary_collections")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        The OCID of the compartment where the build is running.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetBuildRunsFilterResult']]:
        """
        The filters for the trigger.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier that is immutable on creation.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        """
        The OCID of the DevOps project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the build run.
        """
        return pulumi.get(self, "state")


class AwaitableGetBuildRunsResult(GetBuildRunsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBuildRunsResult(
            build_pipeline_id=self.build_pipeline_id,
            build_run_summary_collections=self.build_run_summary_collections,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            project_id=self.project_id,
            state=self.state)


def get_build_runs(build_pipeline_id: Optional[str] = None,
                   compartment_id: Optional[str] = None,
                   display_name: Optional[str] = None,
                   filters: Optional[Sequence[pulumi.InputType['GetBuildRunsFilterArgs']]] = None,
                   id: Optional[str] = None,
                   project_id: Optional[str] = None,
                   state: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBuildRunsResult:
    """
    This data source provides the list of Build Runs in Oracle Cloud Infrastructure Devops service.

    Returns a list of build run summary.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_build_runs = oci.DevOps.get_build_runs(build_pipeline_id=test_build_pipeline["id"],
        compartment_id=compartment_id,
        display_name=build_run_display_name,
        id=build_run_id,
        project_id=test_project["id"],
        state=build_run_state)
    ```


    :param str build_pipeline_id: Unique build pipeline identifier.
    :param str compartment_id: The OCID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param Sequence[pulumi.InputType['GetBuildRunsFilterArgs']] filters: The filters for the trigger.
    :param str id: Unique identifier or OCID for listing a single resource by ID.
    :param str project_id: unique project identifier
    :param str state: A filter to return only build runs that matches the given lifecycle state.
    """
    __args__ = dict()
    __args__['buildPipelineId'] = build_pipeline_id
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['projectId'] = project_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DevOps/getBuildRuns:getBuildRuns', __args__, opts=opts, typ=GetBuildRunsResult).value

    return AwaitableGetBuildRunsResult(
        build_pipeline_id=pulumi.get(__ret__, 'build_pipeline_id'),
        build_run_summary_collections=pulumi.get(__ret__, 'build_run_summary_collections'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        project_id=pulumi.get(__ret__, 'project_id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_build_runs)
def get_build_runs_output(build_pipeline_id: Optional[pulumi.Input[Optional[str]]] = None,
                          compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                          display_name: Optional[pulumi.Input[Optional[str]]] = None,
                          filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetBuildRunsFilterArgs']]]]] = None,
                          id: Optional[pulumi.Input[Optional[str]]] = None,
                          project_id: Optional[pulumi.Input[Optional[str]]] = None,
                          state: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBuildRunsResult]:
    """
    This data source provides the list of Build Runs in Oracle Cloud Infrastructure Devops service.

    Returns a list of build run summary.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_build_runs = oci.DevOps.get_build_runs(build_pipeline_id=test_build_pipeline["id"],
        compartment_id=compartment_id,
        display_name=build_run_display_name,
        id=build_run_id,
        project_id=test_project["id"],
        state=build_run_state)
    ```


    :param str build_pipeline_id: Unique build pipeline identifier.
    :param str compartment_id: The OCID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param Sequence[pulumi.InputType['GetBuildRunsFilterArgs']] filters: The filters for the trigger.
    :param str id: Unique identifier or OCID for listing a single resource by ID.
    :param str project_id: unique project identifier
    :param str state: A filter to return only build runs that matches the given lifecycle state.
    """
    ...
