# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TokenArgs', 'Token']

@pulumi.input_type
class TokenArgs:
    def __init__(__self__, *,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 renew: Optional[pulumi.Input[bool]] = None,
                 ttl: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Token resource.
        :param pulumi.Input[Mapping[str, Any]] annotations: (Computed) Annotations of the token (map)
        :param pulumi.Input[str] cluster_id: Cluster ID for scoped token (string)
        :param pulumi.Input[str] description: Token description (string)
        :param pulumi.Input[Mapping[str, Any]] labels: (Computed) Labels of the token (map)
        :param pulumi.Input[bool] renew: Renew expired or disabled token
        :param pulumi.Input[int] ttl: Token time to live in seconds. Default `0` (int) 
               
               From Rancher v2.4.6 `ttl` is readed in minutes at Rancher API. To avoid breaking change on the provider, we still read in seconds but rounding up division if required.
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if renew is not None:
            pulumi.set(__self__, "renew", renew)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Computed) Annotations of the token (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster ID for scoped token (string)
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Token description (string)
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Computed) Labels of the token (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def renew(self) -> Optional[pulumi.Input[bool]]:
        """
        Renew expired or disabled token
        """
        return pulumi.get(self, "renew")

    @renew.setter
    def renew(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "renew", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Token time to live in seconds. Default `0` (int) 

        From Rancher v2.4.6 `ttl` is readed in minutes at Rancher API. To avoid breaking change on the provider, we still read in seconds but rounding up division if required.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)


@pulumi.input_type
class _TokenState:
    def __init__(__self__, *,
                 access_key: Optional[pulumi.Input[str]] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 expired: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 renew: Optional[pulumi.Input[bool]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Token resources.
        :param pulumi.Input[str] access_key: (Computed) Token access key part (string)
        :param pulumi.Input[Mapping[str, Any]] annotations: (Computed) Annotations of the token (map)
        :param pulumi.Input[str] cluster_id: Cluster ID for scoped token (string)
        :param pulumi.Input[str] description: Token description (string)
        :param pulumi.Input[bool] enabled: (Computed) Token is enabled (bool)
        :param pulumi.Input[bool] expired: (Computed) Token is expired (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: (Computed) Labels of the token (map)
        :param pulumi.Input[str] name: (Computed) Token name (string)
        :param pulumi.Input[bool] renew: Renew expired or disabled token
        :param pulumi.Input[str] secret_key: (Computed/Sensitive) Token secret key part (string)
        :param pulumi.Input[str] token: (Computed/Sensitive) Token value (string)
        :param pulumi.Input[int] ttl: Token time to live in seconds. Default `0` (int) 
               
               From Rancher v2.4.6 `ttl` is readed in minutes at Rancher API. To avoid breaking change on the provider, we still read in seconds but rounding up division if required.
        :param pulumi.Input[str] user_id: (Computed) Token user ID (string)
        """
        if access_key is not None:
            pulumi.set(__self__, "access_key", access_key)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if expired is not None:
            pulumi.set(__self__, "expired", expired)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if renew is not None:
            pulumi.set(__self__, "renew", renew)
        if secret_key is not None:
            pulumi.set(__self__, "secret_key", secret_key)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) Token access key part (string)
        """
        return pulumi.get(self, "access_key")

    @access_key.setter
    def access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Computed) Annotations of the token (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster ID for scoped token (string)
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Token description (string)
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        (Computed) Token is enabled (bool)
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def expired(self) -> Optional[pulumi.Input[bool]]:
        """
        (Computed) Token is expired (bool)
        """
        return pulumi.get(self, "expired")

    @expired.setter
    def expired(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "expired", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (Computed) Labels of the token (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) Token name (string)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def renew(self) -> Optional[pulumi.Input[bool]]:
        """
        Renew expired or disabled token
        """
        return pulumi.get(self, "renew")

    @renew.setter
    def renew(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "renew", value)

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed/Sensitive) Token secret key part (string)
        """
        return pulumi.get(self, "secret_key")

    @secret_key.setter
    def secret_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_key", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed/Sensitive) Token value (string)
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Token time to live in seconds. Default `0` (int) 

        From Rancher v2.4.6 `ttl` is readed in minutes at Rancher API. To avoid breaking change on the provider, we still read in seconds but rounding up division if required.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) Token user ID (string)
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class Token(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 renew: Optional[pulumi.Input[bool]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a Rancher v2 Token resource. This can be used to create Tokens for Rancher v2 provider user and retrieve their information.

        There are 2 kind of tokens:
        - no scoped: valid for global system.
        - scoped: valid for just a specific cluster (`cluster_id` should be provided).

        Tokens can't be updated once created. Any diff in token data will recreate the token. If any token expire, Rancher2 provider will generate a diff to regenerate it.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] annotations: (Computed) Annotations of the token (map)
        :param pulumi.Input[str] cluster_id: Cluster ID for scoped token (string)
        :param pulumi.Input[str] description: Token description (string)
        :param pulumi.Input[Mapping[str, Any]] labels: (Computed) Labels of the token (map)
        :param pulumi.Input[bool] renew: Renew expired or disabled token
        :param pulumi.Input[int] ttl: Token time to live in seconds. Default `0` (int) 
               
               From Rancher v2.4.6 `ttl` is readed in minutes at Rancher API. To avoid breaking change on the provider, we still read in seconds but rounding up division if required.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TokenArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Rancher v2 Token resource. This can be used to create Tokens for Rancher v2 provider user and retrieve their information.

        There are 2 kind of tokens:
        - no scoped: valid for global system.
        - scoped: valid for just a specific cluster (`cluster_id` should be provided).

        Tokens can't be updated once created. Any diff in token data will recreate the token. If any token expire, Rancher2 provider will generate a diff to regenerate it.

        :param str resource_name: The name of the resource.
        :param TokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 renew: Optional[pulumi.Input[bool]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TokenArgs.__new__(TokenArgs)

            __props__.__dict__["annotations"] = annotations
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["renew"] = renew
            __props__.__dict__["ttl"] = ttl
            __props__.__dict__["access_key"] = None
            __props__.__dict__["enabled"] = None
            __props__.__dict__["expired"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["secret_key"] = None
            __props__.__dict__["token"] = None
            __props__.__dict__["user_id"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["secretKey", "token"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Token, __self__).__init__(
            'rancher2:index/token:Token',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_key: Optional[pulumi.Input[str]] = None,
            annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            expired: Optional[pulumi.Input[bool]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            renew: Optional[pulumi.Input[bool]] = None,
            secret_key: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None,
            ttl: Optional[pulumi.Input[int]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'Token':
        """
        Get an existing Token resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key: (Computed) Token access key part (string)
        :param pulumi.Input[Mapping[str, Any]] annotations: (Computed) Annotations of the token (map)
        :param pulumi.Input[str] cluster_id: Cluster ID for scoped token (string)
        :param pulumi.Input[str] description: Token description (string)
        :param pulumi.Input[bool] enabled: (Computed) Token is enabled (bool)
        :param pulumi.Input[bool] expired: (Computed) Token is expired (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: (Computed) Labels of the token (map)
        :param pulumi.Input[str] name: (Computed) Token name (string)
        :param pulumi.Input[bool] renew: Renew expired or disabled token
        :param pulumi.Input[str] secret_key: (Computed/Sensitive) Token secret key part (string)
        :param pulumi.Input[str] token: (Computed/Sensitive) Token value (string)
        :param pulumi.Input[int] ttl: Token time to live in seconds. Default `0` (int) 
               
               From Rancher v2.4.6 `ttl` is readed in minutes at Rancher API. To avoid breaking change on the provider, we still read in seconds but rounding up division if required.
        :param pulumi.Input[str] user_id: (Computed) Token user ID (string)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TokenState.__new__(_TokenState)

        __props__.__dict__["access_key"] = access_key
        __props__.__dict__["annotations"] = annotations
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["expired"] = expired
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["renew"] = renew
        __props__.__dict__["secret_key"] = secret_key
        __props__.__dict__["token"] = token
        __props__.__dict__["ttl"] = ttl
        __props__.__dict__["user_id"] = user_id
        return Token(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[str]:
        """
        (Computed) Token access key part (string)
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Computed) Annotations of the token (map)
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[Optional[str]]:
        """
        Cluster ID for scoped token (string)
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Token description (string)
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        (Computed) Token is enabled (bool)
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def expired(self) -> pulumi.Output[bool]:
        """
        (Computed) Token is expired (bool)
        """
        return pulumi.get(self, "expired")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        (Computed) Labels of the token (map)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        (Computed) Token name (string)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def renew(self) -> pulumi.Output[Optional[bool]]:
        """
        Renew expired or disabled token
        """
        return pulumi.get(self, "renew")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Output[str]:
        """
        (Computed/Sensitive) Token secret key part (string)
        """
        return pulumi.get(self, "secret_key")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        (Computed/Sensitive) Token value (string)
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[int]]:
        """
        Token time to live in seconds. Default `0` (int) 

        From Rancher v2.4.6 `ttl` is readed in minutes at Rancher API. To avoid breaking change on the provider, we still read in seconds but rounding up division if required.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        (Computed) Token user ID (string)
        """
        return pulumi.get(self, "user_id")

