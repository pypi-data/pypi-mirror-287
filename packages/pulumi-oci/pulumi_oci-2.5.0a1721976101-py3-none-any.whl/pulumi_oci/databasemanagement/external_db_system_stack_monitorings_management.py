# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ExternalDbSystemStackMonitoringsManagementArgs', 'ExternalDbSystemStackMonitoringsManagement']

@pulumi.input_type
class ExternalDbSystemStackMonitoringsManagementArgs:
    def __init__(__self__, *,
                 enable_stack_monitoring: pulumi.Input[bool],
                 external_db_system_id: pulumi.Input[str],
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExternalDbSystemStackMonitoringsManagement resource.
        :param pulumi.Input[bool] enable_stack_monitoring: (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
        :param pulumi.Input[bool] is_enabled: The status of the associated service.
        :param pulumi.Input[str] metadata: The associated service-specific inputs in JSON string format, which Database Management can identify.
        """
        pulumi.set(__self__, "enable_stack_monitoring", enable_stack_monitoring)
        pulumi.set(__self__, "external_db_system_id", external_db_system_id)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)

    @property
    @pulumi.getter(name="enableStackMonitoring")
    def enable_stack_monitoring(self) -> pulumi.Input[bool]:
        """
        (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "enable_stack_monitoring")

    @enable_stack_monitoring.setter
    def enable_stack_monitoring(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_stack_monitoring", value)

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
        """
        return pulumi.get(self, "external_db_system_id")

    @external_db_system_id.setter
    def external_db_system_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "external_db_system_id", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The status of the associated service.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        The associated service-specific inputs in JSON string format, which Database Management can identify.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)


@pulumi.input_type
class _ExternalDbSystemStackMonitoringsManagementState:
    def __init__(__self__, *,
                 enable_stack_monitoring: Optional[pulumi.Input[bool]] = None,
                 external_db_system_id: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExternalDbSystemStackMonitoringsManagement resources.
        :param pulumi.Input[bool] enable_stack_monitoring: (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
        :param pulumi.Input[bool] is_enabled: The status of the associated service.
        :param pulumi.Input[str] metadata: The associated service-specific inputs in JSON string format, which Database Management can identify.
        """
        if enable_stack_monitoring is not None:
            pulumi.set(__self__, "enable_stack_monitoring", enable_stack_monitoring)
        if external_db_system_id is not None:
            pulumi.set(__self__, "external_db_system_id", external_db_system_id)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)

    @property
    @pulumi.getter(name="enableStackMonitoring")
    def enable_stack_monitoring(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "enable_stack_monitoring")

    @enable_stack_monitoring.setter
    def enable_stack_monitoring(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_stack_monitoring", value)

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
        """
        return pulumi.get(self, "external_db_system_id")

    @external_db_system_id.setter
    def external_db_system_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_db_system_id", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The status of the associated service.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        The associated service-specific inputs in JSON string format, which Database Management can identify.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)


class ExternalDbSystemStackMonitoringsManagement(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_stack_monitoring: Optional[pulumi.Input[bool]] = None,
                 external_db_system_id: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the External Db System Stack Monitorings Management resource in Oracle Cloud Infrastructure Database Management service.

        Enables Stack Monitoring for all the components of the specified
        external DB system (except databases).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_external_db_system_stack_monitorings_management = oci.database_management.ExternalDbSystemStackMonitoringsManagement("test_external_db_system_stack_monitorings_management",
            external_db_system_id=test_external_db_system["id"],
            enable_stack_monitoring=enable_stack_monitoring,
            is_enabled=external_db_system_stack_monitorings_management_is_enabled,
            metadata=external_db_system_stack_monitorings_management_metadata)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_stack_monitoring: (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
        :param pulumi.Input[bool] is_enabled: The status of the associated service.
        :param pulumi.Input[str] metadata: The associated service-specific inputs in JSON string format, which Database Management can identify.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExternalDbSystemStackMonitoringsManagementArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the External Db System Stack Monitorings Management resource in Oracle Cloud Infrastructure Database Management service.

        Enables Stack Monitoring for all the components of the specified
        external DB system (except databases).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_external_db_system_stack_monitorings_management = oci.database_management.ExternalDbSystemStackMonitoringsManagement("test_external_db_system_stack_monitorings_management",
            external_db_system_id=test_external_db_system["id"],
            enable_stack_monitoring=enable_stack_monitoring,
            is_enabled=external_db_system_stack_monitorings_management_is_enabled,
            metadata=external_db_system_stack_monitorings_management_metadata)
        ```

        :param str resource_name: The name of the resource.
        :param ExternalDbSystemStackMonitoringsManagementArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExternalDbSystemStackMonitoringsManagementArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_stack_monitoring: Optional[pulumi.Input[bool]] = None,
                 external_db_system_id: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExternalDbSystemStackMonitoringsManagementArgs.__new__(ExternalDbSystemStackMonitoringsManagementArgs)

            if enable_stack_monitoring is None and not opts.urn:
                raise TypeError("Missing required property 'enable_stack_monitoring'")
            __props__.__dict__["enable_stack_monitoring"] = enable_stack_monitoring
            if external_db_system_id is None and not opts.urn:
                raise TypeError("Missing required property 'external_db_system_id'")
            __props__.__dict__["external_db_system_id"] = external_db_system_id
            __props__.__dict__["is_enabled"] = is_enabled
            __props__.__dict__["metadata"] = metadata
        super(ExternalDbSystemStackMonitoringsManagement, __self__).__init__(
            'oci:DatabaseManagement/externalDbSystemStackMonitoringsManagement:ExternalDbSystemStackMonitoringsManagement',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable_stack_monitoring: Optional[pulumi.Input[bool]] = None,
            external_db_system_id: Optional[pulumi.Input[str]] = None,
            is_enabled: Optional[pulumi.Input[bool]] = None,
            metadata: Optional[pulumi.Input[str]] = None) -> 'ExternalDbSystemStackMonitoringsManagement':
        """
        Get an existing ExternalDbSystemStackMonitoringsManagement resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_stack_monitoring: (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
        :param pulumi.Input[bool] is_enabled: The status of the associated service.
        :param pulumi.Input[str] metadata: The associated service-specific inputs in JSON string format, which Database Management can identify.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExternalDbSystemStackMonitoringsManagementState.__new__(_ExternalDbSystemStackMonitoringsManagementState)

        __props__.__dict__["enable_stack_monitoring"] = enable_stack_monitoring
        __props__.__dict__["external_db_system_id"] = external_db_system_id
        __props__.__dict__["is_enabled"] = is_enabled
        __props__.__dict__["metadata"] = metadata
        return ExternalDbSystemStackMonitoringsManagement(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="enableStackMonitoring")
    def enable_stack_monitoring(self) -> pulumi.Output[bool]:
        """
        (Updatable) A required field when set to `true` calls enable action and when set to `false` calls disable action.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "enable_stack_monitoring")

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
        """
        return pulumi.get(self, "external_db_system_id")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[bool]:
        """
        The status of the associated service.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[str]:
        """
        The associated service-specific inputs in JSON string format, which Database Management can identify.
        """
        return pulumi.get(self, "metadata")

