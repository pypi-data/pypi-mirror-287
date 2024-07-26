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
    'GetVedgeInventoryResult',
    'AwaitableGetVedgeInventoryResult',
    'get_vedge_inventory',
    'get_vedge_inventory_output',
]

@pulumi.output_type
class GetVedgeInventoryResult:
    """
    A collection of values returned by getVedgeInventory.
    """
    def __init__(__self__, devices=None, id=None):
        if devices and not isinstance(devices, list):
            raise TypeError("Expected argument 'devices' to be a list")
        pulumi.set(__self__, "devices", devices)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def devices(self) -> Sequence['outputs.GetVedgeInventoryDeviceResult']:
        """
        List of returned devices
        """
        return pulumi.get(self, "devices")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the object
        """
        return pulumi.get(self, "id")


class AwaitableGetVedgeInventoryResult(GetVedgeInventoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVedgeInventoryResult(
            devices=self.devices,
            id=self.id)


def get_vedge_inventory(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVedgeInventoryResult:
    """
    This data source can read the VEdge Inventory .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_vedge_inventory()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getVedgeInventory:getVedgeInventory', __args__, opts=opts, typ=GetVedgeInventoryResult).value

    return AwaitableGetVedgeInventoryResult(
        devices=pulumi.get(__ret__, 'devices'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_vedge_inventory)
def get_vedge_inventory_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVedgeInventoryResult]:
    """
    This data source can read the VEdge Inventory .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_vedge_inventory()
    ```
    """
    ...
