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
    'GetSecurityAssessmentFindingsResult',
    'AwaitableGetSecurityAssessmentFindingsResult',
    'get_security_assessment_findings',
    'get_security_assessment_findings_output',
]

@pulumi.output_type
class GetSecurityAssessmentFindingsResult:
    """
    A collection of values returned by getSecurityAssessmentFindings.
    """
    def __init__(__self__, access_level=None, compartment_id_in_subtree=None, filters=None, finding_key=None, findings=None, id=None, is_top_finding=None, references=None, security_assessment_id=None, severity=None, state=None, target_id=None):
        if access_level and not isinstance(access_level, str):
            raise TypeError("Expected argument 'access_level' to be a str")
        pulumi.set(__self__, "access_level", access_level)
        if compartment_id_in_subtree and not isinstance(compartment_id_in_subtree, bool):
            raise TypeError("Expected argument 'compartment_id_in_subtree' to be a bool")
        pulumi.set(__self__, "compartment_id_in_subtree", compartment_id_in_subtree)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if finding_key and not isinstance(finding_key, str):
            raise TypeError("Expected argument 'finding_key' to be a str")
        pulumi.set(__self__, "finding_key", finding_key)
        if findings and not isinstance(findings, list):
            raise TypeError("Expected argument 'findings' to be a list")
        pulumi.set(__self__, "findings", findings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_top_finding and not isinstance(is_top_finding, bool):
            raise TypeError("Expected argument 'is_top_finding' to be a bool")
        pulumi.set(__self__, "is_top_finding", is_top_finding)
        if references and not isinstance(references, str):
            raise TypeError("Expected argument 'references' to be a str")
        pulumi.set(__self__, "references", references)
        if security_assessment_id and not isinstance(security_assessment_id, str):
            raise TypeError("Expected argument 'security_assessment_id' to be a str")
        pulumi.set(__self__, "security_assessment_id", security_assessment_id)
        if severity and not isinstance(severity, str):
            raise TypeError("Expected argument 'severity' to be a str")
        pulumi.set(__self__, "severity", severity)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[str]:
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter(name="compartmentIdInSubtree")
    def compartment_id_in_subtree(self) -> Optional[bool]:
        return pulumi.get(self, "compartment_id_in_subtree")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSecurityAssessmentFindingsFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="findingKey")
    def finding_key(self) -> Optional[str]:
        return pulumi.get(self, "finding_key")

    @property
    @pulumi.getter
    def findings(self) -> Sequence['outputs.GetSecurityAssessmentFindingsFindingResult']:
        """
        The list of findings.
        """
        return pulumi.get(self, "findings")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isTopFinding")
    def is_top_finding(self) -> Optional[bool]:
        """
        Indicates whether a given finding is marked as topFinding or not.
        """
        return pulumi.get(self, "is_top_finding")

    @property
    @pulumi.getter
    def references(self) -> Optional[str]:
        """
        Provides information on whether the finding is related to a CIS Oracle Database Benchmark recommendation, a STIG rule, or a GDPR Article/Recital.
        """
        return pulumi.get(self, "references")

    @property
    @pulumi.getter(name="securityAssessmentId")
    def security_assessment_id(self) -> str:
        return pulumi.get(self, "security_assessment_id")

    @property
    @pulumi.getter
    def severity(self) -> Optional[str]:
        """
        The severity of the finding as determined by security assessment and is same as oracleDefinedSeverity, unless modified by user.
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current state of the finding.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[str]:
        """
        The OCID of the target database.
        """
        return pulumi.get(self, "target_id")


class AwaitableGetSecurityAssessmentFindingsResult(GetSecurityAssessmentFindingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityAssessmentFindingsResult(
            access_level=self.access_level,
            compartment_id_in_subtree=self.compartment_id_in_subtree,
            filters=self.filters,
            finding_key=self.finding_key,
            findings=self.findings,
            id=self.id,
            is_top_finding=self.is_top_finding,
            references=self.references,
            security_assessment_id=self.security_assessment_id,
            severity=self.severity,
            state=self.state,
            target_id=self.target_id)


def get_security_assessment_findings(access_level: Optional[str] = None,
                                     compartment_id_in_subtree: Optional[bool] = None,
                                     filters: Optional[Sequence[pulumi.InputType['GetSecurityAssessmentFindingsFilterArgs']]] = None,
                                     finding_key: Optional[str] = None,
                                     is_top_finding: Optional[bool] = None,
                                     references: Optional[str] = None,
                                     security_assessment_id: Optional[str] = None,
                                     severity: Optional[str] = None,
                                     state: Optional[str] = None,
                                     target_id: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityAssessmentFindingsResult:
    """
    This data source provides the list of Security Assessment Findings in Oracle Cloud Infrastructure Data Safe service.

    List all the findings from all the targets in the specified compartment.


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str finding_key: Each finding in security assessment has an associated key (think of key as a finding's name). For a given finding, the key will be the same across targets. The user can use these keys to filter the findings.
    :param bool is_top_finding: A filter to return only the findings that are marked as top findings.
    :param str references: An optional filter to return only findings containing the specified reference.
    :param str security_assessment_id: The OCID of the security assessment.
    :param str severity: A filter to return only findings of a particular risk level.
    :param str state: A filter to return only the findings that match the specified lifecycle states.
    :param str target_id: A filter to return only items related to a specific target OCID.
    """
    __args__ = dict()
    __args__['accessLevel'] = access_level
    __args__['compartmentIdInSubtree'] = compartment_id_in_subtree
    __args__['filters'] = filters
    __args__['findingKey'] = finding_key
    __args__['isTopFinding'] = is_top_finding
    __args__['references'] = references
    __args__['securityAssessmentId'] = security_assessment_id
    __args__['severity'] = severity
    __args__['state'] = state
    __args__['targetId'] = target_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:DataSafe/getSecurityAssessmentFindings:getSecurityAssessmentFindings', __args__, opts=opts, typ=GetSecurityAssessmentFindingsResult).value

    return AwaitableGetSecurityAssessmentFindingsResult(
        access_level=pulumi.get(__ret__, 'access_level'),
        compartment_id_in_subtree=pulumi.get(__ret__, 'compartment_id_in_subtree'),
        filters=pulumi.get(__ret__, 'filters'),
        finding_key=pulumi.get(__ret__, 'finding_key'),
        findings=pulumi.get(__ret__, 'findings'),
        id=pulumi.get(__ret__, 'id'),
        is_top_finding=pulumi.get(__ret__, 'is_top_finding'),
        references=pulumi.get(__ret__, 'references'),
        security_assessment_id=pulumi.get(__ret__, 'security_assessment_id'),
        severity=pulumi.get(__ret__, 'severity'),
        state=pulumi.get(__ret__, 'state'),
        target_id=pulumi.get(__ret__, 'target_id'))


@_utilities.lift_output_func(get_security_assessment_findings)
def get_security_assessment_findings_output(access_level: Optional[pulumi.Input[Optional[str]]] = None,
                                            compartment_id_in_subtree: Optional[pulumi.Input[Optional[bool]]] = None,
                                            filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSecurityAssessmentFindingsFilterArgs']]]]] = None,
                                            finding_key: Optional[pulumi.Input[Optional[str]]] = None,
                                            is_top_finding: Optional[pulumi.Input[Optional[bool]]] = None,
                                            references: Optional[pulumi.Input[Optional[str]]] = None,
                                            security_assessment_id: Optional[pulumi.Input[str]] = None,
                                            severity: Optional[pulumi.Input[Optional[str]]] = None,
                                            state: Optional[pulumi.Input[Optional[str]]] = None,
                                            target_id: Optional[pulumi.Input[Optional[str]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityAssessmentFindingsResult]:
    """
    This data source provides the list of Security Assessment Findings in Oracle Cloud Infrastructure Data Safe service.

    List all the findings from all the targets in the specified compartment.


    :param str access_level: Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
    :param bool compartment_id_in_subtree: Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.
    :param str finding_key: Each finding in security assessment has an associated key (think of key as a finding's name). For a given finding, the key will be the same across targets. The user can use these keys to filter the findings.
    :param bool is_top_finding: A filter to return only the findings that are marked as top findings.
    :param str references: An optional filter to return only findings containing the specified reference.
    :param str security_assessment_id: The OCID of the security assessment.
    :param str severity: A filter to return only findings of a particular risk level.
    :param str state: A filter to return only the findings that match the specified lifecycle states.
    :param str target_id: A filter to return only items related to a specific target OCID.
    """
    ...
