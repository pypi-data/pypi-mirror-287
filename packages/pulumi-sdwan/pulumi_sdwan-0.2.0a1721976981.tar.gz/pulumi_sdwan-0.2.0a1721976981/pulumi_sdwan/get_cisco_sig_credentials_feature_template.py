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
    'GetCiscoSigCredentialsFeatureTemplateResult',
    'AwaitableGetCiscoSigCredentialsFeatureTemplateResult',
    'get_cisco_sig_credentials_feature_template',
    'get_cisco_sig_credentials_feature_template_output',
]

@pulumi.output_type
class GetCiscoSigCredentialsFeatureTemplateResult:
    """
    A collection of values returned by getCiscoSigCredentialsFeatureTemplate.
    """
    def __init__(__self__, description=None, device_types=None, id=None, name=None, template_type=None, umbrella_api_key=None, umbrella_api_key_variable=None, umbrella_api_secret=None, umbrella_api_secret_variable=None, umbrella_organization_id=None, umbrella_organization_id_variable=None, version=None, zscaler_cloud_name=None, zscaler_cloud_name_variable=None, zscaler_organization=None, zscaler_organization_variable=None, zscaler_partner_api_key=None, zscaler_partner_api_key_variable=None, zscaler_partner_base_uri=None, zscaler_partner_base_uri_variable=None, zscaler_partner_password=None, zscaler_partner_password_variable=None, zscaler_partner_username=None, zscaler_partner_username_variable=None, zscaler_password=None, zscaler_password_variable=None, zscaler_username=None, zscaler_username_variable=None):
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
        if umbrella_api_key and not isinstance(umbrella_api_key, str):
            raise TypeError("Expected argument 'umbrella_api_key' to be a str")
        pulumi.set(__self__, "umbrella_api_key", umbrella_api_key)
        if umbrella_api_key_variable and not isinstance(umbrella_api_key_variable, str):
            raise TypeError("Expected argument 'umbrella_api_key_variable' to be a str")
        pulumi.set(__self__, "umbrella_api_key_variable", umbrella_api_key_variable)
        if umbrella_api_secret and not isinstance(umbrella_api_secret, str):
            raise TypeError("Expected argument 'umbrella_api_secret' to be a str")
        pulumi.set(__self__, "umbrella_api_secret", umbrella_api_secret)
        if umbrella_api_secret_variable and not isinstance(umbrella_api_secret_variable, str):
            raise TypeError("Expected argument 'umbrella_api_secret_variable' to be a str")
        pulumi.set(__self__, "umbrella_api_secret_variable", umbrella_api_secret_variable)
        if umbrella_organization_id and not isinstance(umbrella_organization_id, str):
            raise TypeError("Expected argument 'umbrella_organization_id' to be a str")
        pulumi.set(__self__, "umbrella_organization_id", umbrella_organization_id)
        if umbrella_organization_id_variable and not isinstance(umbrella_organization_id_variable, str):
            raise TypeError("Expected argument 'umbrella_organization_id_variable' to be a str")
        pulumi.set(__self__, "umbrella_organization_id_variable", umbrella_organization_id_variable)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)
        if zscaler_cloud_name and not isinstance(zscaler_cloud_name, int):
            raise TypeError("Expected argument 'zscaler_cloud_name' to be a int")
        pulumi.set(__self__, "zscaler_cloud_name", zscaler_cloud_name)
        if zscaler_cloud_name_variable and not isinstance(zscaler_cloud_name_variable, str):
            raise TypeError("Expected argument 'zscaler_cloud_name_variable' to be a str")
        pulumi.set(__self__, "zscaler_cloud_name_variable", zscaler_cloud_name_variable)
        if zscaler_organization and not isinstance(zscaler_organization, str):
            raise TypeError("Expected argument 'zscaler_organization' to be a str")
        pulumi.set(__self__, "zscaler_organization", zscaler_organization)
        if zscaler_organization_variable and not isinstance(zscaler_organization_variable, str):
            raise TypeError("Expected argument 'zscaler_organization_variable' to be a str")
        pulumi.set(__self__, "zscaler_organization_variable", zscaler_organization_variable)
        if zscaler_partner_api_key and not isinstance(zscaler_partner_api_key, str):
            raise TypeError("Expected argument 'zscaler_partner_api_key' to be a str")
        pulumi.set(__self__, "zscaler_partner_api_key", zscaler_partner_api_key)
        if zscaler_partner_api_key_variable and not isinstance(zscaler_partner_api_key_variable, str):
            raise TypeError("Expected argument 'zscaler_partner_api_key_variable' to be a str")
        pulumi.set(__self__, "zscaler_partner_api_key_variable", zscaler_partner_api_key_variable)
        if zscaler_partner_base_uri and not isinstance(zscaler_partner_base_uri, str):
            raise TypeError("Expected argument 'zscaler_partner_base_uri' to be a str")
        pulumi.set(__self__, "zscaler_partner_base_uri", zscaler_partner_base_uri)
        if zscaler_partner_base_uri_variable and not isinstance(zscaler_partner_base_uri_variable, str):
            raise TypeError("Expected argument 'zscaler_partner_base_uri_variable' to be a str")
        pulumi.set(__self__, "zscaler_partner_base_uri_variable", zscaler_partner_base_uri_variable)
        if zscaler_partner_password and not isinstance(zscaler_partner_password, str):
            raise TypeError("Expected argument 'zscaler_partner_password' to be a str")
        pulumi.set(__self__, "zscaler_partner_password", zscaler_partner_password)
        if zscaler_partner_password_variable and not isinstance(zscaler_partner_password_variable, str):
            raise TypeError("Expected argument 'zscaler_partner_password_variable' to be a str")
        pulumi.set(__self__, "zscaler_partner_password_variable", zscaler_partner_password_variable)
        if zscaler_partner_username and not isinstance(zscaler_partner_username, str):
            raise TypeError("Expected argument 'zscaler_partner_username' to be a str")
        pulumi.set(__self__, "zscaler_partner_username", zscaler_partner_username)
        if zscaler_partner_username_variable and not isinstance(zscaler_partner_username_variable, str):
            raise TypeError("Expected argument 'zscaler_partner_username_variable' to be a str")
        pulumi.set(__self__, "zscaler_partner_username_variable", zscaler_partner_username_variable)
        if zscaler_password and not isinstance(zscaler_password, str):
            raise TypeError("Expected argument 'zscaler_password' to be a str")
        pulumi.set(__self__, "zscaler_password", zscaler_password)
        if zscaler_password_variable and not isinstance(zscaler_password_variable, str):
            raise TypeError("Expected argument 'zscaler_password_variable' to be a str")
        pulumi.set(__self__, "zscaler_password_variable", zscaler_password_variable)
        if zscaler_username and not isinstance(zscaler_username, str):
            raise TypeError("Expected argument 'zscaler_username' to be a str")
        pulumi.set(__self__, "zscaler_username", zscaler_username)
        if zscaler_username_variable and not isinstance(zscaler_username_variable, str):
            raise TypeError("Expected argument 'zscaler_username_variable' to be a str")
        pulumi.set(__self__, "zscaler_username_variable", zscaler_username_variable)

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
    @pulumi.getter(name="umbrellaApiKey")
    def umbrella_api_key(self) -> str:
        """
        API Key
        """
        return pulumi.get(self, "umbrella_api_key")

    @property
    @pulumi.getter(name="umbrellaApiKeyVariable")
    def umbrella_api_key_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "umbrella_api_key_variable")

    @property
    @pulumi.getter(name="umbrellaApiSecret")
    def umbrella_api_secret(self) -> str:
        """
        API Secret
        """
        return pulumi.get(self, "umbrella_api_secret")

    @property
    @pulumi.getter(name="umbrellaApiSecretVariable")
    def umbrella_api_secret_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "umbrella_api_secret_variable")

    @property
    @pulumi.getter(name="umbrellaOrganizationId")
    def umbrella_organization_id(self) -> str:
        """
        Ord ID
        """
        return pulumi.get(self, "umbrella_organization_id")

    @property
    @pulumi.getter(name="umbrellaOrganizationIdVariable")
    def umbrella_organization_id_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "umbrella_organization_id_variable")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The version of the feature template
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="zscalerCloudName")
    def zscaler_cloud_name(self) -> int:
        """
        Third Party Cloud Name
        """
        return pulumi.get(self, "zscaler_cloud_name")

    @property
    @pulumi.getter(name="zscalerCloudNameVariable")
    def zscaler_cloud_name_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "zscaler_cloud_name_variable")

    @property
    @pulumi.getter(name="zscalerOrganization")
    def zscaler_organization(self) -> str:
        """
        Organization Name
        """
        return pulumi.get(self, "zscaler_organization")

    @property
    @pulumi.getter(name="zscalerOrganizationVariable")
    def zscaler_organization_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "zscaler_organization_variable")

    @property
    @pulumi.getter(name="zscalerPartnerApiKey")
    def zscaler_partner_api_key(self) -> str:
        """
        Partner API Key
        """
        return pulumi.get(self, "zscaler_partner_api_key")

    @property
    @pulumi.getter(name="zscalerPartnerApiKeyVariable")
    def zscaler_partner_api_key_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "zscaler_partner_api_key_variable")

    @property
    @pulumi.getter(name="zscalerPartnerBaseUri")
    def zscaler_partner_base_uri(self) -> str:
        """
        Partner Base URI to be used in REST calls
        """
        return pulumi.get(self, "zscaler_partner_base_uri")

    @property
    @pulumi.getter(name="zscalerPartnerBaseUriVariable")
    def zscaler_partner_base_uri_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "zscaler_partner_base_uri_variable")

    @property
    @pulumi.getter(name="zscalerPartnerPassword")
    def zscaler_partner_password(self) -> str:
        """
        Partner Password
        """
        return pulumi.get(self, "zscaler_partner_password")

    @property
    @pulumi.getter(name="zscalerPartnerPasswordVariable")
    def zscaler_partner_password_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "zscaler_partner_password_variable")

    @property
    @pulumi.getter(name="zscalerPartnerUsername")
    def zscaler_partner_username(self) -> str:
        """
        Partner User Name
        """
        return pulumi.get(self, "zscaler_partner_username")

    @property
    @pulumi.getter(name="zscalerPartnerUsernameVariable")
    def zscaler_partner_username_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "zscaler_partner_username_variable")

    @property
    @pulumi.getter(name="zscalerPassword")
    def zscaler_password(self) -> str:
        """
        Password of Zscaler partner account
        """
        return pulumi.get(self, "zscaler_password")

    @property
    @pulumi.getter(name="zscalerPasswordVariable")
    def zscaler_password_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "zscaler_password_variable")

    @property
    @pulumi.getter(name="zscalerUsername")
    def zscaler_username(self) -> str:
        """
        Username of Zscaler partner account
        """
        return pulumi.get(self, "zscaler_username")

    @property
    @pulumi.getter(name="zscalerUsernameVariable")
    def zscaler_username_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "zscaler_username_variable")


class AwaitableGetCiscoSigCredentialsFeatureTemplateResult(GetCiscoSigCredentialsFeatureTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCiscoSigCredentialsFeatureTemplateResult(
            description=self.description,
            device_types=self.device_types,
            id=self.id,
            name=self.name,
            template_type=self.template_type,
            umbrella_api_key=self.umbrella_api_key,
            umbrella_api_key_variable=self.umbrella_api_key_variable,
            umbrella_api_secret=self.umbrella_api_secret,
            umbrella_api_secret_variable=self.umbrella_api_secret_variable,
            umbrella_organization_id=self.umbrella_organization_id,
            umbrella_organization_id_variable=self.umbrella_organization_id_variable,
            version=self.version,
            zscaler_cloud_name=self.zscaler_cloud_name,
            zscaler_cloud_name_variable=self.zscaler_cloud_name_variable,
            zscaler_organization=self.zscaler_organization,
            zscaler_organization_variable=self.zscaler_organization_variable,
            zscaler_partner_api_key=self.zscaler_partner_api_key,
            zscaler_partner_api_key_variable=self.zscaler_partner_api_key_variable,
            zscaler_partner_base_uri=self.zscaler_partner_base_uri,
            zscaler_partner_base_uri_variable=self.zscaler_partner_base_uri_variable,
            zscaler_partner_password=self.zscaler_partner_password,
            zscaler_partner_password_variable=self.zscaler_partner_password_variable,
            zscaler_partner_username=self.zscaler_partner_username,
            zscaler_partner_username_variable=self.zscaler_partner_username_variable,
            zscaler_password=self.zscaler_password,
            zscaler_password_variable=self.zscaler_password_variable,
            zscaler_username=self.zscaler_username,
            zscaler_username_variable=self.zscaler_username_variable)


def get_cisco_sig_credentials_feature_template(id: Optional[str] = None,
                                               name: Optional[str] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCiscoSigCredentialsFeatureTemplateResult:
    """
    This data source can read the Cisco SIG Credentials feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_cisco_sig_credentials_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getCiscoSigCredentialsFeatureTemplate:getCiscoSigCredentialsFeatureTemplate', __args__, opts=opts, typ=GetCiscoSigCredentialsFeatureTemplateResult).value

    return AwaitableGetCiscoSigCredentialsFeatureTemplateResult(
        description=pulumi.get(__ret__, 'description'),
        device_types=pulumi.get(__ret__, 'device_types'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        template_type=pulumi.get(__ret__, 'template_type'),
        umbrella_api_key=pulumi.get(__ret__, 'umbrella_api_key'),
        umbrella_api_key_variable=pulumi.get(__ret__, 'umbrella_api_key_variable'),
        umbrella_api_secret=pulumi.get(__ret__, 'umbrella_api_secret'),
        umbrella_api_secret_variable=pulumi.get(__ret__, 'umbrella_api_secret_variable'),
        umbrella_organization_id=pulumi.get(__ret__, 'umbrella_organization_id'),
        umbrella_organization_id_variable=pulumi.get(__ret__, 'umbrella_organization_id_variable'),
        version=pulumi.get(__ret__, 'version'),
        zscaler_cloud_name=pulumi.get(__ret__, 'zscaler_cloud_name'),
        zscaler_cloud_name_variable=pulumi.get(__ret__, 'zscaler_cloud_name_variable'),
        zscaler_organization=pulumi.get(__ret__, 'zscaler_organization'),
        zscaler_organization_variable=pulumi.get(__ret__, 'zscaler_organization_variable'),
        zscaler_partner_api_key=pulumi.get(__ret__, 'zscaler_partner_api_key'),
        zscaler_partner_api_key_variable=pulumi.get(__ret__, 'zscaler_partner_api_key_variable'),
        zscaler_partner_base_uri=pulumi.get(__ret__, 'zscaler_partner_base_uri'),
        zscaler_partner_base_uri_variable=pulumi.get(__ret__, 'zscaler_partner_base_uri_variable'),
        zscaler_partner_password=pulumi.get(__ret__, 'zscaler_partner_password'),
        zscaler_partner_password_variable=pulumi.get(__ret__, 'zscaler_partner_password_variable'),
        zscaler_partner_username=pulumi.get(__ret__, 'zscaler_partner_username'),
        zscaler_partner_username_variable=pulumi.get(__ret__, 'zscaler_partner_username_variable'),
        zscaler_password=pulumi.get(__ret__, 'zscaler_password'),
        zscaler_password_variable=pulumi.get(__ret__, 'zscaler_password_variable'),
        zscaler_username=pulumi.get(__ret__, 'zscaler_username'),
        zscaler_username_variable=pulumi.get(__ret__, 'zscaler_username_variable'))


@_utilities.lift_output_func(get_cisco_sig_credentials_feature_template)
def get_cisco_sig_credentials_feature_template_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                                      name: Optional[pulumi.Input[Optional[str]]] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCiscoSigCredentialsFeatureTemplateResult]:
    """
    This data source can read the Cisco SIG Credentials feature template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_cisco_sig_credentials_feature_template(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the feature template
    :param str name: The name of the feature template
    """
    ...
