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
    'GetLiveToolsThroughputTestResult',
    'AwaitableGetLiveToolsThroughputTestResult',
    'get_live_tools_throughput_test',
    'get_live_tools_throughput_test_output',
]

@pulumi.output_type
class GetLiveToolsThroughputTestResult:
    """
    A collection of values returned by getLiveToolsThroughputTest.
    """
    def __init__(__self__, id=None, item=None, serial=None, throughput_test_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if item and not isinstance(item, dict):
            raise TypeError("Expected argument 'item' to be a dict")
        pulumi.set(__self__, "item", item)
        if serial and not isinstance(serial, str):
            raise TypeError("Expected argument 'serial' to be a str")
        pulumi.set(__self__, "serial", serial)
        if throughput_test_id and not isinstance(throughput_test_id, str):
            raise TypeError("Expected argument 'throughput_test_id' to be a str")
        pulumi.set(__self__, "throughput_test_id", throughput_test_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def item(self) -> 'outputs.GetLiveToolsThroughputTestItemResult':
        return pulumi.get(self, "item")

    @property
    @pulumi.getter
    def serial(self) -> str:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter(name="throughputTestId")
    def throughput_test_id(self) -> str:
        """
        throughputTestId path parameter. Throughput test ID
        """
        return pulumi.get(self, "throughput_test_id")


class AwaitableGetLiveToolsThroughputTestResult(GetLiveToolsThroughputTestResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLiveToolsThroughputTestResult(
            id=self.id,
            item=self.item,
            serial=self.serial,
            throughput_test_id=self.throughput_test_id)


def get_live_tools_throughput_test(serial: Optional[str] = None,
                                   throughput_test_id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLiveToolsThroughputTestResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.devices.get_live_tools_throughput_test(serial="string",
        throughput_test_id="string")
    pulumi.export("merakiDevicesLiveToolsThroughputTestExample", example.item)
    ```


    :param str serial: serial path parameter.
    :param str throughput_test_id: throughputTestId path parameter. Throughput test ID
    """
    __args__ = dict()
    __args__['serial'] = serial
    __args__['throughputTestId'] = throughput_test_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:devices/getLiveToolsThroughputTest:getLiveToolsThroughputTest', __args__, opts=opts, typ=GetLiveToolsThroughputTestResult).value

    return AwaitableGetLiveToolsThroughputTestResult(
        id=pulumi.get(__ret__, 'id'),
        item=pulumi.get(__ret__, 'item'),
        serial=pulumi.get(__ret__, 'serial'),
        throughput_test_id=pulumi.get(__ret__, 'throughput_test_id'))


@_utilities.lift_output_func(get_live_tools_throughput_test)
def get_live_tools_throughput_test_output(serial: Optional[pulumi.Input[str]] = None,
                                          throughput_test_id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLiveToolsThroughputTestResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.devices.get_live_tools_throughput_test(serial="string",
        throughput_test_id="string")
    pulumi.export("merakiDevicesLiveToolsThroughputTestExample", example.item)
    ```


    :param str serial: serial path parameter.
    :param str throughput_test_id: throughputTestId path parameter. Throughput test ID
    """
    ...
