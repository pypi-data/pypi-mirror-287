# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetConfigurationGroupDevicesResult',
    'AwaitableGetConfigurationGroupDevicesResult',
    'get_configuration_group_devices',
    'get_configuration_group_devices_output',
]

@pulumi.output_type
class GetConfigurationGroupDevicesResult:
    """
    A collection of values returned by getConfigurationGroupDevices.
    """
    def __init__(__self__, configuration_group_id=None, devices=None, id=None):
        if configuration_group_id and not isinstance(configuration_group_id, str):
            raise TypeError("Expected argument 'configuration_group_id' to be a str")
        pulumi.set(__self__, "configuration_group_id", configuration_group_id)
        if devices and not isinstance(devices, list):
            raise TypeError("Expected argument 'devices' to be a list")
        pulumi.set(__self__, "devices", devices)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="configurationGroupId")
    def configuration_group_id(self) -> str:
        """
        Configuration Group ID
        """
        return pulumi.get(self, "configuration_group_id")

    @property
    @pulumi.getter
    def devices(self) -> Sequence['outputs.GetConfigurationGroupDevicesDeviceResult']:
        """
        List of devices
        """
        return pulumi.get(self, "devices")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the object
        """
        return pulumi.get(self, "id")


class AwaitableGetConfigurationGroupDevicesResult(GetConfigurationGroupDevicesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationGroupDevicesResult(
            configuration_group_id=self.configuration_group_id,
            devices=self.devices,
            id=self.id)


def get_configuration_group_devices(configuration_group_id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationGroupDevicesResult:
    """
    This data source can read the Configuration Group Devices .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_configuration_group_devices(configuration_group_id="f6dd22c8-0b4f-496c-9a0b-6813d1f8b8ac")
    ```


    :param str configuration_group_id: Configuration Group ID
    """
    __args__ = dict()
    __args__['configurationGroupId'] = configuration_group_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getConfigurationGroupDevices:getConfigurationGroupDevices', __args__, opts=opts, typ=GetConfigurationGroupDevicesResult).value

    return AwaitableGetConfigurationGroupDevicesResult(
        configuration_group_id=pulumi.get(__ret__, 'configuration_group_id'),
        devices=pulumi.get(__ret__, 'devices'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_configuration_group_devices)
def get_configuration_group_devices_output(configuration_group_id: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationGroupDevicesResult]:
    """
    This data source can read the Configuration Group Devices .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_configuration_group_devices(configuration_group_id="f6dd22c8-0b4f-496c-9a0b-6813d1f8b8ac")
    ```


    :param str configuration_group_id: Configuration Group ID
    """
    ...
