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
    'GetDbSystemPrimaryDbInstanceResult',
    'AwaitableGetDbSystemPrimaryDbInstanceResult',
    'get_db_system_primary_db_instance',
    'get_db_system_primary_db_instance_output',
]

@pulumi.output_type
class GetDbSystemPrimaryDbInstanceResult:
    """
    A collection of values returned by getDbSystemPrimaryDbInstance.
    """
    def __init__(__self__, db_instance_id=None, db_system_id=None, id=None):
        if db_instance_id and not isinstance(db_instance_id, str):
            raise TypeError("Expected argument 'db_instance_id' to be a str")
        pulumi.set(__self__, "db_instance_id", db_instance_id)
        if db_system_id and not isinstance(db_system_id, str):
            raise TypeError("Expected argument 'db_system_id' to be a str")
        pulumi.set(__self__, "db_system_id", db_system_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="dbInstanceId")
    def db_instance_id(self) -> str:
        """
        A unique identifier for the primary database instance node.
        """
        return pulumi.get(self, "db_instance_id")

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> str:
        return pulumi.get(self, "db_system_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetDbSystemPrimaryDbInstanceResult(GetDbSystemPrimaryDbInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbSystemPrimaryDbInstanceResult(
            db_instance_id=self.db_instance_id,
            db_system_id=self.db_system_id,
            id=self.id)


def get_db_system_primary_db_instance(db_system_id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbSystemPrimaryDbInstanceResult:
    """
    This data source provides details about a specific Db System Primary Db Instance resource in Oracle Cloud Infrastructure Psql service.

    Gets the primary database instance node details.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_system_primary_db_instance = oci.Psql.get_db_system_primary_db_instance(db_system_id=test_db_system["id"])
    ```


    :param str db_system_id: A unique identifier for the database system.
    """
    __args__ = dict()
    __args__['dbSystemId'] = db_system_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Psql/getDbSystemPrimaryDbInstance:getDbSystemPrimaryDbInstance', __args__, opts=opts, typ=GetDbSystemPrimaryDbInstanceResult).value

    return AwaitableGetDbSystemPrimaryDbInstanceResult(
        db_instance_id=pulumi.get(__ret__, 'db_instance_id'),
        db_system_id=pulumi.get(__ret__, 'db_system_id'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_db_system_primary_db_instance)
def get_db_system_primary_db_instance_output(db_system_id: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbSystemPrimaryDbInstanceResult]:
    """
    This data source provides details about a specific Db System Primary Db Instance resource in Oracle Cloud Infrastructure Psql service.

    Gets the primary database instance node details.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_db_system_primary_db_instance = oci.Psql.get_db_system_primary_db_instance(db_system_id=test_db_system["id"])
    ```


    :param str db_system_id: A unique identifier for the database system.
    """
    ...
