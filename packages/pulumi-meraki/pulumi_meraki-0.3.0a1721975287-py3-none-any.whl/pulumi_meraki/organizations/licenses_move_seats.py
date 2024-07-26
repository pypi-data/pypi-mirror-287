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

__all__ = ['LicensesMoveSeatsArgs', 'LicensesMoveSeats']

@pulumi.input_type
class LicensesMoveSeatsArgs:
    def __init__(__self__, *,
                 organization_id: pulumi.Input[str],
                 parameters: pulumi.Input['LicensesMoveSeatsParametersArgs']):
        """
        The set of arguments for constructing a LicensesMoveSeats resource.
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        """
        pulumi.set(__self__, "organization_id", organization_id)
        pulumi.set(__self__, "parameters", parameters)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Input['LicensesMoveSeatsParametersArgs']:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: pulumi.Input['LicensesMoveSeatsParametersArgs']):
        pulumi.set(self, "parameters", value)


@pulumi.input_type
class _LicensesMoveSeatsState:
    def __init__(__self__, *,
                 item: Optional[pulumi.Input['LicensesMoveSeatsItemArgs']] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input['LicensesMoveSeatsParametersArgs']] = None):
        """
        Input properties used for looking up and filtering LicensesMoveSeats resources.
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        """
        if item is not None:
            pulumi.set(__self__, "item", item)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)

    @property
    @pulumi.getter
    def item(self) -> Optional[pulumi.Input['LicensesMoveSeatsItemArgs']]:
        return pulumi.get(self, "item")

    @item.setter
    def item(self, value: Optional[pulumi.Input['LicensesMoveSeatsItemArgs']]):
        pulumi.set(self, "item", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input['LicensesMoveSeatsParametersArgs']]:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input['LicensesMoveSeatsParametersArgs']]):
        pulumi.set(self, "parameters", value)


class LicensesMoveSeats(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['LicensesMoveSeatsParametersArgs']]] = None,
                 __props__=None):
        """
        ~>Warning: This resource does not represent a real-world entity in Meraki Dashboard, therefore changing or deleting this resource on its own has no immediate effect. Instead, it is a task part of a Meraki Dashboard workflow. It is executed in Meraki without any additional verification. It does not check if it was executed before or if a similar configuration or action
        already existed previously.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LicensesMoveSeatsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ~>Warning: This resource does not represent a real-world entity in Meraki Dashboard, therefore changing or deleting this resource on its own has no immediate effect. Instead, it is a task part of a Meraki Dashboard workflow. It is executed in Meraki without any additional verification. It does not check if it was executed before or if a similar configuration or action
        already existed previously.

        :param str resource_name: The name of the resource.
        :param LicensesMoveSeatsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LicensesMoveSeatsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['LicensesMoveSeatsParametersArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LicensesMoveSeatsArgs.__new__(LicensesMoveSeatsArgs)

            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            if parameters is None and not opts.urn:
                raise TypeError("Missing required property 'parameters'")
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["item"] = None
        super(LicensesMoveSeats, __self__).__init__(
            'meraki:organizations/licensesMoveSeats:LicensesMoveSeats',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            item: Optional[pulumi.Input[pulumi.InputType['LicensesMoveSeatsItemArgs']]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[pulumi.InputType['LicensesMoveSeatsParametersArgs']]] = None) -> 'LicensesMoveSeats':
        """
        Get an existing LicensesMoveSeats resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LicensesMoveSeatsState.__new__(_LicensesMoveSeatsState)

        __props__.__dict__["item"] = item
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["parameters"] = parameters
        return LicensesMoveSeats(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def item(self) -> pulumi.Output['outputs.LicensesMoveSeatsItem']:
        return pulumi.get(self, "item")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output['outputs.LicensesMoveSeatsParameters']:
        return pulumi.get(self, "parameters")

