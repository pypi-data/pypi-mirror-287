# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ManagementDashboardsImportArgs', 'ManagementDashboardsImport']

@pulumi.input_type
class ManagementDashboardsImportArgs:
    def __init__(__self__, *,
                 import_details: Optional[pulumi.Input[str]] = None,
                 import_details_file: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagementDashboardsImport resource.
        :param pulumi.Input[str] import_details: Array of Dashboards to import. The `import_details` is mandatory if `import_details_path` is not passed. Value should be stringified JSON of [ManagementDashboardImportDetails](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/managementdashboard/20200901/ManagementDashboardImportDetails/)
        """
        if import_details is not None:
            pulumi.set(__self__, "import_details", import_details)
        if import_details_file is not None:
            pulumi.set(__self__, "import_details_file", import_details_file)

    @property
    @pulumi.getter(name="importDetails")
    def import_details(self) -> Optional[pulumi.Input[str]]:
        """
        Array of Dashboards to import. The `import_details` is mandatory if `import_details_path` is not passed. Value should be stringified JSON of [ManagementDashboardImportDetails](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/managementdashboard/20200901/ManagementDashboardImportDetails/)
        """
        return pulumi.get(self, "import_details")

    @import_details.setter
    def import_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "import_details", value)

    @property
    @pulumi.getter(name="importDetailsFile")
    def import_details_file(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "import_details_file")

    @import_details_file.setter
    def import_details_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "import_details_file", value)


@pulumi.input_type
class _ManagementDashboardsImportState:
    def __init__(__self__, *,
                 import_details: Optional[pulumi.Input[str]] = None,
                 import_details_file: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ManagementDashboardsImport resources.
        :param pulumi.Input[str] import_details: Array of Dashboards to import. The `import_details` is mandatory if `import_details_path` is not passed. Value should be stringified JSON of [ManagementDashboardImportDetails](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/managementdashboard/20200901/ManagementDashboardImportDetails/)
        """
        if import_details is not None:
            pulumi.set(__self__, "import_details", import_details)
        if import_details_file is not None:
            pulumi.set(__self__, "import_details_file", import_details_file)

    @property
    @pulumi.getter(name="importDetails")
    def import_details(self) -> Optional[pulumi.Input[str]]:
        """
        Array of Dashboards to import. The `import_details` is mandatory if `import_details_path` is not passed. Value should be stringified JSON of [ManagementDashboardImportDetails](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/managementdashboard/20200901/ManagementDashboardImportDetails/)
        """
        return pulumi.get(self, "import_details")

    @import_details.setter
    def import_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "import_details", value)

    @property
    @pulumi.getter(name="importDetailsFile")
    def import_details_file(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "import_details_file")

    @import_details_file.setter
    def import_details_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "import_details_file", value)


class ManagementDashboardsImport(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 import_details: Optional[pulumi.Input[str]] = None,
                 import_details_file: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Management Dashboards Import resource in Oracle Cloud Infrastructure Management Dashboard service.

        Imports an array of dashboards and their saved searches.
        Here's an example of how you can use CLI to import a dashboard. For information on the details that must be passed to IMPORT, you can use the EXPORT API to obtain the Import.json file:
        `oci management-dashboard dashboard export --query data --export-dashboard-id "{\\"dashboardIds\\":[\\"ocid1.managementdashboard.oc1..dashboardId1\\"]}"  > Import.json`.
        Note that import API updates the resource if it already exists, and creates a new resource if it does not exist. To import to a different compartment, edit and change the compartmentId to the desired compartment OCID.
        Here's an example of how you can use CLI to import:
        `oci management-dashboard dashboard import --from-json file://Import.json`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_management_dashboards_import = oci.management_dashboard.ManagementDashboardsImport("test_management_dashboards_import",
            import_details=sample_import_details,
            import_details_file=sample_import_details_file_path)
        ```

        ## Import

        ManagementDashboardsImport can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:ManagementDashboard/managementDashboardsImport:ManagementDashboardsImport test_management_dashboards_import "id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] import_details: Array of Dashboards to import. The `import_details` is mandatory if `import_details_path` is not passed. Value should be stringified JSON of [ManagementDashboardImportDetails](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/managementdashboard/20200901/ManagementDashboardImportDetails/)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ManagementDashboardsImportArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Management Dashboards Import resource in Oracle Cloud Infrastructure Management Dashboard service.

        Imports an array of dashboards and their saved searches.
        Here's an example of how you can use CLI to import a dashboard. For information on the details that must be passed to IMPORT, you can use the EXPORT API to obtain the Import.json file:
        `oci management-dashboard dashboard export --query data --export-dashboard-id "{\\"dashboardIds\\":[\\"ocid1.managementdashboard.oc1..dashboardId1\\"]}"  > Import.json`.
        Note that import API updates the resource if it already exists, and creates a new resource if it does not exist. To import to a different compartment, edit and change the compartmentId to the desired compartment OCID.
        Here's an example of how you can use CLI to import:
        `oci management-dashboard dashboard import --from-json file://Import.json`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_management_dashboards_import = oci.management_dashboard.ManagementDashboardsImport("test_management_dashboards_import",
            import_details=sample_import_details,
            import_details_file=sample_import_details_file_path)
        ```

        ## Import

        ManagementDashboardsImport can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:ManagementDashboard/managementDashboardsImport:ManagementDashboardsImport test_management_dashboards_import "id"
        ```

        :param str resource_name: The name of the resource.
        :param ManagementDashboardsImportArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagementDashboardsImportArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 import_details: Optional[pulumi.Input[str]] = None,
                 import_details_file: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagementDashboardsImportArgs.__new__(ManagementDashboardsImportArgs)

            __props__.__dict__["import_details"] = import_details
            __props__.__dict__["import_details_file"] = import_details_file
        super(ManagementDashboardsImport, __self__).__init__(
            'oci:ManagementDashboard/managementDashboardsImport:ManagementDashboardsImport',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            import_details: Optional[pulumi.Input[str]] = None,
            import_details_file: Optional[pulumi.Input[str]] = None) -> 'ManagementDashboardsImport':
        """
        Get an existing ManagementDashboardsImport resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] import_details: Array of Dashboards to import. The `import_details` is mandatory if `import_details_path` is not passed. Value should be stringified JSON of [ManagementDashboardImportDetails](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/managementdashboard/20200901/ManagementDashboardImportDetails/)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ManagementDashboardsImportState.__new__(_ManagementDashboardsImportState)

        __props__.__dict__["import_details"] = import_details
        __props__.__dict__["import_details_file"] = import_details_file
        return ManagementDashboardsImport(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="importDetails")
    def import_details(self) -> pulumi.Output[Optional[str]]:
        """
        Array of Dashboards to import. The `import_details` is mandatory if `import_details_path` is not passed. Value should be stringified JSON of [ManagementDashboardImportDetails](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/managementdashboard/20200901/ManagementDashboardImportDetails/)
        """
        return pulumi.get(self, "import_details")

    @property
    @pulumi.getter(name="importDetailsFile")
    def import_details_file(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "import_details_file")

