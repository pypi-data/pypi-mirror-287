# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SwitchRoutingMulticastRendezvousPointsArgs', 'SwitchRoutingMulticastRendezvousPoints']

@pulumi.input_type
class SwitchRoutingMulticastRendezvousPointsArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 interface_ip: Optional[pulumi.Input[str]] = None,
                 multicast_group: Optional[pulumi.Input[str]] = None,
                 rendezvous_point_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SwitchRoutingMulticastRendezvousPoints resource.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] interface_ip: The IP address of the interface where the RP needs to be created.
        :param pulumi.Input[str] multicast_group: 'Any', or the IP address of a multicast group
        :param pulumi.Input[str] rendezvous_point_id: rendezvousPointId path parameter. Rendezvous point ID
        """
        pulumi.set(__self__, "network_id", network_id)
        if interface_ip is not None:
            pulumi.set(__self__, "interface_ip", interface_ip)
        if multicast_group is not None:
            pulumi.set(__self__, "multicast_group", multicast_group)
        if rendezvous_point_id is not None:
            pulumi.set(__self__, "rendezvous_point_id", rendezvous_point_id)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="interfaceIp")
    def interface_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the interface where the RP needs to be created.
        """
        return pulumi.get(self, "interface_ip")

    @interface_ip.setter
    def interface_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_ip", value)

    @property
    @pulumi.getter(name="multicastGroup")
    def multicast_group(self) -> Optional[pulumi.Input[str]]:
        """
        'Any', or the IP address of a multicast group
        """
        return pulumi.get(self, "multicast_group")

    @multicast_group.setter
    def multicast_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "multicast_group", value)

    @property
    @pulumi.getter(name="rendezvousPointId")
    def rendezvous_point_id(self) -> Optional[pulumi.Input[str]]:
        """
        rendezvousPointId path parameter. Rendezvous point ID
        """
        return pulumi.get(self, "rendezvous_point_id")

    @rendezvous_point_id.setter
    def rendezvous_point_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rendezvous_point_id", value)


@pulumi.input_type
class _SwitchRoutingMulticastRendezvousPointsState:
    def __init__(__self__, *,
                 interface_ip: Optional[pulumi.Input[str]] = None,
                 interface_name: Optional[pulumi.Input[str]] = None,
                 multicast_group: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 rendezvous_point_id: Optional[pulumi.Input[str]] = None,
                 serial: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SwitchRoutingMulticastRendezvousPoints resources.
        :param pulumi.Input[str] interface_ip: The IP address of the interface where the RP needs to be created.
        :param pulumi.Input[str] multicast_group: 'Any', or the IP address of a multicast group
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] rendezvous_point_id: rendezvousPointId path parameter. Rendezvous point ID
        """
        if interface_ip is not None:
            pulumi.set(__self__, "interface_ip", interface_ip)
        if interface_name is not None:
            pulumi.set(__self__, "interface_name", interface_name)
        if multicast_group is not None:
            pulumi.set(__self__, "multicast_group", multicast_group)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if rendezvous_point_id is not None:
            pulumi.set(__self__, "rendezvous_point_id", rendezvous_point_id)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)

    @property
    @pulumi.getter(name="interfaceIp")
    def interface_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the interface where the RP needs to be created.
        """
        return pulumi.get(self, "interface_ip")

    @interface_ip.setter
    def interface_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_ip", value)

    @property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "interface_name")

    @interface_name.setter
    def interface_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_name", value)

    @property
    @pulumi.getter(name="multicastGroup")
    def multicast_group(self) -> Optional[pulumi.Input[str]]:
        """
        'Any', or the IP address of a multicast group
        """
        return pulumi.get(self, "multicast_group")

    @multicast_group.setter
    def multicast_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "multicast_group", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="rendezvousPointId")
    def rendezvous_point_id(self) -> Optional[pulumi.Input[str]]:
        """
        rendezvousPointId path parameter. Rendezvous point ID
        """
        return pulumi.get(self, "rendezvous_point_id")

    @rendezvous_point_id.setter
    def rendezvous_point_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rendezvous_point_id", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial", value)


class SwitchRoutingMulticastRendezvousPoints(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 interface_ip: Optional[pulumi.Input[str]] = None,
                 multicast_group: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 rendezvous_point_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.networks.SwitchRoutingMulticastRendezvousPoints("example",
            interface_ip="192.168.1.2",
            multicast_group="Any",
            network_id="string")
        pulumi.export("merakiNetworksSwitchRoutingMulticastRendezvousPointsExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchRoutingMulticastRendezvousPoints:SwitchRoutingMulticastRendezvousPoints example "network_id,rendezvous_point_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] interface_ip: The IP address of the interface where the RP needs to be created.
        :param pulumi.Input[str] multicast_group: 'Any', or the IP address of a multicast group
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] rendezvous_point_id: rendezvousPointId path parameter. Rendezvous point ID
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SwitchRoutingMulticastRendezvousPointsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.networks.SwitchRoutingMulticastRendezvousPoints("example",
            interface_ip="192.168.1.2",
            multicast_group="Any",
            network_id="string")
        pulumi.export("merakiNetworksSwitchRoutingMulticastRendezvousPointsExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchRoutingMulticastRendezvousPoints:SwitchRoutingMulticastRendezvousPoints example "network_id,rendezvous_point_id"
        ```

        :param str resource_name: The name of the resource.
        :param SwitchRoutingMulticastRendezvousPointsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SwitchRoutingMulticastRendezvousPointsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 interface_ip: Optional[pulumi.Input[str]] = None,
                 multicast_group: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 rendezvous_point_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SwitchRoutingMulticastRendezvousPointsArgs.__new__(SwitchRoutingMulticastRendezvousPointsArgs)

            __props__.__dict__["interface_ip"] = interface_ip
            __props__.__dict__["multicast_group"] = multicast_group
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["rendezvous_point_id"] = rendezvous_point_id
            __props__.__dict__["interface_name"] = None
            __props__.__dict__["serial"] = None
        super(SwitchRoutingMulticastRendezvousPoints, __self__).__init__(
            'meraki:networks/switchRoutingMulticastRendezvousPoints:SwitchRoutingMulticastRendezvousPoints',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            interface_ip: Optional[pulumi.Input[str]] = None,
            interface_name: Optional[pulumi.Input[str]] = None,
            multicast_group: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            rendezvous_point_id: Optional[pulumi.Input[str]] = None,
            serial: Optional[pulumi.Input[str]] = None) -> 'SwitchRoutingMulticastRendezvousPoints':
        """
        Get an existing SwitchRoutingMulticastRendezvousPoints resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] interface_ip: The IP address of the interface where the RP needs to be created.
        :param pulumi.Input[str] multicast_group: 'Any', or the IP address of a multicast group
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] rendezvous_point_id: rendezvousPointId path parameter. Rendezvous point ID
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SwitchRoutingMulticastRendezvousPointsState.__new__(_SwitchRoutingMulticastRendezvousPointsState)

        __props__.__dict__["interface_ip"] = interface_ip
        __props__.__dict__["interface_name"] = interface_name
        __props__.__dict__["multicast_group"] = multicast_group
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["rendezvous_point_id"] = rendezvous_point_id
        __props__.__dict__["serial"] = serial
        return SwitchRoutingMulticastRendezvousPoints(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="interfaceIp")
    def interface_ip(self) -> pulumi.Output[str]:
        """
        The IP address of the interface where the RP needs to be created.
        """
        return pulumi.get(self, "interface_ip")

    @property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "interface_name")

    @property
    @pulumi.getter(name="multicastGroup")
    def multicast_group(self) -> pulumi.Output[str]:
        """
        'Any', or the IP address of a multicast group
        """
        return pulumi.get(self, "multicast_group")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="rendezvousPointId")
    def rendezvous_point_id(self) -> pulumi.Output[str]:
        """
        rendezvousPointId path parameter. Rendezvous point ID
        """
        return pulumi.get(self, "rendezvous_point_id")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[str]:
        return pulumi.get(self, "serial")

