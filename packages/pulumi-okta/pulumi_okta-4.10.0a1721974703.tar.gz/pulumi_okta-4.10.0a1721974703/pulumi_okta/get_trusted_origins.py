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

__all__ = [
    'GetTrustedOriginsResult',
    'AwaitableGetTrustedOriginsResult',
    'get_trusted_origins',
    'get_trusted_origins_output',
]

@pulumi.output_type
class GetTrustedOriginsResult:
    """
    A collection of values returned by getTrustedOrigins.
    """
    def __init__(__self__, filter=None, id=None, trusted_origins=None):
        if filter and not isinstance(filter, str):
            raise TypeError("Expected argument 'filter' to be a str")
        pulumi.set(__self__, "filter", filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if trusted_origins and not isinstance(trusted_origins, list):
            raise TypeError("Expected argument 'trusted_origins' to be a list")
        pulumi.set(__self__, "trusted_origins", trusted_origins)

    @property
    @pulumi.getter
    def filter(self) -> Optional[str]:
        """
        Filter criteria. Filter value will be URL-encoded by the provider
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="trustedOrigins")
    def trusted_origins(self) -> Sequence['outputs.GetTrustedOriginsTrustedOriginResult']:
        return pulumi.get(self, "trusted_origins")


class AwaitableGetTrustedOriginsResult(GetTrustedOriginsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrustedOriginsResult(
            filter=self.filter,
            id=self.id,
            trusted_origins=self.trusted_origins)


def get_trusted_origins(filter: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrustedOriginsResult:
    """
    Get List of Trusted Origins using filters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    all = okta.get_trusted_origins()
    ```


    :param str filter: Filter criteria. Filter value will be URL-encoded by the provider
    """
    __args__ = dict()
    __args__['filter'] = filter
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:index/getTrustedOrigins:getTrustedOrigins', __args__, opts=opts, typ=GetTrustedOriginsResult).value

    return AwaitableGetTrustedOriginsResult(
        filter=pulumi.get(__ret__, 'filter'),
        id=pulumi.get(__ret__, 'id'),
        trusted_origins=pulumi.get(__ret__, 'trusted_origins'))


@_utilities.lift_output_func(get_trusted_origins)
def get_trusted_origins_output(filter: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrustedOriginsResult]:
    """
    Get List of Trusted Origins using filters.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    all = okta.get_trusted_origins()
    ```


    :param str filter: Filter criteria. Filter value will be URL-encoded by the provider
    """
    ...
