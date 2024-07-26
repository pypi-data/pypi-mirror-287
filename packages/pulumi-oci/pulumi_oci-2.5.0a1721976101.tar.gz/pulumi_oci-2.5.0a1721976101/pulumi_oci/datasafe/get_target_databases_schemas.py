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
    'GetTargetDatabasesSchemasResult',
    'AwaitableGetTargetDatabasesSchemasResult',
    'get_target_databases_schemas',
    'get_target_databases_schemas_output',
]

@pulumi.output_type
class GetTargetDatabasesSchemasResult:
    """
    A collection of values returned by getTargetDatabasesSchemas.
    """
    def __init__(__self__, filters=None, id=None, is_oracle_maintained=None, schema_name_contains=None, schema_names=None, schemas=None, target_database_id=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_oracle_maintained and not isinstance(is_oracle_maintained, bool):
            raise TypeError("Expected argument 'is_oracle_maintained' to be a bool")
        pulumi.set(__self__, "is_oracle_maintained", is_oracle_maintained)
        if schema_name_contains and not isinstance(schema_name_contains, str):
            raise TypeError("Expected argument 'schema_name_contains' to be a str")
        pulumi.set(__self__, "schema_name_contains", schema_name_contains)
        if schema_names and not isinstance(schema_names, list):
            raise TypeError("Expected argument 'schema_names' to be a list")
        pulumi.set(__self__, "schema_names", schema_names)
        if schemas and not isinstance(schemas, list):
            raise TypeError("Expected argument 'schemas' to be a list")
        pulumi.set(__self__, "schemas", schemas)
        if target_database_id and not isinstance(target_database_id, str):
            raise TypeError("Expected argument 'target_database_id' to be a str")
        pulumi.set(__self__, "target_database_id", target_database_id)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetTargetDatabasesSchemasFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isOracleMaintained")
    def is_oracle_maintained(self) -> Optional[bool]:
        """
        Indicates if the schema is oracle supplied.
        """
        return pulumi.get(self, "is_oracle_maintained")

    @property
    @pulumi.getter(name="schemaNameContains")
    def schema_name_contains(self) -> Optional[str]:
        return pulumi.get(self, "schema_name_contains")

    @property
    @pulumi.getter(name="schemaNames")
    def schema_names(self) -> Optional[Sequence[str]]:
        """
        Name of the schema.
        """
        return pulumi.get(self, "schema_names")

    @property
    @pulumi.getter
    def schemas(self) -> Sequence['outputs.GetTargetDatabasesSchemasSchemaResult']:
        """
        The list of schemas.
        """
        return pulumi.get(self, "schemas")

    @property
    @pulumi.getter(name="targetDatabaseId")
    def target_database_id(self) -> str:
        return pulumi.get(self, "target_database_id")


class AwaitableGetTargetDatabasesSchemasResult(GetTargetDatabasesSchemasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTargetDatabasesSchemasResult(
            filters=self.filters,
            id=self.id,
            is_oracle_maintained=self.is_oracle_maintained,
            schema_name_contains=self.schema_name_contains,
            schema_names=self.schema_names,
            schemas=self.schemas,
            target_database_id=self.target_database_id)


def get_target_databases_schemas(filters: Optional[Sequence[pulumi.InputType['GetTargetDatabasesSchemasFilterArgs']]] = None,
                                 is_oracle_maintained: Optional[bool] = None,
                                 schema_name_contains: Optional[str] = None,
                                 schema_names: Optional[Sequence[str]] = None,
                                 target_database_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTargetDatabasesSchemasResult:
    """
    This data source provides the list of Target Databases Schemas in Oracle Cloud Infrastructure Data Safe service.

    Returns list of schema.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_target_databases_schemas = oci.DataSafe.get_target_databases_schemas(target_database_id=test_target_database["id"],
        is_oracle_maintained=target_databases_schema_is_oracle_maintained,
        schema_names=target_databases_schema_schema_name,
        schema_name_contains=target_databases_schema_schema_name_contains)
    ```


    :param bool is_oracle_maintained: A filter to return only items related to specific type of schema.
    :param str schema_name_contains: A filter to return only items if schema name contains a specific string.
    :param Sequence[str] schema_names: A filter to return only items related to specific schema name.
    :param str target_database_id: The OCID of the Data Safe target database.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['isOracleMaintained'] = is_oracle_maintained
    __args__['schemaNameContains'] = schema_name_contains
    __args__['schemaNames'] = schema_names
    __args__['targetDatabaseId'] = target_database_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getTargetDatabasesSchemas:getTargetDatabasesSchemas', __args__, opts=opts, typ=GetTargetDatabasesSchemasResult).value

    return AwaitableGetTargetDatabasesSchemasResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        is_oracle_maintained=pulumi.get(__ret__, 'is_oracle_maintained'),
        schema_name_contains=pulumi.get(__ret__, 'schema_name_contains'),
        schema_names=pulumi.get(__ret__, 'schema_names'),
        schemas=pulumi.get(__ret__, 'schemas'),
        target_database_id=pulumi.get(__ret__, 'target_database_id'))


@_utilities.lift_output_func(get_target_databases_schemas)
def get_target_databases_schemas_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTargetDatabasesSchemasFilterArgs']]]]] = None,
                                        is_oracle_maintained: Optional[pulumi.Input[Optional[bool]]] = None,
                                        schema_name_contains: Optional[pulumi.Input[Optional[str]]] = None,
                                        schema_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                        target_database_id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTargetDatabasesSchemasResult]:
    """
    This data source provides the list of Target Databases Schemas in Oracle Cloud Infrastructure Data Safe service.

    Returns list of schema.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_target_databases_schemas = oci.DataSafe.get_target_databases_schemas(target_database_id=test_target_database["id"],
        is_oracle_maintained=target_databases_schema_is_oracle_maintained,
        schema_names=target_databases_schema_schema_name,
        schema_name_contains=target_databases_schema_schema_name_contains)
    ```


    :param bool is_oracle_maintained: A filter to return only items related to specific type of schema.
    :param str schema_name_contains: A filter to return only items if schema name contains a specific string.
    :param Sequence[str] schema_names: A filter to return only items related to specific schema name.
    :param str target_database_id: The OCID of the Data Safe target database.
    """
    ...
