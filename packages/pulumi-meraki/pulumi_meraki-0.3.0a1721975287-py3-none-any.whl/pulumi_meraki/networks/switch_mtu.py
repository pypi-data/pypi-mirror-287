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

__all__ = ['SwitchMtuArgs', 'SwitchMtu']

@pulumi.input_type
class SwitchMtuArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 default_mtu_size: Optional[pulumi.Input[int]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchMtuOverrideArgs']]]] = None):
        """
        The set of arguments for constructing a SwitchMtu resource.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[int] default_mtu_size: MTU size for the entire network. Default value is 9578.
        :param pulumi.Input[Sequence[pulumi.Input['SwitchMtuOverrideArgs']]] overrides: Override MTU size for individual switches or switch templates.
                 An empty array will clear overrides.
        """
        pulumi.set(__self__, "network_id", network_id)
        if default_mtu_size is not None:
            pulumi.set(__self__, "default_mtu_size", default_mtu_size)
        if overrides is not None:
            pulumi.set(__self__, "overrides", overrides)

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
    @pulumi.getter(name="defaultMtuSize")
    def default_mtu_size(self) -> Optional[pulumi.Input[int]]:
        """
        MTU size for the entire network. Default value is 9578.
        """
        return pulumi.get(self, "default_mtu_size")

    @default_mtu_size.setter
    def default_mtu_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_mtu_size", value)

    @property
    @pulumi.getter
    def overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SwitchMtuOverrideArgs']]]]:
        """
        Override MTU size for individual switches or switch templates.
          An empty array will clear overrides.
        """
        return pulumi.get(self, "overrides")

    @overrides.setter
    def overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchMtuOverrideArgs']]]]):
        pulumi.set(self, "overrides", value)


@pulumi.input_type
class _SwitchMtuState:
    def __init__(__self__, *,
                 default_mtu_size: Optional[pulumi.Input[int]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchMtuOverrideArgs']]]] = None):
        """
        Input properties used for looking up and filtering SwitchMtu resources.
        :param pulumi.Input[int] default_mtu_size: MTU size for the entire network. Default value is 9578.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[Sequence[pulumi.Input['SwitchMtuOverrideArgs']]] overrides: Override MTU size for individual switches or switch templates.
                 An empty array will clear overrides.
        """
        if default_mtu_size is not None:
            pulumi.set(__self__, "default_mtu_size", default_mtu_size)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if overrides is not None:
            pulumi.set(__self__, "overrides", overrides)

    @property
    @pulumi.getter(name="defaultMtuSize")
    def default_mtu_size(self) -> Optional[pulumi.Input[int]]:
        """
        MTU size for the entire network. Default value is 9578.
        """
        return pulumi.get(self, "default_mtu_size")

    @default_mtu_size.setter
    def default_mtu_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_mtu_size", value)

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
    def overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SwitchMtuOverrideArgs']]]]:
        """
        Override MTU size for individual switches or switch templates.
          An empty array will clear overrides.
        """
        return pulumi.get(self, "overrides")

    @overrides.setter
    def overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SwitchMtuOverrideArgs']]]]):
        pulumi.set(self, "overrides", value)


class SwitchMtu(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_mtu_size: Optional[pulumi.Input[int]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchMtuOverrideArgs']]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchMtu:SwitchMtu example "network_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] default_mtu_size: MTU size for the entire network. Default value is 9578.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchMtuOverrideArgs']]]] overrides: Override MTU size for individual switches or switch templates.
                 An empty array will clear overrides.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SwitchMtuArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchMtu:SwitchMtu example "network_id"
        ```

        :param str resource_name: The name of the resource.
        :param SwitchMtuArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SwitchMtuArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_mtu_size: Optional[pulumi.Input[int]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchMtuOverrideArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SwitchMtuArgs.__new__(SwitchMtuArgs)

            __props__.__dict__["default_mtu_size"] = default_mtu_size
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["overrides"] = overrides
        super(SwitchMtu, __self__).__init__(
            'meraki:networks/switchMtu:SwitchMtu',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_mtu_size: Optional[pulumi.Input[int]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchMtuOverrideArgs']]]]] = None) -> 'SwitchMtu':
        """
        Get an existing SwitchMtu resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] default_mtu_size: MTU size for the entire network. Default value is 9578.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SwitchMtuOverrideArgs']]]] overrides: Override MTU size for individual switches or switch templates.
                 An empty array will clear overrides.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SwitchMtuState.__new__(_SwitchMtuState)

        __props__.__dict__["default_mtu_size"] = default_mtu_size
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["overrides"] = overrides
        return SwitchMtu(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultMtuSize")
    def default_mtu_size(self) -> pulumi.Output[int]:
        """
        MTU size for the entire network. Default value is 9578.
        """
        return pulumi.get(self, "default_mtu_size")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def overrides(self) -> pulumi.Output[Sequence['outputs.SwitchMtuOverride']]:
        """
        Override MTU size for individual switches or switch templates.
          An empty array will clear overrides.
        """
        return pulumi.get(self, "overrides")

