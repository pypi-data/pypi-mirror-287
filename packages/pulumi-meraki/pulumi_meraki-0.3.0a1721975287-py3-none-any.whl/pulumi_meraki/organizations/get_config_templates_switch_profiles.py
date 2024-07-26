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
    'GetConfigTemplatesSwitchProfilesResult',
    'AwaitableGetConfigTemplatesSwitchProfilesResult',
    'get_config_templates_switch_profiles',
    'get_config_templates_switch_profiles_output',
]

@pulumi.output_type
class GetConfigTemplatesSwitchProfilesResult:
    """
    A collection of values returned by getConfigTemplatesSwitchProfiles.
    """
    def __init__(__self__, config_template_id=None, id=None, items=None, organization_id=None):
        if config_template_id and not isinstance(config_template_id, str):
            raise TypeError("Expected argument 'config_template_id' to be a str")
        pulumi.set(__self__, "config_template_id", config_template_id)
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
    @pulumi.getter(name="configTemplateId")
    def config_template_id(self) -> str:
        """
        configTemplateId path parameter. Config template ID
        """
        return pulumi.get(self, "config_template_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.GetConfigTemplatesSwitchProfilesItemResult']:
        """
        Array of ResponseSwitchGetOrganizationConfigTemplateSwitchProfiles
        """
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")


class AwaitableGetConfigTemplatesSwitchProfilesResult(GetConfigTemplatesSwitchProfilesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigTemplatesSwitchProfilesResult(
            config_template_id=self.config_template_id,
            id=self.id,
            items=self.items,
            organization_id=self.organization_id)


def get_config_templates_switch_profiles(config_template_id: Optional[str] = None,
                                         organization_id: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigTemplatesSwitchProfilesResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.organizations.get_config_templates_switch_profiles(config_template_id="string",
        organization_id="string")
    pulumi.export("merakiOrganizationsConfigTemplatesSwitchProfilesExample", example.items)
    ```


    :param str config_template_id: configTemplateId path parameter. Config template ID
    :param str organization_id: organizationId path parameter. Organization ID
    """
    __args__ = dict()
    __args__['configTemplateId'] = config_template_id
    __args__['organizationId'] = organization_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('meraki:organizations/getConfigTemplatesSwitchProfiles:getConfigTemplatesSwitchProfiles', __args__, opts=opts, typ=GetConfigTemplatesSwitchProfilesResult).value

    return AwaitableGetConfigTemplatesSwitchProfilesResult(
        config_template_id=pulumi.get(__ret__, 'config_template_id'),
        id=pulumi.get(__ret__, 'id'),
        items=pulumi.get(__ret__, 'items'),
        organization_id=pulumi.get(__ret__, 'organization_id'))


@_utilities.lift_output_func(get_config_templates_switch_profiles)
def get_config_templates_switch_profiles_output(config_template_id: Optional[pulumi.Input[str]] = None,
                                                organization_id: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigTemplatesSwitchProfilesResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_meraki as meraki

    example = meraki.organizations.get_config_templates_switch_profiles(config_template_id="string",
        organization_id="string")
    pulumi.export("merakiOrganizationsConfigTemplatesSwitchProfilesExample", example.items)
    ```


    :param str config_template_id: configTemplateId path parameter. Config template ID
    :param str organization_id: organizationId path parameter. Organization ID
    """
    ...
