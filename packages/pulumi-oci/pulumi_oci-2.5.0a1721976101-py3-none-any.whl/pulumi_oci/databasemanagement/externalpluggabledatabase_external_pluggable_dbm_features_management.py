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

__all__ = ['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementArgs', 'ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagement']

@pulumi.input_type
class ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementArgs:
    def __init__(__self__, *,
                 enable_external_pluggable_dbm_feature: pulumi.Input[bool],
                 external_pluggable_database_id: pulumi.Input[str],
                 feature_details: Optional[pulumi.Input['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']] = None):
        """
        The set of arguments for constructing a ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagement resource.
        :param pulumi.Input[bool] enable_external_pluggable_dbm_feature: (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_pluggable_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external pluggable database.
        :param pulumi.Input['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs'] feature_details: The details required to enable the specified Database Management feature.
        """
        pulumi.set(__self__, "enable_external_pluggable_dbm_feature", enable_external_pluggable_dbm_feature)
        pulumi.set(__self__, "external_pluggable_database_id", external_pluggable_database_id)
        if feature_details is not None:
            pulumi.set(__self__, "feature_details", feature_details)

    @property
    @pulumi.getter(name="enableExternalPluggableDbmFeature")
    def enable_external_pluggable_dbm_feature(self) -> pulumi.Input[bool]:
        """
        (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "enable_external_pluggable_dbm_feature")

    @enable_external_pluggable_dbm_feature.setter
    def enable_external_pluggable_dbm_feature(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_external_pluggable_dbm_feature", value)

    @property
    @pulumi.getter(name="externalPluggableDatabaseId")
    def external_pluggable_database_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external pluggable database.
        """
        return pulumi.get(self, "external_pluggable_database_id")

    @external_pluggable_database_id.setter
    def external_pluggable_database_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "external_pluggable_database_id", value)

    @property
    @pulumi.getter(name="featureDetails")
    def feature_details(self) -> Optional[pulumi.Input['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']]:
        """
        The details required to enable the specified Database Management feature.
        """
        return pulumi.get(self, "feature_details")

    @feature_details.setter
    def feature_details(self, value: Optional[pulumi.Input['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']]):
        pulumi.set(self, "feature_details", value)


@pulumi.input_type
class _ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementState:
    def __init__(__self__, *,
                 enable_external_pluggable_dbm_feature: Optional[pulumi.Input[bool]] = None,
                 external_pluggable_database_id: Optional[pulumi.Input[str]] = None,
                 feature_details: Optional[pulumi.Input['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']] = None):
        """
        Input properties used for looking up and filtering ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagement resources.
        :param pulumi.Input[bool] enable_external_pluggable_dbm_feature: (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_pluggable_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external pluggable database.
        :param pulumi.Input['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs'] feature_details: The details required to enable the specified Database Management feature.
        """
        if enable_external_pluggable_dbm_feature is not None:
            pulumi.set(__self__, "enable_external_pluggable_dbm_feature", enable_external_pluggable_dbm_feature)
        if external_pluggable_database_id is not None:
            pulumi.set(__self__, "external_pluggable_database_id", external_pluggable_database_id)
        if feature_details is not None:
            pulumi.set(__self__, "feature_details", feature_details)

    @property
    @pulumi.getter(name="enableExternalPluggableDbmFeature")
    def enable_external_pluggable_dbm_feature(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "enable_external_pluggable_dbm_feature")

    @enable_external_pluggable_dbm_feature.setter
    def enable_external_pluggable_dbm_feature(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_external_pluggable_dbm_feature", value)

    @property
    @pulumi.getter(name="externalPluggableDatabaseId")
    def external_pluggable_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external pluggable database.
        """
        return pulumi.get(self, "external_pluggable_database_id")

    @external_pluggable_database_id.setter
    def external_pluggable_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_pluggable_database_id", value)

    @property
    @pulumi.getter(name="featureDetails")
    def feature_details(self) -> Optional[pulumi.Input['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']]:
        """
        The details required to enable the specified Database Management feature.
        """
        return pulumi.get(self, "feature_details")

    @feature_details.setter
    def feature_details(self, value: Optional[pulumi.Input['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']]):
        pulumi.set(self, "feature_details", value)


class ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagement(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_external_pluggable_dbm_feature: Optional[pulumi.Input[bool]] = None,
                 external_pluggable_database_id: Optional[pulumi.Input[str]] = None,
                 feature_details: Optional[pulumi.Input[pulumi.InputType['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']]] = None,
                 __props__=None):
        """
        This resource provides the Externalpluggabledatabase External Pluggable Dbm Features Management resource in Oracle Cloud Infrastructure Database Management service.

        Enables a Database Management feature for the specified external pluggable database.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_external_pluggable_dbm_feature: (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_pluggable_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external pluggable database.
        :param pulumi.Input[pulumi.InputType['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']] feature_details: The details required to enable the specified Database Management feature.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Externalpluggabledatabase External Pluggable Dbm Features Management resource in Oracle Cloud Infrastructure Database Management service.

        Enables a Database Management feature for the specified external pluggable database.

        :param str resource_name: The name of the resource.
        :param ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_external_pluggable_dbm_feature: Optional[pulumi.Input[bool]] = None,
                 external_pluggable_database_id: Optional[pulumi.Input[str]] = None,
                 feature_details: Optional[pulumi.Input[pulumi.InputType['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementArgs.__new__(ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementArgs)

            if enable_external_pluggable_dbm_feature is None and not opts.urn:
                raise TypeError("Missing required property 'enable_external_pluggable_dbm_feature'")
            __props__.__dict__["enable_external_pluggable_dbm_feature"] = enable_external_pluggable_dbm_feature
            if external_pluggable_database_id is None and not opts.urn:
                raise TypeError("Missing required property 'external_pluggable_database_id'")
            __props__.__dict__["external_pluggable_database_id"] = external_pluggable_database_id
            __props__.__dict__["feature_details"] = feature_details
        super(ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagement, __self__).__init__(
            'oci:DatabaseManagement/externalpluggabledatabaseExternalPluggableDbmFeaturesManagement:ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagement',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable_external_pluggable_dbm_feature: Optional[pulumi.Input[bool]] = None,
            external_pluggable_database_id: Optional[pulumi.Input[str]] = None,
            feature_details: Optional[pulumi.Input[pulumi.InputType['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']]] = None) -> 'ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagement':
        """
        Get an existing ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagement resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_external_pluggable_dbm_feature: (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_pluggable_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external pluggable database.
        :param pulumi.Input[pulumi.InputType['ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetailsArgs']] feature_details: The details required to enable the specified Database Management feature.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementState.__new__(_ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementState)

        __props__.__dict__["enable_external_pluggable_dbm_feature"] = enable_external_pluggable_dbm_feature
        __props__.__dict__["external_pluggable_database_id"] = external_pluggable_database_id
        __props__.__dict__["feature_details"] = feature_details
        return ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagement(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="enableExternalPluggableDbmFeature")
    def enable_external_pluggable_dbm_feature(self) -> pulumi.Output[bool]:
        """
        (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "enable_external_pluggable_dbm_feature")

    @property
    @pulumi.getter(name="externalPluggableDatabaseId")
    def external_pluggable_database_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external pluggable database.
        """
        return pulumi.get(self, "external_pluggable_database_id")

    @property
    @pulumi.getter(name="featureDetails")
    def feature_details(self) -> pulumi.Output['outputs.ExternalpluggabledatabaseExternalPluggableDbmFeaturesManagementFeatureDetails']:
        """
        The details required to enable the specified Database Management feature.
        """
        return pulumi.get(self, "feature_details")

