# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserCapabilitiesManagementArgs', 'UserCapabilitiesManagement']

@pulumi.input_type
class UserCapabilitiesManagementArgs:
    def __init__(__self__, *,
                 user_id: pulumi.Input[str],
                 can_use_api_keys: Optional[pulumi.Input[bool]] = None,
                 can_use_auth_tokens: Optional[pulumi.Input[bool]] = None,
                 can_use_console_password: Optional[pulumi.Input[bool]] = None,
                 can_use_customer_secret_keys: Optional[pulumi.Input[bool]] = None,
                 can_use_smtp_credentials: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a UserCapabilitiesManagement resource.
        :param pulumi.Input[str] user_id: The OCID of the user.
        :param pulumi.Input[bool] can_use_api_keys: (Updatable) Indicates if the user can use API keys.
        :param pulumi.Input[bool] can_use_auth_tokens: (Updatable) Indicates if the user can use SWIFT passwords / auth tokens.
        :param pulumi.Input[bool] can_use_console_password: (Updatable) Indicates if the user can log in to the console.
        :param pulumi.Input[bool] can_use_customer_secret_keys: (Updatable) Indicates if the user can use SigV4 symmetric keys.
        :param pulumi.Input[bool] can_use_smtp_credentials: (Updatable) Indicates if the user can use SMTP passwords.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        pulumi.set(__self__, "user_id", user_id)
        if can_use_api_keys is not None:
            pulumi.set(__self__, "can_use_api_keys", can_use_api_keys)
        if can_use_auth_tokens is not None:
            pulumi.set(__self__, "can_use_auth_tokens", can_use_auth_tokens)
        if can_use_console_password is not None:
            pulumi.set(__self__, "can_use_console_password", can_use_console_password)
        if can_use_customer_secret_keys is not None:
            pulumi.set(__self__, "can_use_customer_secret_keys", can_use_customer_secret_keys)
        if can_use_smtp_credentials is not None:
            pulumi.set(__self__, "can_use_smtp_credentials", can_use_smtp_credentials)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        The OCID of the user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="canUseApiKeys")
    def can_use_api_keys(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can use API keys.
        """
        return pulumi.get(self, "can_use_api_keys")

    @can_use_api_keys.setter
    def can_use_api_keys(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_api_keys", value)

    @property
    @pulumi.getter(name="canUseAuthTokens")
    def can_use_auth_tokens(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can use SWIFT passwords / auth tokens.
        """
        return pulumi.get(self, "can_use_auth_tokens")

    @can_use_auth_tokens.setter
    def can_use_auth_tokens(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_auth_tokens", value)

    @property
    @pulumi.getter(name="canUseConsolePassword")
    def can_use_console_password(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can log in to the console.
        """
        return pulumi.get(self, "can_use_console_password")

    @can_use_console_password.setter
    def can_use_console_password(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_console_password", value)

    @property
    @pulumi.getter(name="canUseCustomerSecretKeys")
    def can_use_customer_secret_keys(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can use SigV4 symmetric keys.
        """
        return pulumi.get(self, "can_use_customer_secret_keys")

    @can_use_customer_secret_keys.setter
    def can_use_customer_secret_keys(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_customer_secret_keys", value)

    @property
    @pulumi.getter(name="canUseSmtpCredentials")
    def can_use_smtp_credentials(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can use SMTP passwords.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "can_use_smtp_credentials")

    @can_use_smtp_credentials.setter
    def can_use_smtp_credentials(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_smtp_credentials", value)


@pulumi.input_type
class _UserCapabilitiesManagementState:
    def __init__(__self__, *,
                 can_use_api_keys: Optional[pulumi.Input[bool]] = None,
                 can_use_auth_tokens: Optional[pulumi.Input[bool]] = None,
                 can_use_console_password: Optional[pulumi.Input[bool]] = None,
                 can_use_customer_secret_keys: Optional[pulumi.Input[bool]] = None,
                 can_use_smtp_credentials: Optional[pulumi.Input[bool]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserCapabilitiesManagement resources.
        :param pulumi.Input[bool] can_use_api_keys: (Updatable) Indicates if the user can use API keys.
        :param pulumi.Input[bool] can_use_auth_tokens: (Updatable) Indicates if the user can use SWIFT passwords / auth tokens.
        :param pulumi.Input[bool] can_use_console_password: (Updatable) Indicates if the user can log in to the console.
        :param pulumi.Input[bool] can_use_customer_secret_keys: (Updatable) Indicates if the user can use SigV4 symmetric keys.
        :param pulumi.Input[bool] can_use_smtp_credentials: (Updatable) Indicates if the user can use SMTP passwords.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] user_id: The OCID of the user.
        """
        if can_use_api_keys is not None:
            pulumi.set(__self__, "can_use_api_keys", can_use_api_keys)
        if can_use_auth_tokens is not None:
            pulumi.set(__self__, "can_use_auth_tokens", can_use_auth_tokens)
        if can_use_console_password is not None:
            pulumi.set(__self__, "can_use_console_password", can_use_console_password)
        if can_use_customer_secret_keys is not None:
            pulumi.set(__self__, "can_use_customer_secret_keys", can_use_customer_secret_keys)
        if can_use_smtp_credentials is not None:
            pulumi.set(__self__, "can_use_smtp_credentials", can_use_smtp_credentials)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="canUseApiKeys")
    def can_use_api_keys(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can use API keys.
        """
        return pulumi.get(self, "can_use_api_keys")

    @can_use_api_keys.setter
    def can_use_api_keys(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_api_keys", value)

    @property
    @pulumi.getter(name="canUseAuthTokens")
    def can_use_auth_tokens(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can use SWIFT passwords / auth tokens.
        """
        return pulumi.get(self, "can_use_auth_tokens")

    @can_use_auth_tokens.setter
    def can_use_auth_tokens(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_auth_tokens", value)

    @property
    @pulumi.getter(name="canUseConsolePassword")
    def can_use_console_password(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can log in to the console.
        """
        return pulumi.get(self, "can_use_console_password")

    @can_use_console_password.setter
    def can_use_console_password(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_console_password", value)

    @property
    @pulumi.getter(name="canUseCustomerSecretKeys")
    def can_use_customer_secret_keys(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can use SigV4 symmetric keys.
        """
        return pulumi.get(self, "can_use_customer_secret_keys")

    @can_use_customer_secret_keys.setter
    def can_use_customer_secret_keys(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_customer_secret_keys", value)

    @property
    @pulumi.getter(name="canUseSmtpCredentials")
    def can_use_smtp_credentials(self) -> Optional[pulumi.Input[bool]]:
        """
        (Updatable) Indicates if the user can use SMTP passwords.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "can_use_smtp_credentials")

    @can_use_smtp_credentials.setter
    def can_use_smtp_credentials(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "can_use_smtp_credentials", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OCID of the user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class UserCapabilitiesManagement(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 can_use_api_keys: Optional[pulumi.Input[bool]] = None,
                 can_use_auth_tokens: Optional[pulumi.Input[bool]] = None,
                 can_use_console_password: Optional[pulumi.Input[bool]] = None,
                 can_use_customer_secret_keys: Optional[pulumi.Input[bool]] = None,
                 can_use_smtp_credentials: Optional[pulumi.Input[bool]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the User Capabilities Management resource in Oracle Cloud Infrastructure Identity service.

        Manages the capabilities of the specified user.

        **Important:** Deleting the User Capabilities Management leaves the User resource in its existing state (rather than returning to its defaults)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_user_capabilities_management = oci.identity.UserCapabilitiesManagement("test_user_capabilities_management",
            user_id=user1["id"],
            can_use_api_keys=True,
            can_use_auth_tokens=True,
            can_use_console_password=False,
            can_use_customer_secret_keys=True,
            can_use_smtp_credentials=True)
        ```

        ## Import

        Users can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Identity/userCapabilitiesManagement:UserCapabilitiesManagement test_user_capabilities_management "capabilities/{userId}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] can_use_api_keys: (Updatable) Indicates if the user can use API keys.
        :param pulumi.Input[bool] can_use_auth_tokens: (Updatable) Indicates if the user can use SWIFT passwords / auth tokens.
        :param pulumi.Input[bool] can_use_console_password: (Updatable) Indicates if the user can log in to the console.
        :param pulumi.Input[bool] can_use_customer_secret_keys: (Updatable) Indicates if the user can use SigV4 symmetric keys.
        :param pulumi.Input[bool] can_use_smtp_credentials: (Updatable) Indicates if the user can use SMTP passwords.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] user_id: The OCID of the user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserCapabilitiesManagementArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the User Capabilities Management resource in Oracle Cloud Infrastructure Identity service.

        Manages the capabilities of the specified user.

        **Important:** Deleting the User Capabilities Management leaves the User resource in its existing state (rather than returning to its defaults)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_user_capabilities_management = oci.identity.UserCapabilitiesManagement("test_user_capabilities_management",
            user_id=user1["id"],
            can_use_api_keys=True,
            can_use_auth_tokens=True,
            can_use_console_password=False,
            can_use_customer_secret_keys=True,
            can_use_smtp_credentials=True)
        ```

        ## Import

        Users can be imported using the `id`, e.g.

        ```sh
        $ pulumi import oci:Identity/userCapabilitiesManagement:UserCapabilitiesManagement test_user_capabilities_management "capabilities/{userId}"
        ```

        :param str resource_name: The name of the resource.
        :param UserCapabilitiesManagementArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserCapabilitiesManagementArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 can_use_api_keys: Optional[pulumi.Input[bool]] = None,
                 can_use_auth_tokens: Optional[pulumi.Input[bool]] = None,
                 can_use_console_password: Optional[pulumi.Input[bool]] = None,
                 can_use_customer_secret_keys: Optional[pulumi.Input[bool]] = None,
                 can_use_smtp_credentials: Optional[pulumi.Input[bool]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserCapabilitiesManagementArgs.__new__(UserCapabilitiesManagementArgs)

            __props__.__dict__["can_use_api_keys"] = can_use_api_keys
            __props__.__dict__["can_use_auth_tokens"] = can_use_auth_tokens
            __props__.__dict__["can_use_console_password"] = can_use_console_password
            __props__.__dict__["can_use_customer_secret_keys"] = can_use_customer_secret_keys
            __props__.__dict__["can_use_smtp_credentials"] = can_use_smtp_credentials
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
        super(UserCapabilitiesManagement, __self__).__init__(
            'oci:Identity/userCapabilitiesManagement:UserCapabilitiesManagement',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            can_use_api_keys: Optional[pulumi.Input[bool]] = None,
            can_use_auth_tokens: Optional[pulumi.Input[bool]] = None,
            can_use_console_password: Optional[pulumi.Input[bool]] = None,
            can_use_customer_secret_keys: Optional[pulumi.Input[bool]] = None,
            can_use_smtp_credentials: Optional[pulumi.Input[bool]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'UserCapabilitiesManagement':
        """
        Get an existing UserCapabilitiesManagement resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] can_use_api_keys: (Updatable) Indicates if the user can use API keys.
        :param pulumi.Input[bool] can_use_auth_tokens: (Updatable) Indicates if the user can use SWIFT passwords / auth tokens.
        :param pulumi.Input[bool] can_use_console_password: (Updatable) Indicates if the user can log in to the console.
        :param pulumi.Input[bool] can_use_customer_secret_keys: (Updatable) Indicates if the user can use SigV4 symmetric keys.
        :param pulumi.Input[bool] can_use_smtp_credentials: (Updatable) Indicates if the user can use SMTP passwords.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[str] user_id: The OCID of the user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserCapabilitiesManagementState.__new__(_UserCapabilitiesManagementState)

        __props__.__dict__["can_use_api_keys"] = can_use_api_keys
        __props__.__dict__["can_use_auth_tokens"] = can_use_auth_tokens
        __props__.__dict__["can_use_console_password"] = can_use_console_password
        __props__.__dict__["can_use_customer_secret_keys"] = can_use_customer_secret_keys
        __props__.__dict__["can_use_smtp_credentials"] = can_use_smtp_credentials
        __props__.__dict__["user_id"] = user_id
        return UserCapabilitiesManagement(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="canUseApiKeys")
    def can_use_api_keys(self) -> pulumi.Output[bool]:
        """
        (Updatable) Indicates if the user can use API keys.
        """
        return pulumi.get(self, "can_use_api_keys")

    @property
    @pulumi.getter(name="canUseAuthTokens")
    def can_use_auth_tokens(self) -> pulumi.Output[bool]:
        """
        (Updatable) Indicates if the user can use SWIFT passwords / auth tokens.
        """
        return pulumi.get(self, "can_use_auth_tokens")

    @property
    @pulumi.getter(name="canUseConsolePassword")
    def can_use_console_password(self) -> pulumi.Output[bool]:
        """
        (Updatable) Indicates if the user can log in to the console.
        """
        return pulumi.get(self, "can_use_console_password")

    @property
    @pulumi.getter(name="canUseCustomerSecretKeys")
    def can_use_customer_secret_keys(self) -> pulumi.Output[bool]:
        """
        (Updatable) Indicates if the user can use SigV4 symmetric keys.
        """
        return pulumi.get(self, "can_use_customer_secret_keys")

    @property
    @pulumi.getter(name="canUseSmtpCredentials")
    def can_use_smtp_credentials(self) -> pulumi.Output[bool]:
        """
        (Updatable) Indicates if the user can use SMTP passwords.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "can_use_smtp_credentials")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The OCID of the user.
        """
        return pulumi.get(self, "user_id")

