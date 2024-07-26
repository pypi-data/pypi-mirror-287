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

__all__ = ['ClientsSplashAuthorizationStatusArgs', 'ClientsSplashAuthorizationStatus']

@pulumi.input_type
class ClientsSplashAuthorizationStatusArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 network_id: pulumi.Input[str],
                 ssids: Optional[pulumi.Input['ClientsSplashAuthorizationStatusSsidsArgs']] = None):
        """
        The set of arguments for constructing a ClientsSplashAuthorizationStatus resource.
        :param pulumi.Input[str] client_id: clientId path parameter. Client ID
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input['ClientsSplashAuthorizationStatusSsidsArgs'] ssids: The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "network_id", network_id)
        if ssids is not None:
            pulumi.set(__self__, "ssids", ssids)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        """
        clientId path parameter. Client ID
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

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
    def ssids(self) -> Optional[pulumi.Input['ClientsSplashAuthorizationStatusSsidsArgs']]:
        """
        The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs
        """
        return pulumi.get(self, "ssids")

    @ssids.setter
    def ssids(self, value: Optional[pulumi.Input['ClientsSplashAuthorizationStatusSsidsArgs']]):
        pulumi.set(self, "ssids", value)


@pulumi.input_type
class _ClientsSplashAuthorizationStatusState:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 ssids: Optional[pulumi.Input['ClientsSplashAuthorizationStatusSsidsArgs']] = None):
        """
        Input properties used for looking up and filtering ClientsSplashAuthorizationStatus resources.
        :param pulumi.Input[str] client_id: clientId path parameter. Client ID
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input['ClientsSplashAuthorizationStatusSsidsArgs'] ssids: The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if ssids is not None:
            pulumi.set(__self__, "ssids", ssids)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        clientId path parameter. Client ID
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

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
    def ssids(self) -> Optional[pulumi.Input['ClientsSplashAuthorizationStatusSsidsArgs']]:
        """
        The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs
        """
        return pulumi.get(self, "ssids")

    @ssids.setter
    def ssids(self, value: Optional[pulumi.Input['ClientsSplashAuthorizationStatusSsidsArgs']]):
        pulumi.set(self, "ssids", value)


class ClientsSplashAuthorizationStatus(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 ssids: Optional[pulumi.Input[pulumi.InputType['ClientsSplashAuthorizationStatusSsidsArgs']]] = None,
                 __props__=None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/clientsSplashAuthorizationStatus:ClientsSplashAuthorizationStatus example "client_id,network_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: clientId path parameter. Client ID
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[pulumi.InputType['ClientsSplashAuthorizationStatusSsidsArgs']] ssids: The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClientsSplashAuthorizationStatusArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/clientsSplashAuthorizationStatus:ClientsSplashAuthorizationStatus example "client_id,network_id"
        ```

        :param str resource_name: The name of the resource.
        :param ClientsSplashAuthorizationStatusArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClientsSplashAuthorizationStatusArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 ssids: Optional[pulumi.Input[pulumi.InputType['ClientsSplashAuthorizationStatusSsidsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClientsSplashAuthorizationStatusArgs.__new__(ClientsSplashAuthorizationStatusArgs)

            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = client_id
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["ssids"] = ssids
        super(ClientsSplashAuthorizationStatus, __self__).__init__(
            'meraki:networks/clientsSplashAuthorizationStatus:ClientsSplashAuthorizationStatus',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            ssids: Optional[pulumi.Input[pulumi.InputType['ClientsSplashAuthorizationStatusSsidsArgs']]] = None) -> 'ClientsSplashAuthorizationStatus':
        """
        Get an existing ClientsSplashAuthorizationStatus resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: clientId path parameter. Client ID
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[pulumi.InputType['ClientsSplashAuthorizationStatusSsidsArgs']] ssids: The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClientsSplashAuthorizationStatusState.__new__(_ClientsSplashAuthorizationStatusState)

        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["ssids"] = ssids
        return ClientsSplashAuthorizationStatus(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        clientId path parameter. Client ID
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter
    def ssids(self) -> pulumi.Output['outputs.ClientsSplashAuthorizationStatusSsids']:
        """
        The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs
        """
        return pulumi.get(self, "ssids")

