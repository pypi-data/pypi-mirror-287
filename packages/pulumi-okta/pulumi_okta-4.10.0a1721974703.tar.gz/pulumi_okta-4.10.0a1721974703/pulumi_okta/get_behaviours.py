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
    'GetBehavioursResult',
    'AwaitableGetBehavioursResult',
    'get_behaviours',
    'get_behaviours_output',
]

@pulumi.output_type
class GetBehavioursResult:
    """
    A collection of values returned by getBehaviours.
    """
    def __init__(__self__, behaviors=None, id=None, q=None):
        if behaviors and not isinstance(behaviors, list):
            raise TypeError("Expected argument 'behaviors' to be a list")
        pulumi.set(__self__, "behaviors", behaviors)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if q and not isinstance(q, str):
            raise TypeError("Expected argument 'q' to be a str")
        pulumi.set(__self__, "q", q)

    @property
    @pulumi.getter
    def behaviors(self) -> Sequence['outputs.GetBehavioursBehaviorResult']:
        return pulumi.get(self, "behaviors")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def q(self) -> Optional[str]:
        """
        Searches the name property of behaviors for matching value
        """
        return pulumi.get(self, "q")


class AwaitableGetBehavioursResult(GetBehavioursResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBehavioursResult(
            behaviors=self.behaviors,
            id=self.id,
            q=self.q)


def get_behaviours(q: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBehavioursResult:
    """
    Get a behaviors by search criteria.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.get_behaviours(q="New")
    ```


    :param str q: Searches the name property of behaviors for matching value
    """
    __args__ = dict()
    __args__['q'] = q
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('okta:index/getBehaviours:getBehaviours', __args__, opts=opts, typ=GetBehavioursResult).value

    return AwaitableGetBehavioursResult(
        behaviors=pulumi.get(__ret__, 'behaviors'),
        id=pulumi.get(__ret__, 'id'),
        q=pulumi.get(__ret__, 'q'))


@_utilities.lift_output_func(get_behaviours)
def get_behaviours_output(q: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBehavioursResult]:
    """
    Get a behaviors by search criteria.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.get_behaviours(q="New")
    ```


    :param str q: Searches the name property of behaviors for matching value
    """
    ...
