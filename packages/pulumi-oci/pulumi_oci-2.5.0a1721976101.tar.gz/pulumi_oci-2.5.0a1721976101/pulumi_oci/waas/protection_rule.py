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

__all__ = ['ProtectionRuleArgs', 'ProtectionRule']

@pulumi.input_type
class ProtectionRuleArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 waas_policy_id: pulumi.Input[str],
                 action: Optional[pulumi.Input[str]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionRuleExclusionArgs']]]] = None):
        """
        The set of arguments for constructing a ProtectionRule resource.
        :param pulumi.Input[str] key: (Updatable) The unique key of the protection rule.
        :param pulumi.Input[str] waas_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        :param pulumi.Input[str] action: (Updatable) The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
        :param pulumi.Input[Sequence[pulumi.Input['ProtectionRuleExclusionArgs']]] exclusions: (Updatable)
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "waas_policy_id", waas_policy_id)
        if action is not None:
            pulumi.set(__self__, "action", action)
        if exclusions is not None:
            pulumi.set(__self__, "exclusions", exclusions)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        (Updatable) The unique key of the protection rule.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="waasPolicyId")
    def waas_policy_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        """
        return pulumi.get(self, "waas_policy_id")

    @waas_policy_id.setter
    def waas_policy_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "waas_policy_id", value)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionRuleExclusionArgs']]]]:
        """
        (Updatable)
        """
        return pulumi.get(self, "exclusions")

    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionRuleExclusionArgs']]]]):
        pulumi.set(self, "exclusions", value)


@pulumi.input_type
class _ProtectionRuleState:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionRuleExclusionArgs']]]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mod_security_rule_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 waas_policy_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProtectionRule resources.
        :param pulumi.Input[str] action: (Updatable) The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
        :param pulumi.Input[str] description: The description of the protection rule.
        :param pulumi.Input[Sequence[pulumi.Input['ProtectionRuleExclusionArgs']]] exclusions: (Updatable)
        :param pulumi.Input[str] key: (Updatable) The unique key of the protection rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: The list of labels for the protection rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mod_security_rule_ids: The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see [Mod Security's documentation](https://www.modsecurity.org/CRS/Documentation/index.html).
        :param pulumi.Input[str] name: The name of the protection rule.
        :param pulumi.Input[str] waas_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if exclusions is not None:
            pulumi.set(__self__, "exclusions", exclusions)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if mod_security_rule_ids is not None:
            pulumi.set(__self__, "mod_security_rule_ids", mod_security_rule_ids)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if waas_policy_id is not None:
            pulumi.set(__self__, "waas_policy_id", waas_policy_id)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the protection rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionRuleExclusionArgs']]]]:
        """
        (Updatable)
        """
        return pulumi.get(self, "exclusions")

    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProtectionRuleExclusionArgs']]]]):
        pulumi.set(self, "exclusions", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) The unique key of the protection rule.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of labels for the protection rule.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="modSecurityRuleIds")
    def mod_security_rule_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see [Mod Security's documentation](https://www.modsecurity.org/CRS/Documentation/index.html).
        """
        return pulumi.get(self, "mod_security_rule_ids")

    @mod_security_rule_ids.setter
    def mod_security_rule_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "mod_security_rule_ids", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the protection rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="waasPolicyId")
    def waas_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        """
        return pulumi.get(self, "waas_policy_id")

    @waas_policy_id.setter
    def waas_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "waas_policy_id", value)


class ProtectionRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProtectionRuleExclusionArgs']]]]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 waas_policy_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Protection Rule resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

        Updates the action for each specified protection rule. Requests can either be allowed, blocked, or trigger an alert if they meet the parameters of an applied rule. For more information on protection rules, see [WAF Protection Rules](https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafprotectionrules.htm).
        This operation can update or disable protection rules depending on the structure of the request body.
        Protection rules can be updated by changing the properties of the protection rule object with the rule's key specified in the key field.

        ## Import

        ProtectionRules can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Waas/protectionRule:ProtectionRule test_protection_rule "waasPolicyId/{waasPolicyId}/key/{key}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: (Updatable) The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProtectionRuleExclusionArgs']]]] exclusions: (Updatable)
        :param pulumi.Input[str] key: (Updatable) The unique key of the protection rule.
        :param pulumi.Input[str] waas_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProtectionRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Protection Rule resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

        Updates the action for each specified protection rule. Requests can either be allowed, blocked, or trigger an alert if they meet the parameters of an applied rule. For more information on protection rules, see [WAF Protection Rules](https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafprotectionrules.htm).
        This operation can update or disable protection rules depending on the structure of the request body.
        Protection rules can be updated by changing the properties of the protection rule object with the rule's key specified in the key field.

        ## Import

        ProtectionRules can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Waas/protectionRule:ProtectionRule test_protection_rule "waasPolicyId/{waasPolicyId}/key/{key}"
        ```

        :param str resource_name: The name of the resource.
        :param ProtectionRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProtectionRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProtectionRuleExclusionArgs']]]]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 waas_policy_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProtectionRuleArgs.__new__(ProtectionRuleArgs)

            __props__.__dict__["action"] = action
            __props__.__dict__["exclusions"] = exclusions
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            if waas_policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'waas_policy_id'")
            __props__.__dict__["waas_policy_id"] = waas_policy_id
            __props__.__dict__["description"] = None
            __props__.__dict__["labels"] = None
            __props__.__dict__["mod_security_rule_ids"] = None
            __props__.__dict__["name"] = None
        super(ProtectionRule, __self__).__init__(
            'oci:Waas/protectionRule:ProtectionRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProtectionRuleExclusionArgs']]]]] = None,
            key: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            mod_security_rule_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            waas_policy_id: Optional[pulumi.Input[str]] = None) -> 'ProtectionRule':
        """
        Get an existing ProtectionRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: (Updatable) The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
        :param pulumi.Input[str] description: The description of the protection rule.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProtectionRuleExclusionArgs']]]] exclusions: (Updatable)
        :param pulumi.Input[str] key: (Updatable) The unique key of the protection rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: The list of labels for the protection rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mod_security_rule_ids: The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see [Mod Security's documentation](https://www.modsecurity.org/CRS/Documentation/index.html).
        :param pulumi.Input[str] name: The name of the protection rule.
        :param pulumi.Input[str] waas_policy_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProtectionRuleState.__new__(_ProtectionRuleState)

        __props__.__dict__["action"] = action
        __props__.__dict__["description"] = description
        __props__.__dict__["exclusions"] = exclusions
        __props__.__dict__["key"] = key
        __props__.__dict__["labels"] = labels
        __props__.__dict__["mod_security_rule_ids"] = mod_security_rule_ids
        __props__.__dict__["name"] = name
        __props__.__dict__["waas_policy_id"] = waas_policy_id
        return ProtectionRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        (Updatable) The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the protection rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def exclusions(self) -> pulumi.Output[Sequence['outputs.ProtectionRuleExclusion']]:
        """
        (Updatable)
        """
        return pulumi.get(self, "exclusions")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        (Updatable) The unique key of the protection rule.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of labels for the protection rule.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="modSecurityRuleIds")
    def mod_security_rule_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see [Mod Security's documentation](https://www.modsecurity.org/CRS/Documentation/index.html).
        """
        return pulumi.get(self, "mod_security_rule_ids")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the protection rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="waasPolicyId")
    def waas_policy_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        """
        return pulumi.get(self, "waas_policy_id")

