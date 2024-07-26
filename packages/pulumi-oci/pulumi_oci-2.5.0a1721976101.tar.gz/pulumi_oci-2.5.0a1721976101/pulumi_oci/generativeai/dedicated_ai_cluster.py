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

__all__ = ['DedicatedAiClusterArgs', 'DedicatedAiCluster']

@pulumi.input_type
class DedicatedAiClusterArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 unit_count: pulumi.Input[int],
                 unit_shape: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a DedicatedAiCluster resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The compartment OCID to create the dedicated AI cluster in.
        :param pulumi.Input[str] type: The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.
               
               Allowed values are:
               * HOSTING
               * FINE_TUNING
        :param pulumi.Input[int] unit_count: (Updatable) The number of dedicated units in this AI cluster.
        :param pulumi.Input[str] unit_shape: The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.
               
               Allowed values are:
               * LARGE_COHERE
               * LARGE_COHERE_V2
               * SMALL_COHERE
               * SMALL_COHERE_V2
               * EMBED_COHERE
               * LLAMA2_70
               * LARGE_GENERIC
               * LARGE_COHERE_V2_2
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] description: (Updatable) An optional description of the dedicated AI cluster.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name. Does not have to be unique, and it's changeable.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "unit_count", unit_count)
        pulumi.set(__self__, "unit_shape", unit_shape)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) The compartment OCID to create the dedicated AI cluster in.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.

        Allowed values are:
        * HOSTING
        * FINE_TUNING
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="unitCount")
    def unit_count(self) -> pulumi.Input[int]:
        """
        (Updatable) The number of dedicated units in this AI cluster.
        """
        return pulumi.get(self, "unit_count")

    @unit_count.setter
    def unit_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "unit_count", value)

    @property
    @pulumi.getter(name="unitShape")
    def unit_shape(self) -> pulumi.Input[str]:
        """
        The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.

        Allowed values are:
        * LARGE_COHERE
        * LARGE_COHERE_V2
        * SMALL_COHERE
        * SMALL_COHERE_V2
        * EMBED_COHERE
        * LLAMA2_70
        * LARGE_GENERIC
        * LARGE_COHERE_V2_2


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "unit_shape")

    @unit_shape.setter
    def unit_shape(self, value: pulumi.Input[str]):
        pulumi.set(self, "unit_shape", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) An optional description of the dedicated AI cluster.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user-friendly name. Does not have to be unique, and it's changeable.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)


@pulumi.input_type
class _DedicatedAiClusterState:
    def __init__(__self__, *,
                 capacities: Optional[pulumi.Input[Sequence[pulumi.Input['DedicatedAiClusterCapacityArgs']]]] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 unit_count: Optional[pulumi.Input[int]] = None,
                 unit_shape: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DedicatedAiCluster resources.
        :param pulumi.Input[Sequence[pulumi.Input['DedicatedAiClusterCapacityArgs']]] capacities: The total capacity for a dedicated AI cluster.
        :param pulumi.Input[str] compartment_id: (Updatable) The compartment OCID to create the dedicated AI cluster in.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] description: (Updatable) An optional description of the dedicated AI cluster.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name. Does not have to be unique, and it's changeable.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state with detail that can provide actionable information.
        :param pulumi.Input[str] state: The current state of the dedicated AI cluster.
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time the dedicated AI cluster was created, in the format defined by RFC 3339
        :param pulumi.Input[str] time_updated: The date and time the dedicated AI cluster was updated, in the format defined by RFC 3339
        :param pulumi.Input[str] type: The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.
               
               Allowed values are:
               * HOSTING
               * FINE_TUNING
        :param pulumi.Input[int] unit_count: (Updatable) The number of dedicated units in this AI cluster.
        :param pulumi.Input[str] unit_shape: The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.
               
               Allowed values are:
               * LARGE_COHERE
               * LARGE_COHERE_V2
               * SMALL_COHERE
               * SMALL_COHERE_V2
               * EMBED_COHERE
               * LLAMA2_70
               * LARGE_GENERIC
               * LARGE_COHERE_V2_2
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if capacities is not None:
            pulumi.set(__self__, "capacities", capacities)
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
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if system_tags is not None:
            pulumi.set(__self__, "system_tags", system_tags)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if unit_count is not None:
            pulumi.set(__self__, "unit_count", unit_count)
        if unit_shape is not None:
            pulumi.set(__self__, "unit_shape", unit_shape)

    @property
    @pulumi.getter
    def capacities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DedicatedAiClusterCapacityArgs']]]]:
        """
        The total capacity for a dedicated AI cluster.
        """
        return pulumi.get(self, "capacities")

    @capacities.setter
    def capacities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DedicatedAiClusterCapacityArgs']]]]):
        pulumi.set(self, "capacities", value)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The compartment OCID to create the dedicated AI cluster in.
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) An optional description of the dedicated AI cluster.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A user-friendly name. Does not have to be unique, and it's changeable.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state with detail that can provide actionable information.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the dedicated AI cluster.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @system_tags.setter
    def system_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "system_tags", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the dedicated AI cluster was created, in the format defined by RFC 3339
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the dedicated AI cluster was updated, in the format defined by RFC 3339
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.

        Allowed values are:
        * HOSTING
        * FINE_TUNING
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="unitCount")
    def unit_count(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The number of dedicated units in this AI cluster.
        """
        return pulumi.get(self, "unit_count")

    @unit_count.setter
    def unit_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "unit_count", value)

    @property
    @pulumi.getter(name="unitShape")
    def unit_shape(self) -> Optional[pulumi.Input[str]]:
        """
        The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.

        Allowed values are:
        * LARGE_COHERE
        * LARGE_COHERE_V2
        * SMALL_COHERE
        * SMALL_COHERE_V2
        * EMBED_COHERE
        * LLAMA2_70
        * LARGE_GENERIC
        * LARGE_COHERE_V2_2


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "unit_shape")

    @unit_shape.setter
    def unit_shape(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unit_shape", value)


class DedicatedAiCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 unit_count: Optional[pulumi.Input[int]] = None,
                 unit_shape: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Dedicated Ai Cluster resource in Oracle Cloud Infrastructure Generative AI service.

        Creates a dedicated AI cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_dedicated_ai_cluster = oci.generative_ai.DedicatedAiCluster("test_dedicated_ai_cluster",
            compartment_id=compartment_id,
            type=dedicated_ai_cluster_type,
            unit_count=dedicated_ai_cluster_unit_count,
            unit_shape=dedicated_ai_cluster_unit_shape,
            defined_tags={
                "Operations.CostCenter": "42",
            },
            description=dedicated_ai_cluster_description,
            display_name=dedicated_ai_cluster_display_name,
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        DedicatedAiClusters can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:GenerativeAi/dedicatedAiCluster:DedicatedAiCluster test_dedicated_ai_cluster "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) The compartment OCID to create the dedicated AI cluster in.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] description: (Updatable) An optional description of the dedicated AI cluster.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name. Does not have to be unique, and it's changeable.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] type: The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.
               
               Allowed values are:
               * HOSTING
               * FINE_TUNING
        :param pulumi.Input[int] unit_count: (Updatable) The number of dedicated units in this AI cluster.
        :param pulumi.Input[str] unit_shape: The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.
               
               Allowed values are:
               * LARGE_COHERE
               * LARGE_COHERE_V2
               * SMALL_COHERE
               * SMALL_COHERE_V2
               * EMBED_COHERE
               * LLAMA2_70
               * LARGE_GENERIC
               * LARGE_COHERE_V2_2
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DedicatedAiClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Dedicated Ai Cluster resource in Oracle Cloud Infrastructure Generative AI service.

        Creates a dedicated AI cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_dedicated_ai_cluster = oci.generative_ai.DedicatedAiCluster("test_dedicated_ai_cluster",
            compartment_id=compartment_id,
            type=dedicated_ai_cluster_type,
            unit_count=dedicated_ai_cluster_unit_count,
            unit_shape=dedicated_ai_cluster_unit_shape,
            defined_tags={
                "Operations.CostCenter": "42",
            },
            description=dedicated_ai_cluster_description,
            display_name=dedicated_ai_cluster_display_name,
            freeform_tags={
                "Department": "Finance",
            })
        ```

        ## Import

        DedicatedAiClusters can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:GenerativeAi/dedicatedAiCluster:DedicatedAiCluster test_dedicated_ai_cluster "id"
        ```

        :param str resource_name: The name of the resource.
        :param DedicatedAiClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DedicatedAiClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 type: Optional[pulumi.Input[str]] = None,
                 unit_count: Optional[pulumi.Input[int]] = None,
                 unit_shape: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DedicatedAiClusterArgs.__new__(DedicatedAiClusterArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if unit_count is None and not opts.urn:
                raise TypeError("Missing required property 'unit_count'")
            __props__.__dict__["unit_count"] = unit_count
            if unit_shape is None and not opts.urn:
                raise TypeError("Missing required property 'unit_shape'")
            __props__.__dict__["unit_shape"] = unit_shape
            __props__.__dict__["capacities"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(DedicatedAiCluster, __self__).__init__(
            'oci:GenerativeAi/dedicatedAiCluster:DedicatedAiCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            capacities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DedicatedAiClusterCapacityArgs']]]]] = None,
            compartment_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            unit_count: Optional[pulumi.Input[int]] = None,
            unit_shape: Optional[pulumi.Input[str]] = None) -> 'DedicatedAiCluster':
        """
        Get an existing DedicatedAiCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DedicatedAiClusterCapacityArgs']]]] capacities: The total capacity for a dedicated AI cluster.
        :param pulumi.Input[str] compartment_id: (Updatable) The compartment OCID to create the dedicated AI cluster in.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] description: (Updatable) An optional description of the dedicated AI cluster.
        :param pulumi.Input[str] display_name: (Updatable) A user-friendly name. Does not have to be unique, and it's changeable.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state with detail that can provide actionable information.
        :param pulumi.Input[str] state: The current state of the dedicated AI cluster.
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time the dedicated AI cluster was created, in the format defined by RFC 3339
        :param pulumi.Input[str] time_updated: The date and time the dedicated AI cluster was updated, in the format defined by RFC 3339
        :param pulumi.Input[str] type: The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.
               
               Allowed values are:
               * HOSTING
               * FINE_TUNING
        :param pulumi.Input[int] unit_count: (Updatable) The number of dedicated units in this AI cluster.
        :param pulumi.Input[str] unit_shape: The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.
               
               Allowed values are:
               * LARGE_COHERE
               * LARGE_COHERE_V2
               * SMALL_COHERE
               * SMALL_COHERE_V2
               * EMBED_COHERE
               * LLAMA2_70
               * LARGE_GENERIC
               * LARGE_COHERE_V2_2
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DedicatedAiClusterState.__new__(_DedicatedAiClusterState)

        __props__.__dict__["capacities"] = capacities
        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        __props__.__dict__["type"] = type
        __props__.__dict__["unit_count"] = unit_count
        __props__.__dict__["unit_shape"] = unit_shape
        return DedicatedAiCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def capacities(self) -> pulumi.Output[Sequence['outputs.DedicatedAiClusterCapacity']]:
        """
        The total capacity for a dedicated AI cluster.
        """
        return pulumi.get(self, "capacities")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) The compartment OCID to create the dedicated AI cluster in.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        (Updatable) An optional description of the dedicated AI cluster.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) A user-friendly name. Does not have to be unique, and it's changeable.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state with detail that can provide actionable information.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the dedicated AI cluster.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the dedicated AI cluster was created, in the format defined by RFC 3339
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The date and time the dedicated AI cluster was updated, in the format defined by RFC 3339
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The dedicated AI cluster type indicating whether this is a fine-tuning/training processor or hosting/inference processor.

        Allowed values are:
        * HOSTING
        * FINE_TUNING
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="unitCount")
    def unit_count(self) -> pulumi.Output[int]:
        """
        (Updatable) The number of dedicated units in this AI cluster.
        """
        return pulumi.get(self, "unit_count")

    @property
    @pulumi.getter(name="unitShape")
    def unit_shape(self) -> pulumi.Output[str]:
        """
        The shape of dedicated unit in this AI cluster. The underlying hardware configuration is hidden from customers.

        Allowed values are:
        * LARGE_COHERE
        * LARGE_COHERE_V2
        * SMALL_COHERE
        * SMALL_COHERE_V2
        * EMBED_COHERE
        * LLAMA2_70
        * LARGE_GENERIC
        * LARGE_COHERE_V2_2


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "unit_shape")

