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
    'GetUrlFilteringPolicyDefinitionResult',
    'AwaitableGetUrlFilteringPolicyDefinitionResult',
    'get_url_filtering_policy_definition',
    'get_url_filtering_policy_definition_output',
]

@pulumi.output_type
class GetUrlFilteringPolicyDefinitionResult:
    """
    A collection of values returned by getUrlFilteringPolicyDefinition.
    """
    def __init__(__self__, alerts=None, allow_url_list_id=None, allow_url_list_version=None, block_page_action=None, block_page_contents=None, block_url_list_id=None, block_url_list_version=None, description=None, id=None, mode=None, name=None, target_vpns=None, version=None, web_categories=None, web_categories_action=None, web_reputation=None):
        if alerts and not isinstance(alerts, list):
            raise TypeError("Expected argument 'alerts' to be a list")
        pulumi.set(__self__, "alerts", alerts)
        if allow_url_list_id and not isinstance(allow_url_list_id, str):
            raise TypeError("Expected argument 'allow_url_list_id' to be a str")
        pulumi.set(__self__, "allow_url_list_id", allow_url_list_id)
        if allow_url_list_version and not isinstance(allow_url_list_version, int):
            raise TypeError("Expected argument 'allow_url_list_version' to be a int")
        pulumi.set(__self__, "allow_url_list_version", allow_url_list_version)
        if block_page_action and not isinstance(block_page_action, str):
            raise TypeError("Expected argument 'block_page_action' to be a str")
        pulumi.set(__self__, "block_page_action", block_page_action)
        if block_page_contents and not isinstance(block_page_contents, str):
            raise TypeError("Expected argument 'block_page_contents' to be a str")
        pulumi.set(__self__, "block_page_contents", block_page_contents)
        if block_url_list_id and not isinstance(block_url_list_id, str):
            raise TypeError("Expected argument 'block_url_list_id' to be a str")
        pulumi.set(__self__, "block_url_list_id", block_url_list_id)
        if block_url_list_version and not isinstance(block_url_list_version, int):
            raise TypeError("Expected argument 'block_url_list_version' to be a int")
        pulumi.set(__self__, "block_url_list_version", block_url_list_version)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if target_vpns and not isinstance(target_vpns, list):
            raise TypeError("Expected argument 'target_vpns' to be a list")
        pulumi.set(__self__, "target_vpns", target_vpns)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)
        if web_categories and not isinstance(web_categories, list):
            raise TypeError("Expected argument 'web_categories' to be a list")
        pulumi.set(__self__, "web_categories", web_categories)
        if web_categories_action and not isinstance(web_categories_action, str):
            raise TypeError("Expected argument 'web_categories_action' to be a str")
        pulumi.set(__self__, "web_categories_action", web_categories_action)
        if web_reputation and not isinstance(web_reputation, str):
            raise TypeError("Expected argument 'web_reputation' to be a str")
        pulumi.set(__self__, "web_reputation", web_reputation)

    @property
    @pulumi.getter
    def alerts(self) -> Sequence[str]:
        """
        List of alerts options that will be exported as syslog messages
        """
        return pulumi.get(self, "alerts")

    @property
    @pulumi.getter(name="allowUrlListId")
    def allow_url_list_id(self) -> str:
        """
        Allow URL list ID
        """
        return pulumi.get(self, "allow_url_list_id")

    @property
    @pulumi.getter(name="allowUrlListVersion")
    def allow_url_list_version(self) -> int:
        """
        Allow URL list version
        """
        return pulumi.get(self, "allow_url_list_version")

    @property
    @pulumi.getter(name="blockPageAction")
    def block_page_action(self) -> str:
        """
        Redirect to a URL or display a message when a blocked page is accessed.
        """
        return pulumi.get(self, "block_page_action")

    @property
    @pulumi.getter(name="blockPageContents")
    def block_page_contents(self) -> str:
        """
        The message displayed or URL redirected to when a blocked page is accessed.
        """
        return pulumi.get(self, "block_page_contents")

    @property
    @pulumi.getter(name="blockUrlListId")
    def block_url_list_id(self) -> str:
        """
        Block URL list ID
        """
        return pulumi.get(self, "block_url_list_id")

    @property
    @pulumi.getter(name="blockUrlListVersion")
    def block_url_list_version(self) -> int:
        """
        Block URL list version
        """
        return pulumi.get(self, "block_url_list_version")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the policy definition.
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
    def mode(self) -> str:
        """
        The policy mode
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy definition.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="targetVpns")
    def target_vpns(self) -> Sequence[str]:
        """
        List of VPN IDs
        """
        return pulumi.get(self, "target_vpns")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The version of the object
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="webCategories")
    def web_categories(self) -> Sequence[str]:
        """
        List of categories to block or allow
        """
        return pulumi.get(self, "web_categories")

    @property
    @pulumi.getter(name="webCategoriesAction")
    def web_categories_action(self) -> str:
        """
        whether the selected web categories should be blocked or allowed.
        """
        return pulumi.get(self, "web_categories_action")

    @property
    @pulumi.getter(name="webReputation")
    def web_reputation(self) -> str:
        """
        The web reputation of the policy definition
        """
        return pulumi.get(self, "web_reputation")


class AwaitableGetUrlFilteringPolicyDefinitionResult(GetUrlFilteringPolicyDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUrlFilteringPolicyDefinitionResult(
            alerts=self.alerts,
            allow_url_list_id=self.allow_url_list_id,
            allow_url_list_version=self.allow_url_list_version,
            block_page_action=self.block_page_action,
            block_page_contents=self.block_page_contents,
            block_url_list_id=self.block_url_list_id,
            block_url_list_version=self.block_url_list_version,
            description=self.description,
            id=self.id,
            mode=self.mode,
            name=self.name,
            target_vpns=self.target_vpns,
            version=self.version,
            web_categories=self.web_categories,
            web_categories_action=self.web_categories_action,
            web_reputation=self.web_reputation)


def get_url_filtering_policy_definition(id: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUrlFilteringPolicyDefinitionResult:
    """
    This data source can read the URL Filtering Policy Definition .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_url_filtering_policy_definition(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the object
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getUrlFilteringPolicyDefinition:getUrlFilteringPolicyDefinition', __args__, opts=opts, typ=GetUrlFilteringPolicyDefinitionResult).value

    return AwaitableGetUrlFilteringPolicyDefinitionResult(
        alerts=pulumi.get(__ret__, 'alerts'),
        allow_url_list_id=pulumi.get(__ret__, 'allow_url_list_id'),
        allow_url_list_version=pulumi.get(__ret__, 'allow_url_list_version'),
        block_page_action=pulumi.get(__ret__, 'block_page_action'),
        block_page_contents=pulumi.get(__ret__, 'block_page_contents'),
        block_url_list_id=pulumi.get(__ret__, 'block_url_list_id'),
        block_url_list_version=pulumi.get(__ret__, 'block_url_list_version'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        mode=pulumi.get(__ret__, 'mode'),
        name=pulumi.get(__ret__, 'name'),
        target_vpns=pulumi.get(__ret__, 'target_vpns'),
        version=pulumi.get(__ret__, 'version'),
        web_categories=pulumi.get(__ret__, 'web_categories'),
        web_categories_action=pulumi.get(__ret__, 'web_categories_action'),
        web_reputation=pulumi.get(__ret__, 'web_reputation'))


@_utilities.lift_output_func(get_url_filtering_policy_definition)
def get_url_filtering_policy_definition_output(id: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUrlFilteringPolicyDefinitionResult]:
    """
    This data source can read the URL Filtering Policy Definition .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_url_filtering_policy_definition(id="f6b2c44c-693c-4763-b010-895aa3d236bd")
    ```


    :param str id: The id of the object
    """
    ...
