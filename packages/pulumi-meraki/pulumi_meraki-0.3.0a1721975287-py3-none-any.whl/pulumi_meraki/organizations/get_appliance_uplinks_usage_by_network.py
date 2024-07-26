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
    'GetApplianceUplinksUsageByNetworkResult',
    'AwaitableGetApplianceUplinksUsageByNetworkResult',
    'get_appliance_uplinks_usage_by_network',
    'get_appliance_uplinks_usage_by_network_output',
]

@pulumi.output_type
class GetApplianceUplinksUsageByNetworkResult:
    """
    A collection of values returned by getApplianceUplinksUsageByNetwork.
    """
    def __init__(__self__, id=None, items=None, organization_id=None, t0=None, t1=None, timespan=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if t0 and not isinstance(t0, str):
            raise TypeError("Expected argument 't0' to be a str")
        pulumi.set(__self__, "t0", t0)
        if t1 and not isinstance(t1, str):
            raise TypeError("Expected argument 't1' to be a str")
        pulumi.set(__self__, "t1", t1)
        if timespan and not isinstance(timespan, float):
            raise TypeError("Expected argument 'timespan' to be a float")
        pulumi.set(__self__, "timespan", timespan)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetApplianceUplinksUsageByNetworkItemResult']:
        """
        Array of ResponseApplianceGetOrganizationApplianceUplinksUsageByNetwork
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter
    def t0(self) -> Optional[str]:
        """
        t0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        """
        return pulumi.get(self, "t0")

    @property
    @pulumi.getter
    def t1(self) -> Optional[str]:
        """
        t1 query parameter. The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        """
        return pulumi.get(self, "t1")

    @property
    @pulumi.getter
    def timespan(self) -> Optional[float]:
        """
        timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 1 day.
        """
        return pulumi.get(self, "timespan")


class AwaitableGetApplianceUplinksUsageByNetworkResult(GetApplianceUplinksUsageByNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplianceUplinksUsageByNetworkResult(
            id=self.id,
            items=self.items,
            organization_id=self.organization_id,
            t0=self.t0,
            t1=self.t1,
            timespan=self.timespan)


def get_appliance_uplinks_usage_by_network(organization_id: Optional[str] = None,
                                           t0: Optional[str] = None,
                                           t1: Optional[str] = None,
                                           timespan: Optional[float] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplianceUplinksUsageByNetworkResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.organizations.get_appliance_uplinks_usage_by_network(organization_id="string",
        t0="string",
        t1="string",
        timespan=1)
    pulumi.export("merakiOrganizationsApplianceUplinksUsageByNetworkExample", example.items)
    ```


    :param str organization_id: organizationId path parameter. Organization ID
    :param str t0: t0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :param str t1: t1 query parameter. The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
    :param float timespan: timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 1 day.
    """
    __args__ = dict()
    __args__['organizationId'] = organization_id
    __args__['t0'] = t0
    __args__['t1'] = t1
    __args__['timespan'] = timespan
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:organizations/getApplianceUplinksUsageByNetwork:getApplianceUplinksUsageByNetwork', __args__, opts=opts, typ=GetApplianceUplinksUsageByNetworkResult).value

    return AwaitableGetApplianceUplinksUsageByNetworkResult(
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        organization_id=pulumi.get(__ret__, 'organization_id'),
        t0=pulumi.get(__ret__, 't0'),
        t1=pulumi.get(__ret__, 't1'),
        timespan=pulumi.get(__ret__, 'timespan'))


@_utilities.lift_output_func(get_appliance_uplinks_usage_by_network)
def get_appliance_uplinks_usage_by_network_output(organization_id: Optional[pulumi.Input[str]] = None,
                                                  t0: Optional[pulumi.Input[Optional[str]]] = None,
                                                  t1: Optional[pulumi.Input[Optional[str]]] = None,
                                                  timespan: Optional[pulumi.Input[Optional[float]]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplianceUplinksUsageByNetworkResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.organizations.get_appliance_uplinks_usage_by_network(organization_id="string",
        t0="string",
        t1="string",
        timespan=1)
    pulumi.export("merakiOrganizationsApplianceUplinksUsageByNetworkExample", example.items)
    ```


    :param str organization_id: organizationId path parameter. Organization ID
    :param str t0: t0 query parameter. The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :param str t1: t1 query parameter. The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
    :param float timespan: timespan query parameter. The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 1 day.
    """
    ...
