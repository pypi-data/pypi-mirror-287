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
    'GetLogAnalyticsLogGroupsResult',
    'AwaitableGetLogAnalyticsLogGroupsResult',
    'get_log_analytics_log_groups',
    'get_log_analytics_log_groups_output',
]

@pulumi.output_type
class GetLogAnalyticsLogGroupsResult:
    """
    A collection of values returned by getLogAnalyticsLogGroups.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, log_analytics_log_group_summary_collections=None, namespace=None):
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
        if log_analytics_log_group_summary_collections and not isinstance(log_analytics_log_group_summary_collections, list):
            raise TypeError("Expected argument 'log_analytics_log_group_summary_collections' to be a list")
        pulumi.set(__self__, "log_analytics_log_group_summary_collections", log_analytics_log_group_summary_collections)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier [OCID] (https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name that is changeable and that does not have to be unique. Format: a leading alphanumeric, followed by zero or more alphanumerics, underscores, spaces, backslashes, or hyphens in any order). No trailing spaces allowed.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetLogAnalyticsLogGroupsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logAnalyticsLogGroupSummaryCollections")
    def log_analytics_log_group_summary_collections(self) -> Sequence['outputs.GetLogAnalyticsLogGroupsLogAnalyticsLogGroupSummaryCollectionResult']:
        """
        The list of log_analytics_log_group_summary_collection.
        """
        return pulumi.get(self, "log_analytics_log_group_summary_collections")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")


class AwaitableGetLogAnalyticsLogGroupsResult(GetLogAnalyticsLogGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogAnalyticsLogGroupsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            log_analytics_log_group_summary_collections=self.log_analytics_log_group_summary_collections,
            namespace=self.namespace)


def get_log_analytics_log_groups(compartment_id: Optional[str] = None,
                                 display_name: Optional[str] = None,
                                 filters: Optional[Sequence[pulumi.InputType['GetLogAnalyticsLogGroupsFilterArgs']]] = None,
                                 namespace: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogAnalyticsLogGroupsResult:
    """
    This data source provides the list of Log Analytics Log Groups in Oracle Cloud Infrastructure Log Analytics service.

    Returns a list of log groups in a compartment. You may limit the number of log groups, provide sorting options, and filter the results by specifying a display name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_log_analytics_log_groups = oci.LogAnalytics.get_log_analytics_log_groups(compartment_id=compartment_id,
        namespace=log_analytics_log_group_namespace,
        display_name=log_analytics_log_group_display_name)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only log analytics log groups whose displayName matches the entire display name given. The match is case-insensitive.
    :param str namespace: The Logging Analytics namespace used for the request.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['namespace'] = namespace
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LogAnalytics/getLogAnalyticsLogGroups:getLogAnalyticsLogGroups', __args__, opts=opts, typ=GetLogAnalyticsLogGroupsResult).value

    return AwaitableGetLogAnalyticsLogGroupsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        log_analytics_log_group_summary_collections=pulumi.get(__ret__, 'log_analytics_log_group_summary_collections'),
        namespace=pulumi.get(__ret__, 'namespace'))


@_utilities.lift_output_func(get_log_analytics_log_groups)
def get_log_analytics_log_groups_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                        display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                        filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetLogAnalyticsLogGroupsFilterArgs']]]]] = None,
                                        namespace: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLogAnalyticsLogGroupsResult]:
    """
    This data source provides the list of Log Analytics Log Groups in Oracle Cloud Infrastructure Log Analytics service.

    Returns a list of log groups in a compartment. You may limit the number of log groups, provide sorting options, and filter the results by specifying a display name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_log_analytics_log_groups = oci.LogAnalytics.get_log_analytics_log_groups(compartment_id=compartment_id,
        namespace=log_analytics_log_group_namespace,
        display_name=log_analytics_log_group_display_name)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only log analytics log groups whose displayName matches the entire display name given. The match is case-insensitive.
    :param str namespace: The Logging Analytics namespace used for the request.
    """
    ...
