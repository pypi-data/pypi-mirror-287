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
    'GetCiscoDhcpServerFeatureTemplateResult',
    'AwaitableGetCiscoDhcpServerFeatureTemplateResult',
    'get_cisco_dhcp_server_feature_template',
    'get_cisco_dhcp_server_feature_template_output',
]

@pulumi.output_type
class GetCiscoDhcpServerFeatureTemplateResult:
    """
    A collection of values returned by getCiscoDhcpServerFeatureTemplate.
    """
    def __init__(__self__, address_pool=None, address_pool_variable=None, default_gateway=None, default_gateway_variable=None, description=None, device_types=None, dns_servers=None, dns_servers_variable=None, domain_name=None, domain_name_variable=None, exclude_addresses=None, exclude_addresses_variable=None, id=None, interface_mtu=None, interface_mtu_variable=None, lease_time=None, lease_time_variable=None, name=None, options=None, static_leases=None, template_type=None, tftp_servers=None, tftp_servers_variable=None, version=None):
        if address_pool and not isinstance(address_pool, str):
            raise TypeError("Expected argument 'address_pool' to be a str")
        pulumi.set(__self__, "address_pool", address_pool)
        if address_pool_variable and not isinstance(address_pool_variable, str):
            raise TypeError("Expected argument 'address_pool_variable' to be a str")
        pulumi.set(__self__, "address_pool_variable", address_pool_variable)
        if default_gateway and not isinstance(default_gateway, str):
            raise TypeError("Expected argument 'default_gateway' to be a str")
        pulumi.set(__self__, "default_gateway", default_gateway)
        if default_gateway_variable and not isinstance(default_gateway_variable, str):
            raise TypeError("Expected argument 'default_gateway_variable' to be a str")
        pulumi.set(__self__, "default_gateway_variable", default_gateway_variable)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if device_types and not isinstance(device_types, list):
            raise TypeError("Expected argument 'device_types' to be a list")
        pulumi.set(__self__, "device_types", device_types)
        if dns_servers and not isinstance(dns_servers, list):
            raise TypeError("Expected argument 'dns_servers' to be a list")
        pulumi.set(__self__, "dns_servers", dns_servers)
        if dns_servers_variable and not isinstance(dns_servers_variable, str):
            raise TypeError("Expected argument 'dns_servers_variable' to be a str")
        pulumi.set(__self__, "dns_servers_variable", dns_servers_variable)
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if domain_name_variable and not isinstance(domain_name_variable, str):
            raise TypeError("Expected argument 'domain_name_variable' to be a str")
        pulumi.set(__self__, "domain_name_variable", domain_name_variable)
        if exclude_addresses and not isinstance(exclude_addresses, list):
            raise TypeError("Expected argument 'exclude_addresses' to be a list")
        pulumi.set(__self__, "exclude_addresses", exclude_addresses)
        if exclude_addresses_variable and not isinstance(exclude_addresses_variable, str):
            raise TypeError("Expected argument 'exclude_addresses_variable' to be a str")
        pulumi.set(__self__, "exclude_addresses_variable", exclude_addresses_variable)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interface_mtu and not isinstance(interface_mtu, int):
            raise TypeError("Expected argument 'interface_mtu' to be a int")
        pulumi.set(__self__, "interface_mtu", interface_mtu)
        if interface_mtu_variable and not isinstance(interface_mtu_variable, str):
            raise TypeError("Expected argument 'interface_mtu_variable' to be a str")
        pulumi.set(__self__, "interface_mtu_variable", interface_mtu_variable)
        if lease_time and not isinstance(lease_time, int):
            raise TypeError("Expected argument 'lease_time' to be a int")
        pulumi.set(__self__, "lease_time", lease_time)
        if lease_time_variable and not isinstance(lease_time_variable, str):
            raise TypeError("Expected argument 'lease_time_variable' to be a str")
        pulumi.set(__self__, "lease_time_variable", lease_time_variable)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if options and not isinstance(options, list):
            raise TypeError("Expected argument 'options' to be a list")
        pulumi.set(__self__, "options", options)
        if static_leases and not isinstance(static_leases, list):
            raise TypeError("Expected argument 'static_leases' to be a list")
        pulumi.set(__self__, "static_leases", static_leases)
        if template_type and not isinstance(template_type, str):
            raise TypeError("Expected argument 'template_type' to be a str")
        pulumi.set(__self__, "template_type", template_type)
        if tftp_servers and not isinstance(tftp_servers, list):
            raise TypeError("Expected argument 'tftp_servers' to be a list")
        pulumi.set(__self__, "tftp_servers", tftp_servers)
        if tftp_servers_variable and not isinstance(tftp_servers_variable, str):
            raise TypeError("Expected argument 'tftp_servers_variable' to be a str")
        pulumi.set(__self__, "tftp_servers_variable", tftp_servers_variable)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="addressPool")
    def address_pool(self) -> str:
        """
        Configure IPv4 prefix range of the DHCP address pool
        """
        return pulumi.get(self, "address_pool")

    @property
    @pulumi.getter(name="addressPoolVariable")
    def address_pool_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "address_pool_variable")

    @property
    @pulumi.getter(name="defaultGateway")
    def default_gateway(self) -> str:
        """
        Set IP address of default gateway
        """
        return pulumi.get(self, "default_gateway")

    @property
    @pulumi.getter(name="defaultGatewayVariable")
    def default_gateway_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "default_gateway_variable")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the feature template
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceTypes")
    def device_types(self) -> Sequence[str]:
        """
        List of supported device types
        """
        return pulumi.get(self, "device_types")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Sequence[str]:
        """
        Configure one or more DNS server IP addresses
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter(name="dnsServersVariable")
    def dns_servers_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "dns_servers_variable")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        """
        Set domain name client uses to resolve hostnames
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="domainNameVariable")
    def domain_name_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "domain_name_variable")

    @property
    @pulumi.getter(name="excludeAddresses")
    def exclude_addresses(self) -> Sequence[str]:
        """
        Configure IPv4 address to exclude from DHCP address pool
        """
        return pulumi.get(self, "exclude_addresses")

    @property
    @pulumi.getter(name="excludeAddressesVariable")
    def exclude_addresses_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "exclude_addresses_variable")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the feature template
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="interfaceMtu")
    def interface_mtu(self) -> int:
        """
        Set MTU on interface to DHCP client
        """
        return pulumi.get(self, "interface_mtu")

    @property
    @pulumi.getter(name="interfaceMtuVariable")
    def interface_mtu_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "interface_mtu_variable")

    @property
    @pulumi.getter(name="leaseTime")
    def lease_time(self) -> int:
        """
        Configure how long a DHCP-assigned IP address is valid
        """
        return pulumi.get(self, "lease_time")

    @property
    @pulumi.getter(name="leaseTimeVariable")
    def lease_time_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "lease_time_variable")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the feature template
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> Sequence['outputs.GetCiscoDhcpServerFeatureTemplateOptionResult']:
        """
        Configure Options Code
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="staticLeases")
    def static_leases(self) -> Sequence['outputs.GetCiscoDhcpServerFeatureTemplateStaticLeaseResult']:
        """
        Configure static IP addresses
        """
        return pulumi.get(self, "static_leases")

    @property
    @pulumi.getter(name="templateType")
    def template_type(self) -> str:
        """
        The template type
        """
        return pulumi.get(self, "template_type")

    @property
    @pulumi.getter(name="tftpServers")
    def tftp_servers(self) -> Sequence[str]:
        """
        Configure TFTP server IP addresses
        """
        return pulumi.get(self, "tftp_servers")

    @property
    @pulumi.getter(name="tftpServersVariable")
    def tftp_servers_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "tftp_servers_variable")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The version of the feature template
        """
        return pulumi.get(self, "version")


class AwaitableGetCiscoDhcpServerFeatureTemplateResult(GetCiscoDhcpServerFeatureTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCiscoDhcpServerFeatureTemplateResult(
            address_pool=self.address_pool,
            address_pool_variable=self.address_pool_variable,
            default_gateway=self.default_gateway,
            default_gateway_variable=self.default_gateway_variable,
            description=self.description,
            device_types=self.device_types,
            dns_servers=self.dns_servers,
            dns_servers_variable=self.dns_servers_variable,
            domain_name=self.domain_name,
            domain_name_variable=self.domain_name_variable,
            exclude_addresses=self.exclude_addresses,
            exclude_addresses_variable=self.exclude_addresses_variable,
            id=self.id,
            interface_mtu=self.interface_mtu,
            interface_mtu_variable=self.interface_mtu_variable,
            lease_time=self.lease_time,
            lease_time_variable=self.lease_time_variable,
            name=self.name,
            options=self.options,
            static_leases=self.static_leases,
            template_type=self.template_type,
            tftp_servers=self.tftp_servers,
            tftp_servers_variable=self.tftp_servers_variable,
            version=self.version)


def get_cisco_dhcp_server_feature_template(id: Optional[str] = None,
                                           name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCiscoDhcpServerFeatureTemplateResult:
    """
    This data source can read the Cisco DHCP Server feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_cisco_dhcp_server_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getCiscoDhcpServerFeatureTemplate:getCiscoDhcpServerFeatureTemplate', __args__, opts=opts, typ=GetCiscoDhcpServerFeatureTemplateResult).value

    return AwaitableGetCiscoDhcpServerFeatureTemplateResult(
        address_pool=pulumi.get(__ret__, 'address_pool'),
        address_pool_variable=pulumi.get(__ret__, 'address_pool_variable'),
        default_gateway=pulumi.get(__ret__, 'default_gateway'),
        default_gateway_variable=pulumi.get(__ret__, 'default_gateway_variable'),
        description=pulumi.get(__ret__, 'description'),
        device_types=pulumi.get(__ret__, 'device_types'),
        dns_servers=pulumi.get(__ret__, 'dns_servers'),
        dns_servers_variable=pulumi.get(__ret__, 'dns_servers_variable'),
        domain_name=pulumi.get(__ret__, 'domain_name'),
        domain_name_variable=pulumi.get(__ret__, 'domain_name_variable'),
        exclude_addresses=pulumi.get(__ret__, 'exclude_addresses'),
        exclude_addresses_variable=pulumi.get(__ret__, 'exclude_addresses_variable'),
        id=pulumi.get(__ret__, 'id'),
        interface_mtu=pulumi.get(__ret__, 'interface_mtu'),
        interface_mtu_variable=pulumi.get(__ret__, 'interface_mtu_variable'),
        lease_time=pulumi.get(__ret__, 'lease_time'),
        lease_time_variable=pulumi.get(__ret__, 'lease_time_variable'),
        name=pulumi.get(__ret__, 'name'),
        options=pulumi.get(__ret__, 'options'),
        static_leases=pulumi.get(__ret__, 'static_leases'),
        template_type=pulumi.get(__ret__, 'template_type'),
        tftp_servers=pulumi.get(__ret__, 'tftp_servers'),
        tftp_servers_variable=pulumi.get(__ret__, 'tftp_servers_variable'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_cisco_dhcp_server_feature_template)
def get_cisco_dhcp_server_feature_template_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                                  name: Optional[pulumi.Input[Optional[str]]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCiscoDhcpServerFeatureTemplateResult]:
    """
    This data source can read the Cisco DHCP Server feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_cisco_dhcp_server_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    ...
