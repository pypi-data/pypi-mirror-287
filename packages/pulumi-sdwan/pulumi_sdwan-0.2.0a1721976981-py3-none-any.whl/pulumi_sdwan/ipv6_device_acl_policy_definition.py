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

__all__ = ['Ipv6DeviceAclPolicyDefinitionArgs', 'Ipv6DeviceAclPolicyDefinition']

@pulumi.input_type
class Ipv6DeviceAclPolicyDefinitionArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 sequences: pulumi.Input[Sequence[pulumi.Input['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]],
                 default_action: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Ipv6DeviceAclPolicyDefinition resource.
        :param pulumi.Input[str] description: The description of the policy definition
        :param pulumi.Input[Sequence[pulumi.Input['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]] sequences: List of ACL sequences
        :param pulumi.Input[str] default_action: Default action, either `accept` or `drop` - Choices: `accept`, `drop`
        :param pulumi.Input[str] name: The name of the policy definition
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "sequences", sequences)
        if default_action is not None:
            pulumi.set(__self__, "default_action", default_action)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the policy definition
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def sequences(self) -> pulumi.Input[Sequence[pulumi.Input['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]:
        """
        List of ACL sequences
        """
        return pulumi.get(self, "sequences")

    @sequences.setter
    def sequences(self, value: pulumi.Input[Sequence[pulumi.Input['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]):
        pulumi.set(self, "sequences", value)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[str]]:
        """
        Default action, either `accept` or `drop` - Choices: `accept`, `drop`
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy definition
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _Ipv6DeviceAclPolicyDefinitionState:
    def __init__(__self__, *,
                 default_action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sequences: Optional[pulumi.Input[Sequence[pulumi.Input['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Ipv6DeviceAclPolicyDefinition resources.
        :param pulumi.Input[str] default_action: Default action, either `accept` or `drop` - Choices: `accept`, `drop`
        :param pulumi.Input[str] description: The description of the policy definition
        :param pulumi.Input[str] name: The name of the policy definition
        :param pulumi.Input[Sequence[pulumi.Input['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]] sequences: List of ACL sequences
        :param pulumi.Input[str] type: Type
        :param pulumi.Input[int] version: The version of the object
        """
        if default_action is not None:
            pulumi.set(__self__, "default_action", default_action)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sequences is not None:
            pulumi.set(__self__, "sequences", sequences)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[str]]:
        """
        Default action, either `accept` or `drop` - Choices: `accept`, `drop`
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy definition
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy definition
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def sequences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]]:
        """
        List of ACL sequences
        """
        return pulumi.get(self, "sequences")

    @sequences.setter
    def sequences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]]):
        pulumi.set(self, "sequences", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

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


class Ipv6DeviceAclPolicyDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sequences: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]]] = None,
                 __props__=None):
        """
        This resource can manage a IPv6 Device ACL Policy Definition .

        ## Import

        ```sh
        $ pulumi import sdwan:index/ipv6DeviceAclPolicyDefinition:Ipv6DeviceAclPolicyDefinition example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_action: Default action, either `accept` or `drop` - Choices: `accept`, `drop`
        :param pulumi.Input[str] description: The description of the policy definition
        :param pulumi.Input[str] name: The name of the policy definition
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]] sequences: List of ACL sequences
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Ipv6DeviceAclPolicyDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage a IPv6 Device ACL Policy Definition .

        ## Import

        ```sh
        $ pulumi import sdwan:index/ipv6DeviceAclPolicyDefinition:Ipv6DeviceAclPolicyDefinition example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param Ipv6DeviceAclPolicyDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(Ipv6DeviceAclPolicyDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_action: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sequences: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = Ipv6DeviceAclPolicyDefinitionArgs.__new__(Ipv6DeviceAclPolicyDefinitionArgs)

            __props__.__dict__["default_action"] = default_action
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if sequences is None and not opts.urn:
                raise TypeError("Missing required property 'sequences'")
            __props__.__dict__["sequences"] = sequences
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        super(Ipv6DeviceAclPolicyDefinition, __self__).__init__(
            'sdwan:index/ipv6DeviceAclPolicyDefinition:Ipv6DeviceAclPolicyDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_action: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sequences: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'Ipv6DeviceAclPolicyDefinition':
        """
        Get an existing Ipv6DeviceAclPolicyDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_action: Default action, either `accept` or `drop` - Choices: `accept`, `drop`
        :param pulumi.Input[str] description: The description of the policy definition
        :param pulumi.Input[str] name: The name of the policy definition
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['Ipv6DeviceAclPolicyDefinitionSequenceArgs']]]] sequences: List of ACL sequences
        :param pulumi.Input[str] type: Type
        :param pulumi.Input[int] version: The version of the object
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _Ipv6DeviceAclPolicyDefinitionState.__new__(_Ipv6DeviceAclPolicyDefinitionState)

        __props__.__dict__["default_action"] = default_action
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["sequences"] = sequences
        __props__.__dict__["type"] = type
        __props__.__dict__["version"] = version
        return Ipv6DeviceAclPolicyDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Output[Optional[str]]:
        """
        Default action, either `accept` or `drop` - Choices: `accept`, `drop`
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the policy definition
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy definition
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sequences(self) -> pulumi.Output[Sequence['outputs.Ipv6DeviceAclPolicyDefinitionSequence']]:
        """
        List of ACL sequences
        """
        return pulumi.get(self, "sequences")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The version of the object
        """
        return pulumi.get(self, "version")

