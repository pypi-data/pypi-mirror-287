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
    'GetListingPackagesResult',
    'AwaitableGetListingPackagesResult',
    'get_listing_packages',
    'get_listing_packages_output',
]

@pulumi.output_type
class GetListingPackagesResult:
    """
    A collection of values returned by getListingPackages.
    """
    def __init__(__self__, compartment_id=None, filters=None, id=None, listing_id=None, listing_packages=None, package_type=None, package_version=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if listing_id and not isinstance(listing_id, str):
            raise TypeError("Expected argument 'listing_id' to be a str")
        pulumi.set(__self__, "listing_id", listing_id)
        if listing_packages and not isinstance(listing_packages, list):
            raise TypeError("Expected argument 'listing_packages' to be a list")
        pulumi.set(__self__, "listing_packages", listing_packages)
        if package_type and not isinstance(package_type, str):
            raise TypeError("Expected argument 'package_type' to be a str")
        pulumi.set(__self__, "package_type", package_type)
        if package_version and not isinstance(package_version, str):
            raise TypeError("Expected argument 'package_version' to be a str")
        pulumi.set(__self__, "package_version", package_version)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetListingPackagesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> str:
        """
        The ID of the listing that the specified package belongs to.
        """
        return pulumi.get(self, "listing_id")

    @property
    @pulumi.getter(name="listingPackages")
    def listing_packages(self) -> Sequence['outputs.GetListingPackagesListingPackageResult']:
        """
        The list of listing_packages.
        """
        return pulumi.get(self, "listing_packages")

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> Optional[str]:
        """
        The specified package's type.
        """
        return pulumi.get(self, "package_type")

    @property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> Optional[str]:
        return pulumi.get(self, "package_version")


class AwaitableGetListingPackagesResult(GetListingPackagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListingPackagesResult(
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            listing_id=self.listing_id,
            listing_packages=self.listing_packages,
            package_type=self.package_type,
            package_version=self.package_version)


def get_listing_packages(compartment_id: Optional[str] = None,
                         filters: Optional[Sequence[pulumi.InputType['GetListingPackagesFilterArgs']]] = None,
                         listing_id: Optional[str] = None,
                         package_type: Optional[str] = None,
                         package_version: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListingPackagesResult:
    """
    This data source provides the list of Listing Packages in Oracle Cloud Infrastructure Marketplace service.

    Gets the list of packages for a listing.

    If you plan to launch an instance from an image listing, you must first subscribe to the listing. When
    you launch the instance, you also need to provide the image ID of the listing resource version that you want.

    Subscribing to the listing requires you to first get a signature from the terms of use agreement for the
    listing resource version. To get the signature, issue a [GetAppCatalogListingAgreements](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements) API call.
    The [AppCatalogListingResourceVersionAgreements](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements) object, including
    its signature, is returned in the response. With the signature for the terms of use agreement for the desired
    listing resource version, create a subscription by issuing a
    [CreateAppCatalogSubscription](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription) API call.

    To get the image ID to launch an instance, issue a [GetAppCatalogListingResourceVersion](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion) API call.
    Lastly, to launch the instance, use the image ID of the listing resource version to issue a [LaunchInstance](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) API call.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_listing_packages = oci.Marketplace.get_listing_packages(listing_id=test_listing["id"],
        compartment_id=compartment_id,
        package_type=listing_package_package_type,
        package_version=listing_package_package_version)
    ```


    :param str compartment_id: The unique identifier for the compartment.
    :param str listing_id: The unique identifier for the listing.
    :param str package_type: A filter to return only packages that match the given package type exactly.
    :param str package_version: The version of the package. Package versions are unique within a listing.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['listingId'] = listing_id
    __args__['packageType'] = package_type
    __args__['packageVersion'] = package_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Marketplace/getListingPackages:getListingPackages', __args__, opts=opts, typ=GetListingPackagesResult).value

    return AwaitableGetListingPackagesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        listing_id=pulumi.get(__ret__, 'listing_id'),
        listing_packages=pulumi.get(__ret__, 'listing_packages'),
        package_type=pulumi.get(__ret__, 'package_type'),
        package_version=pulumi.get(__ret__, 'package_version'))


@_utilities.lift_output_func(get_listing_packages)
def get_listing_packages_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetListingPackagesFilterArgs']]]]] = None,
                                listing_id: Optional[pulumi.Input[str]] = None,
                                package_type: Optional[pulumi.Input[Optional[str]]] = None,
                                package_version: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetListingPackagesResult]:
    """
    This data source provides the list of Listing Packages in Oracle Cloud Infrastructure Marketplace service.

    Gets the list of packages for a listing.

    If you plan to launch an instance from an image listing, you must first subscribe to the listing. When
    you launch the instance, you also need to provide the image ID of the listing resource version that you want.

    Subscribing to the listing requires you to first get a signature from the terms of use agreement for the
    listing resource version. To get the signature, issue a [GetAppCatalogListingAgreements](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements) API call.
    The [AppCatalogListingResourceVersionAgreements](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements) object, including
    its signature, is returned in the response. With the signature for the terms of use agreement for the desired
    listing resource version, create a subscription by issuing a
    [CreateAppCatalogSubscription](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription) API call.

    To get the image ID to launch an instance, issue a [GetAppCatalogListingResourceVersion](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion) API call.
    Lastly, to launch the instance, use the image ID of the listing resource version to issue a [LaunchInstance](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) API call.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_listing_packages = oci.Marketplace.get_listing_packages(listing_id=test_listing["id"],
        compartment_id=compartment_id,
        package_type=listing_package_package_type,
        package_version=listing_package_package_version)
    ```


    :param str compartment_id: The unique identifier for the compartment.
    :param str listing_id: The unique identifier for the listing.
    :param str package_type: A filter to return only packages that match the given package type exactly.
    :param str package_version: The version of the package. Package versions are unique within a listing.
    """
    ...
