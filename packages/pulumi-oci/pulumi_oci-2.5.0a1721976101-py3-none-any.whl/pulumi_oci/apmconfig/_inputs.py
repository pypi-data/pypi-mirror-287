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
    'ConfigDimensionArgs',
    'ConfigInUseByArgs',
    'ConfigMetricArgs',
    'ConfigRuleArgs',
    'GetConfigsFilterArgs',
]

@pulumi.input_type
class ConfigDimensionArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 value_source: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: (Updatable) The name of the dimension.
        :param pulumi.Input[str] value_source: (Updatable) The source to populate the dimension. This must not be specified.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value_source is not None:
            pulumi.set(__self__, "value_source", value_source)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The name of the dimension.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="valueSource")
    def value_source(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The source to populate the dimension. This must not be specified.
        """
        return pulumi.get(self, "value_source")

    @value_source.setter
    def value_source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value_source", value)


@pulumi.input_type
class ConfigInUseByArgs:
    def __init__(__self__, *,
                 config_type: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 options_group: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] config_type: (Updatable) The type of configuration item.
        :param pulumi.Input[str] display_name: (Updatable) The name by which a configuration entity is displayed to the end user.
        :param pulumi.Input[str] id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration item. An OCID is generated when the item is created.
        :param pulumi.Input[str] options_group: A string that specifies the group that an OPTIONS item belongs to.
        """
        if config_type is not None:
            pulumi.set(__self__, "config_type", config_type)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if options_group is not None:
            pulumi.set(__self__, "options_group", options_group)

    @property
    @pulumi.getter(name="configType")
    def config_type(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The type of configuration item.
        """
        return pulumi.get(self, "config_type")

    @config_type.setter
    def config_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_type", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The name by which a configuration entity is displayed to the end user.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the configuration item. An OCID is generated when the item is created.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="optionsGroup")
    def options_group(self) -> Optional[pulumi.Input[str]]:
        """
        A string that specifies the group that an OPTIONS item belongs to.
        """
        return pulumi.get(self, "options_group")

    @options_group.setter
    def options_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "options_group", value)


@pulumi.input_type
class ConfigMetricArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 unit: Optional[pulumi.Input[str]] = None,
                 value_source: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] description: (Updatable) A description of the metric.
        :param pulumi.Input[str] name: (Updatable) The name of the metric. This must be a known metric name.
        :param pulumi.Input[str] unit: (Updatable) The unit of the metric.
        :param pulumi.Input[str] value_source: (Updatable) This must not be set.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if unit is not None:
            pulumi.set(__self__, "unit", unit)
        if value_source is not None:
            pulumi.set(__self__, "value_source", value_source)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) A description of the metric.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The name of the metric. This must be a known metric name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The unit of the metric.
        """
        return pulumi.get(self, "unit")

    @unit.setter
    def unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unit", value)

    @property
    @pulumi.getter(name="valueSource")
    def value_source(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) This must not be set.
        """
        return pulumi.get(self, "value_source")

    @value_source.setter
    def value_source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value_source", value)


@pulumi.input_type
class ConfigRuleArgs:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 filter_text: Optional[pulumi.Input[str]] = None,
                 is_apply_to_error_spans: Optional[pulumi.Input[bool]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 satisfied_response_time: Optional[pulumi.Input[int]] = None,
                 tolerating_response_time: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] display_name: (Updatable) The name by which a configuration entity is displayed to the end user.
        :param pulumi.Input[str] filter_text: (Updatable) The string that defines the Span Filter expression.
        :param pulumi.Input[bool] is_apply_to_error_spans: (Updatable) Specifies whether an Apdex score should be computed for error spans. Setting it to "true" means that the Apdex score is computed in the usual way. Setting it to "false" skips the Apdex computation and sets the Apdex score to "frustrating" regardless of the configured thresholds. The default is "false".
        :param pulumi.Input[bool] is_enabled: (Updatable) Specifies whether the Apdex score should be computed for spans matching the rule. This can be used to disable Apdex score for spans that do not need or require it. The default is "true".
        :param pulumi.Input[int] priority: (Updatable) The priority controls the order in which multiple rules in a rule set are applied. Lower values indicate higher priorities. Rules with higher priority are applied first, and once a match is found, the rest of the rules are ignored. Rules within the same rule set cannot have the same priority.
        :param pulumi.Input[int] satisfied_response_time: (Updatable) The maximum response time in milliseconds that is considered "satisfactory" for the end user.
        :param pulumi.Input[int] tolerating_response_time: (Updatable) The maximum response time in milliseconds that is considered "tolerable" for the end user. A response time beyond this threshold is considered "frustrating". This value cannot be lower than "satisfiedResponseTime". 
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if filter_text is not None:
            pulumi.set(__self__, "filter_text", filter_text)
        if is_apply_to_error_spans is not None:
            pulumi.set(__self__, "is_apply_to_error_spans", is_apply_to_error_spans)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if satisfied_response_time is not None:
            pulumi.set(__self__, "satisfied_response_time", satisfied_response_time)
        if tolerating_response_time is not None:
            pulumi.set(__self__, "tolerating_response_time", tolerating_response_time)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The name by which a configuration entity is displayed to the end user.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="filterText")
    def filter_text(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The string that defines the Span Filter expression.
        """
        return pulumi.get(self, "filter_text")

    @filter_text.setter
    def filter_text(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter_text", value)

    @property
    @pulumi.getter(name="isApplyToErrorSpans")
    def is_apply_to_error_spans(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Specifies whether an Apdex score should be computed for error spans. Setting it to "true" means that the Apdex score is computed in the usual way. Setting it to "false" skips the Apdex computation and sets the Apdex score to "frustrating" regardless of the configured thresholds. The default is "false".
        """
        return pulumi.get(self, "is_apply_to_error_spans")

    @is_apply_to_error_spans.setter
    def is_apply_to_error_spans(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_apply_to_error_spans", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Specifies whether the Apdex score should be computed for spans matching the rule. This can be used to disable Apdex score for spans that do not need or require it. The default is "true".
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The priority controls the order in which multiple rules in a rule set are applied. Lower values indicate higher priorities. Rules with higher priority are applied first, and once a match is found, the rest of the rules are ignored. Rules within the same rule set cannot have the same priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="satisfiedResponseTime")
    def satisfied_response_time(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The maximum response time in milliseconds that is considered "satisfactory" for the end user.
        """
        return pulumi.get(self, "satisfied_response_time")

    @satisfied_response_time.setter
    def satisfied_response_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "satisfied_response_time", value)

    @property
    @pulumi.getter(name="toleratingResponseTime")
    def tolerating_response_time(self) -> Optional[pulumi.Input[int]]:
        """
        (Updatable) The maximum response time in milliseconds that is considered "tolerable" for the end user. A response time beyond this threshold is considered "frustrating". This value cannot be lower than "satisfiedResponseTime". 


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "tolerating_response_time")

    @tolerating_response_time.setter
    def tolerating_response_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tolerating_response_time", value)


@pulumi.input_type
class GetConfigsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        """
        :param str name: The name of the metric. This must be a known metric name.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the metric. This must be a known metric name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


