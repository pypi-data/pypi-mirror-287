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
    'GetApplianceSsidsResult',
    'AwaitableGetApplianceSsidsResult',
    'get_appliance_ssids',
    'get_appliance_ssids_output',
]

@pulumi.output_type
class GetApplianceSsidsResult:
    """
    A collection of values returned by getApplianceSsids.
    """
    def __init__(__self__, id=None, item=None, items=None, network_id=None, number=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if item and not isinstance(item, dict):
            raise TypeError("Expected argument 'item' to be a dict")
        pulumi.set(__self__, "item", item)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if number and not isinstance(number, str):
            raise TypeError("Expected argument 'number' to be a str")
        pulumi.set(__self__, "number", number)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def item(self) -> 'outputs.GetApplianceSsidsItemResult':
        return pulumi.get(self, "item")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetApplianceSsidsItemResult']:
        """
        Array of ResponseApplianceGetNetworkApplianceSsids
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def number(self) -> Optional[str]:
        """
        number path parameter.
        """
        return pulumi.get(self, "number")


class AwaitableGetApplianceSsidsResult(GetApplianceSsidsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplianceSsidsResult(
            id=self.id,
            item=self.item,
            items=self.items,
            network_id=self.network_id,
            number=self.number)


def get_appliance_ssids(network_id: Optional[str] = None,
                        number: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplianceSsidsResult:
    """
    ## Example Usage


    :param str network_id: networkId path parameter. Network ID
    :param str number: number path parameter.
    """
    __args__ = dict()
    __args__['networkId'] = network_id
    __args__['number'] = number
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:networks/getApplianceSsids:getApplianceSsids', __args__, opts=opts, typ=GetApplianceSsidsResult).value

    return AwaitableGetApplianceSsidsResult(
        id=pulumi.get(__ret__, 'id'),
        item=pulumi.get(__ret__, 'item'),
        items=pulumi.get(__ret__, 'items'),
        network_id=pulumi.get(__ret__, 'network_id'),
        number=pulumi.get(__ret__, 'number'))


@_utilities.lift_output_func(get_appliance_ssids)
def get_appliance_ssids_output(network_id: Optional[pulumi.Input[Optional[str]]] = None,
                               number: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplianceSsidsResult]:
    """
    ## Example Usage


    :param str network_id: networkId path parameter. Network ID
    :param str number: number path parameter.
    """
    ...
