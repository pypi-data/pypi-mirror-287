# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['BrandArgs', 'Brand']

@pulumi.input_type
class BrandArgs:
    def __init__(__self__, *,
                 agree_to_custom_privacy_policy: Optional[pulumi.Input[bool]] = None,
                 brand_id: Optional[pulumi.Input[str]] = None,
                 custom_privacy_policy_url: Optional[pulumi.Input[str]] = None,
                 default_app_app_instance_id: Optional[pulumi.Input[str]] = None,
                 default_app_app_link_name: Optional[pulumi.Input[str]] = None,
                 default_app_classic_application_uri: Optional[pulumi.Input[str]] = None,
                 locale: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remove_powered_by_okta: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Brand resource.
        :param pulumi.Input[bool] agree_to_custom_privacy_policy: Is a required input flag with when changing custom*privacy*url, shouldn't be considered as a readable property
        :param pulumi.Input[str] brand_id: Brand ID - Note: Okta API for brands only reads and updates therefore the okta*brand resource needs to act as a quasi data source. Do this by setting brand*id. `DEPRECATED`: Okta has fully support brand creation, this attribute is a no op and will be removed
        :param pulumi.Input[str] custom_privacy_policy_url: Custom privacy policy URL
        :param pulumi.Input[str] default_app_app_instance_id: Default app app instance id
        :param pulumi.Input[str] default_app_app_link_name: Default app app link name
        :param pulumi.Input[str] default_app_classic_application_uri: Default app classic application uri
        :param pulumi.Input[str] locale: The language specified as an IETF BCP 47 language tag
        :param pulumi.Input[str] name: Name of the brand
        :param pulumi.Input[bool] remove_powered_by_okta: Removes "Powered by Okta" from the Okta-hosted sign-in page and "© 2021 Okta, Inc." from the Okta End-User Dashboard
        """
        if agree_to_custom_privacy_policy is not None:
            pulumi.set(__self__, "agree_to_custom_privacy_policy", agree_to_custom_privacy_policy)
        if brand_id is not None:
            warnings.warn("""Okta has fully support brand creation, this attribute is a no op and will be removed""", DeprecationWarning)
            pulumi.log.warn("""brand_id is deprecated: Okta has fully support brand creation, this attribute is a no op and will be removed""")
        if brand_id is not None:
            pulumi.set(__self__, "brand_id", brand_id)
        if custom_privacy_policy_url is not None:
            pulumi.set(__self__, "custom_privacy_policy_url", custom_privacy_policy_url)
        if default_app_app_instance_id is not None:
            pulumi.set(__self__, "default_app_app_instance_id", default_app_app_instance_id)
        if default_app_app_link_name is not None:
            pulumi.set(__self__, "default_app_app_link_name", default_app_app_link_name)
        if default_app_classic_application_uri is not None:
            pulumi.set(__self__, "default_app_classic_application_uri", default_app_classic_application_uri)
        if locale is not None:
            pulumi.set(__self__, "locale", locale)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if remove_powered_by_okta is not None:
            pulumi.set(__self__, "remove_powered_by_okta", remove_powered_by_okta)

    @property
    @pulumi.getter(name="agreeToCustomPrivacyPolicy")
    def agree_to_custom_privacy_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Is a required input flag with when changing custom*privacy*url, shouldn't be considered as a readable property
        """
        return pulumi.get(self, "agree_to_custom_privacy_policy")

    @agree_to_custom_privacy_policy.setter
    def agree_to_custom_privacy_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "agree_to_custom_privacy_policy", value)

    @property
    @pulumi.getter(name="brandId")
    @_utilities.deprecated("""Okta has fully support brand creation, this attribute is a no op and will be removed""")
    def brand_id(self) -> Optional[pulumi.Input[str]]:
        """
        Brand ID - Note: Okta API for brands only reads and updates therefore the okta*brand resource needs to act as a quasi data source. Do this by setting brand*id. `DEPRECATED`: Okta has fully support brand creation, this attribute is a no op and will be removed
        """
        return pulumi.get(self, "brand_id")

    @brand_id.setter
    def brand_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "brand_id", value)

    @property
    @pulumi.getter(name="customPrivacyPolicyUrl")
    def custom_privacy_policy_url(self) -> Optional[pulumi.Input[str]]:
        """
        Custom privacy policy URL
        """
        return pulumi.get(self, "custom_privacy_policy_url")

    @custom_privacy_policy_url.setter
    def custom_privacy_policy_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_privacy_policy_url", value)

    @property
    @pulumi.getter(name="defaultAppAppInstanceId")
    def default_app_app_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        Default app app instance id
        """
        return pulumi.get(self, "default_app_app_instance_id")

    @default_app_app_instance_id.setter
    def default_app_app_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_app_app_instance_id", value)

    @property
    @pulumi.getter(name="defaultAppAppLinkName")
    def default_app_app_link_name(self) -> Optional[pulumi.Input[str]]:
        """
        Default app app link name
        """
        return pulumi.get(self, "default_app_app_link_name")

    @default_app_app_link_name.setter
    def default_app_app_link_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_app_app_link_name", value)

    @property
    @pulumi.getter(name="defaultAppClassicApplicationUri")
    def default_app_classic_application_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Default app classic application uri
        """
        return pulumi.get(self, "default_app_classic_application_uri")

    @default_app_classic_application_uri.setter
    def default_app_classic_application_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_app_classic_application_uri", value)

    @property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[str]]:
        """
        The language specified as an IETF BCP 47 language tag
        """
        return pulumi.get(self, "locale")

    @locale.setter
    def locale(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "locale", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the brand
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="removePoweredByOkta")
    def remove_powered_by_okta(self) -> Optional[pulumi.Input[bool]]:
        """
        Removes "Powered by Okta" from the Okta-hosted sign-in page and "© 2021 Okta, Inc." from the Okta End-User Dashboard
        """
        return pulumi.get(self, "remove_powered_by_okta")

    @remove_powered_by_okta.setter
    def remove_powered_by_okta(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_powered_by_okta", value)


@pulumi.input_type
class _BrandState:
    def __init__(__self__, *,
                 agree_to_custom_privacy_policy: Optional[pulumi.Input[bool]] = None,
                 brand_id: Optional[pulumi.Input[str]] = None,
                 custom_privacy_policy_url: Optional[pulumi.Input[str]] = None,
                 default_app_app_instance_id: Optional[pulumi.Input[str]] = None,
                 default_app_app_link_name: Optional[pulumi.Input[str]] = None,
                 default_app_classic_application_uri: Optional[pulumi.Input[str]] = None,
                 email_domain_id: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 links: Optional[pulumi.Input[str]] = None,
                 locale: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remove_powered_by_okta: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Brand resources.
        :param pulumi.Input[bool] agree_to_custom_privacy_policy: Is a required input flag with when changing custom*privacy*url, shouldn't be considered as a readable property
        :param pulumi.Input[str] brand_id: Brand ID - Note: Okta API for brands only reads and updates therefore the okta*brand resource needs to act as a quasi data source. Do this by setting brand*id. `DEPRECATED`: Okta has fully support brand creation, this attribute is a no op and will be removed
        :param pulumi.Input[str] custom_privacy_policy_url: Custom privacy policy URL
        :param pulumi.Input[str] default_app_app_instance_id: Default app app instance id
        :param pulumi.Input[str] default_app_app_link_name: Default app app link name
        :param pulumi.Input[str] default_app_classic_application_uri: Default app classic application uri
        :param pulumi.Input[str] email_domain_id: Email Domain ID tied to this brand
        :param pulumi.Input[bool] is_default: Is this the default brand
        :param pulumi.Input[str] links: Link relations for this object - JSON HAL - Discoverable resources related to the brand
        :param pulumi.Input[str] locale: The language specified as an IETF BCP 47 language tag
        :param pulumi.Input[str] name: Name of the brand
        :param pulumi.Input[bool] remove_powered_by_okta: Removes "Powered by Okta" from the Okta-hosted sign-in page and "© 2021 Okta, Inc." from the Okta End-User Dashboard
        """
        if agree_to_custom_privacy_policy is not None:
            pulumi.set(__self__, "agree_to_custom_privacy_policy", agree_to_custom_privacy_policy)
        if brand_id is not None:
            warnings.warn("""Okta has fully support brand creation, this attribute is a no op and will be removed""", DeprecationWarning)
            pulumi.log.warn("""brand_id is deprecated: Okta has fully support brand creation, this attribute is a no op and will be removed""")
        if brand_id is not None:
            pulumi.set(__self__, "brand_id", brand_id)
        if custom_privacy_policy_url is not None:
            pulumi.set(__self__, "custom_privacy_policy_url", custom_privacy_policy_url)
        if default_app_app_instance_id is not None:
            pulumi.set(__self__, "default_app_app_instance_id", default_app_app_instance_id)
        if default_app_app_link_name is not None:
            pulumi.set(__self__, "default_app_app_link_name", default_app_app_link_name)
        if default_app_classic_application_uri is not None:
            pulumi.set(__self__, "default_app_classic_application_uri", default_app_classic_application_uri)
        if email_domain_id is not None:
            pulumi.set(__self__, "email_domain_id", email_domain_id)
        if is_default is not None:
            pulumi.set(__self__, "is_default", is_default)
        if links is not None:
            pulumi.set(__self__, "links", links)
        if locale is not None:
            pulumi.set(__self__, "locale", locale)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if remove_powered_by_okta is not None:
            pulumi.set(__self__, "remove_powered_by_okta", remove_powered_by_okta)

    @property
    @pulumi.getter(name="agreeToCustomPrivacyPolicy")
    def agree_to_custom_privacy_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Is a required input flag with when changing custom*privacy*url, shouldn't be considered as a readable property
        """
        return pulumi.get(self, "agree_to_custom_privacy_policy")

    @agree_to_custom_privacy_policy.setter
    def agree_to_custom_privacy_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "agree_to_custom_privacy_policy", value)

    @property
    @pulumi.getter(name="brandId")
    @_utilities.deprecated("""Okta has fully support brand creation, this attribute is a no op and will be removed""")
    def brand_id(self) -> Optional[pulumi.Input[str]]:
        """
        Brand ID - Note: Okta API for brands only reads and updates therefore the okta*brand resource needs to act as a quasi data source. Do this by setting brand*id. `DEPRECATED`: Okta has fully support brand creation, this attribute is a no op and will be removed
        """
        return pulumi.get(self, "brand_id")

    @brand_id.setter
    def brand_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "brand_id", value)

    @property
    @pulumi.getter(name="customPrivacyPolicyUrl")
    def custom_privacy_policy_url(self) -> Optional[pulumi.Input[str]]:
        """
        Custom privacy policy URL
        """
        return pulumi.get(self, "custom_privacy_policy_url")

    @custom_privacy_policy_url.setter
    def custom_privacy_policy_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_privacy_policy_url", value)

    @property
    @pulumi.getter(name="defaultAppAppInstanceId")
    def default_app_app_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        Default app app instance id
        """
        return pulumi.get(self, "default_app_app_instance_id")

    @default_app_app_instance_id.setter
    def default_app_app_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_app_app_instance_id", value)

    @property
    @pulumi.getter(name="defaultAppAppLinkName")
    def default_app_app_link_name(self) -> Optional[pulumi.Input[str]]:
        """
        Default app app link name
        """
        return pulumi.get(self, "default_app_app_link_name")

    @default_app_app_link_name.setter
    def default_app_app_link_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_app_app_link_name", value)

    @property
    @pulumi.getter(name="defaultAppClassicApplicationUri")
    def default_app_classic_application_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Default app classic application uri
        """
        return pulumi.get(self, "default_app_classic_application_uri")

    @default_app_classic_application_uri.setter
    def default_app_classic_application_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_app_classic_application_uri", value)

    @property
    @pulumi.getter(name="emailDomainId")
    def email_domain_id(self) -> Optional[pulumi.Input[str]]:
        """
        Email Domain ID tied to this brand
        """
        return pulumi.get(self, "email_domain_id")

    @email_domain_id.setter
    def email_domain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email_domain_id", value)

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[bool]]:
        """
        Is this the default brand
        """
        return pulumi.get(self, "is_default")

    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default", value)

    @property
    @pulumi.getter
    def links(self) -> Optional[pulumi.Input[str]]:
        """
        Link relations for this object - JSON HAL - Discoverable resources related to the brand
        """
        return pulumi.get(self, "links")

    @links.setter
    def links(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "links", value)

    @property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[str]]:
        """
        The language specified as an IETF BCP 47 language tag
        """
        return pulumi.get(self, "locale")

    @locale.setter
    def locale(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "locale", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the brand
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="removePoweredByOkta")
    def remove_powered_by_okta(self) -> Optional[pulumi.Input[bool]]:
        """
        Removes "Powered by Okta" from the Okta-hosted sign-in page and "© 2021 Okta, Inc." from the Okta End-User Dashboard
        """
        return pulumi.get(self, "remove_powered_by_okta")

    @remove_powered_by_okta.setter
    def remove_powered_by_okta(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_powered_by_okta", value)


class Brand(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agree_to_custom_privacy_policy: Optional[pulumi.Input[bool]] = None,
                 brand_id: Optional[pulumi.Input[str]] = None,
                 custom_privacy_policy_url: Optional[pulumi.Input[str]] = None,
                 default_app_app_instance_id: Optional[pulumi.Input[str]] = None,
                 default_app_app_link_name: Optional[pulumi.Input[str]] = None,
                 default_app_classic_application_uri: Optional[pulumi.Input[str]] = None,
                 locale: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remove_powered_by_okta: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.Brand("example", name="example")
        ```

        ## Import

        ```sh
        $ pulumi import okta:index/brand:Brand example &#60;brand id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] agree_to_custom_privacy_policy: Is a required input flag with when changing custom*privacy*url, shouldn't be considered as a readable property
        :param pulumi.Input[str] brand_id: Brand ID - Note: Okta API for brands only reads and updates therefore the okta*brand resource needs to act as a quasi data source. Do this by setting brand*id. `DEPRECATED`: Okta has fully support brand creation, this attribute is a no op and will be removed
        :param pulumi.Input[str] custom_privacy_policy_url: Custom privacy policy URL
        :param pulumi.Input[str] default_app_app_instance_id: Default app app instance id
        :param pulumi.Input[str] default_app_app_link_name: Default app app link name
        :param pulumi.Input[str] default_app_classic_application_uri: Default app classic application uri
        :param pulumi.Input[str] locale: The language specified as an IETF BCP 47 language tag
        :param pulumi.Input[str] name: Name of the brand
        :param pulumi.Input[bool] remove_powered_by_okta: Removes "Powered by Okta" from the Okta-hosted sign-in page and "© 2021 Okta, Inc." from the Okta End-User Dashboard
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[BrandArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.Brand("example", name="example")
        ```

        ## Import

        ```sh
        $ pulumi import okta:index/brand:Brand example &#60;brand id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param BrandArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BrandArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agree_to_custom_privacy_policy: Optional[pulumi.Input[bool]] = None,
                 brand_id: Optional[pulumi.Input[str]] = None,
                 custom_privacy_policy_url: Optional[pulumi.Input[str]] = None,
                 default_app_app_instance_id: Optional[pulumi.Input[str]] = None,
                 default_app_app_link_name: Optional[pulumi.Input[str]] = None,
                 default_app_classic_application_uri: Optional[pulumi.Input[str]] = None,
                 locale: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remove_powered_by_okta: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BrandArgs.__new__(BrandArgs)

            __props__.__dict__["agree_to_custom_privacy_policy"] = agree_to_custom_privacy_policy
            __props__.__dict__["brand_id"] = brand_id
            __props__.__dict__["custom_privacy_policy_url"] = custom_privacy_policy_url
            __props__.__dict__["default_app_app_instance_id"] = default_app_app_instance_id
            __props__.__dict__["default_app_app_link_name"] = default_app_app_link_name
            __props__.__dict__["default_app_classic_application_uri"] = default_app_classic_application_uri
            __props__.__dict__["locale"] = locale
            __props__.__dict__["name"] = name
            __props__.__dict__["remove_powered_by_okta"] = remove_powered_by_okta
            __props__.__dict__["email_domain_id"] = None
            __props__.__dict__["is_default"] = None
            __props__.__dict__["links"] = None
        super(Brand, __self__).__init__(
            'okta:index/brand:Brand',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            agree_to_custom_privacy_policy: Optional[pulumi.Input[bool]] = None,
            brand_id: Optional[pulumi.Input[str]] = None,
            custom_privacy_policy_url: Optional[pulumi.Input[str]] = None,
            default_app_app_instance_id: Optional[pulumi.Input[str]] = None,
            default_app_app_link_name: Optional[pulumi.Input[str]] = None,
            default_app_classic_application_uri: Optional[pulumi.Input[str]] = None,
            email_domain_id: Optional[pulumi.Input[str]] = None,
            is_default: Optional[pulumi.Input[bool]] = None,
            links: Optional[pulumi.Input[str]] = None,
            locale: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            remove_powered_by_okta: Optional[pulumi.Input[bool]] = None) -> 'Brand':
        """
        Get an existing Brand resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] agree_to_custom_privacy_policy: Is a required input flag with when changing custom*privacy*url, shouldn't be considered as a readable property
        :param pulumi.Input[str] brand_id: Brand ID - Note: Okta API for brands only reads and updates therefore the okta*brand resource needs to act as a quasi data source. Do this by setting brand*id. `DEPRECATED`: Okta has fully support brand creation, this attribute is a no op and will be removed
        :param pulumi.Input[str] custom_privacy_policy_url: Custom privacy policy URL
        :param pulumi.Input[str] default_app_app_instance_id: Default app app instance id
        :param pulumi.Input[str] default_app_app_link_name: Default app app link name
        :param pulumi.Input[str] default_app_classic_application_uri: Default app classic application uri
        :param pulumi.Input[str] email_domain_id: Email Domain ID tied to this brand
        :param pulumi.Input[bool] is_default: Is this the default brand
        :param pulumi.Input[str] links: Link relations for this object - JSON HAL - Discoverable resources related to the brand
        :param pulumi.Input[str] locale: The language specified as an IETF BCP 47 language tag
        :param pulumi.Input[str] name: Name of the brand
        :param pulumi.Input[bool] remove_powered_by_okta: Removes "Powered by Okta" from the Okta-hosted sign-in page and "© 2021 Okta, Inc." from the Okta End-User Dashboard
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BrandState.__new__(_BrandState)

        __props__.__dict__["agree_to_custom_privacy_policy"] = agree_to_custom_privacy_policy
        __props__.__dict__["brand_id"] = brand_id
        __props__.__dict__["custom_privacy_policy_url"] = custom_privacy_policy_url
        __props__.__dict__["default_app_app_instance_id"] = default_app_app_instance_id
        __props__.__dict__["default_app_app_link_name"] = default_app_app_link_name
        __props__.__dict__["default_app_classic_application_uri"] = default_app_classic_application_uri
        __props__.__dict__["email_domain_id"] = email_domain_id
        __props__.__dict__["is_default"] = is_default
        __props__.__dict__["links"] = links
        __props__.__dict__["locale"] = locale
        __props__.__dict__["name"] = name
        __props__.__dict__["remove_powered_by_okta"] = remove_powered_by_okta
        return Brand(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agreeToCustomPrivacyPolicy")
    def agree_to_custom_privacy_policy(self) -> pulumi.Output[bool]:
        """
        Is a required input flag with when changing custom*privacy*url, shouldn't be considered as a readable property
        """
        return pulumi.get(self, "agree_to_custom_privacy_policy")

    @property
    @pulumi.getter(name="brandId")
    @_utilities.deprecated("""Okta has fully support brand creation, this attribute is a no op and will be removed""")
    def brand_id(self) -> pulumi.Output[str]:
        """
        Brand ID - Note: Okta API for brands only reads and updates therefore the okta*brand resource needs to act as a quasi data source. Do this by setting brand*id. `DEPRECATED`: Okta has fully support brand creation, this attribute is a no op and will be removed
        """
        return pulumi.get(self, "brand_id")

    @property
    @pulumi.getter(name="customPrivacyPolicyUrl")
    def custom_privacy_policy_url(self) -> pulumi.Output[Optional[str]]:
        """
        Custom privacy policy URL
        """
        return pulumi.get(self, "custom_privacy_policy_url")

    @property
    @pulumi.getter(name="defaultAppAppInstanceId")
    def default_app_app_instance_id(self) -> pulumi.Output[Optional[str]]:
        """
        Default app app instance id
        """
        return pulumi.get(self, "default_app_app_instance_id")

    @property
    @pulumi.getter(name="defaultAppAppLinkName")
    def default_app_app_link_name(self) -> pulumi.Output[Optional[str]]:
        """
        Default app app link name
        """
        return pulumi.get(self, "default_app_app_link_name")

    @property
    @pulumi.getter(name="defaultAppClassicApplicationUri")
    def default_app_classic_application_uri(self) -> pulumi.Output[Optional[str]]:
        """
        Default app classic application uri
        """
        return pulumi.get(self, "default_app_classic_application_uri")

    @property
    @pulumi.getter(name="emailDomainId")
    def email_domain_id(self) -> pulumi.Output[str]:
        """
        Email Domain ID tied to this brand
        """
        return pulumi.get(self, "email_domain_id")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[bool]:
        """
        Is this the default brand
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter
    def links(self) -> pulumi.Output[str]:
        """
        Link relations for this object - JSON HAL - Discoverable resources related to the brand
        """
        return pulumi.get(self, "links")

    @property
    @pulumi.getter
    def locale(self) -> pulumi.Output[Optional[str]]:
        """
        The language specified as an IETF BCP 47 language tag
        """
        return pulumi.get(self, "locale")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the brand
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="removePoweredByOkta")
    def remove_powered_by_okta(self) -> pulumi.Output[bool]:
        """
        Removes "Powered by Okta" from the Okta-hosted sign-in page and "© 2021 Okta, Inc." from the Okta End-User Dashboard
        """
        return pulumi.get(self, "remove_powered_by_okta")

