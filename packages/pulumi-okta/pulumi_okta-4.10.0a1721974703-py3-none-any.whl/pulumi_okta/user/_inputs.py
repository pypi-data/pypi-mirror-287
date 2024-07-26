# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'UserPasswordHashArgs',
    'GetUserSearchArgs',
    'GetUsersSearchArgs',
]

@pulumi.input_type
class UserPasswordHashArgs:
    def __init__(__self__, *,
                 algorithm: pulumi.Input[str],
                 value: pulumi.Input[str],
                 salt: Optional[pulumi.Input[str]] = None,
                 salt_order: Optional[pulumi.Input[str]] = None,
                 work_factor: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] algorithm: The algorithm used to generate the hash using the password
        :param pulumi.Input[str] value: For SHA-512, SHA-256, SHA-1, MD5, This is the actual base64-encoded hash of the password (and salt, if used). This is the Base64 encoded value of the SHA-512/SHA-256/SHA-1/MD5 digest that was computed by either pre-fixing or post-fixing the salt to the password, depending on the saltOrder. If a salt was not used in the source system, then this should just be the the Base64 encoded value of the password's SHA-512/SHA-256/SHA-1/MD5 digest. For BCRYPT, This is the actual radix64-encoded hashed password.
        :param pulumi.Input[str] salt: Only required for salted hashes
        :param pulumi.Input[str] salt_order: Specifies whether salt was pre- or postfixed to the password before hashing
        :param pulumi.Input[int] work_factor: Governs the strength of the hash and the time required to compute it. Only required for BCRYPT algorithm
        """
        pulumi.set(__self__, "algorithm", algorithm)
        pulumi.set(__self__, "value", value)
        if salt is not None:
            pulumi.set(__self__, "salt", salt)
        if salt_order is not None:
            pulumi.set(__self__, "salt_order", salt_order)
        if work_factor is not None:
            pulumi.set(__self__, "work_factor", work_factor)

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input[str]:
        """
        The algorithm used to generate the hash using the password
        """
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: pulumi.Input[str]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        For SHA-512, SHA-256, SHA-1, MD5, This is the actual base64-encoded hash of the password (and salt, if used). This is the Base64 encoded value of the SHA-512/SHA-256/SHA-1/MD5 digest that was computed by either pre-fixing or post-fixing the salt to the password, depending on the saltOrder. If a salt was not used in the source system, then this should just be the the Base64 encoded value of the password's SHA-512/SHA-256/SHA-1/MD5 digest. For BCRYPT, This is the actual radix64-encoded hashed password.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def salt(self) -> Optional[pulumi.Input[str]]:
        """
        Only required for salted hashes
        """
        return pulumi.get(self, "salt")

    @salt.setter
    def salt(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "salt", value)

    @property
    @pulumi.getter(name="saltOrder")
    def salt_order(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether salt was pre- or postfixed to the password before hashing
        """
        return pulumi.get(self, "salt_order")

    @salt_order.setter
    def salt_order(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "salt_order", value)

    @property
    @pulumi.getter(name="workFactor")
    def work_factor(self) -> Optional[pulumi.Input[int]]:
        """
        Governs the strength of the hash and the time required to compute it. Only required for BCRYPT algorithm
        """
        return pulumi.get(self, "work_factor")

    @work_factor.setter
    def work_factor(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "work_factor", value)


@pulumi.input_type
class GetUserSearchArgs:
    def __init__(__self__, *,
                 comparison: Optional[str] = None,
                 expression: Optional[str] = None,
                 name: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str expression: A raw search expression string. This requires the search feature be on. Please see Okta documentation on their filter API for users. https://developer.okta.com/docs/api/resources/users#list-users-with-search
        :param str name: Property name to search for. This requires the search feature be on. Please see Okta documentation on their filter API for users. https://developer.okta.com/docs/api/resources/users#list-users-with-search
        """
        if comparison is not None:
            pulumi.set(__self__, "comparison", comparison)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def comparison(self) -> Optional[str]:
        return pulumi.get(self, "comparison")

    @comparison.setter
    def comparison(self, value: Optional[str]):
        pulumi.set(self, "comparison", value)

    @property
    @pulumi.getter
    def expression(self) -> Optional[str]:
        """
        A raw search expression string. This requires the search feature be on. Please see Okta documentation on their filter API for users. https://developer.okta.com/docs/api/resources/users#list-users-with-search
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Property name to search for. This requires the search feature be on. Please see Okta documentation on their filter API for users. https://developer.okta.com/docs/api/resources/users#list-users-with-search
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class GetUsersSearchArgs:
    def __init__(__self__, *,
                 comparison: Optional[str] = None,
                 expression: Optional[str] = None,
                 name: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str expression: A raw search expression string. This requires the search feature be on. Please see Okta documentation on their filter API for users. https://developer.okta.com/docs/api/resources/users#list-users-with-search
        :param str name: Property name to search for. This requires the search feature be on. Please see Okta documentation on their filter API for users. https://developer.okta.com/docs/api/resources/users#list-users-with-search
        """
        if comparison is not None:
            pulumi.set(__self__, "comparison", comparison)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def comparison(self) -> Optional[str]:
        return pulumi.get(self, "comparison")

    @comparison.setter
    def comparison(self, value: Optional[str]):
        pulumi.set(self, "comparison", value)

    @property
    @pulumi.getter
    def expression(self) -> Optional[str]:
        """
        A raw search expression string. This requires the search feature be on. Please see Okta documentation on their filter API for users. https://developer.okta.com/docs/api/resources/users#list-users-with-search
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Property name to search for. This requires the search feature be on. Please see Okta documentation on their filter API for users. https://developer.okta.com/docs/api/resources/users#list-users-with-search
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[str]):
        pulumi.set(self, "value", value)


