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

__all__ = ['ResponderRecipeArgs', 'ResponderRecipe']

@pulumi.input_type
class ResponderRecipeArgs:
    def __init__(__self__, *,
                 compartment_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 source_responder_recipe_id: pulumi.Input[str],
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 responder_rules: Optional[pulumi.Input[Sequence[pulumi.Input['ResponderRecipeResponderRuleArgs']]]] = None):
        """
        The set of arguments for constructing a ResponderRecipe resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment OCID
        :param pulumi.Input[str] display_name: (Updatable) Responder recipe display name.
               
               Avoid entering confidential information.
        :param pulumi.Input[str] source_responder_recipe_id: The unique identifier of the source responder recipe
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) Responder recipe description.
               
               Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
               
               Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input['ResponderRecipeResponderRuleArgs']]] responder_rules: (Updatable) List of responder rules to override from source responder recipe
        """
        pulumi.set(__self__, "compartment_id", compartment_id)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "source_responder_recipe_id", source_responder_recipe_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if responder_rules is not None:
            pulumi.set(__self__, "responder_rules", responder_rules)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Input[str]:
        """
        (Updatable) Compartment OCID
        """
        return pulumi.get(self, "compartment_id")

    @compartment_id.setter
    def compartment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compartment_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        (Updatable) Responder recipe display name.

        Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="sourceResponderRecipeId")
    def source_responder_recipe_id(self) -> pulumi.Input[str]:
        """
        The unique identifier of the source responder recipe


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "source_responder_recipe_id")

    @source_responder_recipe_id.setter
    def source_responder_recipe_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_responder_recipe_id", value)

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
        (Updatable) Responder recipe description.

        Avoid entering confidential information.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`

        Avoid entering confidential information.
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="responderRules")
    def responder_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResponderRecipeResponderRuleArgs']]]]:
        """
        (Updatable) List of responder rules to override from source responder recipe
        """
        return pulumi.get(self, "responder_rules")

    @responder_rules.setter
    def responder_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResponderRecipeResponderRuleArgs']]]]):
        pulumi.set(self, "responder_rules", value)


@pulumi.input_type
class _ResponderRecipeState:
    def __init__(__self__, *,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 effective_responder_rules: Optional[pulumi.Input[Sequence[pulumi.Input['ResponderRecipeEffectiveResponderRuleArgs']]]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 responder_rules: Optional[pulumi.Input[Sequence[pulumi.Input['ResponderRecipeResponderRuleArgs']]]] = None,
                 source_responder_recipe_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ResponderRecipe resources.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment OCID
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) Responder recipe description.
               
               Avoid entering confidential information.
        :param pulumi.Input[str] display_name: (Updatable) Responder recipe display name.
               
               Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input['ResponderRecipeEffectiveResponderRuleArgs']]] effective_responder_rules: List of currently enabled responder rules for the responder type, for recipe after applying defaults
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
               
               Avoid entering confidential information.
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] owner: Owner of responder recipe
        :param pulumi.Input[Sequence[pulumi.Input['ResponderRecipeResponderRuleArgs']]] responder_rules: (Updatable) List of responder rules to override from source responder recipe
        :param pulumi.Input[str] source_responder_recipe_id: The unique identifier of the source responder recipe
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current lifecycle state of the example
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time the responder recipe was created. Format defined by RFC3339.
        :param pulumi.Input[str] time_updated: The date and time the responder recipe was last updated. Format defined by RFC3339.
        """
        if compartment_id is not None:
            pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if effective_responder_rules is not None:
            pulumi.set(__self__, "effective_responder_rules", effective_responder_rules)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if responder_rules is not None:
            pulumi.set(__self__, "responder_rules", responder_rules)
        if source_responder_recipe_id is not None:
            pulumi.set(__self__, "source_responder_recipe_id", source_responder_recipe_id)
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
        (Updatable) Compartment OCID
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
        (Updatable) Responder recipe description.

        Avoid entering confidential information.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Responder recipe display name.

        Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="effectiveResponderRules")
    def effective_responder_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResponderRecipeEffectiveResponderRuleArgs']]]]:
        """
        List of currently enabled responder rules for the responder type, for recipe after applying defaults
        """
        return pulumi.get(self, "effective_responder_rules")

    @effective_responder_rules.setter
    def effective_responder_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResponderRecipeEffectiveResponderRuleArgs']]]]):
        pulumi.set(self, "effective_responder_rules", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`

        Avoid entering confidential information.
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        Owner of responder recipe
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter(name="responderRules")
    def responder_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResponderRecipeResponderRuleArgs']]]]:
        """
        (Updatable) List of responder rules to override from source responder recipe
        """
        return pulumi.get(self, "responder_rules")

    @responder_rules.setter
    def responder_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResponderRecipeResponderRuleArgs']]]]):
        pulumi.set(self, "responder_rules", value)

    @property
    @pulumi.getter(name="sourceResponderRecipeId")
    def source_responder_recipe_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the source responder recipe


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "source_responder_recipe_id")

    @source_responder_recipe_id.setter
    def source_responder_recipe_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_responder_recipe_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current lifecycle state of the example
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @system_tags.setter
    def system_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "system_tags", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the responder recipe was created. Format defined by RFC3339.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time the responder recipe was last updated. Format defined by RFC3339.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class ResponderRecipe(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 responder_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponderRecipeResponderRuleArgs']]]]] = None,
                 source_responder_recipe_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Responder Recipe resource in Oracle Cloud Infrastructure Cloud Guard service.

        Creates a responder recipe (ResponderRecipe resource), from values passed in a
        CreateResponderRecipeDetails resource.

        ## Import

        ResponderRecipes can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:CloudGuard/responderRecipe:ResponderRecipe test_responder_recipe "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment OCID
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) Responder recipe description.
               
               Avoid entering confidential information.
        :param pulumi.Input[str] display_name: (Updatable) Responder recipe display name.
               
               Avoid entering confidential information.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
               
               Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponderRecipeResponderRuleArgs']]]] responder_rules: (Updatable) List of responder rules to override from source responder recipe
        :param pulumi.Input[str] source_responder_recipe_id: The unique identifier of the source responder recipe
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResponderRecipeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Responder Recipe resource in Oracle Cloud Infrastructure Cloud Guard service.

        Creates a responder recipe (ResponderRecipe resource), from values passed in a
        CreateResponderRecipeDetails resource.

        ## Import

        ResponderRecipes can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:CloudGuard/responderRecipe:ResponderRecipe test_responder_recipe "id"
        ```

        :param str resource_name: The name of the resource.
        :param ResponderRecipeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResponderRecipeArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 responder_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponderRecipeResponderRuleArgs']]]]] = None,
                 source_responder_recipe_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResponderRecipeArgs.__new__(ResponderRecipeArgs)

            if compartment_id is None and not opts.urn:
                raise TypeError("Missing required property 'compartment_id'")
            __props__.__dict__["compartment_id"] = compartment_id
            __props__.__dict__["defined_tags"] = defined_tags
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["freeform_tags"] = freeform_tags
            __props__.__dict__["responder_rules"] = responder_rules
            if source_responder_recipe_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_responder_recipe_id'")
            __props__.__dict__["source_responder_recipe_id"] = source_responder_recipe_id
            __props__.__dict__["effective_responder_rules"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["owner"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(ResponderRecipe, __self__).__init__(
            'oci:CloudGuard/responderRecipe:ResponderRecipe',
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
            effective_responder_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponderRecipeEffectiveResponderRuleArgs']]]]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            responder_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponderRecipeResponderRuleArgs']]]]] = None,
            source_responder_recipe_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'ResponderRecipe':
        """
        Get an existing ResponderRecipe resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compartment_id: (Updatable) Compartment OCID
        :param pulumi.Input[Mapping[str, Any]] defined_tags: (Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        :param pulumi.Input[str] description: (Updatable) Responder recipe description.
               
               Avoid entering confidential information.
        :param pulumi.Input[str] display_name: (Updatable) Responder recipe display name.
               
               Avoid entering confidential information.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponderRecipeEffectiveResponderRuleArgs']]]] effective_responder_rules: List of currently enabled responder rules for the responder type, for recipe after applying defaults
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
               
               Avoid entering confidential information.
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] owner: Owner of responder recipe
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResponderRecipeResponderRuleArgs']]]] responder_rules: (Updatable) List of responder rules to override from source responder recipe
        :param pulumi.Input[str] source_responder_recipe_id: The unique identifier of the source responder recipe
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] state: The current lifecycle state of the example
        :param pulumi.Input[Mapping[str, Any]] system_tags: System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        :param pulumi.Input[str] time_created: The date and time the responder recipe was created. Format defined by RFC3339.
        :param pulumi.Input[str] time_updated: The date and time the responder recipe was last updated. Format defined by RFC3339.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResponderRecipeState.__new__(_ResponderRecipeState)

        __props__.__dict__["compartment_id"] = compartment_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["effective_responder_rules"] = effective_responder_rules
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["owner"] = owner
        __props__.__dict__["responder_rules"] = responder_rules
        __props__.__dict__["source_responder_recipe_id"] = source_responder_recipe_id
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return ResponderRecipe(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> pulumi.Output[str]:
        """
        (Updatable) Compartment OCID
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
    def description(self) -> pulumi.Output[str]:
        """
        (Updatable) Responder recipe description.

        Avoid entering confidential information.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        (Updatable) Responder recipe display name.

        Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="effectiveResponderRules")
    def effective_responder_rules(self) -> pulumi.Output[Sequence['outputs.ResponderRecipeEffectiveResponderRule']]:
        """
        List of currently enabled responder rules for the responder type, for recipe after applying defaults
        """
        return pulumi.get(self, "effective_responder_rules")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Updatable) Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`

        Avoid entering confidential information.
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        Owner of responder recipe
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="responderRules")
    def responder_rules(self) -> pulumi.Output[Sequence['outputs.ResponderRecipeResponderRule']]:
        """
        (Updatable) List of responder rules to override from source responder recipe
        """
        return pulumi.get(self, "responder_rules")

    @property
    @pulumi.getter(name="sourceResponderRecipeId")
    def source_responder_recipe_id(self) -> pulumi.Output[str]:
        """
        The unique identifier of the source responder recipe


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "source_responder_recipe_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current lifecycle state of the example
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). System tags can be viewed by users, but can only be created by the system.  Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The date and time the responder recipe was created. Format defined by RFC3339.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The date and time the responder recipe was last updated. Format defined by RFC3339.
        """
        return pulumi.get(self, "time_updated")

