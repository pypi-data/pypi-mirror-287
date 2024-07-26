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
    'GetZoneListPolicyObjectResult',
    'AwaitableGetZoneListPolicyObjectResult',
    'get_zone_list_policy_object',
    'get_zone_list_policy_object_output',
]

@pulumi.output_type
class GetZoneListPolicyObjectResult:
    """
    A collection of values returned by getZoneListPolicyObject.
    """
    def __init__(__self__, entries=None, id=None, name=None, version=None):
        if entries and not isinstance(entries, list):
            raise TypeError("Expected argument 'entries' to be a list")
        pulumi.set(__self__, "entries", entries)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def entries(self) -> Sequence['outputs.GetZoneListPolicyObjectEntryResult']:
        """
        List of entries
        """
        return pulumi.get(self, "entries")

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
        The name of the policy object
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The version of the object
        """
        return pulumi.get(self, "version")


class AwaitableGetZoneListPolicyObjectResult(GetZoneListPolicyObjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZoneListPolicyObjectResult(
            entries=self.entries,
            id=self.id,
            name=self.name,
            version=self.version)


def get_zone_list_policy_object(id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZoneListPolicyObjectResult:
    """
    This data source can read the Zone List Policy Object .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_zone_list_policy_object(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the object
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getZoneListPolicyObject:getZoneListPolicyObject', __args__, opts=opts, typ=GetZoneListPolicyObjectResult).value

    return AwaitableGetZoneListPolicyObjectResult(
        entries=pulumi.get(__ret__, 'entries'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_zone_list_policy_object)
def get_zone_list_policy_object_output(id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZoneListPolicyObjectResult]:
    """
    This data source can read the Zone List Policy Object .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_zone_list_policy_object(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the object
    """
    ...
