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
                 apikey: Optional[pulumi.Input[str]] = None,
                 enable_ddi: Optional[pulumi.Input[bool]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 ignore_ssl: Optional[pulumi.Input[bool]] = None,
                 rate_limit_parallelism: Optional[pulumi.Input[int]] = None,
                 retry_max: Optional[pulumi.Input[int]] = None,
                 user_agent: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] apikey: The ns1 API key (required)
        :param pulumi.Input[bool] enable_ddi: Deprecated, no longer in use
        :param pulumi.Input[str] endpoint: URL prefix (including version) for API calls
        :param pulumi.Input[bool] ignore_ssl: Don't validate server SSL/TLS certificate
        :param pulumi.Input[int] rate_limit_parallelism: Tune response to rate limits, see docs
        :param pulumi.Input[int] retry_max: Maximum retries for 50x errors (-1 to disable)
        :param pulumi.Input[str] user_agent: User-Agent string to use in NS1 API requests
        """
        if apikey is not None:
            pulumi.set(__self__, "apikey", apikey)
        if enable_ddi is not None:
            pulumi.set(__self__, "enable_ddi", enable_ddi)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if ignore_ssl is not None:
            pulumi.set(__self__, "ignore_ssl", ignore_ssl)
        if rate_limit_parallelism is not None:
            pulumi.set(__self__, "rate_limit_parallelism", rate_limit_parallelism)
        if retry_max is not None:
            pulumi.set(__self__, "retry_max", retry_max)
        if user_agent is not None:
            pulumi.set(__self__, "user_agent", user_agent)

    @property
    @pulumi.getter
    def apikey(self) -> Optional[pulumi.Input[str]]:
        """
        The ns1 API key (required)
        """
        return pulumi.get(self, "apikey")

    @apikey.setter
    def apikey(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "apikey", value)

    @property
    @pulumi.getter(name="enableDdi")
    def enable_ddi(self) -> Optional[pulumi.Input[bool]]:
        """
        Deprecated, no longer in use
        """
        return pulumi.get(self, "enable_ddi")

    @enable_ddi.setter
    def enable_ddi(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_ddi", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        URL prefix (including version) for API calls
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="ignoreSsl")
    def ignore_ssl(self) -> Optional[pulumi.Input[bool]]:
        """
        Don't validate server SSL/TLS certificate
        """
        return pulumi.get(self, "ignore_ssl")

    @ignore_ssl.setter
    def ignore_ssl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_ssl", value)

    @property
    @pulumi.getter(name="rateLimitParallelism")
    def rate_limit_parallelism(self) -> Optional[pulumi.Input[int]]:
        """
        Tune response to rate limits, see docs
        """
        return pulumi.get(self, "rate_limit_parallelism")

    @rate_limit_parallelism.setter
    def rate_limit_parallelism(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rate_limit_parallelism", value)

    @property
    @pulumi.getter(name="retryMax")
    def retry_max(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum retries for 50x errors (-1 to disable)
        """
        return pulumi.get(self, "retry_max")

    @retry_max.setter
    def retry_max(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retry_max", value)

    @property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> Optional[pulumi.Input[str]]:
        """
        User-Agent string to use in NS1 API requests
        """
        return pulumi.get(self, "user_agent")

    @user_agent.setter
    def user_agent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_agent", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apikey: Optional[pulumi.Input[str]] = None,
                 enable_ddi: Optional[pulumi.Input[bool]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 ignore_ssl: Optional[pulumi.Input[bool]] = None,
                 rate_limit_parallelism: Optional[pulumi.Input[int]] = None,
                 retry_max: Optional[pulumi.Input[int]] = None,
                 user_agent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the ns1 package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] apikey: The ns1 API key (required)
        :param pulumi.Input[bool] enable_ddi: Deprecated, no longer in use
        :param pulumi.Input[str] endpoint: URL prefix (including version) for API calls
        :param pulumi.Input[bool] ignore_ssl: Don't validate server SSL/TLS certificate
        :param pulumi.Input[int] rate_limit_parallelism: Tune response to rate limits, see docs
        :param pulumi.Input[int] retry_max: Maximum retries for 50x errors (-1 to disable)
        :param pulumi.Input[str] user_agent: User-Agent string to use in NS1 API requests
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the ns1 package. By default, resources use package-wide configuration
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
                 apikey: Optional[pulumi.Input[str]] = None,
                 enable_ddi: Optional[pulumi.Input[bool]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 ignore_ssl: Optional[pulumi.Input[bool]] = None,
                 rate_limit_parallelism: Optional[pulumi.Input[int]] = None,
                 retry_max: Optional[pulumi.Input[int]] = None,
                 user_agent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["apikey"] = apikey
            __props__.__dict__["enable_ddi"] = pulumi.Output.from_input(enable_ddi).apply(pulumi.runtime.to_json) if enable_ddi is not None else None
            __props__.__dict__["endpoint"] = endpoint
            __props__.__dict__["ignore_ssl"] = pulumi.Output.from_input(ignore_ssl).apply(pulumi.runtime.to_json) if ignore_ssl is not None else None
            __props__.__dict__["rate_limit_parallelism"] = pulumi.Output.from_input(rate_limit_parallelism).apply(pulumi.runtime.to_json) if rate_limit_parallelism is not None else None
            __props__.__dict__["retry_max"] = pulumi.Output.from_input(retry_max).apply(pulumi.runtime.to_json) if retry_max is not None else None
            __props__.__dict__["user_agent"] = user_agent
        super(Provider, __self__).__init__(
            'ns1',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter
    def apikey(self) -> pulumi.Output[Optional[str]]:
        """
        The ns1 API key (required)
        """
        return pulumi.get(self, "apikey")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        URL prefix (including version) for API calls
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> pulumi.Output[Optional[str]]:
        """
        User-Agent string to use in NS1 API requests
        """
        return pulumi.get(self, "user_agent")

