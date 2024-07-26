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
    'GetRoutePolicyDefinitionResult',
    'AwaitableGetRoutePolicyDefinitionResult',
    'get_route_policy_definition',
    'get_route_policy_definition_output',
]

@pulumi.output_type
class GetRoutePolicyDefinitionResult:
    """
    A collection of values returned by getRoutePolicyDefinition.
    """
    def __init__(__self__, default_action=None, description=None, id=None, name=None, sequences=None, type=None, version=None):
        if default_action and not isinstance(default_action, str):
            raise TypeError("Expected argument 'default_action' to be a str")
        pulumi.set(__self__, "default_action", default_action)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sequences and not isinstance(sequences, list):
            raise TypeError("Expected argument 'sequences' to be a list")
        pulumi.set(__self__, "sequences", sequences)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> str:
        """
        Default action, either `accept` or `reject`
        """
        return pulumi.get(self, "default_action")

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
    def sequences(self) -> Sequence['outputs.GetRoutePolicyDefinitionSequenceResult']:
        """
        List of ACL sequences
        """
        return pulumi.get(self, "sequences")

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


class AwaitableGetRoutePolicyDefinitionResult(GetRoutePolicyDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoutePolicyDefinitionResult(
            default_action=self.default_action,
            description=self.description,
            id=self.id,
            name=self.name,
            sequences=self.sequences,
            type=self.type,
            version=self.version)


def get_route_policy_definition(id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoutePolicyDefinitionResult:
    """
    This data source can read the Route Policy Definition .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_route_policy_definition(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the object
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getRoutePolicyDefinition:getRoutePolicyDefinition', __args__, opts=opts, typ=GetRoutePolicyDefinitionResult).value

    return AwaitableGetRoutePolicyDefinitionResult(
        default_action=pulumi.get(__ret__, 'default_action'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        sequences=pulumi.get(__ret__, 'sequences'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_route_policy_definition)
def get_route_policy_definition_output(id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoutePolicyDefinitionResult]:
    """
    This data source can read the Route Policy Definition .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_route_policy_definition(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the object
    """
    ...
