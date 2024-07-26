# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ServerPolicyArgs', 'ServerPolicy']

@pulumi.input_type
class ServerPolicyArgs:
    def __init__(__self__, *,
                 auth_server_id: pulumi.Input[str],
                 client_whitelists: pulumi.Input[Sequence[pulumi.Input[str]]],
                 description: pulumi.Input[str],
                 priority: pulumi.Input[int],
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerPolicy resource.
        :param pulumi.Input[str] auth_server_id: The ID of the Auth Server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_whitelists: The clients to whitelist the policy for. `[ALL_CLIENTS]` is a special value that can be used to whitelist all clients, otherwise it is a list of client ids.
        :param pulumi.Input[str] description: The description of the Auth Server Policy.
        :param pulumi.Input[int] priority: Priority of the auth server policy
        :param pulumi.Input[str] name: The name of the Auth Server Policy.
        :param pulumi.Input[str] status: Default to `ACTIVE`
        """
        pulumi.set(__self__, "auth_server_id", auth_server_id)
        pulumi.set(__self__, "client_whitelists", client_whitelists)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "priority", priority)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="authServerId")
    def auth_server_id(self) -> pulumi.Input[str]:
        """
        The ID of the Auth Server.
        """
        return pulumi.get(self, "auth_server_id")

    @auth_server_id.setter
    def auth_server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "auth_server_id", value)

    @property
    @pulumi.getter(name="clientWhitelists")
    def client_whitelists(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The clients to whitelist the policy for. `[ALL_CLIENTS]` is a special value that can be used to whitelist all clients, otherwise it is a list of client ids.
        """
        return pulumi.get(self, "client_whitelists")

    @client_whitelists.setter
    def client_whitelists(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "client_whitelists", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the Auth Server Policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Input[int]:
        """
        Priority of the auth server policy
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Auth Server Policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Default to `ACTIVE`
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _ServerPolicyState:
    def __init__(__self__, *,
                 auth_server_id: Optional[pulumi.Input[str]] = None,
                 client_whitelists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServerPolicy resources.
        :param pulumi.Input[str] auth_server_id: The ID of the Auth Server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_whitelists: The clients to whitelist the policy for. `[ALL_CLIENTS]` is a special value that can be used to whitelist all clients, otherwise it is a list of client ids.
        :param pulumi.Input[str] description: The description of the Auth Server Policy.
        :param pulumi.Input[str] name: The name of the Auth Server Policy.
        :param pulumi.Input[int] priority: Priority of the auth server policy
        :param pulumi.Input[str] status: Default to `ACTIVE`
        """
        if auth_server_id is not None:
            pulumi.set(__self__, "auth_server_id", auth_server_id)
        if client_whitelists is not None:
            pulumi.set(__self__, "client_whitelists", client_whitelists)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="authServerId")
    def auth_server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Auth Server.
        """
        return pulumi.get(self, "auth_server_id")

    @auth_server_id.setter
    def auth_server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_server_id", value)

    @property
    @pulumi.getter(name="clientWhitelists")
    def client_whitelists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The clients to whitelist the policy for. `[ALL_CLIENTS]` is a special value that can be used to whitelist all clients, otherwise it is a list of client ids.
        """
        return pulumi.get(self, "client_whitelists")

    @client_whitelists.setter
    def client_whitelists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "client_whitelists", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Auth Server Policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Auth Server Policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority of the auth server policy
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Default to `ACTIVE`
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class ServerPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_server_id: Optional[pulumi.Input[str]] = None,
                 client_whitelists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an Authorization Server Policy. This resource allows you to create and configure an Authorization Server Policy.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.auth.ServerPolicy("example",
            auth_server_id="<auth server id>",
            status="ACTIVE",
            name="example",
            description="example",
            priority=1,
            client_whitelists=["ALL_CLIENTS"])
        ```

        ## Import

        ```sh
        $ pulumi import okta:auth/serverPolicy:ServerPolicy example &#60;auth server id&#62;/&#60;policy id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_server_id: The ID of the Auth Server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_whitelists: The clients to whitelist the policy for. `[ALL_CLIENTS]` is a special value that can be used to whitelist all clients, otherwise it is a list of client ids.
        :param pulumi.Input[str] description: The description of the Auth Server Policy.
        :param pulumi.Input[str] name: The name of the Auth Server Policy.
        :param pulumi.Input[int] priority: Priority of the auth server policy
        :param pulumi.Input[str] status: Default to `ACTIVE`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an Authorization Server Policy. This resource allows you to create and configure an Authorization Server Policy.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.auth.ServerPolicy("example",
            auth_server_id="<auth server id>",
            status="ACTIVE",
            name="example",
            description="example",
            priority=1,
            client_whitelists=["ALL_CLIENTS"])
        ```

        ## Import

        ```sh
        $ pulumi import okta:auth/serverPolicy:ServerPolicy example &#60;auth server id&#62;/&#60;policy id&#62;
        ```

        :param str resource_name: The name of the resource.
        :param ServerPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_server_id: Optional[pulumi.Input[str]] = None,
                 client_whitelists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerPolicyArgs.__new__(ServerPolicyArgs)

            if auth_server_id is None and not opts.urn:
                raise TypeError("Missing required property 'auth_server_id'")
            __props__.__dict__["auth_server_id"] = auth_server_id
            if client_whitelists is None and not opts.urn:
                raise TypeError("Missing required property 'client_whitelists'")
            __props__.__dict__["client_whitelists"] = client_whitelists
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__.__dict__["priority"] = priority
            __props__.__dict__["status"] = status
        super(ServerPolicy, __self__).__init__(
            'okta:auth/serverPolicy:ServerPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth_server_id: Optional[pulumi.Input[str]] = None,
            client_whitelists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'ServerPolicy':
        """
        Get an existing ServerPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_server_id: The ID of the Auth Server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] client_whitelists: The clients to whitelist the policy for. `[ALL_CLIENTS]` is a special value that can be used to whitelist all clients, otherwise it is a list of client ids.
        :param pulumi.Input[str] description: The description of the Auth Server Policy.
        :param pulumi.Input[str] name: The name of the Auth Server Policy.
        :param pulumi.Input[int] priority: Priority of the auth server policy
        :param pulumi.Input[str] status: Default to `ACTIVE`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServerPolicyState.__new__(_ServerPolicyState)

        __props__.__dict__["auth_server_id"] = auth_server_id
        __props__.__dict__["client_whitelists"] = client_whitelists
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["status"] = status
        return ServerPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authServerId")
    def auth_server_id(self) -> pulumi.Output[str]:
        """
        The ID of the Auth Server.
        """
        return pulumi.get(self, "auth_server_id")

    @property
    @pulumi.getter(name="clientWhitelists")
    def client_whitelists(self) -> pulumi.Output[Sequence[str]]:
        """
        The clients to whitelist the policy for. `[ALL_CLIENTS]` is a special value that can be used to whitelist all clients, otherwise it is a list of client ids.
        """
        return pulumi.get(self, "client_whitelists")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the Auth Server Policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Auth Server Policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Priority of the auth server policy
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Default to `ACTIVE`
        """
        return pulumi.get(self, "status")

