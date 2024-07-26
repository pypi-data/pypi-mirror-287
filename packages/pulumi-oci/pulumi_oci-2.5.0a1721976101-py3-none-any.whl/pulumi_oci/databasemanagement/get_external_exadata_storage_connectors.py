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
    'GetExternalExadataStorageConnectorsResult',
    'AwaitableGetExternalExadataStorageConnectorsResult',
    'get_external_exadata_storage_connectors',
    'get_external_exadata_storage_connectors_output',
]

@pulumi.output_type
class GetExternalExadataStorageConnectorsResult:
    """
    A collection of values returned by getExternalExadataStorageConnectors.
    """
    def __init__(__self__, compartment_id=None, display_name=None, external_exadata_infrastructure_id=None, external_exadata_storage_connector_collections=None, filters=None, id=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_exadata_infrastructure_id and not isinstance(external_exadata_infrastructure_id, str):
            raise TypeError("Expected argument 'external_exadata_infrastructure_id' to be a str")
        pulumi.set(__self__, "external_exadata_infrastructure_id", external_exadata_infrastructure_id)
        if external_exadata_storage_connector_collections and not isinstance(external_exadata_storage_connector_collections, list):
            raise TypeError("Expected argument 'external_exadata_storage_connector_collections' to be a list")
        pulumi.set(__self__, "external_exadata_storage_connector_collections", external_exadata_storage_connector_collections)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The name of the Exadata resource. English letters, numbers, "-", "_" and "." only.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalExadataInfrastructureId")
    def external_exadata_infrastructure_id(self) -> str:
        return pulumi.get(self, "external_exadata_infrastructure_id")

    @property
    @pulumi.getter(name="externalExadataStorageConnectorCollections")
    def external_exadata_storage_connector_collections(self) -> Sequence['outputs.GetExternalExadataStorageConnectorsExternalExadataStorageConnectorCollectionResult']:
        """
        The list of external_exadata_storage_connector_collection.
        """
        return pulumi.get(self, "external_exadata_storage_connector_collections")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetExternalExadataStorageConnectorsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetExternalExadataStorageConnectorsResult(GetExternalExadataStorageConnectorsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalExadataStorageConnectorsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            external_exadata_infrastructure_id=self.external_exadata_infrastructure_id,
            external_exadata_storage_connector_collections=self.external_exadata_storage_connector_collections,
            filters=self.filters,
            id=self.id)


def get_external_exadata_storage_connectors(compartment_id: Optional[str] = None,
                                            display_name: Optional[str] = None,
                                            external_exadata_infrastructure_id: Optional[str] = None,
                                            filters: Optional[Sequence[pulumi.InputType['GetExternalExadataStorageConnectorsFilterArgs']]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalExadataStorageConnectorsResult:
    """
    This data source provides the list of External Exadata Storage Connectors in Oracle Cloud Infrastructure Database Management service.

    Lists the Exadata storage server connectors for the specified Exadata infrastructure.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_exadata_storage_connectors = oci.DatabaseManagement.get_external_exadata_storage_connectors(compartment_id=compartment_id,
        external_exadata_infrastructure_id=test_external_exadata_infrastructure["id"],
        display_name=external_exadata_storage_connector_display_name)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: The optional single value query filter parameter on the entity display name.
    :param str external_exadata_infrastructure_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['externalExadataInfrastructureId'] = external_exadata_infrastructure_id
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DatabaseManagement/getExternalExadataStorageConnectors:getExternalExadataStorageConnectors', __args__, opts=opts, typ=GetExternalExadataStorageConnectorsResult).value

    return AwaitableGetExternalExadataStorageConnectorsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_exadata_infrastructure_id=pulumi.get(__ret__, 'external_exadata_infrastructure_id'),
        external_exadata_storage_connector_collections=pulumi.get(__ret__, 'external_exadata_storage_connector_collections'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_external_exadata_storage_connectors)
def get_external_exadata_storage_connectors_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                                   display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                                   external_exadata_infrastructure_id: Optional[pulumi.Input[str]] = None,
                                                   filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetExternalExadataStorageConnectorsFilterArgs']]]]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalExadataStorageConnectorsResult]:
    """
    This data source provides the list of External Exadata Storage Connectors in Oracle Cloud Infrastructure Database Management service.

    Lists the Exadata storage server connectors for the specified Exadata infrastructure.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_external_exadata_storage_connectors = oci.DatabaseManagement.get_external_exadata_storage_connectors(compartment_id=compartment_id,
        external_exadata_infrastructure_id=test_external_exadata_infrastructure["id"],
        display_name=external_exadata_storage_connector_display_name)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    :param str display_name: The optional single value query filter parameter on the entity display name.
    :param str external_exadata_infrastructure_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata infrastructure.
    """
    ...
