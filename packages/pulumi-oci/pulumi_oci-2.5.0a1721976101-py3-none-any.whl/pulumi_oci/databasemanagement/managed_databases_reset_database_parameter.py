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

__all__ = ['ManagedDatabasesResetDatabaseParameterArgs', 'ManagedDatabasesResetDatabaseParameter']

@pulumi.input_type
class ManagedDatabasesResetDatabaseParameterArgs:
    def __init__(__self__, *,
                 managed_database_id: pulumi.Input[str],
                 parameters: pulumi.Input[Sequence[pulumi.Input[str]]],
                 scope: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterCredentialsArgs']] = None,
                 database_credential: Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']] = None):
        """
        The set of arguments for constructing a ManagedDatabasesResetDatabaseParameter resource.
        :param pulumi.Input[str] managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] parameters: A list of database parameter names.
        :param pulumi.Input[str] scope: The clause used to specify when the parameter change takes effect.
               
               Use `MEMORY` to make the change in memory and ensure that it takes effect immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input['ManagedDatabasesResetDatabaseParameterCredentialsArgs'] credentials: The database credentials used to perform management activity. Provide one of the following attribute set. (userName, password, role) OR (userName, secretId, role) OR (namedCredentialId)
        :param pulumi.Input['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs'] database_credential: The credential to connect to the database to perform tablespace administration tasks.
        """
        pulumi.set(__self__, "managed_database_id", managed_database_id)
        pulumi.set(__self__, "parameters", parameters)
        pulumi.set(__self__, "scope", scope)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if database_credential is not None:
            pulumi.set(__self__, "database_credential", database_credential)

    @property
    @pulumi.getter(name="managedDatabaseId")
    def managed_database_id(self) -> pulumi.Input[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
        """
        return pulumi.get(self, "managed_database_id")

    @managed_database_id.setter
    def managed_database_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_database_id", value)

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of database parameter names.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The clause used to specify when the parameter change takes effect.

        Use `MEMORY` to make the change in memory and ensure that it takes effect immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterCredentialsArgs']]:
        """
        The database credentials used to perform management activity. Provide one of the following attribute set. (userName, password, role) OR (userName, secretId, role) OR (namedCredentialId)
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterCredentialsArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter(name="databaseCredential")
    def database_credential(self) -> Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']]:
        """
        The credential to connect to the database to perform tablespace administration tasks.
        """
        return pulumi.get(self, "database_credential")

    @database_credential.setter
    def database_credential(self, value: Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']]):
        pulumi.set(self, "database_credential", value)


@pulumi.input_type
class _ManagedDatabasesResetDatabaseParameterState:
    def __init__(__self__, *,
                 credentials: Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterCredentialsArgs']] = None,
                 database_credential: Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']] = None,
                 managed_database_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ManagedDatabasesResetDatabaseParameter resources.
        :param pulumi.Input['ManagedDatabasesResetDatabaseParameterCredentialsArgs'] credentials: The database credentials used to perform management activity. Provide one of the following attribute set. (userName, password, role) OR (userName, secretId, role) OR (namedCredentialId)
        :param pulumi.Input['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs'] database_credential: The credential to connect to the database to perform tablespace administration tasks.
        :param pulumi.Input[str] managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] parameters: A list of database parameter names.
        :param pulumi.Input[str] scope: The clause used to specify when the parameter change takes effect.
               
               Use `MEMORY` to make the change in memory and ensure that it takes effect immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if database_credential is not None:
            pulumi.set(__self__, "database_credential", database_credential)
        if managed_database_id is not None:
            pulumi.set(__self__, "managed_database_id", managed_database_id)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterCredentialsArgs']]:
        """
        The database credentials used to perform management activity. Provide one of the following attribute set. (userName, password, role) OR (userName, secretId, role) OR (namedCredentialId)
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterCredentialsArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter(name="databaseCredential")
    def database_credential(self) -> Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']]:
        """
        The credential to connect to the database to perform tablespace administration tasks.
        """
        return pulumi.get(self, "database_credential")

    @database_credential.setter
    def database_credential(self, value: Optional[pulumi.Input['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']]):
        pulumi.set(self, "database_credential", value)

    @property
    @pulumi.getter(name="managedDatabaseId")
    def managed_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
        """
        return pulumi.get(self, "managed_database_id")

    @managed_database_id.setter
    def managed_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_database_id", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of database parameter names.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The clause used to specify when the parameter change takes effect.

        Use `MEMORY` to make the change in memory and ensure that it takes effect immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


class ManagedDatabasesResetDatabaseParameter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterCredentialsArgs']]] = None,
                 database_credential: Optional[pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']]] = None,
                 managed_database_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Managed Databases Reset Database Parameter resource in Oracle Cloud Infrastructure Database Management service.

        Resets database parameter values to their default or startup values.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_managed_databases_reset_database_parameter = oci.database_management.ManagedDatabasesResetDatabaseParameter("test_managed_databases_reset_database_parameter",
            managed_database_id=test_managed_database["id"],
            parameters=managed_databases_reset_database_parameter_parameters,
            scope=managed_databases_reset_database_parameter_scope,
            credentials=oci.database_management.ManagedDatabasesResetDatabaseParameterCredentialsArgs(
                password=managed_databases_reset_database_parameter_credentials_password,
                role=managed_databases_reset_database_parameter_credentials_role,
                secret_id=test_secret["id"],
                user_name=test_user["name"],
            ),
            database_credential=oci.database_management.ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs(
                credential_type=managed_databases_reset_database_parameter_database_credential_credential_type,
                named_credential_id=test_named_credential["id"],
                password=managed_databases_reset_database_parameter_database_credential_password,
                password_secret_id=test_secret["id"],
                role=managed_databases_reset_database_parameter_database_credential_role,
                username=managed_databases_reset_database_parameter_database_credential_username,
            ))
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterCredentialsArgs']] credentials: The database credentials used to perform management activity. Provide one of the following attribute set. (userName, password, role) OR (userName, secretId, role) OR (namedCredentialId)
        :param pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']] database_credential: The credential to connect to the database to perform tablespace administration tasks.
        :param pulumi.Input[str] managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] parameters: A list of database parameter names.
        :param pulumi.Input[str] scope: The clause used to specify when the parameter change takes effect.
               
               Use `MEMORY` to make the change in memory and ensure that it takes effect immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedDatabasesResetDatabaseParameterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Managed Databases Reset Database Parameter resource in Oracle Cloud Infrastructure Database Management service.

        Resets database parameter values to their default or startup values.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_managed_databases_reset_database_parameter = oci.database_management.ManagedDatabasesResetDatabaseParameter("test_managed_databases_reset_database_parameter",
            managed_database_id=test_managed_database["id"],
            parameters=managed_databases_reset_database_parameter_parameters,
            scope=managed_databases_reset_database_parameter_scope,
            credentials=oci.database_management.ManagedDatabasesResetDatabaseParameterCredentialsArgs(
                password=managed_databases_reset_database_parameter_credentials_password,
                role=managed_databases_reset_database_parameter_credentials_role,
                secret_id=test_secret["id"],
                user_name=test_user["name"],
            ),
            database_credential=oci.database_management.ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs(
                credential_type=managed_databases_reset_database_parameter_database_credential_credential_type,
                named_credential_id=test_named_credential["id"],
                password=managed_databases_reset_database_parameter_database_credential_password,
                password_secret_id=test_secret["id"],
                role=managed_databases_reset_database_parameter_database_credential_role,
                username=managed_databases_reset_database_parameter_database_credential_username,
            ))
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param ManagedDatabasesResetDatabaseParameterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedDatabasesResetDatabaseParameterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterCredentialsArgs']]] = None,
                 database_credential: Optional[pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']]] = None,
                 managed_database_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedDatabasesResetDatabaseParameterArgs.__new__(ManagedDatabasesResetDatabaseParameterArgs)

            __props__.__dict__["credentials"] = credentials
            __props__.__dict__["database_credential"] = database_credential
            if managed_database_id is None and not opts.urn:
                raise TypeError("Missing required property 'managed_database_id'")
            __props__.__dict__["managed_database_id"] = managed_database_id
            if parameters is None and not opts.urn:
                raise TypeError("Missing required property 'parameters'")
            __props__.__dict__["parameters"] = parameters
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
        super(ManagedDatabasesResetDatabaseParameter, __self__).__init__(
            'oci:DatabaseManagement/managedDatabasesResetDatabaseParameter:ManagedDatabasesResetDatabaseParameter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            credentials: Optional[pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterCredentialsArgs']]] = None,
            database_credential: Optional[pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']]] = None,
            managed_database_id: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'ManagedDatabasesResetDatabaseParameter':
        """
        Get an existing ManagedDatabasesResetDatabaseParameter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterCredentialsArgs']] credentials: The database credentials used to perform management activity. Provide one of the following attribute set. (userName, password, role) OR (userName, secretId, role) OR (namedCredentialId)
        :param pulumi.Input[pulumi.InputType['ManagedDatabasesResetDatabaseParameterDatabaseCredentialArgs']] database_credential: The credential to connect to the database to perform tablespace administration tasks.
        :param pulumi.Input[str] managed_database_id: The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] parameters: A list of database parameter names.
        :param pulumi.Input[str] scope: The clause used to specify when the parameter change takes effect.
               
               Use `MEMORY` to make the change in memory and ensure that it takes effect immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ManagedDatabasesResetDatabaseParameterState.__new__(_ManagedDatabasesResetDatabaseParameterState)

        __props__.__dict__["credentials"] = credentials
        __props__.__dict__["database_credential"] = database_credential
        __props__.__dict__["managed_database_id"] = managed_database_id
        __props__.__dict__["parameters"] = parameters
        __props__.__dict__["scope"] = scope
        return ManagedDatabasesResetDatabaseParameter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output['outputs.ManagedDatabasesResetDatabaseParameterCredentials']:
        """
        The database credentials used to perform management activity. Provide one of the following attribute set. (userName, password, role) OR (userName, secretId, role) OR (namedCredentialId)
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="databaseCredential")
    def database_credential(self) -> pulumi.Output['outputs.ManagedDatabasesResetDatabaseParameterDatabaseCredential']:
        """
        The credential to connect to the database to perform tablespace administration tasks.
        """
        return pulumi.get(self, "database_credential")

    @property
    @pulumi.getter(name="managedDatabaseId")
    def managed_database_id(self) -> pulumi.Output[str]:
        """
        The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Managed Database.
        """
        return pulumi.get(self, "managed_database_id")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of database parameter names.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        The clause used to specify when the parameter change takes effect.

        Use `MEMORY` to make the change in memory and ensure that it takes effect immediately. Use `SPFILE` to make the change in the server parameter file. The change takes effect when the database is next shut down and started up again. Use `BOTH` to make the change in memory and in the server parameter file. The change takes effect immediately and persists after the database is shut down and started up again.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "scope")

