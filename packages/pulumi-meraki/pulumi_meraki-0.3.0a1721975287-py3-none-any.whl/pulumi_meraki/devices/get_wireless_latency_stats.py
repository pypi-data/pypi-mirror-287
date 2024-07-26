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
    'GetWirelessLatencyStatsResult',
    'AwaitableGetWirelessLatencyStatsResult',
    'get_wireless_latency_stats',
    'get_wireless_latency_stats_output',
]

@pulumi.output_type
class GetWirelessLatencyStatsResult:
    """
    A collection of values returned by getWirelessLatencyStats.
    """
    def __init__(__self__, ap_tag=None, band=None, fields=None, id=None, item=None, serial=None, ssid=None, t0=None, t1=None, timespan=None, vlan=None):
        if ap_tag and not isinstance(ap_tag, str):
            raise TypeError("Expected argument 'ap_tag' to be a str")
        pulumi.set(__self__, "ap_tag", ap_tag)
        if band and not isinstance(band, str):
            raise TypeError("Expected argument 'band' to be a str")
        pulumi.set(__self__, "band", band)
        if fields and not isinstance(fields, str):
            raise TypeError("Expected argument 'fields' to be a str")
        pulumi.set(__self__, "fields", fields)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if item and not isinstance(item, dict):
            raise TypeError("Expected argument 'item' to be a dict")
        pulumi.set(__self__, "item", item)
        if serial and not isinstance(serial, str):
            raise TypeError("Expected argument 'serial' to be a str")
        pulumi.set(__self__, "serial", serial)
        if ssid and not isinstance(ssid, int):
            raise TypeError("Expected argument 'ssid' to be a int")
        pulumi.set(__self__, "ssid", ssid)
        if t0 and not isinstance(t0, str):
            raise TypeError("Expected argument 't0' to be a str")
        pulumi.set(__self__, "t0", t0)
        if t1 and not isinstance(t1, str):
            raise TypeError("Expected argument 't1' to be a str")
        pulumi.set(__self__, "t1", t1)
        if timespan and not isinstance(timespan, float):
            raise TypeError("Expected argument 'timespan' to be a float")
        pulumi.set(__self__, "timespan", timespan)
        if vlan and not isinstance(vlan, int):
            raise TypeError("Expected argument 'vlan' to be a int")
        pulumi.set(__self__, "vlan", vlan)

    @property
    @pulumi.getter(name="apTag")
    def ap_tag(self) -> Optional[str]:
        """
        apTag query parameter. Filter results by AP Tag
        """
        return pulumi.get(self, "ap_tag")

    @property
    @pulumi.getter
    def band(self) -> Optional[str]:
        """
        band query parameter. Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        """
        return pulumi.get(self, "band")

    @property
    @pulumi.getter
    def fields(self) -> Optional[str]:
        """
        fields query parameter. Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def item(self) -> 'outputs.GetWirelessLatencyStatsItemResult':
        return pulumi.get(self, "item")

    @property
    @pulumi.getter
    def serial(self) -> str:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter
    def ssid(self) -> Optional[int]:
        """
        ssid query parameter. Filter results by SSID
        """
        return pulumi.get(self, "ssid")

    @property
    @pulumi.getter
    def t0(self) -> Optional[str]:
        """
        t0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        """
        return pulumi.get(self, "t0")

    @property
    @pulumi.getter
    def t1(self) -> Optional[str]:
        """
        t1 query parameter. The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        """
        return pulumi.get(self, "t1")

    @property
    @pulumi.getter
    def timespan(self) -> Optional[float]:
        """
        timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        """
        return pulumi.get(self, "timespan")

    @property
    @pulumi.getter
    def vlan(self) -> Optional[int]:
        """
        vlan query parameter. Filter results by VLAN
        """
        return pulumi.get(self, "vlan")


class AwaitableGetWirelessLatencyStatsResult(GetWirelessLatencyStatsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWirelessLatencyStatsResult(
            ap_tag=self.ap_tag,
            band=self.band,
            fields=self.fields,
            id=self.id,
            item=self.item,
            serial=self.serial,
            ssid=self.ssid,
            t0=self.t0,
            t1=self.t1,
            timespan=self.timespan,
            vlan=self.vlan)


def get_wireless_latency_stats(ap_tag: Optional[str] = None,
                               band: Optional[str] = None,
                               fields: Optional[str] = None,
                               serial: Optional[str] = None,
                               ssid: Optional[int] = None,
                               t0: Optional[str] = None,
                               t1: Optional[str] = None,
                               timespan: Optional[float] = None,
                               vlan: Optional[int] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWirelessLatencyStatsResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.devices.get_wireless_latency_stats(ap_tag="string",
        band="string",
        fields="string",
        serial="string",
        ssid=1,
        t0="string",
        t1="string",
        timespan=1,
        vlan=1)
    pulumi.export("merakiDevicesWirelessLatencyStatsExample", example.item)
    ```


    :param str ap_tag: apTag query parameter. Filter results by AP Tag
    :param str band: band query parameter. Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    :param str fields: fields query parameter. Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    :param str serial: serial path parameter.
    :param int ssid: ssid query parameter. Filter results by SSID
    :param str t0: t0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :param str t1: t1 query parameter. The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :param float timespan: timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :param int vlan: vlan query parameter. Filter results by VLAN
    """
    __args__ = dict()
    __args__['apTag'] = ap_tag
    __args__['band'] = band
    __args__['fields'] = fields
    __args__['serial'] = serial
    __args__['ssid'] = ssid
    __args__['t0'] = t0
    __args__['t1'] = t1
    __args__['timespan'] = timespan
    __args__['vlan'] = vlan
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:devices/getWirelessLatencyStats:getWirelessLatencyStats', __args__, opts=opts, typ=GetWirelessLatencyStatsResult).value

    return AwaitableGetWirelessLatencyStatsResult(
        ap_tag=pulumi.get(__ret__, 'ap_tag'),
        band=pulumi.get(__ret__, 'band'),
        fields=pulumi.get(__ret__, 'fields'),
        id=pulumi.get(__ret__, 'id'),
        item=pulumi.get(__ret__, 'item'),
        serial=pulumi.get(__ret__, 'serial'),
        ssid=pulumi.get(__ret__, 'ssid'),
        t0=pulumi.get(__ret__, 't0'),
        t1=pulumi.get(__ret__, 't1'),
        timespan=pulumi.get(__ret__, 'timespan'),
        vlan=pulumi.get(__ret__, 'vlan'))


@_utilities.lift_output_func(get_wireless_latency_stats)
def get_wireless_latency_stats_output(ap_tag: Optional[pulumi.Input[Optional[str]]] = None,
                                      band: Optional[pulumi.Input[Optional[str]]] = None,
                                      fields: Optional[pulumi.Input[Optional[str]]] = None,
                                      serial: Optional[pulumi.Input[str]] = None,
                                      ssid: Optional[pulumi.Input[Optional[int]]] = None,
                                      t0: Optional[pulumi.Input[Optional[str]]] = None,
                                      t1: Optional[pulumi.Input[Optional[str]]] = None,
                                      timespan: Optional[pulumi.Input[Optional[float]]] = None,
                                      vlan: Optional[pulumi.Input[Optional[int]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWirelessLatencyStatsResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.devices.get_wireless_latency_stats(ap_tag="string",
        band="string",
        fields="string",
        serial="string",
        ssid=1,
        t0="string",
        t1="string",
        timespan=1,
        vlan=1)
    pulumi.export("merakiDevicesWirelessLatencyStatsExample", example.item)
    ```


    :param str ap_tag: apTag query parameter. Filter results by AP Tag
    :param str band: band query parameter. Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    :param str fields: fields query parameter. Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    :param str serial: serial path parameter.
    :param int ssid: ssid query parameter. Filter results by SSID
    :param str t0: t0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :param str t1: t1 query parameter. The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :param float timespan: timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :param int vlan: vlan query parameter. Filter results by VLAN
    """
    ...
