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

__all__ = ['SwitchDhcpServerPolicyArpInspectionTrustedServersArgs', 'SwitchDhcpServerPolicyArpInspectionTrustedServers']

@pulumi.input_type
class SwitchDhcpServerPolicyArpInspectionTrustedServersArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 ipv4: Optional[pulumi.Input['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 trusted_server_id: Optional[pulumi.Input[str]] = None,
                 vlan: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a SwitchDhcpServerPolicyArpInspectionTrustedServers resource.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args'] ipv4: IPv4 attributes of the trusted server.
        :param pulumi.Input[str] mac: Mac address of the trusted server.
        :param pulumi.Input[str] trusted_server_id: ID of the trusted server.
        :param pulumi.Input[int] vlan: Vlan ID of the trusted server.
        """
        pulumi.set(__self__, "network_id", network_id)
        if ipv4 is not None:
            pulumi.set(__self__, "ipv4", ipv4)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if trusted_server_id is not None:
            pulumi.set(__self__, "trusted_server_id", trusted_server_id)
        if vlan is not None:
            pulumi.set(__self__, "vlan", vlan)

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
    @pulumi.getter
    def ipv4(self) -> Optional[pulumi.Input['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']]:
        """
        IPv4 attributes of the trusted server.
        """
        return pulumi.get(self, "ipv4")

    @ipv4.setter
    def ipv4(self, value: Optional[pulumi.Input['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']]):
        pulumi.set(self, "ipv4", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[str]]:
        """
        Mac address of the trusted server.
        """
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter(name="trustedServerId")
    def trusted_server_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the trusted server.
        """
        return pulumi.get(self, "trusted_server_id")

    @trusted_server_id.setter
    def trusted_server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trusted_server_id", value)

    @property
    @pulumi.getter
    def vlan(self) -> Optional[pulumi.Input[int]]:
        """
        Vlan ID of the trusted server.
        """
        return pulumi.get(self, "vlan")

    @vlan.setter
    def vlan(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vlan", value)


@pulumi.input_type
class _SwitchDhcpServerPolicyArpInspectionTrustedServersState:
    def __init__(__self__, *,
                 ipv4: Optional[pulumi.Input['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 trusted_server_id: Optional[pulumi.Input[str]] = None,
                 vlan: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering SwitchDhcpServerPolicyArpInspectionTrustedServers resources.
        :param pulumi.Input['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args'] ipv4: IPv4 attributes of the trusted server.
        :param pulumi.Input[str] mac: Mac address of the trusted server.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] trusted_server_id: ID of the trusted server.
        :param pulumi.Input[int] vlan: Vlan ID of the trusted server.
        """
        if ipv4 is not None:
            pulumi.set(__self__, "ipv4", ipv4)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if trusted_server_id is not None:
            pulumi.set(__self__, "trusted_server_id", trusted_server_id)
        if vlan is not None:
            pulumi.set(__self__, "vlan", vlan)

    @property
    @pulumi.getter
    def ipv4(self) -> Optional[pulumi.Input['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']]:
        """
        IPv4 attributes of the trusted server.
        """
        return pulumi.get(self, "ipv4")

    @ipv4.setter
    def ipv4(self, value: Optional[pulumi.Input['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']]):
        pulumi.set(self, "ipv4", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[str]]:
        """
        Mac address of the trusted server.
        """
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac", value)

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
    @pulumi.getter(name="trustedServerId")
    def trusted_server_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the trusted server.
        """
        return pulumi.get(self, "trusted_server_id")

    @trusted_server_id.setter
    def trusted_server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trusted_server_id", value)

    @property
    @pulumi.getter
    def vlan(self) -> Optional[pulumi.Input[int]]:
        """
        Vlan ID of the trusted server.
        """
        return pulumi.get(self, "vlan")

    @vlan.setter
    def vlan(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vlan", value)


class SwitchDhcpServerPolicyArpInspectionTrustedServers(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ipv4: Optional[pulumi.Input[pulumi.InputType['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 trusted_server_id: Optional[pulumi.Input[str]] = None,
                 vlan: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.networks.SwitchDhcpServerPolicyArpInspectionTrustedServers("example",
            ipv4=meraki.networks.SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args(
                address="1.2.3.4",
            ),
            mac="00:11:22:33:44:55",
            network_id="string",
            vlan=100)
        pulumi.export("merakiNetworksSwitchDhcpServerPolicyArpInspectionTrustedServersExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchDhcpServerPolicyArpInspectionTrustedServers:SwitchDhcpServerPolicyArpInspectionTrustedServers example "network_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']] ipv4: IPv4 attributes of the trusted server.
        :param pulumi.Input[str] mac: Mac address of the trusted server.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] trusted_server_id: ID of the trusted server.
        :param pulumi.Input[int] vlan: Vlan ID of the trusted server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SwitchDhcpServerPolicyArpInspectionTrustedServersArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.networks.SwitchDhcpServerPolicyArpInspectionTrustedServers("example",
            ipv4=meraki.networks.SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args(
                address="1.2.3.4",
            ),
            mac="00:11:22:33:44:55",
            network_id="string",
            vlan=100)
        pulumi.export("merakiNetworksSwitchDhcpServerPolicyArpInspectionTrustedServersExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchDhcpServerPolicyArpInspectionTrustedServers:SwitchDhcpServerPolicyArpInspectionTrustedServers example "network_id"
        ```

        :param str resource_name: The name of the resource.
        :param SwitchDhcpServerPolicyArpInspectionTrustedServersArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SwitchDhcpServerPolicyArpInspectionTrustedServersArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ipv4: Optional[pulumi.Input[pulumi.InputType['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 trusted_server_id: Optional[pulumi.Input[str]] = None,
                 vlan: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SwitchDhcpServerPolicyArpInspectionTrustedServersArgs.__new__(SwitchDhcpServerPolicyArpInspectionTrustedServersArgs)

            __props__.__dict__["ipv4"] = ipv4
            __props__.__dict__["mac"] = mac
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["trusted_server_id"] = trusted_server_id
            __props__.__dict__["vlan"] = vlan
        super(SwitchDhcpServerPolicyArpInspectionTrustedServers, __self__).__init__(
            'meraki:networks/switchDhcpServerPolicyArpInspectionTrustedServers:SwitchDhcpServerPolicyArpInspectionTrustedServers',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ipv4: Optional[pulumi.Input[pulumi.InputType['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']]] = None,
            mac: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            trusted_server_id: Optional[pulumi.Input[str]] = None,
            vlan: Optional[pulumi.Input[int]] = None) -> 'SwitchDhcpServerPolicyArpInspectionTrustedServers':
        """
        Get an existing SwitchDhcpServerPolicyArpInspectionTrustedServers resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4Args']] ipv4: IPv4 attributes of the trusted server.
        :param pulumi.Input[str] mac: Mac address of the trusted server.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] trusted_server_id: ID of the trusted server.
        :param pulumi.Input[int] vlan: Vlan ID of the trusted server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SwitchDhcpServerPolicyArpInspectionTrustedServersState.__new__(_SwitchDhcpServerPolicyArpInspectionTrustedServersState)

        __props__.__dict__["ipv4"] = ipv4
        __props__.__dict__["mac"] = mac
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["trusted_server_id"] = trusted_server_id
        __props__.__dict__["vlan"] = vlan
        return SwitchDhcpServerPolicyArpInspectionTrustedServers(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def ipv4(self) -> pulumi.Output['outputs.SwitchDhcpServerPolicyArpInspectionTrustedServersIpv4']:
        """
        IPv4 attributes of the trusted server.
        """
        return pulumi.get(self, "ipv4")

    @property
    @pulumi.getter
    def mac(self) -> pulumi.Output[str]:
        """
        Mac address of the trusted server.
        """
        return pulumi.get(self, "mac")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="trustedServerId")
    def trusted_server_id(self) -> pulumi.Output[str]:
        """
        ID of the trusted server.
        """
        return pulumi.get(self, "trusted_server_id")

    @property
    @pulumi.getter
    def vlan(self) -> pulumi.Output[int]:
        """
        Vlan ID of the trusted server.
        """
        return pulumi.get(self, "vlan")

