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
    'GetSecurityPolicyDeploymentResult',
    'AwaitableGetSecurityPolicyDeploymentResult',
    'get_security_policy_deployment',
    'get_security_policy_deployment_output',
]

@pulumi.output_type
class GetSecurityPolicyDeploymentResult:
    """
    A collection of values returned by getSecurityPolicyDeployment.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, description=None, display_name=None, freeform_tags=None, id=None, lifecycle_details=None, security_policy_deployment_id=None, security_policy_id=None, state=None, system_tags=None, target_id=None, time_created=None, time_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lifecycle_details and not isinstance(lifecycle_details, str):
            raise TypeError("Expected argument 'lifecycle_details' to be a str")
        pulumi.set(__self__, "lifecycle_details", lifecycle_details)
        if security_policy_deployment_id and not isinstance(security_policy_deployment_id, str):
            raise TypeError("Expected argument 'security_policy_deployment_id' to be a str")
        pulumi.set(__self__, "security_policy_deployment_id", security_policy_deployment_id)
        if security_policy_id and not isinstance(security_policy_id, str):
            raise TypeError("Expected argument 'security_policy_id' to be a str")
        pulumi.set(__self__, "security_policy_id", security_policy_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_updated and not isinstance(time_updated, str):
            raise TypeError("Expected argument 'time_updated' to be a str")
        pulumi.set(__self__, "time_updated", time_updated)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID of the compartment containing the security policy deployment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Operations.CostCenter": "42"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the security policy deployment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the security policy deployment.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)  Example: `{"Department": "Finance"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The OCID of the security policy deployment.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> str:
        """
        Details about the current state of the security policy deployment in Data Safe.
        """
        return pulumi.get(self, "lifecycle_details")

    @property
    @pulumi.getter(name="securityPolicyDeploymentId")
    def security_policy_deployment_id(self) -> str:
        return pulumi.get(self, "security_policy_deployment_id")

    @property
    @pulumi.getter(name="securityPolicyId")
    def security_policy_id(self) -> str:
        """
        The OCID of the security policy corresponding to the security policy deployment.
        """
        return pulumi.get(self, "security_policy_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the security policy deployment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> str:
        """
        The OCID of the target where the security policy is deployed.
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time that the security policy deployment was created, in the format defined by RFC3339.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The last date and time the security policy deployment was updated, in the format defined by RFC3339.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetSecurityPolicyDeploymentResult(GetSecurityPolicyDeploymentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityPolicyDeploymentResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            description=self.description,
            display_name=self.display_name,
            freeform_tags=self.freeform_tags,
            id=self.id,
            lifecycle_details=self.lifecycle_details,
            security_policy_deployment_id=self.security_policy_deployment_id,
            security_policy_id=self.security_policy_id,
            state=self.state,
            system_tags=self.system_tags,
            target_id=self.target_id,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_security_policy_deployment(security_policy_deployment_id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityPolicyDeploymentResult:
    """
    This data source provides details about a specific Security Policy Deployment resource in Oracle Cloud Infrastructure Data Safe service.

    Gets a security policy deployment by identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_security_policy_deployment = oci.DataSafe.get_security_policy_deployment(security_policy_deployment_id=test_security_policy_deployment_oci_data_safe_security_policy_deployment["id"])
    ```


    :param str security_policy_deployment_id: The OCID of the security policy deployment resource.
    """
    __args__ = dict()
    __args__['securityPolicyDeploymentId'] = security_policy_deployment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getSecurityPolicyDeployment:getSecurityPolicyDeployment', __args__, opts=opts, typ=GetSecurityPolicyDeploymentResult).value

    return AwaitableGetSecurityPolicyDeploymentResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        lifecycle_details=pulumi.get(__ret__, 'lifecycle_details'),
        security_policy_deployment_id=pulumi.get(__ret__, 'security_policy_deployment_id'),
        security_policy_id=pulumi.get(__ret__, 'security_policy_id'),
        state=pulumi.get(__ret__, 'state'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        target_id=pulumi.get(__ret__, 'target_id'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_security_policy_deployment)
def get_security_policy_deployment_output(security_policy_deployment_id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityPolicyDeploymentResult]:
    """
    This data source provides details about a specific Security Policy Deployment resource in Oracle Cloud Infrastructure Data Safe service.

    Gets a security policy deployment by identifier.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_security_policy_deployment = oci.DataSafe.get_security_policy_deployment(security_policy_deployment_id=test_security_policy_deployment_oci_data_safe_security_policy_deployment["id"])
    ```


    :param str security_policy_deployment_id: The OCID of the security policy deployment resource.
    """
    ...
