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

__all__ = ['ManagedInstanceGroupUpdateAllPackagesManagementArgs', 'ManagedInstanceGroupUpdateAllPackagesManagement']

@pulumi.input_type
class ManagedInstanceGroupUpdateAllPackagesManagementArgs:
    def __init__(__self__, *,
                 managed_instance_group_id: pulumi.Input[str],
                 update_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 work_request_details: Optional[pulumi.Input['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']] = None):
        """
        The set of arguments for constructing a ManagedInstanceGroupUpdateAllPackagesManagement resource.
        :param pulumi.Input[str] managed_instance_group_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] update_types: The type of updates to be applied.
        :param pulumi.Input['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs'] work_request_details: Provides the name and description of the job.
        """
        pulumi.set(__self__, "managed_instance_group_id", managed_instance_group_id)
        if update_types is not None:
            pulumi.set(__self__, "update_types", update_types)
        if work_request_details is not None:
            pulumi.set(__self__, "work_request_details", work_request_details)

    @property
    @pulumi.getter(name="managedInstanceGroupId")
    def managed_instance_group_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
        """
        return pulumi.get(self, "managed_instance_group_id")

    @managed_instance_group_id.setter
    def managed_instance_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_group_id", value)

    @property
    @pulumi.getter(name="updateTypes")
    def update_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The type of updates to be applied.
        """
        return pulumi.get(self, "update_types")

    @update_types.setter
    def update_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "update_types", value)

    @property
    @pulumi.getter(name="workRequestDetails")
    def work_request_details(self) -> Optional[pulumi.Input['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']]:
        """
        Provides the name and description of the job.
        """
        return pulumi.get(self, "work_request_details")

    @work_request_details.setter
    def work_request_details(self, value: Optional[pulumi.Input['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']]):
        pulumi.set(self, "work_request_details", value)


@pulumi.input_type
class _ManagedInstanceGroupUpdateAllPackagesManagementState:
    def __init__(__self__, *,
                 managed_instance_group_id: Optional[pulumi.Input[str]] = None,
                 update_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 work_request_details: Optional[pulumi.Input['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']] = None):
        """
        Input properties used for looking up and filtering ManagedInstanceGroupUpdateAllPackagesManagement resources.
        :param pulumi.Input[str] managed_instance_group_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] update_types: The type of updates to be applied.
        :param pulumi.Input['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs'] work_request_details: Provides the name and description of the job.
        """
        if managed_instance_group_id is not None:
            pulumi.set(__self__, "managed_instance_group_id", managed_instance_group_id)
        if update_types is not None:
            pulumi.set(__self__, "update_types", update_types)
        if work_request_details is not None:
            pulumi.set(__self__, "work_request_details", work_request_details)

    @property
    @pulumi.getter(name="managedInstanceGroupId")
    def managed_instance_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
        """
        return pulumi.get(self, "managed_instance_group_id")

    @managed_instance_group_id.setter
    def managed_instance_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_instance_group_id", value)

    @property
    @pulumi.getter(name="updateTypes")
    def update_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The type of updates to be applied.
        """
        return pulumi.get(self, "update_types")

    @update_types.setter
    def update_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "update_types", value)

    @property
    @pulumi.getter(name="workRequestDetails")
    def work_request_details(self) -> Optional[pulumi.Input['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']]:
        """
        Provides the name and description of the job.
        """
        return pulumi.get(self, "work_request_details")

    @work_request_details.setter
    def work_request_details(self, value: Optional[pulumi.Input['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']]):
        pulumi.set(self, "work_request_details", value)


class ManagedInstanceGroupUpdateAllPackagesManagement(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 managed_instance_group_id: Optional[pulumi.Input[str]] = None,
                 update_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 work_request_details: Optional[pulumi.Input[pulumi.InputType['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']]] = None,
                 __props__=None):
        """
        This resource provides the Managed Instance Group Update All Packages Management resource in Oracle Cloud Infrastructure Os Management Hub service.

        Updates all packages on each managed instance in the specified managed instance group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_managed_instance_group_update_all_packages_management = oci.os_management_hub.ManagedInstanceGroupUpdateAllPackagesManagement("test_managed_instance_group_update_all_packages_management",
            managed_instance_group_id=test_managed_instance_group["id"],
            update_types=managed_instance_group_update_all_packages_management_update_types,
            work_request_details=oci.os_management_hub.ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs(
                description=managed_instance_group_update_all_packages_management_work_request_details_description,
                display_name=managed_instance_group_update_all_packages_management_work_request_details_display_name,
            ))
        ```

        ## Import

        ManagedInstanceGroupUpdateAllPackagesManagement can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:OsManagementHub/managedInstanceGroupUpdateAllPackagesManagement:ManagedInstanceGroupUpdateAllPackagesManagement test_managed_instance_group_update_all_packages_management "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] managed_instance_group_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] update_types: The type of updates to be applied.
        :param pulumi.Input[pulumi.InputType['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']] work_request_details: Provides the name and description of the job.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedInstanceGroupUpdateAllPackagesManagementArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Managed Instance Group Update All Packages Management resource in Oracle Cloud Infrastructure Os Management Hub service.

        Updates all packages on each managed instance in the specified managed instance group.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_managed_instance_group_update_all_packages_management = oci.os_management_hub.ManagedInstanceGroupUpdateAllPackagesManagement("test_managed_instance_group_update_all_packages_management",
            managed_instance_group_id=test_managed_instance_group["id"],
            update_types=managed_instance_group_update_all_packages_management_update_types,
            work_request_details=oci.os_management_hub.ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs(
                description=managed_instance_group_update_all_packages_management_work_request_details_description,
                display_name=managed_instance_group_update_all_packages_management_work_request_details_display_name,
            ))
        ```

        ## Import

        ManagedInstanceGroupUpdateAllPackagesManagement can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:OsManagementHub/managedInstanceGroupUpdateAllPackagesManagement:ManagedInstanceGroupUpdateAllPackagesManagement test_managed_instance_group_update_all_packages_management "id"
        ```

        :param str resource_name: The name of the resource.
        :param ManagedInstanceGroupUpdateAllPackagesManagementArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedInstanceGroupUpdateAllPackagesManagementArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 managed_instance_group_id: Optional[pulumi.Input[str]] = None,
                 update_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 work_request_details: Optional[pulumi.Input[pulumi.InputType['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedInstanceGroupUpdateAllPackagesManagementArgs.__new__(ManagedInstanceGroupUpdateAllPackagesManagementArgs)

            if managed_instance_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_group_id'")
            __props__.__dict__["managed_instance_group_id"] = managed_instance_group_id
            __props__.__dict__["update_types"] = update_types
            __props__.__dict__["work_request_details"] = work_request_details
        super(ManagedInstanceGroupUpdateAllPackagesManagement, __self__).__init__(
            'oci:OsManagementHub/managedInstanceGroupUpdateAllPackagesManagement:ManagedInstanceGroupUpdateAllPackagesManagement',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            managed_instance_group_id: Optional[pulumi.Input[str]] = None,
            update_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            work_request_details: Optional[pulumi.Input[pulumi.InputType['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']]] = None) -> 'ManagedInstanceGroupUpdateAllPackagesManagement':
        """
        Get an existing ManagedInstanceGroupUpdateAllPackagesManagement resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] managed_instance_group_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] update_types: The type of updates to be applied.
        :param pulumi.Input[pulumi.InputType['ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetailsArgs']] work_request_details: Provides the name and description of the job.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ManagedInstanceGroupUpdateAllPackagesManagementState.__new__(_ManagedInstanceGroupUpdateAllPackagesManagementState)

        __props__.__dict__["managed_instance_group_id"] = managed_instance_group_id
        __props__.__dict__["update_types"] = update_types
        __props__.__dict__["work_request_details"] = work_request_details
        return ManagedInstanceGroupUpdateAllPackagesManagement(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="managedInstanceGroupId")
    def managed_instance_group_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
        """
        return pulumi.get(self, "managed_instance_group_id")

    @property
    @pulumi.getter(name="updateTypes")
    def update_types(self) -> pulumi.Output[Sequence[str]]:
        """
        The type of updates to be applied.
        """
        return pulumi.get(self, "update_types")

    @property
    @pulumi.getter(name="workRequestDetails")
    def work_request_details(self) -> pulumi.Output['outputs.ManagedInstanceGroupUpdateAllPackagesManagementWorkRequestDetails']:
        """
        Provides the name and description of the job.
        """
        return pulumi.get(self, "work_request_details")

