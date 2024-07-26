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
    'GetAutonomousDatabaseRegionalWalletManagementResult',
    'AwaitableGetAutonomousDatabaseRegionalWalletManagementResult',
    'get_autonomous_database_regional_wallet_management',
    'get_autonomous_database_regional_wallet_management_output',
]

@pulumi.output_type
class GetAutonomousDatabaseRegionalWalletManagementResult:
    """
    A collection of values returned by getAutonomousDatabaseRegionalWalletManagement.
    """
    def __init__(__self__, grace_period=None, id=None, should_rotate=None, state=None, time_rotated=None):
        if grace_period and not isinstance(grace_period, int):
            raise TypeError("Expected argument 'grace_period' to be a int")
        pulumi.set(__self__, "grace_period", grace_period)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if should_rotate and not isinstance(should_rotate, bool):
            raise TypeError("Expected argument 'should_rotate' to be a bool")
        pulumi.set(__self__, "should_rotate", should_rotate)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_rotated and not isinstance(time_rotated, str):
            raise TypeError("Expected argument 'time_rotated' to be a str")
        pulumi.set(__self__, "time_rotated", time_rotated)

    @property
    @pulumi.getter(name="gracePeriod")
    def grace_period(self) -> int:
        return pulumi.get(self, "grace_period")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="shouldRotate")
    def should_rotate(self) -> bool:
        return pulumi.get(self, "should_rotate")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current lifecycle state of the Autonomous Database wallet.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeRotated")
    def time_rotated(self) -> str:
        """
        The date and time the wallet was last rotated.
        """
        return pulumi.get(self, "time_rotated")


class AwaitableGetAutonomousDatabaseRegionalWalletManagementResult(GetAutonomousDatabaseRegionalWalletManagementResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutonomousDatabaseRegionalWalletManagementResult(
            grace_period=self.grace_period,
            id=self.id,
            should_rotate=self.should_rotate,
            state=self.state,
            time_rotated=self.time_rotated)


def get_autonomous_database_regional_wallet_management(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutonomousDatabaseRegionalWalletManagementResult:
    """
    This data source provides details about a specific Autonomous Database Regional Wallet Management resource in Oracle Cloud Infrastructure Database service.

    Gets the Autonomous Database regional wallet details.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_autonomous_database_regional_wallet_management = oci.Database.get_autonomous_database_regional_wallet_management()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Database/getAutonomousDatabaseRegionalWalletManagement:getAutonomousDatabaseRegionalWalletManagement', __args__, opts=opts, typ=GetAutonomousDatabaseRegionalWalletManagementResult).value

    return AwaitableGetAutonomousDatabaseRegionalWalletManagementResult(
        grace_period=pulumi.get(__ret__, 'grace_period'),
        id=pulumi.get(__ret__, 'id'),
        should_rotate=pulumi.get(__ret__, 'should_rotate'),
        state=pulumi.get(__ret__, 'state'),
        time_rotated=pulumi.get(__ret__, 'time_rotated'))


@_utilities.lift_output_func(get_autonomous_database_regional_wallet_management)
def get_autonomous_database_regional_wallet_management_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutonomousDatabaseRegionalWalletManagementResult]:
    """
    This data source provides details about a specific Autonomous Database Regional Wallet Management resource in Oracle Cloud Infrastructure Database service.

    Gets the Autonomous Database regional wallet details.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_autonomous_database_regional_wallet_management = oci.Database.get_autonomous_database_regional_wallet_management()
    ```
    """
    ...
