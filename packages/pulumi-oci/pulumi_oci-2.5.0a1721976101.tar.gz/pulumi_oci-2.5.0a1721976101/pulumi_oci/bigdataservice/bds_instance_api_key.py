# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BdsInstanceApiKeyArgs', 'BdsInstanceApiKey']

@pulumi.input_type
class BdsInstanceApiKeyArgs:
    def __init__(__self__, *,
                 bds_instance_id: pulumi.Input[str],
                 key_alias: pulumi.Input[str],
                 passphrase: pulumi.Input[str],
                 user_id: pulumi.Input[str],
                 default_region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BdsInstanceApiKey resource.
        :param pulumi.Input[str] bds_instance_id: The OCID of the cluster.
        :param pulumi.Input[str] key_alias: User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster. Only ASCII alphanumeric characters with no spaces allowed.
        :param pulumi.Input[str] passphrase: Base64 passphrase used to secure the private key which will be created on user behalf.
        :param pulumi.Input[str] user_id: The OCID of the user for whom this new generated API key pair will be created.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] default_region: The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/ for additional information.
        """
        pulumi.set(__self__, "bds_instance_id", bds_instance_id)
        pulumi.set(__self__, "key_alias", key_alias)
        pulumi.set(__self__, "passphrase", passphrase)
        pulumi.set(__self__, "user_id", user_id)
        if default_region is not None:
            pulumi.set(__self__, "default_region", default_region)

    @property
    @pulumi.getter(name="bdsInstanceId")
    def bds_instance_id(self) -> pulumi.Input[str]:
        """
        The OCID of the cluster.
        """
        return pulumi.get(self, "bds_instance_id")

    @bds_instance_id.setter
    def bds_instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "bds_instance_id", value)

    @property
    @pulumi.getter(name="keyAlias")
    def key_alias(self) -> pulumi.Input[str]:
        """
        User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster. Only ASCII alphanumeric characters with no spaces allowed.
        """
        return pulumi.get(self, "key_alias")

    @key_alias.setter
    def key_alias(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_alias", value)

    @property
    @pulumi.getter
    def passphrase(self) -> pulumi.Input[str]:
        """
        Base64 passphrase used to secure the private key which will be created on user behalf.
        """
        return pulumi.get(self, "passphrase")

    @passphrase.setter
    def passphrase(self, value: pulumi.Input[str]):
        pulumi.set(self, "passphrase", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        The OCID of the user for whom this new generated API key pair will be created.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="defaultRegion")
    def default_region(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/ for additional information.
        """
        return pulumi.get(self, "default_region")

    @default_region.setter
    def default_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_region", value)


@pulumi.input_type
class _BdsInstanceApiKeyState:
    def __init__(__self__, *,
                 bds_instance_id: Optional[pulumi.Input[str]] = None,
                 default_region: Optional[pulumi.Input[str]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 key_alias: Optional[pulumi.Input[str]] = None,
                 passphrase: Optional[pulumi.Input[str]] = None,
                 pemfilepath: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 time_created: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BdsInstanceApiKey resources.
        :param pulumi.Input[str] bds_instance_id: The OCID of the cluster.
        :param pulumi.Input[str] default_region: The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/ for additional information.
        :param pulumi.Input[str] fingerprint: The fingerprint that corresponds to the public API key requested.
        :param pulumi.Input[str] key_alias: User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster. Only ASCII alphanumeric characters with no spaces allowed.
        :param pulumi.Input[str] passphrase: Base64 passphrase used to secure the private key which will be created on user behalf.
        :param pulumi.Input[str] pemfilepath: The full path and file name of the private key used for authentication. This location will be automatically selected on the BDS local file system.
        :param pulumi.Input[str] state: The current status of the API key.
        :param pulumi.Input[str] tenant_id: The OCID of your tenancy.
        :param pulumi.Input[str] time_created: The time the API key was created, shown as an RFC 3339 formatted datetime string.
        :param pulumi.Input[str] user_id: The OCID of the user for whom this new generated API key pair will be created.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if bds_instance_id is not None:
            pulumi.set(__self__, "bds_instance_id", bds_instance_id)
        if default_region is not None:
            pulumi.set(__self__, "default_region", default_region)
        if fingerprint is not None:
            pulumi.set(__self__, "fingerprint", fingerprint)
        if key_alias is not None:
            pulumi.set(__self__, "key_alias", key_alias)
        if passphrase is not None:
            pulumi.set(__self__, "passphrase", passphrase)
        if pemfilepath is not None:
            pulumi.set(__self__, "pemfilepath", pemfilepath)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if time_created is not None:
            pulumi.set(__self__, "time_created", time_created)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="bdsInstanceId")
    def bds_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the cluster.
        """
        return pulumi.get(self, "bds_instance_id")

    @bds_instance_id.setter
    def bds_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bds_instance_id", value)

    @property
    @pulumi.getter(name="defaultRegion")
    def default_region(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/ for additional information.
        """
        return pulumi.get(self, "default_region")

    @default_region.setter
    def default_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_region", value)

    @property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[str]]:
        """
        The fingerprint that corresponds to the public API key requested.
        """
        return pulumi.get(self, "fingerprint")

    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fingerprint", value)

    @property
    @pulumi.getter(name="keyAlias")
    def key_alias(self) -> Optional[pulumi.Input[str]]:
        """
        User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster. Only ASCII alphanumeric characters with no spaces allowed.
        """
        return pulumi.get(self, "key_alias")

    @key_alias.setter
    def key_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_alias", value)

    @property
    @pulumi.getter
    def passphrase(self) -> Optional[pulumi.Input[str]]:
        """
        Base64 passphrase used to secure the private key which will be created on user behalf.
        """
        return pulumi.get(self, "passphrase")

    @passphrase.setter
    def passphrase(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "passphrase", value)

    @property
    @pulumi.getter
    def pemfilepath(self) -> Optional[pulumi.Input[str]]:
        """
        The full path and file name of the private key used for authentication. This location will be automatically selected on the BDS local file system.
        """
        return pulumi.get(self, "pemfilepath")

    @pemfilepath.setter
    def pemfilepath(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pemfilepath", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current status of the API key.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of your tenancy.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the API key was created, shown as an RFC 3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_created", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the user for whom this new generated API key pair will be created.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class BdsInstanceApiKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bds_instance_id: Optional[pulumi.Input[str]] = None,
                 default_region: Optional[pulumi.Input[str]] = None,
                 key_alias: Optional[pulumi.Input[str]] = None,
                 passphrase: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Bds Instance Api Key resource in Oracle Cloud Infrastructure Big Data Service service.

        Create an API key on behalf of the specified user.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_bds_instance_api_key = oci.big_data_service.BdsInstanceApiKey("test_bds_instance_api_key",
            bds_instance_id=test_bds_instance["id"],
            key_alias=bds_instance_api_key_key_alias,
            passphrase=bds_instance_api_key_passphrase,
            user_id=test_user["id"],
            default_region=bds_instance_api_key_default_region)
        ```

        ## Import

        BdsInstanceApiKeys can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:BigDataService/bdsInstanceApiKey:BdsInstanceApiKey test_bds_instance_api_key "bdsInstances/{bdsInstanceId}/apiKeys/{apiKeyId}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bds_instance_id: The OCID of the cluster.
        :param pulumi.Input[str] default_region: The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/ for additional information.
        :param pulumi.Input[str] key_alias: User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster. Only ASCII alphanumeric characters with no spaces allowed.
        :param pulumi.Input[str] passphrase: Base64 passphrase used to secure the private key which will be created on user behalf.
        :param pulumi.Input[str] user_id: The OCID of the user for whom this new generated API key pair will be created.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BdsInstanceApiKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Bds Instance Api Key resource in Oracle Cloud Infrastructure Big Data Service service.

        Create an API key on behalf of the specified user.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_bds_instance_api_key = oci.big_data_service.BdsInstanceApiKey("test_bds_instance_api_key",
            bds_instance_id=test_bds_instance["id"],
            key_alias=bds_instance_api_key_key_alias,
            passphrase=bds_instance_api_key_passphrase,
            user_id=test_user["id"],
            default_region=bds_instance_api_key_default_region)
        ```

        ## Import

        BdsInstanceApiKeys can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:BigDataService/bdsInstanceApiKey:BdsInstanceApiKey test_bds_instance_api_key "bdsInstances/{bdsInstanceId}/apiKeys/{apiKeyId}"
        ```

        :param str resource_name: The name of the resource.
        :param BdsInstanceApiKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BdsInstanceApiKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bds_instance_id: Optional[pulumi.Input[str]] = None,
                 default_region: Optional[pulumi.Input[str]] = None,
                 key_alias: Optional[pulumi.Input[str]] = None,
                 passphrase: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BdsInstanceApiKeyArgs.__new__(BdsInstanceApiKeyArgs)

            if bds_instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'bds_instance_id'")
            __props__.__dict__["bds_instance_id"] = bds_instance_id
            __props__.__dict__["default_region"] = default_region
            if key_alias is None and not opts.urn:
                raise TypeError("Missing required property 'key_alias'")
            __props__.__dict__["key_alias"] = key_alias
            if passphrase is None and not opts.urn:
                raise TypeError("Missing required property 'passphrase'")
            __props__.__dict__["passphrase"] = None if passphrase is None else pulumi.Output.secret(passphrase)
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["fingerprint"] = None
            __props__.__dict__["pemfilepath"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["time_created"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["passphrase"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(BdsInstanceApiKey, __self__).__init__(
            'oci:BigDataService/bdsInstanceApiKey:BdsInstanceApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bds_instance_id: Optional[pulumi.Input[str]] = None,
            default_region: Optional[pulumi.Input[str]] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            key_alias: Optional[pulumi.Input[str]] = None,
            passphrase: Optional[pulumi.Input[str]] = None,
            pemfilepath: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            time_created: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'BdsInstanceApiKey':
        """
        Get an existing BdsInstanceApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bds_instance_id: The OCID of the cluster.
        :param pulumi.Input[str] default_region: The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/ for additional information.
        :param pulumi.Input[str] fingerprint: The fingerprint that corresponds to the public API key requested.
        :param pulumi.Input[str] key_alias: User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster. Only ASCII alphanumeric characters with no spaces allowed.
        :param pulumi.Input[str] passphrase: Base64 passphrase used to secure the private key which will be created on user behalf.
        :param pulumi.Input[str] pemfilepath: The full path and file name of the private key used for authentication. This location will be automatically selected on the BDS local file system.
        :param pulumi.Input[str] state: The current status of the API key.
        :param pulumi.Input[str] tenant_id: The OCID of your tenancy.
        :param pulumi.Input[str] time_created: The time the API key was created, shown as an RFC 3339 formatted datetime string.
        :param pulumi.Input[str] user_id: The OCID of the user for whom this new generated API key pair will be created.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BdsInstanceApiKeyState.__new__(_BdsInstanceApiKeyState)

        __props__.__dict__["bds_instance_id"] = bds_instance_id
        __props__.__dict__["default_region"] = default_region
        __props__.__dict__["fingerprint"] = fingerprint
        __props__.__dict__["key_alias"] = key_alias
        __props__.__dict__["passphrase"] = passphrase
        __props__.__dict__["pemfilepath"] = pemfilepath
        __props__.__dict__["state"] = state
        __props__.__dict__["tenant_id"] = tenant_id
        __props__.__dict__["time_created"] = time_created
        __props__.__dict__["user_id"] = user_id
        return BdsInstanceApiKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bdsInstanceId")
    def bds_instance_id(self) -> pulumi.Output[str]:
        """
        The OCID of the cluster.
        """
        return pulumi.get(self, "bds_instance_id")

    @property
    @pulumi.getter(name="defaultRegion")
    def default_region(self) -> pulumi.Output[str]:
        """
        The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/ for additional information.
        """
        return pulumi.get(self, "default_region")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        The fingerprint that corresponds to the public API key requested.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="keyAlias")
    def key_alias(self) -> pulumi.Output[str]:
        """
        User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster. Only ASCII alphanumeric characters with no spaces allowed.
        """
        return pulumi.get(self, "key_alias")

    @property
    @pulumi.getter
    def passphrase(self) -> pulumi.Output[str]:
        """
        Base64 passphrase used to secure the private key which will be created on user behalf.
        """
        return pulumi.get(self, "passphrase")

    @property
    @pulumi.getter
    def pemfilepath(self) -> pulumi.Output[str]:
        """
        The full path and file name of the private key used for authentication. This location will be automatically selected on the BDS local file system.
        """
        return pulumi.get(self, "pemfilepath")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current status of the API key.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The OCID of your tenancy.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        The time the API key was created, shown as an RFC 3339 formatted datetime string.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The OCID of the user for whom this new generated API key pair will be created.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "user_id")

