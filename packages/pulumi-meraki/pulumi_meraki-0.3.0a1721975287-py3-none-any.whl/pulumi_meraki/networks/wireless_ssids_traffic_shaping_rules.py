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

__all__ = ['WirelessSsidsTrafficShapingRulesArgs', 'WirelessSsidsTrafficShapingRules']

@pulumi.input_type
class WirelessSsidsTrafficShapingRulesArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 number: pulumi.Input[str],
                 default_rules_enabled: Optional[pulumi.Input[bool]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsTrafficShapingRulesRuleArgs']]]] = None,
                 traffic_shaping_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a WirelessSsidsTrafficShapingRules resource.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] number: number path parameter.
        :param pulumi.Input[bool] default_rules_enabled: Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        :param pulumi.Input[Sequence[pulumi.Input['WirelessSsidsTrafficShapingRulesRuleArgs']]] rules: An array of traffic shaping rules. Rules are applied in the order that
               they are specified in. An empty list (or null) means no rules. Note that
               you are allowed a maximum of 8 rules.
        :param pulumi.Input[bool] traffic_shaping_enabled: Whether traffic shaping rules are applied to clients on your SSID.
        """
        pulumi.set(__self__, "network_id", network_id)
        pulumi.set(__self__, "number", number)
        if default_rules_enabled is not None:
            pulumi.set(__self__, "default_rules_enabled", default_rules_enabled)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if traffic_shaping_enabled is not None:
            pulumi.set(__self__, "traffic_shaping_enabled", traffic_shaping_enabled)

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
    @pulumi.getter(name="defaultRulesEnabled")
    def default_rules_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        """
        return pulumi.get(self, "default_rules_enabled")

    @default_rules_enabled.setter
    def default_rules_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "default_rules_enabled", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsTrafficShapingRulesRuleArgs']]]]:
        """
        An array of traffic shaping rules. Rules are applied in the order that
        they are specified in. An empty list (or null) means no rules. Note that
        you are allowed a maximum of 8 rules.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsTrafficShapingRulesRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="trafficShapingEnabled")
    def traffic_shaping_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether traffic shaping rules are applied to clients on your SSID.
        """
        return pulumi.get(self, "traffic_shaping_enabled")

    @traffic_shaping_enabled.setter
    def traffic_shaping_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "traffic_shaping_enabled", value)


@pulumi.input_type
class _WirelessSsidsTrafficShapingRulesState:
    def __init__(__self__, *,
                 default_rules_enabled: Optional[pulumi.Input[bool]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 number: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsTrafficShapingRulesRuleArgs']]]] = None,
                 traffic_shaping_enabled: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering WirelessSsidsTrafficShapingRules resources.
        :param pulumi.Input[bool] default_rules_enabled: Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] number: number path parameter.
        :param pulumi.Input[Sequence[pulumi.Input['WirelessSsidsTrafficShapingRulesRuleArgs']]] rules: An array of traffic shaping rules. Rules are applied in the order that
               they are specified in. An empty list (or null) means no rules. Note that
               you are allowed a maximum of 8 rules.
        :param pulumi.Input[bool] traffic_shaping_enabled: Whether traffic shaping rules are applied to clients on your SSID.
        """
        if default_rules_enabled is not None:
            pulumi.set(__self__, "default_rules_enabled", default_rules_enabled)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if number is not None:
            pulumi.set(__self__, "number", number)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if traffic_shaping_enabled is not None:
            pulumi.set(__self__, "traffic_shaping_enabled", traffic_shaping_enabled)

    @property
    @pulumi.getter(name="defaultRulesEnabled")
    def default_rules_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        """
        return pulumi.get(self, "default_rules_enabled")

    @default_rules_enabled.setter
    def default_rules_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "default_rules_enabled", value)

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
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsTrafficShapingRulesRuleArgs']]]]:
        """
        An array of traffic shaping rules. Rules are applied in the order that
        they are specified in. An empty list (or null) means no rules. Note that
        you are allowed a maximum of 8 rules.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WirelessSsidsTrafficShapingRulesRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="trafficShapingEnabled")
    def traffic_shaping_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether traffic shaping rules are applied to clients on your SSID.
        """
        return pulumi.get(self, "traffic_shaping_enabled")

    @traffic_shaping_enabled.setter
    def traffic_shaping_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "traffic_shaping_enabled", value)


class WirelessSsidsTrafficShapingRules(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_rules_enabled: Optional[pulumi.Input[bool]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 number: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsTrafficShapingRulesRuleArgs']]]]] = None,
                 traffic_shaping_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/wirelessSsidsTrafficShapingRules:WirelessSsidsTrafficShapingRules example "network_id,number"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] default_rules_enabled: Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] number: number path parameter.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsTrafficShapingRulesRuleArgs']]]] rules: An array of traffic shaping rules. Rules are applied in the order that
               they are specified in. An empty list (or null) means no rules. Note that
               you are allowed a maximum of 8 rules.
        :param pulumi.Input[bool] traffic_shaping_enabled: Whether traffic shaping rules are applied to clients on your SSID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WirelessSsidsTrafficShapingRulesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/wirelessSsidsTrafficShapingRules:WirelessSsidsTrafficShapingRules example "network_id,number"
        ```

        :param str resource_name: The name of the resource.
        :param WirelessSsidsTrafficShapingRulesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WirelessSsidsTrafficShapingRulesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_rules_enabled: Optional[pulumi.Input[bool]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 number: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsTrafficShapingRulesRuleArgs']]]]] = None,
                 traffic_shaping_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WirelessSsidsTrafficShapingRulesArgs.__new__(WirelessSsidsTrafficShapingRulesArgs)

            __props__.__dict__["default_rules_enabled"] = default_rules_enabled
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            if number is None and not opts.urn:
                raise TypeError("Missing required property 'number'")
            __props__.__dict__["number"] = number
            __props__.__dict__["rules"] = rules
            __props__.__dict__["traffic_shaping_enabled"] = traffic_shaping_enabled
        super(WirelessSsidsTrafficShapingRules, __self__).__init__(
            'meraki:networks/wirelessSsidsTrafficShapingRules:WirelessSsidsTrafficShapingRules',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_rules_enabled: Optional[pulumi.Input[bool]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            number: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsTrafficShapingRulesRuleArgs']]]]] = None,
            traffic_shaping_enabled: Optional[pulumi.Input[bool]] = None) -> 'WirelessSsidsTrafficShapingRules':
        """
        Get an existing WirelessSsidsTrafficShapingRules resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] default_rules_enabled: Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] number: number path parameter.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WirelessSsidsTrafficShapingRulesRuleArgs']]]] rules: An array of traffic shaping rules. Rules are applied in the order that
               they are specified in. An empty list (or null) means no rules. Note that
               you are allowed a maximum of 8 rules.
        :param pulumi.Input[bool] traffic_shaping_enabled: Whether traffic shaping rules are applied to clients on your SSID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WirelessSsidsTrafficShapingRulesState.__new__(_WirelessSsidsTrafficShapingRulesState)

        __props__.__dict__["default_rules_enabled"] = default_rules_enabled
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["number"] = number
        __props__.__dict__["rules"] = rules
        __props__.__dict__["traffic_shaping_enabled"] = traffic_shaping_enabled
        return WirelessSsidsTrafficShapingRules(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultRulesEnabled")
    def default_rules_enabled(self) -> pulumi.Output[bool]:
        """
        Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        """
        return pulumi.get(self, "default_rules_enabled")

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
    def rules(self) -> pulumi.Output[Sequence['outputs.WirelessSsidsTrafficShapingRulesRule']]:
        """
        An array of traffic shaping rules. Rules are applied in the order that
        they are specified in. An empty list (or null) means no rules. Note that
        you are allowed a maximum of 8 rules.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="trafficShapingEnabled")
    def traffic_shaping_enabled(self) -> pulumi.Output[bool]:
        """
        Whether traffic shaping rules are applied to clients on your SSID.
        """
        return pulumi.get(self, "traffic_shaping_enabled")

