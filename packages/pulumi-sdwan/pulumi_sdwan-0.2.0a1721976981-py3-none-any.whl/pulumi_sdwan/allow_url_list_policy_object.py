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

__all__ = ['AllowUrlListPolicyObjectArgs', 'AllowUrlListPolicyObject']

@pulumi.input_type
class AllowUrlListPolicyObjectArgs:
    def __init__(__self__, *,
                 entries: pulumi.Input[Sequence[pulumi.Input['AllowUrlListPolicyObjectEntryArgs']]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AllowUrlListPolicyObject resource.
        :param pulumi.Input[Sequence[pulumi.Input['AllowUrlListPolicyObjectEntryArgs']]] entries: List of entries
        :param pulumi.Input[str] name: The name of the policy object
        """
        pulumi.set(__self__, "entries", entries)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def entries(self) -> pulumi.Input[Sequence[pulumi.Input['AllowUrlListPolicyObjectEntryArgs']]]:
        """
        List of entries
        """
        return pulumi.get(self, "entries")

    @entries.setter
    def entries(self, value: pulumi.Input[Sequence[pulumi.Input['AllowUrlListPolicyObjectEntryArgs']]]):
        pulumi.set(self, "entries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy object
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AllowUrlListPolicyObjectState:
    def __init__(__self__, *,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input['AllowUrlListPolicyObjectEntryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering AllowUrlListPolicyObject resources.
        :param pulumi.Input[Sequence[pulumi.Input['AllowUrlListPolicyObjectEntryArgs']]] entries: List of entries
        :param pulumi.Input[str] name: The name of the policy object
        :param pulumi.Input[int] version: The version of the object
        """
        if entries is not None:
            pulumi.set(__self__, "entries", entries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AllowUrlListPolicyObjectEntryArgs']]]]:
        """
        List of entries
        """
        return pulumi.get(self, "entries")

    @entries.setter
    def entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AllowUrlListPolicyObjectEntryArgs']]]]):
        pulumi.set(self, "entries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy object
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


class AllowUrlListPolicyObject(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AllowUrlListPolicyObjectEntryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource can manage a Allow URL List Policy Object .

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sdwan as sdwan

        example = sdwan.AllowUrlListPolicyObject("example",
            name="Example",
            entries=[sdwan.AllowUrlListPolicyObjectEntryArgs(
                url="cisco.com",
            )])
        ```

        ## Import

        ```sh
        $ pulumi import sdwan:index/allowUrlListPolicyObject:AllowUrlListPolicyObject example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AllowUrlListPolicyObjectEntryArgs']]]] entries: List of entries
        :param pulumi.Input[str] name: The name of the policy object
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AllowUrlListPolicyObjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage a Allow URL List Policy Object .

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sdwan as sdwan

        example = sdwan.AllowUrlListPolicyObject("example",
            name="Example",
            entries=[sdwan.AllowUrlListPolicyObjectEntryArgs(
                url="cisco.com",
            )])
        ```

        ## Import

        ```sh
        $ pulumi import sdwan:index/allowUrlListPolicyObject:AllowUrlListPolicyObject example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param AllowUrlListPolicyObjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AllowUrlListPolicyObjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AllowUrlListPolicyObjectEntryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AllowUrlListPolicyObjectArgs.__new__(AllowUrlListPolicyObjectArgs)

            if entries is None and not opts.urn:
                raise TypeError("Missing required property 'entries'")
            __props__.__dict__["entries"] = entries
            __props__.__dict__["name"] = name
            __props__.__dict__["version"] = None
        super(AllowUrlListPolicyObject, __self__).__init__(
            'sdwan:index/allowUrlListPolicyObject:AllowUrlListPolicyObject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AllowUrlListPolicyObjectEntryArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'AllowUrlListPolicyObject':
        """
        Get an existing AllowUrlListPolicyObject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AllowUrlListPolicyObjectEntryArgs']]]] entries: List of entries
        :param pulumi.Input[str] name: The name of the policy object
        :param pulumi.Input[int] version: The version of the object
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AllowUrlListPolicyObjectState.__new__(_AllowUrlListPolicyObjectState)

        __props__.__dict__["entries"] = entries
        __props__.__dict__["name"] = name
        __props__.__dict__["version"] = version
        return AllowUrlListPolicyObject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def entries(self) -> pulumi.Output[Sequence['outputs.AllowUrlListPolicyObjectEntry']]:
        """
        List of entries
        """
        return pulumi.get(self, "entries")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy object
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The version of the object
        """
        return pulumi.get(self, "version")

