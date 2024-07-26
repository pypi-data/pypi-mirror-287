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
                 api_key: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 admin_api_key: Optional[pulumi.Input[str]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 cacert_file: Optional[pulumi.Input[str]] = None,
                 infrastructure_api_url: Optional[pulumi.Input[str]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 insights_insert_key: Optional[pulumi.Input[str]] = None,
                 insights_insert_url: Optional[pulumi.Input[str]] = None,
                 insights_query_url: Optional[pulumi.Input[str]] = None,
                 nerdgraph_api_url: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 synthetics_api_url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] region: The data center for which your New Relic account is configured. Only one region per provider block is permitted.
        """
        pulumi.set(__self__, "api_key", api_key)
        if account_id is None:
            account_id = _utilities.get_env('NEW_RELIC_ACCOUNT_ID')
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if admin_api_key is not None:
            pulumi.set(__self__, "admin_api_key", admin_api_key)
        if api_url is not None:
            warnings.warn("""New Relic internal use only. API URLs are now configured based on the configured region.""", DeprecationWarning)
            pulumi.log.warn("""api_url is deprecated: New Relic internal use only. API URLs are now configured based on the configured region.""")
        if api_url is not None:
            pulumi.set(__self__, "api_url", api_url)
        if cacert_file is not None:
            pulumi.set(__self__, "cacert_file", cacert_file)
        if infrastructure_api_url is not None:
            warnings.warn("""New Relic internal use only. API URLs are now configured based on the configured region.""", DeprecationWarning)
            pulumi.log.warn("""infrastructure_api_url is deprecated: New Relic internal use only. API URLs are now configured based on the configured region.""")
        if infrastructure_api_url is not None:
            pulumi.set(__self__, "infrastructure_api_url", infrastructure_api_url)
        if insecure_skip_verify is not None:
            pulumi.set(__self__, "insecure_skip_verify", insecure_skip_verify)
        if insights_insert_key is not None:
            pulumi.set(__self__, "insights_insert_key", insights_insert_key)
        if insights_insert_url is not None:
            pulumi.set(__self__, "insights_insert_url", insights_insert_url)
        if insights_query_url is not None:
            pulumi.set(__self__, "insights_query_url", insights_query_url)
        if nerdgraph_api_url is not None:
            warnings.warn("""New Relic internal use only. API URLs are now configured based on the configured region.""", DeprecationWarning)
            pulumi.log.warn("""nerdgraph_api_url is deprecated: New Relic internal use only. API URLs are now configured based on the configured region.""")
        if nerdgraph_api_url is not None:
            pulumi.set(__self__, "nerdgraph_api_url", nerdgraph_api_url)
        if region is None:
            region = (_utilities.get_env('NEW_RELIC_REGION') or 'US')
        if region is not None:
            pulumi.set(__self__, "region", region)
        if synthetics_api_url is not None:
            warnings.warn("""New Relic internal use only. API URLs are now configured based on the configured region.""", DeprecationWarning)
            pulumi.log.warn("""synthetics_api_url is deprecated: New Relic internal use only. API URLs are now configured based on the configured region.""")
        if synthetics_api_url is not None:
            pulumi.set(__self__, "synthetics_api_url", synthetics_api_url)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="adminApiKey")
    def admin_api_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "admin_api_key")

    @admin_api_key.setter
    def admin_api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "admin_api_key", value)

    @property
    @pulumi.getter(name="apiUrl")
    @_utilities.deprecated("""New Relic internal use only. API URLs are now configured based on the configured region.""")
    def api_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "api_url")

    @api_url.setter
    def api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_url", value)

    @property
    @pulumi.getter(name="cacertFile")
    def cacert_file(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cacert_file")

    @cacert_file.setter
    def cacert_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cacert_file", value)

    @property
    @pulumi.getter(name="infrastructureApiUrl")
    @_utilities.deprecated("""New Relic internal use only. API URLs are now configured based on the configured region.""")
    def infrastructure_api_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "infrastructure_api_url")

    @infrastructure_api_url.setter
    def infrastructure_api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "infrastructure_api_url", value)

    @property
    @pulumi.getter(name="insecureSkipVerify")
    def insecure_skip_verify(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "insecure_skip_verify")

    @insecure_skip_verify.setter
    def insecure_skip_verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure_skip_verify", value)

    @property
    @pulumi.getter(name="insightsInsertKey")
    def insights_insert_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "insights_insert_key")

    @insights_insert_key.setter
    def insights_insert_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "insights_insert_key", value)

    @property
    @pulumi.getter(name="insightsInsertUrl")
    def insights_insert_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "insights_insert_url")

    @insights_insert_url.setter
    def insights_insert_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "insights_insert_url", value)

    @property
    @pulumi.getter(name="insightsQueryUrl")
    def insights_query_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "insights_query_url")

    @insights_query_url.setter
    def insights_query_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "insights_query_url", value)

    @property
    @pulumi.getter(name="nerdgraphApiUrl")
    @_utilities.deprecated("""New Relic internal use only. API URLs are now configured based on the configured region.""")
    def nerdgraph_api_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "nerdgraph_api_url")

    @nerdgraph_api_url.setter
    def nerdgraph_api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nerdgraph_api_url", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The data center for which your New Relic account is configured. Only one region per provider block is permitted.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="syntheticsApiUrl")
    @_utilities.deprecated("""New Relic internal use only. API URLs are now configured based on the configured region.""")
    def synthetics_api_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "synthetics_api_url")

    @synthetics_api_url.setter
    def synthetics_api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "synthetics_api_url", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 admin_api_key: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 cacert_file: Optional[pulumi.Input[str]] = None,
                 infrastructure_api_url: Optional[pulumi.Input[str]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 insights_insert_key: Optional[pulumi.Input[str]] = None,
                 insights_insert_url: Optional[pulumi.Input[str]] = None,
                 insights_query_url: Optional[pulumi.Input[str]] = None,
                 nerdgraph_api_url: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 synthetics_api_url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the newrelic package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] region: The data center for which your New Relic account is configured. Only one region per provider block is permitted.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the newrelic package. By default, resources use package-wide configuration
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
                 account_id: Optional[pulumi.Input[str]] = None,
                 admin_api_key: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 cacert_file: Optional[pulumi.Input[str]] = None,
                 infrastructure_api_url: Optional[pulumi.Input[str]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 insights_insert_key: Optional[pulumi.Input[str]] = None,
                 insights_insert_url: Optional[pulumi.Input[str]] = None,
                 insights_query_url: Optional[pulumi.Input[str]] = None,
                 nerdgraph_api_url: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 synthetics_api_url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if account_id is None:
                account_id = _utilities.get_env('NEW_RELIC_ACCOUNT_ID')
            __props__.__dict__["account_id"] = None if account_id is None else pulumi.Output.secret(account_id)
            __props__.__dict__["admin_api_key"] = None if admin_api_key is None else pulumi.Output.secret(admin_api_key)
            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["api_url"] = api_url
            __props__.__dict__["cacert_file"] = cacert_file
            __props__.__dict__["infrastructure_api_url"] = infrastructure_api_url
            __props__.__dict__["insecure_skip_verify"] = pulumi.Output.from_input(insecure_skip_verify).apply(pulumi.runtime.to_json) if insecure_skip_verify is not None else None
            __props__.__dict__["insights_insert_key"] = None if insights_insert_key is None else pulumi.Output.secret(insights_insert_key)
            __props__.__dict__["insights_insert_url"] = insights_insert_url
            __props__.__dict__["insights_query_url"] = insights_query_url
            __props__.__dict__["nerdgraph_api_url"] = nerdgraph_api_url
            if region is None:
                region = (_utilities.get_env('NEW_RELIC_REGION') or 'US')
            __props__.__dict__["region"] = region
            __props__.__dict__["synthetics_api_url"] = synthetics_api_url
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["accountId", "adminApiKey", "apiKey", "insightsInsertKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'newrelic',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="adminApiKey")
    def admin_api_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "admin_api_key")

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="apiUrl")
    @_utilities.deprecated("""New Relic internal use only. API URLs are now configured based on the configured region.""")
    def api_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "api_url")

    @property
    @pulumi.getter(name="cacertFile")
    def cacert_file(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cacert_file")

    @property
    @pulumi.getter(name="infrastructureApiUrl")
    @_utilities.deprecated("""New Relic internal use only. API URLs are now configured based on the configured region.""")
    def infrastructure_api_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "infrastructure_api_url")

    @property
    @pulumi.getter(name="insightsInsertKey")
    def insights_insert_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "insights_insert_key")

    @property
    @pulumi.getter(name="insightsInsertUrl")
    def insights_insert_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "insights_insert_url")

    @property
    @pulumi.getter(name="insightsQueryUrl")
    def insights_query_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "insights_query_url")

    @property
    @pulumi.getter(name="nerdgraphApiUrl")
    @_utilities.deprecated("""New Relic internal use only. API URLs are now configured based on the configured region.""")
    def nerdgraph_api_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "nerdgraph_api_url")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The data center for which your New Relic account is configured. Only one region per provider block is permitted.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="syntheticsApiUrl")
    @_utilities.deprecated("""New Relic internal use only. API URLs are now configured based on the configured region.""")
    def synthetics_api_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "synthetics_api_url")

