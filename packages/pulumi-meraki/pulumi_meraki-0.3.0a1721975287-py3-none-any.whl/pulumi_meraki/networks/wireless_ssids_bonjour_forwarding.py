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

__all__ = ['WirelessSsidsBonjourForwardingArgs', 'WirelessSsidsBonjourForwarding']

@pulumi.input_type
class WirelessSsidsBonjourForwardingArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 number: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 exception: Optional[pulumi.Input['WirelessSsidsBonjourForwardingExceptionArgs']] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsBonjourForwardingRuleArgs']]]] = None):
        """
        The set of arguments for constructing a WirelessSsidsBonjourForwarding resource.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] number: number path parameter.
        :param pulumi.Input[bool] enabled: If true, Bonjour forwarding is enabled on the SSID.
        :param pulumi.Input['WirelessSsidsBonjourForwardingExceptionArgs'] exception: Bonjour forwarding exception
        :param pulumi.Input[Sequence[pulumi.Input['WirelessSsidsBonjourForwardingRuleArgs']]] rules: Bonjour forwarding rules
        """
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "number", number)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if exception is not None:
            pulumi.set(__self__, "exception", exception)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

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
    def number(self) -> pulumi.Input[str]:
        """
        number path parameter.
        """
        return pulumi.get(self, "number")

    @number.setter
    def number(self, value: pulumi.Input[str]):
        pulumi.set(self, "number", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, Bonjour forwarding is enabled on the SSID.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def exception(self) -> Optional[pulumi.Input['WirelessSsidsBonjourForwardingExceptionArgs']]:
        """
        Bonjour forwarding exception
        """
        return pulumi.get(self, "exception")

    @exception.setter
    def exception(self, value: Optional[pulumi.Input['WirelessSsidsBonjourForwardingExceptionArgs']]):
        pulumi.set(self, "exception", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsBonjourForwardingRuleArgs']]]]:
        """
        Bonjour forwarding rules
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsBonjourForwardingRuleArgs']]]]):
        pulumi.set(self, "rules", value)


@pulumi.input_type
class _WirelessSsidsBonjourForwardingState:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 exception: Optional[pulumi.Input['WirelessSsidsBonjourForwardingExceptionArgs']] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 number: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsBonjourForwardingRuleArgs']]]] = None):
        """
        Input properties used for looking up and filtering WirelessSsidsBonjourForwarding resources.
        :param pulumi.Input[bool] enabled: If true, Bonjour forwarding is enabled on the SSID.
        :param pulumi.Input['WirelessSsidsBonjourForwardingExceptionArgs'] exception: Bonjour forwarding exception
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] number: number path parameter.
        :param pulumi.Input[Sequence[pulumi.Input['WirelessSsidsBonjourForwardingRuleArgs']]] rules: Bonjour forwarding rules
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if exception is not None:
            pulumi.set(__self__, "exception", exception)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if number is not None:
            pulumi.set(__self__, "number", number)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, Bonjour forwarding is enabled on the SSID.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def exception(self) -> Optional[pulumi.Input['WirelessSsidsBonjourForwardingExceptionArgs']]:
        """
        Bonjour forwarding exception
        """
        return pulumi.get(self, "exception")

    @exception.setter
    def exception(self, value: Optional[pulumi.Input['WirelessSsidsBonjourForwardingExceptionArgs']]):
        pulumi.set(self, "exception", value)

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
    @pulumi.getter
    def number(self) -> Optional[pulumi.Input[str]]:
        """
        number path parameter.
        """
        return pulumi.get(self, "number")

    @number.setter
    def number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "number", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsBonjourForwardingRuleArgs']]]]:
        """
        Bonjour forwarding rules
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsBonjourForwardingRuleArgs']]]]):
        pulumi.set(self, "rules", value)


class WirelessSsidsBonjourForwarding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 exception: Optional[pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingExceptionArgs']]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 number: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingRuleArgs']]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/wirelessSsidsBonjourForwarding:WirelessSsidsBonjourForwarding example "network_id,number"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: If true, Bonjour forwarding is enabled on the SSID.
        :param pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingExceptionArgs']] exception: Bonjour forwarding exception
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] number: number path parameter.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingRuleArgs']]]] rules: Bonjour forwarding rules
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WirelessSsidsBonjourForwardingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/wirelessSsidsBonjourForwarding:WirelessSsidsBonjourForwarding example "network_id,number"
        ```

        :param str resource_name: The name of the resource.
        :param WirelessSsidsBonjourForwardingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WirelessSsidsBonjourForwardingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 exception: Optional[pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingExceptionArgs']]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 number: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingRuleArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WirelessSsidsBonjourForwardingArgs.__new__(WirelessSsidsBonjourForwardingArgs)

            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["exception"] = exception
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            if number is None and not opts.urn:
                raise TypeError("Missing required property 'number'")
            __props__.__dict__["number"] = number
            __props__.__dict__["rules"] = rules
        super(WirelessSsidsBonjourForwarding, __self__).__init__(
            'meraki:networks/wirelessSsidsBonjourForwarding:WirelessSsidsBonjourForwarding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            exception: Optional[pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingExceptionArgs']]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            number: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingRuleArgs']]]]] = None) -> 'WirelessSsidsBonjourForwarding':
        """
        Get an existing WirelessSsidsBonjourForwarding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: If true, Bonjour forwarding is enabled on the SSID.
        :param pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingExceptionArgs']] exception: Bonjour forwarding exception
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] number: number path parameter.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsBonjourForwardingRuleArgs']]]] rules: Bonjour forwarding rules
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WirelessSsidsBonjourForwardingState.__new__(_WirelessSsidsBonjourForwardingState)

        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["exception"] = exception
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["number"] = number
        __props__.__dict__["rules"] = rules
        return WirelessSsidsBonjourForwarding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        If true, Bonjour forwarding is enabled on the SSID.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def exception(self) -> pulumi.Output['outputs.WirelessSsidsBonjourForwardingException']:
        """
        Bonjour forwarding exception
        """
        return pulumi.get(self, "exception")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def number(self) -> pulumi.Output[str]:
        """
        number path parameter.
        """
        return pulumi.get(self, "number")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.WirelessSsidsBonjourForwardingRule']]:
        """
        Bonjour forwarding rules
        """
        return pulumi.get(self, "rules")

