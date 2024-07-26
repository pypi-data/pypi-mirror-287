# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetListenerResult',
    'AwaitableGetListenerResult',
    'get_listener',
    'get_listener_output',
]

@pulumi.output_type
class GetListenerResult:
    """
    A collection of values returned by getListener.
    """
    def __init__(__self__, default_backend_set_name=None, id=None, ip_version=None, is_ppv2enabled=None, listener_name=None, name=None, network_load_balancer_id=None, port=None, protocol=None):
        if default_backend_set_name and not isinstance(default_backend_set_name, str):
            raise TypeError("Expected argument 'default_backend_set_name' to be a str")
        pulumi.set(__self__, "default_backend_set_name", default_backend_set_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_version and not isinstance(ip_version, str):
            raise TypeError("Expected argument 'ip_version' to be a str")
        pulumi.set(__self__, "ip_version", ip_version)
        if is_ppv2enabled and not isinstance(is_ppv2enabled, bool):
            raise TypeError("Expected argument 'is_ppv2enabled' to be a bool")
        pulumi.set(__self__, "is_ppv2enabled", is_ppv2enabled)
        if listener_name and not isinstance(listener_name, str):
            raise TypeError("Expected argument 'listener_name' to be a str")
        pulumi.set(__self__, "listener_name", listener_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_load_balancer_id and not isinstance(network_load_balancer_id, str):
            raise TypeError("Expected argument 'network_load_balancer_id' to be a str")
        pulumi.set(__self__, "network_load_balancer_id", network_load_balancer_id)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="defaultBackendSetName")
    def default_backend_set_name(self) -> str:
        """
        The name of the associated backend set.  Example: `example_backend_set`
        """
        return pulumi.get(self, "default_backend_set_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> str:
        """
        IP version associated with the listener.
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter(name="isPpv2enabled")
    def is_ppv2enabled(self) -> bool:
        """
        Property to enable/disable PPv2 feature for this listener.
        """
        return pulumi.get(self, "is_ppv2enabled")

    @property
    @pulumi.getter(name="listenerName")
    def listener_name(self) -> str:
        return pulumi.get(self, "listener_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A friendly name for the listener. It must be unique and it cannot be changed.  Example: `example_listener`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkLoadBalancerId")
    def network_load_balancer_id(self) -> str:
        return pulumi.get(self, "network_load_balancer_id")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The communication port for the listener.  Example: `80`
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        The protocol on which the listener accepts connection requests. For public network load balancers, ANY protocol refers to TCP/UDP with the wildcard port. For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true). "ListNetworkLoadBalancersProtocols" API is deprecated and it will not return the updated values. Use the allowed values for the protocol instead.  Example: `TCP`
        """
        return pulumi.get(self, "protocol")


class AwaitableGetListenerResult(GetListenerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListenerResult(
            default_backend_set_name=self.default_backend_set_name,
            id=self.id,
            ip_version=self.ip_version,
            is_ppv2enabled=self.is_ppv2enabled,
            listener_name=self.listener_name,
            name=self.name,
            network_load_balancer_id=self.network_load_balancer_id,
            port=self.port,
            protocol=self.protocol)


def get_listener(listener_name: Optional[str] = None,
                 network_load_balancer_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListenerResult:
    """
    This data source provides details about a specific Listener resource in Oracle Cloud Infrastructure Network Load Balancer service.

    Retrieves listener properties associated with a given network load balancer and listener name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_listener = oci.NetworkLoadBalancer.get_listener(listener_name=test_listener_oci_network_load_balancer_listener["name"],
        network_load_balancer_id=test_network_load_balancer["id"])
    ```


    :param str listener_name: The name of the listener to get.  Example: `example_listener`
    :param str network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
    """
    __args__ = dict()
    __args__['listenerName'] = listener_name
    __args__['networkLoadBalancerId'] = network_load_balancer_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:NetworkLoadBalancer/getListener:getListener', __args__, opts=opts, typ=GetListenerResult).value

    return AwaitableGetListenerResult(
        default_backend_set_name=pulumi.get(__ret__, 'default_backend_set_name'),
        id=pulumi.get(__ret__, 'id'),
        ip_version=pulumi.get(__ret__, 'ip_version'),
        is_ppv2enabled=pulumi.get(__ret__, 'is_ppv2enabled'),
        listener_name=pulumi.get(__ret__, 'listener_name'),
        name=pulumi.get(__ret__, 'name'),
        network_load_balancer_id=pulumi.get(__ret__, 'network_load_balancer_id'),
        port=pulumi.get(__ret__, 'port'),
        protocol=pulumi.get(__ret__, 'protocol'))


@_utilities.lift_output_func(get_listener)
def get_listener_output(listener_name: Optional[pulumi.Input[str]] = None,
                        network_load_balancer_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetListenerResult]:
    """
    This data source provides details about a specific Listener resource in Oracle Cloud Infrastructure Network Load Balancer service.

    Retrieves listener properties associated with a given network load balancer and listener name.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_listener = oci.NetworkLoadBalancer.get_listener(listener_name=test_listener_oci_network_load_balancer_listener["name"],
        network_load_balancer_id=test_network_load_balancer["id"])
    ```


    :param str listener_name: The name of the listener to get.  Example: `example_listener`
    :param str network_load_balancer_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
    """
    ...
