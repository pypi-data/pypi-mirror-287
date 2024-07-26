# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IdentityProviderArgs', 'IdentityProvider']

@pulumi.input_type
class IdentityProviderArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 issuer: pulumi.Input[str],
                 jwks_uri: pulumi.Input[str]):
        """
        The set of arguments for constructing a IdentityProvider resource.
        :param pulumi.Input[str] description: A description for the Identity Provider.
        :param pulumi.Input[str] display_name: A human-readable name for the Identity Provider.
        :param pulumi.Input[str] issuer: A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens.
        :param pulumi.Input[str] jwks_uri: A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider.
               
               > **Note:** When using Azure AD identity provider, you can find your Azure Tenant ID in the [Azure Portal under Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "issuer", issuer)
        pulumi.set(__self__, "jwks_uri", jwks_uri)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        A description for the Identity Provider.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        A human-readable name for the Identity Provider.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[str]:
        """
        A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens.
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: pulumi.Input[str]):
        pulumi.set(self, "issuer", value)

    @property
    @pulumi.getter(name="jwksUri")
    def jwks_uri(self) -> pulumi.Input[str]:
        """
        A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider.

        > **Note:** When using Azure AD identity provider, you can find your Azure Tenant ID in the [Azure Portal under Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.
        """
        return pulumi.get(self, "jwks_uri")

    @jwks_uri.setter
    def jwks_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "jwks_uri", value)


@pulumi.input_type
class _IdentityProviderState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 jwks_uri: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IdentityProvider resources.
        :param pulumi.Input[str] description: A description for the Identity Provider.
        :param pulumi.Input[str] display_name: A human-readable name for the Identity Provider.
        :param pulumi.Input[str] issuer: A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens.
        :param pulumi.Input[str] jwks_uri: A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider.
               
               > **Note:** When using Azure AD identity provider, you can find your Azure Tenant ID in the [Azure Portal under Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)
        if jwks_uri is not None:
            pulumi.set(__self__, "jwks_uri", jwks_uri)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Identity Provider.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A human-readable name for the Identity Provider.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[str]]:
        """
        A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens.
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issuer", value)

    @property
    @pulumi.getter(name="jwksUri")
    def jwks_uri(self) -> Optional[pulumi.Input[str]]:
        """
        A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider.

        > **Note:** When using Azure AD identity provider, you can find your Azure Tenant ID in the [Azure Portal under Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.
        """
        return pulumi.get(self, "jwks_uri")

    @jwks_uri.setter
    def jwks_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "jwks_uri", value)


class IdentityProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 jwks_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)

        `IdentityProvider` provides an Identity Provider resource that enables creating, editing, and deleting identity providers on Confluent Cloud.

        ## Example Usage

        ### Example Identity Provider: Azure AD

        ```python
        import pulumi
        import pulumi_confluentcloud as confluentcloud

        azure = confluentcloud.IdentityProvider("azure",
            display_name="My OIDC Provider: Azure AD",
            description="My description",
            issuer="https://login.microsoftonline.com/{tenant_id}/v2.0",
            jwks_uri="https://login.microsoftonline.com/common/discovery/v2.0/keys")
        ```

        ### Example Identity Provider: Okta

        ```python
        import pulumi
        import pulumi_confluentcloud as confluentcloud

        okta = confluentcloud.IdentityProvider("okta",
            display_name="My OIDC Provider: Okta",
            description="My description",
            issuer="https://mycompany.okta.com/oauth2/default",
            jwks_uri="https://mycompany.okta.com/oauth2/default/v1/keys")
        ```

        ## External Documentation

        * [Authenticating with OAuth](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/overview.html).

        ## Import

        You can import an Identity Provider by using Identity Provider ID, for example:

        $ export CONFLUENT_CLOUD_API_KEY="<cloud_api_key>"

        $ export CONFLUENT_CLOUD_API_SECRET="<cloud_api_secret>"

        ```sh
        $ pulumi import confluentcloud:index/identityProvider:IdentityProvider example op-abc123
        ```

        !> **Warning:** Do not forget to delete terminal command history afterwards for security purposes.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for the Identity Provider.
        :param pulumi.Input[str] display_name: A human-readable name for the Identity Provider.
        :param pulumi.Input[str] issuer: A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens.
        :param pulumi.Input[str] jwks_uri: A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider.
               
               > **Note:** When using Azure AD identity provider, you can find your Azure Tenant ID in the [Azure Portal under Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)

        `IdentityProvider` provides an Identity Provider resource that enables creating, editing, and deleting identity providers on Confluent Cloud.

        ## Example Usage

        ### Example Identity Provider: Azure AD

        ```python
        import pulumi
        import pulumi_confluentcloud as confluentcloud

        azure = confluentcloud.IdentityProvider("azure",
            display_name="My OIDC Provider: Azure AD",
            description="My description",
            issuer="https://login.microsoftonline.com/{tenant_id}/v2.0",
            jwks_uri="https://login.microsoftonline.com/common/discovery/v2.0/keys")
        ```

        ### Example Identity Provider: Okta

        ```python
        import pulumi
        import pulumi_confluentcloud as confluentcloud

        okta = confluentcloud.IdentityProvider("okta",
            display_name="My OIDC Provider: Okta",
            description="My description",
            issuer="https://mycompany.okta.com/oauth2/default",
            jwks_uri="https://mycompany.okta.com/oauth2/default/v1/keys")
        ```

        ## External Documentation

        * [Authenticating with OAuth](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/overview.html).

        ## Import

        You can import an Identity Provider by using Identity Provider ID, for example:

        $ export CONFLUENT_CLOUD_API_KEY="<cloud_api_key>"

        $ export CONFLUENT_CLOUD_API_SECRET="<cloud_api_secret>"

        ```sh
        $ pulumi import confluentcloud:index/identityProvider:IdentityProvider example op-abc123
        ```

        !> **Warning:** Do not forget to delete terminal command history afterwards for security purposes.

        :param str resource_name: The name of the resource.
        :param IdentityProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 jwks_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IdentityProviderArgs.__new__(IdentityProviderArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if issuer is None and not opts.urn:
                raise TypeError("Missing required property 'issuer'")
            __props__.__dict__["issuer"] = issuer
            if jwks_uri is None and not opts.urn:
                raise TypeError("Missing required property 'jwks_uri'")
            __props__.__dict__["jwks_uri"] = jwks_uri
        super(IdentityProvider, __self__).__init__(
            'confluentcloud:index/identityProvider:IdentityProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            issuer: Optional[pulumi.Input[str]] = None,
            jwks_uri: Optional[pulumi.Input[str]] = None) -> 'IdentityProvider':
        """
        Get an existing IdentityProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for the Identity Provider.
        :param pulumi.Input[str] display_name: A human-readable name for the Identity Provider.
        :param pulumi.Input[str] issuer: A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens.
        :param pulumi.Input[str] jwks_uri: A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider.
               
               > **Note:** When using Azure AD identity provider, you can find your Azure Tenant ID in the [Azure Portal under Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IdentityProviderState.__new__(_IdentityProviderState)

        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["issuer"] = issuer
        __props__.__dict__["jwks_uri"] = jwks_uri
        return IdentityProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A description for the Identity Provider.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        A human-readable name for the Identity Provider.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def issuer(self) -> pulumi.Output[str]:
        """
        A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens.
        """
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter(name="jwksUri")
    def jwks_uri(self) -> pulumi.Output[str]:
        """
        A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider.

        > **Note:** When using Azure AD identity provider, you can find your Azure Tenant ID in the [Azure Portal under Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.
        """
        return pulumi.get(self, "jwks_uri")

