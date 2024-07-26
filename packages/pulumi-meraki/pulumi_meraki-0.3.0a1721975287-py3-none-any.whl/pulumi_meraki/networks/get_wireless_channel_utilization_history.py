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
    'GetWirelessChannelUtilizationHistoryResult',
    'AwaitableGetWirelessChannelUtilizationHistoryResult',
    'get_wireless_channel_utilization_history',
    'get_wireless_channel_utilization_history_output',
]

@pulumi.output_type
class GetWirelessChannelUtilizationHistoryResult:
    """
    A collection of values returned by getWirelessChannelUtilizationHistory.
    """
    def __init__(__self__, ap_tag=None, auto_resolution=None, band=None, client_id=None, device_serial=None, id=None, items=None, network_id=None, resolution=None, t0=None, t1=None, timespan=None):
        if ap_tag and not isinstance(ap_tag, str):
            raise TypeError("Expected argument 'ap_tag' to be a str")
        pulumi.set(__self__, "ap_tag", ap_tag)
        if auto_resolution and not isinstance(auto_resolution, bool):
            raise TypeError("Expected argument 'auto_resolution' to be a bool")
        pulumi.set(__self__, "auto_resolution", auto_resolution)
        if band and not isinstance(band, str):
            raise TypeError("Expected argument 'band' to be a str")
        pulumi.set(__self__, "band", band)
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if device_serial and not isinstance(device_serial, str):
            raise TypeError("Expected argument 'device_serial' to be a str")
        pulumi.set(__self__, "device_serial", device_serial)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if resolution and not isinstance(resolution, int):
            raise TypeError("Expected argument 'resolution' to be a int")
        pulumi.set(__self__, "resolution", resolution)
        if t0 and not isinstance(t0, str):
            raise TypeError("Expected argument 't0' to be a str")
        pulumi.set(__self__, "t0", t0)
        if t1 and not isinstance(t1, str):
            raise TypeError("Expected argument 't1' to be a str")
        pulumi.set(__self__, "t1", t1)
        if timespan and not isinstance(timespan, float):
            raise TypeError("Expected argument 'timespan' to be a float")
        pulumi.set(__self__, "timespan", timespan)

    @property
    @pulumi.getter(name="apTag")
    def ap_tag(self) -> Optional[str]:
        """
        apTag query parameter. Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
        """
        return pulumi.get(self, "ap_tag")

    @property
    @pulumi.getter(name="autoResolution")
    def auto_resolution(self) -> Optional[bool]:
        """
        autoResolution query parameter. Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
        """
        return pulumi.get(self, "auto_resolution")

    @property
    @pulumi.getter
    def band(self) -> Optional[str]:
        """
        band query parameter. Filter results by band (either '2.4', '5' or '6').
        """
        return pulumi.get(self, "band")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[str]:
        """
        clientId query parameter. Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="deviceSerial")
    def device_serial(self) -> Optional[str]:
        """
        deviceSerial query parameter. Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
        """
        return pulumi.get(self, "device_serial")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetWirelessChannelUtilizationHistoryItemResult']:
        """
        Array of ResponseWirelessGetNetworkWirelessChannelUtilizationHistory
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> str:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def resolution(self) -> Optional[int]:
        """
        resolution query parameter. The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
        """
        return pulumi.get(self, "resolution")

    @property
    @pulumi.getter
    def t0(self) -> Optional[str]:
        """
        t0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        """
        return pulumi.get(self, "t0")

    @property
    @pulumi.getter
    def t1(self) -> Optional[str]:
        """
        t1 query parameter. The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        """
        return pulumi.get(self, "t1")

    @property
    @pulumi.getter
    def timespan(self) -> Optional[float]:
        """
        timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        """
        return pulumi.get(self, "timespan")


class AwaitableGetWirelessChannelUtilizationHistoryResult(GetWirelessChannelUtilizationHistoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWirelessChannelUtilizationHistoryResult(
            ap_tag=self.ap_tag,
            auto_resolution=self.auto_resolution,
            band=self.band,
            client_id=self.client_id,
            device_serial=self.device_serial,
            id=self.id,
            items=self.items,
            network_id=self.network_id,
            resolution=self.resolution,
            t0=self.t0,
            t1=self.t1,
            timespan=self.timespan)


def get_wireless_channel_utilization_history(ap_tag: Optional[str] = None,
                                             auto_resolution: Optional[bool] = None,
                                             band: Optional[str] = None,
                                             client_id: Optional[str] = None,
                                             device_serial: Optional[str] = None,
                                             network_id: Optional[str] = None,
                                             resolution: Optional[int] = None,
                                             t0: Optional[str] = None,
                                             t1: Optional[str] = None,
                                             timespan: Optional[float] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWirelessChannelUtilizationHistoryResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.networks.get_wireless_channel_utilization_history(ap_tag="string",
        auto_resolution=False,
        band="string",
        client_id="string",
        device_serial="string",
        network_id="string",
        resolution=1,
        t0="string",
        t1="string",
        timespan=1)
    pulumi.export("merakiNetworksWirelessChannelUtilizationHistoryExample", example.items)
    ```


    :param str ap_tag: apTag query parameter. Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
    :param bool auto_resolution: autoResolution query parameter. Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
    :param str band: band query parameter. Filter results by band (either '2.4', '5' or '6').
    :param str client_id: clientId query parameter. Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history.
    :param str device_serial: deviceSerial query parameter. Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
    :param str network_id: networkId path parameter. Network ID
    :param int resolution: resolution query parameter. The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
    :param str t0: t0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :param str t1: t1 query parameter. The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :param float timespan: timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    """
    __args__ = dict()
    __args__['apTag'] = ap_tag
    __args__['autoResolution'] = auto_resolution
    __args__['band'] = band
    __args__['clientId'] = client_id
    __args__['deviceSerial'] = device_serial
    __args__['networkId'] = network_id
    __args__['resolution'] = resolution
    __args__['t0'] = t0
    __args__['t1'] = t1
    __args__['timespan'] = timespan
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:networks/getWirelessChannelUtilizationHistory:getWirelessChannelUtilizationHistory', __args__, opts=opts, typ=GetWirelessChannelUtilizationHistoryResult).value

    return AwaitableGetWirelessChannelUtilizationHistoryResult(
        ap_tag=pulumi.get(__ret__, 'ap_tag'),
        auto_resolution=pulumi.get(__ret__, 'auto_resolution'),
        band=pulumi.get(__ret__, 'band'),
        client_id=pulumi.get(__ret__, 'client_id'),
        device_serial=pulumi.get(__ret__, 'device_serial'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        network_id=pulumi.get(__ret__, 'network_id'),
        resolution=pulumi.get(__ret__, 'resolution'),
        t0=pulumi.get(__ret__, 't0'),
        t1=pulumi.get(__ret__, 't1'),
        timespan=pulumi.get(__ret__, 'timespan'))


@_utilities.lift_output_func(get_wireless_channel_utilization_history)
def get_wireless_channel_utilization_history_output(ap_tag: Optional[pulumi.Input[Optional[str]]] = None,
                                                    auto_resolution: Optional[pulumi.Input[Optional[bool]]] = None,
                                                    band: Optional[pulumi.Input[Optional[str]]] = None,
                                                    client_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                    device_serial: Optional[pulumi.Input[Optional[str]]] = None,
                                                    network_id: Optional[pulumi.Input[str]] = None,
                                                    resolution: Optional[pulumi.Input[Optional[int]]] = None,
                                                    t0: Optional[pulumi.Input[Optional[str]]] = None,
                                                    t1: Optional[pulumi.Input[Optional[str]]] = None,
                                                    timespan: Optional[pulumi.Input[Optional[float]]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWirelessChannelUtilizationHistoryResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.networks.get_wireless_channel_utilization_history(ap_tag="string",
        auto_resolution=False,
        band="string",
        client_id="string",
        device_serial="string",
        network_id="string",
        resolution=1,
        t0="string",
        t1="string",
        timespan=1)
    pulumi.export("merakiNetworksWirelessChannelUtilizationHistoryExample", example.items)
    ```


    :param str ap_tag: apTag query parameter. Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
    :param bool auto_resolution: autoResolution query parameter. Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
    :param str band: band query parameter. Filter results by band (either '2.4', '5' or '6').
    :param str client_id: clientId query parameter. Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history.
    :param str device_serial: deviceSerial query parameter. Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
    :param str network_id: networkId path parameter. Network ID
    :param int resolution: resolution query parameter. The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
    :param str t0: t0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :param str t1: t1 query parameter. The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :param float timespan: timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    """
    ...
