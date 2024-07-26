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
    'GetCommitmentsResult',
    'AwaitableGetCommitmentsResult',
    'get_commitments',
    'get_commitments_output',
]

@pulumi.output_type
class GetCommitmentsResult:
    """
    A collection of values returned by getCommitments.
    """
    def __init__(__self__, commitments=None, compartment_id=None, filters=None, id=None, subscribed_service_id=None, x_one_gateway_subscription_id=None, x_one_origin_region=None):
        if commitments and not isinstance(commitments, list):
            raise TypeError("Expected argument 'commitments' to be a list")
        pulumi.set(__self__, "commitments", commitments)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if subscribed_service_id and not isinstance(subscribed_service_id, str):
            raise TypeError("Expected argument 'subscribed_service_id' to be a str")
        pulumi.set(__self__, "subscribed_service_id", subscribed_service_id)
        if x_one_gateway_subscription_id and not isinstance(x_one_gateway_subscription_id, str):
            raise TypeError("Expected argument 'x_one_gateway_subscription_id' to be a str")
        pulumi.set(__self__, "x_one_gateway_subscription_id", x_one_gateway_subscription_id)
        if x_one_origin_region and not isinstance(x_one_origin_region, str):
            raise TypeError("Expected argument 'x_one_origin_region' to be a str")
        pulumi.set(__self__, "x_one_origin_region", x_one_origin_region)

    @property
    @pulumi.getter
    def commitments(self) -> Sequence['outputs.GetCommitmentsCommitmentResult']:
        """
        The list of commitments.
        """
        return pulumi.get(self, "commitments")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetCommitmentsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="subscribedServiceId")
    def subscribed_service_id(self) -> str:
        return pulumi.get(self, "subscribed_service_id")

    @property
    @pulumi.getter(name="xOneGatewaySubscriptionId")
    def x_one_gateway_subscription_id(self) -> Optional[str]:
        return pulumi.get(self, "x_one_gateway_subscription_id")

    @property
    @pulumi.getter(name="xOneOriginRegion")
    def x_one_origin_region(self) -> Optional[str]:
        return pulumi.get(self, "x_one_origin_region")


class AwaitableGetCommitmentsResult(GetCommitmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCommitmentsResult(
            commitments=self.commitments,
            compartment_id=self.compartment_id,
            filters=self.filters,
            id=self.id,
            subscribed_service_id=self.subscribed_service_id,
            x_one_gateway_subscription_id=self.x_one_gateway_subscription_id,
            x_one_origin_region=self.x_one_origin_region)


def get_commitments(compartment_id: Optional[str] = None,
                    filters: Optional[Sequence[pulumi.InputType['GetCommitmentsFilterArgs']]] = None,
                    subscribed_service_id: Optional[str] = None,
                    x_one_gateway_subscription_id: Optional[str] = None,
                    x_one_origin_region: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCommitmentsResult:
    """
    This data source provides the list of Commitments in Oracle Cloud Infrastructure Osub Subscription service.

    This list API returns all commitments for a particular Subscribed Service

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_commitments = oci.OsubSubscription.get_commitments(compartment_id=compartment_id,
        subscribed_service_id=test_service["id"],
        x_one_gateway_subscription_id=commitment_x_one_gateway_subscription_id,
        x_one_origin_region=commitment_x_one_origin_region)
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str subscribed_service_id: This param is used to get the commitments for a particular subscribed service
    :param str x_one_gateway_subscription_id: This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is  to help on Gateway to API calls identification.
    :param str x_one_origin_region: The Oracle Cloud Infrastructure home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['filters'] = filters
    __args__['subscribedServiceId'] = subscribed_service_id
    __args__['xOneGatewaySubscriptionId'] = x_one_gateway_subscription_id
    __args__['xOneOriginRegion'] = x_one_origin_region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:OsubSubscription/getCommitments:getCommitments', __args__, opts=opts, typ=GetCommitmentsResult).value

    return AwaitableGetCommitmentsResult(
        commitments=pulumi.get(__ret__, 'commitments'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        subscribed_service_id=pulumi.get(__ret__, 'subscribed_service_id'),
        x_one_gateway_subscription_id=pulumi.get(__ret__, 'x_one_gateway_subscription_id'),
        x_one_origin_region=pulumi.get(__ret__, 'x_one_origin_region'))


@_utilities.lift_output_func(get_commitments)
def get_commitments_output(compartment_id: Optional[pulumi.Input[str]] = None,
                           filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetCommitmentsFilterArgs']]]]] = None,
                           subscribed_service_id: Optional[pulumi.Input[str]] = None,
                           x_one_gateway_subscription_id: Optional[pulumi.Input[Optional[str]]] = None,
                           x_one_origin_region: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCommitmentsResult]:
    """
    This data source provides the list of Commitments in Oracle Cloud Infrastructure Osub Subscription service.

    This list API returns all commitments for a particular Subscribed Service

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_commitments = oci.OsubSubscription.get_commitments(compartment_id=compartment_id,
        subscribed_service_id=test_service["id"],
        x_one_gateway_subscription_id=commitment_x_one_gateway_subscription_id,
        x_one_origin_region=commitment_x_one_origin_region)
    ```


    :param str compartment_id: The OCID of the compartment.
    :param str subscribed_service_id: This param is used to get the commitments for a particular subscribed service
    :param str x_one_gateway_subscription_id: This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is  to help on Gateway to API calls identification.
    :param str x_one_origin_region: The Oracle Cloud Infrastructure home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.
    """
    ...
