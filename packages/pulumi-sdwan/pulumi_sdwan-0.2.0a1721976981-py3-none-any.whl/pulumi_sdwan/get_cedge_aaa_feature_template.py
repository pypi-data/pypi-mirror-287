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
    'GetCedgeAaaFeatureTemplateResult',
    'AwaitableGetCedgeAaaFeatureTemplateResult',
    'get_cedge_aaa_feature_template',
    'get_cedge_aaa_feature_template_output',
]

@pulumi.output_type
class GetCedgeAaaFeatureTemplateResult:
    """
    A collection of values returned by getCedgeAaaFeatureTemplate.
    """
    def __init__(__self__, accounting_rules=None, authorization_config_commands=None, authorization_config_commands_variable=None, authorization_console=None, authorization_console_variable=None, authorization_rules=None, description=None, device_types=None, dot1x_accounting=None, dot1x_accounting_variable=None, dot1x_authentication=None, dot1x_authentication_variable=None, id=None, name=None, radius_clients=None, radius_dynamic_author_authentication_type=None, radius_dynamic_author_authentication_type_variable=None, radius_dynamic_author_domain_stripping=None, radius_dynamic_author_domain_stripping_variable=None, radius_dynamic_author_port=None, radius_dynamic_author_port_variable=None, radius_dynamic_author_server_key=None, radius_dynamic_author_server_key_variable=None, radius_server_groups=None, radius_trustsec_cts_authorization_list=None, radius_trustsec_cts_authorization_list_variable=None, radius_trustsec_group=None, server_groups_priority_order=None, tacacs_server_groups=None, template_type=None, users=None, version=None):
        if accounting_rules and not isinstance(accounting_rules, list):
            raise TypeError("Expected argument 'accounting_rules' to be a list")
        pulumi.set(__self__, "accounting_rules", accounting_rules)
        if authorization_config_commands and not isinstance(authorization_config_commands, bool):
            raise TypeError("Expected argument 'authorization_config_commands' to be a bool")
        pulumi.set(__self__, "authorization_config_commands", authorization_config_commands)
        if authorization_config_commands_variable and not isinstance(authorization_config_commands_variable, str):
            raise TypeError("Expected argument 'authorization_config_commands_variable' to be a str")
        pulumi.set(__self__, "authorization_config_commands_variable", authorization_config_commands_variable)
        if authorization_console and not isinstance(authorization_console, bool):
            raise TypeError("Expected argument 'authorization_console' to be a bool")
        pulumi.set(__self__, "authorization_console", authorization_console)
        if authorization_console_variable and not isinstance(authorization_console_variable, str):
            raise TypeError("Expected argument 'authorization_console_variable' to be a str")
        pulumi.set(__self__, "authorization_console_variable", authorization_console_variable)
        if authorization_rules and not isinstance(authorization_rules, list):
            raise TypeError("Expected argument 'authorization_rules' to be a list")
        pulumi.set(__self__, "authorization_rules", authorization_rules)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if device_types and not isinstance(device_types, list):
            raise TypeError("Expected argument 'device_types' to be a list")
        pulumi.set(__self__, "device_types", device_types)
        if dot1x_accounting and not isinstance(dot1x_accounting, bool):
            raise TypeError("Expected argument 'dot1x_accounting' to be a bool")
        pulumi.set(__self__, "dot1x_accounting", dot1x_accounting)
        if dot1x_accounting_variable and not isinstance(dot1x_accounting_variable, str):
            raise TypeError("Expected argument 'dot1x_accounting_variable' to be a str")
        pulumi.set(__self__, "dot1x_accounting_variable", dot1x_accounting_variable)
        if dot1x_authentication and not isinstance(dot1x_authentication, bool):
            raise TypeError("Expected argument 'dot1x_authentication' to be a bool")
        pulumi.set(__self__, "dot1x_authentication", dot1x_authentication)
        if dot1x_authentication_variable and not isinstance(dot1x_authentication_variable, str):
            raise TypeError("Expected argument 'dot1x_authentication_variable' to be a str")
        pulumi.set(__self__, "dot1x_authentication_variable", dot1x_authentication_variable)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if radius_clients and not isinstance(radius_clients, list):
            raise TypeError("Expected argument 'radius_clients' to be a list")
        pulumi.set(__self__, "radius_clients", radius_clients)
        if radius_dynamic_author_authentication_type and not isinstance(radius_dynamic_author_authentication_type, str):
            raise TypeError("Expected argument 'radius_dynamic_author_authentication_type' to be a str")
        pulumi.set(__self__, "radius_dynamic_author_authentication_type", radius_dynamic_author_authentication_type)
        if radius_dynamic_author_authentication_type_variable and not isinstance(radius_dynamic_author_authentication_type_variable, str):
            raise TypeError("Expected argument 'radius_dynamic_author_authentication_type_variable' to be a str")
        pulumi.set(__self__, "radius_dynamic_author_authentication_type_variable", radius_dynamic_author_authentication_type_variable)
        if radius_dynamic_author_domain_stripping and not isinstance(radius_dynamic_author_domain_stripping, str):
            raise TypeError("Expected argument 'radius_dynamic_author_domain_stripping' to be a str")
        pulumi.set(__self__, "radius_dynamic_author_domain_stripping", radius_dynamic_author_domain_stripping)
        if radius_dynamic_author_domain_stripping_variable and not isinstance(radius_dynamic_author_domain_stripping_variable, str):
            raise TypeError("Expected argument 'radius_dynamic_author_domain_stripping_variable' to be a str")
        pulumi.set(__self__, "radius_dynamic_author_domain_stripping_variable", radius_dynamic_author_domain_stripping_variable)
        if radius_dynamic_author_port and not isinstance(radius_dynamic_author_port, int):
            raise TypeError("Expected argument 'radius_dynamic_author_port' to be a int")
        pulumi.set(__self__, "radius_dynamic_author_port", radius_dynamic_author_port)
        if radius_dynamic_author_port_variable and not isinstance(radius_dynamic_author_port_variable, str):
            raise TypeError("Expected argument 'radius_dynamic_author_port_variable' to be a str")
        pulumi.set(__self__, "radius_dynamic_author_port_variable", radius_dynamic_author_port_variable)
        if radius_dynamic_author_server_key and not isinstance(radius_dynamic_author_server_key, str):
            raise TypeError("Expected argument 'radius_dynamic_author_server_key' to be a str")
        pulumi.set(__self__, "radius_dynamic_author_server_key", radius_dynamic_author_server_key)
        if radius_dynamic_author_server_key_variable and not isinstance(radius_dynamic_author_server_key_variable, str):
            raise TypeError("Expected argument 'radius_dynamic_author_server_key_variable' to be a str")
        pulumi.set(__self__, "radius_dynamic_author_server_key_variable", radius_dynamic_author_server_key_variable)
        if radius_server_groups and not isinstance(radius_server_groups, list):
            raise TypeError("Expected argument 'radius_server_groups' to be a list")
        pulumi.set(__self__, "radius_server_groups", radius_server_groups)
        if radius_trustsec_cts_authorization_list and not isinstance(radius_trustsec_cts_authorization_list, str):
            raise TypeError("Expected argument 'radius_trustsec_cts_authorization_list' to be a str")
        pulumi.set(__self__, "radius_trustsec_cts_authorization_list", radius_trustsec_cts_authorization_list)
        if radius_trustsec_cts_authorization_list_variable and not isinstance(radius_trustsec_cts_authorization_list_variable, str):
            raise TypeError("Expected argument 'radius_trustsec_cts_authorization_list_variable' to be a str")
        pulumi.set(__self__, "radius_trustsec_cts_authorization_list_variable", radius_trustsec_cts_authorization_list_variable)
        if radius_trustsec_group and not isinstance(radius_trustsec_group, str):
            raise TypeError("Expected argument 'radius_trustsec_group' to be a str")
        pulumi.set(__self__, "radius_trustsec_group", radius_trustsec_group)
        if server_groups_priority_order and not isinstance(server_groups_priority_order, str):
            raise TypeError("Expected argument 'server_groups_priority_order' to be a str")
        pulumi.set(__self__, "server_groups_priority_order", server_groups_priority_order)
        if tacacs_server_groups and not isinstance(tacacs_server_groups, list):
            raise TypeError("Expected argument 'tacacs_server_groups' to be a list")
        pulumi.set(__self__, "tacacs_server_groups", tacacs_server_groups)
        if template_type and not isinstance(template_type, str):
            raise TypeError("Expected argument 'template_type' to be a str")
        pulumi.set(__self__, "template_type", template_type)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="accountingRules")
    def accounting_rules(self) -> Sequence['outputs.GetCedgeAaaFeatureTemplateAccountingRuleResult']:
        """
        Configure the accounting rules
        """
        return pulumi.get(self, "accounting_rules")

    @property
    @pulumi.getter(name="authorizationConfigCommands")
    def authorization_config_commands(self) -> bool:
        """
        For configuration mode commands.
        """
        return pulumi.get(self, "authorization_config_commands")

    @property
    @pulumi.getter(name="authorizationConfigCommandsVariable")
    def authorization_config_commands_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "authorization_config_commands_variable")

    @property
    @pulumi.getter(name="authorizationConsole")
    def authorization_console(self) -> bool:
        """
        For enabling console authorization
        """
        return pulumi.get(self, "authorization_console")

    @property
    @pulumi.getter(name="authorizationConsoleVariable")
    def authorization_console_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "authorization_console_variable")

    @property
    @pulumi.getter(name="authorizationRules")
    def authorization_rules(self) -> Sequence['outputs.GetCedgeAaaFeatureTemplateAuthorizationRuleResult']:
        """
        Configure the Authorization Rules
        """
        return pulumi.get(self, "authorization_rules")

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
    @pulumi.getter(name="dot1xAccounting")
    def dot1x_accounting(self) -> bool:
        """
        Accounting configurations parameters
        """
        return pulumi.get(self, "dot1x_accounting")

    @property
    @pulumi.getter(name="dot1xAccountingVariable")
    def dot1x_accounting_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "dot1x_accounting_variable")

    @property
    @pulumi.getter(name="dot1xAuthentication")
    def dot1x_authentication(self) -> bool:
        """
        Authentication configurations parameters
        """
        return pulumi.get(self, "dot1x_authentication")

    @property
    @pulumi.getter(name="dot1xAuthenticationVariable")
    def dot1x_authentication_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "dot1x_authentication_variable")

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
    @pulumi.getter(name="radiusClients")
    def radius_clients(self) -> Sequence['outputs.GetCedgeAaaFeatureTemplateRadiusClientResult']:
        """
        Specify a RADIUS client
        """
        return pulumi.get(self, "radius_clients")

    @property
    @pulumi.getter(name="radiusDynamicAuthorAuthenticationType")
    def radius_dynamic_author_authentication_type(self) -> str:
        """
        Authentication Type
        """
        return pulumi.get(self, "radius_dynamic_author_authentication_type")

    @property
    @pulumi.getter(name="radiusDynamicAuthorAuthenticationTypeVariable")
    def radius_dynamic_author_authentication_type_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "radius_dynamic_author_authentication_type_variable")

    @property
    @pulumi.getter(name="radiusDynamicAuthorDomainStripping")
    def radius_dynamic_author_domain_stripping(self) -> str:
        """
        Domain Stripping
        """
        return pulumi.get(self, "radius_dynamic_author_domain_stripping")

    @property
    @pulumi.getter(name="radiusDynamicAuthorDomainStrippingVariable")
    def radius_dynamic_author_domain_stripping_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "radius_dynamic_author_domain_stripping_variable")

    @property
    @pulumi.getter(name="radiusDynamicAuthorPort")
    def radius_dynamic_author_port(self) -> int:
        """
        Specify Radius Dynamic Author Port
        """
        return pulumi.get(self, "radius_dynamic_author_port")

    @property
    @pulumi.getter(name="radiusDynamicAuthorPortVariable")
    def radius_dynamic_author_port_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "radius_dynamic_author_port_variable")

    @property
    @pulumi.getter(name="radiusDynamicAuthorServerKey")
    def radius_dynamic_author_server_key(self) -> str:
        """
        Specify a radius dynamic author server-key
        """
        return pulumi.get(self, "radius_dynamic_author_server_key")

    @property
    @pulumi.getter(name="radiusDynamicAuthorServerKeyVariable")
    def radius_dynamic_author_server_key_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "radius_dynamic_author_server_key_variable")

    @property
    @pulumi.getter(name="radiusServerGroups")
    def radius_server_groups(self) -> Sequence['outputs.GetCedgeAaaFeatureTemplateRadiusServerGroupResult']:
        """
        Configure the Radius serverGroup
        """
        return pulumi.get(self, "radius_server_groups")

    @property
    @pulumi.getter(name="radiusTrustsecCtsAuthorizationList")
    def radius_trustsec_cts_authorization_list(self) -> str:
        """
        CTS Authorization List
        """
        return pulumi.get(self, "radius_trustsec_cts_authorization_list")

    @property
    @pulumi.getter(name="radiusTrustsecCtsAuthorizationListVariable")
    def radius_trustsec_cts_authorization_list_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "radius_trustsec_cts_authorization_list_variable")

    @property
    @pulumi.getter(name="radiusTrustsecGroup")
    def radius_trustsec_group(self) -> str:
        """
        RADIUS trustsec group
        """
        return pulumi.get(self, "radius_trustsec_group")

    @property
    @pulumi.getter(name="serverGroupsPriorityOrder")
    def server_groups_priority_order(self) -> str:
        """
        ServerGroups priority order
        """
        return pulumi.get(self, "server_groups_priority_order")

    @property
    @pulumi.getter(name="tacacsServerGroups")
    def tacacs_server_groups(self) -> Sequence['outputs.GetCedgeAaaFeatureTemplateTacacsServerGroupResult']:
        """
        Configure the TACACS serverGroup
        """
        return pulumi.get(self, "tacacs_server_groups")

    @property
    @pulumi.getter(name="templateType")
    def template_type(self) -> str:
        """
        The template type
        """
        return pulumi.get(self, "template_type")

    @property
    @pulumi.getter
    def users(self) -> Sequence['outputs.GetCedgeAaaFeatureTemplateUserResult']:
        """
        Create local login account
        """
        return pulumi.get(self, "users")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The version of the feature template
        """
        return pulumi.get(self, "version")


class AwaitableGetCedgeAaaFeatureTemplateResult(GetCedgeAaaFeatureTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCedgeAaaFeatureTemplateResult(
            accounting_rules=self.accounting_rules,
            authorization_config_commands=self.authorization_config_commands,
            authorization_config_commands_variable=self.authorization_config_commands_variable,
            authorization_console=self.authorization_console,
            authorization_console_variable=self.authorization_console_variable,
            authorization_rules=self.authorization_rules,
            description=self.description,
            device_types=self.device_types,
            dot1x_accounting=self.dot1x_accounting,
            dot1x_accounting_variable=self.dot1x_accounting_variable,
            dot1x_authentication=self.dot1x_authentication,
            dot1x_authentication_variable=self.dot1x_authentication_variable,
            id=self.id,
            name=self.name,
            radius_clients=self.radius_clients,
            radius_dynamic_author_authentication_type=self.radius_dynamic_author_authentication_type,
            radius_dynamic_author_authentication_type_variable=self.radius_dynamic_author_authentication_type_variable,
            radius_dynamic_author_domain_stripping=self.radius_dynamic_author_domain_stripping,
            radius_dynamic_author_domain_stripping_variable=self.radius_dynamic_author_domain_stripping_variable,
            radius_dynamic_author_port=self.radius_dynamic_author_port,
            radius_dynamic_author_port_variable=self.radius_dynamic_author_port_variable,
            radius_dynamic_author_server_key=self.radius_dynamic_author_server_key,
            radius_dynamic_author_server_key_variable=self.radius_dynamic_author_server_key_variable,
            radius_server_groups=self.radius_server_groups,
            radius_trustsec_cts_authorization_list=self.radius_trustsec_cts_authorization_list,
            radius_trustsec_cts_authorization_list_variable=self.radius_trustsec_cts_authorization_list_variable,
            radius_trustsec_group=self.radius_trustsec_group,
            server_groups_priority_order=self.server_groups_priority_order,
            tacacs_server_groups=self.tacacs_server_groups,
            template_type=self.template_type,
            users=self.users,
            version=self.version)


def get_cedge_aaa_feature_template(id: Optional[str] = None,
                                   name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCedgeAaaFeatureTemplateResult:
    """
    This data source can read the cEdge AAA feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_cedge_aaa_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getCedgeAaaFeatureTemplate:getCedgeAaaFeatureTemplate', __args__, opts=opts, typ=GetCedgeAaaFeatureTemplateResult).value

    return AwaitableGetCedgeAaaFeatureTemplateResult(
        accounting_rules=pulumi.get(__ret__, 'accounting_rules'),
        authorization_config_commands=pulumi.get(__ret__, 'authorization_config_commands'),
        authorization_config_commands_variable=pulumi.get(__ret__, 'authorization_config_commands_variable'),
        authorization_console=pulumi.get(__ret__, 'authorization_console'),
        authorization_console_variable=pulumi.get(__ret__, 'authorization_console_variable'),
        authorization_rules=pulumi.get(__ret__, 'authorization_rules'),
        description=pulumi.get(__ret__, 'description'),
        device_types=pulumi.get(__ret__, 'device_types'),
        dot1x_accounting=pulumi.get(__ret__, 'dot1x_accounting'),
        dot1x_accounting_variable=pulumi.get(__ret__, 'dot1x_accounting_variable'),
        dot1x_authentication=pulumi.get(__ret__, 'dot1x_authentication'),
        dot1x_authentication_variable=pulumi.get(__ret__, 'dot1x_authentication_variable'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        radius_clients=pulumi.get(__ret__, 'radius_clients'),
        radius_dynamic_author_authentication_type=pulumi.get(__ret__, 'radius_dynamic_author_authentication_type'),
        radius_dynamic_author_authentication_type_variable=pulumi.get(__ret__, 'radius_dynamic_author_authentication_type_variable'),
        radius_dynamic_author_domain_stripping=pulumi.get(__ret__, 'radius_dynamic_author_domain_stripping'),
        radius_dynamic_author_domain_stripping_variable=pulumi.get(__ret__, 'radius_dynamic_author_domain_stripping_variable'),
        radius_dynamic_author_port=pulumi.get(__ret__, 'radius_dynamic_author_port'),
        radius_dynamic_author_port_variable=pulumi.get(__ret__, 'radius_dynamic_author_port_variable'),
        radius_dynamic_author_server_key=pulumi.get(__ret__, 'radius_dynamic_author_server_key'),
        radius_dynamic_author_server_key_variable=pulumi.get(__ret__, 'radius_dynamic_author_server_key_variable'),
        radius_server_groups=pulumi.get(__ret__, 'radius_server_groups'),
        radius_trustsec_cts_authorization_list=pulumi.get(__ret__, 'radius_trustsec_cts_authorization_list'),
        radius_trustsec_cts_authorization_list_variable=pulumi.get(__ret__, 'radius_trustsec_cts_authorization_list_variable'),
        radius_trustsec_group=pulumi.get(__ret__, 'radius_trustsec_group'),
        server_groups_priority_order=pulumi.get(__ret__, 'server_groups_priority_order'),
        tacacs_server_groups=pulumi.get(__ret__, 'tacacs_server_groups'),
        template_type=pulumi.get(__ret__, 'template_type'),
        users=pulumi.get(__ret__, 'users'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_cedge_aaa_feature_template)
def get_cedge_aaa_feature_template_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                          name: Optional[pulumi.Input[Optional[str]]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCedgeAaaFeatureTemplateResult]:
    """
    This data source can read the cEdge AAA feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_cedge_aaa_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    ...
