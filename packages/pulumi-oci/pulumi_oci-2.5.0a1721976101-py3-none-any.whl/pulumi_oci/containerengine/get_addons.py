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
    'GetAddonsResult',
    'AwaitableGetAddonsResult',
    'get_addons',
    'get_addons_output',
]

@pulumi.output_type
class GetAddonsResult:
    """
    A collection of values returned by getAddons.
    """
    def __init__(__self__, addons=None, cluster_id=None, filters=None, id=None):
        if addons and not isinstance(addons, list):
            raise TypeError("Expected argument 'addons' to be a list")
        pulumi.set(__self__, "addons", addons)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def addons(self) -> Sequence['outputs.GetAddonsAddonResult']:
        """
        The list of addons.
        """
        return pulumi.get(self, "addons")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetAddonsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetAddonsResult(GetAddonsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddonsResult(
            addons=self.addons,
            cluster_id=self.cluster_id,
            filters=self.filters,
            id=self.id)


def get_addons(cluster_id: Optional[str] = None,
               filters: Optional[Sequence[pulumi.InputType['GetAddonsFilterArgs']]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAddonsResult:
    """
    This data source provides the list of Addons in Oracle Cloud Infrastructure Container Engine service.

    List addon for a provisioned cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_addons = oci.ContainerEngine.get_addons(cluster_id=test_cluster["id"])
    ```


    :param str cluster_id: The OCID of the cluster.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ContainerEngine/getAddons:getAddons', __args__, opts=opts, typ=GetAddonsResult).value

    return AwaitableGetAddonsResult(
        addons=pulumi.get(__ret__, 'addons'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_addons)
def get_addons_output(cluster_id: Optional[pulumi.Input[str]] = None,
                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetAddonsFilterArgs']]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAddonsResult]:
    """
    This data source provides the list of Addons in Oracle Cloud Infrastructure Container Engine service.

    List addon for a provisioned cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_addons = oci.ContainerEngine.get_addons(cluster_id=test_cluster["id"])
    ```


    :param str cluster_id: The OCID of the cluster.
    """
    ...
