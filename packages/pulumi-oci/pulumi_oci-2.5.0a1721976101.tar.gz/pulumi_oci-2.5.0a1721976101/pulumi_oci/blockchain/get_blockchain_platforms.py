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
    'GetBlockchainPlatformsResult',
    'AwaitableGetBlockchainPlatformsResult',
    'get_blockchain_platforms',
    'get_blockchain_platforms_output',
]

@pulumi.output_type
class GetBlockchainPlatformsResult:
    """
    A collection of values returned by getBlockchainPlatforms.
    """
    def __init__(__self__, blockchain_platform_collections=None, compartment_id=None, display_name=None, filters=None, id=None, state=None):
        if blockchain_platform_collections and not isinstance(blockchain_platform_collections, list):
            raise TypeError("Expected argument 'blockchain_platform_collections' to be a list")
        pulumi.set(__self__, "blockchain_platform_collections", blockchain_platform_collections)
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
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="blockchainPlatformCollections")
    def blockchain_platform_collections(self) -> Sequence['outputs.GetBlockchainPlatformsBlockchainPlatformCollectionResult']:
        """
        The list of blockchain_platform_collection.
        """
        return pulumi.get(self, "blockchain_platform_collections")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Platform Instance Display name, can be renamed
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetBlockchainPlatformsFilterResult']]:
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
    def state(self) -> Optional[str]:
        """
        The current state of the Platform Instance.
        """
        return pulumi.get(self, "state")


class AwaitableGetBlockchainPlatformsResult(GetBlockchainPlatformsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBlockchainPlatformsResult(
            blockchain_platform_collections=self.blockchain_platform_collections,
            compartment_id=self.compartment_id,
            display_name=self.display_name,
            filters=self.filters,
            id=self.id,
            state=self.state)


def get_blockchain_platforms(compartment_id: Optional[str] = None,
                             display_name: Optional[str] = None,
                             filters: Optional[Sequence[pulumi.InputType['GetBlockchainPlatformsFilterArgs']]] = None,
                             state: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBlockchainPlatformsResult:
    """
    This data source provides the list of Blockchain Platforms in Oracle Cloud Infrastructure Blockchain service.

    Returns a list Blockchain Platform Instances in a compartment

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_blockchain_platforms = oci.Blockchain.get_blockchain_platforms(compartment_id=compartment_id,
        display_name=blockchain_platform_display_name,
        state=blockchain_platform_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`
    :param str state: A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['displayName'] = display_name
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Blockchain/getBlockchainPlatforms:getBlockchainPlatforms', __args__, opts=opts, typ=GetBlockchainPlatformsResult).value

    return AwaitableGetBlockchainPlatformsResult(
        blockchain_platform_collections=pulumi.get(__ret__, 'blockchain_platform_collections'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        display_name=pulumi.get(__ret__, 'display_name'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_blockchain_platforms)
def get_blockchain_platforms_output(compartment_id: Optional[pulumi.Input[str]] = None,
                                    display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                    filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetBlockchainPlatformsFilterArgs']]]]] = None,
                                    state: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBlockchainPlatformsResult]:
    """
    This data source provides the list of Blockchain Platforms in Oracle Cloud Infrastructure Blockchain service.

    Returns a list Blockchain Platform Instances in a compartment

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_blockchain_platforms = oci.Blockchain.get_blockchain_platforms(compartment_id=compartment_id,
        display_name=blockchain_platform_display_name,
        state=blockchain_platform_state)
    ```


    :param str compartment_id: The ID of the compartment in which to list resources.
    :param str display_name: A user-friendly name. Does not have to be unique, and it's changeable. Example: `My new resource`
    :param str state: A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
    """
    ...
