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
    'GetExternalListenersResult',
    'AwaitableGetExternalListenersResult',
    'get_external_listeners',
    'get_external_listeners_output',
]

@pulumi.output_type
class GetExternalListenersResult:
    """
    A collection of values returned by getExternalListeners.
    """
    def __init__(__self__, compartment_id=None, display_name=None, external_db_system_id=None, external_listener_collections=None, filters=None, id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_db_system_id and not isinstance(external_db_system_id, str):
            raise TypeError("Expected argument 'external_db_system_id' to be a str")
        pulumi.set(__self__, "external_db_system_id", external_db_system_id)
        if external_listener_collections and not isinstance(external_listener_collections, list):
            raise TypeError("Expected argument 'external_listener_collections' to be a list")
        pulumi.set(__self__, "external_listener_collections", external_listener_collections)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the external database resides.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The user-friendly name for the database. The name does not have to be unique.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalDbSystemId")
    def external_db_system_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system that the listener is a part of.
        """
        return pulumi.get(self, "external_db_system_id")

    @property
    @pulumi.getter(name="externalListenerCollections")
    def external_listener_collections(self) -> Sequence['outputs.GetExternalListenersExternalListenerCollectionResult']:
        """
        The list of external_listener_collection.
        """
        return pulumi.get(self, "external_listener_collections")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetExternalListenersFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetExternalListenersResult(GetExternalListenersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalListenersResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            external_db_system_id=self.external_db_system_id,
            external_listener_collections=self.external_listener_collections,
            filters=self.filters,
            id=self.id)


def get_external_listeners(compartment_id: Optional[str] = None,
                           display_name: Optional[str] = None,
                           external_db_system_id: Optional[str] = None,
                           filters: Optional[Sequence[pulumi.InputType['GetExternalListenersFilterArgs']]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalListenersResult:
    """
    This data source provides the list of External Listeners in Oracle Cloud Infrastructure Database Management service.

    Lists the listeners in the specified external DB system.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_listeners = oci.DatabaseManagement.get_external_listeners(compartment_id=compartment_id,
        display_name=external_listener_display_name,
        external_db_system_id=test_external_db_system["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to only return the resources that match the entire display name.
    :param str external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['externalDbSystemId'] = external_db_system_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getExternalListeners:getExternalListeners', __args__, opts=opts, typ=GetExternalListenersResult).value

    return AwaitableGetExternalListenersResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_db_system_id=pulumi.get(__ret__, 'external_db_system_id'),
        external_listener_collections=pulumi.get(__ret__, 'external_listener_collections'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_external_listeners)
def get_external_listeners_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                  display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                  external_db_system_id: Optional[pulumi.Input[Optional[str]]] = None,
                                  filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetExternalListenersFilterArgs']]]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalListenersResult]:
    """
    This data source provides the list of External Listeners in Oracle Cloud Infrastructure Database Management service.

    Lists the listeners in the specified external DB system.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_listeners = oci.DatabaseManagement.get_external_listeners(compartment_id=compartment_id,
        display_name=external_listener_display_name,
        external_db_system_id=test_external_db_system["id"])
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: A filter to only return the resources that match the entire display name.
    :param str external_db_system_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the external DB system.
    """
    ...
