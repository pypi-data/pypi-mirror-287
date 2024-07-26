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
    'GetJavaDownloadsJavaLicenseAcceptanceRecordsResult',
    'AwaitableGetJavaDownloadsJavaLicenseAcceptanceRecordsResult',
    'get_java_downloads_java_license_acceptance_records',
    'get_java_downloads_java_license_acceptance_records_output',
]

@pulumi.output_type
class GetJavaDownloadsJavaLicenseAcceptanceRecordsResult:
    """
    A collection of values returned by getJavaDownloadsJavaLicenseAcceptanceRecords.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, java_license_acceptance_record_collections=None, license_type=None, search_by_user=None, status=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if java_license_acceptance_record_collections and not isinstance(java_license_acceptance_record_collections, list):
            raise TypeError("Expected argument 'java_license_acceptance_record_collections' to be a list")
        pulumi.set(__self__, "java_license_acceptance_record_collections", java_license_acceptance_record_collections)
        if license_type and not isinstance(license_type, str):
            raise TypeError("Expected argument 'license_type' to be a str")
        pulumi.set(__self__, "license_type", license_type)
        if search_by_user and not isinstance(search_by_user, str):
            raise TypeError("Expected argument 'search_by_user' to be a str")
        pulumi.set(__self__, "search_by_user", search_by_user)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The tenancy [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user accepting the license.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetJavaDownloadsJavaLicenseAcceptanceRecordsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the principal.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="javaLicenseAcceptanceRecordCollections")
    def java_license_acceptance_record_collections(self) -> Sequence['outputs.GetJavaDownloadsJavaLicenseAcceptanceRecordsJavaLicenseAcceptanceRecordCollectionResult']:
        """
        The list of java_license_acceptance_record_collection.
        """
        return pulumi.get(self, "java_license_acceptance_record_collections")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[str]:
        """
        License type associated with the acceptance.
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter(name="searchByUser")
    def search_by_user(self) -> Optional[str]:
        return pulumi.get(self, "search_by_user")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetJavaDownloadsJavaLicenseAcceptanceRecordsResult(GetJavaDownloadsJavaLicenseAcceptanceRecordsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJavaDownloadsJavaLicenseAcceptanceRecordsResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            java_license_acceptance_record_collections=self.java_license_acceptance_record_collections,
            license_type=self.license_type,
            search_by_user=self.search_by_user,
            status=self.status)


def get_java_downloads_java_license_acceptance_records(compartment_id: Optional[str] = None,
                                                       filters: Optional[Sequence[pulumi.InputType['GetJavaDownloadsJavaLicenseAcceptanceRecordsFilterArgs']]] = None,
                                                       id: Optional[str] = None,
                                                       license_type: Optional[str] = None,
                                                       search_by_user: Optional[str] = None,
                                                       status: Optional[str] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJavaDownloadsJavaLicenseAcceptanceRecordsResult:
    """
    This data source provides the list of Java License Acceptance Records in Oracle Cloud Infrastructure Jms Java Downloads service.

    Returns a list of all the Java license acceptance records in a tenancy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_java_license_acceptance_records = oci.Jms.get_java_downloads_java_license_acceptance_records(compartment_id=tenancy_ocid,
        id=java_license_acceptance_record_id,
        license_type=java_license_acceptance_record_license_type,
        search_by_user=java_license_acceptance_record_search_by_user,
        status=java_license_acceptance_record_status)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy.
    :param str id: Unique Java license acceptance record identifier.
    :param str license_type: Unique Java license type.
    :param str search_by_user: A filter to return only resources that match the user principal detail.  The search string can be any of the property values from the [Principal](https://docs.cloud.oracle.com/iaas/api/#/en/jms/latest/datatypes/Principal) object. This object is used as response datatype for the `createdBy` and `lastUpdatedBy` fields in applicable resource.
    :param str status: The status of license acceptance.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['licenseType'] = license_type
    __args__['searchByUser'] = search_by_user
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Jms/getJavaDownloadsJavaLicenseAcceptanceRecords:getJavaDownloadsJavaLicenseAcceptanceRecords', __args__, opts=opts, typ=GetJavaDownloadsJavaLicenseAcceptanceRecordsResult).value

    return AwaitableGetJavaDownloadsJavaLicenseAcceptanceRecordsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        java_license_acceptance_record_collections=pulumi.get(__ret__, 'java_license_acceptance_record_collections'),
        license_type=pulumi.get(__ret__, 'license_type'),
        search_by_user=pulumi.get(__ret__, 'search_by_user'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_java_downloads_java_license_acceptance_records)
def get_java_downloads_java_license_acceptance_records_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                                              filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetJavaDownloadsJavaLicenseAcceptanceRecordsFilterArgs']]]]] = None,
                                                              id: Optional[pulumi.Input[Optional[str]]] = None,
                                                              license_type: Optional[pulumi.Input[Optional[str]]] = None,
                                                              search_by_user: Optional[pulumi.Input[Optional[str]]] = None,
                                                              status: Optional[pulumi.Input[Optional[str]]] = None,
                                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJavaDownloadsJavaLicenseAcceptanceRecordsResult]:
    """
    This data source provides the list of Java License Acceptance Records in Oracle Cloud Infrastructure Jms Java Downloads service.

    Returns a list of all the Java license acceptance records in a tenancy.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_java_license_acceptance_records = oci.Jms.get_java_downloads_java_license_acceptance_records(compartment_id=tenancy_ocid,
        id=java_license_acceptance_record_id,
        license_type=java_license_acceptance_record_license_type,
        search_by_user=java_license_acceptance_record_search_by_user,
        status=java_license_acceptance_record_status)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy.
    :param str id: Unique Java license acceptance record identifier.
    :param str license_type: Unique Java license type.
    :param str search_by_user: A filter to return only resources that match the user principal detail.  The search string can be any of the property values from the [Principal](https://docs.cloud.oracle.com/iaas/api/#/en/jms/latest/datatypes/Principal) object. This object is used as response datatype for the `createdBy` and `lastUpdatedBy` fields in applicable resource.
    :param str status: The status of license acceptance.
    """
    ...
