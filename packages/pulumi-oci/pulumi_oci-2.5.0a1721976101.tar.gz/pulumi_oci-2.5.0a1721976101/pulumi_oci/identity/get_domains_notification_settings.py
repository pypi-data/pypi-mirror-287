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
    'GetDomainsNotificationSettingsResult',
    'AwaitableGetDomainsNotificationSettingsResult',
    'get_domains_notification_settings',
    'get_domains_notification_settings_output',
]

@pulumi.output_type
class GetDomainsNotificationSettingsResult:
    """
    A collection of values returned by getDomainsNotificationSettings.
    """
    def __init__(__self__, attribute_sets=None, attributes=None, authorization=None, compartment_id=None, id=None, idcs_endpoint=None, items_per_page=None, notification_settings=None, resource_type_schema_version=None, schemas=None, start_index=None, total_results=None):
        if attribute_sets and not isinstance(attribute_sets, list):
            raise TypeError("Expected argument 'attribute_sets' to be a list")
        pulumi.set(__self__, "attribute_sets", attribute_sets)
        if attributes and not isinstance(attributes, str):
            raise TypeError("Expected argument 'attributes' to be a str")
        pulumi.set(__self__, "attributes", attributes)
        if authorization and not isinstance(authorization, str):
            raise TypeError("Expected argument 'authorization' to be a str")
        pulumi.set(__self__, "authorization", authorization)
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idcs_endpoint and not isinstance(idcs_endpoint, str):
            raise TypeError("Expected argument 'idcs_endpoint' to be a str")
        pulumi.set(__self__, "idcs_endpoint", idcs_endpoint)
        if items_per_page and not isinstance(items_per_page, int):
            raise TypeError("Expected argument 'items_per_page' to be a int")
        pulumi.set(__self__, "items_per_page", items_per_page)
        if notification_settings and not isinstance(notification_settings, list):
            raise TypeError("Expected argument 'notification_settings' to be a list")
        pulumi.set(__self__, "notification_settings", notification_settings)
        if resource_type_schema_version and not isinstance(resource_type_schema_version, str):
            raise TypeError("Expected argument 'resource_type_schema_version' to be a str")
        pulumi.set(__self__, "resource_type_schema_version", resource_type_schema_version)
        if schemas and not isinstance(schemas, list):
            raise TypeError("Expected argument 'schemas' to be a list")
        pulumi.set(__self__, "schemas", schemas)
        if start_index and not isinstance(start_index, int):
            raise TypeError("Expected argument 'start_index' to be a int")
        pulumi.set(__self__, "start_index", start_index)
        if total_results and not isinstance(total_results, int):
            raise TypeError("Expected argument 'total_results' to be a int")
        pulumi.set(__self__, "total_results", total_results)

    @property
    @pulumi.getter(name="attributeSets")
    def attribute_sets(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "attribute_sets")

    @property
    @pulumi.getter
    def attributes(self) -> Optional[str]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def authorization(self) -> Optional[str]:
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[str]:
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idcsEndpoint")
    def idcs_endpoint(self) -> str:
        return pulumi.get(self, "idcs_endpoint")

    @property
    @pulumi.getter(name="itemsPerPage")
    def items_per_page(self) -> int:
        return pulumi.get(self, "items_per_page")

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> Sequence['outputs.GetDomainsNotificationSettingsNotificationSettingResult']:
        """
        The list of notification_settings.
        """
        return pulumi.get(self, "notification_settings")

    @property
    @pulumi.getter(name="resourceTypeSchemaVersion")
    def resource_type_schema_version(self) -> Optional[str]:
        return pulumi.get(self, "resource_type_schema_version")

    @property
    @pulumi.getter
    def schemas(self) -> Sequence[str]:
        """
        REQUIRED. The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. This specification defines URIs for User, Group, and a standard \\"enterprise\\" extension. All representations of SCIM schema MUST include a non-zero value array with value(s) of the URIs supported by that representation. Duplicate values MUST NOT be included. Value order is not specified and MUST not impact behavior.
        """
        return pulumi.get(self, "schemas")

    @property
    @pulumi.getter(name="startIndex")
    def start_index(self) -> int:
        return pulumi.get(self, "start_index")

    @property
    @pulumi.getter(name="totalResults")
    def total_results(self) -> int:
        return pulumi.get(self, "total_results")


class AwaitableGetDomainsNotificationSettingsResult(GetDomainsNotificationSettingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainsNotificationSettingsResult(
            attribute_sets=self.attribute_sets,
            attributes=self.attributes,
            authorization=self.authorization,
            compartment_id=self.compartment_id,
            id=self.id,
            idcs_endpoint=self.idcs_endpoint,
            items_per_page=self.items_per_page,
            notification_settings=self.notification_settings,
            resource_type_schema_version=self.resource_type_schema_version,
            schemas=self.schemas,
            start_index=self.start_index,
            total_results=self.total_results)


def get_domains_notification_settings(attribute_sets: Optional[Sequence[str]] = None,
                                      attributes: Optional[str] = None,
                                      authorization: Optional[str] = None,
                                      compartment_id: Optional[str] = None,
                                      idcs_endpoint: Optional[str] = None,
                                      resource_type_schema_version: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainsNotificationSettingsResult:
    """
    This data source provides the list of Notification Settings in Oracle Cloud Infrastructure Identity Domains service.

    Search Notification Settings

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_notification_settings = oci.Identity.get_domains_notification_settings(idcs_endpoint=test_domain["url"],
        attribute_sets=["all"],
        attributes="",
        authorization=notification_setting_authorization,
        resource_type_schema_version=notification_setting_resource_type_schema_version)
    ```


    :param Sequence[str] attribute_sets: A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If 'attributes' query parameter is also available, union of the two is fetched. Valid values - all, always, never, request, default. Values are case-insensitive.
    :param str attributes: A comma-delimited string that specifies the names of resource attributes that should be returned in the response. By default, a response that contains resource attributes contains only attributes that are defined in the schema for that resource type as returned=always or returned=default. An attribute that is defined as returned=request is returned in a response only if the request specifies its name in the value of this query parameter. If a request specifies this query parameter, the response contains the attributes that this query parameter specifies, as well as any attribute that is defined as returned=always.
    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    """
    __args__ = dict()
    __args__['attributeSets'] = attribute_sets
    __args__['attributes'] = attributes
    __args__['authorization'] = authorization
    __args__['compartmentId'] = compartment_id
    __args__['idcsEndpoint'] = idcs_endpoint
    __args__['resourceTypeSchemaVersion'] = resource_type_schema_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Identity/getDomainsNotificationSettings:getDomainsNotificationSettings', __args__, opts=opts, typ=GetDomainsNotificationSettingsResult).value

    return AwaitableGetDomainsNotificationSettingsResult(
        attribute_sets=pulumi.get(__ret__, 'attribute_sets'),
        attributes=pulumi.get(__ret__, 'attributes'),
        authorization=pulumi.get(__ret__, 'authorization'),
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        id=pulumi.get(__ret__, 'id'),
        idcs_endpoint=pulumi.get(__ret__, 'idcs_endpoint'),
        items_per_page=pulumi.get(__ret__, 'items_per_page'),
        notification_settings=pulumi.get(__ret__, 'notification_settings'),
        resource_type_schema_version=pulumi.get(__ret__, 'resource_type_schema_version'),
        schemas=pulumi.get(__ret__, 'schemas'),
        start_index=pulumi.get(__ret__, 'start_index'),
        total_results=pulumi.get(__ret__, 'total_results'))


@_utilities.lift_output_func(get_domains_notification_settings)
def get_domains_notification_settings_output(attribute_sets: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                             attributes: Optional[pulumi.Input[Optional[str]]] = None,
                                             authorization: Optional[pulumi.Input[Optional[str]]] = None,
                                             compartment_id: Optional[pulumi.Input[Optional[str]]] = None,
                                             idcs_endpoint: Optional[pulumi.Input[str]] = None,
                                             resource_type_schema_version: Optional[pulumi.Input[Optional[str]]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainsNotificationSettingsResult]:
    """
    This data source provides the list of Notification Settings in Oracle Cloud Infrastructure Identity Domains service.

    Search Notification Settings

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_notification_settings = oci.Identity.get_domains_notification_settings(idcs_endpoint=test_domain["url"],
        attribute_sets=["all"],
        attributes="",
        authorization=notification_setting_authorization,
        resource_type_schema_version=notification_setting_resource_type_schema_version)
    ```


    :param Sequence[str] attribute_sets: A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If 'attributes' query parameter is also available, union of the two is fetched. Valid values - all, always, never, request, default. Values are case-insensitive.
    :param str attributes: A comma-delimited string that specifies the names of resource attributes that should be returned in the response. By default, a response that contains resource attributes contains only attributes that are defined in the schema for that resource type as returned=always or returned=default. An attribute that is defined as returned=request is returned in a response only if the request specifies its name in the value of this query parameter. If a request specifies this query parameter, the response contains the attributes that this query parameter specifies, as well as any attribute that is defined as returned=always.
    :param str authorization: The Authorization field value consists of credentials containing the authentication information of the user agent for the realm of the resource being requested.
    :param str idcs_endpoint: The basic endpoint for the identity domain
    :param str resource_type_schema_version: An endpoint-specific schema version number to use in the Request. Allowed version values are Earliest Version or Latest Version as specified in each REST API endpoint description, or any sequential number inbetween. All schema attributes/body parameters are a part of version 1. After version 1, any attributes added or deprecated will be tagged with the version that they were added to or deprecated in. If no version is provided, the latest schema version is returned.
    """
    ...
