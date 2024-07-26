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
    'GetReportResult',
    'AwaitableGetReportResult',
    'get_report',
    'get_report_output',
]

@pulumi.output_type
class GetReportResult:
    """
    A collection of values returned by getReport.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, description=None, display_name=None, freeform_tags=None, id=None, mime_type=None, report_definition_id=None, report_id=None, state=None, system_tags=None, time_generated=None, type=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if mime_type and not isinstance(mime_type, str):
            raise TypeError("Expected argument 'mime_type' to be a str")
        pulumi.set(__self__, "mime_type", mime_type)
        if report_definition_id and not isinstance(report_definition_id, str):
            raise TypeError("Expected argument 'report_definition_id' to be a str")
        pulumi.set(__self__, "report_definition_id", report_definition_id)
        if report_id and not isinstance(report_id, str):
            raise TypeError("Expected argument 'report_id' to be a str")
        pulumi.set(__self__, "report_id", report_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_generated and not isinstance(time_generated, str):
            raise TypeError("Expected argument 'time_generated' to be a str")
        pulumi.set(__self__, "time_generated", time_generated)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment containing the report.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Specifies a description of the report.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Name of the report.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the report.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> str:
        """
        Specifies the format of report to be .xls or .pdf or .json
        """
        return pulumi.get(self, "mime_type")

    @property
    @pulumi.getter(name="reportDefinitionId")
    def report_definition_id(self) -> str:
        """
        The OCID of the report definition.
        """
        return pulumi.get(self, "report_definition_id")

    @property
    @pulumi.getter(name="reportId")
    def report_id(self) -> str:
        return pulumi.get(self, "report_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the audit report.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeGenerated")
    def time_generated(self) -> str:
        """
        Specifies the date and time the report was generated.
        """
        return pulumi.get(self, "time_generated")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the audit report.
        """
        return pulumi.get(self, "type")


class AwaitableGetReportResult(GetReportResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReportResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            mime_type=self.mime_type,
            report_definition_id=self.report_definition_id,
            report_id=self.report_id,
            state=self.state,
            system_tags=self.system_tags,
            time_generated=self.time_generated,
            type=self.type)


def get_report(report_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReportResult:
    """
    This data source provides details about a specific Report resource in Oracle Cloud Infrastructure Data Safe service.

    Gets a report by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_report = oci.DataSafe.get_report(report_id=test_report_oci_data_safe_report["id"])
    ```


    :param str report_id: Unique report identifier
    """
    __args__ = dict()
    __args__['reportId'] = report_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getReport:getReport', __args__, opts=opts, typ=GetReportResult).value

    return AwaitableGetReportResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        mime_type=pulumi.get(__ret__, 'mime_type'),
        report_definition_id=pulumi.get(__ret__, 'report_definition_id'),
        report_id=pulumi.get(__ret__, 'report_id'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_generated=pulumi.get(__ret__, 'time_generated'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_report)
def get_report_output(report_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReportResult]:
    """
    This data source provides details about a specific Report resource in Oracle Cloud Infrastructure Data Safe service.

    Gets a report by identifier

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_report = oci.DataSafe.get_report(report_id=test_report_oci_data_safe_report["id"])
    ```


    :param str report_id: Unique report identifier
    """
    ...
