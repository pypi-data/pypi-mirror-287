# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BasicAuthArgs', 'BasicAuth']

@pulumi.input_type
class BasicAuthArgs:
    def __init__(__self__, *,
                 auth_url: pulumi.Input[str],
                 label: pulumi.Input[str],
                 url: pulumi.Input[str],
                 accessibility_error_redirect_url: Optional[pulumi.Input[str]] = None,
                 accessibility_login_redirect_url: Optional[pulumi.Input[str]] = None,
                 accessibility_self_service: Optional[pulumi.Input[bool]] = None,
                 admin_note: Optional[pulumi.Input[str]] = None,
                 app_links_json: Optional[pulumi.Input[str]] = None,
                 auto_submit_toolbar: Optional[pulumi.Input[bool]] = None,
                 enduser_note: Optional[pulumi.Input[str]] = None,
                 hide_ios: Optional[pulumi.Input[bool]] = None,
                 hide_web: Optional[pulumi.Input[bool]] = None,
                 logo: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BasicAuth resource.
        :param pulumi.Input[str] auth_url: The URL of the authenticating site for this app.
        :param pulumi.Input[str] label: The Application's display name.
        :param pulumi.Input[str] url: The URL of the sign-in page for this app.
        :param pulumi.Input[str] accessibility_error_redirect_url: Custom error page URL
        :param pulumi.Input[str] accessibility_login_redirect_url: Custom login page URL
        :param pulumi.Input[bool] accessibility_self_service: Enable self service. Default is `false`
        :param pulumi.Input[str] admin_note: Application notes for admins.
        :param pulumi.Input[str] app_links_json: Displays specific appLinks for the app. The value for each application link should be boolean.
        :param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
        :param pulumi.Input[str] enduser_note: Application notes for end users.
        :param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
        :param pulumi.Input[bool] hide_web: Do not display application icon to users
        :param pulumi.Input[str] logo: Local file path to the logo. The file must be in PNG, JPG, or GIF format, and less than 1 MB in size.
        :param pulumi.Input[str] status: Status of application. By default, it is `ACTIVE`
        """
        pulumi.set(__self__, "auth_url", auth_url)
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "url", url)
        if accessibility_error_redirect_url is not None:
            pulumi.set(__self__, "accessibility_error_redirect_url", accessibility_error_redirect_url)
        if accessibility_login_redirect_url is not None:
            pulumi.set(__self__, "accessibility_login_redirect_url", accessibility_login_redirect_url)
        if accessibility_self_service is not None:
            pulumi.set(__self__, "accessibility_self_service", accessibility_self_service)
        if admin_note is not None:
            pulumi.set(__self__, "admin_note", admin_note)
        if app_links_json is not None:
            pulumi.set(__self__, "app_links_json", app_links_json)
        if auto_submit_toolbar is not None:
            pulumi.set(__self__, "auto_submit_toolbar", auto_submit_toolbar)
        if enduser_note is not None:
            pulumi.set(__self__, "enduser_note", enduser_note)
        if hide_ios is not None:
            pulumi.set(__self__, "hide_ios", hide_ios)
        if hide_web is not None:
            pulumi.set(__self__, "hide_web", hide_web)
        if logo is not None:
            pulumi.set(__self__, "logo", logo)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="authUrl")
    def auth_url(self) -> pulumi.Input[str]:
        """
        The URL of the authenticating site for this app.
        """
        return pulumi.get(self, "auth_url")

    @auth_url.setter
    def auth_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "auth_url", value)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        """
        The Application's display name.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        The URL of the sign-in page for this app.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="accessibilityErrorRedirectUrl")
    def accessibility_error_redirect_url(self) -> Optional[pulumi.Input[str]]:
        """
        Custom error page URL
        """
        return pulumi.get(self, "accessibility_error_redirect_url")

    @accessibility_error_redirect_url.setter
    def accessibility_error_redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accessibility_error_redirect_url", value)

    @property
    @pulumi.getter(name="accessibilityLoginRedirectUrl")
    def accessibility_login_redirect_url(self) -> Optional[pulumi.Input[str]]:
        """
        Custom login page URL
        """
        return pulumi.get(self, "accessibility_login_redirect_url")

    @accessibility_login_redirect_url.setter
    def accessibility_login_redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accessibility_login_redirect_url", value)

    @property
    @pulumi.getter(name="accessibilitySelfService")
    def accessibility_self_service(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable self service. Default is `false`
        """
        return pulumi.get(self, "accessibility_self_service")

    @accessibility_self_service.setter
    def accessibility_self_service(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "accessibility_self_service", value)

    @property
    @pulumi.getter(name="adminNote")
    def admin_note(self) -> Optional[pulumi.Input[str]]:
        """
        Application notes for admins.
        """
        return pulumi.get(self, "admin_note")

    @admin_note.setter
    def admin_note(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_note", value)

    @property
    @pulumi.getter(name="appLinksJson")
    def app_links_json(self) -> Optional[pulumi.Input[str]]:
        """
        Displays specific appLinks for the app. The value for each application link should be boolean.
        """
        return pulumi.get(self, "app_links_json")

    @app_links_json.setter
    def app_links_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_links_json", value)

    @property
    @pulumi.getter(name="autoSubmitToolbar")
    def auto_submit_toolbar(self) -> Optional[pulumi.Input[bool]]:
        """
        Display auto submit toolbar
        """
        return pulumi.get(self, "auto_submit_toolbar")

    @auto_submit_toolbar.setter
    def auto_submit_toolbar(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_submit_toolbar", value)

    @property
    @pulumi.getter(name="enduserNote")
    def enduser_note(self) -> Optional[pulumi.Input[str]]:
        """
        Application notes for end users.
        """
        return pulumi.get(self, "enduser_note")

    @enduser_note.setter
    def enduser_note(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enduser_note", value)

    @property
    @pulumi.getter(name="hideIos")
    def hide_ios(self) -> Optional[pulumi.Input[bool]]:
        """
        Do not display application icon on mobile app
        """
        return pulumi.get(self, "hide_ios")

    @hide_ios.setter
    def hide_ios(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hide_ios", value)

    @property
    @pulumi.getter(name="hideWeb")
    def hide_web(self) -> Optional[pulumi.Input[bool]]:
        """
        Do not display application icon to users
        """
        return pulumi.get(self, "hide_web")

    @hide_web.setter
    def hide_web(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hide_web", value)

    @property
    @pulumi.getter
    def logo(self) -> Optional[pulumi.Input[str]]:
        """
        Local file path to the logo. The file must be in PNG, JPG, or GIF format, and less than 1 MB in size.
        """
        return pulumi.get(self, "logo")

    @logo.setter
    def logo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logo", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of application. By default, it is `ACTIVE`
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _BasicAuthState:
    def __init__(__self__, *,
                 accessibility_error_redirect_url: Optional[pulumi.Input[str]] = None,
                 accessibility_login_redirect_url: Optional[pulumi.Input[str]] = None,
                 accessibility_self_service: Optional[pulumi.Input[bool]] = None,
                 admin_note: Optional[pulumi.Input[str]] = None,
                 app_links_json: Optional[pulumi.Input[str]] = None,
                 auth_url: Optional[pulumi.Input[str]] = None,
                 auto_submit_toolbar: Optional[pulumi.Input[bool]] = None,
                 enduser_note: Optional[pulumi.Input[str]] = None,
                 hide_ios: Optional[pulumi.Input[bool]] = None,
                 hide_web: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 logo: Optional[pulumi.Input[str]] = None,
                 logo_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sign_on_mode: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BasicAuth resources.
        :param pulumi.Input[str] accessibility_error_redirect_url: Custom error page URL
        :param pulumi.Input[str] accessibility_login_redirect_url: Custom login page URL
        :param pulumi.Input[bool] accessibility_self_service: Enable self service. Default is `false`
        :param pulumi.Input[str] admin_note: Application notes for admins.
        :param pulumi.Input[str] app_links_json: Displays specific appLinks for the app. The value for each application link should be boolean.
        :param pulumi.Input[str] auth_url: The URL of the authenticating site for this app.
        :param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
        :param pulumi.Input[str] enduser_note: Application notes for end users.
        :param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
        :param pulumi.Input[bool] hide_web: Do not display application icon to users
        :param pulumi.Input[str] label: The Application's display name.
        :param pulumi.Input[str] logo: Local file path to the logo. The file must be in PNG, JPG, or GIF format, and less than 1 MB in size.
        :param pulumi.Input[str] logo_url: URL of the application's logo
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] sign_on_mode: Sign on mode of application.
        :param pulumi.Input[str] status: Status of application. By default, it is `ACTIVE`
        :param pulumi.Input[str] url: The URL of the sign-in page for this app.
        """
        if accessibility_error_redirect_url is not None:
            pulumi.set(__self__, "accessibility_error_redirect_url", accessibility_error_redirect_url)
        if accessibility_login_redirect_url is not None:
            pulumi.set(__self__, "accessibility_login_redirect_url", accessibility_login_redirect_url)
        if accessibility_self_service is not None:
            pulumi.set(__self__, "accessibility_self_service", accessibility_self_service)
        if admin_note is not None:
            pulumi.set(__self__, "admin_note", admin_note)
        if app_links_json is not None:
            pulumi.set(__self__, "app_links_json", app_links_json)
        if auth_url is not None:
            pulumi.set(__self__, "auth_url", auth_url)
        if auto_submit_toolbar is not None:
            pulumi.set(__self__, "auto_submit_toolbar", auto_submit_toolbar)
        if enduser_note is not None:
            pulumi.set(__self__, "enduser_note", enduser_note)
        if hide_ios is not None:
            pulumi.set(__self__, "hide_ios", hide_ios)
        if hide_web is not None:
            pulumi.set(__self__, "hide_web", hide_web)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if logo is not None:
            pulumi.set(__self__, "logo", logo)
        if logo_url is not None:
            pulumi.set(__self__, "logo_url", logo_url)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sign_on_mode is not None:
            pulumi.set(__self__, "sign_on_mode", sign_on_mode)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="accessibilityErrorRedirectUrl")
    def accessibility_error_redirect_url(self) -> Optional[pulumi.Input[str]]:
        """
        Custom error page URL
        """
        return pulumi.get(self, "accessibility_error_redirect_url")

    @accessibility_error_redirect_url.setter
    def accessibility_error_redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accessibility_error_redirect_url", value)

    @property
    @pulumi.getter(name="accessibilityLoginRedirectUrl")
    def accessibility_login_redirect_url(self) -> Optional[pulumi.Input[str]]:
        """
        Custom login page URL
        """
        return pulumi.get(self, "accessibility_login_redirect_url")

    @accessibility_login_redirect_url.setter
    def accessibility_login_redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accessibility_login_redirect_url", value)

    @property
    @pulumi.getter(name="accessibilitySelfService")
    def accessibility_self_service(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable self service. Default is `false`
        """
        return pulumi.get(self, "accessibility_self_service")

    @accessibility_self_service.setter
    def accessibility_self_service(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "accessibility_self_service", value)

    @property
    @pulumi.getter(name="adminNote")
    def admin_note(self) -> Optional[pulumi.Input[str]]:
        """
        Application notes for admins.
        """
        return pulumi.get(self, "admin_note")

    @admin_note.setter
    def admin_note(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_note", value)

    @property
    @pulumi.getter(name="appLinksJson")
    def app_links_json(self) -> Optional[pulumi.Input[str]]:
        """
        Displays specific appLinks for the app. The value for each application link should be boolean.
        """
        return pulumi.get(self, "app_links_json")

    @app_links_json.setter
    def app_links_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_links_json", value)

    @property
    @pulumi.getter(name="authUrl")
    def auth_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the authenticating site for this app.
        """
        return pulumi.get(self, "auth_url")

    @auth_url.setter
    def auth_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_url", value)

    @property
    @pulumi.getter(name="autoSubmitToolbar")
    def auto_submit_toolbar(self) -> Optional[pulumi.Input[bool]]:
        """
        Display auto submit toolbar
        """
        return pulumi.get(self, "auto_submit_toolbar")

    @auto_submit_toolbar.setter
    def auto_submit_toolbar(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_submit_toolbar", value)

    @property
    @pulumi.getter(name="enduserNote")
    def enduser_note(self) -> Optional[pulumi.Input[str]]:
        """
        Application notes for end users.
        """
        return pulumi.get(self, "enduser_note")

    @enduser_note.setter
    def enduser_note(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enduser_note", value)

    @property
    @pulumi.getter(name="hideIos")
    def hide_ios(self) -> Optional[pulumi.Input[bool]]:
        """
        Do not display application icon on mobile app
        """
        return pulumi.get(self, "hide_ios")

    @hide_ios.setter
    def hide_ios(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hide_ios", value)

    @property
    @pulumi.getter(name="hideWeb")
    def hide_web(self) -> Optional[pulumi.Input[bool]]:
        """
        Do not display application icon to users
        """
        return pulumi.get(self, "hide_web")

    @hide_web.setter
    def hide_web(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hide_web", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        The Application's display name.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def logo(self) -> Optional[pulumi.Input[str]]:
        """
        Local file path to the logo. The file must be in PNG, JPG, or GIF format, and less than 1 MB in size.
        """
        return pulumi.get(self, "logo")

    @logo.setter
    def logo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logo", value)

    @property
    @pulumi.getter(name="logoUrl")
    def logo_url(self) -> Optional[pulumi.Input[str]]:
        """
        URL of the application's logo
        """
        return pulumi.get(self, "logo_url")

    @logo_url.setter
    def logo_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logo_url", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the app.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="signOnMode")
    def sign_on_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Sign on mode of application.
        """
        return pulumi.get(self, "sign_on_mode")

    @sign_on_mode.setter
    def sign_on_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sign_on_mode", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of application. By default, it is `ACTIVE`
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the sign-in page for this app.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class BasicAuth(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accessibility_error_redirect_url: Optional[pulumi.Input[str]] = None,
                 accessibility_login_redirect_url: Optional[pulumi.Input[str]] = None,
                 accessibility_self_service: Optional[pulumi.Input[bool]] = None,
                 admin_note: Optional[pulumi.Input[str]] = None,
                 app_links_json: Optional[pulumi.Input[str]] = None,
                 auth_url: Optional[pulumi.Input[str]] = None,
                 auto_submit_toolbar: Optional[pulumi.Input[bool]] = None,
                 enduser_note: Optional[pulumi.Input[str]] = None,
                 hide_ios: Optional[pulumi.Input[bool]] = None,
                 hide_web: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 logo: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to create and configure an Auto Login Okta Application.
        > During an apply if there is change in status the app will first be
        activated or deactivated in accordance with the status change. Then, all
        other arguments that changed will be applied.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.app.BasicAuth("example",
            label="Example",
            url="https://example.com/login.html",
            auth_url="https://example.com/auth.html")
        ```

        ## Import

        ```sh
        $ pulumi import okta:app/basicAuth:BasicAuth example &#60;app id&#62
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accessibility_error_redirect_url: Custom error page URL
        :param pulumi.Input[str] accessibility_login_redirect_url: Custom login page URL
        :param pulumi.Input[bool] accessibility_self_service: Enable self service. Default is `false`
        :param pulumi.Input[str] admin_note: Application notes for admins.
        :param pulumi.Input[str] app_links_json: Displays specific appLinks for the app. The value for each application link should be boolean.
        :param pulumi.Input[str] auth_url: The URL of the authenticating site for this app.
        :param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
        :param pulumi.Input[str] enduser_note: Application notes for end users.
        :param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
        :param pulumi.Input[bool] hide_web: Do not display application icon to users
        :param pulumi.Input[str] label: The Application's display name.
        :param pulumi.Input[str] logo: Local file path to the logo. The file must be in PNG, JPG, or GIF format, and less than 1 MB in size.
        :param pulumi.Input[str] status: Status of application. By default, it is `ACTIVE`
        :param pulumi.Input[str] url: The URL of the sign-in page for this app.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BasicAuthArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to create and configure an Auto Login Okta Application.
        > During an apply if there is change in status the app will first be
        activated or deactivated in accordance with the status change. Then, all
        other arguments that changed will be applied.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.app.BasicAuth("example",
            label="Example",
            url="https://example.com/login.html",
            auth_url="https://example.com/auth.html")
        ```

        ## Import

        ```sh
        $ pulumi import okta:app/basicAuth:BasicAuth example &#60;app id&#62
        ```

        :param str resource_name: The name of the resource.
        :param BasicAuthArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BasicAuthArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accessibility_error_redirect_url: Optional[pulumi.Input[str]] = None,
                 accessibility_login_redirect_url: Optional[pulumi.Input[str]] = None,
                 accessibility_self_service: Optional[pulumi.Input[bool]] = None,
                 admin_note: Optional[pulumi.Input[str]] = None,
                 app_links_json: Optional[pulumi.Input[str]] = None,
                 auth_url: Optional[pulumi.Input[str]] = None,
                 auto_submit_toolbar: Optional[pulumi.Input[bool]] = None,
                 enduser_note: Optional[pulumi.Input[str]] = None,
                 hide_ios: Optional[pulumi.Input[bool]] = None,
                 hide_web: Optional[pulumi.Input[bool]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 logo: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BasicAuthArgs.__new__(BasicAuthArgs)

            __props__.__dict__["accessibility_error_redirect_url"] = accessibility_error_redirect_url
            __props__.__dict__["accessibility_login_redirect_url"] = accessibility_login_redirect_url
            __props__.__dict__["accessibility_self_service"] = accessibility_self_service
            __props__.__dict__["admin_note"] = admin_note
            __props__.__dict__["app_links_json"] = app_links_json
            if auth_url is None and not opts.urn:
                raise TypeError("Missing required property 'auth_url'")
            __props__.__dict__["auth_url"] = auth_url
            __props__.__dict__["auto_submit_toolbar"] = auto_submit_toolbar
            __props__.__dict__["enduser_note"] = enduser_note
            __props__.__dict__["hide_ios"] = hide_ios
            __props__.__dict__["hide_web"] = hide_web
            if label is None and not opts.urn:
                raise TypeError("Missing required property 'label'")
            __props__.__dict__["label"] = label
            __props__.__dict__["logo"] = logo
            __props__.__dict__["status"] = status
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["logo_url"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["sign_on_mode"] = None
        super(BasicAuth, __self__).__init__(
            'okta:app/basicAuth:BasicAuth',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accessibility_error_redirect_url: Optional[pulumi.Input[str]] = None,
            accessibility_login_redirect_url: Optional[pulumi.Input[str]] = None,
            accessibility_self_service: Optional[pulumi.Input[bool]] = None,
            admin_note: Optional[pulumi.Input[str]] = None,
            app_links_json: Optional[pulumi.Input[str]] = None,
            auth_url: Optional[pulumi.Input[str]] = None,
            auto_submit_toolbar: Optional[pulumi.Input[bool]] = None,
            enduser_note: Optional[pulumi.Input[str]] = None,
            hide_ios: Optional[pulumi.Input[bool]] = None,
            hide_web: Optional[pulumi.Input[bool]] = None,
            label: Optional[pulumi.Input[str]] = None,
            logo: Optional[pulumi.Input[str]] = None,
            logo_url: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sign_on_mode: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'BasicAuth':
        """
        Get an existing BasicAuth resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accessibility_error_redirect_url: Custom error page URL
        :param pulumi.Input[str] accessibility_login_redirect_url: Custom login page URL
        :param pulumi.Input[bool] accessibility_self_service: Enable self service. Default is `false`
        :param pulumi.Input[str] admin_note: Application notes for admins.
        :param pulumi.Input[str] app_links_json: Displays specific appLinks for the app. The value for each application link should be boolean.
        :param pulumi.Input[str] auth_url: The URL of the authenticating site for this app.
        :param pulumi.Input[bool] auto_submit_toolbar: Display auto submit toolbar
        :param pulumi.Input[str] enduser_note: Application notes for end users.
        :param pulumi.Input[bool] hide_ios: Do not display application icon on mobile app
        :param pulumi.Input[bool] hide_web: Do not display application icon to users
        :param pulumi.Input[str] label: The Application's display name.
        :param pulumi.Input[str] logo: Local file path to the logo. The file must be in PNG, JPG, or GIF format, and less than 1 MB in size.
        :param pulumi.Input[str] logo_url: URL of the application's logo
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] sign_on_mode: Sign on mode of application.
        :param pulumi.Input[str] status: Status of application. By default, it is `ACTIVE`
        :param pulumi.Input[str] url: The URL of the sign-in page for this app.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BasicAuthState.__new__(_BasicAuthState)

        __props__.__dict__["accessibility_error_redirect_url"] = accessibility_error_redirect_url
        __props__.__dict__["accessibility_login_redirect_url"] = accessibility_login_redirect_url
        __props__.__dict__["accessibility_self_service"] = accessibility_self_service
        __props__.__dict__["admin_note"] = admin_note
        __props__.__dict__["app_links_json"] = app_links_json
        __props__.__dict__["auth_url"] = auth_url
        __props__.__dict__["auto_submit_toolbar"] = auto_submit_toolbar
        __props__.__dict__["enduser_note"] = enduser_note
        __props__.__dict__["hide_ios"] = hide_ios
        __props__.__dict__["hide_web"] = hide_web
        __props__.__dict__["label"] = label
        __props__.__dict__["logo"] = logo
        __props__.__dict__["logo_url"] = logo_url
        __props__.__dict__["name"] = name
        __props__.__dict__["sign_on_mode"] = sign_on_mode
        __props__.__dict__["status"] = status
        __props__.__dict__["url"] = url
        return BasicAuth(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessibilityErrorRedirectUrl")
    def accessibility_error_redirect_url(self) -> pulumi.Output[Optional[str]]:
        """
        Custom error page URL
        """
        return pulumi.get(self, "accessibility_error_redirect_url")

    @property
    @pulumi.getter(name="accessibilityLoginRedirectUrl")
    def accessibility_login_redirect_url(self) -> pulumi.Output[Optional[str]]:
        """
        Custom login page URL
        """
        return pulumi.get(self, "accessibility_login_redirect_url")

    @property
    @pulumi.getter(name="accessibilitySelfService")
    def accessibility_self_service(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable self service. Default is `false`
        """
        return pulumi.get(self, "accessibility_self_service")

    @property
    @pulumi.getter(name="adminNote")
    def admin_note(self) -> pulumi.Output[Optional[str]]:
        """
        Application notes for admins.
        """
        return pulumi.get(self, "admin_note")

    @property
    @pulumi.getter(name="appLinksJson")
    def app_links_json(self) -> pulumi.Output[Optional[str]]:
        """
        Displays specific appLinks for the app. The value for each application link should be boolean.
        """
        return pulumi.get(self, "app_links_json")

    @property
    @pulumi.getter(name="authUrl")
    def auth_url(self) -> pulumi.Output[str]:
        """
        The URL of the authenticating site for this app.
        """
        return pulumi.get(self, "auth_url")

    @property
    @pulumi.getter(name="autoSubmitToolbar")
    def auto_submit_toolbar(self) -> pulumi.Output[Optional[bool]]:
        """
        Display auto submit toolbar
        """
        return pulumi.get(self, "auto_submit_toolbar")

    @property
    @pulumi.getter(name="enduserNote")
    def enduser_note(self) -> pulumi.Output[Optional[str]]:
        """
        Application notes for end users.
        """
        return pulumi.get(self, "enduser_note")

    @property
    @pulumi.getter(name="hideIos")
    def hide_ios(self) -> pulumi.Output[Optional[bool]]:
        """
        Do not display application icon on mobile app
        """
        return pulumi.get(self, "hide_ios")

    @property
    @pulumi.getter(name="hideWeb")
    def hide_web(self) -> pulumi.Output[Optional[bool]]:
        """
        Do not display application icon to users
        """
        return pulumi.get(self, "hide_web")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        The Application's display name.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def logo(self) -> pulumi.Output[Optional[str]]:
        """
        Local file path to the logo. The file must be in PNG, JPG, or GIF format, and less than 1 MB in size.
        """
        return pulumi.get(self, "logo")

    @property
    @pulumi.getter(name="logoUrl")
    def logo_url(self) -> pulumi.Output[str]:
        """
        URL of the application's logo
        """
        return pulumi.get(self, "logo_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the app.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="signOnMode")
    def sign_on_mode(self) -> pulumi.Output[str]:
        """
        Sign on mode of application.
        """
        return pulumi.get(self, "sign_on_mode")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Status of application. By default, it is `ACTIVE`
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL of the sign-in page for this app.
        """
        return pulumi.get(self, "url")

