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

__all__ = ['MonitoredResourceTypeArgs', 'MonitoredResourceType']

@pulumi.input_type
class MonitoredResourceTypeArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 metadata: Optional[pulumi.Input['MonitoredResourceTypeMetadataArgs']] = None,
                 metric_namespace: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_category: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MonitoredResourceType resource.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the resource type.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A friendly description.
        :param pulumi.Input[str] display_name: (Updatable) Monitored resource type display name.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input['MonitoredResourceTypeMetadataArgs'] metadata: (Updatable) The metadata details for resource type.
        :param pulumi.Input[str] metric_namespace: (Updatable) Metric namespace for resource type.
        :param pulumi.Input[str] name: A unique monitored resource type name. The name must be unique across tenancy.  Name can not be changed.
        :param pulumi.Input[str] resource_category: (Updatable) Resource Category to indicate the kind of resource type.
        :param pulumi.Input[str] source_type: (Updatable) Source type to indicate if the resource is stack monitoring discovered, Oracle Cloud Infrastructure native resource, etc. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if metric_namespace is not None:
            pulumi.set(__self__, "metric_namespace", metric_namespace)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_category is not None:
            pulumi.set(__self__, "resource_category", resource_category)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the resource type.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A friendly description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Monitored resource type display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['MonitoredResourceTypeMetadataArgs']]:
        """
        (Updatable) The metadata details for resource type.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['MonitoredResourceTypeMetadataArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Metric namespace for resource type.
        """
        return pulumi.get(self, "metric_namespace")

    @metric_namespace.setter
    def metric_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_namespace", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique monitored resource type name. The name must be unique across tenancy.  Name can not be changed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceCategory")
    def resource_category(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Resource Category to indicate the kind of resource type.
        """
        return pulumi.get(self, "resource_category")

    @resource_category.setter
    def resource_category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_category", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Source type to indicate if the resource is stack monitoring discovered, Oracle Cloud Infrastructure native resource, etc. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_type", value)


@pulumi.input_type
class _MonitoredResourceTypeState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 metadata: Optional[pulumi.Input['MonitoredResourceTypeMetadataArgs']] = None,
                 metric_namespace: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_category: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MonitoredResourceType resources.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the resource type.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A friendly description.
        :param pulumi.Input[str] display_name: (Updatable) Monitored resource type display name.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input['MonitoredResourceTypeMetadataArgs'] metadata: (Updatable) The metadata details for resource type.
        :param pulumi.Input[str] metric_namespace: (Updatable) Metric namespace for resource type.
        :param pulumi.Input[str] name: A unique monitored resource type name. The name must be unique across tenancy.  Name can not be changed.
        :param pulumi.Input[str] resource_category: (Updatable) Resource Category to indicate the kind of resource type.
        :param pulumi.Input[str] source_type: (Updatable) Source type to indicate if the resource is stack monitoring discovered, Oracle Cloud Infrastructure native resource, etc. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: Lifecycle state of the monitored resource type.
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time when the monitored resource type was created, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        :param pulumi.Input[str] time_updated: The date and time when the monitored resource was updated, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if metric_namespace is not None:
            pulumi.set(__self__, "metric_namespace", metric_namespace)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_category is not None:
            pulumi.set(__self__, "resource_category", resource_category)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if system_tags is not None:
            pulumi.set(__self__, "system_tags", system_tags)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the resource type.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A friendly description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Monitored resource type display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['MonitoredResourceTypeMetadataArgs']]:
        """
        (Updatable) The metadata details for resource type.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['MonitoredResourceTypeMetadataArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Metric namespace for resource type.
        """
        return pulumi.get(self, "metric_namespace")

    @metric_namespace.setter
    def metric_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_namespace", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A unique monitored resource type name. The name must be unique across tenancy.  Name can not be changed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceCategory")
    def resource_category(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Resource Category to indicate the kind of resource type.
        """
        return pulumi.get(self, "resource_category")

    @resource_category.setter
    def resource_category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_category", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Source type to indicate if the resource is stack monitoring discovered, Oracle Cloud Infrastructure native resource, etc. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        Lifecycle state of the monitored resource type.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @system_tags.setter
    def system_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "system_tags", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time when the monitored resource type was created, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time when the monitored resource was updated, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class MonitoredResourceType(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['MonitoredResourceTypeMetadataArgs']]] = None,
                 metric_namespace: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_category: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Monitored Resource Type resource in Oracle Cloud Infrastructure Stack Monitoring service.

        Creates a new monitored resource type.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_monitored_resource_type = oci.stack_monitoring.MonitoredResourceType("test_monitored_resource_type",
            compartment_id=compartment_id,
            name=monitored_resource_type_name,
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=monitored_resource_type_description,
            display_name=monitored_resource_type_display_name,
            freeform_tags={
                "bar-key": "value",
            },
            metadata=oci.stack_monitoring.MonitoredResourceTypeMetadataArgs(
                format=monitored_resource_type_metadata_format,
                agent_properties=monitored_resource_type_metadata_agent_properties,
                required_properties=monitored_resource_type_metadata_required_properties,
                unique_property_sets=[oci.stack_monitoring.MonitoredResourceTypeMetadataUniquePropertySetArgs(
                    properties=monitored_resource_type_metadata_unique_property_sets_properties,
                )],
                valid_properties_for_creates=monitored_resource_type_metadata_valid_properties_for_create,
                valid_properties_for_updates=monitored_resource_type_metadata_valid_properties_for_update,
                valid_property_values=monitored_resource_type_metadata_valid_property_values,
            ),
            metric_namespace=monitored_resource_type_metric_namespace,
            resource_category=monitored_resource_type_resource_category,
            source_type=monitored_resource_type_source_type)
        ```

        ## Import

        MonitoredResourceTypes can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:StackMonitoring/monitoredResourceType:MonitoredResourceType test_monitored_resource_type "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the resource type.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A friendly description.
        :param pulumi.Input[str] display_name: (Updatable) Monitored resource type display name.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[pulumi.InputType['MonitoredResourceTypeMetadataArgs']] metadata: (Updatable) The metadata details for resource type.
        :param pulumi.Input[str] metric_namespace: (Updatable) Metric namespace for resource type.
        :param pulumi.Input[str] name: A unique monitored resource type name. The name must be unique across tenancy.  Name can not be changed.
        :param pulumi.Input[str] resource_category: (Updatable) Resource Category to indicate the kind of resource type.
        :param pulumi.Input[str] source_type: (Updatable) Source type to indicate if the resource is stack monitoring discovered, Oracle Cloud Infrastructure native resource, etc. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MonitoredResourceTypeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Monitored Resource Type resource in Oracle Cloud Infrastructure Stack Monitoring service.

        Creates a new monitored resource type.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_monitored_resource_type = oci.stack_monitoring.MonitoredResourceType("test_monitored_resource_type",
            compartment_id=compartment_id,
            name=monitored_resource_type_name,
            defined_tags={
                "foo-namespace.bar-key": "value",
            },
            description=monitored_resource_type_description,
            display_name=monitored_resource_type_display_name,
            freeform_tags={
                "bar-key": "value",
            },
            metadata=oci.stack_monitoring.MonitoredResourceTypeMetadataArgs(
                format=monitored_resource_type_metadata_format,
                agent_properties=monitored_resource_type_metadata_agent_properties,
                required_properties=monitored_resource_type_metadata_required_properties,
                unique_property_sets=[oci.stack_monitoring.MonitoredResourceTypeMetadataUniquePropertySetArgs(
                    properties=monitored_resource_type_metadata_unique_property_sets_properties,
                )],
                valid_properties_for_creates=monitored_resource_type_metadata_valid_properties_for_create,
                valid_properties_for_updates=monitored_resource_type_metadata_valid_properties_for_update,
                valid_property_values=monitored_resource_type_metadata_valid_property_values,
            ),
            metric_namespace=monitored_resource_type_metric_namespace,
            resource_category=monitored_resource_type_resource_category,
            source_type=monitored_resource_type_source_type)
        ```

        ## Import

        MonitoredResourceTypes can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:StackMonitoring/monitoredResourceType:MonitoredResourceType test_monitored_resource_type "id"
        ```

        :param str resource_name: The name of the resource.
        :param MonitoredResourceTypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MonitoredResourceTypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['MonitoredResourceTypeMetadataArgs']]] = None,
                 metric_namespace: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_category: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MonitoredResourceTypeArgs.__new__(MonitoredResourceTypeArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["metric_namespace"] = metric_namespace
            __props__.__dict__["name"] = name
            __props__.__dict__["resource_category"] = resource_category
            __props__.__dict__["source_type"] = source_type
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(MonitoredResourceType, __self__).__init__(
            'oci:StackMonitoring/monitoredResourceType:MonitoredResourceType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            metadata: Optional[pulumi.Input[pulumi.InputType['MonitoredResourceTypeMetadataArgs']]] = None,
            metric_namespace: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_category: Optional[pulumi.Input[str]] = None,
            source_type: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'MonitoredResourceType':
        """
        Get an existing MonitoredResourceType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the resource type.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) A friendly description.
        :param pulumi.Input[str] display_name: (Updatable) Monitored resource type display name.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        :param pulumi.Input[pulumi.InputType['MonitoredResourceTypeMetadataArgs']] metadata: (Updatable) The metadata details for resource type.
        :param pulumi.Input[str] metric_namespace: (Updatable) Metric namespace for resource type.
        :param pulumi.Input[str] name: A unique monitored resource type name. The name must be unique across tenancy.  Name can not be changed.
        :param pulumi.Input[str] resource_category: (Updatable) Resource Category to indicate the kind of resource type.
        :param pulumi.Input[str] source_type: (Updatable) Source type to indicate if the resource is stack monitoring discovered, Oracle Cloud Infrastructure native resource, etc. 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: Lifecycle state of the monitored resource type.
        :param pulumi.Input[Mapping[str, Any]] system_tags: Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time when the monitored resource type was created, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        :param pulumi.Input[str] time_updated: The date and time when the monitored resource was updated, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MonitoredResourceTypeState.__new__(_MonitoredResourceTypeState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["metric_namespace"] = metric_namespace
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_category"] = resource_category
        __props__.__dict__["source_type"] = source_type
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return MonitoredResourceType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the resource type.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        (Updatable) A friendly description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        (Updatable) Monitored resource type display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.MonitoredResourceTypeMetadata']:
        """
        (Updatable) The metadata details for resource type.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> pulumi.Output[str]:
        """
        (Updatable) Metric namespace for resource type.
        """
        return pulumi.get(self, "metric_namespace")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique monitored resource type name. The name must be unique across tenancy.  Name can not be changed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceCategory")
    def resource_category(self) -> pulumi.Output[str]:
        """
        (Updatable) Resource Category to indicate the kind of resource type.
        """
        return pulumi.get(self, "resource_category")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[str]:
        """
        (Updatable) Source type to indicate if the resource is stack monitoring discovered, Oracle Cloud Infrastructure native resource, etc. 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Lifecycle state of the monitored resource type.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time when the monitored resource type was created, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The date and time when the monitored resource was updated, expressed in  [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.
        """
        return pulumi.get(self, "time_updated")

