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
    'GetLicensingCotermLicensesResult',
    'AwaitableGetLicensingCotermLicensesResult',
    'get_licensing_coterm_licenses',
    'get_licensing_coterm_licenses_output',
]

@pulumi.output_type
class GetLicensingCotermLicensesResult:
    """
    A collection of values returned by getLicensingCotermLicenses.
    """
    def __init__(__self__, ending_before=None, expired=None, id=None, invalidated=None, items=None, organization_id=None, per_page=None, starting_after=None):
        if ending_before and not isinstance(ending_before, str):
            raise TypeError("Expected argument 'ending_before' to be a str")
        pulumi.set(__self__, "ending_before", ending_before)
        if expired and not isinstance(expired, bool):
            raise TypeError("Expected argument 'expired' to be a bool")
        pulumi.set(__self__, "expired", expired)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if invalidated and not isinstance(invalidated, bool):
            raise TypeError("Expected argument 'invalidated' to be a bool")
        pulumi.set(__self__, "invalidated", invalidated)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if per_page and not isinstance(per_page, int):
            raise TypeError("Expected argument 'per_page' to be a int")
        pulumi.set(__self__, "per_page", per_page)
        if starting_after and not isinstance(starting_after, str):
            raise TypeError("Expected argument 'starting_after' to be a str")
        pulumi.set(__self__, "starting_after", starting_after)

    @property
    @pulumi.getter(name="endingBefore")
    def ending_before(self) -> Optional[str]:
        """
        endingBefore query parameter. A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """
        return pulumi.get(self, "ending_before")

    @property
    @pulumi.getter
    def expired(self) -> Optional[bool]:
        """
        expired query parameter. Filter for licenses that are expired
        """
        return pulumi.get(self, "expired")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def invalidated(self) -> Optional[bool]:
        """
        invalidated query parameter. Filter for licenses that are invalidated
        """
        return pulumi.get(self, "invalidated")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetLicensingCotermLicensesItemResult']:
        """
        Array of ResponseLicensingGetOrganizationLicensingCotermLicenses
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
    @pulumi.getter(name="perPage")
    def per_page(self) -> Optional[int]:
        """
        perPage query parameter. The number of entries per page returned. Acceptable range is 3 1000. Default is 1000.
        """
        return pulumi.get(self, "per_page")

    @property
    @pulumi.getter(name="startingAfter")
    def starting_after(self) -> Optional[str]:
        """
        startingAfter query parameter. A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """
        return pulumi.get(self, "starting_after")


class AwaitableGetLicensingCotermLicensesResult(GetLicensingCotermLicensesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLicensingCotermLicensesResult(
            ending_before=self.ending_before,
            expired=self.expired,
            id=self.id,
            invalidated=self.invalidated,
            items=self.items,
            organization_id=self.organization_id,
            per_page=self.per_page,
            starting_after=self.starting_after)


def get_licensing_coterm_licenses(ending_before: Optional[str] = None,
                                  expired: Optional[bool] = None,
                                  invalidated: Optional[bool] = None,
                                  organization_id: Optional[str] = None,
                                  per_page: Optional[int] = None,
                                  starting_after: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLicensingCotermLicensesResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.organizations.get_licensing_coterm_licenses(ending_before="string",
        expired=False,
        invalidated=False,
        organization_id="string",
        per_page=1,
        starting_after="string")
    pulumi.export("merakiOrganizationsLicensingCotermLicensesExample", example.items)
    ```


    :param str ending_before: endingBefore query parameter. A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :param bool expired: expired query parameter. Filter for licenses that are expired
    :param bool invalidated: invalidated query parameter. Filter for licenses that are invalidated
    :param str organization_id: organizationId path parameter. Organization ID
    :param int per_page: perPage query parameter. The number of entries per page returned. Acceptable range is 3 1000. Default is 1000.
    :param str starting_after: startingAfter query parameter. A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    """
    __args__ = dict()
    __args__['endingBefore'] = ending_before
    __args__['expired'] = expired
    __args__['invalidated'] = invalidated
    __args__['organizationId'] = organization_id
    __args__['perPage'] = per_page
    __args__['startingAfter'] = starting_after
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:organizations/getLicensingCotermLicenses:getLicensingCotermLicenses', __args__, opts=opts, typ=GetLicensingCotermLicensesResult).value

    return AwaitableGetLicensingCotermLicensesResult(
        ending_before=pulumi.get(__ret__, 'ending_before'),
        expired=pulumi.get(__ret__, 'expired'),
        id=pulumi.get(__ret__, 'id'),
        invalidated=pulumi.get(__ret__, 'invalidated'),
        items=pulumi.get(__ret__, 'items'),
        organization_id=pulumi.get(__ret__, 'organization_id'),
        per_page=pulumi.get(__ret__, 'per_page'),
        starting_after=pulumi.get(__ret__, 'starting_after'))


@_utilities.lift_output_func(get_licensing_coterm_licenses)
def get_licensing_coterm_licenses_output(ending_before: Optional[pulumi.Input[Optional[str]]] = None,
                                         expired: Optional[pulumi.Input[Optional[bool]]] = None,
                                         invalidated: Optional[pulumi.Input[Optional[bool]]] = None,
                                         organization_id: Optional[pulumi.Input[str]] = None,
                                         per_page: Optional[pulumi.Input[Optional[int]]] = None,
                                         starting_after: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLicensingCotermLicensesResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.organizations.get_licensing_coterm_licenses(ending_before="string",
        expired=False,
        invalidated=False,
        organization_id="string",
        per_page=1,
        starting_after="string")
    pulumi.export("merakiOrganizationsLicensingCotermLicensesExample", example.items)
    ```


    :param str ending_before: endingBefore query parameter. A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :param bool expired: expired query parameter. Filter for licenses that are expired
    :param bool invalidated: invalidated query parameter. Filter for licenses that are invalidated
    :param str organization_id: organizationId path parameter. Organization ID
    :param int per_page: perPage query parameter. The number of entries per page returned. Acceptable range is 3 1000. Default is 1000.
    :param str starting_after: startingAfter query parameter. A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    """
    ...
