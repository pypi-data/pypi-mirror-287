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
    'GetLicenseRecordResult',
    'AwaitableGetLicenseRecordResult',
    'get_license_record',
    'get_license_record_output',
]

@pulumi.output_type
class GetLicenseRecordResult:
    """
    A collection of values returned by getLicenseRecord.
    """
    def __init__(__self__, compartment_id=None, defined_tags=None, display_name=None, expiration_date=None, freeform_tags=None, id=None, is_perpetual=None, is_unlimited=None, license_count=None, license_record_id=None, license_unit=None, product_id=None, product_license=None, product_license_id=None, state=None, support_end_date=None, system_tags=None, time_created=None, time_updated=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if defined_tags and not isinstance(defined_tags, dict):
            raise TypeError("Expected argument 'defined_tags' to be a dict")
        pulumi.set(__self__, "defined_tags", defined_tags)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if expiration_date and not isinstance(expiration_date, str):
            raise TypeError("Expected argument 'expiration_date' to be a str")
        pulumi.set(__self__, "expiration_date", expiration_date)
        if freeform_tags and not isinstance(freeform_tags, dict):
            raise TypeError("Expected argument 'freeform_tags' to be a dict")
        pulumi.set(__self__, "freeform_tags", freeform_tags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_perpetual and not isinstance(is_perpetual, bool):
            raise TypeError("Expected argument 'is_perpetual' to be a bool")
        pulumi.set(__self__, "is_perpetual", is_perpetual)
        if is_unlimited and not isinstance(is_unlimited, bool):
            raise TypeError("Expected argument 'is_unlimited' to be a bool")
        pulumi.set(__self__, "is_unlimited", is_unlimited)
        if license_count and not isinstance(license_count, int):
            raise TypeError("Expected argument 'license_count' to be a int")
        pulumi.set(__self__, "license_count", license_count)
        if license_record_id and not isinstance(license_record_id, str):
            raise TypeError("Expected argument 'license_record_id' to be a str")
        pulumi.set(__self__, "license_record_id", license_record_id)
        if license_unit and not isinstance(license_unit, str):
            raise TypeError("Expected argument 'license_unit' to be a str")
        pulumi.set(__self__, "license_unit", license_unit)
        if product_id and not isinstance(product_id, str):
            raise TypeError("Expected argument 'product_id' to be a str")
        pulumi.set(__self__, "product_id", product_id)
        if product_license and not isinstance(product_license, str):
            raise TypeError("Expected argument 'product_license' to be a str")
        pulumi.set(__self__, "product_license", product_license)
        if product_license_id and not isinstance(product_license_id, str):
            raise TypeError("Expected argument 'product_license_id' to be a str")
        pulumi.set(__self__, "product_license_id", product_license_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if support_end_date and not isinstance(support_end_date, str):
            raise TypeError("Expected argument 'support_end_date' to be a str")
        pulumi.set(__self__, "support_end_date", support_end_date)
        if system_tags and not isinstance(system_tags, dict):
            raise TypeError("Expected argument 'system_tags' to be a dict")
        pulumi.set(__self__, "system_tags", system_tags)
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
        The compartment [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) where the license record is created.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter(name="definedTags")
    def defined_tags(self) -> Mapping[str, Any]:
        """
        Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{"foo-namespace.bar-key": "value"}`
        """
        return pulumi.get(self, "defined_tags")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The license record display name. Avoid entering confidential information.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> str:
        """
        The license record end date in [RFC 3339](https://tools.ietf.org/html/rfc3339) date format. Example: `2018-09-12`
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter(name="freeformTags")
    def freeform_tags(self) -> Mapping[str, Any]:
        """
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{"bar-key": "value"}`
        """
        return pulumi.get(self, "freeform_tags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The license record [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isPerpetual")
    def is_perpetual(self) -> bool:
        """
        Specifies if the license record term is perpertual.
        """
        return pulumi.get(self, "is_perpetual")

    @property
    @pulumi.getter(name="isUnlimited")
    def is_unlimited(self) -> bool:
        """
        Specifies if the license count is unlimited.
        """
        return pulumi.get(self, "is_unlimited")

    @property
    @pulumi.getter(name="licenseCount")
    def license_count(self) -> int:
        """
        The number of license units added by the user for the given license record. Default 1
        """
        return pulumi.get(self, "license_count")

    @property
    @pulumi.getter(name="licenseRecordId")
    def license_record_id(self) -> str:
        return pulumi.get(self, "license_record_id")

    @property
    @pulumi.getter(name="licenseUnit")
    def license_unit(self) -> str:
        """
        The product license unit.
        """
        return pulumi.get(self, "license_unit")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        """
        The license record product ID.
        """
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="productLicense")
    def product_license(self) -> str:
        """
        The product license name with which the license record is associated.
        """
        return pulumi.get(self, "product_license")

    @property
    @pulumi.getter(name="productLicenseId")
    def product_license_id(self) -> str:
        """
        The product license [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) with which the license record is associated.
        """
        return pulumi.get(self, "product_license_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current license record state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="supportEndDate")
    def support_end_date(self) -> str:
        """
        The license record support end date in [RFC 3339](https://tools.ietf.org/html/rfc3339) date format. Example: `2018-09-12`
        """
        return pulumi.get(self, "support_end_date")

    @property
    @pulumi.getter(name="systemTags")
    def system_tags(self) -> Mapping[str, Any]:
        """
        Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{"orcl-cloud.free-tier-retained": "true"}`
        """
        return pulumi.get(self, "system_tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time the license record was created. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeUpdated")
    def time_updated(self) -> str:
        """
        The time the license record was updated. An [RFC 3339](https://tools.ietf.org/html/rfc3339)-formatted datetime string.
        """
        return pulumi.get(self, "time_updated")


class AwaitableGetLicenseRecordResult(GetLicenseRecordResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLicenseRecordResult(
            compartment_id=self.compartment_id,
            defined_tags=self.defined_tags,
            display_name=self.display_name,
            expiration_date=self.expiration_date,
            freeform_tags=self.freeform_tags,
            id=self.id,
            is_perpetual=self.is_perpetual,
            is_unlimited=self.is_unlimited,
            license_count=self.license_count,
            license_record_id=self.license_record_id,
            license_unit=self.license_unit,
            product_id=self.product_id,
            product_license=self.product_license,
            product_license_id=self.product_license_id,
            state=self.state,
            support_end_date=self.support_end_date,
            system_tags=self.system_tags,
            time_created=self.time_created,
            time_updated=self.time_updated)


def get_license_record(license_record_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLicenseRecordResult:
    """
    This data source provides details about a specific License Record resource in Oracle Cloud Infrastructure License Manager service.

    Retrieves license record details by the license record ID in a given compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_license_record = oci.LicenseManager.get_license_record(license_record_id=test_license_record_oci_license_manager_license_record["id"])
    ```


    :param str license_record_id: Unique license record identifier.
    """
    __args__ = dict()
    __args__['licenseRecordId'] = license_record_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:LicenseManager/getLicenseRecord:getLicenseRecord', __args__, opts=opts, typ=GetLicenseRecordResult).value

    return AwaitableGetLicenseRecordResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        defined_tags=pulumi.get(__ret__, 'defined_tags'),
        display_name=pulumi.get(__ret__, 'display_name'),
        expiration_date=pulumi.get(__ret__, 'expiration_date'),
        freeform_tags=pulumi.get(__ret__, 'freeform_tags'),
        id=pulumi.get(__ret__, 'id'),
        is_perpetual=pulumi.get(__ret__, 'is_perpetual'),
        is_unlimited=pulumi.get(__ret__, 'is_unlimited'),
        license_count=pulumi.get(__ret__, 'license_count'),
        license_record_id=pulumi.get(__ret__, 'license_record_id'),
        license_unit=pulumi.get(__ret__, 'license_unit'),
        product_id=pulumi.get(__ret__, 'product_id'),
        product_license=pulumi.get(__ret__, 'product_license'),
        product_license_id=pulumi.get(__ret__, 'product_license_id'),
        state=pulumi.get(__ret__, 'state'),
        support_end_date=pulumi.get(__ret__, 'support_end_date'),
        system_tags=pulumi.get(__ret__, 'system_tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_updated=pulumi.get(__ret__, 'time_updated'))


@_utilities.lift_output_func(get_license_record)
def get_license_record_output(license_record_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLicenseRecordResult]:
    """
    This data source provides details about a specific License Record resource in Oracle Cloud Infrastructure License Manager service.

    Retrieves license record details by the license record ID in a given compartment.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_license_record = oci.LicenseManager.get_license_record(license_record_id=test_license_record_oci_license_manager_license_record["id"])
    ```


    :param str license_record_id: Unique license record identifier.
    """
    ...
