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
    'GetHttpMonitorResult',
    'AwaitableGetHttpMonitorResult',
    'get_http_monitor',
    'get_http_monitor_output',
]

@pulumi.output_type
class GetHttpMonitorResult:
    """
    A collection of values returned by getHttpMonitor.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, display_name=None, freeform_tags=None, headers=None, home_region=None, id=None, interval_in_seconds=None, is_enabled=None, method=None, monitor_id=None, path=None, port=None, protocol=None, results_url=None, targets=None, time_created=None, timeout_in_seconds=None, vantage_point_names=None):
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
        if headers and not isinstance(headers, dict):
            raise TypeError("Expected argument 'headers' to be a dict")
        pulumi.set(__self__, "headers", headers)
        if home_region and not isinstance(home_region, str):
            raise TypeError("Expected argument 'home_region' to be a str")
        pulumi.set(__self__, "home_region", home_region)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interval_in_seconds and not isinstance(interval_in_seconds, int):
            raise TypeError("Expected argument 'interval_in_seconds' to be a int")
        pulumi.set(__self__, "interval_in_seconds", interval_in_seconds)
        if is_enabled and not isinstance(is_enabled, bool):
            raise TypeError("Expected argument 'is_enabled' to be a bool")
        pulumi.set(__self__, "is_enabled", is_enabled)
        if method and not isinstance(method, str):
            raise TypeError("Expected argument 'method' to be a str")
        pulumi.set(__self__, "method", method)
        if monitor_id and not isinstance(monitor_id, str):
            raise TypeError("Expected argument 'monitor_id' to be a str")
        pulumi.set(__self__, "monitor_id", monitor_id)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if results_url and not isinstance(results_url, str):
            raise TypeError("Expected argument 'results_url' to be a str")
        pulumi.set(__self__, "results_url", results_url)
        if targets and not isinstance(targets, list):
            raise TypeError("Expected argument 'targets' to be a list")
        pulumi.set(__self__, "targets", targets)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if timeout_in_seconds and not isinstance(timeout_in_seconds, int):
            raise TypeError("Expected argument 'timeout_in_seconds' to be a int")
        pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)
        if vantage_point_names and not isinstance(vantage_point_names, list):
            raise TypeError("Expected argument 'vantage_point_names' to be a list")
        pulumi.set(__self__, "vantage_point_names", vantage_point_names)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly and mutable name suitable for display in a user interface.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.  For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def headers(self) -> Mapping[str, Any]:
        """
        A dictionary of HTTP request headers.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter(name="homeRegion")
    def home_region(self) -> str:
        """
        The region where updates must be made and where results must be fetched from.
        """
        return pulumi.get(self, "home_region")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="intervalInSeconds")
    def interval_in_seconds(self) -> int:
        """
        The monitor interval in seconds. Valid values: 10, 30, and 60.
        """
        return pulumi.get(self, "interval_in_seconds")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> bool:
        """
        Enables or disables the monitor. Set to 'true' to launch monitoring.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter
    def method(self) -> str:
        """
        The supported HTTP methods available for probes.
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter(name="monitorId")
    def monitor_id(self) -> str:
        return pulumi.get(self, "monitor_id")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        The optional URL path to probe, including query parameters.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The port on which to probe endpoints. If unspecified, probes will use the default port of their protocol.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        The supported protocols available for HTTP probes.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="resultsUrl")
    def results_url(self) -> str:
        """
        A URL for fetching the probe results.
        """
        return pulumi.get(self, "results_url")

    @property
    @pulumi.getter
    def targets(self) -> Sequence[str]:
        """
        A list of targets (hostnames or IP addresses) of the probe.
        """
        return pulumi.get(self, "targets")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The RFC 3339-formatted creation date and time of the probe.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> int:
        """
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60. The probe timeout must be less than or equal to `intervalInSeconds` for monitors.
        """
        return pulumi.get(self, "timeout_in_seconds")

    @property
    @pulumi.getter(name="vantagePointNames")
    def vantage_point_names(self) -> Sequence[str]:
        """
        A list of names of vantage points from which to execute the probe.
        """
        return pulumi.get(self, "vantage_point_names")


class AwaitableGetHttpMonitorResult(GetHttpMonitorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHttpMonitorResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            headers=self.headers,
            home_region=self.home_region,
            id=self.id,
            interval_in_seconds=self.interval_in_seconds,
            is_enabled=self.is_enabled,
            method=self.method,
            monitor_id=self.monitor_id,
            path=self.path,
            port=self.port,
            protocol=self.protocol,
            results_url=self.results_url,
            targets=self.targets,
            time_created=self.time_created,
            timeout_in_seconds=self.timeout_in_seconds,
            vantage_point_names=self.vantage_point_names)


def get_http_monitor(monitor_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHttpMonitorResult:
    """
    This data source provides details about a specific Http Monitor resource in Oracle Cloud Infrastructure Health Checks service.

    Gets the configuration for the specified monitor.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_http_monitor = oci.HealthChecks.get_http_monitor(monitor_id=test_monitor["id"])
    ```


    :param str monitor_id: The OCID of a monitor.
    """
    __args__ = dict()
    __args__['monitorId'] = monitor_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:HealthChecks/getHttpMonitor:getHttpMonitor', __args__, opts=opts, typ=GetHttpMonitorResult).value

    return AwaitableGetHttpMonitorResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        headers=pulumi.get(__ret__, 'headers'),
        home_region=pulumi.get(__ret__, 'home_region'),
        id=pulumi.get(__ret__, 'id'),
        interval_in_seconds=pulumi.get(__ret__, 'interval_in_seconds'),
        is_enabled=pulumi.get(__ret__, 'is_enabled'),
        method=pulumi.get(__ret__, 'method'),
        monitor_id=pulumi.get(__ret__, 'monitor_id'),
        path=pulumi.get(__ret__, 'path'),
        port=pulumi.get(__ret__, 'port'),
        protocol=pulumi.get(__ret__, 'protocol'),
        results_url=pulumi.get(__ret__, 'results_url'),
        targets=pulumi.get(__ret__, 'targets'),
        time_created=pulumi.get(__ret__, 'time_created'),
        timeout_in_seconds=pulumi.get(__ret__, 'timeout_in_seconds'),
        vantage_point_names=pulumi.get(__ret__, 'vantage_point_names'))


@_utilities.lift_output_func(get_http_monitor)
def get_http_monitor_output(monitor_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHttpMonitorResult]:
    """
    This data source provides details about a specific Http Monitor resource in Oracle Cloud Infrastructure Health Checks service.

    Gets the configuration for the specified monitor.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_http_monitor = oci.HealthChecks.get_http_monitor(monitor_id=test_monitor["id"])
    ```


    :param str monitor_id: The OCID of a monitor.
    """
    ...
