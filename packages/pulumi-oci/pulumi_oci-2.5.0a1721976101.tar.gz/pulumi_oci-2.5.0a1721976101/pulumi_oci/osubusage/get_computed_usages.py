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
    'GetComputedUsagesResult',
    'AwaitableGetComputedUsagesResult',
    'get_computed_usages',
    'get_computed_usages_output',
]

@pulumi.output_type
class GetComputedUsagesResult:
    """
    A collection of values returned by getComputedUsages.
    """
    def __init__(__self__, compartment_id=None, computed_product=None, computed_usages=None, filters=None, id=None, parent_product=None, subscription_id=None, time_from=None, time_to=None, x_one_origin_region=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if computed_product and not isinstance(computed_product, str):
            raise TypeError("Expected argument 'computed_product' to be a str")
        pulumi.set(__self__, "computed_product", computed_product)
        if computed_usages and not isinstance(computed_usages, list):
            raise TypeError("Expected argument 'computed_usages' to be a list")
        pulumi.set(__self__, "computed_usages", computed_usages)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if parent_product and not isinstance(parent_product, str):
            raise TypeError("Expected argument 'parent_product' to be a str")
        pulumi.set(__self__, "parent_product", parent_product)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
        if time_from and not isinstance(time_from, str):
            raise TypeError("Expected argument 'time_from' to be a str")
        pulumi.set(__self__, "time_from", time_from)
        if time_to and not isinstance(time_to, str):
            raise TypeError("Expected argument 'time_to' to be a str")
        pulumi.set(__self__, "time_to", time_to)
        if x_one_origin_region and not isinstance(x_one_origin_region, str):
            raise TypeError("Expected argument 'x_one_origin_region' to be a str")
        pulumi.set(__self__, "x_one_origin_region", x_one_origin_region)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="computedProduct")
    def computed_product(self) -> Optional[str]:
        return pulumi.get(self, "computed_product")

    @property
    @pulumi.getter(name="computedUsages")
    def computed_usages(self) -> Sequence['outputs.GetComputedUsagesComputedUsageResult']:
        """
        The list of computed_usages.
        """
        return pulumi.get(self, "computed_usages")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetComputedUsagesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="parentProduct")
    def parent_product(self) -> Optional[str]:
        """
        Product description
        """
        return pulumi.get(self, "parent_product")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="timeFrom")
    def time_from(self) -> str:
        return pulumi.get(self, "time_from")

    @property
    @pulumi.getter(name="timeTo")
    def time_to(self) -> str:
        return pulumi.get(self, "time_to")

    @property
    @pulumi.getter(name="xOneOriginRegion")
    def x_one_origin_region(self) -> Optional[str]:
        return pulumi.get(self, "x_one_origin_region")


class AwaitableGetComputedUsagesResult(GetComputedUsagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComputedUsagesResult(
            compartment_id=self.compartment_id,
            computed_product=self.computed_product,
            computed_usages=self.computed_usages,
            filters=self.filters,
            id=self.id,
            parent_product=self.parent_product,
            subscription_id=self.subscription_id,
            time_from=self.time_from,
            time_to=self.time_to,
            x_one_origin_region=self.x_one_origin_region)


def get_computed_usages(compartment_id: Optional[str] = None,
                        computed_product: Optional[str] = None,
                        filters: Optional[Sequence[pulumi.InputType['GetComputedUsagesFilterArgs']]] = None,
                        parent_product: Optional[str] = None,
                        subscription_id: Optional[str] = None,
                        time_from: Optional[str] = None,
                        time_to: Optional[str] = None,
                        x_one_origin_region: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComputedUsagesResult:
    """
    This data source provides the list of Computed Usages in Oracle Cloud Infrastructure Osub Usage service.

    This is a collection API which returns a list of Computed Usages for given filters.


    :param str compartment_id: The OCID of the root compartment.
    :param str computed_product: Product part number for Computed Usage .
    :param str parent_product: Product part number for subscribed service line, called parent product.
    :param str subscription_id: Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM.
    :param str time_from: Initial date to filter Computed Usage data in SPM. In the case of non aggregated data the time period between of fromDate and toDate , expressed in RFC 3339 timestamp format.
    :param str time_to: Final date to filter Computed Usage data in SPM, expressed in RFC 3339 timestamp format.
    :param str x_one_origin_region: The Oracle Cloud Infrastructure home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['computedProduct'] = computed_product
    __args__['filters'] = filters
    __args__['parentProduct'] = parent_product
    __args__['subscriptionId'] = subscription_id
    __args__['timeFrom'] = time_from
    __args__['timeTo'] = time_to
    __args__['xOneOriginRegion'] = x_one_origin_region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsubUsage/getComputedUsages:getComputedUsages', __args__, opts=opts, typ=GetComputedUsagesResult).value

    return AwaitableGetComputedUsagesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        computed_product=pulumi.get(__ret__, 'computed_product'),
        computed_usages=pulumi.get(__ret__, 'computed_usages'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        parent_product=pulumi.get(__ret__, 'parent_product'),
        subscription_id=pulumi.get(__ret__, 'subscription_id'),
        time_from=pulumi.get(__ret__, 'time_from'),
        time_to=pulumi.get(__ret__, 'time_to'),
        x_one_origin_region=pulumi.get(__ret__, 'x_one_origin_region'))


@_utilities.lift_output_func(get_computed_usages)
def get_computed_usages_output(compartment_id: Optional[pulumi.Input[str]] = None,
                               computed_product: Optional[pulumi.Input[Optional[str]]] = None,
                               filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetComputedUsagesFilterArgs']]]]] = None,
                               parent_product: Optional[pulumi.Input[Optional[str]]] = None,
                               subscription_id: Optional[pulumi.Input[str]] = None,
                               time_from: Optional[pulumi.Input[str]] = None,
                               time_to: Optional[pulumi.Input[str]] = None,
                               x_one_origin_region: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComputedUsagesResult]:
    """
    This data source provides the list of Computed Usages in Oracle Cloud Infrastructure Osub Usage service.

    This is a collection API which returns a list of Computed Usages for given filters.


    :param str compartment_id: The OCID of the root compartment.
    :param str computed_product: Product part number for Computed Usage .
    :param str parent_product: Product part number for subscribed service line, called parent product.
    :param str subscription_id: Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM.
    :param str time_from: Initial date to filter Computed Usage data in SPM. In the case of non aggregated data the time period between of fromDate and toDate , expressed in RFC 3339 timestamp format.
    :param str time_to: Final date to filter Computed Usage data in SPM, expressed in RFC 3339 timestamp format.
    :param str x_one_origin_region: The Oracle Cloud Infrastructure home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.
    """
    ...
