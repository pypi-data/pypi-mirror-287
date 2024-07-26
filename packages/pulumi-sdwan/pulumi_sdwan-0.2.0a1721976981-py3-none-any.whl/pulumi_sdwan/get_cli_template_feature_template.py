# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetCliTemplateFeatureTemplateResult',
    'AwaitableGetCliTemplateFeatureTemplateResult',
    'get_cli_template_feature_template',
    'get_cli_template_feature_template_output',
]

@pulumi.output_type
class GetCliTemplateFeatureTemplateResult:
    """
    A collection of values returned by getCliTemplateFeatureTemplate.
    """
    def __init__(__self__, cli_config=None, description=None, device_types=None, id=None, name=None, template_type=None, version=None):
        if cli_config and not isinstance(cli_config, str):
            raise TypeError("Expected argument 'cli_config' to be a str")
        pulumi.set(__self__, "cli_config", cli_config)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if device_types and not isinstance(device_types, list):
            raise TypeError("Expected argument 'device_types' to be a list")
        pulumi.set(__self__, "device_types", device_types)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if template_type and not isinstance(template_type, str):
            raise TypeError("Expected argument 'template_type' to be a str")
        pulumi.set(__self__, "template_type", template_type)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="cliConfig")
    def cli_config(self) -> str:
        """
        Cli config
        """
        return pulumi.get(self, "cli_config")

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
    @pulumi.getter(name="templateType")
    def template_type(self) -> str:
        """
        The template type
        """
        return pulumi.get(self, "template_type")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The version of the feature template
        """
        return pulumi.get(self, "version")


class AwaitableGetCliTemplateFeatureTemplateResult(GetCliTemplateFeatureTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCliTemplateFeatureTemplateResult(
            cli_config=self.cli_config,
            description=self.description,
            device_types=self.device_types,
            id=self.id,
            name=self.name,
            template_type=self.template_type,
            version=self.version)


def get_cli_template_feature_template(id: Optional[str] = None,
                                      name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCliTemplateFeatureTemplateResult:
    """
    This data source can read the CLI Template feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_cli_template_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getCliTemplateFeatureTemplate:getCliTemplateFeatureTemplate', __args__, opts=opts, typ=GetCliTemplateFeatureTemplateResult).value

    return AwaitableGetCliTemplateFeatureTemplateResult(
        cli_config=pulumi.get(__ret__, 'cli_config'),
        description=pulumi.get(__ret__, 'description'),
        device_types=pulumi.get(__ret__, 'device_types'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        template_type=pulumi.get(__ret__, 'template_type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_cli_template_feature_template)
def get_cli_template_feature_template_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                             name: Optional[pulumi.Input[Optional[str]]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCliTemplateFeatureTemplateResult]:
    """
    This data source can read the CLI Template feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_cli_template_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    ...
