# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetClientScopeResult',
    'AwaitableGetClientScopeResult',
    'get_client_scope',
    'get_client_scope_output',
]

@pulumi.output_type
class GetClientScopeResult:
    """
    A collection of values returned by getClientScope.
    """
    def __init__(__self__, consent_screen_text=None, description=None, gui_order=None, id=None, include_in_token_scope=None, name=None, realm_id=None):
        if consent_screen_text and not isinstance(consent_screen_text, str):
            raise TypeError("Expected argument 'consent_screen_text' to be a str")
        pulumi.set(__self__, "consent_screen_text", consent_screen_text)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if gui_order and not isinstance(gui_order, int):
            raise TypeError("Expected argument 'gui_order' to be a int")
        pulumi.set(__self__, "gui_order", gui_order)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_in_token_scope and not isinstance(include_in_token_scope, bool):
            raise TypeError("Expected argument 'include_in_token_scope' to be a bool")
        pulumi.set(__self__, "include_in_token_scope", include_in_token_scope)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if realm_id and not isinstance(realm_id, str):
            raise TypeError("Expected argument 'realm_id' to be a str")
        pulumi.set(__self__, "realm_id", realm_id)

    @property
    @pulumi.getter(name="consentScreenText")
    def consent_screen_text(self) -> str:
        return pulumi.get(self, "consent_screen_text")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="guiOrder")
    def gui_order(self) -> int:
        return pulumi.get(self, "gui_order")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeInTokenScope")
    def include_in_token_scope(self) -> bool:
        return pulumi.get(self, "include_in_token_scope")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> str:
        return pulumi.get(self, "realm_id")


class AwaitableGetClientScopeResult(GetClientScopeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientScopeResult(
            consent_screen_text=self.consent_screen_text,
            description=self.description,
            gui_order=self.gui_order,
            id=self.id,
            include_in_token_scope=self.include_in_token_scope,
            name=self.name,
            realm_id=self.realm_id)


def get_client_scope(name: Optional[str] = None,
                     realm_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientScopeResult:
    """
    This data source can be used to fetch properties of a Keycloak OpenID client scope for usage with other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_keycloak as keycloak

    offline_access = keycloak.openid.get_client_scope(realm_id="my-realm",
        name="offline_access")
    # use the data source
    audience_mapper = keycloak.openid.AudienceProtocolMapper("audience_mapper",
        realm_id=offline_access.realm_id,
        client_scope_id=offline_access.id,
        name="audience-mapper",
        included_custom_audience="foo")
    ```


    :param str name: The name of the client scope.
    :param str realm_id: The realm id.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['realmId'] = realm_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('keycloak:openid/getClientScope:getClientScope', __args__, opts=opts, typ=GetClientScopeResult).value

    return AwaitableGetClientScopeResult(
        consent_screen_text=pulumi.get(__ret__, 'consent_screen_text'),
        description=pulumi.get(__ret__, 'description'),
        gui_order=pulumi.get(__ret__, 'gui_order'),
        id=pulumi.get(__ret__, 'id'),
        include_in_token_scope=pulumi.get(__ret__, 'include_in_token_scope'),
        name=pulumi.get(__ret__, 'name'),
        realm_id=pulumi.get(__ret__, 'realm_id'))


@_utilities.lift_output_func(get_client_scope)
def get_client_scope_output(name: Optional[pulumi.Input[str]] = None,
                            realm_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClientScopeResult]:
    """
    This data source can be used to fetch properties of a Keycloak OpenID client scope for usage with other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_keycloak as keycloak

    offline_access = keycloak.openid.get_client_scope(realm_id="my-realm",
        name="offline_access")
    # use the data source
    audience_mapper = keycloak.openid.AudienceProtocolMapper("audience_mapper",
        realm_id=offline_access.realm_id,
        client_scope_id=offline_access.id,
        name="audience-mapper",
        included_custom_audience="foo")
    ```


    :param str name: The name of the client scope.
    :param str realm_id: The realm id.
    """
    ...
