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

__all__ = ['ApplianceUplinksSettingsArgs', 'ApplianceUplinksSettings']

@pulumi.input_type
class ApplianceUplinksSettingsArgs:
    def __init__(__self__, *,
                 serial: pulumi.Input[str],
                 interfaces: Optional[pulumi.Input['ApplianceUplinksSettingsInterfacesArgs']] = None):
        """
        The set of arguments for constructing a ApplianceUplinksSettings resource.
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input['ApplianceUplinksSettingsInterfacesArgs'] interfaces: Interface settings.
        """
        pulumi.set(__self__, "serial", serial)
        if interfaces is not None:
            pulumi.set(__self__, "interfaces", interfaces)

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
    @pulumi.getter
    def interfaces(self) -> Optional[pulumi.Input['ApplianceUplinksSettingsInterfacesArgs']]:
        """
        Interface settings.
        """
        return pulumi.get(self, "interfaces")

    @interfaces.setter
    def interfaces(self, value: Optional[pulumi.Input['ApplianceUplinksSettingsInterfacesArgs']]):
        pulumi.set(self, "interfaces", value)


@pulumi.input_type
class _ApplianceUplinksSettingsState:
    def __init__(__self__, *,
                 interfaces: Optional[pulumi.Input['ApplianceUplinksSettingsInterfacesArgs']] = None,
                 serial: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApplianceUplinksSettings resources.
        :param pulumi.Input['ApplianceUplinksSettingsInterfacesArgs'] interfaces: Interface settings.
        :param pulumi.Input[str] serial: serial path parameter.
        """
        if interfaces is not None:
            pulumi.set(__self__, "interfaces", interfaces)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)

    @property
    @pulumi.getter
    def interfaces(self) -> Optional[pulumi.Input['ApplianceUplinksSettingsInterfacesArgs']]:
        """
        Interface settings.
        """
        return pulumi.get(self, "interfaces")

    @interfaces.setter
    def interfaces(self, value: Optional[pulumi.Input['ApplianceUplinksSettingsInterfacesArgs']]):
        pulumi.set(self, "interfaces", value)

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


class ApplianceUplinksSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 interfaces: Optional[pulumi.Input[pulumi.InputType['ApplianceUplinksSettingsInterfacesArgs']]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.devices.ApplianceUplinksSettings("example",
            interfaces=meraki.devices.ApplianceUplinksSettingsInterfacesArgs(
                wan1=meraki.devices.ApplianceUplinksSettingsInterfacesWan1Args(
                    enabled=True,
                    pppoe=meraki.devices.ApplianceUplinksSettingsInterfacesWan1PppoeArgs(
                        authentication=meraki.devices.ApplianceUplinksSettingsInterfacesWan1PppoeAuthenticationArgs(
                            enabled=True,
                            password="password",
                            username="username",
                        ),
                        enabled=True,
                    ),
                    svis=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisArgs(
                        ipv4=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisIpv4Args(
                            address="9.10.11.10/16",
                            assignment_mode="static",
                            gateway="13.14.15.16",
                            nameservers=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisIpv4NameserversArgs(
                                addresses=["1.2.3.4"],
                            ),
                        ),
                        ipv6=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisIpv6Args(
                            address="1:2:3::4",
                            assignment_mode="static",
                            gateway="1:2:3::5",
                            nameservers=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisIpv6NameserversArgs(
                                addresses=[
                                    "1001:4860:4860::8888",
                                    "1001:4860:4860::8844",
                                ],
                            ),
                        ),
                    ),
                    vlan_tagging=meraki.devices.ApplianceUplinksSettingsInterfacesWan1VlanTaggingArgs(
                        enabled=True,
                        vlan_id=1,
                    ),
                ),
                wan2=meraki.devices.ApplianceUplinksSettingsInterfacesWan2Args(
                    enabled=True,
                    pppoe=meraki.devices.ApplianceUplinksSettingsInterfacesWan2PppoeArgs(
                        authentication=meraki.devices.ApplianceUplinksSettingsInterfacesWan2PppoeAuthenticationArgs(
                            enabled=True,
                            password="password",
                            username="username",
                        ),
                        enabled=True,
                    ),
                    svis=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisArgs(
                        ipv4=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisIpv4Args(
                            address="9.10.11.10/16",
                            assignment_mode="static",
                            gateway="13.14.15.16",
                            nameservers=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisIpv4NameserversArgs(
                                addresses=["1.2.3.4"],
                            ),
                        ),
                        ipv6=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisIpv6Args(
                            address="1:2:3::4",
                            assignment_mode="static",
                            gateway="1:2:3::5",
                            nameservers=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisIpv6NameserversArgs(
                                addresses=[
                                    "1001:4860:4860::8888",
                                    "1001:4860:4860::8844",
                                ],
                            ),
                        ),
                    ),
                    vlan_tagging=meraki.devices.ApplianceUplinksSettingsInterfacesWan2VlanTaggingArgs(
                        enabled=True,
                        vlan_id=1,
                    ),
                ),
            ),
            serial="string")
        pulumi.export("merakiDevicesApplianceUplinksSettingsExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:devices/applianceUplinksSettings:ApplianceUplinksSettings example "serial"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ApplianceUplinksSettingsInterfacesArgs']] interfaces: Interface settings.
        :param pulumi.Input[str] serial: serial path parameter.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplianceUplinksSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.devices.ApplianceUplinksSettings("example",
            interfaces=meraki.devices.ApplianceUplinksSettingsInterfacesArgs(
                wan1=meraki.devices.ApplianceUplinksSettingsInterfacesWan1Args(
                    enabled=True,
                    pppoe=meraki.devices.ApplianceUplinksSettingsInterfacesWan1PppoeArgs(
                        authentication=meraki.devices.ApplianceUplinksSettingsInterfacesWan1PppoeAuthenticationArgs(
                            enabled=True,
                            password="password",
                            username="username",
                        ),
                        enabled=True,
                    ),
                    svis=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisArgs(
                        ipv4=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisIpv4Args(
                            address="9.10.11.10/16",
                            assignment_mode="static",
                            gateway="13.14.15.16",
                            nameservers=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisIpv4NameserversArgs(
                                addresses=["1.2.3.4"],
                            ),
                        ),
                        ipv6=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisIpv6Args(
                            address="1:2:3::4",
                            assignment_mode="static",
                            gateway="1:2:3::5",
                            nameservers=meraki.devices.ApplianceUplinksSettingsInterfacesWan1SvisIpv6NameserversArgs(
                                addresses=[
                                    "1001:4860:4860::8888",
                                    "1001:4860:4860::8844",
                                ],
                            ),
                        ),
                    ),
                    vlan_tagging=meraki.devices.ApplianceUplinksSettingsInterfacesWan1VlanTaggingArgs(
                        enabled=True,
                        vlan_id=1,
                    ),
                ),
                wan2=meraki.devices.ApplianceUplinksSettingsInterfacesWan2Args(
                    enabled=True,
                    pppoe=meraki.devices.ApplianceUplinksSettingsInterfacesWan2PppoeArgs(
                        authentication=meraki.devices.ApplianceUplinksSettingsInterfacesWan2PppoeAuthenticationArgs(
                            enabled=True,
                            password="password",
                            username="username",
                        ),
                        enabled=True,
                    ),
                    svis=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisArgs(
                        ipv4=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisIpv4Args(
                            address="9.10.11.10/16",
                            assignment_mode="static",
                            gateway="13.14.15.16",
                            nameservers=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisIpv4NameserversArgs(
                                addresses=["1.2.3.4"],
                            ),
                        ),
                        ipv6=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisIpv6Args(
                            address="1:2:3::4",
                            assignment_mode="static",
                            gateway="1:2:3::5",
                            nameservers=meraki.devices.ApplianceUplinksSettingsInterfacesWan2SvisIpv6NameserversArgs(
                                addresses=[
                                    "1001:4860:4860::8888",
                                    "1001:4860:4860::8844",
                                ],
                            ),
                        ),
                    ),
                    vlan_tagging=meraki.devices.ApplianceUplinksSettingsInterfacesWan2VlanTaggingArgs(
                        enabled=True,
                        vlan_id=1,
                    ),
                ),
            ),
            serial="string")
        pulumi.export("merakiDevicesApplianceUplinksSettingsExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:devices/applianceUplinksSettings:ApplianceUplinksSettings example "serial"
        ```

        :param str resource_name: The name of the resource.
        :param ApplianceUplinksSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplianceUplinksSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 interfaces: Optional[pulumi.Input[pulumi.InputType['ApplianceUplinksSettingsInterfacesArgs']]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplianceUplinksSettingsArgs.__new__(ApplianceUplinksSettingsArgs)

            __props__.__dict__["interfaces"] = interfaces
            if serial is None and not opts.urn:
                raise TypeError("Missing required property 'serial'")
            __props__.__dict__["serial"] = serial
        super(ApplianceUplinksSettings, __self__).__init__(
            'meraki:devices/applianceUplinksSettings:ApplianceUplinksSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            interfaces: Optional[pulumi.Input[pulumi.InputType['ApplianceUplinksSettingsInterfacesArgs']]] = None,
            serial: Optional[pulumi.Input[str]] = None) -> 'ApplianceUplinksSettings':
        """
        Get an existing ApplianceUplinksSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ApplianceUplinksSettingsInterfacesArgs']] interfaces: Interface settings.
        :param pulumi.Input[str] serial: serial path parameter.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApplianceUplinksSettingsState.__new__(_ApplianceUplinksSettingsState)

        __props__.__dict__["interfaces"] = interfaces
        __props__.__dict__["serial"] = serial
        return ApplianceUplinksSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def interfaces(self) -> pulumi.Output['outputs.ApplianceUplinksSettingsInterfaces']:
        """
        Interface settings.
        """
        return pulumi.get(self, "interfaces")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[str]:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

