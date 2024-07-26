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

__all__ = ['SwitchAccessControlListsArgs', 'SwitchAccessControlLists']

@pulumi.input_type
class SwitchAccessControlListsArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRuleArgs']]]] = None,
                 rules_responses: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRulesResponseArgs']]]] = None):
        """
        The set of arguments for constructing a SwitchAccessControlLists resource.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRuleArgs']]] rules: An ordered array of the access control list rules
        :param pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRulesResponseArgs']]] rules_responses: An ordered array of the access control list rules
        """
        pulumi.set(__self__, "network_id", network_id)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if rules_responses is not None:
            pulumi.set(__self__, "rules_responses", rules_responses)

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
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRuleArgs']]]]:
        """
        An ordered array of the access control list rules
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="rulesResponses")
    def rules_responses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRulesResponseArgs']]]]:
        """
        An ordered array of the access control list rules
        """
        return pulumi.get(self, "rules_responses")

    @rules_responses.setter
    def rules_responses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRulesResponseArgs']]]]):
        pulumi.set(self, "rules_responses", value)


@pulumi.input_type
class _SwitchAccessControlListsState:
    def __init__(__self__, *,
                 network_id: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRuleArgs']]]] = None,
                 rules_responses: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRulesResponseArgs']]]] = None):
        """
        Input properties used for looking up and filtering SwitchAccessControlLists resources.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRuleArgs']]] rules: An ordered array of the access control list rules
        :param pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRulesResponseArgs']]] rules_responses: An ordered array of the access control list rules
        """
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if rules_responses is not None:
            pulumi.set(__self__, "rules_responses", rules_responses)

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
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRuleArgs']]]]:
        """
        An ordered array of the access control list rules
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="rulesResponses")
    def rules_responses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRulesResponseArgs']]]]:
        """
        An ordered array of the access control list rules
        """
        return pulumi.get(self, "rules_responses")

    @rules_responses.setter
    def rules_responses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchAccessControlListsRulesResponseArgs']]]]):
        pulumi.set(self, "rules_responses", value)


class SwitchAccessControlLists(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRuleArgs']]]]] = None,
                 rules_responses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRulesResponseArgs']]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchAccessControlLists:SwitchAccessControlLists example "network_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRuleArgs']]]] rules: An ordered array of the access control list rules
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRulesResponseArgs']]]] rules_responses: An ordered array of the access control list rules
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SwitchAccessControlListsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchAccessControlLists:SwitchAccessControlLists example "network_id"
        ```

        :param str resource_name: The name of the resource.
        :param SwitchAccessControlListsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SwitchAccessControlListsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRuleArgs']]]]] = None,
                 rules_responses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRulesResponseArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SwitchAccessControlListsArgs.__new__(SwitchAccessControlListsArgs)

            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["rules"] = rules
            __props__.__dict__["rules_responses"] = rules_responses
        super(SwitchAccessControlLists, __self__).__init__(
            'meraki:networks/switchAccessControlLists:SwitchAccessControlLists',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRuleArgs']]]]] = None,
            rules_responses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRulesResponseArgs']]]]] = None) -> 'SwitchAccessControlLists':
        """
        Get an existing SwitchAccessControlLists resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRuleArgs']]]] rules: An ordered array of the access control list rules
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchAccessControlListsRulesResponseArgs']]]] rules_responses: An ordered array of the access control list rules
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SwitchAccessControlListsState.__new__(_SwitchAccessControlListsState)

        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["rules"] = rules
        __props__.__dict__["rules_responses"] = rules_responses
        return SwitchAccessControlLists(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.SwitchAccessControlListsRule']]:
        """
        An ordered array of the access control list rules
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="rulesResponses")
    def rules_responses(self) -> pulumi.Output[Sequence['outputs.SwitchAccessControlListsRulesResponse']]:
        """
        An ordered array of the access control list rules
        """
        return pulumi.get(self, "rules_responses")

