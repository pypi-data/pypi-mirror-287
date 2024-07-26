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
    'GetShardedDatabasesResult',
    'AwaitableGetShardedDatabasesResult',
    'get_sharded_databases',
    'get_sharded_databases_output',
]

@pulumi.output_type
class GetShardedDatabasesResult:
    """
    A collection of values returned by getShardedDatabases.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, sharded_database_collections=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sharded_database_collections and not isinstance(sharded_database_collections, list):
            raise TypeError("Expected argument 'sharded_database_collections' to be a list")
        pulumi.set(__self__, "sharded_database_collections", sharded_database_collections)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Identifier of the compartment in which sharded database exists.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Oracle sharded database display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetShardedDatabasesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="shardedDatabaseCollections")
    def sharded_database_collections(self) -> Sequence['outputs.GetShardedDatabasesShardedDatabaseCollectionResult']:
        """
        The list of sharded_database_collection.
        """
        return pulumi.get(self, "sharded_database_collections")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Lifecycle states for sharded databases.
        """
        return pulumi.get(self, "state")


class AwaitableGetShardedDatabasesResult(GetShardedDatabasesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetShardedDatabasesResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            sharded_database_collections=self.sharded_database_collections,
            state=self.state)


def get_sharded_databases(compartment_id: Optional[str] = None,
                          display_name: Optional[str] = None,
                          filters: Optional[Sequence[pulumi.InputType['GetShardedDatabasesFilterArgs']]] = None,
                          state: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetShardedDatabasesResult:
    """
    This data source provides the list of Sharded Databases in Oracle Cloud Infrastructure Globally Distributed Database service.

    List of Sharded databases.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sharded_databases = oci.GloballyDistributedDatabase.get_sharded_databases(compartment_id=compartment_id,
        display_name=sharded_database_display_name,
        state=sharded_database_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only sharded databases that match the entire name given. The match is not case sensitive.
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:GloballyDistributedDatabase/getShardedDatabases:getShardedDatabases', __args__, opts=opts, typ=GetShardedDatabasesResult).value

    return AwaitableGetShardedDatabasesResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        sharded_database_collections=pulumi.get(__ret__, 'sharded_database_collections'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_sharded_databases)
def get_sharded_databases_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                 display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                 filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetShardedDatabasesFilterArgs']]]]] = None,
                                 state: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetShardedDatabasesResult]:
    """
    This data source provides the list of Sharded Databases in Oracle Cloud Infrastructure Globally Distributed Database service.

    List of Sharded databases.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_sharded_databases = oci.GloballyDistributedDatabase.get_sharded_databases(compartment_id=compartment_id,
        display_name=sharded_database_display_name,
        state=sharded_database_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only sharded databases that match the entire name given. The match is not case sensitive.
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    """
    ...
