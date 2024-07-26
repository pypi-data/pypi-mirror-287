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
    'GetSwitchPortsResult',
    'AwaitableGetSwitchPortsResult',
    'get_switch_ports',
    'get_switch_ports_output',
]

@pulumi.output_type
class GetSwitchPortsResult:
    """
    A collection of values returned by getSwitchPorts.
    """
    def __init__(__self__, id=None, item=None, items=None, port_id=None, serial=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if item and not isinstance(item, dict):
            raise TypeError("Expected argument 'item' to be a dict")
        pulumi.set(__self__, "item", item)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if port_id and not isinstance(port_id, str):
            raise TypeError("Expected argument 'port_id' to be a str")
        pulumi.set(__self__, "port_id", port_id)
        if serial and not isinstance(serial, str):
            raise TypeError("Expected argument 'serial' to be a str")
        pulumi.set(__self__, "serial", serial)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def item(self) -> 'outputs.GetSwitchPortsItemResult':
        return pulumi.get(self, "item")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetSwitchPortsItemResult']:
        """
        Array of ResponseSwitchGetDeviceSwitchPorts
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="portId")
    def port_id(self) -> Optional[str]:
        """
        portId path parameter. Port ID
        """
        return pulumi.get(self, "port_id")

    @property
    @pulumi.getter
    def serial(self) -> Optional[str]:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")


class AwaitableGetSwitchPortsResult(GetSwitchPortsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSwitchPortsResult(
            id=self.id,
            item=self.item,
            items=self.items,
            port_id=self.port_id,
            serial=self.serial)


def get_switch_ports(port_id: Optional[str] = None,
                     serial: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSwitchPortsResult:
    """
    ## Example Usage


    :param str port_id: portId path parameter. Port ID
    :param str serial: serial path parameter.
    """
    __args__ = dict()
    __args__['portId'] = port_id
    __args__['serial'] = serial
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:devices/getSwitchPorts:getSwitchPorts', __args__, opts=opts, typ=GetSwitchPortsResult).value

    return AwaitableGetSwitchPortsResult(
        id=pulumi.get(__ret__, 'id'),
        item=pulumi.get(__ret__, 'item'),
        items=pulumi.get(__ret__, 'items'),
        port_id=pulumi.get(__ret__, 'port_id'),
        serial=pulumi.get(__ret__, 'serial'))


@_utilities.lift_output_func(get_switch_ports)
def get_switch_ports_output(port_id: Optional[pulumi.Input[Optional[str]]] = None,
                            serial: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSwitchPortsResult]:
    """
    ## Example Usage


    :param str port_id: portId path parameter. Port ID
    :param str serial: serial path parameter.
    """
    ...
