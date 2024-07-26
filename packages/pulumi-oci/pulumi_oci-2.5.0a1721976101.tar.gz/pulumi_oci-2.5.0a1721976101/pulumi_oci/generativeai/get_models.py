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
    def __init__(__self__, capabilities=None, compartment_id=None, display_name=None, filters=None, id=None, model_collections=None, state=None, vendor=None):
        if capabilities and not isinstance(capabilities, list):
            raise TypeError("Expected argument 'capabilities' to be a list")
        pulumi.set(__self__, "capabilities", capabilities)
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
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if vendor and not isinstance(vendor, str):
            raise TypeError("Expected argument 'vendor' to be a str")
        pulumi.set(__self__, "vendor", vendor)

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The compartment OCID for fine-tuned models. For pretrained models, this value is null.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetModelsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        An ID that uniquely identifies a pretrained or fine-tuned model.
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
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The lifecycle state of the model.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def vendor(self) -> Optional[str]:
        return pulumi.get(self, "vendor")


class AwaitableGetModelsResult(GetModelsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetModelsResult(
            capabilities=self.capabilities,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            model_collections=self.model_collections,
            state=self.state,
            vendor=self.vendor)


def get_models(capabilities: Optional[Sequence[str]] = None,
               compartment_id: Optional[str] = None,
               display_name: Optional[str] = None,
               filters: Optional[Sequence[pulumi.InputType['GetModelsFilterArgs']]] = None,
               id: Optional[str] = None,
               state: Optional[str] = None,
               vendor: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetModelsResult:
    """
    This data source provides the list of Models in Oracle Cloud Infrastructure Generative AI service.

    Lists the models in a specific compartment. Includes pretrained base models and fine-tuned custom models.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_models = oci.GenerativeAi.get_models(compartment_id=compartment_id,
        capabilities=model_capability,
        display_name=model_display_name,
        id=model_id,
        state=model_state,
        vendor=model_vendor)
    ```


    :param Sequence[str] capabilities: A filter to return only resources their capability matches the given capability.
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str id: The ID of the model.
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    :param str vendor: A filter to return only resources that match the entire vendor given.
    """
    __args__ = dict()
    __args__['capabilities'] = capabilities
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['id'] = id
    __args__['state'] = state
    __args__['vendor'] = vendor
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:GenerativeAi/getModels:getModels', __args__, opts=opts, typ=GetModelsResult).value

    return AwaitableGetModelsResult(
        capabilities=pulumi.get(__ret__, 'capabilities'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        model_collections=pulumi.get(__ret__, 'model_collections'),
        state=pulumi.get(__ret__, 'state'),
        vendor=pulumi.get(__ret__, 'vendor'))


@_utilities.lift_output_func(get_models)
def get_models_output(capabilities: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      compartment_id: Optional[pulumi.Input[str]] = None,
                      display_name: Optional[pulumi.Input[Optional[str]]] = None,
                      filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetModelsFilterArgs']]]]] = None,
                      id: Optional[pulumi.Input[Optional[str]]] = None,
                      state: Optional[pulumi.Input[Optional[str]]] = None,
                      vendor: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetModelsResult]:
    """
    This data source provides the list of Models in Oracle Cloud Infrastructure Generative AI service.

    Lists the models in a specific compartment. Includes pretrained base models and fine-tuned custom models.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_models = oci.GenerativeAi.get_models(compartment_id=compartment_id,
        capabilities=model_capability,
        display_name=model_display_name,
        id=model_id,
        state=model_state,
        vendor=model_vendor)
    ```


    :param Sequence[str] capabilities: A filter to return only resources their capability matches the given capability.
    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which to list resources.
    :param str display_name: A filter to return only resources that match the given display name exactly.
    :param str id: The ID of the model.
    :param str state: A filter to return only resources their lifecycleState matches the given lifecycleState.
    :param str vendor: A filter to return only resources that match the entire vendor given.
    """
    ...
