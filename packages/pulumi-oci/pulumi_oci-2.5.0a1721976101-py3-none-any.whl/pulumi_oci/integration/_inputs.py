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
    'IntegrationInstanceAlternateCustomEndpointArgs',
    'IntegrationInstanceAttachmentArgs',
    'IntegrationInstanceCustomEndpointArgs',
    'IntegrationInstanceIdcsInfoArgs',
    'IntegrationInstanceNetworkEndpointDetailsArgs',
    'IntegrationInstanceNetworkEndpointDetailsAllowlistedHttpVcnArgs',
    'IntegrationInstancePrivateEndpointOutboundConnectionArgs',
    'GetIntegrationInstancesFilterArgs',
]

@pulumi.input_type
class IntegrationInstanceAlternateCustomEndpointArgs:
    def __init__(__self__, *,
                 hostname: pulumi.Input[str],
                 alias: Optional[pulumi.Input[str]] = None,
                 certificate_secret_id: Optional[pulumi.Input[str]] = None,
                 certificate_secret_version: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] hostname: (Updatable) A custom hostname to be used for the integration instance URL, in FQDN format.
        :param pulumi.Input[str] alias: When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.
        :param pulumi.Input[str] certificate_secret_id: (Updatable) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname. All certificates should be stored in a single base64 encoded secret Note the update will fail if this is not a valid certificate.
        :param pulumi.Input[int] certificate_secret_version: The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
        """
        pulumi.set(__self__, "hostname", hostname)
        if alias is not None:
            pulumi.set(__self__, "alias", alias)
        if certificate_secret_id is not None:
            pulumi.set(__self__, "certificate_secret_id", certificate_secret_id)
        if certificate_secret_version is not None:
            pulumi.set(__self__, "certificate_secret_version", certificate_secret_version)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[str]:
        """
        (Updatable) A custom hostname to be used for the integration instance URL, in FQDN format.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[str]]:
        """
        When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter(name="certificateSecretId")
    def certificate_secret_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname. All certificates should be stored in a single base64 encoded secret Note the update will fail if this is not a valid certificate.
        """
        return pulumi.get(self, "certificate_secret_id")

    @certificate_secret_id.setter
    def certificate_secret_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_secret_id", value)

    @property
    @pulumi.getter(name="certificateSecretVersion")
    def certificate_secret_version(self) -> Optional[pulumi.Input[int]]:
        """
        The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
        """
        return pulumi.get(self, "certificate_secret_version")

    @certificate_secret_version.setter
    def certificate_secret_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "certificate_secret_version", value)


@pulumi.input_type
class IntegrationInstanceAttachmentArgs:
    def __init__(__self__, *,
                 is_implicit: Optional[pulumi.Input[bool]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 target_instance_url: Optional[pulumi.Input[str]] = None,
                 target_role: Optional[pulumi.Input[str]] = None,
                 target_service_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] is_implicit: * If role == `PARENT`, the attached instance was created by this service instance
               * If role == `CHILD`, this instance was created from attached instance on behalf of a user
        :param pulumi.Input[str] target_id: The OCID of the target instance (which could be any other Oracle Cloud Infrastructure PaaS/SaaS resource), to which this instance is attached.
        :param pulumi.Input[str] target_instance_url: The dataplane instance URL of the attached instance
        :param pulumi.Input[str] target_role: The role of the target attachment.
               * `PARENT` - The target instance is the parent of this attachment.
               * `CHILD` - The target instance is the child of this attachment.
        :param pulumi.Input[str] target_service_type: The type of the target instance, such as "FUSION".
        """
        if is_implicit is not None:
            pulumi.set(__self__, "is_implicit", is_implicit)
        if target_id is not None:
            pulumi.set(__self__, "target_id", target_id)
        if target_instance_url is not None:
            pulumi.set(__self__, "target_instance_url", target_instance_url)
        if target_role is not None:
            pulumi.set(__self__, "target_role", target_role)
        if target_service_type is not None:
            pulumi.set(__self__, "target_service_type", target_service_type)

    @property
    @pulumi.getter(name="isImplicit")
    def is_implicit(self) -> Optional[pulumi.Input[bool]]:
        """
        * If role == `PARENT`, the attached instance was created by this service instance
        * If role == `CHILD`, this instance was created from attached instance on behalf of a user
        """
        return pulumi.get(self, "is_implicit")

    @is_implicit.setter
    def is_implicit(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_implicit", value)

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the target instance (which could be any other Oracle Cloud Infrastructure PaaS/SaaS resource), to which this instance is attached.
        """
        return pulumi.get(self, "target_id")

    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_id", value)

    @property
    @pulumi.getter(name="targetInstanceUrl")
    def target_instance_url(self) -> Optional[pulumi.Input[str]]:
        """
        The dataplane instance URL of the attached instance
        """
        return pulumi.get(self, "target_instance_url")

    @target_instance_url.setter
    def target_instance_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_instance_url", value)

    @property
    @pulumi.getter(name="targetRole")
    def target_role(self) -> Optional[pulumi.Input[str]]:
        """
        The role of the target attachment.
        * `PARENT` - The target instance is the parent of this attachment.
        * `CHILD` - The target instance is the child of this attachment.
        """
        return pulumi.get(self, "target_role")

    @target_role.setter
    def target_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_role", value)

    @property
    @pulumi.getter(name="targetServiceType")
    def target_service_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the target instance, such as "FUSION".
        """
        return pulumi.get(self, "target_service_type")

    @target_service_type.setter
    def target_service_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_service_type", value)


@pulumi.input_type
class IntegrationInstanceCustomEndpointArgs:
    def __init__(__self__, *,
                 hostname: pulumi.Input[str],
                 alias: Optional[pulumi.Input[str]] = None,
                 certificate_secret_id: Optional[pulumi.Input[str]] = None,
                 certificate_secret_version: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] hostname: (Updatable) A custom hostname to be used for the integration instance URL, in FQDN format.
        :param pulumi.Input[str] alias: When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.
        :param pulumi.Input[str] certificate_secret_id: (Updatable) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname. All certificates should be stored in a single base64 encoded secret Note the update will fail if this is not a valid certificate.
        :param pulumi.Input[int] certificate_secret_version: The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
        """
        pulumi.set(__self__, "hostname", hostname)
        if alias is not None:
            pulumi.set(__self__, "alias", alias)
        if certificate_secret_id is not None:
            pulumi.set(__self__, "certificate_secret_id", certificate_secret_id)
        if certificate_secret_version is not None:
            pulumi.set(__self__, "certificate_secret_version", certificate_secret_version)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[str]:
        """
        (Updatable) A custom hostname to be used for the integration instance URL, in FQDN format.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[str]]:
        """
        When creating the DNS CNAME record for the custom hostname, this value must be specified in the rdata.
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter(name="certificateSecretId")
    def certificate_secret_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Updatable) Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname. All certificates should be stored in a single base64 encoded secret Note the update will fail if this is not a valid certificate.
        """
        return pulumi.get(self, "certificate_secret_id")

    @certificate_secret_id.setter
    def certificate_secret_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_secret_id", value)

    @property
    @pulumi.getter(name="certificateSecretVersion")
    def certificate_secret_version(self) -> Optional[pulumi.Input[int]]:
        """
        The secret version used for the certificate-secret-id (if certificate-secret-id is specified).
        """
        return pulumi.get(self, "certificate_secret_version")

    @certificate_secret_version.setter
    def certificate_secret_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "certificate_secret_version", value)


@pulumi.input_type
class IntegrationInstanceIdcsInfoArgs:
    def __init__(__self__, *,
                 idcs_app_display_name: Optional[pulumi.Input[str]] = None,
                 idcs_app_id: Optional[pulumi.Input[str]] = None,
                 idcs_app_location_url: Optional[pulumi.Input[str]] = None,
                 idcs_app_name: Optional[pulumi.Input[str]] = None,
                 instance_primary_audience_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] idcs_app_display_name: The IDCS application display name associated with the instance
        :param pulumi.Input[str] idcs_app_id: The IDCS application ID associated with the instance
        :param pulumi.Input[str] idcs_app_location_url: URL for the location of the IDCS Application (used by IDCS APIs)
        :param pulumi.Input[str] idcs_app_name: The IDCS application name associated with the instance
        :param pulumi.Input[str] instance_primary_audience_url: The URL used as the primary audience for integration flows in this instance type: string
        """
        if idcs_app_display_name is not None:
            pulumi.set(__self__, "idcs_app_display_name", idcs_app_display_name)
        if idcs_app_id is not None:
            pulumi.set(__self__, "idcs_app_id", idcs_app_id)
        if idcs_app_location_url is not None:
            pulumi.set(__self__, "idcs_app_location_url", idcs_app_location_url)
        if idcs_app_name is not None:
            pulumi.set(__self__, "idcs_app_name", idcs_app_name)
        if instance_primary_audience_url is not None:
            pulumi.set(__self__, "instance_primary_audience_url", instance_primary_audience_url)

    @property
    @pulumi.getter(name="idcsAppDisplayName")
    def idcs_app_display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The IDCS application display name associated with the instance
        """
        return pulumi.get(self, "idcs_app_display_name")

    @idcs_app_display_name.setter
    def idcs_app_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "idcs_app_display_name", value)

    @property
    @pulumi.getter(name="idcsAppId")
    def idcs_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The IDCS application ID associated with the instance
        """
        return pulumi.get(self, "idcs_app_id")

    @idcs_app_id.setter
    def idcs_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "idcs_app_id", value)

    @property
    @pulumi.getter(name="idcsAppLocationUrl")
    def idcs_app_location_url(self) -> Optional[pulumi.Input[str]]:
        """
        URL for the location of the IDCS Application (used by IDCS APIs)
        """
        return pulumi.get(self, "idcs_app_location_url")

    @idcs_app_location_url.setter
    def idcs_app_location_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "idcs_app_location_url", value)

    @property
    @pulumi.getter(name="idcsAppName")
    def idcs_app_name(self) -> Optional[pulumi.Input[str]]:
        """
        The IDCS application name associated with the instance
        """
        return pulumi.get(self, "idcs_app_name")

    @idcs_app_name.setter
    def idcs_app_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "idcs_app_name", value)

    @property
    @pulumi.getter(name="instancePrimaryAudienceUrl")
    def instance_primary_audience_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL used as the primary audience for integration flows in this instance type: string
        """
        return pulumi.get(self, "instance_primary_audience_url")

    @instance_primary_audience_url.setter
    def instance_primary_audience_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_primary_audience_url", value)


@pulumi.input_type
class IntegrationInstanceNetworkEndpointDetailsArgs:
    def __init__(__self__, *,
                 network_endpoint_type: pulumi.Input[str],
                 allowlisted_http_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allowlisted_http_vcns: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationInstanceNetworkEndpointDetailsAllowlistedHttpVcnArgs']]]] = None,
                 is_integration_vcn_allowlisted: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] network_endpoint_type: The type of network endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowlisted_http_ips: Source IP addresses or IP address ranges ingress rules. (ex: "168.122.59.5", "10.20.30.0/26") An invalid IP or CIDR block will result in a 400 response.
        :param pulumi.Input[Sequence[pulumi.Input['IntegrationInstanceNetworkEndpointDetailsAllowlistedHttpVcnArgs']]] allowlisted_http_vcns: Virtual Cloud Networks allowed to access this network endpoint.
        :param pulumi.Input[bool] is_integration_vcn_allowlisted: The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
        """
        pulumi.set(__self__, "network_endpoint_type", network_endpoint_type)
        if allowlisted_http_ips is not None:
            pulumi.set(__self__, "allowlisted_http_ips", allowlisted_http_ips)
        if allowlisted_http_vcns is not None:
            pulumi.set(__self__, "allowlisted_http_vcns", allowlisted_http_vcns)
        if is_integration_vcn_allowlisted is not None:
            pulumi.set(__self__, "is_integration_vcn_allowlisted", is_integration_vcn_allowlisted)

    @property
    @pulumi.getter(name="networkEndpointType")
    def network_endpoint_type(self) -> pulumi.Input[str]:
        """
        The type of network endpoint.
        """
        return pulumi.get(self, "network_endpoint_type")

    @network_endpoint_type.setter
    def network_endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_endpoint_type", value)

    @property
    @pulumi.getter(name="allowlistedHttpIps")
    def allowlisted_http_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Source IP addresses or IP address ranges ingress rules. (ex: "168.122.59.5", "10.20.30.0/26") An invalid IP or CIDR block will result in a 400 response.
        """
        return pulumi.get(self, "allowlisted_http_ips")

    @allowlisted_http_ips.setter
    def allowlisted_http_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowlisted_http_ips", value)

    @property
    @pulumi.getter(name="allowlistedHttpVcns")
    def allowlisted_http_vcns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationInstanceNetworkEndpointDetailsAllowlistedHttpVcnArgs']]]]:
        """
        Virtual Cloud Networks allowed to access this network endpoint.
        """
        return pulumi.get(self, "allowlisted_http_vcns")

    @allowlisted_http_vcns.setter
    def allowlisted_http_vcns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationInstanceNetworkEndpointDetailsAllowlistedHttpVcnArgs']]]]):
        pulumi.set(self, "allowlisted_http_vcns", value)

    @property
    @pulumi.getter(name="isIntegrationVcnAllowlisted")
    def is_integration_vcn_allowlisted(self) -> Optional[pulumi.Input[bool]]:
        """
        The Integration service's VCN is allow-listed to allow integrations to call back into other integrations
        """
        return pulumi.get(self, "is_integration_vcn_allowlisted")

    @is_integration_vcn_allowlisted.setter
    def is_integration_vcn_allowlisted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_integration_vcn_allowlisted", value)


@pulumi.input_type
class IntegrationInstanceNetworkEndpointDetailsAllowlistedHttpVcnArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 allowlisted_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] id: The Virtual Cloud Network OCID.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowlisted_ips: Source IP addresses or IP address ranges ingress rules. (ex: "168.122.59.5", "10.20.30.0/26") An invalid IP or CIDR block will result in a 400 response.
        """
        pulumi.set(__self__, "id", id)
        if allowlisted_ips is not None:
            pulumi.set(__self__, "allowlisted_ips", allowlisted_ips)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The Virtual Cloud Network OCID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="allowlistedIps")
    def allowlisted_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Source IP addresses or IP address ranges ingress rules. (ex: "168.122.59.5", "10.20.30.0/26") An invalid IP or CIDR block will result in a 400 response.
        """
        return pulumi.get(self, "allowlisted_ips")

    @allowlisted_ips.setter
    def allowlisted_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowlisted_ips", value)


@pulumi.input_type
class IntegrationInstancePrivateEndpointOutboundConnectionArgs:
    def __init__(__self__, *,
                 nsg_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 outbound_connection_type: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] nsg_ids: One or more Network security group Ids. This is an optional argument.
        :param pulumi.Input[str] outbound_connection_type: The type of Outbound Connection.
        :param pulumi.Input[str] subnet_id: Customer Private Network VCN Subnet OCID. This is a required argument.
        """
        if nsg_ids is not None:
            pulumi.set(__self__, "nsg_ids", nsg_ids)
        if outbound_connection_type is not None:
            pulumi.set(__self__, "outbound_connection_type", outbound_connection_type)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="nsgIds")
    def nsg_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        One or more Network security group Ids. This is an optional argument.
        """
        return pulumi.get(self, "nsg_ids")

    @nsg_ids.setter
    def nsg_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "nsg_ids", value)

    @property
    @pulumi.getter(name="outboundConnectionType")
    def outbound_connection_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of Outbound Connection.
        """
        return pulumi.get(self, "outbound_connection_type")

    @outbound_connection_type.setter
    def outbound_connection_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outbound_connection_type", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        Customer Private Network VCN Subnet OCID. This is a required argument.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)


@pulumi.input_type
class GetIntegrationInstancesFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


