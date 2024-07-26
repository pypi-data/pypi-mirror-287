# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SystemMrfProfileParcelArgs', 'SystemMrfProfileParcel']

@pulumi.input_type
class SystemMrfProfileParcelArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_migration_to_mrf: Optional[pulumi.Input[str]] = None,
                 feature_profile_id: Optional[pulumi.Input[str]] = None,
                 migration_bgp_community: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region_id: Optional[pulumi.Input[int]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 role_variable: Optional[pulumi.Input[str]] = None,
                 secondary_region_id: Optional[pulumi.Input[int]] = None,
                 secondary_region_id_variable: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SystemMrfProfileParcel resource.
        :param pulumi.Input[str] description: The description of the profile parcel
        :param pulumi.Input[str] enable_migration_to_mrf: Enable migration mode to Multi-Region Fabric - Choices: `enabled`, `enabled-from-bgp-core`
        :param pulumi.Input[str] feature_profile_id: Feature Profile ID
        :param pulumi.Input[int] migration_bgp_community: Set BGP community during migration from BGP-core based network - Range: `1`-`4294967295`
        :param pulumi.Input[str] name: The name of the profile parcel
        :param pulumi.Input[int] region_id: Set region ID - Range: `1`-`63`
        :param pulumi.Input[str] role: Set the role for router - Choices: `edge-router`, `border-router`
        :param pulumi.Input[str] role_variable: Variable name
        :param pulumi.Input[int] secondary_region_id: Set secondary region ID - Range: `1`-`63`
        :param pulumi.Input[str] secondary_region_id_variable: Variable name
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_migration_to_mrf is not None:
            pulumi.set(__self__, "enable_migration_to_mrf", enable_migration_to_mrf)
        if feature_profile_id is not None:
            pulumi.set(__self__, "feature_profile_id", feature_profile_id)
        if migration_bgp_community is not None:
            pulumi.set(__self__, "migration_bgp_community", migration_bgp_community)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region_id is not None:
            pulumi.set(__self__, "region_id", region_id)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if role_variable is not None:
            pulumi.set(__self__, "role_variable", role_variable)
        if secondary_region_id is not None:
            pulumi.set(__self__, "secondary_region_id", secondary_region_id)
        if secondary_region_id_variable is not None:
            pulumi.set(__self__, "secondary_region_id_variable", secondary_region_id_variable)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the profile parcel
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableMigrationToMrf")
    def enable_migration_to_mrf(self) -> Optional[pulumi.Input[str]]:
        """
        Enable migration mode to Multi-Region Fabric - Choices: `enabled`, `enabled-from-bgp-core`
        """
        return pulumi.get(self, "enable_migration_to_mrf")

    @enable_migration_to_mrf.setter
    def enable_migration_to_mrf(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enable_migration_to_mrf", value)

    @property
    @pulumi.getter(name="featureProfileId")
    def feature_profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        Feature Profile ID
        """
        return pulumi.get(self, "feature_profile_id")

    @feature_profile_id.setter
    def feature_profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "feature_profile_id", value)

    @property
    @pulumi.getter(name="migrationBgpCommunity")
    def migration_bgp_community(self) -> Optional[pulumi.Input[int]]:
        """
        Set BGP community during migration from BGP-core based network - Range: `1`-`4294967295`
        """
        return pulumi.get(self, "migration_bgp_community")

    @migration_bgp_community.setter
    def migration_bgp_community(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "migration_bgp_community", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the profile parcel
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> Optional[pulumi.Input[int]]:
        """
        Set region ID - Range: `1`-`63`
        """
        return pulumi.get(self, "region_id")

    @region_id.setter
    def region_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "region_id", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        Set the role for router - Choices: `edge-router`, `border-router`
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="roleVariable")
    def role_variable(self) -> Optional[pulumi.Input[str]]:
        """
        Variable name
        """
        return pulumi.get(self, "role_variable")

    @role_variable.setter
    def role_variable(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_variable", value)

    @property
    @pulumi.getter(name="secondaryRegionId")
    def secondary_region_id(self) -> Optional[pulumi.Input[int]]:
        """
        Set secondary region ID - Range: `1`-`63`
        """
        return pulumi.get(self, "secondary_region_id")

    @secondary_region_id.setter
    def secondary_region_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "secondary_region_id", value)

    @property
    @pulumi.getter(name="secondaryRegionIdVariable")
    def secondary_region_id_variable(self) -> Optional[pulumi.Input[str]]:
        """
        Variable name
        """
        return pulumi.get(self, "secondary_region_id_variable")

    @secondary_region_id_variable.setter
    def secondary_region_id_variable(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_region_id_variable", value)


@pulumi.input_type
class _SystemMrfProfileParcelState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_migration_to_mrf: Optional[pulumi.Input[str]] = None,
                 feature_profile_id: Optional[pulumi.Input[str]] = None,
                 migration_bgp_community: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region_id: Optional[pulumi.Input[int]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 role_variable: Optional[pulumi.Input[str]] = None,
                 secondary_region_id: Optional[pulumi.Input[int]] = None,
                 secondary_region_id_variable: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering SystemMrfProfileParcel resources.
        :param pulumi.Input[str] description: The description of the profile parcel
        :param pulumi.Input[str] enable_migration_to_mrf: Enable migration mode to Multi-Region Fabric - Choices: `enabled`, `enabled-from-bgp-core`
        :param pulumi.Input[str] feature_profile_id: Feature Profile ID
        :param pulumi.Input[int] migration_bgp_community: Set BGP community during migration from BGP-core based network - Range: `1`-`4294967295`
        :param pulumi.Input[str] name: The name of the profile parcel
        :param pulumi.Input[int] region_id: Set region ID - Range: `1`-`63`
        :param pulumi.Input[str] role: Set the role for router - Choices: `edge-router`, `border-router`
        :param pulumi.Input[str] role_variable: Variable name
        :param pulumi.Input[int] secondary_region_id: Set secondary region ID - Range: `1`-`63`
        :param pulumi.Input[str] secondary_region_id_variable: Variable name
        :param pulumi.Input[int] version: The version of the profile parcel
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_migration_to_mrf is not None:
            pulumi.set(__self__, "enable_migration_to_mrf", enable_migration_to_mrf)
        if feature_profile_id is not None:
            pulumi.set(__self__, "feature_profile_id", feature_profile_id)
        if migration_bgp_community is not None:
            pulumi.set(__self__, "migration_bgp_community", migration_bgp_community)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region_id is not None:
            pulumi.set(__self__, "region_id", region_id)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if role_variable is not None:
            pulumi.set(__self__, "role_variable", role_variable)
        if secondary_region_id is not None:
            pulumi.set(__self__, "secondary_region_id", secondary_region_id)
        if secondary_region_id_variable is not None:
            pulumi.set(__self__, "secondary_region_id_variable", secondary_region_id_variable)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the profile parcel
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableMigrationToMrf")
    def enable_migration_to_mrf(self) -> Optional[pulumi.Input[str]]:
        """
        Enable migration mode to Multi-Region Fabric - Choices: `enabled`, `enabled-from-bgp-core`
        """
        return pulumi.get(self, "enable_migration_to_mrf")

    @enable_migration_to_mrf.setter
    def enable_migration_to_mrf(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enable_migration_to_mrf", value)

    @property
    @pulumi.getter(name="featureProfileId")
    def feature_profile_id(self) -> Optional[pulumi.Input[str]]:
        """
        Feature Profile ID
        """
        return pulumi.get(self, "feature_profile_id")

    @feature_profile_id.setter
    def feature_profile_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "feature_profile_id", value)

    @property
    @pulumi.getter(name="migrationBgpCommunity")
    def migration_bgp_community(self) -> Optional[pulumi.Input[int]]:
        """
        Set BGP community during migration from BGP-core based network - Range: `1`-`4294967295`
        """
        return pulumi.get(self, "migration_bgp_community")

    @migration_bgp_community.setter
    def migration_bgp_community(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "migration_bgp_community", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the profile parcel
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> Optional[pulumi.Input[int]]:
        """
        Set region ID - Range: `1`-`63`
        """
        return pulumi.get(self, "region_id")

    @region_id.setter
    def region_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "region_id", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        Set the role for router - Choices: `edge-router`, `border-router`
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="roleVariable")
    def role_variable(self) -> Optional[pulumi.Input[str]]:
        """
        Variable name
        """
        return pulumi.get(self, "role_variable")

    @role_variable.setter
    def role_variable(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_variable", value)

    @property
    @pulumi.getter(name="secondaryRegionId")
    def secondary_region_id(self) -> Optional[pulumi.Input[int]]:
        """
        Set secondary region ID - Range: `1`-`63`
        """
        return pulumi.get(self, "secondary_region_id")

    @secondary_region_id.setter
    def secondary_region_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "secondary_region_id", value)

    @property
    @pulumi.getter(name="secondaryRegionIdVariable")
    def secondary_region_id_variable(self) -> Optional[pulumi.Input[str]]:
        """
        Variable name
        """
        return pulumi.get(self, "secondary_region_id_variable")

    @secondary_region_id_variable.setter
    def secondary_region_id_variable(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_region_id_variable", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        The version of the profile parcel
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class SystemMrfProfileParcel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_migration_to_mrf: Optional[pulumi.Input[str]] = None,
                 feature_profile_id: Optional[pulumi.Input[str]] = None,
                 migration_bgp_community: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region_id: Optional[pulumi.Input[int]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 role_variable: Optional[pulumi.Input[str]] = None,
                 secondary_region_id: Optional[pulumi.Input[int]] = None,
                 secondary_region_id_variable: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource can manage a System MRF profile parcel.
          - Minimum SD-WAN Manager version: `20.12.0`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sdwan as sdwan

        example = sdwan.SystemMrfProfileParcel("example",
            name="Example",
            description="My Example",
            feature_profile_id="f6dd22c8-0b4f-496c-9a0b-6813d1f8b8ac",
            region_id=1,
            secondary_region_id=2,
            role="edge-router",
            enable_migration_to_mrf="enabled",
            migration_bgp_community=100)
        ```

        ## Import

        ```sh
        $ pulumi import sdwan:index/systemMrfProfileParcel:SystemMrfProfileParcel example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the profile parcel
        :param pulumi.Input[str] enable_migration_to_mrf: Enable migration mode to Multi-Region Fabric - Choices: `enabled`, `enabled-from-bgp-core`
        :param pulumi.Input[str] feature_profile_id: Feature Profile ID
        :param pulumi.Input[int] migration_bgp_community: Set BGP community during migration from BGP-core based network - Range: `1`-`4294967295`
        :param pulumi.Input[str] name: The name of the profile parcel
        :param pulumi.Input[int] region_id: Set region ID - Range: `1`-`63`
        :param pulumi.Input[str] role: Set the role for router - Choices: `edge-router`, `border-router`
        :param pulumi.Input[str] role_variable: Variable name
        :param pulumi.Input[int] secondary_region_id: Set secondary region ID - Range: `1`-`63`
        :param pulumi.Input[str] secondary_region_id_variable: Variable name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SystemMrfProfileParcelArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage a System MRF profile parcel.
          - Minimum SD-WAN Manager version: `20.12.0`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sdwan as sdwan

        example = sdwan.SystemMrfProfileParcel("example",
            name="Example",
            description="My Example",
            feature_profile_id="f6dd22c8-0b4f-496c-9a0b-6813d1f8b8ac",
            region_id=1,
            secondary_region_id=2,
            role="edge-router",
            enable_migration_to_mrf="enabled",
            migration_bgp_community=100)
        ```

        ## Import

        ```sh
        $ pulumi import sdwan:index/systemMrfProfileParcel:SystemMrfProfileParcel example "f6b2c44c-693c-4763-b010-895aa3d236bd"
        ```

        :param str resource_name: The name of the resource.
        :param SystemMrfProfileParcelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SystemMrfProfileParcelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_migration_to_mrf: Optional[pulumi.Input[str]] = None,
                 feature_profile_id: Optional[pulumi.Input[str]] = None,
                 migration_bgp_community: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region_id: Optional[pulumi.Input[int]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 role_variable: Optional[pulumi.Input[str]] = None,
                 secondary_region_id: Optional[pulumi.Input[int]] = None,
                 secondary_region_id_variable: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SystemMrfProfileParcelArgs.__new__(SystemMrfProfileParcelArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["enable_migration_to_mrf"] = enable_migration_to_mrf
            __props__.__dict__["feature_profile_id"] = feature_profile_id
            __props__.__dict__["migration_bgp_community"] = migration_bgp_community
            __props__.__dict__["name"] = name
            __props__.__dict__["region_id"] = region_id
            __props__.__dict__["role"] = role
            __props__.__dict__["role_variable"] = role_variable
            __props__.__dict__["secondary_region_id"] = secondary_region_id
            __props__.__dict__["secondary_region_id_variable"] = secondary_region_id_variable
            __props__.__dict__["version"] = None
        super(SystemMrfProfileParcel, __self__).__init__(
            'sdwan:index/systemMrfProfileParcel:SystemMrfProfileParcel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            enable_migration_to_mrf: Optional[pulumi.Input[str]] = None,
            feature_profile_id: Optional[pulumi.Input[str]] = None,
            migration_bgp_community: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region_id: Optional[pulumi.Input[int]] = None,
            role: Optional[pulumi.Input[str]] = None,
            role_variable: Optional[pulumi.Input[str]] = None,
            secondary_region_id: Optional[pulumi.Input[int]] = None,
            secondary_region_id_variable: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'SystemMrfProfileParcel':
        """
        Get an existing SystemMrfProfileParcel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the profile parcel
        :param pulumi.Input[str] enable_migration_to_mrf: Enable migration mode to Multi-Region Fabric - Choices: `enabled`, `enabled-from-bgp-core`
        :param pulumi.Input[str] feature_profile_id: Feature Profile ID
        :param pulumi.Input[int] migration_bgp_community: Set BGP community during migration from BGP-core based network - Range: `1`-`4294967295`
        :param pulumi.Input[str] name: The name of the profile parcel
        :param pulumi.Input[int] region_id: Set region ID - Range: `1`-`63`
        :param pulumi.Input[str] role: Set the role for router - Choices: `edge-router`, `border-router`
        :param pulumi.Input[str] role_variable: Variable name
        :param pulumi.Input[int] secondary_region_id: Set secondary region ID - Range: `1`-`63`
        :param pulumi.Input[str] secondary_region_id_variable: Variable name
        :param pulumi.Input[int] version: The version of the profile parcel
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SystemMrfProfileParcelState.__new__(_SystemMrfProfileParcelState)

        __props__.__dict__["description"] = description
        __props__.__dict__["enable_migration_to_mrf"] = enable_migration_to_mrf
        __props__.__dict__["feature_profile_id"] = feature_profile_id
        __props__.__dict__["migration_bgp_community"] = migration_bgp_community
        __props__.__dict__["name"] = name
        __props__.__dict__["region_id"] = region_id
        __props__.__dict__["role"] = role
        __props__.__dict__["role_variable"] = role_variable
        __props__.__dict__["secondary_region_id"] = secondary_region_id
        __props__.__dict__["secondary_region_id_variable"] = secondary_region_id_variable
        __props__.__dict__["version"] = version
        return SystemMrfProfileParcel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the profile parcel
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableMigrationToMrf")
    def enable_migration_to_mrf(self) -> pulumi.Output[Optional[str]]:
        """
        Enable migration mode to Multi-Region Fabric - Choices: `enabled`, `enabled-from-bgp-core`
        """
        return pulumi.get(self, "enable_migration_to_mrf")

    @property
    @pulumi.getter(name="featureProfileId")
    def feature_profile_id(self) -> pulumi.Output[Optional[str]]:
        """
        Feature Profile ID
        """
        return pulumi.get(self, "feature_profile_id")

    @property
    @pulumi.getter(name="migrationBgpCommunity")
    def migration_bgp_community(self) -> pulumi.Output[Optional[int]]:
        """
        Set BGP community during migration from BGP-core based network - Range: `1`-`4294967295`
        """
        return pulumi.get(self, "migration_bgp_community")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the profile parcel
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> pulumi.Output[Optional[int]]:
        """
        Set region ID - Range: `1`-`63`
        """
        return pulumi.get(self, "region_id")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[str]]:
        """
        Set the role for router - Choices: `edge-router`, `border-router`
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="roleVariable")
    def role_variable(self) -> pulumi.Output[Optional[str]]:
        """
        Variable name
        """
        return pulumi.get(self, "role_variable")

    @property
    @pulumi.getter(name="secondaryRegionId")
    def secondary_region_id(self) -> pulumi.Output[Optional[int]]:
        """
        Set secondary region ID - Range: `1`-`63`
        """
        return pulumi.get(self, "secondary_region_id")

    @property
    @pulumi.getter(name="secondaryRegionIdVariable")
    def secondary_region_id_variable(self) -> pulumi.Output[Optional[str]]:
        """
        Variable name
        """
        return pulumi.get(self, "secondary_region_id_variable")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        The version of the profile parcel
        """
        return pulumi.get(self, "version")

