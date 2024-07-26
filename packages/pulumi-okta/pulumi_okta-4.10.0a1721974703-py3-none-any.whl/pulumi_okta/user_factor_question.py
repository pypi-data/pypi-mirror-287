# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UserFactorQuestionArgs', 'UserFactorQuestion']

@pulumi.input_type
class UserFactorQuestionArgs:
    def __init__(__self__, *,
                 answer: pulumi.Input[str],
                 key: pulumi.Input[str],
                 user_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a UserFactorQuestion resource.
        :param pulumi.Input[str] answer: Security question answer. Note here that answer won't be set during the resource import.
        :param pulumi.Input[str] key: Security question unique key.
        :param pulumi.Input[str] user_id: ID of the user. Resource will be recreated when `user_id` changes.
        """
        pulumi.set(__self__, "answer", answer)
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter
    def answer(self) -> pulumi.Input[str]:
        """
        Security question answer. Note here that answer won't be set during the resource import.
        """
        return pulumi.get(self, "answer")

    @answer.setter
    def answer(self, value: pulumi.Input[str]):
        pulumi.set(self, "answer", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Security question unique key.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        ID of the user. Resource will be recreated when `user_id` changes.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)


@pulumi.input_type
class _UserFactorQuestionState:
    def __init__(__self__, *,
                 answer: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 text: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserFactorQuestion resources.
        :param pulumi.Input[str] answer: Security question answer. Note here that answer won't be set during the resource import.
        :param pulumi.Input[str] key: Security question unique key.
        :param pulumi.Input[str] status: The status of the security question factor.
        :param pulumi.Input[str] text: Display text for security question.
        :param pulumi.Input[str] user_id: ID of the user. Resource will be recreated when `user_id` changes.
        """
        if answer is not None:
            pulumi.set(__self__, "answer", answer)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if text is not None:
            pulumi.set(__self__, "text", text)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter
    def answer(self) -> Optional[pulumi.Input[str]]:
        """
        Security question answer. Note here that answer won't be set during the resource import.
        """
        return pulumi.get(self, "answer")

    @answer.setter
    def answer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "answer", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Security question unique key.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the security question factor.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[str]]:
        """
        Display text for security question.
        """
        return pulumi.get(self, "text")

    @text.setter
    def text(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "text", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the user. Resource will be recreated when `user_id` changes.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class UserFactorQuestion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 answer: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates security question factor for a user. This resource allows you to create and configure security question factor for a user.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example_user = okta.user.User("example",
            first_name="John",
            last_name="Smith",
            login="john.smith@example.com",
            email="john.smith@example.com")
        example = okta.get_user_security_questions_output(user_id=example_user.id)
        example_factor = okta.factor.Factor("example",
            provider_id="okta_question",
            active=True)
        example_user_factor_question = okta.UserFactorQuestion("example",
            user_id=example_user.id,
            key=example.questions[0].key,
            answer="meatball",
            opts = pulumi.ResourceOptions(depends_on=[example_factor]))
        ```

        ## Import

        ```sh
        $ pulumi import okta:index/userFactorQuestion:UserFactorQuestion example &#60;user id&#62;/&#60;question factor id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] answer: Security question answer. Note here that answer won't be set during the resource import.
        :param pulumi.Input[str] key: Security question unique key.
        :param pulumi.Input[str] user_id: ID of the user. Resource will be recreated when `user_id` changes.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserFactorQuestionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates security question factor for a user. This resource allows you to create and configure security question factor for a user.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example_user = okta.user.User("example",
            first_name="John",
            last_name="Smith",
            login="john.smith@example.com",
            email="john.smith@example.com")
        example = okta.get_user_security_questions_output(user_id=example_user.id)
        example_factor = okta.factor.Factor("example",
            provider_id="okta_question",
            active=True)
        example_user_factor_question = okta.UserFactorQuestion("example",
            user_id=example_user.id,
            key=example.questions[0].key,
            answer="meatball",
            opts = pulumi.ResourceOptions(depends_on=[example_factor]))
        ```

        ## Import

        ```sh
        $ pulumi import okta:index/userFactorQuestion:UserFactorQuestion example &#60;user id&#62;/&#60;question factor id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param UserFactorQuestionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserFactorQuestionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 answer: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserFactorQuestionArgs.__new__(UserFactorQuestionArgs)

            if answer is None and not opts.urn:
                raise TypeError("Missing required property 'answer'")
            __props__.__dict__["answer"] = None if answer is None else pulumi.Output.secret(answer)
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["status"] = None
            __props__.__dict__["text"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["answer"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(UserFactorQuestion, __self__).__init__(
            'okta:index/userFactorQuestion:UserFactorQuestion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            answer: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            text: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'UserFactorQuestion':
        """
        Get an existing UserFactorQuestion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] answer: Security question answer. Note here that answer won't be set during the resource import.
        :param pulumi.Input[str] key: Security question unique key.
        :param pulumi.Input[str] status: The status of the security question factor.
        :param pulumi.Input[str] text: Display text for security question.
        :param pulumi.Input[str] user_id: ID of the user. Resource will be recreated when `user_id` changes.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserFactorQuestionState.__new__(_UserFactorQuestionState)

        __props__.__dict__["answer"] = answer
        __props__.__dict__["key"] = key
        __props__.__dict__["status"] = status
        __props__.__dict__["text"] = text
        __props__.__dict__["user_id"] = user_id
        return UserFactorQuestion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def answer(self) -> pulumi.Output[str]:
        """
        Security question answer. Note here that answer won't be set during the resource import.
        """
        return pulumi.get(self, "answer")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        Security question unique key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the security question factor.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def text(self) -> pulumi.Output[str]:
        """
        Display text for security question.
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        ID of the user. Resource will be recreated when `user_id` changes.
        """
        return pulumi.get(self, "user_id")

