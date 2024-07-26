# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'IntegrationCustomNamespaceSyncRule',
    'IntegrationMetricStatsToSync',
    'IntegrationNamespaceSyncRule',
]

@pulumi.output_type
class IntegrationCustomNamespaceSyncRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultAction":
            suggest = "default_action"
        elif key == "filterAction":
            suggest = "filter_action"
        elif key == "filterSource":
            suggest = "filter_source"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IntegrationCustomNamespaceSyncRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IntegrationCustomNamespaceSyncRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IntegrationCustomNamespaceSyncRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 namespace: str,
                 default_action: Optional[str] = None,
                 filter_action: Optional[str] = None,
                 filter_source: Optional[str] = None):
        """
        :param str namespace: An AWS custom namespace having custom AWS metrics that you want to sync with Splunk Observability Cloud. See the AWS documentation on publishing metrics for more information.
        :param str default_action: Controls the Splunk Observability Cloud default behavior for processing data from an AWS namespace. Splunk Observability Cloud ignores this property unless you specify the `filter_action` and `filter_source` properties. If you do specify them, use this property to control how Splunk Observability Cloud treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
        :param str filter_action: Controls how Splunk Observability Cloud processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
        :param str filter_source: Expression that selects the data that Splunk Observability Cloud should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
        """
        pulumi.set(__self__, "namespace", namespace)
        if default_action is not None:
            pulumi.set(__self__, "default_action", default_action)
        if filter_action is not None:
            pulumi.set(__self__, "filter_action", filter_action)
        if filter_source is not None:
            pulumi.set(__self__, "filter_source", filter_source)

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        An AWS custom namespace having custom AWS metrics that you want to sync with Splunk Observability Cloud. See the AWS documentation on publishing metrics for more information.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[str]:
        """
        Controls the Splunk Observability Cloud default behavior for processing data from an AWS namespace. Splunk Observability Cloud ignores this property unless you specify the `filter_action` and `filter_source` properties. If you do specify them, use this property to control how Splunk Observability Cloud treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter(name="filterAction")
    def filter_action(self) -> Optional[str]:
        """
        Controls how Splunk Observability Cloud processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
        """
        return pulumi.get(self, "filter_action")

    @property
    @pulumi.getter(name="filterSource")
    def filter_source(self) -> Optional[str]:
        """
        Expression that selects the data that Splunk Observability Cloud should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
        """
        return pulumi.get(self, "filter_source")


@pulumi.output_type
class IntegrationMetricStatsToSync(dict):
    def __init__(__self__, *,
                 metric: str,
                 namespace: str,
                 stats: Sequence[str]):
        """
        :param str metric: AWS metric that you want to pick statistics for
        :param str namespace: An AWS namespace having AWS metric that you want to pick statistics for
        :param Sequence[str] stats: AWS statistics you want to collect
        """
        pulumi.set(__self__, "metric", metric)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "stats", stats)

    @property
    @pulumi.getter
    def metric(self) -> str:
        """
        AWS metric that you want to pick statistics for
        """
        return pulumi.get(self, "metric")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        An AWS namespace having AWS metric that you want to pick statistics for
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def stats(self) -> Sequence[str]:
        """
        AWS statistics you want to collect
        """
        return pulumi.get(self, "stats")


@pulumi.output_type
class IntegrationNamespaceSyncRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultAction":
            suggest = "default_action"
        elif key == "filterAction":
            suggest = "filter_action"
        elif key == "filterSource":
            suggest = "filter_source"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IntegrationNamespaceSyncRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IntegrationNamespaceSyncRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IntegrationNamespaceSyncRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 namespace: str,
                 default_action: Optional[str] = None,
                 filter_action: Optional[str] = None,
                 filter_source: Optional[str] = None):
        """
        :param str namespace: An AWS custom namespace having custom AWS metrics that you want to sync with Splunk Observability Cloud. See `services` field description below for additional information.
        :param str default_action: Controls the Splunk Observability Cloud default behavior for processing data from an AWS namespace. Splunk Observability Cloud ignores this property unless you specify the `filter_action` and `filter_source` properties. If you do specify them, use this property to control how Splunk Observability Cloud treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
        :param str filter_action: Controls how Splunk Observability Cloud processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
        :param str filter_source: Expression that selects the data that Splunk Observability Cloud should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
        """
        pulumi.set(__self__, "namespace", namespace)
        if default_action is not None:
            pulumi.set(__self__, "default_action", default_action)
        if filter_action is not None:
            pulumi.set(__self__, "filter_action", filter_action)
        if filter_source is not None:
            pulumi.set(__self__, "filter_source", filter_source)

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        An AWS custom namespace having custom AWS metrics that you want to sync with Splunk Observability Cloud. See `services` field description below for additional information.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[str]:
        """
        Controls the Splunk Observability Cloud default behavior for processing data from an AWS namespace. Splunk Observability Cloud ignores this property unless you specify the `filter_action` and `filter_source` properties. If you do specify them, use this property to control how Splunk Observability Cloud treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter(name="filterAction")
    def filter_action(self) -> Optional[str]:
        """
        Controls how Splunk Observability Cloud processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
        """
        return pulumi.get(self, "filter_action")

    @property
    @pulumi.getter(name="filterSource")
    def filter_source(self) -> Optional[str]:
        """
        Expression that selects the data that Splunk Observability Cloud should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
        """
        return pulumi.get(self, "filter_source")


