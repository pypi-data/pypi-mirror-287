# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CliDeviceTemplateArgs', 'CliDeviceTemplate']

@pulumi.input_type
class CliDeviceTemplateArgs:
    def __init__(__self__, *,
                 cli_configuration: pulumi.Input[str],
                 cli_type: pulumi.Input[str],
                 description: pulumi.Input[str],
                 device_type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CliDeviceTemplate resource.
        :param pulumi.Input[str] cli_configuration: CLI configuration
        :param pulumi.Input[str] cli_type: CLI type - Choices: `device`, `intend`
        :param pulumi.Input[str] description: The description of the device template
        :param pulumi.Input[str] device_type: The device type (e.g., `vedge-ISR-4331`)
        :param pulumi.Input[str] name: The name of the device template
        """
        pulumi.set(__self__, "cli_configuration", cli_configuration)
        pulumi.set(__self__, "cli_type", cli_type)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "device_type", device_type)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="cliConfiguration")
    def cli_configuration(self) -> pulumi.Input[str]:
        """
        CLI configuration
        """
        return pulumi.get(self, "cli_configuration")

    @cli_configuration.setter
    def cli_configuration(self, value: pulumi.Input[str]):
        pulumi.set(self, "cli_configuration", value)

    @property
    @pulumi.getter(name="cliType")
    def cli_type(self) -> pulumi.Input[str]:
        """
        CLI type - Choices: `device`, `intend`
        """
        return pulumi.get(self, "cli_type")

    @cli_type.setter
    def cli_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "cli_type", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the device template
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> pulumi.Input[str]:
        """
        The device type (e.g., `vedge-ISR-4331`)
        """
        return pulumi.get(self, "device_type")

    @device_type.setter
    def device_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the device template
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CliDeviceTemplateState:
    def __init__(__self__, *,
                 cli_configuration: Optional[pulumi.Input[str]] = None,
                 cli_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering CliDeviceTemplate resources.
        :param pulumi.Input[str] cli_configuration: CLI configuration
        :param pulumi.Input[str] cli_type: CLI type - Choices: `device`, `intend`
        :param pulumi.Input[str] description: The description of the device template
        :param pulumi.Input[str] device_type: The device type (e.g., `vedge-ISR-4331`)
        :param pulumi.Input[str] name: The name of the device template
        :param pulumi.Input[int] version: The version of the object
        """
        if cli_configuration is not None:
            pulumi.set(__self__, "cli_configuration", cli_configuration)
        if cli_type is not None:
            pulumi.set(__self__, "cli_type", cli_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_type is not None:
            pulumi.set(__self__, "device_type", device_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="cliConfiguration")
    def cli_configuration(self) -> Optional[pulumi.Input[str]]:
        """
        CLI configuration
        """
        return pulumi.get(self, "cli_configuration")

    @cli_configuration.setter
    def cli_configuration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cli_configuration", value)

    @property
    @pulumi.getter(name="cliType")
    def cli_type(self) -> Optional[pulumi.Input[str]]:
        """
        CLI type - Choices: `device`, `intend`
        """
        return pulumi.get(self, "cli_type")

    @cli_type.setter
    def cli_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cli_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the device template
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> Optional[pulumi.Input[str]]:
        """
        The device type (e.g., `vedge-ISR-4331`)
        """
        return pulumi.get(self, "device_type")

    @device_type.setter
    def device_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the device template
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        The version of the object
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class CliDeviceTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cli_configuration: Optional[pulumi.Input[str]] = None,
                 cli_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource can manage a CLI Device Template .

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sdwan as sdwan

        example = sdwan.CliDeviceTemplate("example",
            name="Example",
            description="My description",
            device_type="vedge-ISR-4331",
            cli_type="device",
            cli_configuration=\"\"\" system
         host-name             R1-ISR4331-1200-1\"\"\")
        ```

        ## Import

        ```sh
        $ pulumi import sdwan:index/cliDeviceTemplate:CliDeviceTemplate example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cli_configuration: CLI configuration
        :param pulumi.Input[str] cli_type: CLI type - Choices: `device`, `intend`
        :param pulumi.Input[str] description: The description of the device template
        :param pulumi.Input[str] device_type: The device type (e.g., `vedge-ISR-4331`)
        :param pulumi.Input[str] name: The name of the device template
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CliDeviceTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage a CLI Device Template .

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sdwan as sdwan

        example = sdwan.CliDeviceTemplate("example",
            name="Example",
            description="My description",
            device_type="vedge-ISR-4331",
            cli_type="device",
            cli_configuration=\"\"\" system
         host-name             R1-ISR4331-1200-1\"\"\")
        ```

        ## Import

        ```sh
        $ pulumi import sdwan:index/cliDeviceTemplate:CliDeviceTemplate example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param CliDeviceTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CliDeviceTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cli_configuration: Optional[pulumi.Input[str]] = None,
                 cli_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CliDeviceTemplateArgs.__new__(CliDeviceTemplateArgs)

            if cli_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'cli_configuration'")
            __props__.__dict__["cli_configuration"] = cli_configuration
            if cli_type is None and not opts.urn:
                raise TypeError("Missing required property 'cli_type'")
            __props__.__dict__["cli_type"] = cli_type
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if device_type is None and not opts.urn:
                raise TypeError("Missing required property 'device_type'")
            __props__.__dict__["device_type"] = device_type
            __props__.__dict__["name"] = name
            __props__.__dict__["version"] = None
        super(CliDeviceTemplate, __self__).__init__(
            'sdwan:index/cliDeviceTemplate:CliDeviceTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cli_configuration: Optional[pulumi.Input[str]] = None,
            cli_type: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            device_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'CliDeviceTemplate':
        """
        Get an existing CliDeviceTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cli_configuration: CLI configuration
        :param pulumi.Input[str] cli_type: CLI type - Choices: `device`, `intend`
        :param pulumi.Input[str] description: The description of the device template
        :param pulumi.Input[str] device_type: The device type (e.g., `vedge-ISR-4331`)
        :param pulumi.Input[str] name: The name of the device template
        :param pulumi.Input[int] version: The version of the object
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CliDeviceTemplateState.__new__(_CliDeviceTemplateState)

        __props__.__dict__["cli_configuration"] = cli_configuration
        __props__.__dict__["cli_type"] = cli_type
        __props__.__dict__["description"] = description
        __props__.__dict__["device_type"] = device_type
        __props__.__dict__["name"] = name
        __props__.__dict__["version"] = version
        return CliDeviceTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cliConfiguration")
    def cli_configuration(self) -> pulumi.Output[str]:
        """
        CLI configuration
        """
        return pulumi.get(self, "cli_configuration")

    @property
    @pulumi.getter(name="cliType")
    def cli_type(self) -> pulumi.Output[str]:
        """
        CLI type - Choices: `device`, `intend`
        """
        return pulumi.get(self, "cli_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the device template
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> pulumi.Output[str]:
        """
        The device type (e.g., `vedge-ISR-4331`)
        """
        return pulumi.get(self, "device_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the device template
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The version of the object
        """
        return pulumi.get(self, "version")

