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
    'GetVpnMembershipPolicyDefinitionResult',
    'AwaitableGetVpnMembershipPolicyDefinitionResult',
    'get_vpn_membership_policy_definition',
    'get_vpn_membership_policy_definition_output',
]

@pulumi.output_type
class GetVpnMembershipPolicyDefinitionResult:
    """
    A collection of values returned by getVpnMembershipPolicyDefinition.
    """
    def __init__(__self__, description=None, id=None, name=None, sites=None, type=None, version=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sites and not isinstance(sites, list):
            raise TypeError("Expected argument 'sites' to be a list")
        pulumi.set(__self__, "sites", sites)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the policy definition
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the object
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy definition
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sites(self) -> Sequence['outputs.GetVpnMembershipPolicyDefinitionSiteResult']:
        """
        List of sites
        """
        return pulumi.get(self, "sites")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The version of the object
        """
        return pulumi.get(self, "version")


class AwaitableGetVpnMembershipPolicyDefinitionResult(GetVpnMembershipPolicyDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpnMembershipPolicyDefinitionResult(
            description=self.description,
            id=self.id,
            name=self.name,
            sites=self.sites,
            type=self.type,
            version=self.version)


def get_vpn_membership_policy_definition(id: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpnMembershipPolicyDefinitionResult:
    """
    This data source can read the VPN Membership Policy Definition .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_vpn_membership_policy_definition(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the object
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getVpnMembershipPolicyDefinition:getVpnMembershipPolicyDefinition', __args__, opts=opts, typ=GetVpnMembershipPolicyDefinitionResult).value

    return AwaitableGetVpnMembershipPolicyDefinitionResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        sites=pulumi.get(__ret__, 'sites'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_vpn_membership_policy_definition)
def get_vpn_membership_policy_definition_output(id: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpnMembershipPolicyDefinitionResult]:
    """
    This data source can read the VPN Membership Policy Definition .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_vpn_membership_policy_definition(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the object
    """
    ...
