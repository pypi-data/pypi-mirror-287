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
    'GetBdsInstancePatchHistoriesResult',
    'AwaitableGetBdsInstancePatchHistoriesResult',
    'get_bds_instance_patch_histories',
    'get_bds_instance_patch_histories_output',
]

@pulumi.output_type
class GetBdsInstancePatchHistoriesResult:
    """
    A collection of values returned by getBdsInstancePatchHistories.
    """
    def __init__(__self__, bds_instance_id=None, filters=None, id=None, patch_histories=None, patch_type=None, patch_version=None, state=None):
        if bds_instance_id and not isinstance(bds_instance_id, str):
            raise TypeError("Expected argument 'bds_instance_id' to be a str")
        pulumi.set(__self__, "bds_instance_id", bds_instance_id)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if patch_histories and not isinstance(patch_histories, list):
            raise TypeError("Expected argument 'patch_histories' to be a list")
        pulumi.set(__self__, "patch_histories", patch_histories)
        if patch_type and not isinstance(patch_type, str):
            raise TypeError("Expected argument 'patch_type' to be a str")
        pulumi.set(__self__, "patch_type", patch_type)
        if patch_version and not isinstance(patch_version, str):
            raise TypeError("Expected argument 'patch_version' to be a str")
        pulumi.set(__self__, "patch_version", patch_version)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="bdsInstanceId")
    def bds_instance_id(self) -> str:
        return pulumi.get(self, "bds_instance_id")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetBdsInstancePatchHistoriesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="patchHistories")
    def patch_histories(self) -> Sequence['outputs.GetBdsInstancePatchHistoriesPatchHistoryResult']:
        """
        The list of patch_histories.
        """
        return pulumi.get(self, "patch_histories")

    @property
    @pulumi.getter(name="patchType")
    def patch_type(self) -> Optional[str]:
        """
        The type of current patch history. DP - Data Plane patch(This history type is internal available only) ODH - Oracle Distribution of Hadoop patch OS - Operating System patch
        """
        return pulumi.get(self, "patch_type")

    @property
    @pulumi.getter(name="patchVersion")
    def patch_version(self) -> Optional[str]:
        return pulumi.get(self, "patch_version")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The status of this patch.
        """
        return pulumi.get(self, "state")


class AwaitableGetBdsInstancePatchHistoriesResult(GetBdsInstancePatchHistoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBdsInstancePatchHistoriesResult(
            bds_instance_id=self.bds_instance_id,
            filters=self.filters,
            id=self.id,
            patch_histories=self.patch_histories,
            patch_type=self.patch_type,
            patch_version=self.patch_version,
            state=self.state)


def get_bds_instance_patch_histories(bds_instance_id: Optional[str] = None,
                                     filters: Optional[Sequence[pulumi.InputType['GetBdsInstancePatchHistoriesFilterArgs']]] = None,
                                     patch_type: Optional[str] = None,
                                     patch_version: Optional[str] = None,
                                     state: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBdsInstancePatchHistoriesResult:
    """
    This data source provides the list of Bds Instance Patch Histories in Oracle Cloud Infrastructure Big Data Service service.

    List the patch history of this cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_bds_instance_patch_histories = oci.BigDataService.get_bds_instance_patch_histories(bds_instance_id=test_bds_instance["id"],
        patch_type=bds_instance_patch_history_patch_type,
        patch_version=bds_instance_patch_history_patch_version,
        state=bds_instance_patch_history_state)
    ```


    :param str bds_instance_id: The OCID of the cluster.
    :param str patch_type: The type of a BDS patch history entity.
    :param str patch_version: The version of the patch
    :param str state: The status of the patch.
    """
    __args__ = dict()
    __args__['bdsInstanceId'] = bds_instance_id
    __args__['filters'] = filters
    __args__['patchType'] = patch_type
    __args__['patchVersion'] = patch_version
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:BigDataService/getBdsInstancePatchHistories:getBdsInstancePatchHistories', __args__, opts=opts, typ=GetBdsInstancePatchHistoriesResult).value

    return AwaitableGetBdsInstancePatchHistoriesResult(
        bds_instance_id=pulumi.get(__ret__, 'bds_instance_id'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        patch_histories=pulumi.get(__ret__, 'patch_histories'),
        patch_type=pulumi.get(__ret__, 'patch_type'),
        patch_version=pulumi.get(__ret__, 'patch_version'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_bds_instance_patch_histories)
def get_bds_instance_patch_histories_output(bds_instance_id: Optional[pulumi.Input[str]] = None,
                                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetBdsInstancePatchHistoriesFilterArgs']]]]] = None,
                                            patch_type: Optional[pulumi.Input[Optional[str]]] = None,
                                            patch_version: Optional[pulumi.Input[Optional[str]]] = None,
                                            state: Optional[pulumi.Input[Optional[str]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBdsInstancePatchHistoriesResult]:
    """
    This data source provides the list of Bds Instance Patch Histories in Oracle Cloud Infrastructure Big Data Service service.

    List the patch history of this cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_bds_instance_patch_histories = oci.BigDataService.get_bds_instance_patch_histories(bds_instance_id=test_bds_instance["id"],
        patch_type=bds_instance_patch_history_patch_type,
        patch_version=bds_instance_patch_history_patch_version,
        state=bds_instance_patch_history_state)
    ```


    :param str bds_instance_id: The OCID of the cluster.
    :param str patch_type: The type of a BDS patch history entity.
    :param str patch_version: The version of the patch
    :param str state: The status of the patch.
    """
    ...
