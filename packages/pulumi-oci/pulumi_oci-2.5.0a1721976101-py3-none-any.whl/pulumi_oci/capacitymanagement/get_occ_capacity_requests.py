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
    'GetOccCapacityRequestsResult',
    'AwaitableGetOccCapacityRequestsResult',
    'get_occ_capacity_requests',
    'get_occ_capacity_requests_output',
]

@pulumi.output_type
class GetOccCapacityRequestsResult:
    """
    A collection of values returned by getOccCapacityRequests.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, namespace=None, occ_availability_catalog_id=None, occ_capacity_request_collections=None):
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
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if occ_availability_catalog_id and not isinstance(occ_availability_catalog_id, str):
            raise TypeError("Expected argument 'occ_availability_catalog_id' to be a str")
        pulumi.set(__self__, "occ_availability_catalog_id", occ_availability_catalog_id)
        if occ_capacity_request_collections and not isinstance(occ_capacity_request_collections, list):
            raise TypeError("Expected argument 'occ_capacity_request_collections' to be a list")
        pulumi.set(__self__, "occ_capacity_request_collections", occ_capacity_request_collections)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the tenancy from which the request was made.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the capacity request.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetOccCapacityRequestsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The OCID of the capacity request.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        The name of the Oracle Cloud Infrastructure service in consideration. For example, Compute, Exadata, and so on.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="occAvailabilityCatalogId")
    def occ_availability_catalog_id(self) -> Optional[str]:
        """
        The OCID of the availability catalog against which the capacity request was placed.
        """
        return pulumi.get(self, "occ_availability_catalog_id")

    @property
    @pulumi.getter(name="occCapacityRequestCollections")
    def occ_capacity_request_collections(self) -> Sequence['outputs.GetOccCapacityRequestsOccCapacityRequestCollectionResult']:
        """
        The list of occ_capacity_request_collection.
        """
        return pulumi.get(self, "occ_capacity_request_collections")


class AwaitableGetOccCapacityRequestsResult(GetOccCapacityRequestsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOccCapacityRequestsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            namespace=self.namespace,
            occ_availability_catalog_id=self.occ_availability_catalog_id,
            occ_capacity_request_collections=self.occ_capacity_request_collections)


def get_occ_capacity_requests(compartment_id: Optional[str] = None,
                              display_name: Optional[str] = None,
                              filters: Optional[Sequence[pulumi.InputType['GetOccCapacityRequestsFilterArgs']]] = None,
                              id: Optional[str] = None,
                              namespace: Optional[str] = None,
                              occ_availability_catalog_id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOccCapacityRequestsResult:
    """
    This data source provides the list of Occ Capacity Requests in Oracle Cloud Infrastructure Capacity Management service.

    Lists all capacity requests.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_occ_capacity_requests = oci.CapacityManagement.get_occ_capacity_requests(compartment_id=compartment_id,
        display_name=occ_capacity_request_display_name,
        id=occ_capacity_request_id,
        namespace=occ_capacity_request_namespace,
        occ_availability_catalog_id=test_occ_availability_catalog["id"])
    ```


    :param str compartment_id: The ocid of the compartment or tenancy in which resources are to be listed. This will also be used for authorization purposes.
    :param str display_name: A filter to return only the resources that match the entire display name. The match is not case sensitive.
    :param str id: A filter to return the list of capacity requests based on the OCID of the capacity request. This is done for the users who have INSPECT permission on the resource but do not have READ permission.
    :param str namespace: The namespace by which we would filter the list.
    :param str occ_availability_catalog_id: A filter to return the list of capacity requests based on the OCID of the availability catalog against which they were created.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['namespace'] = namespace
    __args__['occAvailabilityCatalogId'] = occ_availability_catalog_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:CapacityManagement/getOccCapacityRequests:getOccCapacityRequests', __args__, opts=opts, typ=GetOccCapacityRequestsResult).value

    return AwaitableGetOccCapacityRequestsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        namespace=pulumi.get(__ret__, 'namespace'),
        occ_availability_catalog_id=pulumi.get(__ret__, 'occ_availability_catalog_id'),
        occ_capacity_request_collections=pulumi.get(__ret__, 'occ_capacity_request_collections'))


@_utilities.lift_output_func(get_occ_capacity_requests)
def get_occ_capacity_requests_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                     display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                     filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetOccCapacityRequestsFilterArgs']]]]] = None,
                                     id: Optional[pulumi.Input[Optional[str]]] = None,
                                     namespace: Optional[pulumi.Input[Optional[str]]] = None,
                                     occ_availability_catalog_id: Optional[pulumi.Input[Optional[str]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOccCapacityRequestsResult]:
    """
    This data source provides the list of Occ Capacity Requests in Oracle Cloud Infrastructure Capacity Management service.

    Lists all capacity requests.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_occ_capacity_requests = oci.CapacityManagement.get_occ_capacity_requests(compartment_id=compartment_id,
        display_name=occ_capacity_request_display_name,
        id=occ_capacity_request_id,
        namespace=occ_capacity_request_namespace,
        occ_availability_catalog_id=test_occ_availability_catalog["id"])
    ```


    :param str compartment_id: The ocid of the compartment or tenancy in which resources are to be listed. This will also be used for authorization purposes.
    :param str display_name: A filter to return only the resources that match the entire display name. The match is not case sensitive.
    :param str id: A filter to return the list of capacity requests based on the OCID of the capacity request. This is done for the users who have INSPECT permission on the resource but do not have READ permission.
    :param str namespace: The namespace by which we would filter the list.
    :param str occ_availability_catalog_id: A filter to return the list of capacity requests based on the OCID of the availability catalog against which they were created.
    """
    ...
