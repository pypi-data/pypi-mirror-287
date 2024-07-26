# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 api_version: Optional[pulumi.Input[str]] = None,
                 config_path: Optional[pulumi.Input[str]] = None,
                 config_profile: Optional[pulumi.Input[str]] = None,
                 disable_internal_cache: Optional[pulumi.Input[bool]] = None,
                 event_poll_ms: Optional[pulumi.Input[int]] = None,
                 lke_event_poll_ms: Optional[pulumi.Input[int]] = None,
                 lke_node_ready_poll_ms: Optional[pulumi.Input[int]] = None,
                 max_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 min_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 obj_access_key: Optional[pulumi.Input[str]] = None,
                 obj_bucket_force_delete: Optional[pulumi.Input[bool]] = None,
                 obj_secret_key: Optional[pulumi.Input[str]] = None,
                 obj_use_temp_keys: Optional[pulumi.Input[bool]] = None,
                 skip_implicit_reboots: Optional[pulumi.Input[bool]] = None,
                 skip_instance_delete_poll: Optional[pulumi.Input[bool]] = None,
                 skip_instance_ready_poll: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 ua_prefix: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] api_version: The version of Linode API.
        :param pulumi.Input[str] config_path: The path to the Linode config file to use. (default `~/.config/linode`)
        :param pulumi.Input[str] config_profile: The Linode config profile to use. (default `default`)
        :param pulumi.Input[bool] disable_internal_cache: Disable the internal caching system that backs certain Linode API requests.
        :param pulumi.Input[int] event_poll_ms: The rate in milliseconds to poll for events.
        :param pulumi.Input[int] lke_event_poll_ms: The rate in milliseconds to poll for LKE events.
        :param pulumi.Input[int] lke_node_ready_poll_ms: The rate in milliseconds to poll for an LKE node to be ready.
        :param pulumi.Input[int] max_retry_delay_ms: Maximum delay in milliseconds before retrying a request.
        :param pulumi.Input[int] min_retry_delay_ms: Minimum delay in milliseconds before retrying a request.
        :param pulumi.Input[str] obj_access_key: The access key to be used in ObjectStorageBucket and linode_object_storage_object.
        :param pulumi.Input[bool] obj_bucket_force_delete: If true, when deleting a ObjectStorageBucket any objects and versions will be force deleted.
        :param pulumi.Input[str] obj_secret_key: The secret key to be used in ObjectStorageBucket and linode_object_storage_object.
        :param pulumi.Input[bool] obj_use_temp_keys: If true, temporary object keys will be created implicitly at apply-time for the ObjectStorageObject and
               linode_object_sorage_bucket resource.
        :param pulumi.Input[bool] skip_implicit_reboots: If true, Linode Instances will not be rebooted on config and interface changes.
        :param pulumi.Input[bool] skip_instance_delete_poll: Skip waiting for a Instance resource to finish deleting.
        :param pulumi.Input[bool] skip_instance_ready_poll: Skip waiting for a Instance resource to be running.
        :param pulumi.Input[str] token: The token that allows you access to your Linode account
        :param pulumi.Input[str] ua_prefix: An HTTP User-Agent Prefix to prepend in API requests.
        :param pulumi.Input[str] url: The HTTP(S) API address of the Linode API to use.
        """
        if api_version is None:
            api_version = _utilities.get_env('LINODE_API_VERSION')
        if api_version is not None:
            pulumi.set(__self__, "api_version", api_version)
        if config_path is not None:
            pulumi.set(__self__, "config_path", config_path)
        if config_profile is not None:
            pulumi.set(__self__, "config_profile", config_profile)
        if disable_internal_cache is not None:
            pulumi.set(__self__, "disable_internal_cache", disable_internal_cache)
        if event_poll_ms is not None:
            pulumi.set(__self__, "event_poll_ms", event_poll_ms)
        if lke_event_poll_ms is not None:
            pulumi.set(__self__, "lke_event_poll_ms", lke_event_poll_ms)
        if lke_node_ready_poll_ms is not None:
            pulumi.set(__self__, "lke_node_ready_poll_ms", lke_node_ready_poll_ms)
        if max_retry_delay_ms is not None:
            pulumi.set(__self__, "max_retry_delay_ms", max_retry_delay_ms)
        if min_retry_delay_ms is not None:
            pulumi.set(__self__, "min_retry_delay_ms", min_retry_delay_ms)
        if obj_access_key is not None:
            pulumi.set(__self__, "obj_access_key", obj_access_key)
        if obj_bucket_force_delete is not None:
            pulumi.set(__self__, "obj_bucket_force_delete", obj_bucket_force_delete)
        if obj_secret_key is not None:
            pulumi.set(__self__, "obj_secret_key", obj_secret_key)
        if obj_use_temp_keys is not None:
            pulumi.set(__self__, "obj_use_temp_keys", obj_use_temp_keys)
        if skip_implicit_reboots is not None:
            pulumi.set(__self__, "skip_implicit_reboots", skip_implicit_reboots)
        if skip_instance_delete_poll is not None:
            pulumi.set(__self__, "skip_instance_delete_poll", skip_instance_delete_poll)
        if skip_instance_ready_poll is not None:
            pulumi.set(__self__, "skip_instance_ready_poll", skip_instance_ready_poll)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if ua_prefix is None:
            ua_prefix = _utilities.get_env('LINODE_UA_PREFIX')
        if ua_prefix is not None:
            pulumi.set(__self__, "ua_prefix", ua_prefix)
        if url is None:
            url = _utilities.get_env('LINODE_URL')
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of Linode API.
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter(name="configPath")
    def config_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the Linode config file to use. (default `~/.config/linode`)
        """
        return pulumi.get(self, "config_path")

    @config_path.setter
    def config_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_path", value)

    @property
    @pulumi.getter(name="configProfile")
    def config_profile(self) -> Optional[pulumi.Input[str]]:
        """
        The Linode config profile to use. (default `default`)
        """
        return pulumi.get(self, "config_profile")

    @config_profile.setter
    def config_profile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_profile", value)

    @property
    @pulumi.getter(name="disableInternalCache")
    def disable_internal_cache(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable the internal caching system that backs certain Linode API requests.
        """
        return pulumi.get(self, "disable_internal_cache")

    @disable_internal_cache.setter
    def disable_internal_cache(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_internal_cache", value)

    @property
    @pulumi.getter(name="eventPollMs")
    def event_poll_ms(self) -> Optional[pulumi.Input[int]]:
        """
        The rate in milliseconds to poll for events.
        """
        return pulumi.get(self, "event_poll_ms")

    @event_poll_ms.setter
    def event_poll_ms(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "event_poll_ms", value)

    @property
    @pulumi.getter(name="lkeEventPollMs")
    def lke_event_poll_ms(self) -> Optional[pulumi.Input[int]]:
        """
        The rate in milliseconds to poll for LKE events.
        """
        return pulumi.get(self, "lke_event_poll_ms")

    @lke_event_poll_ms.setter
    def lke_event_poll_ms(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "lke_event_poll_ms", value)

    @property
    @pulumi.getter(name="lkeNodeReadyPollMs")
    def lke_node_ready_poll_ms(self) -> Optional[pulumi.Input[int]]:
        """
        The rate in milliseconds to poll for an LKE node to be ready.
        """
        return pulumi.get(self, "lke_node_ready_poll_ms")

    @lke_node_ready_poll_ms.setter
    def lke_node_ready_poll_ms(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "lke_node_ready_poll_ms", value)

    @property
    @pulumi.getter(name="maxRetryDelayMs")
    def max_retry_delay_ms(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum delay in milliseconds before retrying a request.
        """
        return pulumi.get(self, "max_retry_delay_ms")

    @max_retry_delay_ms.setter
    def max_retry_delay_ms(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_retry_delay_ms", value)

    @property
    @pulumi.getter(name="minRetryDelayMs")
    def min_retry_delay_ms(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum delay in milliseconds before retrying a request.
        """
        return pulumi.get(self, "min_retry_delay_ms")

    @min_retry_delay_ms.setter
    def min_retry_delay_ms(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_retry_delay_ms", value)

    @property
    @pulumi.getter(name="objAccessKey")
    def obj_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        The access key to be used in ObjectStorageBucket and linode_object_storage_object.
        """
        return pulumi.get(self, "obj_access_key")

    @obj_access_key.setter
    def obj_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "obj_access_key", value)

    @property
    @pulumi.getter(name="objBucketForceDelete")
    def obj_bucket_force_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, when deleting a ObjectStorageBucket any objects and versions will be force deleted.
        """
        return pulumi.get(self, "obj_bucket_force_delete")

    @obj_bucket_force_delete.setter
    def obj_bucket_force_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "obj_bucket_force_delete", value)

    @property
    @pulumi.getter(name="objSecretKey")
    def obj_secret_key(self) -> Optional[pulumi.Input[str]]:
        """
        The secret key to be used in ObjectStorageBucket and linode_object_storage_object.
        """
        return pulumi.get(self, "obj_secret_key")

    @obj_secret_key.setter
    def obj_secret_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "obj_secret_key", value)

    @property
    @pulumi.getter(name="objUseTempKeys")
    def obj_use_temp_keys(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, temporary object keys will be created implicitly at apply-time for the ObjectStorageObject and
        linode_object_sorage_bucket resource.
        """
        return pulumi.get(self, "obj_use_temp_keys")

    @obj_use_temp_keys.setter
    def obj_use_temp_keys(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "obj_use_temp_keys", value)

    @property
    @pulumi.getter(name="skipImplicitReboots")
    def skip_implicit_reboots(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, Linode Instances will not be rebooted on config and interface changes.
        """
        return pulumi.get(self, "skip_implicit_reboots")

    @skip_implicit_reboots.setter
    def skip_implicit_reboots(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_implicit_reboots", value)

    @property
    @pulumi.getter(name="skipInstanceDeletePoll")
    def skip_instance_delete_poll(self) -> Optional[pulumi.Input[bool]]:
        """
        Skip waiting for a Instance resource to finish deleting.
        """
        return pulumi.get(self, "skip_instance_delete_poll")

    @skip_instance_delete_poll.setter
    def skip_instance_delete_poll(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_instance_delete_poll", value)

    @property
    @pulumi.getter(name="skipInstanceReadyPoll")
    def skip_instance_ready_poll(self) -> Optional[pulumi.Input[bool]]:
        """
        Skip waiting for a Instance resource to be running.
        """
        return pulumi.get(self, "skip_instance_ready_poll")

    @skip_instance_ready_poll.setter
    def skip_instance_ready_poll(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_instance_ready_poll", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The token that allows you access to your Linode account
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter(name="uaPrefix")
    def ua_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        An HTTP User-Agent Prefix to prepend in API requests.
        """
        return pulumi.get(self, "ua_prefix")

    @ua_prefix.setter
    def ua_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ua_prefix", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP(S) API address of the Linode API to use.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 config_path: Optional[pulumi.Input[str]] = None,
                 config_profile: Optional[pulumi.Input[str]] = None,
                 disable_internal_cache: Optional[pulumi.Input[bool]] = None,
                 event_poll_ms: Optional[pulumi.Input[int]] = None,
                 lke_event_poll_ms: Optional[pulumi.Input[int]] = None,
                 lke_node_ready_poll_ms: Optional[pulumi.Input[int]] = None,
                 max_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 min_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 obj_access_key: Optional[pulumi.Input[str]] = None,
                 obj_bucket_force_delete: Optional[pulumi.Input[bool]] = None,
                 obj_secret_key: Optional[pulumi.Input[str]] = None,
                 obj_use_temp_keys: Optional[pulumi.Input[bool]] = None,
                 skip_implicit_reboots: Optional[pulumi.Input[bool]] = None,
                 skip_instance_delete_poll: Optional[pulumi.Input[bool]] = None,
                 skip_instance_ready_poll: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 ua_prefix: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the linode package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: The version of Linode API.
        :param pulumi.Input[str] config_path: The path to the Linode config file to use. (default `~/.config/linode`)
        :param pulumi.Input[str] config_profile: The Linode config profile to use. (default `default`)
        :param pulumi.Input[bool] disable_internal_cache: Disable the internal caching system that backs certain Linode API requests.
        :param pulumi.Input[int] event_poll_ms: The rate in milliseconds to poll for events.
        :param pulumi.Input[int] lke_event_poll_ms: The rate in milliseconds to poll for LKE events.
        :param pulumi.Input[int] lke_node_ready_poll_ms: The rate in milliseconds to poll for an LKE node to be ready.
        :param pulumi.Input[int] max_retry_delay_ms: Maximum delay in milliseconds before retrying a request.
        :param pulumi.Input[int] min_retry_delay_ms: Minimum delay in milliseconds before retrying a request.
        :param pulumi.Input[str] obj_access_key: The access key to be used in ObjectStorageBucket and linode_object_storage_object.
        :param pulumi.Input[bool] obj_bucket_force_delete: If true, when deleting a ObjectStorageBucket any objects and versions will be force deleted.
        :param pulumi.Input[str] obj_secret_key: The secret key to be used in ObjectStorageBucket and linode_object_storage_object.
        :param pulumi.Input[bool] obj_use_temp_keys: If true, temporary object keys will be created implicitly at apply-time for the ObjectStorageObject and
               linode_object_sorage_bucket resource.
        :param pulumi.Input[bool] skip_implicit_reboots: If true, Linode Instances will not be rebooted on config and interface changes.
        :param pulumi.Input[bool] skip_instance_delete_poll: Skip waiting for a Instance resource to finish deleting.
        :param pulumi.Input[bool] skip_instance_ready_poll: Skip waiting for a Instance resource to be running.
        :param pulumi.Input[str] token: The token that allows you access to your Linode account
        :param pulumi.Input[str] ua_prefix: An HTTP User-Agent Prefix to prepend in API requests.
        :param pulumi.Input[str] url: The HTTP(S) API address of the Linode API to use.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the linode package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 config_path: Optional[pulumi.Input[str]] = None,
                 config_profile: Optional[pulumi.Input[str]] = None,
                 disable_internal_cache: Optional[pulumi.Input[bool]] = None,
                 event_poll_ms: Optional[pulumi.Input[int]] = None,
                 lke_event_poll_ms: Optional[pulumi.Input[int]] = None,
                 lke_node_ready_poll_ms: Optional[pulumi.Input[int]] = None,
                 max_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 min_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 obj_access_key: Optional[pulumi.Input[str]] = None,
                 obj_bucket_force_delete: Optional[pulumi.Input[bool]] = None,
                 obj_secret_key: Optional[pulumi.Input[str]] = None,
                 obj_use_temp_keys: Optional[pulumi.Input[bool]] = None,
                 skip_implicit_reboots: Optional[pulumi.Input[bool]] = None,
                 skip_instance_delete_poll: Optional[pulumi.Input[bool]] = None,
                 skip_instance_ready_poll: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 ua_prefix: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if api_version is None:
                api_version = _utilities.get_env('LINODE_API_VERSION')
            __props__.__dict__["api_version"] = api_version
            __props__.__dict__["config_path"] = config_path
            __props__.__dict__["config_profile"] = config_profile
            __props__.__dict__["disable_internal_cache"] = pulumi.Output.from_input(disable_internal_cache).apply(pulumi.runtime.to_json) if disable_internal_cache is not None else None
            __props__.__dict__["event_poll_ms"] = pulumi.Output.from_input(event_poll_ms).apply(pulumi.runtime.to_json) if event_poll_ms is not None else None
            __props__.__dict__["lke_event_poll_ms"] = pulumi.Output.from_input(lke_event_poll_ms).apply(pulumi.runtime.to_json) if lke_event_poll_ms is not None else None
            __props__.__dict__["lke_node_ready_poll_ms"] = pulumi.Output.from_input(lke_node_ready_poll_ms).apply(pulumi.runtime.to_json) if lke_node_ready_poll_ms is not None else None
            __props__.__dict__["max_retry_delay_ms"] = pulumi.Output.from_input(max_retry_delay_ms).apply(pulumi.runtime.to_json) if max_retry_delay_ms is not None else None
            __props__.__dict__["min_retry_delay_ms"] = pulumi.Output.from_input(min_retry_delay_ms).apply(pulumi.runtime.to_json) if min_retry_delay_ms is not None else None
            __props__.__dict__["obj_access_key"] = obj_access_key
            __props__.__dict__["obj_bucket_force_delete"] = pulumi.Output.from_input(obj_bucket_force_delete).apply(pulumi.runtime.to_json) if obj_bucket_force_delete is not None else None
            __props__.__dict__["obj_secret_key"] = None if obj_secret_key is None else pulumi.Output.secret(obj_secret_key)
            __props__.__dict__["obj_use_temp_keys"] = pulumi.Output.from_input(obj_use_temp_keys).apply(pulumi.runtime.to_json) if obj_use_temp_keys is not None else None
            __props__.__dict__["skip_implicit_reboots"] = pulumi.Output.from_input(skip_implicit_reboots).apply(pulumi.runtime.to_json) if skip_implicit_reboots is not None else None
            __props__.__dict__["skip_instance_delete_poll"] = pulumi.Output.from_input(skip_instance_delete_poll).apply(pulumi.runtime.to_json) if skip_instance_delete_poll is not None else None
            __props__.__dict__["skip_instance_ready_poll"] = pulumi.Output.from_input(skip_instance_ready_poll).apply(pulumi.runtime.to_json) if skip_instance_ready_poll is not None else None
            __props__.__dict__["token"] = token
            if ua_prefix is None:
                ua_prefix = _utilities.get_env('LINODE_UA_PREFIX')
            __props__.__dict__["ua_prefix"] = ua_prefix
            if url is None:
                url = _utilities.get_env('LINODE_URL')
            __props__.__dict__["url"] = url
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["objSecretKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'linode',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of Linode API.
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter(name="configPath")
    def config_path(self) -> pulumi.Output[Optional[str]]:
        """
        The path to the Linode config file to use. (default `~/.config/linode`)
        """
        return pulumi.get(self, "config_path")

    @property
    @pulumi.getter(name="configProfile")
    def config_profile(self) -> pulumi.Output[Optional[str]]:
        """
        The Linode config profile to use. (default `default`)
        """
        return pulumi.get(self, "config_profile")

    @property
    @pulumi.getter(name="objAccessKey")
    def obj_access_key(self) -> pulumi.Output[Optional[str]]:
        """
        The access key to be used in ObjectStorageBucket and linode_object_storage_object.
        """
        return pulumi.get(self, "obj_access_key")

    @property
    @pulumi.getter(name="objSecretKey")
    def obj_secret_key(self) -> pulumi.Output[Optional[str]]:
        """
        The secret key to be used in ObjectStorageBucket and linode_object_storage_object.
        """
        return pulumi.get(self, "obj_secret_key")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[str]]:
        """
        The token that allows you access to your Linode account
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter(name="uaPrefix")
    def ua_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        An HTTP User-Agent Prefix to prepend in API requests.
        """
        return pulumi.get(self, "ua_prefix")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        """
        The HTTP(S) API address of the Linode API to use.
        """
        return pulumi.get(self, "url")

