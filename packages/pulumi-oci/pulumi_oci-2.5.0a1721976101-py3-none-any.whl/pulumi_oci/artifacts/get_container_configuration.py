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
    'GetContainerConfigurationResult',
    'AwaitableGetContainerConfigurationResult',
    'get_container_configuration',
    'get_container_configuration_output',
]

@pulumi.output_type
class GetContainerConfigurationResult:
    """
    A collection of values returned by getContainerConfiguration.
    """
    def __init__(__self__, compartment_id=None, id=None, is_repository_created_on_first_push=None, namespace=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_repository_created_on_first_push and not isinstance(is_repository_created_on_first_push, bool):
            raise TypeError("Expected argument 'is_repository_created_on_first_push' to be a bool")
        pulumi.set(__self__, "is_repository_created_on_first_push", is_repository_created_on_first_push)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isRepositoryCreatedOnFirstPush")
    def is_repository_created_on_first_push(self) -> bool:
        """
        Whether to create a new container repository when a container is pushed to a new repository path. Repositories created in this way belong to the root compartment.
        """
        return pulumi.get(self, "is_repository_created_on_first_push")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        The tenancy namespace used in the container repository path.
        """
        return pulumi.get(self, "namespace")


class AwaitableGetContainerConfigurationResult(GetContainerConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerConfigurationResult(
            compartment_id=self.compartment_id,
            id=self.id,
            is_repository_created_on_first_push=self.is_repository_created_on_first_push,
            namespace=self.namespace)


def get_container_configuration(compartment_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerConfigurationResult:
    """
    This data source provides details about a specific Container Configuration resource in Oracle Cloud Infrastructure Artifacts service.

    Get container configuration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_container_configuration = oci.Artifacts.get_container_configuration(compartment_id=compartment_id)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Artifacts/getContainerConfiguration:getContainerConfiguration', __args__, opts=opts, typ=GetContainerConfigurationResult).value

    return AwaitableGetContainerConfigurationResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        is_repository_created_on_first_push=pulumi.get(__ret__, 'is_repository_created_on_first_push'),
        namespace=pulumi.get(__ret__, 'namespace'))


@_utilities.lift_output_func(get_container_configuration)
def get_container_configuration_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerConfigurationResult]:
    """
    This data source provides details about a specific Container Configuration resource in Oracle Cloud Infrastructure Artifacts service.

    Get container configuration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_container_configuration = oci.Artifacts.get_container_configuration(compartment_id=compartment_id)
    ```


    :param str compartment_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
    """
    ...
