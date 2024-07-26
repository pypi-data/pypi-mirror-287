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
    'GetBackendsResult',
    'AwaitableGetBackendsResult',
    'get_backends',
    'get_backends_output',
]

@pulumi.output_type
class GetBackendsResult:
    """
    A collection of values returned by getBackends.
    """
    def __init__(__self__, backend_collections=None, backend_set_name=None, filters=None, id=None, network_load_balancer_id=None):
        if backend_collections and not isinstance(backend_collections, list):
            raise TypeError("Expected argument 'backend_collections' to be a list")
        pulumi.set(__self__, "backend_collections", backend_collections)
        if backend_set_name and not isinstance(backend_set_name, str):
            raise TypeError("Expected argument 'backend_set_name' to be a str")
        pulumi.set(__self__, "backend_set_name", backend_set_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if network_load_balancer_id and not isinstance(network_load_balancer_id, str):
            raise TypeError("Expected argument 'network_load_balancer_id' to be a str")
        pulumi.set(__self__, "network_load_balancer_id", network_load_balancer_id)

    @property
    @pulumi.getter(name="backendCollections")
    def backend_collections(self) -> Sequence['outputs.GetBackendsBackendCollectionResult']:
        """
        The list of backend_collection.
        """
        return pulumi.get(self, "backend_collections")

    @property
    @pulumi.getter(name="backendSetName")
    def backend_set_name(self) -> str:
        return pulumi.get(self, "backend_set_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetBackendsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="networkLoadBalancerId")
    def network_load_balancer_id(self) -> str:
        return pulumi.get(self, "network_load_balancer_id")


class AwaitableGetBackendsResult(GetBackendsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackendsResult(
            backend_collections=self.backend_collections,
            backend_set_name=self.backend_set_name,
            filters=self.filters,
            id=self.id,
            network_load_balancer_id=self.network_load_balancer_id)


def get_backends(backend_set_name: Optional[str] = None,
                 filters: Optional[Sequence[pulumi.InputType['GetBackendsFilterArgs']]] = None,
                 network_load_balancer_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackendsResult:
    """
    This data source provides the list of Backends in Oracle Cloud Infrastructure Network Load Balancer service.

    Lists the backend servers for a given network load balancer and backend set.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_backends = oci.NetworkLoadBalancer.get_backends(backend_set_name=test_backend_set["name"],
        network_load_balancer_id=test_network_load_balancer["id"])
    ```


    :param str backend_set_name: The name of the backend set associated with the backend servers.  Example: `example_backend_set`
    :param str network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
    """
    __args__ = dict()
    __args__['backendSetName'] = backend_set_name
    __args__['filters'] = filters
    __args__['networkLoadBalancerId'] = network_load_balancer_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:NetworkLoadBalancer/getBackends:getBackends', __args__, opts=opts, typ=GetBackendsResult).value

    return AwaitableGetBackendsResult(
        backend_collections=pulumi.get(__ret__, 'backend_collections'),
        backend_set_name=pulumi.get(__ret__, 'backend_set_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        network_load_balancer_id=pulumi.get(__ret__, 'network_load_balancer_id'))


@_utilities.lift_output_func(get_backends)
def get_backends_output(backend_set_name: Optional[pulumi.Input[str]] = None,
                        filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetBackendsFilterArgs']]]]] = None,
                        network_load_balancer_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackendsResult]:
    """
    This data source provides the list of Backends in Oracle Cloud Infrastructure Network Load Balancer service.

    Lists the backend servers for a given network load balancer and backend set.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_backends = oci.NetworkLoadBalancer.get_backends(backend_set_name=test_backend_set["name"],
        network_load_balancer_id=test_network_load_balancer["id"])
    ```


    :param str backend_set_name: The name of the backend set associated with the backend servers.  Example: `example_backend_set`
    :param str network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
    """
    ...
