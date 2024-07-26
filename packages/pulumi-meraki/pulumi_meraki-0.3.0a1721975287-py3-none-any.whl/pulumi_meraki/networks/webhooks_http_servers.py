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

__all__ = ['WebhooksHttpServersArgs', 'WebhooksHttpServers']

@pulumi.input_type
class WebhooksHttpServersArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 http_server_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 payload_template: Optional[pulumi.Input['WebhooksHttpServersPayloadTemplateArgs']] = None,
                 shared_secret: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebhooksHttpServers resource.
        :param pulumi.Input[str] network_id: A Meraki network ID.
        :param pulumi.Input[str] http_server_id: httpServerId path parameter. Http server ID
        :param pulumi.Input[str] name: A name for easy reference to the HTTP server
        :param pulumi.Input['WebhooksHttpServersPayloadTemplateArgs'] payload_template: The payload template to use when posting data to the HTTP server.
        :param pulumi.Input[str] shared_secret: A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        :param pulumi.Input[str] url: The URL of the HTTP server.
        """
        pulumi.set(__self__, "network_id", network_id)
        if http_server_id is not None:
            pulumi.set(__self__, "http_server_id", http_server_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if payload_template is not None:
            pulumi.set(__self__, "payload_template", payload_template)
        if shared_secret is not None:
            pulumi.set(__self__, "shared_secret", shared_secret)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Input[str]:
        """
        A Meraki network ID.
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="httpServerId")
    def http_server_id(self) -> Optional[pulumi.Input[str]]:
        """
        httpServerId path parameter. Http server ID
        """
        return pulumi.get(self, "http_server_id")

    @http_server_id.setter
    def http_server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "http_server_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for easy reference to the HTTP server
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="payloadTemplate")
    def payload_template(self) -> Optional[pulumi.Input['WebhooksHttpServersPayloadTemplateArgs']]:
        """
        The payload template to use when posting data to the HTTP server.
        """
        return pulumi.get(self, "payload_template")

    @payload_template.setter
    def payload_template(self, value: Optional[pulumi.Input['WebhooksHttpServersPayloadTemplateArgs']]):
        pulumi.set(self, "payload_template", value)

    @property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> Optional[pulumi.Input[str]]:
        """
        A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        """
        return pulumi.get(self, "shared_secret")

    @shared_secret.setter
    def shared_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_secret", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the HTTP server.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


@pulumi.input_type
class _WebhooksHttpServersState:
    def __init__(__self__, *,
                 http_server_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 payload_template: Optional[pulumi.Input['WebhooksHttpServersPayloadTemplateArgs']] = None,
                 shared_secret: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WebhooksHttpServers resources.
        :param pulumi.Input[str] http_server_id: httpServerId path parameter. Http server ID
        :param pulumi.Input[str] name: A name for easy reference to the HTTP server
        :param pulumi.Input[str] network_id: A Meraki network ID.
        :param pulumi.Input['WebhooksHttpServersPayloadTemplateArgs'] payload_template: The payload template to use when posting data to the HTTP server.
        :param pulumi.Input[str] shared_secret: A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        :param pulumi.Input[str] url: The URL of the HTTP server.
        """
        if http_server_id is not None:
            pulumi.set(__self__, "http_server_id", http_server_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if payload_template is not None:
            pulumi.set(__self__, "payload_template", payload_template)
        if shared_secret is not None:
            pulumi.set(__self__, "shared_secret", shared_secret)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="httpServerId")
    def http_server_id(self) -> Optional[pulumi.Input[str]]:
        """
        httpServerId path parameter. Http server ID
        """
        return pulumi.get(self, "http_server_id")

    @http_server_id.setter
    def http_server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "http_server_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for easy reference to the HTTP server
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        A Meraki network ID.
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="payloadTemplate")
    def payload_template(self) -> Optional[pulumi.Input['WebhooksHttpServersPayloadTemplateArgs']]:
        """
        The payload template to use when posting data to the HTTP server.
        """
        return pulumi.get(self, "payload_template")

    @payload_template.setter
    def payload_template(self, value: Optional[pulumi.Input['WebhooksHttpServersPayloadTemplateArgs']]):
        pulumi.set(self, "payload_template", value)

    @property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> Optional[pulumi.Input[str]]:
        """
        A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        """
        return pulumi.get(self, "shared_secret")

    @shared_secret.setter
    def shared_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_secret", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the HTTP server.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class WebhooksHttpServers(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 http_server_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 payload_template: Optional[pulumi.Input[pulumi.InputType['WebhooksHttpServersPayloadTemplateArgs']]] = None,
                 shared_secret: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/webhooksHttpServers:WebhooksHttpServers example "http_server_id,network_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] http_server_id: httpServerId path parameter. Http server ID
        :param pulumi.Input[str] name: A name for easy reference to the HTTP server
        :param pulumi.Input[str] network_id: A Meraki network ID.
        :param pulumi.Input[pulumi.InputType['WebhooksHttpServersPayloadTemplateArgs']] payload_template: The payload template to use when posting data to the HTTP server.
        :param pulumi.Input[str] shared_secret: A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        :param pulumi.Input[str] url: The URL of the HTTP server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebhooksHttpServersArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:networks/webhooksHttpServers:WebhooksHttpServers example "http_server_id,network_id"
        ```

        :param str resource_name: The name of the resource.
        :param WebhooksHttpServersArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebhooksHttpServersArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 http_server_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 payload_template: Optional[pulumi.Input[pulumi.InputType['WebhooksHttpServersPayloadTemplateArgs']]] = None,
                 shared_secret: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebhooksHttpServersArgs.__new__(WebhooksHttpServersArgs)

            __props__.__dict__["http_server_id"] = http_server_id
            __props__.__dict__["name"] = name
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["payload_template"] = payload_template
            __props__.__dict__["shared_secret"] = shared_secret
            __props__.__dict__["url"] = url
        super(WebhooksHttpServers, __self__).__init__(
            'meraki:networks/webhooksHttpServers:WebhooksHttpServers',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            http_server_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            payload_template: Optional[pulumi.Input[pulumi.InputType['WebhooksHttpServersPayloadTemplateArgs']]] = None,
            shared_secret: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'WebhooksHttpServers':
        """
        Get an existing WebhooksHttpServers resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] http_server_id: httpServerId path parameter. Http server ID
        :param pulumi.Input[str] name: A name for easy reference to the HTTP server
        :param pulumi.Input[str] network_id: A Meraki network ID.
        :param pulumi.Input[pulumi.InputType['WebhooksHttpServersPayloadTemplateArgs']] payload_template: The payload template to use when posting data to the HTTP server.
        :param pulumi.Input[str] shared_secret: A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        :param pulumi.Input[str] url: The URL of the HTTP server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WebhooksHttpServersState.__new__(_WebhooksHttpServersState)

        __props__.__dict__["http_server_id"] = http_server_id
        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["payload_template"] = payload_template
        __props__.__dict__["shared_secret"] = shared_secret
        __props__.__dict__["url"] = url
        return WebhooksHttpServers(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="httpServerId")
    def http_server_id(self) -> pulumi.Output[str]:
        """
        httpServerId path parameter. Http server ID
        """
        return pulumi.get(self, "http_server_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A name for easy reference to the HTTP server
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        A Meraki network ID.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="payloadTemplate")
    def payload_template(self) -> pulumi.Output['outputs.WebhooksHttpServersPayloadTemplate']:
        """
        The payload template to use when posting data to the HTTP server.
        """
        return pulumi.get(self, "payload_template")

    @property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> pulumi.Output[str]:
        """
        A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        """
        return pulumi.get(self, "shared_secret")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL of the HTTP server.
        """
        return pulumi.get(self, "url")

