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
    'GetApplianceTrafficShapingUplinkSelectionResult',
    'AwaitableGetApplianceTrafficShapingUplinkSelectionResult',
    'get_appliance_traffic_shaping_uplink_selection',
    'get_appliance_traffic_shaping_uplink_selection_output',
]

@pulumi.output_type
class GetApplianceTrafficShapingUplinkSelectionResult:
    """
    A collection of values returned by getApplianceTrafficShapingUplinkSelection.
    """
    def __init__(__self__, id=None, item=None, network_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if item and not isinstance(item, dict):
            raise TypeError("Expected argument 'item' to be a dict")
        pulumi.set(__self__, "item", item)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def item(self) -> 'outputs.GetApplianceTrafficShapingUplinkSelectionItemResult':
        return pulumi.get(self, "item")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")


class AwaitableGetApplianceTrafficShapingUplinkSelectionResult(GetApplianceTrafficShapingUplinkSelectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplianceTrafficShapingUplinkSelectionResult(
            id=self.id,
            item=self.item,
            network_id=self.network_id)


def get_appliance_traffic_shaping_uplink_selection(network_id: Optional[str] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplianceTrafficShapingUplinkSelectionResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.networks.get_appliance_traffic_shaping_uplink_selection(network_id="string")
    pulumi.export("merakiNetworksApplianceTrafficShapingUplinkSelectionExample", example.item)
    ```


    :param str network_id: networkId path parameter. Network ID
    """
    __args__ = dict()
    __args__['networkId'] = network_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:networks/getApplianceTrafficShapingUplinkSelection:getApplianceTrafficShapingUplinkSelection', __args__, opts=opts, typ=GetApplianceTrafficShapingUplinkSelectionResult).value

    return AwaitableGetApplianceTrafficShapingUplinkSelectionResult(
        id=pulumi.get(__ret__, 'id'),
        item=pulumi.get(__ret__, 'item'),
        network_id=pulumi.get(__ret__, 'network_id'))


@_utilities.lift_output_func(get_appliance_traffic_shaping_uplink_selection)
def get_appliance_traffic_shaping_uplink_selection_output(network_id: Optional[pulumi.Input[str]] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplianceTrafficShapingUplinkSelectionResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.networks.get_appliance_traffic_shaping_uplink_selection(network_id="string")
    pulumi.export("merakiNetworksApplianceTrafficShapingUplinkSelectionExample", example.item)
    ```


    :param str network_id: networkId path parameter. Network ID
    """
    ...
