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
    'GetAppCatalogListingsResult',
    'AwaitableGetAppCatalogListingsResult',
    'get_app_catalog_listings',
    'get_app_catalog_listings_output',
]

@pulumi.output_type
class GetAppCatalogListingsResult:
    """
    A collection of values returned by getAppCatalogListings.
    """
    def __init__(__self__, app_catalog_listings=None, display_name=None, filters=None, id=None, publisher_name=None, publisher_type=None):
        if app_catalog_listings and not isinstance(app_catalog_listings, list):
            raise TypeError("Expected argument 'app_catalog_listings' to be a list")
        pulumi.set(__self__, "app_catalog_listings", app_catalog_listings)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if publisher_name and not isinstance(publisher_name, str):
            raise TypeError("Expected argument 'publisher_name' to be a str")
        pulumi.set(__self__, "publisher_name", publisher_name)
        if publisher_type and not isinstance(publisher_type, str):
            raise TypeError("Expected argument 'publisher_type' to be a str")
        pulumi.set(__self__, "publisher_type", publisher_type)

    @property
    @pulumi.getter(name="appCatalogListings")
    def app_catalog_listings(self) -> Sequence['outputs.GetAppCatalogListingsAppCatalogListingResult']:
        """
        The list of app_catalog_listings.
        """
        return pulumi.get(self, "app_catalog_listings")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAppCatalogListingsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="publisherName")
    def publisher_name(self) -> Optional[str]:
        """
        The name of the publisher who published this listing.
        """
        return pulumi.get(self, "publisher_name")

    @property
    @pulumi.getter(name="publisherType")
    def publisher_type(self) -> Optional[str]:
        return pulumi.get(self, "publisher_type")


class AwaitableGetAppCatalogListingsResult(GetAppCatalogListingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppCatalogListingsResult(
            app_catalog_listings=self.app_catalog_listings,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            publisher_name=self.publisher_name,
            publisher_type=self.publisher_type)


def get_app_catalog_listings(display_name: Optional[str] = None,
                             filters: Optional[Sequence[pulumi.InputType['GetAppCatalogListingsFilterArgs']]] = None,
                             publisher_name: Optional[str] = None,
                             publisher_type: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppCatalogListingsResult:
    """
    This data source provides the list of App Catalog Listings in Oracle Cloud Infrastructure Core service.

    Lists the published listings.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_app_catalog_listings = oci.Core.get_app_catalog_listings(display_name=app_catalog_listing_display_name,
        publisher_name=app_catalog_listing_publisher_name,
        publisher_type=app_catalog_listing_publisher_type)
    ```


    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str publisher_name: A filter to return only the publisher that matches the given publisher name exactly.
    :param str publisher_type: A filter to return only publishers that match the given publisher type exactly. Valid types are OCI, ORACLE, TRUSTED, STANDARD.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['publisherName'] = publisher_name
    __args__['publisherType'] = publisher_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getAppCatalogListings:getAppCatalogListings', __args__, opts=opts, typ=GetAppCatalogListingsResult).value

    return AwaitableGetAppCatalogListingsResult(
        app_catalog_listings=pulumi.get(__ret__, 'app_catalog_listings'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        publisher_name=pulumi.get(__ret__, 'publisher_name'),
        publisher_type=pulumi.get(__ret__, 'publisher_type'))


@_utilities.lift_output_func(get_app_catalog_listings)
def get_app_catalog_listings_output(display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                    filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAppCatalogListingsFilterArgs']]]]] = None,
                                    publisher_name: Optional[pulumi.Input[Optional[str]]] = None,
                                    publisher_type: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppCatalogListingsResult]:
    """
    This data source provides the list of App Catalog Listings in Oracle Cloud Infrastructure Core service.

    Lists the published listings.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_app_catalog_listings = oci.Core.get_app_catalog_listings(display_name=app_catalog_listing_display_name,
        publisher_name=app_catalog_listing_publisher_name,
        publisher_type=app_catalog_listing_publisher_type)
    ```


    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str publisher_name: A filter to return only the publisher that matches the given publisher name exactly.
    :param str publisher_type: A filter to return only publishers that match the given publisher type exactly. Valid types are OCI, ORACLE, TRUSTED, STANDARD.
    """
    ...
