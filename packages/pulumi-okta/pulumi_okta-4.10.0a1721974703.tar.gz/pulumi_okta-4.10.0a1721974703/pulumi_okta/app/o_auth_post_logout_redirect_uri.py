# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['OAuthPostLogoutRedirectUriArgs', 'OAuthPostLogoutRedirectUri']

@pulumi.input_type
class OAuthPostLogoutRedirectUriArgs:
    def __init__(__self__, *,
                 app_id: pulumi.Input[str],
                 uri: pulumi.Input[str]):
        """
        The set of arguments for constructing a OAuthPostLogoutRedirectUri resource.
        :param pulumi.Input[str] app_id: OAuth application ID.
        :param pulumi.Input[str] uri: Post Logout Redirect URI to append to Okta OIDC application.
        """
        pulumi.set(__self__, "app_id", app_id)
        pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[str]:
        """
        OAuth application ID.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Input[str]:
        """
        Post Logout Redirect URI to append to Okta OIDC application.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "uri", value)


@pulumi.input_type
class _OAuthPostLogoutRedirectUriState:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OAuthPostLogoutRedirectUri resources.
        :param pulumi.Input[str] app_id: OAuth application ID.
        :param pulumi.Input[str] uri: Post Logout Redirect URI to append to Okta OIDC application.
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        OAuth application ID.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        Post Logout Redirect URI to append to Okta OIDC application.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


class OAuthPostLogoutRedirectUri(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to manage post logout redirection URI for use in redirect-based flows.

        > `app.OAuthPostLogoutRedirectUri` has been marked deprecated and will
        be removed in the v5 release of the provider. Operators should manage the post
        logout redirect URIs for an oauth app directly on that resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        test = okta.app.OAuth("test",
            label="testAcc_replace_with_uuid",
            type="web",
            grant_types=["authorization_code"],
            response_types=["code"],
            redirect_uris=["myapp://callback"],
            post_logout_redirect_uris=["https://www.example.com"])
        test_o_auth_post_logout_redirect_uri = okta.app.OAuthPostLogoutRedirectUri("test",
            app_id=test.id,
            uri="https://www.example.com")
        ```

        ## Import

        ```sh
        $ pulumi import okta:app/oAuthPostLogoutRedirectUri:OAuthPostLogoutRedirectUri example &#60;app id&#62;/&#60;uri&#62
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: OAuth application ID.
        :param pulumi.Input[str] uri: Post Logout Redirect URI to append to Okta OIDC application.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OAuthPostLogoutRedirectUriArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to manage post logout redirection URI for use in redirect-based flows.

        > `app.OAuthPostLogoutRedirectUri` has been marked deprecated and will
        be removed in the v5 release of the provider. Operators should manage the post
        logout redirect URIs for an oauth app directly on that resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        test = okta.app.OAuth("test",
            label="testAcc_replace_with_uuid",
            type="web",
            grant_types=["authorization_code"],
            response_types=["code"],
            redirect_uris=["myapp://callback"],
            post_logout_redirect_uris=["https://www.example.com"])
        test_o_auth_post_logout_redirect_uri = okta.app.OAuthPostLogoutRedirectUri("test",
            app_id=test.id,
            uri="https://www.example.com")
        ```

        ## Import

        ```sh
        $ pulumi import okta:app/oAuthPostLogoutRedirectUri:OAuthPostLogoutRedirectUri example &#60;app id&#62;/&#60;uri&#62
        ```

        :param str resource_name: The name of the resource.
        :param OAuthPostLogoutRedirectUriArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OAuthPostLogoutRedirectUriArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OAuthPostLogoutRedirectUriArgs.__new__(OAuthPostLogoutRedirectUriArgs)

            if app_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_id'")
            __props__.__dict__["app_id"] = app_id
            if uri is None and not opts.urn:
                raise TypeError("Missing required property 'uri'")
            __props__.__dict__["uri"] = uri
        super(OAuthPostLogoutRedirectUri, __self__).__init__(
            'okta:app/oAuthPostLogoutRedirectUri:OAuthPostLogoutRedirectUri',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            uri: Optional[pulumi.Input[str]] = None) -> 'OAuthPostLogoutRedirectUri':
        """
        Get an existing OAuthPostLogoutRedirectUri resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: OAuth application ID.
        :param pulumi.Input[str] uri: Post Logout Redirect URI to append to Okta OIDC application.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OAuthPostLogoutRedirectUriState.__new__(_OAuthPostLogoutRedirectUriState)

        __props__.__dict__["app_id"] = app_id
        __props__.__dict__["uri"] = uri
        return OAuthPostLogoutRedirectUri(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        OAuth application ID.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[str]:
        """
        Post Logout Redirect URI to append to Okta OIDC application.
        """
        return pulumi.get(self, "uri")

