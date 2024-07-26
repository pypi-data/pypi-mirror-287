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

__all__ = [
    'GetInsightMonitoredMediaServersResult',
    'AwaitableGetInsightMonitoredMediaServersResult',
    'get_insight_monitored_media_servers',
    'get_insight_monitored_media_servers_output',
]

@pulumi.output_type
class GetInsightMonitoredMediaServersResult:
    """
    A collection of values returned by getInsightMonitoredMediaServers.
    """
    def __init__(__self__, id=None, item=None, items=None, monitored_media_server_id=None, organization_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if item and not isinstance(item, dict):
            raise TypeError("Expected argument 'item' to be a dict")
        pulumi.set(__self__, "item", item)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if monitored_media_server_id and not isinstance(monitored_media_server_id, str):
            raise TypeError("Expected argument 'monitored_media_server_id' to be a str")
        pulumi.set(__self__, "monitored_media_server_id", monitored_media_server_id)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def item(self) -> 'outputs.GetInsightMonitoredMediaServersItemResult':
        return pulumi.get(self, "item")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetInsightMonitoredMediaServersItemResult']:
        """
        Array of ResponseInsightGetOrganizationInsightMonitoredMediaServers
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="monitoredMediaServerId")
    def monitored_media_server_id(self) -> Optional[str]:
        """
        monitoredMediaServerId path parameter. Monitored media server ID
        """
        return pulumi.get(self, "monitored_media_server_id")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[str]:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")


class AwaitableGetInsightMonitoredMediaServersResult(GetInsightMonitoredMediaServersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInsightMonitoredMediaServersResult(
            id=self.id,
            item=self.item,
            items=self.items,
            monitored_media_server_id=self.monitored_media_server_id,
            organization_id=self.organization_id)


def get_insight_monitored_media_servers(monitored_media_server_id: Optional[str] = None,
                                        organization_id: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInsightMonitoredMediaServersResult:
    """
    ## Example Usage


    :param str monitored_media_server_id: monitoredMediaServerId path parameter. Monitored media server ID
    :param str organization_id: organizationId path parameter. Organization ID
    """
    __args__ = dict()
    __args__['monitoredMediaServerId'] = monitored_media_server_id
    __args__['organizationId'] = organization_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:organizations/getInsightMonitoredMediaServers:getInsightMonitoredMediaServers', __args__, opts=opts, typ=GetInsightMonitoredMediaServersResult).value

    return AwaitableGetInsightMonitoredMediaServersResult(
        id=pulumi.get(__ret__, 'id'),
        item=pulumi.get(__ret__, 'item'),
        items=pulumi.get(__ret__, 'items'),
        monitored_media_server_id=pulumi.get(__ret__, 'monitored_media_server_id'),
        organization_id=pulumi.get(__ret__, 'organization_id'))


@_utilities.lift_output_func(get_insight_monitored_media_servers)
def get_insight_monitored_media_servers_output(monitored_media_server_id: Optional[pulumi.Input[Optional[str]]] = None,
                                               organization_id: Optional[pulumi.Input[Optional[str]]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInsightMonitoredMediaServersResult]:
    """
    ## Example Usage


    :param str monitored_media_server_id: monitoredMediaServerId path parameter. Monitored media server ID
    :param str organization_id: organizationId path parameter. Organization ID
    """
    ...
