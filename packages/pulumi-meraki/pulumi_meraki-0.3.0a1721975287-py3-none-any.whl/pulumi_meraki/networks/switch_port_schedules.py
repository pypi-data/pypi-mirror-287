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

__all__ = ['SwitchPortSchedulesArgs', 'SwitchPortSchedules']

@pulumi.input_type
class SwitchPortSchedulesArgs:
    def __init__(__self__, *,
                 network_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 port_schedule: Optional[pulumi.Input['SwitchPortSchedulesPortScheduleArgs']] = None,
                 port_schedule_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SwitchPortSchedules resource.
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[str] name: The name for your port schedule. Required
        :param pulumi.Input['SwitchPortSchedulesPortScheduleArgs'] port_schedule: The schedule for switch port scheduling. Schedules are applied to days of the week.
               When it's empty, default schedule with all days of a week are configured.
               Any unspecified day in the schedule is added as a default schedule configuration of the day.
        :param pulumi.Input[str] port_schedule_id: portScheduleId path parameter. Port schedule ID
        """
        pulumi.set(__self__, "network_id", network_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port_schedule is not None:
            pulumi.set(__self__, "port_schedule", port_schedule)
        if port_schedule_id is not None:
            pulumi.set(__self__, "port_schedule_id", port_schedule_id)

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
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for your port schedule. Required
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="portSchedule")
    def port_schedule(self) -> Optional[pulumi.Input['SwitchPortSchedulesPortScheduleArgs']]:
        """
        The schedule for switch port scheduling. Schedules are applied to days of the week.
        When it's empty, default schedule with all days of a week are configured.
        Any unspecified day in the schedule is added as a default schedule configuration of the day.
        """
        return pulumi.get(self, "port_schedule")

    @port_schedule.setter
    def port_schedule(self, value: Optional[pulumi.Input['SwitchPortSchedulesPortScheduleArgs']]):
        pulumi.set(self, "port_schedule", value)

    @property
    @pulumi.getter(name="portScheduleId")
    def port_schedule_id(self) -> Optional[pulumi.Input[str]]:
        """
        portScheduleId path parameter. Port schedule ID
        """
        return pulumi.get(self, "port_schedule_id")

    @port_schedule_id.setter
    def port_schedule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_schedule_id", value)


@pulumi.input_type
class _SwitchPortSchedulesState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 port_schedule: Optional[pulumi.Input['SwitchPortSchedulesPortScheduleArgs']] = None,
                 port_schedule_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SwitchPortSchedules resources.
        :param pulumi.Input[str] name: The name for your port schedule. Required
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input['SwitchPortSchedulesPortScheduleArgs'] port_schedule: The schedule for switch port scheduling. Schedules are applied to days of the week.
               When it's empty, default schedule with all days of a week are configured.
               Any unspecified day in the schedule is added as a default schedule configuration of the day.
        :param pulumi.Input[str] port_schedule_id: portScheduleId path parameter. Port schedule ID
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if port_schedule is not None:
            pulumi.set(__self__, "port_schedule", port_schedule)
        if port_schedule_id is not None:
            pulumi.set(__self__, "port_schedule_id", port_schedule_id)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for your port schedule. Required
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="portSchedule")
    def port_schedule(self) -> Optional[pulumi.Input['SwitchPortSchedulesPortScheduleArgs']]:
        """
        The schedule for switch port scheduling. Schedules are applied to days of the week.
        When it's empty, default schedule with all days of a week are configured.
        Any unspecified day in the schedule is added as a default schedule configuration of the day.
        """
        return pulumi.get(self, "port_schedule")

    @port_schedule.setter
    def port_schedule(self, value: Optional[pulumi.Input['SwitchPortSchedulesPortScheduleArgs']]):
        pulumi.set(self, "port_schedule", value)

    @property
    @pulumi.getter(name="portScheduleId")
    def port_schedule_id(self) -> Optional[pulumi.Input[str]]:
        """
        portScheduleId path parameter. Port schedule ID
        """
        return pulumi.get(self, "port_schedule_id")

    @port_schedule_id.setter
    def port_schedule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_schedule_id", value)


class SwitchPortSchedules(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 port_schedule: Optional[pulumi.Input[pulumi.InputType['SwitchPortSchedulesPortScheduleArgs']]] = None,
                 port_schedule_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.networks.SwitchPortSchedules("example",
            name="Weekdays schedule",
            network_id="string",
            port_schedule=meraki.networks.SwitchPortSchedulesPortScheduleArgs(
                friday=meraki.networks.SwitchPortSchedulesPortScheduleFridayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
                monday=meraki.networks.SwitchPortSchedulesPortScheduleMondayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
                saturday=meraki.networks.SwitchPortSchedulesPortScheduleSaturdayArgs(
                    active=False,
                    from_="0:00",
                    to="24:00",
                ),
                sunday=meraki.networks.SwitchPortSchedulesPortScheduleSundayArgs(
                    active=False,
                    from_="0:00",
                    to="24:00",
                ),
                thursday=meraki.networks.SwitchPortSchedulesPortScheduleThursdayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
                tuesday=meraki.networks.SwitchPortSchedulesPortScheduleTuesdayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
                wednesday=meraki.networks.SwitchPortSchedulesPortScheduleWednesdayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
            ))
        pulumi.export("merakiNetworksSwitchPortSchedulesExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchPortSchedules:SwitchPortSchedules example "network_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name for your port schedule. Required
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[pulumi.InputType['SwitchPortSchedulesPortScheduleArgs']] port_schedule: The schedule for switch port scheduling. Schedules are applied to days of the week.
               When it's empty, default schedule with all days of a week are configured.
               Any unspecified day in the schedule is added as a default schedule configuration of the day.
        :param pulumi.Input[str] port_schedule_id: portScheduleId path parameter. Port schedule ID
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SwitchPortSchedulesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.networks.SwitchPortSchedules("example",
            name="Weekdays schedule",
            network_id="string",
            port_schedule=meraki.networks.SwitchPortSchedulesPortScheduleArgs(
                friday=meraki.networks.SwitchPortSchedulesPortScheduleFridayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
                monday=meraki.networks.SwitchPortSchedulesPortScheduleMondayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
                saturday=meraki.networks.SwitchPortSchedulesPortScheduleSaturdayArgs(
                    active=False,
                    from_="0:00",
                    to="24:00",
                ),
                sunday=meraki.networks.SwitchPortSchedulesPortScheduleSundayArgs(
                    active=False,
                    from_="0:00",
                    to="24:00",
                ),
                thursday=meraki.networks.SwitchPortSchedulesPortScheduleThursdayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
                tuesday=meraki.networks.SwitchPortSchedulesPortScheduleTuesdayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
                wednesday=meraki.networks.SwitchPortSchedulesPortScheduleWednesdayArgs(
                    active=True,
                    from_="9:00",
                    to="17:00",
                ),
            ))
        pulumi.export("merakiNetworksSwitchPortSchedulesExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:networks/switchPortSchedules:SwitchPortSchedules example "network_id"
        ```

        :param str resource_name: The name of the resource.
        :param SwitchPortSchedulesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SwitchPortSchedulesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 port_schedule: Optional[pulumi.Input[pulumi.InputType['SwitchPortSchedulesPortScheduleArgs']]] = None,
                 port_schedule_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SwitchPortSchedulesArgs.__new__(SwitchPortSchedulesArgs)

            __props__.__dict__["name"] = name
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__.__dict__["network_id"] = network_id
            __props__.__dict__["port_schedule"] = port_schedule
            __props__.__dict__["port_schedule_id"] = port_schedule_id
        super(SwitchPortSchedules, __self__).__init__(
            'meraki:networks/switchPortSchedules:SwitchPortSchedules',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            port_schedule: Optional[pulumi.Input[pulumi.InputType['SwitchPortSchedulesPortScheduleArgs']]] = None,
            port_schedule_id: Optional[pulumi.Input[str]] = None) -> 'SwitchPortSchedules':
        """
        Get an existing SwitchPortSchedules resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name for your port schedule. Required
        :param pulumi.Input[str] network_id: networkId path parameter. Network ID
        :param pulumi.Input[pulumi.InputType['SwitchPortSchedulesPortScheduleArgs']] port_schedule: The schedule for switch port scheduling. Schedules are applied to days of the week.
               When it's empty, default schedule with all days of a week are configured.
               Any unspecified day in the schedule is added as a default schedule configuration of the day.
        :param pulumi.Input[str] port_schedule_id: portScheduleId path parameter. Port schedule ID
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SwitchPortSchedulesState.__new__(_SwitchPortSchedulesState)

        __props__.__dict__["name"] = name
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["port_schedule"] = port_schedule
        __props__.__dict__["port_schedule_id"] = port_schedule_id
        return SwitchPortSchedules(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for your port schedule. Required
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        networkId path parameter. Network ID
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="portSchedule")
    def port_schedule(self) -> pulumi.Output['outputs.SwitchPortSchedulesPortSchedule']:
        """
        The schedule for switch port scheduling. Schedules are applied to days of the week.
        When it's empty, default schedule with all days of a week are configured.
        Any unspecified day in the schedule is added as a default schedule configuration of the day.
        """
        return pulumi.get(self, "port_schedule")

    @property
    @pulumi.getter(name="portScheduleId")
    def port_schedule_id(self) -> pulumi.Output[str]:
        """
        portScheduleId path parameter. Port schedule ID
        """
        return pulumi.get(self, "port_schedule_id")

