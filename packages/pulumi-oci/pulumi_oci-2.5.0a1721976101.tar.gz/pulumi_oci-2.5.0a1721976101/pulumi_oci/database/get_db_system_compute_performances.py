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
    'GetDbSystemComputePerformancesResult',
    'AwaitableGetDbSystemComputePerformancesResult',
    'get_db_system_compute_performances',
    'get_db_system_compute_performances_output',
]

@pulumi.output_type
class GetDbSystemComputePerformancesResult:
    """
    A collection of values returned by getDbSystemComputePerformances.
    """
    def __init__(__self__, db_system_compute_performances=None, db_system_shape=None, filters=None, id=None):
        if db_system_compute_performances and not isinstance(db_system_compute_performances, list):
            raise TypeError("Expected argument 'db_system_compute_performances' to be a list")
        pulumi.set(__self__, "db_system_compute_performances", db_system_compute_performances)
        if db_system_shape and not isinstance(db_system_shape, str):
            raise TypeError("Expected argument 'db_system_shape' to be a str")
        pulumi.set(__self__, "db_system_shape", db_system_shape)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="dbSystemComputePerformances")
    def db_system_compute_performances(self) -> Sequence['outputs.GetDbSystemComputePerformancesDbSystemComputePerformanceResult']:
        """
        The list of db_system_compute_performances.
        """
        return pulumi.get(self, "db_system_compute_performances")

    @property
    @pulumi.getter(name="dbSystemShape")
    def db_system_shape(self) -> Optional[str]:
        return pulumi.get(self, "db_system_shape")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetDbSystemComputePerformancesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetDbSystemComputePerformancesResult(GetDbSystemComputePerformancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbSystemComputePerformancesResult(
            db_system_compute_performances=self.db_system_compute_performances,
            db_system_shape=self.db_system_shape,
            filters=self.filters,
            id=self.id)


def get_db_system_compute_performances(db_system_shape: Optional[str] = None,
                                       filters: Optional[Sequence[pulumi.InputType['GetDbSystemComputePerformancesFilterArgs']]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbSystemComputePerformancesResult:
    """
    This data source provides the list of Db System Compute Performances in Oracle Cloud Infrastructure Database service.

    Gets a list of expected compute performance parameters for a virtual machine DB system based on system configuration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_system_compute_performances = oci.Database.get_db_system_compute_performances(db_system_shape=db_system_compute_performance_db_system_shape)
    ```


    :param str db_system_shape: If provided, filters the results to the set of database versions which are supported for the given shape.
    """
    __args__ = dict()
    __args__['dbSystemShape'] = db_system_shape
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getDbSystemComputePerformances:getDbSystemComputePerformances', __args__, opts=opts, typ=GetDbSystemComputePerformancesResult).value

    return AwaitableGetDbSystemComputePerformancesResult(
        db_system_compute_performances=pulumi.get(__ret__, 'db_system_compute_performances'),
        db_system_shape=pulumi.get(__ret__, 'db_system_shape'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_db_system_compute_performances)
def get_db_system_compute_performances_output(db_system_shape: Optional[pulumi.Input[Optional[str]]] = None,
                                              filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetDbSystemComputePerformancesFilterArgs']]]]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbSystemComputePerformancesResult]:
    """
    This data source provides the list of Db System Compute Performances in Oracle Cloud Infrastructure Database service.

    Gets a list of expected compute performance parameters for a virtual machine DB system based on system configuration.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_system_compute_performances = oci.Database.get_db_system_compute_performances(db_system_shape=db_system_compute_performance_db_system_shape)
    ```


    :param str db_system_shape: If provided, filters the results to the set of database versions which are supported for the given shape.
    """
    ...
