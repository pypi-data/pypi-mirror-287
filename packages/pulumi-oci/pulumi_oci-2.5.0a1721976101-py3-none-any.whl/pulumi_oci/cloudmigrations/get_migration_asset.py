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
    'GetMigrationAssetResult',
    'AwaitableGetMigrationAssetResult',
    'get_migration_asset',
    'get_migration_asset_output',
]

@pulumi.output_type
class GetMigrationAssetResult:
    """
    A collection of values returned by getMigrationAsset.
    """
    def __init__(__self__, availability_domain=None, compartment_id=None, depended_on_bies=None, display_name=None, id=None, inventory_asset_id=None, lifecycle_details=None, migration_asset_depends_ons=None, migration_asset_id=None, migration_id=None, notifications=None, parent_snapshot=None, replication_compartment_id=None, replication_schedule_id=None, snap_shot_bucket_name=None, snapshots=None, source_asset_id=None, state=None, tenancy_id=None, time_created=None, time_updated=None, type=None):
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if depended_on_bies and not isinstance(depended_on_bies, list):
            raise TypeError("Expected argument 'depended_on_bies' to be a list")
        pulumi.set(__self__, "depended_on_bies", depended_on_bies)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inventory_asset_id and not isinstance(inventory_asset_id, str):
            raise TypeError("Expected argument 'inventory_asset_id' to be a str")
        pulumi.set(__self__, "inventory_asset_id", inventory_asset_id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if migration_asset_depends_ons and not isinstance(migration_asset_depends_ons, list):
            raise TypeError("Expected argument 'migration_asset_depends_ons' to be a list")
        pulumi.set(__self__, "migration_asset_depends_ons", migration_asset_depends_ons)
        if migration_asset_id and not isinstance(migration_asset_id, str):
            raise TypeError("Expected argument 'migration_asset_id' to be a str")
        pulumi.set(__self__, "migration_asset_id", migration_asset_id)
        if migration_id and not isinstance(migration_id, str):
            raise TypeError("Expected argument 'migration_id' to be a str")
        pulumi.set(__self__, "migration_id", migration_id)
        if notifications and not isinstance(notifications, list):
            raise TypeError("Expected argument 'notifications' to be a list")
        pulumi.set(__self__, "notifications", notifications)
        if parent_snapshot and not isinstance(parent_snapshot, str):
            raise TypeError("Expected argument 'parent_snapshot' to be a str")
        pulumi.set(__self__, "parent_snapshot", parent_snapshot)
        if replication_compartment_id and not isinstance(replication_compartment_id, str):
            raise TypeError("Expected argument 'replication_compartment_id' to be a str")
        pulumi.set(__self__, "replication_compartment_id", replication_compartment_id)
        if replication_schedule_id and not isinstance(replication_schedule_id, str):
            raise TypeError("Expected argument 'replication_schedule_id' to be a str")
        pulumi.set(__self__, "replication_schedule_id", replication_schedule_id)
        if snap_shot_bucket_name and not isinstance(snap_shot_bucket_name, str):
            raise TypeError("Expected argument 'snap_shot_bucket_name' to be a str")
        pulumi.set(__self__, "snap_shot_bucket_name", snap_shot_bucket_name)
        if snapshots and not isinstance(snapshots, dict):
            raise TypeError("Expected argument 'snapshots' to be a dict")
        pulumi.set(__self__, "snapshots", snapshots)
        if source_asset_id and not isinstance(source_asset_id, str):
            raise TypeError("Expected argument 'source_asset_id' to be a str")
        pulumi.set(__self__, "source_asset_id", source_asset_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tenancy_id and not isinstance(tenancy_id, str):
            raise TypeError("Expected argument 'tenancy_id' to be a str")
        pulumi.set(__self__, "tenancy_id", tenancy_id)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        Availability domain
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        Compartment Identifier
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="dependedOnBies")
    def depended_on_bies(self) -> Sequence[str]:
        """
        List of migration assets that depend on the asset.
        """
        return pulumi.get(self, "depended_on_bies")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Asset ID generated by mirgration service. It is used in the mirgration service pipeline.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inventoryAssetId")
    def inventory_asset_id(self) -> str:
        return pulumi.get(self, "inventory_asset_id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="migrationAssetDependsOns")
    def migration_asset_depends_ons(self) -> Sequence[str]:
        return pulumi.get(self, "migration_asset_depends_ons")

    @property
    @pulumi.getter(name="migrationAssetId")
    def migration_asset_id(self) -> str:
        return pulumi.get(self, "migration_asset_id")

    @property
    @pulumi.getter(name="migrationId")
    def migration_id(self) -> str:
        """
        OCID of the associated migration.
        """
        return pulumi.get(self, "migration_id")

    @property
    @pulumi.getter
    def notifications(self) -> Sequence[str]:
        """
        List of notifications
        """
        return pulumi.get(self, "notifications")

    @property
    @pulumi.getter(name="parentSnapshot")
    def parent_snapshot(self) -> str:
        """
        The parent snapshot of the migration asset to be used by the replication task.
        """
        return pulumi.get(self, "parent_snapshot")

    @property
    @pulumi.getter(name="replicationCompartmentId")
    def replication_compartment_id(self) -> str:
        """
        Replication compartment identifier
        """
        return pulumi.get(self, "replication_compartment_id")

    @property
    @pulumi.getter(name="replicationScheduleId")
    def replication_schedule_id(self) -> str:
        """
        Replication schedule identifier
        """
        return pulumi.get(self, "replication_schedule_id")

    @property
    @pulumi.getter(name="snapShotBucketName")
    def snap_shot_bucket_name(self) -> str:
        """
        Name of snapshot bucket
        """
        return pulumi.get(self, "snap_shot_bucket_name")

    @property
    @pulumi.getter
    def snapshots(self) -> Mapping[str, Any]:
        """
        Key-value pair representing disks ID mapped to the OCIDs of replicated or hydration server volume snapshots. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "snapshots")

    @property
    @pulumi.getter(name="sourceAssetId")
    def source_asset_id(self) -> str:
        """
        OCID that is referenced to an asset for an inventory.
        """
        return pulumi.get(self, "source_asset_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the migration asset.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tenancyId")
    def tenancy_id(self) -> str:
        """
        Tenancy identifier
        """
        return pulumi.get(self, "tenancy_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time when the migration asset was created. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time when the migration asset was updated. An RFC3339 formatted datetime string.
        """
        return pulumi.get(self, "time_updated")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of asset referenced for inventory.
        """
        return pulumi.get(self, "type")


class AwaitableGetMigrationAssetResult(GetMigrationAssetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMigrationAssetResult(
            availability_domain=self.availability_domain,
            compartment_id=self.compartment_id,
            depended_on_bies=self.depended_on_bies,
            display_name=self.display_name,
            id=self.id,
            inventory_asset_id=self.inventory_asset_id,
            lifecycle_details=self.lifecycle_details,
            migration_asset_depends_ons=self.migration_asset_depends_ons,
            migration_asset_id=self.migration_asset_id,
            migration_id=self.migration_id,
            notifications=self.notifications,
            parent_snapshot=self.parent_snapshot,
            replication_compartment_id=self.replication_compartment_id,
            replication_schedule_id=self.replication_schedule_id,
            snap_shot_bucket_name=self.snap_shot_bucket_name,
            snapshots=self.snapshots,
            source_asset_id=self.source_asset_id,
            state=self.state,
            tenancy_id=self.tenancy_id,
            time_created=self.time_created,
            time_updated=self.time_updated,
            type=self.type)


def get_migration_asset(migration_asset_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMigrationAssetResult:
    """
    This data source provides details about a specific Migration Asset resource in Oracle Cloud Infrastructure Cloud Migrations service.

    Gets a migration asset by identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_migration_asset = oci.CloudMigrations.get_migration_asset(migration_asset_id=test_migration_asset_oci_cloud_migrations_migration_asset["id"])
    ```


    :param str migration_asset_id: Unique migration asset identifier
    """
    __args__ = dict()
    __args__['migrationAssetId'] = migration_asset_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:CloudMigrations/getMigrationAsset:getMigrationAsset', __args__, opts=opts, typ=GetMigrationAssetResult).value

    return AwaitableGetMigrationAssetResult(
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        depended_on_bies=pulumi.get(__ret__, 'depended_on_bies'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        inventory_asset_id=pulumi.get(__ret__, 'inventory_asset_id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        migration_asset_depends_ons=pulumi.get(__ret__, 'migration_asset_depends_ons'),
        migration_asset_id=pulumi.get(__ret__, 'migration_asset_id'),
        migration_id=pulumi.get(__ret__, 'migration_id'),
        notifications=pulumi.get(__ret__, 'notifications'),
        parent_snapshot=pulumi.get(__ret__, 'parent_snapshot'),
        replication_compartment_id=pulumi.get(__ret__, 'replication_compartment_id'),
        replication_schedule_id=pulumi.get(__ret__, 'replication_schedule_id'),
        snap_shot_bucket_name=pulumi.get(__ret__, 'snap_shot_bucket_name'),
        snapshots=pulumi.get(__ret__, 'snapshots'),
        source_asset_id=pulumi.get(__ret__, 'source_asset_id'),
        state=pulumi.get(__ret__, 'state'),
        tenancy_id=pulumi.get(__ret__, 'tenancy_id'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_migration_asset)
def get_migration_asset_output(migration_asset_id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMigrationAssetResult]:
    """
    This data source provides details about a specific Migration Asset resource in Oracle Cloud Infrastructure Cloud Migrations service.

    Gets a migration asset by identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_migration_asset = oci.CloudMigrations.get_migration_asset(migration_asset_id=test_migration_asset_oci_cloud_migrations_migration_asset["id"])
    ```


    :param str migration_asset_id: Unique migration asset identifier
    """
    ...
