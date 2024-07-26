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

__all__ = ['LiveToolsThroughputTestArgs', 'LiveToolsThroughputTest']

@pulumi.input_type
class LiveToolsThroughputTestArgs:
    def __init__(__self__, *,
                 serial: pulumi.Input[str],
                 callback: Optional[pulumi.Input['LiveToolsThroughputTestCallbackArgs']] = None,
                 throughput_test_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LiveToolsThroughputTest resource.
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input['LiveToolsThroughputTestCallbackArgs'] callback: Details for the callback. Please include either an httpServerId OR url and sharedSecret
        :param pulumi.Input[str] throughput_test_id: ID of throughput test job
        """
        pulumi.set(__self__, "serial", serial)
        if callback is not None:
            pulumi.set(__self__, "callback", callback)
        if throughput_test_id is not None:
            pulumi.set(__self__, "throughput_test_id", throughput_test_id)

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Input[str]:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: pulumi.Input[str]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter
    def callback(self) -> Optional[pulumi.Input['LiveToolsThroughputTestCallbackArgs']]:
        """
        Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """
        return pulumi.get(self, "callback")

    @callback.setter
    def callback(self, value: Optional[pulumi.Input['LiveToolsThroughputTestCallbackArgs']]):
        pulumi.set(self, "callback", value)

    @property
    @pulumi.getter(name="throughputTestId")
    def throughput_test_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of throughput test job
        """
        return pulumi.get(self, "throughput_test_id")

    @throughput_test_id.setter
    def throughput_test_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "throughput_test_id", value)


@pulumi.input_type
class _LiveToolsThroughputTestState:
    def __init__(__self__, *,
                 callback: Optional[pulumi.Input['LiveToolsThroughputTestCallbackArgs']] = None,
                 error: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input['LiveToolsThroughputTestRequestArgs']] = None,
                 result: Optional[pulumi.Input['LiveToolsThroughputTestResultArgs']] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 throughput_test_id: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LiveToolsThroughputTest resources.
        :param pulumi.Input['LiveToolsThroughputTestCallbackArgs'] callback: Details for the callback. Please include either an httpServerId OR url and sharedSecret
        :param pulumi.Input[str] error: Description of the error.
        :param pulumi.Input['LiveToolsThroughputTestRequestArgs'] request: The parameters of the throughput test request
        :param pulumi.Input['LiveToolsThroughputTestResultArgs'] result: Result of the throughput test request
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input[str] status: Status of the throughput test request
        :param pulumi.Input[str] throughput_test_id: ID of throughput test job
        :param pulumi.Input[str] url: GET this url to check the status of your throughput test request
        """
        if callback is not None:
            pulumi.set(__self__, "callback", callback)
        if error is not None:
            pulumi.set(__self__, "error", error)
        if request is not None:
            pulumi.set(__self__, "request", request)
        if result is not None:
            pulumi.set(__self__, "result", result)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if throughput_test_id is not None:
            pulumi.set(__self__, "throughput_test_id", throughput_test_id)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def callback(self) -> Optional[pulumi.Input['LiveToolsThroughputTestCallbackArgs']]:
        """
        Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """
        return pulumi.get(self, "callback")

    @callback.setter
    def callback(self, value: Optional[pulumi.Input['LiveToolsThroughputTestCallbackArgs']]):
        pulumi.set(self, "callback", value)

    @property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the error.
        """
        return pulumi.get(self, "error")

    @error.setter
    def error(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "error", value)

    @property
    @pulumi.getter
    def request(self) -> Optional[pulumi.Input['LiveToolsThroughputTestRequestArgs']]:
        """
        The parameters of the throughput test request
        """
        return pulumi.get(self, "request")

    @request.setter
    def request(self, value: Optional[pulumi.Input['LiveToolsThroughputTestRequestArgs']]):
        pulumi.set(self, "request", value)

    @property
    @pulumi.getter
    def result(self) -> Optional[pulumi.Input['LiveToolsThroughputTestResultArgs']]:
        """
        Result of the throughput test request
        """
        return pulumi.get(self, "result")

    @result.setter
    def result(self, value: Optional[pulumi.Input['LiveToolsThroughputTestResultArgs']]):
        pulumi.set(self, "result", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[pulumi.Input[str]]:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the throughput test request
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="throughputTestId")
    def throughput_test_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of throughput test job
        """
        return pulumi.get(self, "throughput_test_id")

    @throughput_test_id.setter
    def throughput_test_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "throughput_test_id", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        GET this url to check the status of your throughput test request
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class LiveToolsThroughputTest(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 callback: Optional[pulumi.Input[pulumi.InputType['LiveToolsThroughputTestCallbackArgs']]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 throughput_test_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:devices/liveToolsThroughputTest:LiveToolsThroughputTest example "serial,throughput_test_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['LiveToolsThroughputTestCallbackArgs']] callback: Details for the callback. Please include either an httpServerId OR url and sharedSecret
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input[str] throughput_test_id: ID of throughput test job
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LiveToolsThroughputTestArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:devices/liveToolsThroughputTest:LiveToolsThroughputTest example "serial,throughput_test_id"
        ```

        :param str resource_name: The name of the resource.
        :param LiveToolsThroughputTestArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LiveToolsThroughputTestArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 callback: Optional[pulumi.Input[pulumi.InputType['LiveToolsThroughputTestCallbackArgs']]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 throughput_test_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LiveToolsThroughputTestArgs.__new__(LiveToolsThroughputTestArgs)

            __props__.__dict__["callback"] = callback
            if serial is None and not opts.urn:
                raise TypeError("Missing required property 'serial'")
            __props__.__dict__["serial"] = serial
            __props__.__dict__["throughput_test_id"] = throughput_test_id
            __props__.__dict__["error"] = None
            __props__.__dict__["request"] = None
            __props__.__dict__["result"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["url"] = None
        super(LiveToolsThroughputTest, __self__).__init__(
            'meraki:devices/liveToolsThroughputTest:LiveToolsThroughputTest',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            callback: Optional[pulumi.Input[pulumi.InputType['LiveToolsThroughputTestCallbackArgs']]] = None,
            error: Optional[pulumi.Input[str]] = None,
            request: Optional[pulumi.Input[pulumi.InputType['LiveToolsThroughputTestRequestArgs']]] = None,
            result: Optional[pulumi.Input[pulumi.InputType['LiveToolsThroughputTestResultArgs']]] = None,
            serial: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            throughput_test_id: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'LiveToolsThroughputTest':
        """
        Get an existing LiveToolsThroughputTest resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['LiveToolsThroughputTestCallbackArgs']] callback: Details for the callback. Please include either an httpServerId OR url and sharedSecret
        :param pulumi.Input[str] error: Description of the error.
        :param pulumi.Input[pulumi.InputType['LiveToolsThroughputTestRequestArgs']] request: The parameters of the throughput test request
        :param pulumi.Input[pulumi.InputType['LiveToolsThroughputTestResultArgs']] result: Result of the throughput test request
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input[str] status: Status of the throughput test request
        :param pulumi.Input[str] throughput_test_id: ID of throughput test job
        :param pulumi.Input[str] url: GET this url to check the status of your throughput test request
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LiveToolsThroughputTestState.__new__(_LiveToolsThroughputTestState)

        __props__.__dict__["callback"] = callback
        __props__.__dict__["error"] = error
        __props__.__dict__["request"] = request
        __props__.__dict__["result"] = result
        __props__.__dict__["serial"] = serial
        __props__.__dict__["status"] = status
        __props__.__dict__["throughput_test_id"] = throughput_test_id
        __props__.__dict__["url"] = url
        return LiveToolsThroughputTest(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def callback(self) -> pulumi.Output['outputs.LiveToolsThroughputTestCallback']:
        """
        Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """
        return pulumi.get(self, "callback")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output[str]:
        """
        Description of the error.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def request(self) -> pulumi.Output['outputs.LiveToolsThroughputTestRequest']:
        """
        The parameters of the throughput test request
        """
        return pulumi.get(self, "request")

    @property
    @pulumi.getter
    def result(self) -> pulumi.Output['outputs.LiveToolsThroughputTestResult']:
        """
        Result of the throughput test request
        """
        return pulumi.get(self, "result")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[str]:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the throughput test request
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="throughputTestId")
    def throughput_test_id(self) -> pulumi.Output[str]:
        """
        ID of throughput test job
        """
        return pulumi.get(self, "throughput_test_id")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        GET this url to check the status of your throughput test request
        """
        return pulumi.get(self, "url")

