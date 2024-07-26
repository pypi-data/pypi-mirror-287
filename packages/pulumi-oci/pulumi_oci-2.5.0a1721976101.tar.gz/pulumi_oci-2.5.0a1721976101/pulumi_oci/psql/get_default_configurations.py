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
    'GetDefaultConfigurationsResult',
    'AwaitableGetDefaultConfigurationsResult',
    'get_default_configurations',
    'get_default_configurations_output',
]

@pulumi.output_type
class GetDefaultConfigurationsResult:
    """
    A collection of values returned by getDefaultConfigurations.
    """
    def __init__(__self__, configuration_id=None, db_version=None, default_configuration_collections=None, display_name=None, filters=None, id=None, shape=None, state=None):
        if configuration_id and not isinstance(configuration_id, str):
            raise TypeError("Expected argument 'configuration_id' to be a str")
        pulumi.set(__self__, "configuration_id", configuration_id)
        if db_version and not isinstance(db_version, str):
            raise TypeError("Expected argument 'db_version' to be a str")
        pulumi.set(__self__, "db_version", db_version)
        if default_configuration_collections and not isinstance(default_configuration_collections, list):
            raise TypeError("Expected argument 'default_configuration_collections' to be a list")
        pulumi.set(__self__, "default_configuration_collections", default_configuration_collections)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if shape and not isinstance(shape, str):
            raise TypeError("Expected argument 'shape' to be a str")
        pulumi.set(__self__, "shape", shape)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> Optional[str]:
        return pulumi.get(self, "configuration_id")

    @property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> Optional[str]:
        """
        Version of the PostgreSQL database.
        """
        return pulumi.get(self, "db_version")

    @property
    @pulumi.getter(name="defaultConfigurationCollections")
    def default_configuration_collections(self) -> Sequence['outputs.GetDefaultConfigurationsDefaultConfigurationCollectionResult']:
        """
        The list of default_configuration_collection.
        """
        return pulumi.get(self, "default_configuration_collections")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        A user-friendly display name for the configuration.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDefaultConfigurationsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def shape(self) -> Optional[str]:
        """
        The name of the shape for the configuration. Example: `VM.Standard.E4.Flex`
        """
        return pulumi.get(self, "shape")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the configuration.
        """
        return pulumi.get(self, "state")


class AwaitableGetDefaultConfigurationsResult(GetDefaultConfigurationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDefaultConfigurationsResult(
            configuration_id=self.configuration_id,
            db_version=self.db_version,
            default_configuration_collections=self.default_configuration_collections,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            shape=self.shape,
            state=self.state)


def get_default_configurations(configuration_id: Optional[str] = None,
                               db_version: Optional[str] = None,
                               display_name: Optional[str] = None,
                               filters: Optional[Sequence[pulumi.InputType['GetDefaultConfigurationsFilterArgs']]] = None,
                               shape: Optional[str] = None,
                               state: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDefaultConfigurationsResult:
    """
    This data source provides the list of Default Configurations in Oracle Cloud Infrastructure Psql service.

    Returns a list of default configurations.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_default_configurations = oci.Psql.get_default_configurations(configuration_id=test_configuration["id"],
        db_version=default_configuration_db_version,
        display_name=default_configuration_display_name,
        shape=default_configuration_shape,
        state=default_configuration_state)
    ```


    :param str configuration_id: A unique identifier for the configuration.
    :param str db_version: Verison of the PostgreSQL database, such as 14.9.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str shape: The name of the shape for the configuration. Example: `VM.Standard.E4.Flex`
    :param str state: A filter to return only resources if their `lifecycleState` matches the given `lifecycleState`.
    """
    __args__ = dict()
    __args__['configurationId'] = configuration_id
    __args__['dbVersion'] = db_version
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['shape'] = shape
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Psql/getDefaultConfigurations:getDefaultConfigurations', __args__, opts=opts, typ=GetDefaultConfigurationsResult).value

    return AwaitableGetDefaultConfigurationsResult(
        configuration_id=pulumi.get(__ret__, 'configuration_id'),
        db_version=pulumi.get(__ret__, 'db_version'),
        default_configuration_collections=pulumi.get(__ret__, 'default_configuration_collections'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        shape=pulumi.get(__ret__, 'shape'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_default_configurations)
def get_default_configurations_output(configuration_id: Optional[pulumi.Input[Optional[str]]] = None,
                                      db_version: Optional[pulumi.Input[Optional[str]]] = None,
                                      display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDefaultConfigurationsFilterArgs']]]]] = None,
                                      shape: Optional[pulumi.Input[Optional[str]]] = None,
                                      state: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDefaultConfigurationsResult]:
    """
    This data source provides the list of Default Configurations in Oracle Cloud Infrastructure Psql service.

    Returns a list of default configurations.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_default_configurations = oci.Psql.get_default_configurations(configuration_id=test_configuration["id"],
        db_version=default_configuration_db_version,
        display_name=default_configuration_display_name,
        shape=default_configuration_shape,
        state=default_configuration_state)
    ```


    :param str configuration_id: A unique identifier for the configuration.
    :param str db_version: Verison of the PostgreSQL database, such as 14.9.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str shape: The name of the shape for the configuration. Example: `VM.Standard.E4.Flex`
    :param str state: A filter to return only resources if their `lifecycleState` matches the given `lifecycleState`.
    """
    ...
