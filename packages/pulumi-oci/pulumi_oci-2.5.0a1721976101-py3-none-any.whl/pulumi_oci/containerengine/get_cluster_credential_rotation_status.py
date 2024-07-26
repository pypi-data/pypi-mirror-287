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
    'GetClusterCredentialRotationStatusResult',
    'AwaitableGetClusterCredentialRotationStatusResult',
    'get_cluster_credential_rotation_status',
    'get_cluster_credential_rotation_status_output',
]

@pulumi.output_type
class GetClusterCredentialRotationStatusResult:
    """
    A collection of values returned by getClusterCredentialRotationStatus.
    """
    def __init__(__self__, cluster_id=None, id=None, status=None, status_details=None, time_auto_completion_scheduled=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_details and not isinstance(status_details, str):
            raise TypeError("Expected argument 'status_details' to be a str")
        pulumi.set(__self__, "status_details", status_details)
        if time_auto_completion_scheduled and not isinstance(time_auto_completion_scheduled, str):
            raise TypeError("Expected argument 'time_auto_completion_scheduled' to be a str")
        pulumi.set(__self__, "time_auto_completion_scheduled", time_auto_completion_scheduled)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Credential rotation status of a kubernetes cluster IN_PROGRESS: Issuing new credentials to kubernetes cluster control plane and worker nodes or retiring old credentials from kubernetes cluster control plane and worker nodes. WAITING: Waiting for customer to invoke the complete rotation action or the automcatic complete rotation action. COMPLETED: New credentials are functional on kuberentes cluster.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> str:
        """
        Details of a kuberenetes cluster credential rotation status: ISSUING_NEW_CREDENTIALS: Credential rotation is in progress. Starting to issue new credentials to kubernetes cluster control plane and worker nodes. NEW_CREDENTIALS_ISSUED: New credentials are added. At this stage cluster has both old and new credentials and is awaiting old credentials retirement. RETIRING_OLD_CREDENTIALS: Retirement of old credentials is in progress. Starting to remove old credentials from kubernetes cluster control plane and worker nodes. COMPLETED: Credential rotation is complete. Old credentials are retired.
        """
        return pulumi.get(self, "status_details")

    @property
    @pulumi.getter(name="timeAutoCompletionScheduled")
    def time_auto_completion_scheduled(self) -> str:
        """
        The time by which retirement of old credentials should start.
        """
        return pulumi.get(self, "time_auto_completion_scheduled")


class AwaitableGetClusterCredentialRotationStatusResult(GetClusterCredentialRotationStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterCredentialRotationStatusResult(
            cluster_id=self.cluster_id,
            id=self.id,
            status=self.status,
            status_details=self.status_details,
            time_auto_completion_scheduled=self.time_auto_completion_scheduled)


def get_cluster_credential_rotation_status(cluster_id: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterCredentialRotationStatusResult:
    """
    This data source provides details about a specific Cluster Credential Rotation Status resource in Oracle Cloud Infrastructure Container Engine service.

    Get cluster credential rotation status.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cluster_credential_rotation_status = oci.ContainerEngine.get_cluster_credential_rotation_status(cluster_id=test_cluster["id"])
    ```


    :param str cluster_id: The OCID of the cluster.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:ContainerEngine/getClusterCredentialRotationStatus:getClusterCredentialRotationStatus', __args__, opts=opts, typ=GetClusterCredentialRotationStatusResult).value

    return AwaitableGetClusterCredentialRotationStatusResult(
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        id=pulumi.get(__ret__, 'id'),
        status=pulumi.get(__ret__, 'status'),
        status_details=pulumi.get(__ret__, 'status_details'),
        time_auto_completion_scheduled=pulumi.get(__ret__, 'time_auto_completion_scheduled'))


@_utilities.lift_output_func(get_cluster_credential_rotation_status)
def get_cluster_credential_rotation_status_output(cluster_id: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterCredentialRotationStatusResult]:
    """
    This data source provides details about a specific Cluster Credential Rotation Status resource in Oracle Cloud Infrastructure Container Engine service.

    Get cluster credential rotation status.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_cluster_credential_rotation_status = oci.ContainerEngine.get_cluster_credential_rotation_status(cluster_id=test_cluster["id"])
    ```


    :param str cluster_id: The OCID of the cluster.
    """
    ...
