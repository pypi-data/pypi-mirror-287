# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetRoleSubscriptionResult',
    'AwaitableGetRoleSubscriptionResult',
    'get_role_subscription',
    'get_role_subscription_output',
]

@pulumi.output_type
class GetRoleSubscriptionResult:
    """
    A collection of values returned by getRoleSubscription.
    """
    def __init__(__self__, id=None, notification_type=None, role_type=None, status=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if notification_type and not isinstance(notification_type, str):
            raise TypeError("Expected argument 'notification_type' to be a str")
        pulumi.set(__self__, "notification_type", notification_type)
        if role_type and not isinstance(role_type, str):
            raise TypeError("Expected argument 'role_type' to be a str")
        pulumi.set(__self__, "role_type", role_type)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> str:
        """
        Type of the notification
        """
        return pulumi.get(self, "notification_type")

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> str:
        """
        Type of the role
        """
        return pulumi.get(self, "role_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of subscription
        """
        return pulumi.get(self, "status")


class AwaitableGetRoleSubscriptionResult(GetRoleSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleSubscriptionResult(
            id=self.id,
            notification_type=self.notification_type,
            role_type=self.role_type,
            status=self.status)


def get_role_subscription(notification_type: Optional[str] = None,
                          role_type: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleSubscriptionResult:
    """
    Get subscriptions of a Role with a specific type

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.get_role_subscription(notification_type="APP_IMPORT",
        role_type="SUPER_ADMIN")
    ```


    :param str notification_type: Type of the notification
    :param str role_type: Type of the role
    """
    __args__ = dict()
    __args__['notificationType'] = notification_type
    __args__['roleType'] = role_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:index/getRoleSubscription:getRoleSubscription', __args__, opts=opts, typ=GetRoleSubscriptionResult).value

    return AwaitableGetRoleSubscriptionResult(
        id=pulumi.get(__ret__, 'id'),
        notification_type=pulumi.get(__ret__, 'notification_type'),
        role_type=pulumi.get(__ret__, 'role_type'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_role_subscription)
def get_role_subscription_output(notification_type: Optional[pulumi.Input[str]] = None,
                                 role_type: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleSubscriptionResult]:
    """
    Get subscriptions of a Role with a specific type

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.get_role_subscription(notification_type="APP_IMPORT",
        role_type="SUPER_ADMIN")
    ```


    :param str notification_type: Type of the notification
    :param str role_type: Type of the role
    """
    ...
