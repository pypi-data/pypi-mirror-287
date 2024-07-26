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
    'GetListingsResult',
    'AwaitableGetListingsResult',
    'get_listings',
    'get_listings_output',
]

@pulumi.output_type
class GetListingsResult:
    """
    A collection of values returned by getListings.
    """
    def __init__(__self__, categories=None, compartment_id=None, filters=None, id=None, image_id=None, is_featured=None, listing_id=None, listing_types=None, listings=None, names=None, operating_systems=None, package_type=None, pricings=None, publisher_id=None):
        if categories and not isinstance(categories, list):
            raise TypeError("Expected argument 'categories' to be a list")
        pulumi.set(__self__, "categories", categories)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if is_featured and not isinstance(is_featured, bool):
            raise TypeError("Expected argument 'is_featured' to be a bool")
        pulumi.set(__self__, "is_featured", is_featured)
        if listing_id and not isinstance(listing_id, str):
            raise TypeError("Expected argument 'listing_id' to be a str")
        pulumi.set(__self__, "listing_id", listing_id)
        if listing_types and not isinstance(listing_types, list):
            raise TypeError("Expected argument 'listing_types' to be a list")
        pulumi.set(__self__, "listing_types", listing_types)
        if listings and not isinstance(listings, list):
            raise TypeError("Expected argument 'listings' to be a list")
        pulumi.set(__self__, "listings", listings)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if operating_systems and not isinstance(operating_systems, list):
            raise TypeError("Expected argument 'operating_systems' to be a list")
        pulumi.set(__self__, "operating_systems", operating_systems)
        if package_type and not isinstance(package_type, str):
            raise TypeError("Expected argument 'package_type' to be a str")
        pulumi.set(__self__, "package_type", package_type)
        if pricings and not isinstance(pricings, list):
            raise TypeError("Expected argument 'pricings' to be a list")
        pulumi.set(__self__, "pricings", pricings)
        if publisher_id and not isinstance(publisher_id, str):
            raise TypeError("Expected argument 'publisher_id' to be a str")
        pulumi.set(__self__, "publisher_id", publisher_id)

    @property
    @pulumi.getter
    def categories(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetListingsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[str]:
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="isFeatured")
    def is_featured(self) -> Optional[bool]:
        """
        Indicates whether the listing is included in Featured Listings.
        """
        return pulumi.get(self, "is_featured")

    @property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> Optional[str]:
        return pulumi.get(self, "listing_id")

    @property
    @pulumi.getter(name="listingTypes")
    def listing_types(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "listing_types")

    @property
    @pulumi.getter
    def listings(self) -> Sequence['outputs.GetListingsListingResult']:
        """
        The list of listings.
        """
        return pulumi.get(self, "listings")

    @property
    @pulumi.getter
    def names(self) -> Optional[Sequence[str]]:
        """
        Text that describes the resource.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="operatingSystems")
    def operating_systems(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "operating_systems")

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> Optional[str]:
        """
        The listing's package type.
        """
        return pulumi.get(self, "package_type")

    @property
    @pulumi.getter
    def pricings(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "pricings")

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> Optional[str]:
        return pulumi.get(self, "publisher_id")


class AwaitableGetListingsResult(GetListingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListingsResult(
            categories=self.categories,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            image_id=self.image_id,
            is_featured=self.is_featured,
            listing_id=self.listing_id,
            listing_types=self.listing_types,
            listings=self.listings,
            names=self.names,
            operating_systems=self.operating_systems,
            package_type=self.package_type,
            pricings=self.pricings,
            publisher_id=self.publisher_id)


def get_listings(categories: Optional[Sequence[str]] = None,
                 compartment_id: Optional[str] = None,
                 filters: Optional[Sequence[pulumi.InputType['GetListingsFilterArgs']]] = None,
                 image_id: Optional[str] = None,
                 is_featured: Optional[bool] = None,
                 listing_id: Optional[str] = None,
                 listing_types: Optional[Sequence[str]] = None,
                 names: Optional[Sequence[str]] = None,
                 operating_systems: Optional[Sequence[str]] = None,
                 package_type: Optional[str] = None,
                 pricings: Optional[Sequence[str]] = None,
                 publisher_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListingsResult:
    """
    This data source provides the list of Listings in Oracle Cloud Infrastructure Marketplace service.

    Gets a list of listings from Oracle Cloud Infrastructure Marketplace by searching keywords and
    filtering according to listing attributes.

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

    test_listings = oci.Marketplace.get_listings(categories=listing_category,
        compartment_id=compartment_id,
        image_id=test_image["id"],
        is_featured=listing_is_featured,
        listing_id=test_listing["id"],
        listing_types=listing_listing_types,
        names=listing_name,
        operating_systems=listing_operating_systems,
        package_type=listing_package_type,
        pricings=listing_pricing,
        publisher_id=test_publisher["id"])
    ```


    :param Sequence[str] categories: Name of the product category or categories. If you specify multiple categories, then Marketplace returns any listing with one or more matching categories.
    :param str compartment_id: The unique identifier for the compartment. It is mandatory when used in non-commercial realms.
    :param str image_id: The image identifier of the listing.
    :param bool is_featured: Indicates whether to show only featured listings. If this is set to `false` or is omitted, then all listings will be returned.
    :param str listing_id: The unique identifier for the listing.
    :param Sequence[str] listing_types: The type of the listing.
    :param Sequence[str] names: The name of the listing.
    :param Sequence[str] operating_systems: The operating system of the listing.
    :param str package_type: A filter to return only packages that match the given package type exactly.
    :param Sequence[str] pricings: Name of the pricing type. If multiple pricing types are provided, then any listing with one or more matching pricing models will be returned.
    :param str publisher_id: Limit results to just this publisher.
    """
    __args__ = dict()
    __args__['categories'] = categories
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['imageId'] = image_id
    __args__['isFeatured'] = is_featured
    __args__['listingId'] = listing_id
    __args__['listingTypes'] = listing_types
    __args__['names'] = names
    __args__['operatingSystems'] = operating_systems
    __args__['packageType'] = package_type
    __args__['pricings'] = pricings
    __args__['publisherId'] = publisher_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Marketplace/getListings:getListings', __args__, opts=opts, typ=GetListingsResult).value

    return AwaitableGetListingsResult(
        categories=pulumi.get(__ret__, 'categories'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        image_id=pulumi.get(__ret__, 'image_id'),
        is_featured=pulumi.get(__ret__, 'is_featured'),
        listing_id=pulumi.get(__ret__, 'listing_id'),
        listing_types=pulumi.get(__ret__, 'listing_types'),
        listings=pulumi.get(__ret__, 'listings'),
        names=pulumi.get(__ret__, 'names'),
        operating_systems=pulumi.get(__ret__, 'operating_systems'),
        package_type=pulumi.get(__ret__, 'package_type'),
        pricings=pulumi.get(__ret__, 'pricings'),
        publisher_id=pulumi.get(__ret__, 'publisher_id'))


@_utilities.lift_output_func(get_listings)
def get_listings_output(categories: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                        compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                        filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetListingsFilterArgs']]]]] = None,
                        image_id: Optional[pulumi.Input[Optional[str]]] = None,
                        is_featured: Optional[pulumi.Input[Optional[bool]]] = None,
                        listing_id: Optional[pulumi.Input[Optional[str]]] = None,
                        listing_types: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                        names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                        operating_systems: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                        package_type: Optional[pulumi.Input[Optional[str]]] = None,
                        pricings: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                        publisher_id: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetListingsResult]:
    """
    This data source provides the list of Listings in Oracle Cloud Infrastructure Marketplace service.

    Gets a list of listings from Oracle Cloud Infrastructure Marketplace by searching keywords and
    filtering according to listing attributes.

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

    test_listings = oci.Marketplace.get_listings(categories=listing_category,
        compartment_id=compartment_id,
        image_id=test_image["id"],
        is_featured=listing_is_featured,
        listing_id=test_listing["id"],
        listing_types=listing_listing_types,
        names=listing_name,
        operating_systems=listing_operating_systems,
        package_type=listing_package_type,
        pricings=listing_pricing,
        publisher_id=test_publisher["id"])
    ```


    :param Sequence[str] categories: Name of the product category or categories. If you specify multiple categories, then Marketplace returns any listing with one or more matching categories.
    :param str compartment_id: The unique identifier for the compartment. It is mandatory when used in non-commercial realms.
    :param str image_id: The image identifier of the listing.
    :param bool is_featured: Indicates whether to show only featured listings. If this is set to `false` or is omitted, then all listings will be returned.
    :param str listing_id: The unique identifier for the listing.
    :param Sequence[str] listing_types: The type of the listing.
    :param Sequence[str] names: The name of the listing.
    :param Sequence[str] operating_systems: The operating system of the listing.
    :param str package_type: A filter to return only packages that match the given package type exactly.
    :param Sequence[str] pricings: Name of the pricing type. If multiple pricing types are provided, then any listing with one or more matching pricing models will be returned.
    :param str publisher_id: Limit results to just this publisher.
    """
    ...
