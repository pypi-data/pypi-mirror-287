# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['InvitationArgs', 'Invitation']

@pulumi.input_type
class InvitationArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 allow_deletion: Optional[pulumi.Input[bool]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Invitation resource.
        :param pulumi.Input[str] email: The user/invitee's email address.
        :param pulumi.Input[str] auth_type: Accepted values are: `AUTH_TYPE_LOCAL` and `AUTH_TYPE_SSO`. The user/invitee's authentication type. Note that only the [`OrganizationAdmin role`](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin) can invite `AUTH_TYPE_LOCAL` users to SSO organizations. The user's auth_type is set as `AUTH_TYPE_SSO` by default if the organization has SSO enabled. Otherwise, the user's auth_type is `AUTH_TYPE_LOCAL` by default.
        """
        pulumi.set(__self__, "email", email)
        if allow_deletion is not None:
            pulumi.set(__self__, "allow_deletion", allow_deletion)
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        The user/invitee's email address.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="allowDeletion")
    def allow_deletion(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_deletion")

    @allow_deletion.setter
    def allow_deletion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_deletion", value)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[str]]:
        """
        Accepted values are: `AUTH_TYPE_LOCAL` and `AUTH_TYPE_SSO`. The user/invitee's authentication type. Note that only the [`OrganizationAdmin role`](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin) can invite `AUTH_TYPE_LOCAL` users to SSO organizations. The user's auth_type is set as `AUTH_TYPE_SSO` by default if the organization has SSO enabled. Otherwise, the user's auth_type is `AUTH_TYPE_LOCAL` by default.
        """
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_type", value)


@pulumi.input_type
class _InvitationState:
    def __init__(__self__, *,
                 accepted_at: Optional[pulumi.Input[str]] = None,
                 allow_deletion: Optional[pulumi.Input[bool]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 creators: Optional[pulumi.Input[Sequence[pulumi.Input['InvitationCreatorArgs']]]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input['InvitationUserArgs']]]] = None):
        """
        Input properties used for looking up and filtering Invitation resources.
        :param pulumi.Input[str] accepted_at: (Optional String) The timestamp that the invitation was accepted.
        :param pulumi.Input[str] auth_type: Accepted values are: `AUTH_TYPE_LOCAL` and `AUTH_TYPE_SSO`. The user/invitee's authentication type. Note that only the [`OrganizationAdmin role`](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin) can invite `AUTH_TYPE_LOCAL` users to SSO organizations. The user's auth_type is set as `AUTH_TYPE_SSO` by default if the organization has SSO enabled. Otherwise, the user's auth_type is `AUTH_TYPE_LOCAL` by default.
        :param pulumi.Input[Sequence[pulumi.Input['InvitationCreatorArgs']]] creators: (Required Configuration Block) supports the following:
        :param pulumi.Input[str] email: The user/invitee's email address.
        :param pulumi.Input[str] expires_at: (Optional String) The timestamp that the invitation will expire.
        :param pulumi.Input[str] status: (Optional String) The status of invitations. Accepted values are: `INVITE_STATUS_SENT`,`INVITE_STATUS_STAGED`,`INVITE_STATUS_ACCEPTED`,`INVITE_STATUS_EXPIRED`, and `INVITE_STATUS_DEACTIVATED`.
        :param pulumi.Input[Sequence[pulumi.Input['InvitationUserArgs']]] users: (Required Configuration Block) supports the following:
        """
        if accepted_at is not None:
            pulumi.set(__self__, "accepted_at", accepted_at)
        if allow_deletion is not None:
            pulumi.set(__self__, "allow_deletion", allow_deletion)
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)
        if creators is not None:
            pulumi.set(__self__, "creators", creators)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if users is not None:
            pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter(name="acceptedAt")
    def accepted_at(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional String) The timestamp that the invitation was accepted.
        """
        return pulumi.get(self, "accepted_at")

    @accepted_at.setter
    def accepted_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accepted_at", value)

    @property
    @pulumi.getter(name="allowDeletion")
    def allow_deletion(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_deletion")

    @allow_deletion.setter
    def allow_deletion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_deletion", value)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[str]]:
        """
        Accepted values are: `AUTH_TYPE_LOCAL` and `AUTH_TYPE_SSO`. The user/invitee's authentication type. Note that only the [`OrganizationAdmin role`](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin) can invite `AUTH_TYPE_LOCAL` users to SSO organizations. The user's auth_type is set as `AUTH_TYPE_SSO` by default if the organization has SSO enabled. Otherwise, the user's auth_type is `AUTH_TYPE_LOCAL` by default.
        """
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter
    def creators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InvitationCreatorArgs']]]]:
        """
        (Required Configuration Block) supports the following:
        """
        return pulumi.get(self, "creators")

    @creators.setter
    def creators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InvitationCreatorArgs']]]]):
        pulumi.set(self, "creators", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The user/invitee's email address.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional String) The timestamp that the invitation will expire.
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        (Optional String) The status of invitations. Accepted values are: `INVITE_STATUS_SENT`,`INVITE_STATUS_STAGED`,`INVITE_STATUS_ACCEPTED`,`INVITE_STATUS_EXPIRED`, and `INVITE_STATUS_DEACTIVATED`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InvitationUserArgs']]]]:
        """
        (Required Configuration Block) supports the following:
        """
        return pulumi.get(self, "users")

    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InvitationUserArgs']]]]):
        pulumi.set(self, "users", value)


class Invitation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_deletion: Optional[pulumi.Input[bool]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)

        `Invitation` provides an invitation resource that enables creating, reading, and deleting invitation on Confluent Cloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_confluentcloud as confluentcloud

        main = confluentcloud.Invitation("main", email="")
        main2 = confluentcloud.Invitation("main2",
            email="",
            auth_type="AUTH_TYPE_LOCAL")
        ```

        ## Import

        You can import an Invitation by using Invitation ID, for example:

        $ export CONFLUENT_CLOUD_API_KEY="<cloud_api_key>"

        $ export CONFLUENT_CLOUD_API_SECRET="<cloud_api_secret>"

        ```sh
        $ pulumi import confluentcloud:index/invitation:Invitation main i-gxxn1
        ```

        !> **Warning:** Do not forget to delete terminal command history afterwards for security purposes.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_type: Accepted values are: `AUTH_TYPE_LOCAL` and `AUTH_TYPE_SSO`. The user/invitee's authentication type. Note that only the [`OrganizationAdmin role`](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin) can invite `AUTH_TYPE_LOCAL` users to SSO organizations. The user's auth_type is set as `AUTH_TYPE_SSO` by default if the organization has SSO enabled. Otherwise, the user's auth_type is `AUTH_TYPE_LOCAL` by default.
        :param pulumi.Input[str] email: The user/invitee's email address.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InvitationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)

        `Invitation` provides an invitation resource that enables creating, reading, and deleting invitation on Confluent Cloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_confluentcloud as confluentcloud

        main = confluentcloud.Invitation("main", email="")
        main2 = confluentcloud.Invitation("main2",
            email="",
            auth_type="AUTH_TYPE_LOCAL")
        ```

        ## Import

        You can import an Invitation by using Invitation ID, for example:

        $ export CONFLUENT_CLOUD_API_KEY="<cloud_api_key>"

        $ export CONFLUENT_CLOUD_API_SECRET="<cloud_api_secret>"

        ```sh
        $ pulumi import confluentcloud:index/invitation:Invitation main i-gxxn1
        ```

        !> **Warning:** Do not forget to delete terminal command history afterwards for security purposes.

        :param str resource_name: The name of the resource.
        :param InvitationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InvitationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_deletion: Optional[pulumi.Input[bool]] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InvitationArgs.__new__(InvitationArgs)

            __props__.__dict__["allow_deletion"] = allow_deletion
            __props__.__dict__["auth_type"] = auth_type
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            __props__.__dict__["accepted_at"] = None
            __props__.__dict__["creators"] = None
            __props__.__dict__["expires_at"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["users"] = None
        super(Invitation, __self__).__init__(
            'confluentcloud:index/invitation:Invitation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accepted_at: Optional[pulumi.Input[str]] = None,
            allow_deletion: Optional[pulumi.Input[bool]] = None,
            auth_type: Optional[pulumi.Input[str]] = None,
            creators: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InvitationCreatorArgs']]]]] = None,
            email: Optional[pulumi.Input[str]] = None,
            expires_at: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            users: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InvitationUserArgs']]]]] = None) -> 'Invitation':
        """
        Get an existing Invitation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accepted_at: (Optional String) The timestamp that the invitation was accepted.
        :param pulumi.Input[str] auth_type: Accepted values are: `AUTH_TYPE_LOCAL` and `AUTH_TYPE_SSO`. The user/invitee's authentication type. Note that only the [`OrganizationAdmin role`](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin) can invite `AUTH_TYPE_LOCAL` users to SSO organizations. The user's auth_type is set as `AUTH_TYPE_SSO` by default if the organization has SSO enabled. Otherwise, the user's auth_type is `AUTH_TYPE_LOCAL` by default.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InvitationCreatorArgs']]]] creators: (Required Configuration Block) supports the following:
        :param pulumi.Input[str] email: The user/invitee's email address.
        :param pulumi.Input[str] expires_at: (Optional String) The timestamp that the invitation will expire.
        :param pulumi.Input[str] status: (Optional String) The status of invitations. Accepted values are: `INVITE_STATUS_SENT`,`INVITE_STATUS_STAGED`,`INVITE_STATUS_ACCEPTED`,`INVITE_STATUS_EXPIRED`, and `INVITE_STATUS_DEACTIVATED`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InvitationUserArgs']]]] users: (Required Configuration Block) supports the following:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InvitationState.__new__(_InvitationState)

        __props__.__dict__["accepted_at"] = accepted_at
        __props__.__dict__["allow_deletion"] = allow_deletion
        __props__.__dict__["auth_type"] = auth_type
        __props__.__dict__["creators"] = creators
        __props__.__dict__["email"] = email
        __props__.__dict__["expires_at"] = expires_at
        __props__.__dict__["status"] = status
        __props__.__dict__["users"] = users
        return Invitation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptedAt")
    def accepted_at(self) -> pulumi.Output[str]:
        """
        (Optional String) The timestamp that the invitation was accepted.
        """
        return pulumi.get(self, "accepted_at")

    @property
    @pulumi.getter(name="allowDeletion")
    def allow_deletion(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "allow_deletion")

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[str]:
        """
        Accepted values are: `AUTH_TYPE_LOCAL` and `AUTH_TYPE_SSO`. The user/invitee's authentication type. Note that only the [`OrganizationAdmin role`](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin) can invite `AUTH_TYPE_LOCAL` users to SSO organizations. The user's auth_type is set as `AUTH_TYPE_SSO` by default if the organization has SSO enabled. Otherwise, the user's auth_type is `AUTH_TYPE_LOCAL` by default.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter
    def creators(self) -> pulumi.Output[Sequence['outputs.InvitationCreator']]:
        """
        (Required Configuration Block) supports the following:
        """
        return pulumi.get(self, "creators")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The user/invitee's email address.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[str]:
        """
        (Optional String) The timestamp that the invitation will expire.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        (Optional String) The status of invitations. Accepted values are: `INVITE_STATUS_SENT`,`INVITE_STATUS_STAGED`,`INVITE_STATUS_ACCEPTED`,`INVITE_STATUS_EXPIRED`, and `INVITE_STATUS_DEACTIVATED`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def users(self) -> pulumi.Output[Sequence['outputs.InvitationUser']]:
        """
        (Required Configuration Block) supports the following:
        """
        return pulumi.get(self, "users")

