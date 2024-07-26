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
    'GetSmDevicesSecurityCentersResult',
    'AwaitableGetSmDevicesSecurityCentersResult',
    'get_sm_devices_security_centers',
    'get_sm_devices_security_centers_output',
]

@pulumi.output_type
class GetSmDevicesSecurityCentersResult:
    """
    A collection of values returned by getSmDevicesSecurityCenters.
    """
    def __init__(__self__, device_id=None, id=None, items=None, network_id=None):
        if device_id and not isinstance(device_id, str):
            raise TypeError("Expected argument 'device_id' to be a str")
        pulumi.set(__self__, "device_id", device_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[str]:
        """
        deviceId path parameter. Device ID
        """
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetSmDevicesSecurityCentersItemResult']:
        """
        Array of ResponseSmGetNetworkSmDeviceSoftwares
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")


class AwaitableGetSmDevicesSecurityCentersResult(GetSmDevicesSecurityCentersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSmDevicesSecurityCentersResult(
            device_id=self.device_id,
            id=self.id,
            items=self.items,
            network_id=self.network_id)


def get_sm_devices_security_centers(device_id: Optional[str] = None,
                                    network_id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSmDevicesSecurityCentersResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.networks.get_sm_devices_security_centers(device_id="string",
        network_id="string")
    pulumi.export("merakiNetworksSmDevicesSecurityCentersExample", example.items)
    ```


    :param str device_id: deviceId path parameter. Device ID
    :param str network_id: networkId path parameter. Network ID
    """
    __args__ = dict()
    __args__['deviceId'] = device_id
    __args__['networkId'] = network_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:networks/getSmDevicesSecurityCenters:getSmDevicesSecurityCenters', __args__, opts=opts, typ=GetSmDevicesSecurityCentersResult).value

    return AwaitableGetSmDevicesSecurityCentersResult(
        device_id=pulumi.get(__ret__, 'device_id'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        network_id=pulumi.get(__ret__, 'network_id'))


@_utilities.lift_output_func(get_sm_devices_security_centers)
def get_sm_devices_security_centers_output(device_id: Optional[pulumi.Input[Optional[str]]] = None,
                                           network_id: Optional[pulumi.Input[Optional[str]]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSmDevicesSecurityCentersResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.networks.get_sm_devices_security_centers(device_id="string",
        network_id="string")
    pulumi.export("merakiNetworksSmDevicesSecurityCentersExample", example.items)
    ```


    :param str device_id: deviceId path parameter. Device ID
    :param str network_id: networkId path parameter. Network ID
    """
    ...
