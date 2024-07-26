# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['OrgConfigurationArgs', 'OrgConfiguration']

@pulumi.input_type
class OrgConfigurationArgs:
    def __init__(__self__, *,
                 company_name: pulumi.Input[str],
                 address1: Optional[pulumi.Input[str]] = None,
                 address2: Optional[pulumi.Input[str]] = None,
                 billing_contact_user: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 end_user_support_help_url: Optional[pulumi.Input[str]] = None,
                 logo: Optional[pulumi.Input[str]] = None,
                 opt_out_communication_emails: Optional[pulumi.Input[bool]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 support_phone_number: Optional[pulumi.Input[str]] = None,
                 technical_contact_user: Optional[pulumi.Input[str]] = None,
                 website: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OrgConfiguration resource.
        :param pulumi.Input[str] company_name: Name of org
        :param pulumi.Input[str] address1: Primary address of org
        :param pulumi.Input[str] address2: Secondary address of org
        :param pulumi.Input[str] billing_contact_user: User ID representing the billing contact
        :param pulumi.Input[str] city: City of org
        :param pulumi.Input[str] country: Country of org
        :param pulumi.Input[str] end_user_support_help_url: Support link of org
        :param pulumi.Input[str] logo: Logo of org. The file must be in PNG, JPG, or GIF format and less than 1 MB in size. For best results use landscape orientation, a transparent background, and a minimum size of 420px by 120px to prevent upscaling.
        :param pulumi.Input[bool] opt_out_communication_emails: Indicates whether the org's users receive Okta Communication emails
        :param pulumi.Input[str] phone_number: Support help phone of org
        :param pulumi.Input[str] postal_code: Postal code of org
        :param pulumi.Input[str] state: State of org
        :param pulumi.Input[str] support_phone_number: Support help phone of org
        :param pulumi.Input[str] technical_contact_user: User ID representing the technical contact
        :param pulumi.Input[str] website: The org's website
        """
        pulumi.set(__self__, "company_name", company_name)
        if address1 is not None:
            pulumi.set(__self__, "address1", address1)
        if address2 is not None:
            pulumi.set(__self__, "address2", address2)
        if billing_contact_user is not None:
            pulumi.set(__self__, "billing_contact_user", billing_contact_user)
        if city is not None:
            pulumi.set(__self__, "city", city)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if end_user_support_help_url is not None:
            pulumi.set(__self__, "end_user_support_help_url", end_user_support_help_url)
        if logo is not None:
            pulumi.set(__self__, "logo", logo)
        if opt_out_communication_emails is not None:
            pulumi.set(__self__, "opt_out_communication_emails", opt_out_communication_emails)
        if phone_number is not None:
            pulumi.set(__self__, "phone_number", phone_number)
        if postal_code is not None:
            pulumi.set(__self__, "postal_code", postal_code)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if support_phone_number is not None:
            pulumi.set(__self__, "support_phone_number", support_phone_number)
        if technical_contact_user is not None:
            pulumi.set(__self__, "technical_contact_user", technical_contact_user)
        if website is not None:
            pulumi.set(__self__, "website", website)

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> pulumi.Input[str]:
        """
        Name of org
        """
        return pulumi.get(self, "company_name")

    @company_name.setter
    def company_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "company_name", value)

    @property
    @pulumi.getter
    def address1(self) -> Optional[pulumi.Input[str]]:
        """
        Primary address of org
        """
        return pulumi.get(self, "address1")

    @address1.setter
    def address1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address1", value)

    @property
    @pulumi.getter
    def address2(self) -> Optional[pulumi.Input[str]]:
        """
        Secondary address of org
        """
        return pulumi.get(self, "address2")

    @address2.setter
    def address2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address2", value)

    @property
    @pulumi.getter(name="billingContactUser")
    def billing_contact_user(self) -> Optional[pulumi.Input[str]]:
        """
        User ID representing the billing contact
        """
        return pulumi.get(self, "billing_contact_user")

    @billing_contact_user.setter
    def billing_contact_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_contact_user", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        City of org
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        Country of org
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter(name="endUserSupportHelpUrl")
    def end_user_support_help_url(self) -> Optional[pulumi.Input[str]]:
        """
        Support link of org
        """
        return pulumi.get(self, "end_user_support_help_url")

    @end_user_support_help_url.setter
    def end_user_support_help_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_user_support_help_url", value)

    @property
    @pulumi.getter
    def logo(self) -> Optional[pulumi.Input[str]]:
        """
        Logo of org. The file must be in PNG, JPG, or GIF format and less than 1 MB in size. For best results use landscape orientation, a transparent background, and a minimum size of 420px by 120px to prevent upscaling.
        """
        return pulumi.get(self, "logo")

    @logo.setter
    def logo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logo", value)

    @property
    @pulumi.getter(name="optOutCommunicationEmails")
    def opt_out_communication_emails(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the org's users receive Okta Communication emails
        """
        return pulumi.get(self, "opt_out_communication_emails")

    @opt_out_communication_emails.setter
    def opt_out_communication_emails(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "opt_out_communication_emails", value)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[str]]:
        """
        Support help phone of org
        """
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone_number", value)

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[str]]:
        """
        Postal code of org
        """
        return pulumi.get(self, "postal_code")

    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "postal_code", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of org
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="supportPhoneNumber")
    def support_phone_number(self) -> Optional[pulumi.Input[str]]:
        """
        Support help phone of org
        """
        return pulumi.get(self, "support_phone_number")

    @support_phone_number.setter
    def support_phone_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "support_phone_number", value)

    @property
    @pulumi.getter(name="technicalContactUser")
    def technical_contact_user(self) -> Optional[pulumi.Input[str]]:
        """
        User ID representing the technical contact
        """
        return pulumi.get(self, "technical_contact_user")

    @technical_contact_user.setter
    def technical_contact_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "technical_contact_user", value)

    @property
    @pulumi.getter
    def website(self) -> Optional[pulumi.Input[str]]:
        """
        The org's website
        """
        return pulumi.get(self, "website")

    @website.setter
    def website(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "website", value)


@pulumi.input_type
class _OrgConfigurationState:
    def __init__(__self__, *,
                 address1: Optional[pulumi.Input[str]] = None,
                 address2: Optional[pulumi.Input[str]] = None,
                 billing_contact_user: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 company_name: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 end_user_support_help_url: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 logo: Optional[pulumi.Input[str]] = None,
                 opt_out_communication_emails: Optional[pulumi.Input[bool]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
                 support_phone_number: Optional[pulumi.Input[str]] = None,
                 technical_contact_user: Optional[pulumi.Input[str]] = None,
                 website: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OrgConfiguration resources.
        :param pulumi.Input[str] address1: Primary address of org
        :param pulumi.Input[str] address2: Secondary address of org
        :param pulumi.Input[str] billing_contact_user: User ID representing the billing contact
        :param pulumi.Input[str] city: City of org
        :param pulumi.Input[str] company_name: Name of org
        :param pulumi.Input[str] country: Country of org
        :param pulumi.Input[str] end_user_support_help_url: Support link of org
        :param pulumi.Input[str] expires_at: Expiration of org
        :param pulumi.Input[str] logo: Logo of org. The file must be in PNG, JPG, or GIF format and less than 1 MB in size. For best results use landscape orientation, a transparent background, and a minimum size of 420px by 120px to prevent upscaling.
        :param pulumi.Input[bool] opt_out_communication_emails: Indicates whether the org's users receive Okta Communication emails
        :param pulumi.Input[str] phone_number: Support help phone of org
        :param pulumi.Input[str] postal_code: Postal code of org
        :param pulumi.Input[str] state: State of org
        :param pulumi.Input[str] subdomain: Subdomain of org
        :param pulumi.Input[str] support_phone_number: Support help phone of org
        :param pulumi.Input[str] technical_contact_user: User ID representing the technical contact
        :param pulumi.Input[str] website: The org's website
        """
        if address1 is not None:
            pulumi.set(__self__, "address1", address1)
        if address2 is not None:
            pulumi.set(__self__, "address2", address2)
        if billing_contact_user is not None:
            pulumi.set(__self__, "billing_contact_user", billing_contact_user)
        if city is not None:
            pulumi.set(__self__, "city", city)
        if company_name is not None:
            pulumi.set(__self__, "company_name", company_name)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if end_user_support_help_url is not None:
            pulumi.set(__self__, "end_user_support_help_url", end_user_support_help_url)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if logo is not None:
            pulumi.set(__self__, "logo", logo)
        if opt_out_communication_emails is not None:
            pulumi.set(__self__, "opt_out_communication_emails", opt_out_communication_emails)
        if phone_number is not None:
            pulumi.set(__self__, "phone_number", phone_number)
        if postal_code is not None:
            pulumi.set(__self__, "postal_code", postal_code)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if subdomain is not None:
            pulumi.set(__self__, "subdomain", subdomain)
        if support_phone_number is not None:
            pulumi.set(__self__, "support_phone_number", support_phone_number)
        if technical_contact_user is not None:
            pulumi.set(__self__, "technical_contact_user", technical_contact_user)
        if website is not None:
            pulumi.set(__self__, "website", website)

    @property
    @pulumi.getter
    def address1(self) -> Optional[pulumi.Input[str]]:
        """
        Primary address of org
        """
        return pulumi.get(self, "address1")

    @address1.setter
    def address1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address1", value)

    @property
    @pulumi.getter
    def address2(self) -> Optional[pulumi.Input[str]]:
        """
        Secondary address of org
        """
        return pulumi.get(self, "address2")

    @address2.setter
    def address2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address2", value)

    @property
    @pulumi.getter(name="billingContactUser")
    def billing_contact_user(self) -> Optional[pulumi.Input[str]]:
        """
        User ID representing the billing contact
        """
        return pulumi.get(self, "billing_contact_user")

    @billing_contact_user.setter
    def billing_contact_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_contact_user", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        City of org
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of org
        """
        return pulumi.get(self, "company_name")

    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "company_name", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        """
        Country of org
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter(name="endUserSupportHelpUrl")
    def end_user_support_help_url(self) -> Optional[pulumi.Input[str]]:
        """
        Support link of org
        """
        return pulumi.get(self, "end_user_support_help_url")

    @end_user_support_help_url.setter
    def end_user_support_help_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_user_support_help_url", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        Expiration of org
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)

    @property
    @pulumi.getter
    def logo(self) -> Optional[pulumi.Input[str]]:
        """
        Logo of org. The file must be in PNG, JPG, or GIF format and less than 1 MB in size. For best results use landscape orientation, a transparent background, and a minimum size of 420px by 120px to prevent upscaling.
        """
        return pulumi.get(self, "logo")

    @logo.setter
    def logo(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logo", value)

    @property
    @pulumi.getter(name="optOutCommunicationEmails")
    def opt_out_communication_emails(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the org's users receive Okta Communication emails
        """
        return pulumi.get(self, "opt_out_communication_emails")

    @opt_out_communication_emails.setter
    def opt_out_communication_emails(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "opt_out_communication_emails", value)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[str]]:
        """
        Support help phone of org
        """
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone_number", value)

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[str]]:
        """
        Postal code of org
        """
        return pulumi.get(self, "postal_code")

    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "postal_code", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of org
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def subdomain(self) -> Optional[pulumi.Input[str]]:
        """
        Subdomain of org
        """
        return pulumi.get(self, "subdomain")

    @subdomain.setter
    def subdomain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdomain", value)

    @property
    @pulumi.getter(name="supportPhoneNumber")
    def support_phone_number(self) -> Optional[pulumi.Input[str]]:
        """
        Support help phone of org
        """
        return pulumi.get(self, "support_phone_number")

    @support_phone_number.setter
    def support_phone_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "support_phone_number", value)

    @property
    @pulumi.getter(name="technicalContactUser")
    def technical_contact_user(self) -> Optional[pulumi.Input[str]]:
        """
        User ID representing the technical contact
        """
        return pulumi.get(self, "technical_contact_user")

    @technical_contact_user.setter
    def technical_contact_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "technical_contact_user", value)

    @property
    @pulumi.getter
    def website(self) -> Optional[pulumi.Input[str]]:
        """
        The org's website
        """
        return pulumi.get(self, "website")

    @website.setter
    def website(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "website", value)


class OrgConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address1: Optional[pulumi.Input[str]] = None,
                 address2: Optional[pulumi.Input[str]] = None,
                 billing_contact_user: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 company_name: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 end_user_support_help_url: Optional[pulumi.Input[str]] = None,
                 logo: Optional[pulumi.Input[str]] = None,
                 opt_out_communication_emails: Optional[pulumi.Input[bool]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 support_phone_number: Optional[pulumi.Input[str]] = None,
                 technical_contact_user: Optional[pulumi.Input[str]] = None,
                 website: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages org settings, logo, support and communication.

        > **IMPORTANT:** You must specify all Org Setting properties when you update an org's profile. Any property not specified in the script will be deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.OrgConfiguration("example",
            company_name="Umbrella Corporation",
            website="https://terraform.io")
        ```

        ## Import

        ```sh
        $ pulumi import okta:index/orgConfiguration:OrgConfiguration example _
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address1: Primary address of org
        :param pulumi.Input[str] address2: Secondary address of org
        :param pulumi.Input[str] billing_contact_user: User ID representing the billing contact
        :param pulumi.Input[str] city: City of org
        :param pulumi.Input[str] company_name: Name of org
        :param pulumi.Input[str] country: Country of org
        :param pulumi.Input[str] end_user_support_help_url: Support link of org
        :param pulumi.Input[str] logo: Logo of org. The file must be in PNG, JPG, or GIF format and less than 1 MB in size. For best results use landscape orientation, a transparent background, and a minimum size of 420px by 120px to prevent upscaling.
        :param pulumi.Input[bool] opt_out_communication_emails: Indicates whether the org's users receive Okta Communication emails
        :param pulumi.Input[str] phone_number: Support help phone of org
        :param pulumi.Input[str] postal_code: Postal code of org
        :param pulumi.Input[str] state: State of org
        :param pulumi.Input[str] support_phone_number: Support help phone of org
        :param pulumi.Input[str] technical_contact_user: User ID representing the technical contact
        :param pulumi.Input[str] website: The org's website
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrgConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages org settings, logo, support and communication.

        > **IMPORTANT:** You must specify all Org Setting properties when you update an org's profile. Any property not specified in the script will be deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.OrgConfiguration("example",
            company_name="Umbrella Corporation",
            website="https://terraform.io")
        ```

        ## Import

        ```sh
        $ pulumi import okta:index/orgConfiguration:OrgConfiguration example _
        ```

        :param str resource_name: The name of the resource.
        :param OrgConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrgConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address1: Optional[pulumi.Input[str]] = None,
                 address2: Optional[pulumi.Input[str]] = None,
                 billing_contact_user: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 company_name: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 end_user_support_help_url: Optional[pulumi.Input[str]] = None,
                 logo: Optional[pulumi.Input[str]] = None,
                 opt_out_communication_emails: Optional[pulumi.Input[bool]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 support_phone_number: Optional[pulumi.Input[str]] = None,
                 technical_contact_user: Optional[pulumi.Input[str]] = None,
                 website: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrgConfigurationArgs.__new__(OrgConfigurationArgs)

            __props__.__dict__["address1"] = address1
            __props__.__dict__["address2"] = address2
            __props__.__dict__["billing_contact_user"] = billing_contact_user
            __props__.__dict__["city"] = city
            if company_name is None and not opts.urn:
                raise TypeError("Missing required property 'company_name'")
            __props__.__dict__["company_name"] = company_name
            __props__.__dict__["country"] = country
            __props__.__dict__["end_user_support_help_url"] = end_user_support_help_url
            __props__.__dict__["logo"] = logo
            __props__.__dict__["opt_out_communication_emails"] = opt_out_communication_emails
            __props__.__dict__["phone_number"] = phone_number
            __props__.__dict__["postal_code"] = postal_code
            __props__.__dict__["state"] = state
            __props__.__dict__["support_phone_number"] = support_phone_number
            __props__.__dict__["technical_contact_user"] = technical_contact_user
            __props__.__dict__["website"] = website
            __props__.__dict__["expires_at"] = None
            __props__.__dict__["subdomain"] = None
        super(OrgConfiguration, __self__).__init__(
            'okta:index/orgConfiguration:OrgConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address1: Optional[pulumi.Input[str]] = None,
            address2: Optional[pulumi.Input[str]] = None,
            billing_contact_user: Optional[pulumi.Input[str]] = None,
            city: Optional[pulumi.Input[str]] = None,
            company_name: Optional[pulumi.Input[str]] = None,
            country: Optional[pulumi.Input[str]] = None,
            end_user_support_help_url: Optional[pulumi.Input[str]] = None,
            expires_at: Optional[pulumi.Input[str]] = None,
            logo: Optional[pulumi.Input[str]] = None,
            opt_out_communication_emails: Optional[pulumi.Input[bool]] = None,
            phone_number: Optional[pulumi.Input[str]] = None,
            postal_code: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            subdomain: Optional[pulumi.Input[str]] = None,
            support_phone_number: Optional[pulumi.Input[str]] = None,
            technical_contact_user: Optional[pulumi.Input[str]] = None,
            website: Optional[pulumi.Input[str]] = None) -> 'OrgConfiguration':
        """
        Get an existing OrgConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address1: Primary address of org
        :param pulumi.Input[str] address2: Secondary address of org
        :param pulumi.Input[str] billing_contact_user: User ID representing the billing contact
        :param pulumi.Input[str] city: City of org
        :param pulumi.Input[str] company_name: Name of org
        :param pulumi.Input[str] country: Country of org
        :param pulumi.Input[str] end_user_support_help_url: Support link of org
        :param pulumi.Input[str] expires_at: Expiration of org
        :param pulumi.Input[str] logo: Logo of org. The file must be in PNG, JPG, or GIF format and less than 1 MB in size. For best results use landscape orientation, a transparent background, and a minimum size of 420px by 120px to prevent upscaling.
        :param pulumi.Input[bool] opt_out_communication_emails: Indicates whether the org's users receive Okta Communication emails
        :param pulumi.Input[str] phone_number: Support help phone of org
        :param pulumi.Input[str] postal_code: Postal code of org
        :param pulumi.Input[str] state: State of org
        :param pulumi.Input[str] subdomain: Subdomain of org
        :param pulumi.Input[str] support_phone_number: Support help phone of org
        :param pulumi.Input[str] technical_contact_user: User ID representing the technical contact
        :param pulumi.Input[str] website: The org's website
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OrgConfigurationState.__new__(_OrgConfigurationState)

        __props__.__dict__["address1"] = address1
        __props__.__dict__["address2"] = address2
        __props__.__dict__["billing_contact_user"] = billing_contact_user
        __props__.__dict__["city"] = city
        __props__.__dict__["company_name"] = company_name
        __props__.__dict__["country"] = country
        __props__.__dict__["end_user_support_help_url"] = end_user_support_help_url
        __props__.__dict__["expires_at"] = expires_at
        __props__.__dict__["logo"] = logo
        __props__.__dict__["opt_out_communication_emails"] = opt_out_communication_emails
        __props__.__dict__["phone_number"] = phone_number
        __props__.__dict__["postal_code"] = postal_code
        __props__.__dict__["state"] = state
        __props__.__dict__["subdomain"] = subdomain
        __props__.__dict__["support_phone_number"] = support_phone_number
        __props__.__dict__["technical_contact_user"] = technical_contact_user
        __props__.__dict__["website"] = website
        return OrgConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address1(self) -> pulumi.Output[Optional[str]]:
        """
        Primary address of org
        """
        return pulumi.get(self, "address1")

    @property
    @pulumi.getter
    def address2(self) -> pulumi.Output[Optional[str]]:
        """
        Secondary address of org
        """
        return pulumi.get(self, "address2")

    @property
    @pulumi.getter(name="billingContactUser")
    def billing_contact_user(self) -> pulumi.Output[Optional[str]]:
        """
        User ID representing the billing contact
        """
        return pulumi.get(self, "billing_contact_user")

    @property
    @pulumi.getter
    def city(self) -> pulumi.Output[Optional[str]]:
        """
        City of org
        """
        return pulumi.get(self, "city")

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> pulumi.Output[str]:
        """
        Name of org
        """
        return pulumi.get(self, "company_name")

    @property
    @pulumi.getter
    def country(self) -> pulumi.Output[Optional[str]]:
        """
        Country of org
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter(name="endUserSupportHelpUrl")
    def end_user_support_help_url(self) -> pulumi.Output[Optional[str]]:
        """
        Support link of org
        """
        return pulumi.get(self, "end_user_support_help_url")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[str]:
        """
        Expiration of org
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter
    def logo(self) -> pulumi.Output[Optional[str]]:
        """
        Logo of org. The file must be in PNG, JPG, or GIF format and less than 1 MB in size. For best results use landscape orientation, a transparent background, and a minimum size of 420px by 120px to prevent upscaling.
        """
        return pulumi.get(self, "logo")

    @property
    @pulumi.getter(name="optOutCommunicationEmails")
    def opt_out_communication_emails(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the org's users receive Okta Communication emails
        """
        return pulumi.get(self, "opt_out_communication_emails")

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Output[Optional[str]]:
        """
        Support help phone of org
        """
        return pulumi.get(self, "phone_number")

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> pulumi.Output[Optional[str]]:
        """
        Postal code of org
        """
        return pulumi.get(self, "postal_code")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        State of org
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def subdomain(self) -> pulumi.Output[str]:
        """
        Subdomain of org
        """
        return pulumi.get(self, "subdomain")

    @property
    @pulumi.getter(name="supportPhoneNumber")
    def support_phone_number(self) -> pulumi.Output[Optional[str]]:
        """
        Support help phone of org
        """
        return pulumi.get(self, "support_phone_number")

    @property
    @pulumi.getter(name="technicalContactUser")
    def technical_contact_user(self) -> pulumi.Output[Optional[str]]:
        """
        User ID representing the technical contact
        """
        return pulumi.get(self, "technical_contact_user")

    @property
    @pulumi.getter
    def website(self) -> pulumi.Output[Optional[str]]:
        """
        The org's website
        """
        return pulumi.get(self, "website")

