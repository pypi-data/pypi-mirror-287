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

__all__ = [
    'GetVolumeResult',
    'AwaitableGetVolumeResult',
    'get_volume',
    'get_volume_output',
]

@pulumi.output_type
class GetVolumeResult:
    """
    A collection of values returned by getVolume.
    """
    def __init__(__self__, auto_tuned_vpus_per_gb=None, autotune_policies=None, availability_domain=None, backup_policy_id=None, block_volume_replicas=None, block_volume_replicas_deletion=None, cluster_placement_group_id=None, compartment_id=None, defined_tags=None, display_name=None, freeform_tags=None, id=None, is_auto_tune_enabled=None, is_hydrated=None, kms_key_id=None, size_in_gbs=None, size_in_mbs=None, source_details=None, state=None, system_tags=None, time_created=None, volume_backup_id=None, volume_group_id=None, volume_id=None, vpus_per_gb=None):
        if auto_tuned_vpus_per_gb and not isinstance(auto_tuned_vpus_per_gb, str):
            raise TypeError("Expected argument 'auto_tuned_vpus_per_gb' to be a str")
        pulumi.set(__self__, "auto_tuned_vpus_per_gb", auto_tuned_vpus_per_gb)
        if autotune_policies and not isinstance(autotune_policies, list):
            raise TypeError("Expected argument 'autotune_policies' to be a list")
        pulumi.set(__self__, "autotune_policies", autotune_policies)
        if availability_domain and not isinstance(availability_domain, str):
            raise TypeError("Expected argument 'availability_domain' to be a str")
        pulumi.set(__self__, "availability_domain", availability_domain)
        if backup_policy_id and not isinstance(backup_policy_id, str):
            raise TypeError("Expected argument 'backup_policy_id' to be a str")
        pulumi.set(__self__, "backup_policy_id", backup_policy_id)
        if block_volume_replicas and not isinstance(block_volume_replicas, list):
            raise TypeError("Expected argument 'block_volume_replicas' to be a list")
        pulumi.set(__self__, "block_volume_replicas", block_volume_replicas)
        if block_volume_replicas_deletion and not isinstance(block_volume_replicas_deletion, bool):
            raise TypeError("Expected argument 'block_volume_replicas_deletion' to be a bool")
        pulumi.set(__self__, "block_volume_replicas_deletion", block_volume_replicas_deletion)
        if cluster_placement_group_id and not isinstance(cluster_placement_group_id, str):
            raise TypeError("Expected argument 'cluster_placement_group_id' to be a str")
        pulumi.set(__self__, "cluster_placement_group_id", cluster_placement_group_id)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_auto_tune_enabled and not isinstance(is_auto_tune_enabled, bool):
            raise TypeError("Expected argument 'is_auto_tune_enabled' to be a bool")
        pulumi.set(__self__, "is_auto_tune_enabled", is_auto_tune_enabled)
        if is_hydrated and not isinstance(is_hydrated, bool):
            raise TypeError("Expected argument 'is_hydrated' to be a bool")
        pulumi.set(__self__, "is_hydrated", is_hydrated)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if size_in_gbs and not isinstance(size_in_gbs, str):
            raise TypeError("Expected argument 'size_in_gbs' to be a str")
        pulumi.set(__self__, "size_in_gbs", size_in_gbs)
        if size_in_mbs and not isinstance(size_in_mbs, str):
            raise TypeError("Expected argument 'size_in_mbs' to be a str")
        pulumi.set(__self__, "size_in_mbs", size_in_mbs)
        if source_details and not isinstance(source_details, list):
            raise TypeError("Expected argument 'source_details' to be a list")
        pulumi.set(__self__, "source_details", source_details)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if volume_backup_id and not isinstance(volume_backup_id, str):
            raise TypeError("Expected argument 'volume_backup_id' to be a str")
        pulumi.set(__self__, "volume_backup_id", volume_backup_id)
        if volume_group_id and not isinstance(volume_group_id, str):
            raise TypeError("Expected argument 'volume_group_id' to be a str")
        pulumi.set(__self__, "volume_group_id", volume_group_id)
        if volume_id and not isinstance(volume_id, str):
            raise TypeError("Expected argument 'volume_id' to be a str")
        pulumi.set(__self__, "volume_id", volume_id)
        if vpus_per_gb and not isinstance(vpus_per_gb, str):
            raise TypeError("Expected argument 'vpus_per_gb' to be a str")
        pulumi.set(__self__, "vpus_per_gb", vpus_per_gb)

    @property
    @pulumi.getter(name="autoTunedVpusPerGb")
    def auto_tuned_vpus_per_gb(self) -> str:
        """
        The number of Volume Performance Units per GB that this volume is effectively tuned to.
        """
        return pulumi.get(self, "auto_tuned_vpus_per_gb")

    @property
    @pulumi.getter(name="autotunePolicies")
    def autotune_policies(self) -> Sequence['outputs.GetVolumeAutotunePolicyResult']:
        """
        The list of autotune policies enabled for this volume.
        """
        return pulumi.get(self, "autotune_policies")

    @property
    @pulumi.getter(name="availabilityDomain")
    def availability_domain(self) -> str:
        """
        The availability domain of the block volume replica.  Example: `Uocm:PHX-AD-1`
        """
        return pulumi.get(self, "availability_domain")

    @property
    @pulumi.getter(name="backupPolicyId")
    @_utilities.deprecated("""The 'backup_policy_id' field has been deprecated. Please use the 'oci_core_volume_backup_policy_assignment' resource instead.""")
    def backup_policy_id(self) -> str:
        return pulumi.get(self, "backup_policy_id")

    @property
    @pulumi.getter(name="blockVolumeReplicas")
    def block_volume_replicas(self) -> Sequence['outputs.GetVolumeBlockVolumeReplicaResult']:
        """
        The list of block volume replicas of this volume.
        """
        return pulumi.get(self, "block_volume_replicas")

    @property
    @pulumi.getter(name="blockVolumeReplicasDeletion")
    def block_volume_replicas_deletion(self) -> bool:
        return pulumi.get(self, "block_volume_replicas_deletion")

    @property
    @pulumi.getter(name="clusterPlacementGroupId")
    def cluster_placement_group_id(self) -> str:
        """
        The clusterPlacementGroup Id of the volume for volume placement.
        """
        return pulumi.get(self, "cluster_placement_group_id")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment that contains the volume.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the block volume replica.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAutoTuneEnabled")
    def is_auto_tune_enabled(self) -> bool:
        """
        Specifies whether the auto-tune performance is enabled for this volume. This field is deprecated. Use the `DetachedVolumeAutotunePolicy` instead to enable the volume for detached autotune.
        """
        return pulumi.get(self, "is_auto_tune_enabled")

    @property
    @pulumi.getter(name="isHydrated")
    def is_hydrated(self) -> bool:
        """
        Specifies whether the cloned volume's data has finished copying from the source volume or backup.
        """
        return pulumi.get(self, "is_hydrated")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> str:
        """
        The OCID of the Vault service key which is the master encryption key for the volume.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="sizeInGbs")
    def size_in_gbs(self) -> str:
        """
        The size of the volume in GBs.
        """
        return pulumi.get(self, "size_in_gbs")

    @property
    @pulumi.getter(name="sizeInMbs")
    @_utilities.deprecated("""The 'size_in_mbs' field has been deprecated. Please use 'size_in_gbs' instead.""")
    def size_in_mbs(self) -> str:
        """
        The size of the volume in MBs. This field is deprecated. Use sizeInGBs instead.
        """
        return pulumi.get(self, "size_in_mbs")

    @property
    @pulumi.getter(name="sourceDetails")
    def source_details(self) -> Sequence['outputs.GetVolumeSourceDetailResult']:
        return pulumi.get(self, "source_details")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of a volume.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The date and time the volume was created. Format defined by [RFC3339](https://tools.ietf.org/html/rfc3339).
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="volumeBackupId")
    def volume_backup_id(self) -> str:
        return pulumi.get(self, "volume_backup_id")

    @property
    @pulumi.getter(name="volumeGroupId")
    def volume_group_id(self) -> str:
        """
        The OCID of the source volume group.
        """
        return pulumi.get(self, "volume_group_id")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> str:
        return pulumi.get(self, "volume_id")

    @property
    @pulumi.getter(name="vpusPerGb")
    def vpus_per_gb(self) -> str:
        """
        The number of volume performance units (VPUs) that will be applied to this volume per GB, representing the Block Volume service's elastic performance options. See [Block Volume Performance Levels](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/blockvolumeperformance.htm#perf_levels) for more information.
        """
        return pulumi.get(self, "vpus_per_gb")


class AwaitableGetVolumeResult(GetVolumeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeResult(
            auto_tuned_vpus_per_gb=self.auto_tuned_vpus_per_gb,
            autotune_policies=self.autotune_policies,
            availability_domain=self.availability_domain,
            backup_policy_id=self.backup_policy_id,
            block_volume_replicas=self.block_volume_replicas,
            block_volume_replicas_deletion=self.block_volume_replicas_deletion,
            cluster_placement_group_id=self.cluster_placement_group_id,
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            is_auto_tune_enabled=self.is_auto_tune_enabled,
            is_hydrated=self.is_hydrated,
            kms_key_id=self.kms_key_id,
            size_in_gbs=self.size_in_gbs,
            size_in_mbs=self.size_in_mbs,
            source_details=self.source_details,
            state=self.state,
            system_tags=self.system_tags,
            time_created=self.time_created,
            volume_backup_id=self.volume_backup_id,
            volume_group_id=self.volume_group_id,
            volume_id=self.volume_id,
            vpus_per_gb=self.vpus_per_gb)


def get_volume(volume_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeResult:
    """
    This data source provides details about a specific Volume resource in Oracle Cloud Infrastructure Core service.

    Gets information for the specified volume.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_volume = oci.Core.get_volume(volume_id=test_volume_oci_core_volume["id"])
    ```


    :param str volume_id: The OCID of the volume.
    """
    __args__ = dict()
    __args__['volumeId'] = volume_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Core/getVolume:getVolume', __args__, opts=opts, typ=GetVolumeResult).value

    return AwaitableGetVolumeResult(
        auto_tuned_vpus_per_gb=pulumi.get(__ret__, 'auto_tuned_vpus_per_gb'),
        autotune_policies=pulumi.get(__ret__, 'autotune_policies'),
        availability_domain=pulumi.get(__ret__, 'availability_domain'),
        backup_policy_id=pulumi.get(__ret__, 'backup_policy_id'),
        block_volume_replicas=pulumi.get(__ret__, 'block_volume_replicas'),
        block_volume_replicas_deletion=pulumi.get(__ret__, 'block_volume_replicas_deletion'),
        cluster_placement_group_id=pulumi.get(__ret__, 'cluster_placement_group_id'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        is_auto_tune_enabled=pulumi.get(__ret__, 'is_auto_tune_enabled'),
        is_hydrated=pulumi.get(__ret__, 'is_hydrated'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        size_in_gbs=pulumi.get(__ret__, 'size_in_gbs'),
        size_in_mbs=pulumi.get(__ret__, 'size_in_mbs'),
        source_details=pulumi.get(__ret__, 'source_details'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        volume_backup_id=pulumi.get(__ret__, 'volume_backup_id'),
        volume_group_id=pulumi.get(__ret__, 'volume_group_id'),
        volume_id=pulumi.get(__ret__, 'volume_id'),
        vpus_per_gb=pulumi.get(__ret__, 'vpus_per_gb'))


@_utilities.lift_output_func(get_volume)
def get_volume_output(volume_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumeResult]:
    """
    This data source provides details about a specific Volume resource in Oracle Cloud Infrastructure Core service.

    Gets information for the specified volume.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_volume = oci.Core.get_volume(volume_id=test_volume_oci_core_volume["id"])
    ```


    :param str volume_id: The OCID of the volume.
    """
    ...
