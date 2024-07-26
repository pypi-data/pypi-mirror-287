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
from ._inputs import *

__all__ = ['BaseArgs', 'Base']

@pulumi.input_type
class BaseArgs:
    def __init__(__self__, *,
                 serial: pulumi.Input[str],
                 address: Optional[pulumi.Input[str]] = None,
                 floor_plan_id: Optional[pulumi.Input[str]] = None,
                 lat: Optional[pulumi.Input[float]] = None,
                 lng: Optional[pulumi.Input[float]] = None,
                 move_map_marker: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 switch_profile_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Base resource.
        :param pulumi.Input[str] serial: Serial number of the device
        :param pulumi.Input[str] address: Physical address of the device
        :param pulumi.Input[str] floor_plan_id: The floor plan to associate to this device. null disassociates the device from the floorplan.
        :param pulumi.Input[float] lat: Latitude of the device
        :param pulumi.Input[float] lng: Longitude of the device
        :param pulumi.Input[bool] move_map_marker: Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
        :param pulumi.Input[str] name: Name of the device
        :param pulumi.Input[str] notes: Notes for the device, limited to 255 characters
        :param pulumi.Input[str] switch_profile_id: The ID of a switch template to bind to the device (for available switch templates, see the 'Switch Templates' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch template, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: List of tags assigned to the device
        """
        pulumi.set(__self__, "serial", serial)
        if address is not None:
            pulumi.set(__self__, "address", address)
        if floor_plan_id is not None:
            pulumi.set(__self__, "floor_plan_id", floor_plan_id)
        if lat is not None:
            pulumi.set(__self__, "lat", lat)
        if lng is not None:
            pulumi.set(__self__, "lng", lng)
        if move_map_marker is not None:
            pulumi.set(__self__, "move_map_marker", move_map_marker)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if switch_profile_id is not None:
            pulumi.set(__self__, "switch_profile_id", switch_profile_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Input[str]:
        """
        Serial number of the device
        """
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: pulumi.Input[str]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        Physical address of the device
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter(name="floorPlanId")
    def floor_plan_id(self) -> Optional[pulumi.Input[str]]:
        """
        The floor plan to associate to this device. null disassociates the device from the floorplan.
        """
        return pulumi.get(self, "floor_plan_id")

    @floor_plan_id.setter
    def floor_plan_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "floor_plan_id", value)

    @property
    @pulumi.getter
    def lat(self) -> Optional[pulumi.Input[float]]:
        """
        Latitude of the device
        """
        return pulumi.get(self, "lat")

    @lat.setter
    def lat(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "lat", value)

    @property
    @pulumi.getter
    def lng(self) -> Optional[pulumi.Input[float]]:
        """
        Longitude of the device
        """
        return pulumi.get(self, "lng")

    @lng.setter
    def lng(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "lng", value)

    @property
    @pulumi.getter(name="moveMapMarker")
    def move_map_marker(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
        """
        return pulumi.get(self, "move_map_marker")

    @move_map_marker.setter
    def move_map_marker(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "move_map_marker", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the device
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        Notes for the device, limited to 255 characters
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="switchProfileId")
    def switch_profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a switch template to bind to the device (for available switch templates, see the 'Switch Templates' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch template, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
        """
        return pulumi.get(self, "switch_profile_id")

    @switch_profile_id.setter
    def switch_profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "switch_profile_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of tags assigned to the device
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _BaseState:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 details: Optional[pulumi.Input[Sequence[pulumi.Input['BaseDetailArgs']]]] = None,
                 firmware: Optional[pulumi.Input[str]] = None,
                 floor_plan_id: Optional[pulumi.Input[str]] = None,
                 imei: Optional[pulumi.Input[str]] = None,
                 lan_ip: Optional[pulumi.Input[str]] = None,
                 lat: Optional[pulumi.Input[float]] = None,
                 lng: Optional[pulumi.Input[float]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 move_map_marker: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 product_type: Optional[pulumi.Input[str]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 switch_profile_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Base resources.
        :param pulumi.Input[str] address: Physical address of the device
        :param pulumi.Input[Sequence[pulumi.Input['BaseDetailArgs']]] details: Additional device information
        :param pulumi.Input[str] firmware: Firmware version of the device
        :param pulumi.Input[str] floor_plan_id: The floor plan to associate to this device. null disassociates the device from the floorplan.
        :param pulumi.Input[str] imei: IMEI of the device, if applicable
        :param pulumi.Input[str] lan_ip: LAN IP address of the device
        :param pulumi.Input[float] lat: Latitude of the device
        :param pulumi.Input[float] lng: Longitude of the device
        :param pulumi.Input[str] mac: MAC address of the device
        :param pulumi.Input[str] model: Model of the device
        :param pulumi.Input[bool] move_map_marker: Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
        :param pulumi.Input[str] name: Name of the device
        :param pulumi.Input[str] network_id: ID of the network the device belongs to
        :param pulumi.Input[str] notes: Notes for the device, limited to 255 characters
        :param pulumi.Input[str] product_type: Product type of the device
        :param pulumi.Input[str] serial: Serial number of the device
        :param pulumi.Input[str] switch_profile_id: The ID of a switch template to bind to the device (for available switch templates, see the 'Switch Templates' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch template, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: List of tags assigned to the device
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if details is not None:
            pulumi.set(__self__, "details", details)
        if firmware is not None:
            pulumi.set(__self__, "firmware", firmware)
        if floor_plan_id is not None:
            pulumi.set(__self__, "floor_plan_id", floor_plan_id)
        if imei is not None:
            pulumi.set(__self__, "imei", imei)
        if lan_ip is not None:
            pulumi.set(__self__, "lan_ip", lan_ip)
        if lat is not None:
            pulumi.set(__self__, "lat", lat)
        if lng is not None:
            pulumi.set(__self__, "lng", lng)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if model is not None:
            pulumi.set(__self__, "model", model)
        if move_map_marker is not None:
            pulumi.set(__self__, "move_map_marker", move_map_marker)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if product_type is not None:
            pulumi.set(__self__, "product_type", product_type)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)
        if switch_profile_id is not None:
            pulumi.set(__self__, "switch_profile_id", switch_profile_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        Physical address of the device
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BaseDetailArgs']]]]:
        """
        Additional device information
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BaseDetailArgs']]]]):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter
    def firmware(self) -> Optional[pulumi.Input[str]]:
        """
        Firmware version of the device
        """
        return pulumi.get(self, "firmware")

    @firmware.setter
    def firmware(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "firmware", value)

    @property
    @pulumi.getter(name="floorPlanId")
    def floor_plan_id(self) -> Optional[pulumi.Input[str]]:
        """
        The floor plan to associate to this device. null disassociates the device from the floorplan.
        """
        return pulumi.get(self, "floor_plan_id")

    @floor_plan_id.setter
    def floor_plan_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "floor_plan_id", value)

    @property
    @pulumi.getter
    def imei(self) -> Optional[pulumi.Input[str]]:
        """
        IMEI of the device, if applicable
        """
        return pulumi.get(self, "imei")

    @imei.setter
    def imei(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "imei", value)

    @property
    @pulumi.getter(name="lanIp")
    def lan_ip(self) -> Optional[pulumi.Input[str]]:
        """
        LAN IP address of the device
        """
        return pulumi.get(self, "lan_ip")

    @lan_ip.setter
    def lan_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lan_ip", value)

    @property
    @pulumi.getter
    def lat(self) -> Optional[pulumi.Input[float]]:
        """
        Latitude of the device
        """
        return pulumi.get(self, "lat")

    @lat.setter
    def lat(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "lat", value)

    @property
    @pulumi.getter
    def lng(self) -> Optional[pulumi.Input[float]]:
        """
        Longitude of the device
        """
        return pulumi.get(self, "lng")

    @lng.setter
    def lng(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "lng", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[str]]:
        """
        MAC address of the device
        """
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[str]]:
        """
        Model of the device
        """
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter(name="moveMapMarker")
    def move_map_marker(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
        """
        return pulumi.get(self, "move_map_marker")

    @move_map_marker.setter
    def move_map_marker(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "move_map_marker", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the device
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the network the device belongs to
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        Notes for the device, limited to 255 characters
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="productType")
    def product_type(self) -> Optional[pulumi.Input[str]]:
        """
        Product type of the device
        """
        return pulumi.get(self, "product_type")

    @product_type.setter
    def product_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_type", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[str]]:
        """
        Serial number of the device
        """
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter(name="switchProfileId")
    def switch_profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a switch template to bind to the device (for available switch templates, see the 'Switch Templates' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch template, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
        """
        return pulumi.get(self, "switch_profile_id")

    @switch_profile_id.setter
    def switch_profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "switch_profile_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of tags assigned to the device
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Base(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 floor_plan_id: Optional[pulumi.Input[str]] = None,
                 lat: Optional[pulumi.Input[float]] = None,
                 lng: Optional[pulumi.Input[float]] = None,
                 move_map_marker: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 switch_profile_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.devices.Base("example",
            lat=37.4180951010362,
            lng=-122.098531723022,
            name="My AP",
            serial="string",
            tags=["recently-added"])
        pulumi.export("merakiDevicesExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:devices/base:base example "organization_id,serial"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: Physical address of the device
        :param pulumi.Input[str] floor_plan_id: The floor plan to associate to this device. null disassociates the device from the floorplan.
        :param pulumi.Input[float] lat: Latitude of the device
        :param pulumi.Input[float] lng: Longitude of the device
        :param pulumi.Input[bool] move_map_marker: Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
        :param pulumi.Input[str] name: Name of the device
        :param pulumi.Input[str] notes: Notes for the device, limited to 255 characters
        :param pulumi.Input[str] serial: Serial number of the device
        :param pulumi.Input[str] switch_profile_id: The ID of a switch template to bind to the device (for available switch templates, see the 'Switch Templates' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch template, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: List of tags assigned to the device
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.devices.Base("example",
            lat=37.4180951010362,
            lng=-122.098531723022,
            name="My AP",
            serial="string",
            tags=["recently-added"])
        pulumi.export("merakiDevicesExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:devices/base:base example "organization_id,serial"
        ```

        :param str resource_name: The name of the resource.
        :param BaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 floor_plan_id: Optional[pulumi.Input[str]] = None,
                 lat: Optional[pulumi.Input[float]] = None,
                 lng: Optional[pulumi.Input[float]] = None,
                 move_map_marker: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 switch_profile_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BaseArgs.__new__(BaseArgs)

            __props__.__dict__["address"] = address
            __props__.__dict__["floor_plan_id"] = floor_plan_id
            __props__.__dict__["lat"] = lat
            __props__.__dict__["lng"] = lng
            __props__.__dict__["move_map_marker"] = move_map_marker
            __props__.__dict__["name"] = name
            __props__.__dict__["notes"] = notes
            if serial is None and not opts.urn:
                raise TypeError("Missing required property 'serial'")
            __props__.__dict__["serial"] = serial
            __props__.__dict__["switch_profile_id"] = switch_profile_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["details"] = None
            __props__.__dict__["firmware"] = None
            __props__.__dict__["imei"] = None
            __props__.__dict__["lan_ip"] = None
            __props__.__dict__["mac"] = None
            __props__.__dict__["model"] = None
            __props__.__dict__["network_id"] = None
            __props__.__dict__["product_type"] = None
        super(Base, __self__).__init__(
            'meraki:devices/base:base',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[str]] = None,
            details: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BaseDetailArgs']]]]] = None,
            firmware: Optional[pulumi.Input[str]] = None,
            floor_plan_id: Optional[pulumi.Input[str]] = None,
            imei: Optional[pulumi.Input[str]] = None,
            lan_ip: Optional[pulumi.Input[str]] = None,
            lat: Optional[pulumi.Input[float]] = None,
            lng: Optional[pulumi.Input[float]] = None,
            mac: Optional[pulumi.Input[str]] = None,
            model: Optional[pulumi.Input[str]] = None,
            move_map_marker: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            notes: Optional[pulumi.Input[str]] = None,
            product_type: Optional[pulumi.Input[str]] = None,
            serial: Optional[pulumi.Input[str]] = None,
            switch_profile_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Base':
        """
        Get an existing Base resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: Physical address of the device
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BaseDetailArgs']]]] details: Additional device information
        :param pulumi.Input[str] firmware: Firmware version of the device
        :param pulumi.Input[str] floor_plan_id: The floor plan to associate to this device. null disassociates the device from the floorplan.
        :param pulumi.Input[str] imei: IMEI of the device, if applicable
        :param pulumi.Input[str] lan_ip: LAN IP address of the device
        :param pulumi.Input[float] lat: Latitude of the device
        :param pulumi.Input[float] lng: Longitude of the device
        :param pulumi.Input[str] mac: MAC address of the device
        :param pulumi.Input[str] model: Model of the device
        :param pulumi.Input[bool] move_map_marker: Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
        :param pulumi.Input[str] name: Name of the device
        :param pulumi.Input[str] network_id: ID of the network the device belongs to
        :param pulumi.Input[str] notes: Notes for the device, limited to 255 characters
        :param pulumi.Input[str] product_type: Product type of the device
        :param pulumi.Input[str] serial: Serial number of the device
        :param pulumi.Input[str] switch_profile_id: The ID of a switch template to bind to the device (for available switch templates, see the 'Switch Templates' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch template, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: List of tags assigned to the device
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BaseState.__new__(_BaseState)

        __props__.__dict__["address"] = address
        __props__.__dict__["details"] = details
        __props__.__dict__["firmware"] = firmware
        __props__.__dict__["floor_plan_id"] = floor_plan_id
        __props__.__dict__["imei"] = imei
        __props__.__dict__["lan_ip"] = lan_ip
        __props__.__dict__["lat"] = lat
        __props__.__dict__["lng"] = lng
        __props__.__dict__["mac"] = mac
        __props__.__dict__["model"] = model
        __props__.__dict__["move_map_marker"] = move_map_marker
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["notes"] = notes
        __props__.__dict__["product_type"] = product_type
        __props__.__dict__["serial"] = serial
        __props__.__dict__["switch_profile_id"] = switch_profile_id
        __props__.__dict__["tags"] = tags
        return Base(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        Physical address of the device
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def details(self) -> pulumi.Output[Sequence['outputs.BaseDetail']]:
        """
        Additional device information
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def firmware(self) -> pulumi.Output[str]:
        """
        Firmware version of the device
        """
        return pulumi.get(self, "firmware")

    @property
    @pulumi.getter(name="floorPlanId")
    def floor_plan_id(self) -> pulumi.Output[str]:
        """
        The floor plan to associate to this device. null disassociates the device from the floorplan.
        """
        return pulumi.get(self, "floor_plan_id")

    @property
    @pulumi.getter
    def imei(self) -> pulumi.Output[str]:
        """
        IMEI of the device, if applicable
        """
        return pulumi.get(self, "imei")

    @property
    @pulumi.getter(name="lanIp")
    def lan_ip(self) -> pulumi.Output[str]:
        """
        LAN IP address of the device
        """
        return pulumi.get(self, "lan_ip")

    @property
    @pulumi.getter
    def lat(self) -> pulumi.Output[float]:
        """
        Latitude of the device
        """
        return pulumi.get(self, "lat")

    @property
    @pulumi.getter
    def lng(self) -> pulumi.Output[float]:
        """
        Longitude of the device
        """
        return pulumi.get(self, "lng")

    @property
    @pulumi.getter
    def mac(self) -> pulumi.Output[str]:
        """
        MAC address of the device
        """
        return pulumi.get(self, "mac")

    @property
    @pulumi.getter
    def model(self) -> pulumi.Output[str]:
        """
        Model of the device
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter(name="moveMapMarker")
    def move_map_marker(self) -> pulumi.Output[bool]:
        """
        Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
        """
        return pulumi.get(self, "move_map_marker")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the device
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        ID of the network the device belongs to
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[str]:
        """
        Notes for the device, limited to 255 characters
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="productType")
    def product_type(self) -> pulumi.Output[str]:
        """
        Product type of the device
        """
        return pulumi.get(self, "product_type")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[str]:
        """
        Serial number of the device
        """
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter(name="switchProfileId")
    def switch_profile_id(self) -> pulumi.Output[str]:
        """
        The ID of a switch template to bind to the device (for available switch templates, see the 'Switch Templates' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch template, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
        """
        return pulumi.get(self, "switch_profile_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[str]]:
        """
        List of tags assigned to the device
        """
        return pulumi.get(self, "tags")

