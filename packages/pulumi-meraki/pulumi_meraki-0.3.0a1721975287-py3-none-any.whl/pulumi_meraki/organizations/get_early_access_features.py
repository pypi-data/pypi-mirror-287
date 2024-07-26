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
    'GetEarlyAccessFeaturesResult',
    'AwaitableGetEarlyAccessFeaturesResult',
    'get_early_access_features',
    'get_early_access_features_output',
]

@pulumi.output_type
class GetEarlyAccessFeaturesResult:
    """
    A collection of values returned by getEarlyAccessFeatures.
    """
    def __init__(__self__, id=None, items=None, organization_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetEarlyAccessFeaturesItemResult']:
        """
        Array of ResponseOrganizationsGetOrganizationEarlyAccessFeatures
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")


class AwaitableGetEarlyAccessFeaturesResult(GetEarlyAccessFeaturesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEarlyAccessFeaturesResult(
            id=self.id,
            items=self.items,
            organization_id=self.organization_id)


def get_early_access_features(organization_id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEarlyAccessFeaturesResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.organizations.get_early_access_features(organization_id="string")
    pulumi.export("merakiOrganizationsEarlyAccessFeaturesExample", example.items)
    ```


    :param str organization_id: organizationId path parameter. Organization ID
    """
    __args__ = dict()
    __args__['organizationId'] = organization_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:organizations/getEarlyAccessFeatures:getEarlyAccessFeatures', __args__, opts=opts, typ=GetEarlyAccessFeaturesResult).value

    return AwaitableGetEarlyAccessFeaturesResult(
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        organization_id=pulumi.get(__ret__, 'organization_id'))


@_utilities.lift_output_func(get_early_access_features)
def get_early_access_features_output(organization_id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEarlyAccessFeaturesResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.organizations.get_early_access_features(organization_id="string")
    pulumi.export("merakiOrganizationsEarlyAccessFeaturesExample", example.items)
    ```


    :param str organization_id: organizationId path parameter. Organization ID
    """
    ...
