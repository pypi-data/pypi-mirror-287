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
    'GetModelsResult',
    'AwaitableGetModelsResult',
    'get_models',
    'get_models_output',
]

@pulumi.output_type
class GetModelsResult:
    """
    A collection of values returned by getModels.
    """
    def __init__(__self__, compartment_id=None, display_name=None, filters=None, id=None, model_collections=None, project_id=None, state=None):
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
        if model_collections and not isinstance(model_collections, list):
            raise TypeError("Expected argument 'model_collections' to be a list")
        pulumi.set(__self__, "model_collections", model_collections)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Model Identifier, can be renamed
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetModelsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Unique identifier that is immutable on creation
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modelCollections")
    def model_collections(self) -> Sequence['outputs.GetModelsModelCollectionResult']:
        """
        The list of model_collection.
        """
        return pulumi.get(self, "model_collections")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate with the model.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the Model.
        """
        return pulumi.get(self, "state")


class AwaitableGetModelsResult(GetModelsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetModelsResult(
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            model_collections=self.model_collections,
            project_id=self.project_id,
            state=self.state)


def get_models(compartment_id: Optional[str] = None,
               display_name: Optional[str] = None,
               filters: Optional[Sequence[pulumi.InputType['GetModelsFilterArgs']]] = None,
               id: Optional[str] = None,
               project_id: Optional[str] = None,
               state: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetModelsResult:
    """
    This data source provides the list of Models in Oracle Cloud Infrastructure Ai Vision service.

    Returns a list of Models.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_models = oci.AiVision.get_models(compartment_id=compartment_id,
        display_name=model_display_name,
        id=model_id,
        project_id=test_project["id"],
        state=model_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str id: unique Model identifier
    :param str project_id: The ID of the project for which to list the objects.
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['projectId'] = project_id
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:AiVision/getModels:getModels', __args__, opts=opts, typ=GetModelsResult).value

    return AwaitableGetModelsResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        model_collections=pulumi.get(__ret__, 'model_collections'),
        project_id=pulumi.get(__ret__, 'project_id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_models)
def get_models_output(compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                      display_name: Optional[pulumi.Input[Optional[str]]] = None,
                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetModelsFilterArgs']]]]] = None,
                      id: Optional[pulumi.Input[Optional[str]]] = None,
                      project_id: Optional[pulumi.Input[Optional[str]]] = None,
                      state: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetModelsResult]:
    """
    This data source provides the list of Models in Oracle Cloud Infrastructure Ai Vision service.

    Returns a list of Models.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_models = oci.AiVision.get_models(compartment_id=compartment_id,
        display_name=model_display_name,
        id=model_id,
        project_id=test_project["id"],
        state=model_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the entire display name given.
    :param str id: unique Model identifier
    :param str project_id: The ID of the project for which to list the objects.
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    """
    ...
