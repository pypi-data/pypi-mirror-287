# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['UsageArgs', 'Usage']

@pulumi.input_type
class UsageArgs:
    def __init__(__self__, *,
                 granularity: pulumi.Input[str],
                 tenant_id: pulumi.Input[str],
                 time_usage_ended: pulumi.Input[str],
                 time_usage_started: pulumi.Input[str],
                 compartment_depth: Optional[pulumi.Input[float]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 forecast: Optional[pulumi.Input['UsageForecastArgs']] = None,
                 group_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 group_by_tags: Optional[pulumi.Input[Sequence[pulumi.Input['UsageGroupByTagArgs']]]] = None,
                 is_aggregate_by_time: Optional[pulumi.Input[bool]] = None,
                 query_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Usage resource.
        :param pulumi.Input[str] granularity: The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.
        :param pulumi.Input[str] tenant_id: Tenant ID.
        :param pulumi.Input[str] time_usage_ended: The usage end time.
        :param pulumi.Input[str] time_usage_started: The usage start time.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        :param pulumi.Input[float] compartment_depth: The compartment depth level.
        :param pulumi.Input[str] filter: The filter object for query usage.
        :param pulumi.Input['UsageForecastArgs'] forecast: Forecast configuration of usage/cost.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_bies: Aggregate the result by. example: `["tagNamespace", "tagKey", "tagValue", "service", "skuName", "skuPartNumber", "unit", "compartmentName", "compartmentPath", "compartmentId", "platform", "region", "logicalAd", "resourceId", "tenantId", "tenantName"]`
        :param pulumi.Input[Sequence[pulumi.Input['UsageGroupByTagArgs']]] group_by_tags: GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{"namespace":"oracle", "key":"createdBy"]`
        :param pulumi.Input[bool] is_aggregate_by_time: Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.
        :param pulumi.Input[str] query_type: The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data. AllCredit - Query the credit adjustments and expired credit.
        """
        pulumi.set(__self__, "granularity", granularity)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "time_usage_ended", time_usage_ended)
        pulumi.set(__self__, "time_usage_started", time_usage_started)
        if compartment_depth is not None:
            pulumi.set(__self__, "compartment_depth", compartment_depth)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if forecast is not None:
            pulumi.set(__self__, "forecast", forecast)
        if group_bies is not None:
            pulumi.set(__self__, "group_bies", group_bies)
        if group_by_tags is not None:
            pulumi.set(__self__, "group_by_tags", group_by_tags)
        if is_aggregate_by_time is not None:
            pulumi.set(__self__, "is_aggregate_by_time", is_aggregate_by_time)
        if query_type is not None:
            pulumi.set(__self__, "query_type", query_type)

    @property
    @pulumi.getter
    def granularity(self) -> pulumi.Input[str]:
        """
        The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.
        """
        return pulumi.get(self, "granularity")

    @granularity.setter
    def granularity(self, value: pulumi.Input[str]):
        pulumi.set(self, "granularity", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[str]:
        """
        Tenant ID.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter(name="timeUsageEnded")
    def time_usage_ended(self) -> pulumi.Input[str]:
        """
        The usage end time.
        """
        return pulumi.get(self, "time_usage_ended")

    @time_usage_ended.setter
    def time_usage_ended(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_usage_ended", value)

    @property
    @pulumi.getter(name="timeUsageStarted")
    def time_usage_started(self) -> pulumi.Input[str]:
        """
        The usage start time.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "time_usage_started")

    @time_usage_started.setter
    def time_usage_started(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_usage_started", value)

    @property
    @pulumi.getter(name="compartmentDepth")
    def compartment_depth(self) -> Optional[pulumi.Input[float]]:
        """
        The compartment depth level.
        """
        return pulumi.get(self, "compartment_depth")

    @compartment_depth.setter
    def compartment_depth(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "compartment_depth", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        The filter object for query usage.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def forecast(self) -> Optional[pulumi.Input['UsageForecastArgs']]:
        """
        Forecast configuration of usage/cost.
        """
        return pulumi.get(self, "forecast")

    @forecast.setter
    def forecast(self, value: Optional[pulumi.Input['UsageForecastArgs']]):
        pulumi.set(self, "forecast", value)

    @property
    @pulumi.getter(name="groupBies")
    def group_bies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Aggregate the result by. example: `["tagNamespace", "tagKey", "tagValue", "service", "skuName", "skuPartNumber", "unit", "compartmentName", "compartmentPath", "compartmentId", "platform", "region", "logicalAd", "resourceId", "tenantId", "tenantName"]`
        """
        return pulumi.get(self, "group_bies")

    @group_bies.setter
    def group_bies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_bies", value)

    @property
    @pulumi.getter(name="groupByTags")
    def group_by_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UsageGroupByTagArgs']]]]:
        """
        GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{"namespace":"oracle", "key":"createdBy"]`
        """
        return pulumi.get(self, "group_by_tags")

    @group_by_tags.setter
    def group_by_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UsageGroupByTagArgs']]]]):
        pulumi.set(self, "group_by_tags", value)

    @property
    @pulumi.getter(name="isAggregateByTime")
    def is_aggregate_by_time(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.
        """
        return pulumi.get(self, "is_aggregate_by_time")

    @is_aggregate_by_time.setter
    def is_aggregate_by_time(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_aggregate_by_time", value)

    @property
    @pulumi.getter(name="queryType")
    def query_type(self) -> Optional[pulumi.Input[str]]:
        """
        The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data. AllCredit - Query the credit adjustments and expired credit.
        """
        return pulumi.get(self, "query_type")

    @query_type.setter
    def query_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query_type", value)


@pulumi.input_type
class _UsageState:
    def __init__(__self__, *,
                 compartment_depth: Optional[pulumi.Input[float]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 forecast: Optional[pulumi.Input['UsageForecastArgs']] = None,
                 granularity: Optional[pulumi.Input[str]] = None,
                 group_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 group_by_tags: Optional[pulumi.Input[Sequence[pulumi.Input['UsageGroupByTagArgs']]]] = None,
                 is_aggregate_by_time: Optional[pulumi.Input[bool]] = None,
                 items: Optional[pulumi.Input[Sequence[pulumi.Input['UsageItemArgs']]]] = None,
                 query_type: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 time_usage_ended: Optional[pulumi.Input[str]] = None,
                 time_usage_started: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Usage resources.
        :param pulumi.Input[float] compartment_depth: The compartment depth level.
        :param pulumi.Input[str] filter: The filter object for query usage.
        :param pulumi.Input['UsageForecastArgs'] forecast: Forecast configuration of usage/cost.
        :param pulumi.Input[str] granularity: The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_bies: Aggregate the result by. example: `["tagNamespace", "tagKey", "tagValue", "service", "skuName", "skuPartNumber", "unit", "compartmentName", "compartmentPath", "compartmentId", "platform", "region", "logicalAd", "resourceId", "tenantId", "tenantName"]`
        :param pulumi.Input[Sequence[pulumi.Input['UsageGroupByTagArgs']]] group_by_tags: GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{"namespace":"oracle", "key":"createdBy"]`
        :param pulumi.Input[bool] is_aggregate_by_time: Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.
        :param pulumi.Input[Sequence[pulumi.Input['UsageItemArgs']]] items: A list of usage items.
        :param pulumi.Input[str] query_type: The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data. AllCredit - Query the credit adjustments and expired credit.
        :param pulumi.Input[str] tenant_id: Tenant ID.
        :param pulumi.Input[str] time_usage_ended: The usage end time.
        :param pulumi.Input[str] time_usage_started: The usage start time.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        if compartment_depth is not None:
            pulumi.set(__self__, "compartment_depth", compartment_depth)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if forecast is not None:
            pulumi.set(__self__, "forecast", forecast)
        if granularity is not None:
            pulumi.set(__self__, "granularity", granularity)
        if group_bies is not None:
            pulumi.set(__self__, "group_bies", group_bies)
        if group_by_tags is not None:
            pulumi.set(__self__, "group_by_tags", group_by_tags)
        if is_aggregate_by_time is not None:
            pulumi.set(__self__, "is_aggregate_by_time", is_aggregate_by_time)
        if items is not None:
            pulumi.set(__self__, "items", items)
        if query_type is not None:
            pulumi.set(__self__, "query_type", query_type)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if time_usage_ended is not None:
            pulumi.set(__self__, "time_usage_ended", time_usage_ended)
        if time_usage_started is not None:
            pulumi.set(__self__, "time_usage_started", time_usage_started)

    @property
    @pulumi.getter(name="compartmentDepth")
    def compartment_depth(self) -> Optional[pulumi.Input[float]]:
        """
        The compartment depth level.
        """
        return pulumi.get(self, "compartment_depth")

    @compartment_depth.setter
    def compartment_depth(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "compartment_depth", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[str]]:
        """
        The filter object for query usage.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def forecast(self) -> Optional[pulumi.Input['UsageForecastArgs']]:
        """
        Forecast configuration of usage/cost.
        """
        return pulumi.get(self, "forecast")

    @forecast.setter
    def forecast(self, value: Optional[pulumi.Input['UsageForecastArgs']]):
        pulumi.set(self, "forecast", value)

    @property
    @pulumi.getter
    def granularity(self) -> Optional[pulumi.Input[str]]:
        """
        The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.
        """
        return pulumi.get(self, "granularity")

    @granularity.setter
    def granularity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "granularity", value)

    @property
    @pulumi.getter(name="groupBies")
    def group_bies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Aggregate the result by. example: `["tagNamespace", "tagKey", "tagValue", "service", "skuName", "skuPartNumber", "unit", "compartmentName", "compartmentPath", "compartmentId", "platform", "region", "logicalAd", "resourceId", "tenantId", "tenantName"]`
        """
        return pulumi.get(self, "group_bies")

    @group_bies.setter
    def group_bies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_bies", value)

    @property
    @pulumi.getter(name="groupByTags")
    def group_by_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UsageGroupByTagArgs']]]]:
        """
        GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{"namespace":"oracle", "key":"createdBy"]`
        """
        return pulumi.get(self, "group_by_tags")

    @group_by_tags.setter
    def group_by_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UsageGroupByTagArgs']]]]):
        pulumi.set(self, "group_by_tags", value)

    @property
    @pulumi.getter(name="isAggregateByTime")
    def is_aggregate_by_time(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.
        """
        return pulumi.get(self, "is_aggregate_by_time")

    @is_aggregate_by_time.setter
    def is_aggregate_by_time(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_aggregate_by_time", value)

    @property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UsageItemArgs']]]]:
        """
        A list of usage items.
        """
        return pulumi.get(self, "items")

    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UsageItemArgs']]]]):
        pulumi.set(self, "items", value)

    @property
    @pulumi.getter(name="queryType")
    def query_type(self) -> Optional[pulumi.Input[str]]:
        """
        The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data. AllCredit - Query the credit adjustments and expired credit.
        """
        return pulumi.get(self, "query_type")

    @query_type.setter
    def query_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query_type", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Tenant ID.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter(name="timeUsageEnded")
    def time_usage_ended(self) -> Optional[pulumi.Input[str]]:
        """
        The usage end time.
        """
        return pulumi.get(self, "time_usage_ended")

    @time_usage_ended.setter
    def time_usage_ended(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_usage_ended", value)

    @property
    @pulumi.getter(name="timeUsageStarted")
    def time_usage_started(self) -> Optional[pulumi.Input[str]]:
        """
        The usage start time.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "time_usage_started")

    @time_usage_started.setter
    def time_usage_started(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_usage_started", value)


class Usage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_depth: Optional[pulumi.Input[float]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 forecast: Optional[pulumi.Input[pulumi.InputType['UsageForecastArgs']]] = None,
                 granularity: Optional[pulumi.Input[str]] = None,
                 group_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 group_by_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsageGroupByTagArgs']]]]] = None,
                 is_aggregate_by_time: Optional[pulumi.Input[bool]] = None,
                 query_type: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 time_usage_ended: Optional[pulumi.Input[str]] = None,
                 time_usage_started: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource provides the Usage resource in Oracle Cloud Infrastructure Metering Computation service.

        Returns usage for the given account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_usage = oci.metering_computation.Usage("test_usage",
            granularity=usage_granularity,
            tenant_id=test_tenant["id"],
            time_usage_ended=usage_time_usage_ended,
            time_usage_started=usage_time_usage_started,
            compartment_depth=usage_compartment_depth,
            filter=usage_filter,
            forecast=oci.metering_computation.UsageForecastArgs(
                time_forecast_ended=usage_forecast_time_forecast_ended,
                forecast_type=usage_forecast_forecast_type,
                time_forecast_started=usage_forecast_time_forecast_started,
            ),
            group_bies=usage_group_by,
            group_by_tags=[oci.metering_computation.UsageGroupByTagArgs(
                key=usage_group_by_tag_key,
                namespace=usage_group_by_tag_namespace,
                value=usage_group_by_tag_value,
            )],
            is_aggregate_by_time=usage_is_aggregate_by_time,
            query_type=usage_query_type)
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] compartment_depth: The compartment depth level.
        :param pulumi.Input[str] filter: The filter object for query usage.
        :param pulumi.Input[pulumi.InputType['UsageForecastArgs']] forecast: Forecast configuration of usage/cost.
        :param pulumi.Input[str] granularity: The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_bies: Aggregate the result by. example: `["tagNamespace", "tagKey", "tagValue", "service", "skuName", "skuPartNumber", "unit", "compartmentName", "compartmentPath", "compartmentId", "platform", "region", "logicalAd", "resourceId", "tenantId", "tenantName"]`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsageGroupByTagArgs']]]] group_by_tags: GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{"namespace":"oracle", "key":"createdBy"]`
        :param pulumi.Input[bool] is_aggregate_by_time: Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.
        :param pulumi.Input[str] query_type: The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data. AllCredit - Query the credit adjustments and expired credit.
        :param pulumi.Input[str] tenant_id: Tenant ID.
        :param pulumi.Input[str] time_usage_ended: The usage end time.
        :param pulumi.Input[str] time_usage_started: The usage start time.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UsageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource provides the Usage resource in Oracle Cloud Infrastructure Metering Computation service.

        Returns usage for the given account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_oci as oci

        test_usage = oci.metering_computation.Usage("test_usage",
            granularity=usage_granularity,
            tenant_id=test_tenant["id"],
            time_usage_ended=usage_time_usage_ended,
            time_usage_started=usage_time_usage_started,
            compartment_depth=usage_compartment_depth,
            filter=usage_filter,
            forecast=oci.metering_computation.UsageForecastArgs(
                time_forecast_ended=usage_forecast_time_forecast_ended,
                forecast_type=usage_forecast_forecast_type,
                time_forecast_started=usage_forecast_time_forecast_started,
            ),
            group_bies=usage_group_by,
            group_by_tags=[oci.metering_computation.UsageGroupByTagArgs(
                key=usage_group_by_tag_key,
                namespace=usage_group_by_tag_namespace,
                value=usage_group_by_tag_value,
            )],
            is_aggregate_by_time=usage_is_aggregate_by_time,
            query_type=usage_query_type)
        ```

        ## Import

        Import is not supported for this resource.

        :param str resource_name: The name of the resource.
        :param UsageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UsageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compartment_depth: Optional[pulumi.Input[float]] = None,
                 filter: Optional[pulumi.Input[str]] = None,
                 forecast: Optional[pulumi.Input[pulumi.InputType['UsageForecastArgs']]] = None,
                 granularity: Optional[pulumi.Input[str]] = None,
                 group_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 group_by_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsageGroupByTagArgs']]]]] = None,
                 is_aggregate_by_time: Optional[pulumi.Input[bool]] = None,
                 query_type: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 time_usage_ended: Optional[pulumi.Input[str]] = None,
                 time_usage_started: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UsageArgs.__new__(UsageArgs)

            __props__.__dict__["compartment_depth"] = compartment_depth
            __props__.__dict__["filter"] = filter
            __props__.__dict__["forecast"] = forecast
            if granularity is None and not opts.urn:
                raise TypeError("Missing required property 'granularity'")
            __props__.__dict__["granularity"] = granularity
            __props__.__dict__["group_bies"] = group_bies
            __props__.__dict__["group_by_tags"] = group_by_tags
            __props__.__dict__["is_aggregate_by_time"] = is_aggregate_by_time
            __props__.__dict__["query_type"] = query_type
            if tenant_id is None and not opts.urn:
                raise TypeError("Missing required property 'tenant_id'")
            __props__.__dict__["tenant_id"] = tenant_id
            if time_usage_ended is None and not opts.urn:
                raise TypeError("Missing required property 'time_usage_ended'")
            __props__.__dict__["time_usage_ended"] = time_usage_ended
            if time_usage_started is None and not opts.urn:
                raise TypeError("Missing required property 'time_usage_started'")
            __props__.__dict__["time_usage_started"] = time_usage_started
            __props__.__dict__["items"] = None
        super(Usage, __self__).__init__(
            'oci:MeteringComputation/usage:Usage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compartment_depth: Optional[pulumi.Input[float]] = None,
            filter: Optional[pulumi.Input[str]] = None,
            forecast: Optional[pulumi.Input[pulumi.InputType['UsageForecastArgs']]] = None,
            granularity: Optional[pulumi.Input[str]] = None,
            group_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            group_by_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsageGroupByTagArgs']]]]] = None,
            is_aggregate_by_time: Optional[pulumi.Input[bool]] = None,
            items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsageItemArgs']]]]] = None,
            query_type: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            time_usage_ended: Optional[pulumi.Input[str]] = None,
            time_usage_started: Optional[pulumi.Input[str]] = None) -> 'Usage':
        """
        Get an existing Usage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] compartment_depth: The compartment depth level.
        :param pulumi.Input[str] filter: The filter object for query usage.
        :param pulumi.Input[pulumi.InputType['UsageForecastArgs']] forecast: Forecast configuration of usage/cost.
        :param pulumi.Input[str] granularity: The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_bies: Aggregate the result by. example: `["tagNamespace", "tagKey", "tagValue", "service", "skuName", "skuPartNumber", "unit", "compartmentName", "compartmentPath", "compartmentId", "platform", "region", "logicalAd", "resourceId", "tenantId", "tenantName"]`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsageGroupByTagArgs']]]] group_by_tags: GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{"namespace":"oracle", "key":"createdBy"]`
        :param pulumi.Input[bool] is_aggregate_by_time: Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UsageItemArgs']]]] items: A list of usage items.
        :param pulumi.Input[str] query_type: The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data. AllCredit - Query the credit adjustments and expired credit.
        :param pulumi.Input[str] tenant_id: Tenant ID.
        :param pulumi.Input[str] time_usage_ended: The usage end time.
        :param pulumi.Input[str] time_usage_started: The usage start time.
               
               
               ** IMPORTANT **
               Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UsageState.__new__(_UsageState)

        __props__.__dict__["compartment_depth"] = compartment_depth
        __props__.__dict__["filter"] = filter
        __props__.__dict__["forecast"] = forecast
        __props__.__dict__["granularity"] = granularity
        __props__.__dict__["group_bies"] = group_bies
        __props__.__dict__["group_by_tags"] = group_by_tags
        __props__.__dict__["is_aggregate_by_time"] = is_aggregate_by_time
        __props__.__dict__["items"] = items
        __props__.__dict__["query_type"] = query_type
        __props__.__dict__["tenant_id"] = tenant_id
        __props__.__dict__["time_usage_ended"] = time_usage_ended
        __props__.__dict__["time_usage_started"] = time_usage_started
        return Usage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compartmentDepth")
    def compartment_depth(self) -> pulumi.Output[float]:
        """
        The compartment depth level.
        """
        return pulumi.get(self, "compartment_depth")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[str]]:
        """
        The filter object for query usage.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def forecast(self) -> pulumi.Output['outputs.UsageForecast']:
        """
        Forecast configuration of usage/cost.
        """
        return pulumi.get(self, "forecast")

    @property
    @pulumi.getter
    def granularity(self) -> pulumi.Output[str]:
        """
        The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.
        """
        return pulumi.get(self, "granularity")

    @property
    @pulumi.getter(name="groupBies")
    def group_bies(self) -> pulumi.Output[Sequence[str]]:
        """
        Aggregate the result by. example: `["tagNamespace", "tagKey", "tagValue", "service", "skuName", "skuPartNumber", "unit", "compartmentName", "compartmentPath", "compartmentId", "platform", "region", "logicalAd", "resourceId", "tenantId", "tenantName"]`
        """
        return pulumi.get(self, "group_bies")

    @property
    @pulumi.getter(name="groupByTags")
    def group_by_tags(self) -> pulumi.Output[Sequence['outputs.UsageGroupByTag']]:
        """
        GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example: `[{"namespace":"oracle", "key":"createdBy"]`
        """
        return pulumi.get(self, "group_by_tags")

    @property
    @pulumi.getter(name="isAggregateByTime")
    def is_aggregate_by_time(self) -> pulumi.Output[bool]:
        """
        Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.
        """
        return pulumi.get(self, "is_aggregate_by_time")

    @property
    @pulumi.getter
    def items(self) -> pulumi.Output[Sequence['outputs.UsageItem']]:
        """
        A list of usage items.
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="queryType")
    def query_type(self) -> pulumi.Output[str]:
        """
        The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data. AllCredit - Query the credit adjustments and expired credit.
        """
        return pulumi.get(self, "query_type")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        Tenant ID.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="timeUsageEnded")
    def time_usage_ended(self) -> pulumi.Output[str]:
        """
        The usage end time.
        """
        return pulumi.get(self, "time_usage_ended")

    @property
    @pulumi.getter(name="timeUsageStarted")
    def time_usage_started(self) -> pulumi.Output[str]:
        """
        The usage start time.


        ** IMPORTANT **
        Any change to a property that does not support update will force the destruction and recreation of the resource with the new property values
        """
        return pulumi.get(self, "time_usage_started")

