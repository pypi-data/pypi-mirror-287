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
    'GetPrivateEndpointResult',
    'AwaitableGetPrivateEndpointResult',
    'get_private_endpoint',
    'get_private_endpoint_output',
]

@pulumi.output_type
class GetPrivateEndpointResult:
    """
    A collection of values returned by getPrivateEndpoint.
    """
    def __init__(__self__, compartment_id=None, created_by=None, data_science_private_endpoint_id=None, data_science_resource_type=None, defined_tags=None, description=None, display_name=None, fqdn=None, freeform_tags=None, id=None, lifecycle_details=None, nsg_ids=None, state=None, sub_domain=None, subnet_id=None, system_tags=None, time_created=None, time_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if data_science_private_endpoint_id and not isinstance(data_science_private_endpoint_id, str):
            raise TypeError("Expected argument 'data_science_private_endpoint_id' to be a str")
        pulumi.set(__self__, "data_science_private_endpoint_id", data_science_private_endpoint_id)
        if data_science_resource_type and not isinstance(data_science_resource_type, str):
            raise TypeError("Expected argument 'data_science_resource_type' to be a str")
        pulumi.set(__self__, "data_science_resource_type", data_science_resource_type)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if nsg_ids and not isinstance(nsg_ids, list):
            raise TypeError("Expected argument 'nsg_ids' to be a list")
        pulumi.set(__self__, "nsg_ids", nsg_ids)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if sub_domain and not isinstance(sub_domain, str):
            raise TypeError("Expected argument 'sub_domain' to be a str")
        pulumi.set(__self__, "sub_domain", sub_domain)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create private endpoint.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> str:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user that created the private endpoint.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="dataSciencePrivateEndpointId")
    def data_science_private_endpoint_id(self) -> str:
        return pulumi.get(self, "data_science_private_endpoint_id")

    @property
    @pulumi.getter(name="dataScienceResourceType")
    def data_science_resource_type(self) -> str:
        """
        Data Science resource type.
        """
        return pulumi.get(self, "data_science_resource_type")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A user friendly description. Avoid entering confidential information.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user friendly name. It doesn't have to be unique. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        Accesing the Data Science resource using FQDN.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of a private endpoint.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Details of the state of Data Science private endpoint.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="nsgIds")
    def nsg_ids(self) -> Sequence[str]:
        """
        An array of network security group OCIDs.
        """
        return pulumi.get(self, "nsg_ids")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the Data Science private endpoint.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subDomain")
    def sub_domain(self) -> str:
        return pulumi.get(self, "sub_domain")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The OCID of a subnet.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time that the Data Science private endpoint was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. Example: `2018-04-03T21:10:29.600Z`
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The date and time that the Data Science private endpoint was updated expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. Example: `2018-04-03T21:10:29.600Z`
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetPrivateEndpointResult(GetPrivateEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateEndpointResult(
            compartment_id=self.compartment_id,
            created_by=self.created_by,
            data_science_private_endpoint_id=self.data_science_private_endpoint_id,
            data_science_resource_type=self.data_science_resource_type,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            fqdn=self.fqdn,
            freeform_tags=self.freeform_tags,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            nsg_ids=self.nsg_ids,
            state=self.state,
            sub_domain=self.sub_domain,
            subnet_id=self.subnet_id,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_private_endpoint(data_science_private_endpoint_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateEndpointResult:
    """
    This data source provides details about a specific Data Science Private Endpoint resource in Oracle Cloud Infrastructure Data Science service.

    Retrieves an private endpoint using a `privateEndpointId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_data_science_private_endpoint = oci.DataScience.get_private_endpoint(data_science_private_endpoint_id=test_data_science_private_endpoint_oci_datascience_private_endpoint["id"])
    ```


    :param str data_science_private_endpoint_id: The unique ID for a Data Science private endpoint.
    """
    __args__ = dict()
    __args__['dataSciencePrivateEndpointId'] = data_science_private_endpoint_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataScience/getPrivateEndpoint:getPrivateEndpoint', __args__, opts=opts, typ=GetPrivateEndpointResult).value

    return AwaitableGetPrivateEndpointResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        created_by=pulumi.get(__ret__, 'created_by'),
        data_science_private_endpoint_id=pulumi.get(__ret__, 'data_science_private_endpoint_id'),
        data_science_resource_type=pulumi.get(__ret__, 'data_science_resource_type'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        fqdn=pulumi.get(__ret__, 'fqdn'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        nsg_ids=pulumi.get(__ret__, 'nsg_ids'),
        state=pulumi.get(__ret__, 'state'),
        sub_domain=pulumi.get(__ret__, 'sub_domain'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_private_endpoint)
def get_private_endpoint_output(data_science_private_endpoint_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateEndpointResult]:
    """
    This data source provides details about a specific Data Science Private Endpoint resource in Oracle Cloud Infrastructure Data Science service.

    Retrieves an private endpoint using a `privateEndpointId`.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_data_science_private_endpoint = oci.DataScience.get_private_endpoint(data_science_private_endpoint_id=test_data_science_private_endpoint_oci_datascience_private_endpoint["id"])
    ```


    :param str data_science_private_endpoint_id: The unique ID for a Data Science private endpoint.
    """
    ...
