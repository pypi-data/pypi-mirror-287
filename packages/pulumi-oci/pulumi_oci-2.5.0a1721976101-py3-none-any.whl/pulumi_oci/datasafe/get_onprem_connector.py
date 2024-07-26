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
    'GetOnpremConnectorResult',
    'AwaitableGetOnpremConnectorResult',
    'get_onprem_connector',
    'get_onprem_connector_output',
]

@pulumi.output_type
class GetOnpremConnectorResult:
    """
    A collection of values returned by getOnpremConnector.
    """
    def __init__(__self__, available_version=None, compartment_id=None, created_version=None, defined_tags=None, description=None, display_name=None, freeform_tags=None, id=None, lifecycle_details=None, on_prem_connector_id=None, state=None, system_tags=None, time_created=None):
        if available_version and not isinstance(available_version, str):
            raise TypeError("Expected argument 'available_version' to be a str")
        pulumi.set(__self__, "available_version", available_version)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if created_version and not isinstance(created_version, str):
            raise TypeError("Expected argument 'created_version' to be a str")
        pulumi.set(__self__, "created_version", created_version)
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
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if on_prem_connector_id and not isinstance(on_prem_connector_id, str):
            raise TypeError("Expected argument 'on_prem_connector_id' to be a str")
        pulumi.set(__self__, "on_prem_connector_id", on_prem_connector_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)

    @property
    @pulumi.getter(name="availableVersion")
    def available_version(self) -> str:
        """
        Latest available version of the on-premises connector.
        """
        return pulumi.get(self, "available_version")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the on-premises connector.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="createdVersion")
    def created_version(self) -> str:
        """
        Created version of the on-premises connector.
        """
        return pulumi.get(self, "created_version")

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
        The description of the on-premises connector.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the on-premises connector.
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
        The OCID of the on-premises connector.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Details about the current state of the on-premises connector.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="onPremConnectorId")
    def on_prem_connector_id(self) -> str:
        return pulumi.get(self, "on_prem_connector_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the on-premises connector.
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
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the on-premises connector was created, in the format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_created")


class AwaitableGetOnpremConnectorResult(GetOnpremConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOnpremConnectorResult(
            available_version=self.available_version,
            compartment_id=self.compartment_id,
            created_version=self.created_version,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            on_prem_connector_id=self.on_prem_connector_id,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created)


def get_onprem_connector(on_prem_connector_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOnpremConnectorResult:
    """
    This data source provides details about a specific On Prem Connector resource in Oracle Cloud Infrastructure Data Safe service.

    Gets the details of the specified on-premises connector.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_on_prem_connector = oci.DataSafe.get_onprem_connector(on_prem_connector_id=test_on_prem_connector_oci_data_safe_on_prem_connector["id"])
    ```


    :param str on_prem_connector_id: The OCID of the on-premises connector.
    """
    __args__ = dict()
    __args__['onPremConnectorId'] = on_prem_connector_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getOnpremConnector:getOnpremConnector', __args__, opts=opts, typ=GetOnpremConnectorResult).value

    return AwaitableGetOnpremConnectorResult(
        available_version=pulumi.get(__ret__, 'available_version'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        created_version=pulumi.get(__ret__, 'created_version'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        on_prem_connector_id=pulumi.get(__ret__, 'on_prem_connector_id'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'))


@_utilities.lift_output_func(get_onprem_connector)
def get_onprem_connector_output(on_prem_connector_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOnpremConnectorResult]:
    """
    This data source provides details about a specific On Prem Connector resource in Oracle Cloud Infrastructure Data Safe service.

    Gets the details of the specified on-premises connector.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_on_prem_connector = oci.DataSafe.get_onprem_connector(on_prem_connector_id=test_on_prem_connector_oci_data_safe_on_prem_connector["id"])
    ```


    :param str on_prem_connector_id: The OCID of the on-premises connector.
    """
    ...
