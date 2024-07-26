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
    'GetSamlRolesResult',
    'AwaitableGetSamlRolesResult',
    'get_saml_roles',
    'get_saml_roles_output',
]

@pulumi.output_type
class GetSamlRolesResult:
    """
    A collection of values returned by getSamlRoles.
    """
    def __init__(__self__, id=None, item=None, items=None, organization_id=None, saml_role_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if item and not isinstance(item, dict):
            raise TypeError("Expected argument 'item' to be a dict")
        pulumi.set(__self__, "item", item)
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if saml_role_id and not isinstance(saml_role_id, str):
            raise TypeError("Expected argument 'saml_role_id' to be a str")
        pulumi.set(__self__, "saml_role_id", saml_role_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def item(self) -> 'outputs.GetSamlRolesItemResult':
        return pulumi.get(self, "item")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetSamlRolesItemResult']:
        """
        Array of ResponseOrganizationsGetOrganizationSamlRoles
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[str]:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="samlRoleId")
    def saml_role_id(self) -> Optional[str]:
        """
        samlRoleId path parameter. Saml role ID
        """
        return pulumi.get(self, "saml_role_id")


class AwaitableGetSamlRolesResult(GetSamlRolesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSamlRolesResult(
            id=self.id,
            item=self.item,
            items=self.items,
            organization_id=self.organization_id,
            saml_role_id=self.saml_role_id)


def get_saml_roles(organization_id: Optional[str] = None,
                   saml_role_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSamlRolesResult:
    """
    ## Example Usage


    :param str organization_id: organizationId path parameter. Organization ID
    :param str saml_role_id: samlRoleId path parameter. Saml role ID
    """
    __args__ = dict()
    __args__['organizationId'] = organization_id
    __args__['samlRoleId'] = saml_role_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:organizations/getSamlRoles:getSamlRoles', __args__, opts=opts, typ=GetSamlRolesResult).value

    return AwaitableGetSamlRolesResult(
        id=pulumi.get(__ret__, 'id'),
        item=pulumi.get(__ret__, 'item'),
        items=pulumi.get(__ret__, 'items'),
        organization_id=pulumi.get(__ret__, 'organization_id'),
        saml_role_id=pulumi.get(__ret__, 'saml_role_id'))


@_utilities.lift_output_func(get_saml_roles)
def get_saml_roles_output(organization_id: Optional[pulumi.Input[Optional[str]]] = None,
                          saml_role_id: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSamlRolesResult]:
    """
    ## Example Usage


    :param str organization_id: organizationId path parameter. Organization ID
    :param str saml_role_id: samlRoleId path parameter. Saml role ID
    """
    ...
