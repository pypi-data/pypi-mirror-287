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
from ._inputs import *

__all__ = ['CiscoSecureInternetGatewayFeatureTemplateArgs', 'CiscoSecureInternetGatewayFeatureTemplate']

@pulumi.input_type
class CiscoSecureInternetGatewayFeatureTemplateArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 device_types: pulumi.Input[Sequence[pulumi.Input[str]]],
                 interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]] = None,
                 tracker_source_ip: Optional[pulumi.Input[str]] = None,
                 tracker_source_ip_variable: Optional[pulumi.Input[str]] = None,
                 trackers: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]] = None,
                 vpn_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a CiscoSecureInternetGatewayFeatureTemplate resource.
        :param pulumi.Input[str] description: The description of the feature template
        :param pulumi.Input[Sequence[pulumi.Input[str]]] device_types: List of supported device types - Choices: `vedge-C8000V`, `vedge-C8300-1N1S-4T2X`, `vedge-C8300-1N1S-6T`,
               `vedge-C8300-2N2S-6T`, `vedge-C8300-2N2S-4T2X`, `vedge-C8500-12X4QC`, `vedge-C8500-12X`, `vedge-C8500-20X6C`,
               `vedge-C8500L-8S4X`, `vedge-C8200-1N-4T`, `vedge-C8200L-1N-4T`
        :param pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]] interfaces: Interface name: IPsec when present
        :param pulumi.Input[str] name: The name of the feature template
        :param pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]] services: Configure services
        :param pulumi.Input[str] tracker_source_ip: Source IP address for Tracker
        :param pulumi.Input[str] tracker_source_ip_variable: Variable name
        :param pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]] trackers: Tracker configuration
        :param pulumi.Input[int] vpn_id: List of VPN instances - Range: `0`-`65527` - Default value: `0`
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "device_types", device_types)
        if interfaces is not None:
            pulumi.set(__self__, "interfaces", interfaces)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if services is not None:
            pulumi.set(__self__, "services", services)
        if tracker_source_ip is not None:
            pulumi.set(__self__, "tracker_source_ip", tracker_source_ip)
        if tracker_source_ip_variable is not None:
            pulumi.set(__self__, "tracker_source_ip_variable", tracker_source_ip_variable)
        if trackers is not None:
            pulumi.set(__self__, "trackers", trackers)
        if vpn_id is not None:
            pulumi.set(__self__, "vpn_id", vpn_id)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the feature template
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceTypes")
    def device_types(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of supported device types - Choices: `vedge-C8000V`, `vedge-C8300-1N1S-4T2X`, `vedge-C8300-1N1S-6T`,
        `vedge-C8300-2N2S-6T`, `vedge-C8300-2N2S-4T2X`, `vedge-C8500-12X4QC`, `vedge-C8500-12X`, `vedge-C8500-20X6C`,
        `vedge-C8500L-8S4X`, `vedge-C8200-1N-4T`, `vedge-C8200L-1N-4T`
        """
        return pulumi.get(self, "device_types")

    @device_types.setter
    def device_types(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "device_types", value)

    @property
    @pulumi.getter
    def interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]]:
        """
        Interface name: IPsec when present
        """
        return pulumi.get(self, "interfaces")

    @interfaces.setter
    def interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]]):
        pulumi.set(self, "interfaces", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the feature template
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]]:
        """
        Configure services
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]]):
        pulumi.set(self, "services", value)

    @property
    @pulumi.getter(name="trackerSourceIp")
    def tracker_source_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Source IP address for Tracker
        """
        return pulumi.get(self, "tracker_source_ip")

    @tracker_source_ip.setter
    def tracker_source_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tracker_source_ip", value)

    @property
    @pulumi.getter(name="trackerSourceIpVariable")
    def tracker_source_ip_variable(self) -> Optional[pulumi.Input[str]]:
        """
        Variable name
        """
        return pulumi.get(self, "tracker_source_ip_variable")

    @tracker_source_ip_variable.setter
    def tracker_source_ip_variable(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tracker_source_ip_variable", value)

    @property
    @pulumi.getter
    def trackers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]]:
        """
        Tracker configuration
        """
        return pulumi.get(self, "trackers")

    @trackers.setter
    def trackers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]]):
        pulumi.set(self, "trackers", value)

    @property
    @pulumi.getter(name="vpnId")
    def vpn_id(self) -> Optional[pulumi.Input[int]]:
        """
        List of VPN instances - Range: `0`-`65527` - Default value: `0`
        """
        return pulumi.get(self, "vpn_id")

    @vpn_id.setter
    def vpn_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vpn_id", value)


@pulumi.input_type
class _CiscoSecureInternetGatewayFeatureTemplateState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 device_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]] = None,
                 template_type: Optional[pulumi.Input[str]] = None,
                 tracker_source_ip: Optional[pulumi.Input[str]] = None,
                 tracker_source_ip_variable: Optional[pulumi.Input[str]] = None,
                 trackers: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]] = None,
                 version: Optional[pulumi.Input[int]] = None,
                 vpn_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering CiscoSecureInternetGatewayFeatureTemplate resources.
        :param pulumi.Input[str] description: The description of the feature template
        :param pulumi.Input[Sequence[pulumi.Input[str]]] device_types: List of supported device types - Choices: `vedge-C8000V`, `vedge-C8300-1N1S-4T2X`, `vedge-C8300-1N1S-6T`,
               `vedge-C8300-2N2S-6T`, `vedge-C8300-2N2S-4T2X`, `vedge-C8500-12X4QC`, `vedge-C8500-12X`, `vedge-C8500-20X6C`,
               `vedge-C8500L-8S4X`, `vedge-C8200-1N-4T`, `vedge-C8200L-1N-4T`
        :param pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]] interfaces: Interface name: IPsec when present
        :param pulumi.Input[str] name: The name of the feature template
        :param pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]] services: Configure services
        :param pulumi.Input[str] template_type: The template type
        :param pulumi.Input[str] tracker_source_ip: Source IP address for Tracker
        :param pulumi.Input[str] tracker_source_ip_variable: Variable name
        :param pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]] trackers: Tracker configuration
        :param pulumi.Input[int] version: The version of the feature template
        :param pulumi.Input[int] vpn_id: List of VPN instances - Range: `0`-`65527` - Default value: `0`
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_types is not None:
            pulumi.set(__self__, "device_types", device_types)
        if interfaces is not None:
            pulumi.set(__self__, "interfaces", interfaces)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if services is not None:
            pulumi.set(__self__, "services", services)
        if template_type is not None:
            pulumi.set(__self__, "template_type", template_type)
        if tracker_source_ip is not None:
            pulumi.set(__self__, "tracker_source_ip", tracker_source_ip)
        if tracker_source_ip_variable is not None:
            pulumi.set(__self__, "tracker_source_ip_variable", tracker_source_ip_variable)
        if trackers is not None:
            pulumi.set(__self__, "trackers", trackers)
        if version is not None:
            pulumi.set(__self__, "version", version)
        if vpn_id is not None:
            pulumi.set(__self__, "vpn_id", vpn_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the feature template
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceTypes")
    def device_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of supported device types - Choices: `vedge-C8000V`, `vedge-C8300-1N1S-4T2X`, `vedge-C8300-1N1S-6T`,
        `vedge-C8300-2N2S-6T`, `vedge-C8300-2N2S-4T2X`, `vedge-C8500-12X4QC`, `vedge-C8500-12X`, `vedge-C8500-20X6C`,
        `vedge-C8500L-8S4X`, `vedge-C8200-1N-4T`, `vedge-C8200L-1N-4T`
        """
        return pulumi.get(self, "device_types")

    @device_types.setter
    def device_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "device_types", value)

    @property
    @pulumi.getter
    def interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]]:
        """
        Interface name: IPsec when present
        """
        return pulumi.get(self, "interfaces")

    @interfaces.setter
    def interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]]):
        pulumi.set(self, "interfaces", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the feature template
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]]:
        """
        Configure services
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]]):
        pulumi.set(self, "services", value)

    @property
    @pulumi.getter(name="templateType")
    def template_type(self) -> Optional[pulumi.Input[str]]:
        """
        The template type
        """
        return pulumi.get(self, "template_type")

    @template_type.setter
    def template_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_type", value)

    @property
    @pulumi.getter(name="trackerSourceIp")
    def tracker_source_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Source IP address for Tracker
        """
        return pulumi.get(self, "tracker_source_ip")

    @tracker_source_ip.setter
    def tracker_source_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tracker_source_ip", value)

    @property
    @pulumi.getter(name="trackerSourceIpVariable")
    def tracker_source_ip_variable(self) -> Optional[pulumi.Input[str]]:
        """
        Variable name
        """
        return pulumi.get(self, "tracker_source_ip_variable")

    @tracker_source_ip_variable.setter
    def tracker_source_ip_variable(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tracker_source_ip_variable", value)

    @property
    @pulumi.getter
    def trackers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]]:
        """
        Tracker configuration
        """
        return pulumi.get(self, "trackers")

    @trackers.setter
    def trackers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]]):
        pulumi.set(self, "trackers", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        The version of the feature template
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="vpnId")
    def vpn_id(self) -> Optional[pulumi.Input[int]]:
        """
        List of VPN instances - Range: `0`-`65527` - Default value: `0`
        """
        return pulumi.get(self, "vpn_id")

    @vpn_id.setter
    def vpn_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vpn_id", value)


class CiscoSecureInternetGatewayFeatureTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]]] = None,
                 tracker_source_ip: Optional[pulumi.Input[str]] = None,
                 tracker_source_ip_variable: Optional[pulumi.Input[str]] = None,
                 trackers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]]] = None,
                 vpn_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        This resource can manage a Cisco Secure Internet Gateway feature template.
          - Minimum SD-WAN Manager version: `15.0.0`

        ## Import

        ```sh
        $ pulumi import sdwan:index/ciscoSecureInternetGatewayFeatureTemplate:CiscoSecureInternetGatewayFeatureTemplate example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the feature template
        :param pulumi.Input[Sequence[pulumi.Input[str]]] device_types: List of supported device types - Choices: `vedge-C8000V`, `vedge-C8300-1N1S-4T2X`, `vedge-C8300-1N1S-6T`,
               `vedge-C8300-2N2S-6T`, `vedge-C8300-2N2S-4T2X`, `vedge-C8500-12X4QC`, `vedge-C8500-12X`, `vedge-C8500-20X6C`,
               `vedge-C8500L-8S4X`, `vedge-C8200-1N-4T`, `vedge-C8200L-1N-4T`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]] interfaces: Interface name: IPsec when present
        :param pulumi.Input[str] name: The name of the feature template
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]] services: Configure services
        :param pulumi.Input[str] tracker_source_ip: Source IP address for Tracker
        :param pulumi.Input[str] tracker_source_ip_variable: Variable name
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]] trackers: Tracker configuration
        :param pulumi.Input[int] vpn_id: List of VPN instances - Range: `0`-`65527` - Default value: `0`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CiscoSecureInternetGatewayFeatureTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage a Cisco Secure Internet Gateway feature template.
          - Minimum SD-WAN Manager version: `15.0.0`

        ## Import

        ```sh
        $ pulumi import sdwan:index/ciscoSecureInternetGatewayFeatureTemplate:CiscoSecureInternetGatewayFeatureTemplate example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param CiscoSecureInternetGatewayFeatureTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CiscoSecureInternetGatewayFeatureTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]]] = None,
                 tracker_source_ip: Optional[pulumi.Input[str]] = None,
                 tracker_source_ip_variable: Optional[pulumi.Input[str]] = None,
                 trackers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]]] = None,
                 vpn_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CiscoSecureInternetGatewayFeatureTemplateArgs.__new__(CiscoSecureInternetGatewayFeatureTemplateArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if device_types is None and not opts.urn:
                raise TypeError("Missing required property 'device_types'")
            __props__.__dict__["device_types"] = device_types
            __props__.__dict__["interfaces"] = interfaces
            __props__.__dict__["name"] = name
            __props__.__dict__["services"] = services
            __props__.__dict__["tracker_source_ip"] = tracker_source_ip
            __props__.__dict__["tracker_source_ip_variable"] = tracker_source_ip_variable
            __props__.__dict__["trackers"] = trackers
            __props__.__dict__["vpn_id"] = vpn_id
            __props__.__dict__["template_type"] = None
            __props__.__dict__["version"] = None
        super(CiscoSecureInternetGatewayFeatureTemplate, __self__).__init__(
            'sdwan:index/ciscoSecureInternetGatewayFeatureTemplate:CiscoSecureInternetGatewayFeatureTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            device_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]]] = None,
            template_type: Optional[pulumi.Input[str]] = None,
            tracker_source_ip: Optional[pulumi.Input[str]] = None,
            tracker_source_ip_variable: Optional[pulumi.Input[str]] = None,
            trackers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]]] = None,
            version: Optional[pulumi.Input[int]] = None,
            vpn_id: Optional[pulumi.Input[int]] = None) -> 'CiscoSecureInternetGatewayFeatureTemplate':
        """
        Get an existing CiscoSecureInternetGatewayFeatureTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the feature template
        :param pulumi.Input[Sequence[pulumi.Input[str]]] device_types: List of supported device types - Choices: `vedge-C8000V`, `vedge-C8300-1N1S-4T2X`, `vedge-C8300-1N1S-6T`,
               `vedge-C8300-2N2S-6T`, `vedge-C8300-2N2S-4T2X`, `vedge-C8500-12X4QC`, `vedge-C8500-12X`, `vedge-C8500-20X6C`,
               `vedge-C8500L-8S4X`, `vedge-C8200-1N-4T`, `vedge-C8200L-1N-4T`
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateInterfaceArgs']]]] interfaces: Interface name: IPsec when present
        :param pulumi.Input[str] name: The name of the feature template
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateServiceArgs']]]] services: Configure services
        :param pulumi.Input[str] template_type: The template type
        :param pulumi.Input[str] tracker_source_ip: Source IP address for Tracker
        :param pulumi.Input[str] tracker_source_ip_variable: Variable name
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CiscoSecureInternetGatewayFeatureTemplateTrackerArgs']]]] trackers: Tracker configuration
        :param pulumi.Input[int] version: The version of the feature template
        :param pulumi.Input[int] vpn_id: List of VPN instances - Range: `0`-`65527` - Default value: `0`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CiscoSecureInternetGatewayFeatureTemplateState.__new__(_CiscoSecureInternetGatewayFeatureTemplateState)

        __props__.__dict__["description"] = description
        __props__.__dict__["device_types"] = device_types
        __props__.__dict__["interfaces"] = interfaces
        __props__.__dict__["name"] = name
        __props__.__dict__["services"] = services
        __props__.__dict__["template_type"] = template_type
        __props__.__dict__["tracker_source_ip"] = tracker_source_ip
        __props__.__dict__["tracker_source_ip_variable"] = tracker_source_ip_variable
        __props__.__dict__["trackers"] = trackers
        __props__.__dict__["version"] = version
        __props__.__dict__["vpn_id"] = vpn_id
        return CiscoSecureInternetGatewayFeatureTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the feature template
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceTypes")
    def device_types(self) -> pulumi.Output[Sequence[str]]:
        """
        List of supported device types - Choices: `vedge-C8000V`, `vedge-C8300-1N1S-4T2X`, `vedge-C8300-1N1S-6T`,
        `vedge-C8300-2N2S-6T`, `vedge-C8300-2N2S-4T2X`, `vedge-C8500-12X4QC`, `vedge-C8500-12X`, `vedge-C8500-20X6C`,
        `vedge-C8500L-8S4X`, `vedge-C8200-1N-4T`, `vedge-C8200L-1N-4T`
        """
        return pulumi.get(self, "device_types")

    @property
    @pulumi.getter
    def interfaces(self) -> pulumi.Output[Optional[Sequence['outputs.CiscoSecureInternetGatewayFeatureTemplateInterface']]]:
        """
        Interface name: IPsec when present
        """
        return pulumi.get(self, "interfaces")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the feature template
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def services(self) -> pulumi.Output[Optional[Sequence['outputs.CiscoSecureInternetGatewayFeatureTemplateService']]]:
        """
        Configure services
        """
        return pulumi.get(self, "services")

    @property
    @pulumi.getter(name="templateType")
    def template_type(self) -> pulumi.Output[str]:
        """
        The template type
        """
        return pulumi.get(self, "template_type")

    @property
    @pulumi.getter(name="trackerSourceIp")
    def tracker_source_ip(self) -> pulumi.Output[Optional[str]]:
        """
        Source IP address for Tracker
        """
        return pulumi.get(self, "tracker_source_ip")

    @property
    @pulumi.getter(name="trackerSourceIpVariable")
    def tracker_source_ip_variable(self) -> pulumi.Output[Optional[str]]:
        """
        Variable name
        """
        return pulumi.get(self, "tracker_source_ip_variable")

    @property
    @pulumi.getter
    def trackers(self) -> pulumi.Output[Optional[Sequence['outputs.CiscoSecureInternetGatewayFeatureTemplateTracker']]]:
        """
        Tracker configuration
        """
        return pulumi.get(self, "trackers")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The version of the feature template
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="vpnId")
    def vpn_id(self) -> pulumi.Output[Optional[int]]:
        """
        List of VPN instances - Range: `0`-`65527` - Default value: `0`
        """
        return pulumi.get(self, "vpn_id")

