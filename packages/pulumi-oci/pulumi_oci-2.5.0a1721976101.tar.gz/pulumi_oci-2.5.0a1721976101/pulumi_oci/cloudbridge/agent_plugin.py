# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AgentPluginArgs', 'AgentPlugin']

@pulumi.input_type
class AgentPluginArgs:
    def __init__(__self__, *,
                 agent_id: pulumi.Input[str],
                 plugin_name: pulumi.Input[str],
                 desired_state: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AgentPlugin resource.
        :param pulumi.Input[str] agent_id: Unique Agent identifier path parameter.
        :param pulumi.Input[str] plugin_name: Unique plugin identifier path parameter.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] desired_state: (Updatable) State to which the customer wants the plugin to move to.
        """
        pulumi.set(__self__, "agent_id", agent_id)
        pulumi.set(__self__, "plugin_name", plugin_name)
        if desired_state is not None:
            pulumi.set(__self__, "desired_state", desired_state)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[str]:
        """
        Unique Agent identifier path parameter.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="pluginName")
    def plugin_name(self) -> pulumi.Input[str]:
        """
        Unique plugin identifier path parameter.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "plugin_name")

    @plugin_name.setter
    def plugin_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "plugin_name", value)

    @property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) State to which the customer wants the plugin to move to.
        """
        return pulumi.get(self, "desired_state")

    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "desired_state", value)


@pulumi.input_type
class _AgentPluginState:
    def __init__(__self__, *,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 desired_state: Optional[pulumi.Input[str]] = None,
                 freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 lifecycle_details: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 plugin_name: Optional[pulumi.Input[str]] = None,
                 plugin_version: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 time_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AgentPlugin resources.
        :param pulumi.Input[str] agent_id: Unique Agent identifier path parameter.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] desired_state: (Updatable) State to which the customer wants the plugin to move to.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] name: Plugin identifier, which can be renamed.
        :param pulumi.Input[str] plugin_name: Unique plugin identifier path parameter.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] plugin_version: Plugin version.
        :param pulumi.Input[str] state: The current state of the plugin.
        :param pulumi.Input[Mapping[str, Any]] system_tags: The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`
        :param pulumi.Input[str] time_created: The time when the Agent was created. An RFC3339 formatted datetime string.
        :param pulumi.Input[str] time_updated: The time when the Agent was updated. An RFC3339 formatted datetime string.
        """
        if agent_id is not None:
            pulumi.set(__self__, "agent_id", agent_id)
        if defined_tags is not None:
            pulumi.set(__self__, "defined_tags", defined_tags)
        if desired_state is not None:
            pulumi.set(__self__, "desired_state", desired_state)
        if freeform_tags is not None:
            pulumi.set(__self__, "freeform_tags", freeform_tags)
        if lifecycle_details is not None:
            pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if plugin_name is not None:
            pulumi.set(__self__, "plugin_name", plugin_name)
        if plugin_version is not None:
            pulumi.set(__self__, "plugin_version", plugin_version)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if system_tags is not None:
            pulumi.set(__self__, "system_tags", system_tags)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if time_updated is not None:
            pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique Agent identifier path parameter.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @defined_tags.setter
    def defined_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "defined_tags", value)

    @property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) State to which the customer wants the plugin to move to.
        """
        return pulumi.get(self, "desired_state")

    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "desired_state", value)

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @freeform_tags.setter
    def freeform_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "freeform_tags", value)

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[str]]:
        """
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lifecycle_details", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Plugin identifier, which can be renamed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pluginName")
    def plugin_name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique plugin identifier path parameter.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "plugin_name")

    @plugin_name.setter
    def plugin_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugin_name", value)

    @property
    @pulumi.getter(name="pluginVersion")
    def plugin_version(self) -> Optional[pulumi.Input[str]]:
        """
        Plugin version.
        """
        return pulumi.get(self, "plugin_version")

    @plugin_version.setter
    def plugin_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plugin_version", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the plugin.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`
        """
        return pulumi.get(self, "system_tags")

    @system_tags.setter
    def system_tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "system_tags", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the Agent was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the Agent was updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @time_updated.setter
    def time_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_updated", value)


class AgentPlugin(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 desired_state: Optional[pulumi.Input[str]] = None,
                 plugin_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Agent Plugin resource in Oracle Cloud Infrastructure Cloud Bridge service.

        Updates the plugin.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_agent_plugin = oci.cloud_bridge.AgentPlugin("test_agent_plugin",
            agent_id=test_agent["id"],
            plugin_name=agent_plugin_plugin_name,
            desired_state=agent_plugin_desired_state)
        ```

        ## Import

        AgentPlugins can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:CloudBridge/agentPlugin:AgentPlugin test_agent_plugin "agents/{agentId}/plugins/{pluginName}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_id: Unique Agent identifier path parameter.
        :param pulumi.Input[str] desired_state: (Updatable) State to which the customer wants the plugin to move to.
        :param pulumi.Input[str] plugin_name: Unique plugin identifier path parameter.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgentPluginArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Agent Plugin resource in Oracle Cloud Infrastructure Cloud Bridge service.

        Updates the plugin.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_agent_plugin = oci.cloud_bridge.AgentPlugin("test_agent_plugin",
            agent_id=test_agent["id"],
            plugin_name=agent_plugin_plugin_name,
            desired_state=agent_plugin_desired_state)
        ```

        ## Import

        AgentPlugins can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:CloudBridge/agentPlugin:AgentPlugin test_agent_plugin "agents/{agentId}/plugins/{pluginName}"
        ```

        :param str resource_name: The name of the resource.
        :param AgentPluginArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgentPluginArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 desired_state: Optional[pulumi.Input[str]] = None,
                 plugin_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AgentPluginArgs.__new__(AgentPluginArgs)

            if agent_id is None and not opts.urn:
                raise TypeError("Missing required property 'agent_id'")
            __props__.__dict__["agent_id"] = agent_id
            __props__.__dict__["desired_state"] = desired_state
            if plugin_name is None and not opts.urn:
                raise TypeError("Missing required property 'plugin_name'")
            __props__.__dict__["plugin_name"] = plugin_name
            __props__.__dict__["defined_tags"] = None
            __props__.__dict__["freeform_tags"] = None
            __props__.__dict__["lifecycle_details"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["plugin_version"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_tags"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_updated"] = None
        super(AgentPlugin, __self__).__init__(
            'oci:CloudBridge/agentPlugin:AgentPlugin',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            agent_id: Optional[pulumi.Input[str]] = None,
            defined_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            desired_state: Optional[pulumi.Input[str]] = None,
            freeform_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            lifecycle_details: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            plugin_name: Optional[pulumi.Input[str]] = None,
            plugin_version: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            system_tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            time_updated: Optional[pulumi.Input[str]] = None) -> 'AgentPlugin':
        """
        Get an existing AgentPlugin resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_id: Unique Agent identifier path parameter.
        :param pulumi.Input[Mapping[str, Any]] defined_tags: The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        :param pulumi.Input[str] desired_state: (Updatable) State to which the customer wants the plugin to move to.
        :param pulumi.Input[Mapping[str, Any]] freeform_tags: The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        :param pulumi.Input[str] lifecycle_details: A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.
        :param pulumi.Input[str] name: Plugin identifier, which can be renamed.
        :param pulumi.Input[str] plugin_name: Unique plugin identifier path parameter.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] plugin_version: Plugin version.
        :param pulumi.Input[str] state: The current state of the plugin.
        :param pulumi.Input[Mapping[str, Any]] system_tags: The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`
        :param pulumi.Input[str] time_created: The time when the Agent was created. An RFC3339 formatted datetime string.
        :param pulumi.Input[str] time_updated: The time when the Agent was updated. An RFC3339 formatted datetime string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AgentPluginState.__new__(_AgentPluginState)

        __props__.__dict__["agent_id"] = agent_id
        __props__.__dict__["defined_tags"] = defined_tags
        __props__.__dict__["desired_state"] = desired_state
        __props__.__dict__["freeform_tags"] = freeform_tags
        __props__.__dict__["lifecycle_details"] = lifecycle_details
        __props__.__dict__["name"] = name
        __props__.__dict__["plugin_name"] = plugin_name
        __props__.__dict__["plugin_version"] = plugin_version
        __props__.__dict__["state"] = state
        __props__.__dict__["system_tags"] = system_tags
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["time_updated"] = time_updated
        return AgentPlugin(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[str]:
        """
        Unique Agent identifier path parameter.
        """
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Output[str]:
        """
        (Updatable) State to which the customer wants the plugin to move to.
        """
        return pulumi.get(self, "desired_state")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> pulumi.Output[str]:
        """
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Plugin identifier, which can be renamed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pluginName")
    def plugin_name(self) -> pulumi.Output[str]:
        """
        Unique plugin identifier path parameter.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "plugin_name")

    @property
    @pulumi.getter(name="pluginVersion")
    def plugin_version(self) -> pulumi.Output[str]:
        """
        Plugin version.
        """
        return pulumi.get(self, "plugin_version")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the plugin.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{orcl-cloud: {free-tier-retain: true}}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time when the Agent was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> pulumi.Output[str]:
        """
        The time when the Agent was updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

