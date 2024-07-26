# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CameraQualityAndRetentionArgs', 'CameraQualityAndRetention']

@pulumi.input_type
class CameraQualityAndRetentionArgs:
    def __init__(__self__, *,
                 serial: pulumi.Input[str],
                 audio_recording_enabled: Optional[pulumi.Input[bool]] = None,
                 motion_based_retention_enabled: Optional[pulumi.Input[bool]] = None,
                 motion_detector_version: Optional[pulumi.Input[int]] = None,
                 profile_id: Optional[pulumi.Input[str]] = None,
                 quality: Optional[pulumi.Input[str]] = None,
                 resolution: Optional[pulumi.Input[str]] = None,
                 restricted_bandwidth_mode_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a CameraQualityAndRetention resource.
        :param pulumi.Input[str] serial: serial path parameter.
        :param pulumi.Input[bool] audio_recording_enabled: Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
        :param pulumi.Input[bool] motion_based_retention_enabled: Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
        :param pulumi.Input[int] motion_detector_version: The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        :param pulumi.Input[str] profile_id: The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        :param pulumi.Input[str] quality: Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
        :param pulumi.Input[str] resolution: Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
        :param pulumi.Input[bool] restricted_bandwidth_mode_enabled: Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
        """
        pulumi.set(__self__, "serial", serial)
        if audio_recording_enabled is not None:
            pulumi.set(__self__, "audio_recording_enabled", audio_recording_enabled)
        if motion_based_retention_enabled is not None:
            pulumi.set(__self__, "motion_based_retention_enabled", motion_based_retention_enabled)
        if motion_detector_version is not None:
            pulumi.set(__self__, "motion_detector_version", motion_detector_version)
        if profile_id is not None:
            pulumi.set(__self__, "profile_id", profile_id)
        if quality is not None:
            pulumi.set(__self__, "quality", quality)
        if resolution is not None:
            pulumi.set(__self__, "resolution", resolution)
        if restricted_bandwidth_mode_enabled is not None:
            pulumi.set(__self__, "restricted_bandwidth_mode_enabled", restricted_bandwidth_mode_enabled)

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
    @pulumi.getter(name="audioRecordingEnabled")
    def audio_recording_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
        """
        return pulumi.get(self, "audio_recording_enabled")

    @audio_recording_enabled.setter
    def audio_recording_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "audio_recording_enabled", value)

    @property
    @pulumi.getter(name="motionBasedRetentionEnabled")
    def motion_based_retention_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
        """
        return pulumi.get(self, "motion_based_retention_enabled")

    @motion_based_retention_enabled.setter
    def motion_based_retention_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "motion_based_retention_enabled", value)

    @property
    @pulumi.getter(name="motionDetectorVersion")
    def motion_detector_version(self) -> Optional[pulumi.Input[int]]:
        """
        The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        """
        return pulumi.get(self, "motion_detector_version")

    @motion_detector_version.setter
    def motion_detector_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "motion_detector_version", value)

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        """
        return pulumi.get(self, "profile_id")

    @profile_id.setter
    def profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_id", value)

    @property
    @pulumi.getter
    def quality(self) -> Optional[pulumi.Input[str]]:
        """
        Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
        """
        return pulumi.get(self, "quality")

    @quality.setter
    def quality(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "quality", value)

    @property
    @pulumi.getter
    def resolution(self) -> Optional[pulumi.Input[str]]:
        """
        Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
        """
        return pulumi.get(self, "resolution")

    @resolution.setter
    def resolution(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resolution", value)

    @property
    @pulumi.getter(name="restrictedBandwidthModeEnabled")
    def restricted_bandwidth_mode_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
        """
        return pulumi.get(self, "restricted_bandwidth_mode_enabled")

    @restricted_bandwidth_mode_enabled.setter
    def restricted_bandwidth_mode_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "restricted_bandwidth_mode_enabled", value)


@pulumi.input_type
class _CameraQualityAndRetentionState:
    def __init__(__self__, *,
                 audio_recording_enabled: Optional[pulumi.Input[bool]] = None,
                 motion_based_retention_enabled: Optional[pulumi.Input[bool]] = None,
                 motion_detector_version: Optional[pulumi.Input[int]] = None,
                 profile_id: Optional[pulumi.Input[str]] = None,
                 quality: Optional[pulumi.Input[str]] = None,
                 resolution: Optional[pulumi.Input[str]] = None,
                 restricted_bandwidth_mode_enabled: Optional[pulumi.Input[bool]] = None,
                 serial: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CameraQualityAndRetention resources.
        :param pulumi.Input[bool] audio_recording_enabled: Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
        :param pulumi.Input[bool] motion_based_retention_enabled: Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
        :param pulumi.Input[int] motion_detector_version: The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        :param pulumi.Input[str] profile_id: The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        :param pulumi.Input[str] quality: Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
        :param pulumi.Input[str] resolution: Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
        :param pulumi.Input[bool] restricted_bandwidth_mode_enabled: Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
        :param pulumi.Input[str] serial: serial path parameter.
        """
        if audio_recording_enabled is not None:
            pulumi.set(__self__, "audio_recording_enabled", audio_recording_enabled)
        if motion_based_retention_enabled is not None:
            pulumi.set(__self__, "motion_based_retention_enabled", motion_based_retention_enabled)
        if motion_detector_version is not None:
            pulumi.set(__self__, "motion_detector_version", motion_detector_version)
        if profile_id is not None:
            pulumi.set(__self__, "profile_id", profile_id)
        if quality is not None:
            pulumi.set(__self__, "quality", quality)
        if resolution is not None:
            pulumi.set(__self__, "resolution", resolution)
        if restricted_bandwidth_mode_enabled is not None:
            pulumi.set(__self__, "restricted_bandwidth_mode_enabled", restricted_bandwidth_mode_enabled)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)

    @property
    @pulumi.getter(name="audioRecordingEnabled")
    def audio_recording_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
        """
        return pulumi.get(self, "audio_recording_enabled")

    @audio_recording_enabled.setter
    def audio_recording_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "audio_recording_enabled", value)

    @property
    @pulumi.getter(name="motionBasedRetentionEnabled")
    def motion_based_retention_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
        """
        return pulumi.get(self, "motion_based_retention_enabled")

    @motion_based_retention_enabled.setter
    def motion_based_retention_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "motion_based_retention_enabled", value)

    @property
    @pulumi.getter(name="motionDetectorVersion")
    def motion_detector_version(self) -> Optional[pulumi.Input[int]]:
        """
        The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        """
        return pulumi.get(self, "motion_detector_version")

    @motion_detector_version.setter
    def motion_detector_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "motion_detector_version", value)

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        """
        return pulumi.get(self, "profile_id")

    @profile_id.setter
    def profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_id", value)

    @property
    @pulumi.getter
    def quality(self) -> Optional[pulumi.Input[str]]:
        """
        Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
        """
        return pulumi.get(self, "quality")

    @quality.setter
    def quality(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "quality", value)

    @property
    @pulumi.getter
    def resolution(self) -> Optional[pulumi.Input[str]]:
        """
        Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
        """
        return pulumi.get(self, "resolution")

    @resolution.setter
    def resolution(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resolution", value)

    @property
    @pulumi.getter(name="restrictedBandwidthModeEnabled")
    def restricted_bandwidth_mode_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
        """
        return pulumi.get(self, "restricted_bandwidth_mode_enabled")

    @restricted_bandwidth_mode_enabled.setter
    def restricted_bandwidth_mode_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "restricted_bandwidth_mode_enabled", value)

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


class CameraQualityAndRetention(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audio_recording_enabled: Optional[pulumi.Input[bool]] = None,
                 motion_based_retention_enabled: Optional[pulumi.Input[bool]] = None,
                 motion_detector_version: Optional[pulumi.Input[int]] = None,
                 profile_id: Optional[pulumi.Input[str]] = None,
                 quality: Optional[pulumi.Input[str]] = None,
                 resolution: Optional[pulumi.Input[str]] = None,
                 restricted_bandwidth_mode_enabled: Optional[pulumi.Input[bool]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.devices.CameraQualityAndRetention("example",
            audio_recording_enabled=False,
            motion_based_retention_enabled=False,
            motion_detector_version=2,
            profile_id="1234",
            quality="Standard",
            resolution="1280x720",
            restricted_bandwidth_mode_enabled=False,
            serial="string")
        pulumi.export("merakiDevicesCameraQualityAndRetentionExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:devices/cameraQualityAndRetention:CameraQualityAndRetention example "serial"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] audio_recording_enabled: Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
        :param pulumi.Input[bool] motion_based_retention_enabled: Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
        :param pulumi.Input[int] motion_detector_version: The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        :param pulumi.Input[str] profile_id: The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        :param pulumi.Input[str] quality: Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
        :param pulumi.Input[str] resolution: Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
        :param pulumi.Input[bool] restricted_bandwidth_mode_enabled: Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
        :param pulumi.Input[str] serial: serial path parameter.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CameraQualityAndRetentionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.devices.CameraQualityAndRetention("example",
            audio_recording_enabled=False,
            motion_based_retention_enabled=False,
            motion_detector_version=2,
            profile_id="1234",
            quality="Standard",
            resolution="1280x720",
            restricted_bandwidth_mode_enabled=False,
            serial="string")
        pulumi.export("merakiDevicesCameraQualityAndRetentionExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:devices/cameraQualityAndRetention:CameraQualityAndRetention example "serial"
        ```

        :param str resource_name: The name of the resource.
        :param CameraQualityAndRetentionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CameraQualityAndRetentionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audio_recording_enabled: Optional[pulumi.Input[bool]] = None,
                 motion_based_retention_enabled: Optional[pulumi.Input[bool]] = None,
                 motion_detector_version: Optional[pulumi.Input[int]] = None,
                 profile_id: Optional[pulumi.Input[str]] = None,
                 quality: Optional[pulumi.Input[str]] = None,
                 resolution: Optional[pulumi.Input[str]] = None,
                 restricted_bandwidth_mode_enabled: Optional[pulumi.Input[bool]] = None,
                 serial: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CameraQualityAndRetentionArgs.__new__(CameraQualityAndRetentionArgs)

            __props__.__dict__["audio_recording_enabled"] = audio_recording_enabled
            __props__.__dict__["motion_based_retention_enabled"] = motion_based_retention_enabled
            __props__.__dict__["motion_detector_version"] = motion_detector_version
            __props__.__dict__["profile_id"] = profile_id
            __props__.__dict__["quality"] = quality
            __props__.__dict__["resolution"] = resolution
            __props__.__dict__["restricted_bandwidth_mode_enabled"] = restricted_bandwidth_mode_enabled
            if serial is None and not opts.urn:
                raise TypeError("Missing required property 'serial'")
            __props__.__dict__["serial"] = serial
        super(CameraQualityAndRetention, __self__).__init__(
            'meraki:devices/cameraQualityAndRetention:CameraQualityAndRetention',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            audio_recording_enabled: Optional[pulumi.Input[bool]] = None,
            motion_based_retention_enabled: Optional[pulumi.Input[bool]] = None,
            motion_detector_version: Optional[pulumi.Input[int]] = None,
            profile_id: Optional[pulumi.Input[str]] = None,
            quality: Optional[pulumi.Input[str]] = None,
            resolution: Optional[pulumi.Input[str]] = None,
            restricted_bandwidth_mode_enabled: Optional[pulumi.Input[bool]] = None,
            serial: Optional[pulumi.Input[str]] = None) -> 'CameraQualityAndRetention':
        """
        Get an existing CameraQualityAndRetention resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] audio_recording_enabled: Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
        :param pulumi.Input[bool] motion_based_retention_enabled: Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
        :param pulumi.Input[int] motion_detector_version: The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        :param pulumi.Input[str] profile_id: The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        :param pulumi.Input[str] quality: Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
        :param pulumi.Input[str] resolution: Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
        :param pulumi.Input[bool] restricted_bandwidth_mode_enabled: Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
        :param pulumi.Input[str] serial: serial path parameter.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CameraQualityAndRetentionState.__new__(_CameraQualityAndRetentionState)

        __props__.__dict__["audio_recording_enabled"] = audio_recording_enabled
        __props__.__dict__["motion_based_retention_enabled"] = motion_based_retention_enabled
        __props__.__dict__["motion_detector_version"] = motion_detector_version
        __props__.__dict__["profile_id"] = profile_id
        __props__.__dict__["quality"] = quality
        __props__.__dict__["resolution"] = resolution
        __props__.__dict__["restricted_bandwidth_mode_enabled"] = restricted_bandwidth_mode_enabled
        __props__.__dict__["serial"] = serial
        return CameraQualityAndRetention(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="audioRecordingEnabled")
    def audio_recording_enabled(self) -> pulumi.Output[bool]:
        """
        Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
        """
        return pulumi.get(self, "audio_recording_enabled")

    @property
    @pulumi.getter(name="motionBasedRetentionEnabled")
    def motion_based_retention_enabled(self) -> pulumi.Output[bool]:
        """
        Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
        """
        return pulumi.get(self, "motion_based_retention_enabled")

    @property
    @pulumi.getter(name="motionDetectorVersion")
    def motion_detector_version(self) -> pulumi.Output[int]:
        """
        The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        """
        return pulumi.get(self, "motion_detector_version")

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> pulumi.Output[str]:
        """
        The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        """
        return pulumi.get(self, "profile_id")

    @property
    @pulumi.getter
    def quality(self) -> pulumi.Output[str]:
        """
        Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
        """
        return pulumi.get(self, "quality")

    @property
    @pulumi.getter
    def resolution(self) -> pulumi.Output[str]:
        """
        Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
        """
        return pulumi.get(self, "resolution")

    @property
    @pulumi.getter(name="restrictedBandwidthModeEnabled")
    def restricted_bandwidth_mode_enabled(self) -> pulumi.Output[bool]:
        """
        Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
        """
        return pulumi.get(self, "restricted_bandwidth_mode_enabled")

    @property
    @pulumi.getter
    def serial(self) -> pulumi.Output[str]:
        """
        serial path parameter.
        """
        return pulumi.get(self, "serial")

