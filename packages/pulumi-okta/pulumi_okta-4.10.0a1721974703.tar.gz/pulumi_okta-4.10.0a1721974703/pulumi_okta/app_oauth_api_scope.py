# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AppOauthApiScopeArgs', 'AppOauthApiScope']

@pulumi.input_type
class AppOauthApiScopeArgs:
    def __init__(__self__, *,
                 app_id: pulumi.Input[str],
                 issuer: pulumi.Input[str],
                 scopes: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The set of arguments for constructing a AppOauthApiScope resource.
        :param pulumi.Input[str] app_id: ID of the application.
        :param pulumi.Input[str] issuer: The issuer of your Org Authorization Server, your Org URL.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes of the application for which consent is granted.
        """
        pulumi.set(__self__, "app_id", app_id)
        pulumi.set(__self__, "issuer", issuer)
        pulumi.set(__self__, "scopes", scopes)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[str]:
        """
        ID of the application.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[str]:
        """
        The issuer of your Org Authorization Server, your Org URL.
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: pulumi.Input[str]):
        pulumi.set(self, "issuer", value)

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Scopes of the application for which consent is granted.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "scopes", value)


@pulumi.input_type
class _AppOauthApiScopeState:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering AppOauthApiScope resources.
        :param pulumi.Input[str] app_id: ID of the application.
        :param pulumi.Input[str] issuer: The issuer of your Org Authorization Server, your Org URL.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes of the application for which consent is granted.
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the application.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[str]]:
        """
        The issuer of your Org Authorization Server, your Org URL.
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issuer", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Scopes of the application for which consent is granted.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)


class AppOauthApiScope(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages API scopes for OAuth applications.
        This resource allows you to grant or revoke API scopes for OAuth2 applications within your organization.
        Note: you have to create an application before using this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.AppOauthApiScope("example",
            app_id="<application_id>",
            issuer="<your org domain>",
            scopes=[
                "okta.users.read",
                "okta.users.manage",
            ])
        ```

        ## Import

        ```sh
        $ pulumi import okta:index/appOauthApiScope:AppOauthApiScope example &#60;app id&#62
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: ID of the application.
        :param pulumi.Input[str] issuer: The issuer of your Org Authorization Server, your Org URL.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes of the application for which consent is granted.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppOauthApiScopeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages API scopes for OAuth applications.
        This resource allows you to grant or revoke API scopes for OAuth2 applications within your organization.
        Note: you have to create an application before using this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.AppOauthApiScope("example",
            app_id="<application_id>",
            issuer="<your org domain>",
            scopes=[
                "okta.users.read",
                "okta.users.manage",
            ])
        ```

        ## Import

        ```sh
        $ pulumi import okta:index/appOauthApiScope:AppOauthApiScope example &#60;app id&#62
        ```

        :param str resource_name: The name of the resource.
        :param AppOauthApiScopeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppOauthApiScopeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppOauthApiScopeArgs.__new__(AppOauthApiScopeArgs)

            if app_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_id'")
            __props__.__dict__["app_id"] = app_id
            if issuer is None and not opts.urn:
                raise TypeError("Missing required property 'issuer'")
            __props__.__dict__["issuer"] = issuer
            if scopes is None and not opts.urn:
                raise TypeError("Missing required property 'scopes'")
            __props__.__dict__["scopes"] = scopes
        super(AppOauthApiScope, __self__).__init__(
            'okta:index/appOauthApiScope:AppOauthApiScope',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            issuer: Optional[pulumi.Input[str]] = None,
            scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'AppOauthApiScope':
        """
        Get an existing AppOauthApiScope resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: ID of the application.
        :param pulumi.Input[str] issuer: The issuer of your Org Authorization Server, your Org URL.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes of the application for which consent is granted.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppOauthApiScopeState.__new__(_AppOauthApiScopeState)

        __props__.__dict__["app_id"] = app_id
        __props__.__dict__["issuer"] = issuer
        __props__.__dict__["scopes"] = scopes
        return AppOauthApiScope(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        ID of the application.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def issuer(self) -> pulumi.Output[str]:
        """
        The issuer of your Org Authorization Server, your Org URL.
        """
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        Scopes of the application for which consent is granted.
        """
        return pulumi.get(self, "scopes")

