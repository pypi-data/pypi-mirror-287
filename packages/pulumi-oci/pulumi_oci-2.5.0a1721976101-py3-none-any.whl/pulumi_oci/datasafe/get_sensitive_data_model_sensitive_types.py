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
    'GetSensitiveDataModelSensitiveTypesResult',
    'AwaitableGetSensitiveDataModelSensitiveTypesResult',
    'get_sensitive_data_model_sensitive_types',
    'get_sensitive_data_model_sensitive_types_output',
]

@pulumi.output_type
class GetSensitiveDataModelSensitiveTypesResult:
    """
    A collection of values returned by getSensitiveDataModelSensitiveTypes.
    """
    def __init__(__self__, filters=None, id=None, sensitive_data_model_id=None, sensitive_data_model_sensitive_type_collections=None, sensitive_type_id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sensitive_data_model_id and not isinstance(sensitive_data_model_id, str):
            raise TypeError("Expected argument 'sensitive_data_model_id' to be a str")
        pulumi.set(__self__, "sensitive_data_model_id", sensitive_data_model_id)
        if sensitive_data_model_sensitive_type_collections and not isinstance(sensitive_data_model_sensitive_type_collections, list):
            raise TypeError("Expected argument 'sensitive_data_model_sensitive_type_collections' to be a list")
        pulumi.set(__self__, "sensitive_data_model_sensitive_type_collections", sensitive_data_model_sensitive_type_collections)
        if sensitive_type_id and not isinstance(sensitive_type_id, str):
            raise TypeError("Expected argument 'sensitive_type_id' to be a str")
        pulumi.set(__self__, "sensitive_type_id", sensitive_type_id)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSensitiveDataModelSensitiveTypesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="sensitiveDataModelId")
    def sensitive_data_model_id(self) -> str:
        return pulumi.get(self, "sensitive_data_model_id")

    @property
    @pulumi.getter(name="sensitiveDataModelSensitiveTypeCollections")
    def sensitive_data_model_sensitive_type_collections(self) -> Sequence['outputs.GetSensitiveDataModelSensitiveTypesSensitiveDataModelSensitiveTypeCollectionResult']:
        """
        The list of sensitive_data_model_sensitive_type_collection.
        """
        return pulumi.get(self, "sensitive_data_model_sensitive_type_collections")

    @property
    @pulumi.getter(name="sensitiveTypeId")
    def sensitive_type_id(self) -> Optional[str]:
        """
        The OCID of the sensitive type.
        """
        return pulumi.get(self, "sensitive_type_id")


class AwaitableGetSensitiveDataModelSensitiveTypesResult(GetSensitiveDataModelSensitiveTypesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSensitiveDataModelSensitiveTypesResult(
            filters=self.filters,
            id=self.id,
            sensitive_data_model_id=self.sensitive_data_model_id,
            sensitive_data_model_sensitive_type_collections=self.sensitive_data_model_sensitive_type_collections,
            sensitive_type_id=self.sensitive_type_id)


def get_sensitive_data_model_sensitive_types(filters: Optional[Sequence[pulumi.InputType['GetSensitiveDataModelSensitiveTypesFilterArgs']]] = None,
                                             sensitive_data_model_id: Optional[str] = None,
                                             sensitive_type_id: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSensitiveDataModelSensitiveTypesResult:
    """
    This data source provides the list of Sensitive Data Model Sensitive Types in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of sensitive type Ids present in the specified sensitive data model.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sensitive_data_model_sensitive_types = oci.DataSafe.get_sensitive_data_model_sensitive_types(sensitive_data_model_id=test_sensitive_data_model["id"],
        sensitive_type_id=test_sensitive_type["id"])
    ```


    :param str sensitive_data_model_id: The OCID of the sensitive data model.
    :param str sensitive_type_id: A filter to return only items related to a specific sensitive type OCID.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sensitiveDataModelId'] = sensitive_data_model_id
    __args__['sensitiveTypeId'] = sensitive_type_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getSensitiveDataModelSensitiveTypes:getSensitiveDataModelSensitiveTypes', __args__, opts=opts, typ=GetSensitiveDataModelSensitiveTypesResult).value

    return AwaitableGetSensitiveDataModelSensitiveTypesResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        sensitive_data_model_id=pulumi.get(__ret__, 'sensitive_data_model_id'),
        sensitive_data_model_sensitive_type_collections=pulumi.get(__ret__, 'sensitive_data_model_sensitive_type_collections'),
        sensitive_type_id=pulumi.get(__ret__, 'sensitive_type_id'))


@_utilities.lift_output_func(get_sensitive_data_model_sensitive_types)
def get_sensitive_data_model_sensitive_types_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSensitiveDataModelSensitiveTypesFilterArgs']]]]] = None,
                                                    sensitive_data_model_id: Optional[pulumi.Input[str]] = None,
                                                    sensitive_type_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSensitiveDataModelSensitiveTypesResult]:
    """
    This data source provides the list of Sensitive Data Model Sensitive Types in Oracle Cloud Infrastructure Data Safe service.

    Gets a list of sensitive type Ids present in the specified sensitive data model.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sensitive_data_model_sensitive_types = oci.DataSafe.get_sensitive_data_model_sensitive_types(sensitive_data_model_id=test_sensitive_data_model["id"],
        sensitive_type_id=test_sensitive_type["id"])
    ```


    :param str sensitive_data_model_id: The OCID of the sensitive data model.
    :param str sensitive_type_id: A filter to return only items related to a specific sensitive type OCID.
    """
    ...
