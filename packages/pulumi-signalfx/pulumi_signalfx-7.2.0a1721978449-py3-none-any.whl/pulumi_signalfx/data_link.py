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
from ._inputs import *

__all__ = ['DataLinkArgs', 'DataLink']

@pulumi.input_type
class DataLinkArgs:
    def __init__(__self__, *,
                 context_dashboard_id: Optional[pulumi.Input[str]] = None,
                 property_name: Optional[pulumi.Input[str]] = None,
                 property_value: Optional[pulumi.Input[str]] = None,
                 target_external_urls: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetExternalUrlArgs']]]] = None,
                 target_signalfx_dashboards: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSignalfxDashboardArgs']]]] = None,
                 target_splunks: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSplunkArgs']]]] = None):
        """
        The set of arguments for constructing a DataLink resource.
        :param pulumi.Input[str] context_dashboard_id: If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
        :param pulumi.Input[str] property_name: Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
        :param pulumi.Input[str] property_value: Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
        :param pulumi.Input[Sequence[pulumi.Input['DataLinkTargetExternalUrlArgs']]] target_external_urls: Link to an external URL
        :param pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSignalfxDashboardArgs']]] target_signalfx_dashboards: Link to a Splunk Observability Cloud dashboard
        :param pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSplunkArgs']]] target_splunks: Link to an external URL
        """
        if context_dashboard_id is not None:
            pulumi.set(__self__, "context_dashboard_id", context_dashboard_id)
        if property_name is not None:
            pulumi.set(__self__, "property_name", property_name)
        if property_value is not None:
            pulumi.set(__self__, "property_value", property_value)
        if target_external_urls is not None:
            pulumi.set(__self__, "target_external_urls", target_external_urls)
        if target_signalfx_dashboards is not None:
            pulumi.set(__self__, "target_signalfx_dashboards", target_signalfx_dashboards)
        if target_splunks is not None:
            pulumi.set(__self__, "target_splunks", target_splunks)

    @property
    @pulumi.getter(name="contextDashboardId")
    def context_dashboard_id(self) -> Optional[pulumi.Input[str]]:
        """
        If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
        """
        return pulumi.get(self, "context_dashboard_id")

    @context_dashboard_id.setter
    def context_dashboard_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context_dashboard_id", value)

    @property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
        """
        return pulumi.get(self, "property_name")

    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_name", value)

    @property
    @pulumi.getter(name="propertyValue")
    def property_value(self) -> Optional[pulumi.Input[str]]:
        """
        Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
        """
        return pulumi.get(self, "property_value")

    @property_value.setter
    def property_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_value", value)

    @property
    @pulumi.getter(name="targetExternalUrls")
    def target_external_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetExternalUrlArgs']]]]:
        """
        Link to an external URL
        """
        return pulumi.get(self, "target_external_urls")

    @target_external_urls.setter
    def target_external_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetExternalUrlArgs']]]]):
        pulumi.set(self, "target_external_urls", value)

    @property
    @pulumi.getter(name="targetSignalfxDashboards")
    def target_signalfx_dashboards(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSignalfxDashboardArgs']]]]:
        """
        Link to a Splunk Observability Cloud dashboard
        """
        return pulumi.get(self, "target_signalfx_dashboards")

    @target_signalfx_dashboards.setter
    def target_signalfx_dashboards(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSignalfxDashboardArgs']]]]):
        pulumi.set(self, "target_signalfx_dashboards", value)

    @property
    @pulumi.getter(name="targetSplunks")
    def target_splunks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSplunkArgs']]]]:
        """
        Link to an external URL
        """
        return pulumi.get(self, "target_splunks")

    @target_splunks.setter
    def target_splunks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSplunkArgs']]]]):
        pulumi.set(self, "target_splunks", value)


@pulumi.input_type
class _DataLinkState:
    def __init__(__self__, *,
                 context_dashboard_id: Optional[pulumi.Input[str]] = None,
                 property_name: Optional[pulumi.Input[str]] = None,
                 property_value: Optional[pulumi.Input[str]] = None,
                 target_external_urls: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetExternalUrlArgs']]]] = None,
                 target_signalfx_dashboards: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSignalfxDashboardArgs']]]] = None,
                 target_splunks: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSplunkArgs']]]] = None):
        """
        Input properties used for looking up and filtering DataLink resources.
        :param pulumi.Input[str] context_dashboard_id: If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
        :param pulumi.Input[str] property_name: Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
        :param pulumi.Input[str] property_value: Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
        :param pulumi.Input[Sequence[pulumi.Input['DataLinkTargetExternalUrlArgs']]] target_external_urls: Link to an external URL
        :param pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSignalfxDashboardArgs']]] target_signalfx_dashboards: Link to a Splunk Observability Cloud dashboard
        :param pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSplunkArgs']]] target_splunks: Link to an external URL
        """
        if context_dashboard_id is not None:
            pulumi.set(__self__, "context_dashboard_id", context_dashboard_id)
        if property_name is not None:
            pulumi.set(__self__, "property_name", property_name)
        if property_value is not None:
            pulumi.set(__self__, "property_value", property_value)
        if target_external_urls is not None:
            pulumi.set(__self__, "target_external_urls", target_external_urls)
        if target_signalfx_dashboards is not None:
            pulumi.set(__self__, "target_signalfx_dashboards", target_signalfx_dashboards)
        if target_splunks is not None:
            pulumi.set(__self__, "target_splunks", target_splunks)

    @property
    @pulumi.getter(name="contextDashboardId")
    def context_dashboard_id(self) -> Optional[pulumi.Input[str]]:
        """
        If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
        """
        return pulumi.get(self, "context_dashboard_id")

    @context_dashboard_id.setter
    def context_dashboard_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context_dashboard_id", value)

    @property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
        """
        return pulumi.get(self, "property_name")

    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_name", value)

    @property
    @pulumi.getter(name="propertyValue")
    def property_value(self) -> Optional[pulumi.Input[str]]:
        """
        Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
        """
        return pulumi.get(self, "property_value")

    @property_value.setter
    def property_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_value", value)

    @property
    @pulumi.getter(name="targetExternalUrls")
    def target_external_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetExternalUrlArgs']]]]:
        """
        Link to an external URL
        """
        return pulumi.get(self, "target_external_urls")

    @target_external_urls.setter
    def target_external_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetExternalUrlArgs']]]]):
        pulumi.set(self, "target_external_urls", value)

    @property
    @pulumi.getter(name="targetSignalfxDashboards")
    def target_signalfx_dashboards(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSignalfxDashboardArgs']]]]:
        """
        Link to a Splunk Observability Cloud dashboard
        """
        return pulumi.get(self, "target_signalfx_dashboards")

    @target_signalfx_dashboards.setter
    def target_signalfx_dashboards(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSignalfxDashboardArgs']]]]):
        pulumi.set(self, "target_signalfx_dashboards", value)

    @property
    @pulumi.getter(name="targetSplunks")
    def target_splunks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSplunkArgs']]]]:
        """
        Link to an external URL
        """
        return pulumi.get(self, "target_splunks")

    @target_splunks.setter
    def target_splunks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataLinkTargetSplunkArgs']]]]):
        pulumi.set(self, "target_splunks", value)


class DataLink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context_dashboard_id: Optional[pulumi.Input[str]] = None,
                 property_name: Optional[pulumi.Input[str]] = None,
                 property_value: Optional[pulumi.Input[str]] = None,
                 target_external_urls: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetExternalUrlArgs']]]]] = None,
                 target_signalfx_dashboards: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSignalfxDashboardArgs']]]]] = None,
                 target_splunks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSplunkArgs']]]]] = None,
                 __props__=None):
        """
        Manage Splunk Observability Cloud [Data Links](https://docs.signalfx.com/en/latest/managing/data-links.html).

        ## Example

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] context_dashboard_id: If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
        :param pulumi.Input[str] property_name: Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
        :param pulumi.Input[str] property_value: Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetExternalUrlArgs']]]] target_external_urls: Link to an external URL
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSignalfxDashboardArgs']]]] target_signalfx_dashboards: Link to a Splunk Observability Cloud dashboard
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSplunkArgs']]]] target_splunks: Link to an external URL
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DataLinkArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manage Splunk Observability Cloud [Data Links](https://docs.signalfx.com/en/latest/managing/data-links.html).

        ## Example

        :param str resource_name: The name of the resource.
        :param DataLinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataLinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context_dashboard_id: Optional[pulumi.Input[str]] = None,
                 property_name: Optional[pulumi.Input[str]] = None,
                 property_value: Optional[pulumi.Input[str]] = None,
                 target_external_urls: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetExternalUrlArgs']]]]] = None,
                 target_signalfx_dashboards: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSignalfxDashboardArgs']]]]] = None,
                 target_splunks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSplunkArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataLinkArgs.__new__(DataLinkArgs)

            __props__.__dict__["context_dashboard_id"] = context_dashboard_id
            __props__.__dict__["property_name"] = property_name
            __props__.__dict__["property_value"] = property_value
            __props__.__dict__["target_external_urls"] = target_external_urls
            __props__.__dict__["target_signalfx_dashboards"] = target_signalfx_dashboards
            __props__.__dict__["target_splunks"] = target_splunks
        super(DataLink, __self__).__init__(
            'signalfx:index/dataLink:DataLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            context_dashboard_id: Optional[pulumi.Input[str]] = None,
            property_name: Optional[pulumi.Input[str]] = None,
            property_value: Optional[pulumi.Input[str]] = None,
            target_external_urls: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetExternalUrlArgs']]]]] = None,
            target_signalfx_dashboards: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSignalfxDashboardArgs']]]]] = None,
            target_splunks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSplunkArgs']]]]] = None) -> 'DataLink':
        """
        Get an existing DataLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] context_dashboard_id: If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
        :param pulumi.Input[str] property_name: Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
        :param pulumi.Input[str] property_value: Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetExternalUrlArgs']]]] target_external_urls: Link to an external URL
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSignalfxDashboardArgs']]]] target_signalfx_dashboards: Link to a Splunk Observability Cloud dashboard
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataLinkTargetSplunkArgs']]]] target_splunks: Link to an external URL
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DataLinkState.__new__(_DataLinkState)

        __props__.__dict__["context_dashboard_id"] = context_dashboard_id
        __props__.__dict__["property_name"] = property_name
        __props__.__dict__["property_value"] = property_value
        __props__.__dict__["target_external_urls"] = target_external_urls
        __props__.__dict__["target_signalfx_dashboards"] = target_signalfx_dashboards
        __props__.__dict__["target_splunks"] = target_splunks
        return DataLink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contextDashboardId")
    def context_dashboard_id(self) -> pulumi.Output[Optional[str]]:
        """
        If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
        """
        return pulumi.get(self, "context_dashboard_id")

    @property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
        """
        return pulumi.get(self, "property_name")

    @property
    @pulumi.getter(name="propertyValue")
    def property_value(self) -> pulumi.Output[Optional[str]]:
        """
        Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
        """
        return pulumi.get(self, "property_value")

    @property
    @pulumi.getter(name="targetExternalUrls")
    def target_external_urls(self) -> pulumi.Output[Optional[Sequence['outputs.DataLinkTargetExternalUrl']]]:
        """
        Link to an external URL
        """
        return pulumi.get(self, "target_external_urls")

    @property
    @pulumi.getter(name="targetSignalfxDashboards")
    def target_signalfx_dashboards(self) -> pulumi.Output[Optional[Sequence['outputs.DataLinkTargetSignalfxDashboard']]]:
        """
        Link to a Splunk Observability Cloud dashboard
        """
        return pulumi.get(self, "target_signalfx_dashboards")

    @property
    @pulumi.getter(name="targetSplunks")
    def target_splunks(self) -> pulumi.Output[Optional[Sequence['outputs.DataLinkTargetSplunk']]]:
        """
        Link to an external URL
        """
        return pulumi.get(self, "target_splunks")

