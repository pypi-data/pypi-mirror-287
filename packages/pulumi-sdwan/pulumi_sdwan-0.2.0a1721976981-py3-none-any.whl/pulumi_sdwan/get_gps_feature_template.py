# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetGpsFeatureTemplateResult',
    'AwaitableGetGpsFeatureTemplateResult',
    'get_gps_feature_template',
    'get_gps_feature_template_output',
]

@pulumi.output_type
class GetGpsFeatureTemplateResult:
    """
    A collection of values returned by getGpsFeatureTemplate.
    """
    def __init__(__self__, description=None, destination_address=None, destination_address_variable=None, destination_port=None, destination_port_variable=None, device_types=None, enable=None, enable_variable=None, gps_mode=None, gps_mode_variable=None, id=None, name=None, nmea=None, nmea_variable=None, source_address=None, source_address_variable=None, template_type=None, version=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if destination_address and not isinstance(destination_address, str):
            raise TypeError("Expected argument 'destination_address' to be a str")
        pulumi.set(__self__, "destination_address", destination_address)
        if destination_address_variable and not isinstance(destination_address_variable, str):
            raise TypeError("Expected argument 'destination_address_variable' to be a str")
        pulumi.set(__self__, "destination_address_variable", destination_address_variable)
        if destination_port and not isinstance(destination_port, int):
            raise TypeError("Expected argument 'destination_port' to be a int")
        pulumi.set(__self__, "destination_port", destination_port)
        if destination_port_variable and not isinstance(destination_port_variable, str):
            raise TypeError("Expected argument 'destination_port_variable' to be a str")
        pulumi.set(__self__, "destination_port_variable", destination_port_variable)
        if device_types and not isinstance(device_types, list):
            raise TypeError("Expected argument 'device_types' to be a list")
        pulumi.set(__self__, "device_types", device_types)
        if enable and not isinstance(enable, bool):
            raise TypeError("Expected argument 'enable' to be a bool")
        pulumi.set(__self__, "enable", enable)
        if enable_variable and not isinstance(enable_variable, str):
            raise TypeError("Expected argument 'enable_variable' to be a str")
        pulumi.set(__self__, "enable_variable", enable_variable)
        if gps_mode and not isinstance(gps_mode, str):
            raise TypeError("Expected argument 'gps_mode' to be a str")
        pulumi.set(__self__, "gps_mode", gps_mode)
        if gps_mode_variable and not isinstance(gps_mode_variable, str):
            raise TypeError("Expected argument 'gps_mode_variable' to be a str")
        pulumi.set(__self__, "gps_mode_variable", gps_mode_variable)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nmea and not isinstance(nmea, bool):
            raise TypeError("Expected argument 'nmea' to be a bool")
        pulumi.set(__self__, "nmea", nmea)
        if nmea_variable and not isinstance(nmea_variable, str):
            raise TypeError("Expected argument 'nmea_variable' to be a str")
        pulumi.set(__self__, "nmea_variable", nmea_variable)
        if source_address and not isinstance(source_address, str):
            raise TypeError("Expected argument 'source_address' to be a str")
        pulumi.set(__self__, "source_address", source_address)
        if source_address_variable and not isinstance(source_address_variable, str):
            raise TypeError("Expected argument 'source_address_variable' to be a str")
        pulumi.set(__self__, "source_address_variable", source_address_variable)
        if template_type and not isinstance(template_type, str):
            raise TypeError("Expected argument 'template_type' to be a str")
        pulumi.set(__self__, "template_type", template_type)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the feature template
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> str:
        """
        Destination address
        """
        return pulumi.get(self, "destination_address")

    @property
    @pulumi.getter(name="destinationAddressVariable")
    def destination_address_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "destination_address_variable")

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> int:
        """
        Destination port
        """
        return pulumi.get(self, "destination_port")

    @property
    @pulumi.getter(name="destinationPortVariable")
    def destination_port_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "destination_port_variable")

    @property
    @pulumi.getter(name="deviceTypes")
    def device_types(self) -> Sequence[str]:
        """
        List of supported device types
        """
        return pulumi.get(self, "device_types")

    @property
    @pulumi.getter
    def enable(self) -> bool:
        """
        Enable/disable GPS
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter(name="enableVariable")
    def enable_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "enable_variable")

    @property
    @pulumi.getter(name="gpsMode")
    def gps_mode(self) -> str:
        """
        Select GPS mode
        """
        return pulumi.get(self, "gps_mode")

    @property
    @pulumi.getter(name="gpsModeVariable")
    def gps_mode_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "gps_mode_variable")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the feature template
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the feature template
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nmea(self) -> bool:
        """
        Enable/disable NMEA data
        """
        return pulumi.get(self, "nmea")

    @property
    @pulumi.getter(name="nmeaVariable")
    def nmea_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "nmea_variable")

    @property
    @pulumi.getter(name="sourceAddress")
    def source_address(self) -> str:
        """
        Source address
        """
        return pulumi.get(self, "source_address")

    @property
    @pulumi.getter(name="sourceAddressVariable")
    def source_address_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "source_address_variable")

    @property
    @pulumi.getter(name="templateType")
    def template_type(self) -> str:
        """
        The template type
        """
        return pulumi.get(self, "template_type")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The version of the feature template
        """
        return pulumi.get(self, "version")


class AwaitableGetGpsFeatureTemplateResult(GetGpsFeatureTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGpsFeatureTemplateResult(
            description=self.description,
            destination_address=self.destination_address,
            destination_address_variable=self.destination_address_variable,
            destination_port=self.destination_port,
            destination_port_variable=self.destination_port_variable,
            device_types=self.device_types,
            enable=self.enable,
            enable_variable=self.enable_variable,
            gps_mode=self.gps_mode,
            gps_mode_variable=self.gps_mode_variable,
            id=self.id,
            name=self.name,
            nmea=self.nmea,
            nmea_variable=self.nmea_variable,
            source_address=self.source_address,
            source_address_variable=self.source_address_variable,
            template_type=self.template_type,
            version=self.version)


def get_gps_feature_template(id: Optional[str] = None,
                             name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGpsFeatureTemplateResult:
    """
    This data source can read the gps feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_gps_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getGpsFeatureTemplate:getGpsFeatureTemplate', __args__, opts=opts, typ=GetGpsFeatureTemplateResult).value

    return AwaitableGetGpsFeatureTemplateResult(
        description=pulumi.get(__ret__, 'description'),
        destination_address=pulumi.get(__ret__, 'destination_address'),
        destination_address_variable=pulumi.get(__ret__, 'destination_address_variable'),
        destination_port=pulumi.get(__ret__, 'destination_port'),
        destination_port_variable=pulumi.get(__ret__, 'destination_port_variable'),
        device_types=pulumi.get(__ret__, 'device_types'),
        enable=pulumi.get(__ret__, 'enable'),
        enable_variable=pulumi.get(__ret__, 'enable_variable'),
        gps_mode=pulumi.get(__ret__, 'gps_mode'),
        gps_mode_variable=pulumi.get(__ret__, 'gps_mode_variable'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        nmea=pulumi.get(__ret__, 'nmea'),
        nmea_variable=pulumi.get(__ret__, 'nmea_variable'),
        source_address=pulumi.get(__ret__, 'source_address'),
        source_address_variable=pulumi.get(__ret__, 'source_address_variable'),
        template_type=pulumi.get(__ret__, 'template_type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_gps_feature_template)
def get_gps_feature_template_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                    name: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGpsFeatureTemplateResult]:
    """
    This data source can read the gps feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_gps_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    ...
