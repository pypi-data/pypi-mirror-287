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
    'GetSwitchAccessPoliciesResult',
    'AwaitableGetSwitchAccessPoliciesResult',
    'get_switch_access_policies',
    'get_switch_access_policies_output',
]

@pulumi.output_type
class GetSwitchAccessPoliciesResult:
    """
    A collection of values returned by getSwitchAccessPolicies.
    """
    def __init__(__self__, access_policy_number=None, id=None, item=None, items=None, network_id=None):
        if access_policy_number and not isinstance(access_policy_number, str):
            raise TypeError("Expected argument 'access_policy_number' to be a str")
        pulumi.set(__self__, "access_policy_number", access_policy_number)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if item and not isinstance(item, dict):
            raise TypeError("Expected argument 'item' to be a dict")
        pulumi.set(__self__, "item", item)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)

    @property
    @pulumi.getter(name="accessPolicyNumber")
    def access_policy_number(self) -> Optional[str]:
        """
        accessPolicyNumber path parameter. Access policy number
        """
        return pulumi.get(self, "access_policy_number")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def item(self) -> 'outputs.GetSwitchAccessPoliciesItemResult':
        return pulumi.get(self, "item")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetSwitchAccessPoliciesItemResult']:
        """
        Array of ResponseSwitchGetNetworkSwitchAccessPolicies
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")


class AwaitableGetSwitchAccessPoliciesResult(GetSwitchAccessPoliciesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSwitchAccessPoliciesResult(
            access_policy_number=self.access_policy_number,
            id=self.id,
            item=self.item,
            items=self.items,
            network_id=self.network_id)


def get_switch_access_policies(access_policy_number: Optional[str] = None,
                               network_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSwitchAccessPoliciesResult:
    """
    ## Example Usage


    :param str access_policy_number: accessPolicyNumber path parameter. Access policy number
    :param str network_id: networkId path parameter. Network ID
    """
    __args__ = dict()
    __args__['accessPolicyNumber'] = access_policy_number
    __args__['networkId'] = network_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:networks/getSwitchAccessPolicies:getSwitchAccessPolicies', __args__, opts=opts, typ=GetSwitchAccessPoliciesResult).value

    return AwaitableGetSwitchAccessPoliciesResult(
        access_policy_number=pulumi.get(__ret__, 'access_policy_number'),
        id=pulumi.get(__ret__, 'id'),
        item=pulumi.get(__ret__, 'item'),
        items=pulumi.get(__ret__, 'items'),
        network_id=pulumi.get(__ret__, 'network_id'))


@_utilities.lift_output_func(get_switch_access_policies)
def get_switch_access_policies_output(access_policy_number: Optional[pulumi.Input[Optional[str]]] = None,
                                      network_id: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSwitchAccessPoliciesResult]:
    """
    ## Example Usage


    :param str access_policy_number: accessPolicyNumber path parameter. Access policy number
    :param str network_id: networkId path parameter. Network ID
    """
    ...
