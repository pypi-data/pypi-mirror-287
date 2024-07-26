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
    'GetSendersResult',
    'AwaitableGetSendersResult',
    'get_senders',
    'get_senders_output',
]

@pulumi.output_type
class GetSendersResult:
    """
    A collection of values returned by getSenders.
    """
    def __init__(__self__, compartment_id=None, domain=None, email_address=None, filters=None, id=None, senders=None, state=None):
        if compartment_id and not isinstance(compartment_id, str):
            raise TypeError("Expected argument 'compartment_id' to be a str")
        pulumi.set(__self__, "compartment_id", compartment_id)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if email_address and not isinstance(email_address, str):
            raise TypeError("Expected argument 'email_address' to be a str")
        pulumi.set(__self__, "email_address", email_address)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if senders and not isinstance(senders, list):
            raise TypeError("Expected argument 'senders' to be a list")
        pulumi.set(__self__, "senders", senders)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> str:
        """
        The OCID for the compartment.
        """
        return pulumi.get(self, "compartment_id")

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[str]:
        """
        The email address of the sender.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetSendersFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def senders(self) -> Sequence['outputs.GetSendersSenderResult']:
        """
        The list of senders.
        """
        return pulumi.get(self, "senders")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The current status of the approved sender.
        """
        return pulumi.get(self, "state")


class AwaitableGetSendersResult(GetSendersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSendersResult(
            compartment_id=self.compartment_id,
            domain=self.domain,
            email_address=self.email_address,
            filters=self.filters,
            id=self.id,
            senders=self.senders,
            state=self.state)


def get_senders(compartment_id: Optional[str] = None,
                domain: Optional[str] = None,
                email_address: Optional[str] = None,
                filters: Optional[Sequence[pulumi.InputType['GetSendersFilterArgs']]] = None,
                state: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSendersResult:
    """
    This data source provides the list of Senders in Oracle Cloud Infrastructure Email service.

    Gets a collection of approved sender email addresses and sender IDs.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_senders = oci.Email.get_senders(compartment_id=compartment_id,
        domain=sender_domain,
        email_address=sender_email_address,
        state=sender_state)
    ```


    :param str compartment_id: The OCID for the compartment.
    :param str domain: A filter to only return resources that match the given domain exactly.
    :param str email_address: The email address of the approved sender.
    :param str state: The current state of a sender.
    """
    __args__ = dict()
    __args__['compartmentId'] = compartment_id
    __args__['domain'] = domain
    __args__['emailAddress'] = email_address
    __args__['filters'] = filters
    __args__['state'] = state
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('oci:Email/getSenders:getSenders', __args__, opts=opts, typ=GetSendersResult).value

    return AwaitableGetSendersResult(
        compartment_id=pulumi.get(__ret__, 'compartment_id'),
        domain=pulumi.get(__ret__, 'domain'),
        email_address=pulumi.get(__ret__, 'email_address'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        senders=pulumi.get(__ret__, 'senders'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_senders)
def get_senders_output(compartment_id: Optional[pulumi.Input[str]] = None,
                       domain: Optional[pulumi.Input[Optional[str]]] = None,
                       email_address: Optional[pulumi.Input[Optional[str]]] = None,
                       filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetSendersFilterArgs']]]]] = None,
                       state: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSendersResult]:
    """
    This data source provides the list of Senders in Oracle Cloud Infrastructure Email service.

    Gets a collection of approved sender email addresses and sender IDs.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_oci as oci

    test_senders = oci.Email.get_senders(compartment_id=compartment_id,
        domain=sender_domain,
        email_address=sender_email_address,
        state=sender_state)
    ```


    :param str compartment_id: The OCID for the compartment.
    :param str domain: A filter to only return resources that match the given domain exactly.
    :param str email_address: The email address of the approved sender.
    :param str state: The current state of a sender.
    """
    ...
