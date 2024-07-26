# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SwitchRoutingStaticRoutesArgs', 'SwitchRoutingStaticRoutes']

@pulumi.input_type
class SwitchRoutingStaticRoutesArgs:
    def __init__(__self__, *,
                 serial: pulumi.Input[str],
                 advertise_via_ospf_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 next_hop_ip: Optional[pulumi.Input[str]] = None,
                 prefer_over_ospf_routes_enabled: Optional[pulumi.Input[bool]] = None,
                 static_route_id: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SwitchRoutingStaticRoutes resource.
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input[bool] advertise_via_ospf_enabled: Option to advertise static routes via OSPF
        :param pulumi.Input[str] name: The name or description of the layer 3 static route
        :param pulumi.Input[str] next_hop_ip: The IP address of the router to which traffic for this destination network should be sent
        :param pulumi.Input[bool] prefer_over_ospf_routes_enabled: Option to prefer static routes over OSPF routes
        :param pulumi.Input[str] static_route_id: The identifier of a layer 3 static route
        :param pulumi.Input[str] subnet: The IP address of the subnetwork specified in CIDR notation (ex. 1.2.3.0/24)
        """
        pulumi.set(__self__, "serial", serial)
        if advertise_via_ospf_enabled is not None:
            pulumi.set(__self__, "advertise_via_ospf_enabled", advertise_via_ospf_enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if next_hop_ip is not None:
            pulumi.set(__self__, "next_hop_ip", next_hop_ip)
        if prefer_over_ospf_routes_enabled is not None:
            pulumi.set(__self__, "prefer_over_ospf_routes_enabled", prefer_over_ospf_routes_enabled)
        if static_route_id is not None:
            pulumi.set(__self__, "static_route_id", static_route_id)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Input[str]:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: pulumi.Input[str]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter(name="advertiseViaOspfEnabled")
    def advertise_via_ospf_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to advertise static routes via OSPF
        """
        return pulumi.get(self, "advertise_via_ospf_enabled")

    @advertise_via_ospf_enabled.setter
    def advertise_via_ospf_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "advertise_via_ospf_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name or description of the layer 3 static route
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nextHopIp")
    def next_hop_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the router to which traffic for this destination network should be sent
        """
        return pulumi.get(self, "next_hop_ip")

    @next_hop_ip.setter
    def next_hop_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_hop_ip", value)

    @property
    @pulumi.getter(name="preferOverOspfRoutesEnabled")
    def prefer_over_ospf_routes_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to prefer static routes over OSPF routes
        """
        return pulumi.get(self, "prefer_over_ospf_routes_enabled")

    @prefer_over_ospf_routes_enabled.setter
    def prefer_over_ospf_routes_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "prefer_over_ospf_routes_enabled", value)

    @property
    @pulumi.getter(name="staticRouteId")
    def static_route_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of a layer 3 static route
        """
        return pulumi.get(self, "static_route_id")

    @static_route_id.setter
    def static_route_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "static_route_id", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the subnetwork specified in CIDR notation (ex. 1.2.3.0/24)
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet", value)


@pulumi.input_type
class _SwitchRoutingStaticRoutesState:
    def __init__(__self__, *,
                 advertise_via_ospf_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 next_hop_ip: Optional[pulumi.Input[str]] = None,
                 prefer_over_ospf_routes_enabled: Optional[pulumi.Input[bool]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 static_route_id: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SwitchRoutingStaticRoutes resources.
        :param pulumi.Input[bool] advertise_via_ospf_enabled: Option to advertise static routes via OSPF
        :param pulumi.Input[str] name: The name or description of the layer 3 static route
        :param pulumi.Input[str] next_hop_ip: The IP address of the router to which traffic for this destination network should be sent
        :param pulumi.Input[bool] prefer_over_ospf_routes_enabled: Option to prefer static routes over OSPF routes
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input[str] static_route_id: The identifier of a layer 3 static route
        :param pulumi.Input[str] subnet: The IP address of the subnetwork specified in CIDR notation (ex. 1.2.3.0/24)
        """
        if advertise_via_ospf_enabled is not None:
            pulumi.set(__self__, "advertise_via_ospf_enabled", advertise_via_ospf_enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if next_hop_ip is not None:
            pulumi.set(__self__, "next_hop_ip", next_hop_ip)
        if prefer_over_ospf_routes_enabled is not None:
            pulumi.set(__self__, "prefer_over_ospf_routes_enabled", prefer_over_ospf_routes_enabled)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)
        if static_route_id is not None:
            pulumi.set(__self__, "static_route_id", static_route_id)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)

    @property
    @pulumi.getter(name="advertiseViaOspfEnabled")
    def advertise_via_ospf_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to advertise static routes via OSPF
        """
        return pulumi.get(self, "advertise_via_ospf_enabled")

    @advertise_via_ospf_enabled.setter
    def advertise_via_ospf_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "advertise_via_ospf_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name or description of the layer 3 static route
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nextHopIp")
    def next_hop_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the router to which traffic for this destination network should be sent
        """
        return pulumi.get(self, "next_hop_ip")

    @next_hop_ip.setter
    def next_hop_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_hop_ip", value)

    @property
    @pulumi.getter(name="preferOverOspfRoutesEnabled")
    def prefer_over_ospf_routes_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to prefer static routes over OSPF routes
        """
        return pulumi.get(self, "prefer_over_ospf_routes_enabled")

    @prefer_over_ospf_routes_enabled.setter
    def prefer_over_ospf_routes_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "prefer_over_ospf_routes_enabled", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[str]]:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter(name="staticRouteId")
    def static_route_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of a layer 3 static route
        """
        return pulumi.get(self, "static_route_id")

    @static_route_id.setter
    def static_route_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "static_route_id", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the subnetwork specified in CIDR notation (ex. 1.2.3.0/24)
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet", value)


class SwitchRoutingStaticRoutes(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advertise_via_ospf_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 next_hop_ip: Optional[pulumi.Input[str]] = None,
                 prefer_over_ospf_routes_enabled: Optional[pulumi.Input[bool]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 static_route_id: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.devices.SwitchRoutingStaticRoutes("example",
            advertise_via_ospf_enabled=False,
            name="My route",
            next_hop_ip="1.2.3.4",
            prefer_over_ospf_routes_enabled=False,
            serial="string",
            subnet="192.168.1.0/24")
        pulumi.export("merakiDevicesSwitchRoutingStaticRoutesExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:devices/switchRoutingStaticRoutes:SwitchRoutingStaticRoutes example "serial,static_route_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] advertise_via_ospf_enabled: Option to advertise static routes via OSPF
        :param pulumi.Input[str] name: The name or description of the layer 3 static route
        :param pulumi.Input[str] next_hop_ip: The IP address of the router to which traffic for this destination network should be sent
        :param pulumi.Input[bool] prefer_over_ospf_routes_enabled: Option to prefer static routes over OSPF routes
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input[str] static_route_id: The identifier of a layer 3 static route
        :param pulumi.Input[str] subnet: The IP address of the subnetwork specified in CIDR notation (ex. 1.2.3.0/24)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SwitchRoutingStaticRoutesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.devices.SwitchRoutingStaticRoutes("example",
            advertise_via_ospf_enabled=False,
            name="My route",
            next_hop_ip="1.2.3.4",
            prefer_over_ospf_routes_enabled=False,
            serial="string",
            subnet="192.168.1.0/24")
        pulumi.export("merakiDevicesSwitchRoutingStaticRoutesExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:devices/switchRoutingStaticRoutes:SwitchRoutingStaticRoutes example "serial,static_route_id"
        ```

        :param str resource_name: The name of the resource.
        :param SwitchRoutingStaticRoutesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SwitchRoutingStaticRoutesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advertise_via_ospf_enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 next_hop_ip: Optional[pulumi.Input[str]] = None,
                 prefer_over_ospf_routes_enabled: Optional[pulumi.Input[bool]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 static_route_id: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SwitchRoutingStaticRoutesArgs.__new__(SwitchRoutingStaticRoutesArgs)

            __props__.__dict__["advertise_via_ospf_enabled"] = advertise_via_ospf_enabled
            __props__.__dict__["name"] = name
            __props__.__dict__["next_hop_ip"] = next_hop_ip
            __props__.__dict__["prefer_over_ospf_routes_enabled"] = prefer_over_ospf_routes_enabled
            if serial is None and not opts.urn:
                raise TypeError("Missing required property 'serial'")
            __props__.__dict__["serial"] = serial
            __props__.__dict__["static_route_id"] = static_route_id
            __props__.__dict__["subnet"] = subnet
        super(SwitchRoutingStaticRoutes, __self__).__init__(
            'meraki:devices/switchRoutingStaticRoutes:SwitchRoutingStaticRoutes',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            advertise_via_ospf_enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            next_hop_ip: Optional[pulumi.Input[str]] = None,
            prefer_over_ospf_routes_enabled: Optional[pulumi.Input[bool]] = None,
            serial: Optional[pulumi.Input[str]] = None,
            static_route_id: Optional[pulumi.Input[str]] = None,
            subnet: Optional[pulumi.Input[str]] = None) -> 'SwitchRoutingStaticRoutes':
        """
        Get an existing SwitchRoutingStaticRoutes resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] advertise_via_ospf_enabled: Option to advertise static routes via OSPF
        :param pulumi.Input[str] name: The name or description of the layer 3 static route
        :param pulumi.Input[str] next_hop_ip: The IP address of the router to which traffic for this destination network should be sent
        :param pulumi.Input[bool] prefer_over_ospf_routes_enabled: Option to prefer static routes over OSPF routes
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input[str] static_route_id: The identifier of a layer 3 static route
        :param pulumi.Input[str] subnet: The IP address of the subnetwork specified in CIDR notation (ex. 1.2.3.0/24)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SwitchRoutingStaticRoutesState.__new__(_SwitchRoutingStaticRoutesState)

        __props__.__dict__["advertise_via_ospf_enabled"] = advertise_via_ospf_enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["next_hop_ip"] = next_hop_ip
        __props__.__dict__["prefer_over_ospf_routes_enabled"] = prefer_over_ospf_routes_enabled
        __props__.__dict__["serial"] = serial
        __props__.__dict__["static_route_id"] = static_route_id
        __props__.__dict__["subnet"] = subnet
        return SwitchRoutingStaticRoutes(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="advertiseViaOspfEnabled")
    def advertise_via_ospf_enabled(self) -> pulumi.Output[bool]:
        """
        Option to advertise static routes via OSPF
        """
        return pulumi.get(self, "advertise_via_ospf_enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name or description of the layer 3 static route
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextHopIp")
    def next_hop_ip(self) -> pulumi.Output[str]:
        """
        The IP address of the router to which traffic for this destination network should be sent
        """
        return pulumi.get(self, "next_hop_ip")

    @property
    @pulumi.getter(name="preferOverOspfRoutesEnabled")
    def prefer_over_ospf_routes_enabled(self) -> pulumi.Output[bool]:
        """
        Option to prefer static routes over OSPF routes
        """
        return pulumi.get(self, "prefer_over_ospf_routes_enabled")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[str]:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter(name="staticRouteId")
    def static_route_id(self) -> pulumi.Output[str]:
        """
        The identifier of a layer 3 static route
        """
        return pulumi.get(self, "static_route_id")

    @property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[str]:
        """
        The IP address of the subnetwork specified in CIDR notation (ex. 1.2.3.0/24)
        """
        return pulumi.get(self, "subnet")

