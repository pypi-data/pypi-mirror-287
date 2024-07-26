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

__all__ = [
    'GetPrivateEndpointsResult',
    'AwaitableGetPrivateEndpointsResult',
    'get_private_endpoints',
    'get_private_endpoints_output',
]

@pulumi.output_type
class GetPrivateEndpointsResult:
    """
    A collection of values returned by getPrivateEndpoints.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, private_endpoint_collections=None, private_endpoint_id=None, vcn_id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if private_endpoint_collections and not isinstance(private_endpoint_collections, list):
            raise TypeError("Expected argument 'private_endpoint_collections' to be a list")
        pulumi.set(__self__, "private_endpoint_collections", private_endpoint_collections)
        if private_endpoint_id and not isinstance(private_endpoint_id, str):
            raise TypeError("Expected argument 'private_endpoint_id' to be a str")
        pulumi.set(__self__, "private_endpoint_id", private_endpoint_id)
        if vcn_id and not isinstance(vcn_id, str):
            raise TypeError("Expected argument 'vcn_id' to be a str")
        pulumi.set(__self__, "vcn_id", vcn_id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing this private endpoint details.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetPrivateEndpointsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="privateEndpointCollections")
    def private_endpoint_collections(self) -> Sequence['outputs.GetPrivateEndpointsPrivateEndpointCollectionResult']:
        """
        The list of private_endpoint_collection.
        """
        return pulumi.get(self, "private_endpoint_collections")

    @property
    @pulumi.getter(name="privateEndpointId")
    def private_endpoint_id(self) -> Optional[str]:
        return pulumi.get(self, "private_endpoint_id")

    @property
    @pulumi.getter(name="vcnId")
    def vcn_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN for the private endpoint.
        """
        return pulumi.get(self, "vcn_id")


class AwaitableGetPrivateEndpointsResult(GetPrivateEndpointsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateEndpointsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            private_endpoint_collections=self.private_endpoint_collections,
            private_endpoint_id=self.private_endpoint_id,
            vcn_id=self.vcn_id)


def get_private_endpoints(compartment_id: Optional[str] = None,
                          display_name: Optional[str] = None,
                          filters: Optional[Sequence[pulumi.InputType['GetPrivateEndpointsFilterArgs']]] = None,
                          private_endpoint_id: Optional[str] = None,
                          vcn_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateEndpointsResult:
    """
    This data source provides the list of Private Endpoints in Oracle Cloud Infrastructure Resource Manager service.

    Lists private endpoints according to the specified filter.
    - For `compartmentId`, lists all private endpoint in the matching compartment.
    - For `privateEndpointId`, lists the matching private endpoint.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_private_endpoints = oci.ResourceManager.get_private_endpoints(compartment_id=compartment_id,
        display_name=private_endpoint_display_name,
        private_endpoint_id=test_private_endpoint["id"],
        vcn_id=test_vcn["id"])
    ```


    :param str compartment_id: A filter to return only resources that exist in the compartment, identified by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.
    :param str private_endpoint_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private endpoint.
    :param str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['privateEndpointId'] = private_endpoint_id
    __args__['vcnId'] = vcn_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ResourceManager/getPrivateEndpoints:getPrivateEndpoints', __args__, opts=opts, typ=GetPrivateEndpointsResult).value

    return AwaitableGetPrivateEndpointsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        private_endpoint_collections=pulumi.get(__ret__, 'private_endpoint_collections'),
        private_endpoint_id=pulumi.get(__ret__, 'private_endpoint_id'),
        vcn_id=pulumi.get(__ret__, 'vcn_id'))


@_utilities.lift_output_func(get_private_endpoints)
def get_private_endpoints_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                 display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetPrivateEndpointsFilterArgs']]]]] = None,
                                 private_endpoint_id: Optional[pulumi.Input[Optional[str]]] = None,
                                 vcn_id: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateEndpointsResult]:
    """
    This data source provides the list of Private Endpoints in Oracle Cloud Infrastructure Resource Manager service.

    Lists private endpoints according to the specified filter.
    - For `compartmentId`, lists all private endpoint in the matching compartment.
    - For `privateEndpointId`, lists the matching private endpoint.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_private_endpoints = oci.ResourceManager.get_private_endpoints(compartment_id=compartment_id,
        display_name=private_endpoint_display_name,
        private_endpoint_id=test_private_endpoint["id"],
        vcn_id=test_vcn["id"])
    ```


    :param str compartment_id: A filter to return only resources that exist in the compartment, identified by [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    :param str display_name: A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.
    :param str private_endpoint_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the private endpoint.
    :param str vcn_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
    """
    ...
