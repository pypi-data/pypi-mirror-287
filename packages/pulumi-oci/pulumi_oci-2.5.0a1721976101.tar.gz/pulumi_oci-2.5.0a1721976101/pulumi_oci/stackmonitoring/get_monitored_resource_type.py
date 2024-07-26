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

__all__ = [
    'GetMonitoredResourceTypeResult',
    'AwaitableGetMonitoredResourceTypeResult',
    'get_monitored_resource_type',
    'get_monitored_resource_type_output',
]

@pulumi.output_type
class GetMonitoredResourceTypeResult:
    """
    A collection of values returned by getMonitoredResourceType.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, description=None, display_name=None, freeform_tags=None, id=None, metadatas=None, metric_namespace=None, monitored_resource_type_id=None, name=None, resource_category=None, source_type=None, state=None, system_tags=None, time_created=None, time_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadatas and not isinstance(metadatas, list):
            raise TypeError("Expected argument 'metadatas' to be a list")
        pulumi.set(__self__, "metadatas", metadatas)
        if metric_namespace and not isinstance(metric_namespace, str):
            raise TypeError("Expected argument 'metric_namespace' to be a str")
        pulumi.set(__self__, "metric_namespace", metric_namespace)
        if monitored_resource_type_id and not isinstance(monitored_resource_type_id, str):
            raise TypeError("Expected argument 'monitored_resource_type_id' to be a str")
        pulumi.set(__self__, "monitored_resource_type_id", monitored_resource_type_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_category and not isinstance(resource_category, str):
            raise TypeError("Expected argument 'resource_category' to be a str")
        pulumi.set(__self__, "resource_category", resource_category)
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        pulumi.set(__self__, "source_type", source_type)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the resource type.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A friendly description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Monitored resource type display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Monitored resource type identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metadatas(self) -> Sequence['outputs.GetMonitoredResourceTypeMetadataResult']:
        """
        The metadata details for resource type.
        """
        return pulumi.get(self, "metadatas")

    @property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> str:
        """
        Metric namespace for resource type.
        """
        return pulumi.get(self, "metric_namespace")

    @property
    @pulumi.getter(name="monitoredResourceTypeId")
    def monitored_resource_type_id(self) -> str:
        return pulumi.get(self, "monitored_resource_type_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique monitored resource type name. The name must be unique across tenancy.  Name can not be changed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceCategory")
    def resource_category(self) -> str:
        """
        Resource Category to indicate the kind of resource type.
        """
        return pulumi.get(self, "resource_category")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> str:
        """
        Source type to indicate if the resource is stack monitoring discovered, Oracle Cloud Infrastructure native resource, etc.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Lifecycle state of the monitored resource type.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time when the monitored resource type was created, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time when the monitored resource was updated, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetMonitoredResourceTypeResult(GetMonitoredResourceTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMonitoredResourceTypeResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            metadatas=self.metadatas,
            metric_namespace=self.metric_namespace,
            monitored_resource_type_id=self.monitored_resource_type_id,
            name=self.name,
            resource_category=self.resource_category,
            source_type=self.source_type,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_monitored_resource_type(monitored_resource_type_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMonitoredResourceTypeResult:
    """
    This data source provides details about a specific Monitored Resource Type resource in Oracle Cloud Infrastructure Stack Monitoring service.

    Gets a monitored resource type by identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_monitored_resource_type = oci.StackMonitoring.get_monitored_resource_type(monitored_resource_type_id=test_monitored_resource_type_oci_stack_monitoring_monitored_resource_type["id"])
    ```


    :param str monitored_resource_type_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of monitored resource type.
    """
    __args__ = dict()
    __args__['monitoredResourceTypeId'] = monitored_resource_type_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:StackMonitoring/getMonitoredResourceType:getMonitoredResourceType', __args__, opts=opts, typ=GetMonitoredResourceTypeResult).value

    return AwaitableGetMonitoredResourceTypeResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        metadatas=pulumi.get(__ret__, 'metadatas'),
        metric_namespace=pulumi.get(__ret__, 'metric_namespace'),
        monitored_resource_type_id=pulumi.get(__ret__, 'monitored_resource_type_id'),
        name=pulumi.get(__ret__, 'name'),
        resource_category=pulumi.get(__ret__, 'resource_category'),
        source_type=pulumi.get(__ret__, 'source_type'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_monitored_resource_type)
def get_monitored_resource_type_output(monitored_resource_type_id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMonitoredResourceTypeResult]:
    """
    This data source provides details about a specific Monitored Resource Type resource in Oracle Cloud Infrastructure Stack Monitoring service.

    Gets a monitored resource type by identifier [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_monitored_resource_type = oci.StackMonitoring.get_monitored_resource_type(monitored_resource_type_id=test_monitored_resource_type_oci_stack_monitoring_monitored_resource_type["id"])
    ```


    :param str monitored_resource_type_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of monitored resource type.
    """
    ...
