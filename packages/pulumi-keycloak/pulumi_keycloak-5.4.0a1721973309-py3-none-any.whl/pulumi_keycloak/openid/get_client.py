# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetClientResult',
    'AwaitableGetClientResult',
    'get_client',
    'get_client_output',
]

@pulumi.output_type
class GetClientResult:
    """
    A collection of values returned by getClient.
    """
    def __init__(__self__, access_token_lifespan=None, access_type=None, admin_url=None, authentication_flow_binding_overrides=None, authorizations=None, backchannel_logout_revoke_offline_sessions=None, backchannel_logout_session_required=None, backchannel_logout_url=None, base_url=None, client_authenticator_type=None, client_id=None, client_offline_session_idle_timeout=None, client_offline_session_max_lifespan=None, client_secret=None, client_session_idle_timeout=None, client_session_max_lifespan=None, consent_required=None, consent_screen_text=None, description=None, direct_access_grants_enabled=None, display_on_consent_screen=None, enabled=None, exclude_session_state_from_auth_response=None, extra_config=None, frontchannel_logout_enabled=None, frontchannel_logout_url=None, full_scope_allowed=None, id=None, implicit_flow_enabled=None, login_theme=None, name=None, oauth2_device_authorization_grant_enabled=None, oauth2_device_code_lifespan=None, oauth2_device_polling_interval=None, pkce_code_challenge_method=None, realm_id=None, resource_server_id=None, root_url=None, service_account_user_id=None, service_accounts_enabled=None, standard_flow_enabled=None, use_refresh_tokens=None, use_refresh_tokens_client_credentials=None, valid_post_logout_redirect_uris=None, valid_redirect_uris=None, web_origins=None):
        if access_token_lifespan and not isinstance(access_token_lifespan, str):
            raise TypeError("Expected argument 'access_token_lifespan' to be a str")
        pulumi.set(__self__, "access_token_lifespan", access_token_lifespan)
        if access_type and not isinstance(access_type, str):
            raise TypeError("Expected argument 'access_type' to be a str")
        pulumi.set(__self__, "access_type", access_type)
        if admin_url and not isinstance(admin_url, str):
            raise TypeError("Expected argument 'admin_url' to be a str")
        pulumi.set(__self__, "admin_url", admin_url)
        if authentication_flow_binding_overrides and not isinstance(authentication_flow_binding_overrides, list):
            raise TypeError("Expected argument 'authentication_flow_binding_overrides' to be a list")
        pulumi.set(__self__, "authentication_flow_binding_overrides", authentication_flow_binding_overrides)
        if authorizations and not isinstance(authorizations, list):
            raise TypeError("Expected argument 'authorizations' to be a list")
        pulumi.set(__self__, "authorizations", authorizations)
        if backchannel_logout_revoke_offline_sessions and not isinstance(backchannel_logout_revoke_offline_sessions, bool):
            raise TypeError("Expected argument 'backchannel_logout_revoke_offline_sessions' to be a bool")
        pulumi.set(__self__, "backchannel_logout_revoke_offline_sessions", backchannel_logout_revoke_offline_sessions)
        if backchannel_logout_session_required and not isinstance(backchannel_logout_session_required, bool):
            raise TypeError("Expected argument 'backchannel_logout_session_required' to be a bool")
        pulumi.set(__self__, "backchannel_logout_session_required", backchannel_logout_session_required)
        if backchannel_logout_url and not isinstance(backchannel_logout_url, str):
            raise TypeError("Expected argument 'backchannel_logout_url' to be a str")
        pulumi.set(__self__, "backchannel_logout_url", backchannel_logout_url)
        if base_url and not isinstance(base_url, str):
            raise TypeError("Expected argument 'base_url' to be a str")
        pulumi.set(__self__, "base_url", base_url)
        if client_authenticator_type and not isinstance(client_authenticator_type, str):
            raise TypeError("Expected argument 'client_authenticator_type' to be a str")
        pulumi.set(__self__, "client_authenticator_type", client_authenticator_type)
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if client_offline_session_idle_timeout and not isinstance(client_offline_session_idle_timeout, str):
            raise TypeError("Expected argument 'client_offline_session_idle_timeout' to be a str")
        pulumi.set(__self__, "client_offline_session_idle_timeout", client_offline_session_idle_timeout)
        if client_offline_session_max_lifespan and not isinstance(client_offline_session_max_lifespan, str):
            raise TypeError("Expected argument 'client_offline_session_max_lifespan' to be a str")
        pulumi.set(__self__, "client_offline_session_max_lifespan", client_offline_session_max_lifespan)
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)
        if client_session_idle_timeout and not isinstance(client_session_idle_timeout, str):
            raise TypeError("Expected argument 'client_session_idle_timeout' to be a str")
        pulumi.set(__self__, "client_session_idle_timeout", client_session_idle_timeout)
        if client_session_max_lifespan and not isinstance(client_session_max_lifespan, str):
            raise TypeError("Expected argument 'client_session_max_lifespan' to be a str")
        pulumi.set(__self__, "client_session_max_lifespan", client_session_max_lifespan)
        if consent_required and not isinstance(consent_required, bool):
            raise TypeError("Expected argument 'consent_required' to be a bool")
        pulumi.set(__self__, "consent_required", consent_required)
        if consent_screen_text and not isinstance(consent_screen_text, str):
            raise TypeError("Expected argument 'consent_screen_text' to be a str")
        pulumi.set(__self__, "consent_screen_text", consent_screen_text)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if direct_access_grants_enabled and not isinstance(direct_access_grants_enabled, bool):
            raise TypeError("Expected argument 'direct_access_grants_enabled' to be a bool")
        pulumi.set(__self__, "direct_access_grants_enabled", direct_access_grants_enabled)
        if display_on_consent_screen and not isinstance(display_on_consent_screen, bool):
            raise TypeError("Expected argument 'display_on_consent_screen' to be a bool")
        pulumi.set(__self__, "display_on_consent_screen", display_on_consent_screen)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if exclude_session_state_from_auth_response and not isinstance(exclude_session_state_from_auth_response, bool):
            raise TypeError("Expected argument 'exclude_session_state_from_auth_response' to be a bool")
        pulumi.set(__self__, "exclude_session_state_from_auth_response", exclude_session_state_from_auth_response)
        if extra_config and not isinstance(extra_config, dict):
            raise TypeError("Expected argument 'extra_config' to be a dict")
        pulumi.set(__self__, "extra_config", extra_config)
        if frontchannel_logout_enabled and not isinstance(frontchannel_logout_enabled, bool):
            raise TypeError("Expected argument 'frontchannel_logout_enabled' to be a bool")
        pulumi.set(__self__, "frontchannel_logout_enabled", frontchannel_logout_enabled)
        if frontchannel_logout_url and not isinstance(frontchannel_logout_url, str):
            raise TypeError("Expected argument 'frontchannel_logout_url' to be a str")
        pulumi.set(__self__, "frontchannel_logout_url", frontchannel_logout_url)
        if full_scope_allowed and not isinstance(full_scope_allowed, bool):
            raise TypeError("Expected argument 'full_scope_allowed' to be a bool")
        pulumi.set(__self__, "full_scope_allowed", full_scope_allowed)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if implicit_flow_enabled and not isinstance(implicit_flow_enabled, bool):
            raise TypeError("Expected argument 'implicit_flow_enabled' to be a bool")
        pulumi.set(__self__, "implicit_flow_enabled", implicit_flow_enabled)
        if login_theme and not isinstance(login_theme, str):
            raise TypeError("Expected argument 'login_theme' to be a str")
        pulumi.set(__self__, "login_theme", login_theme)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if oauth2_device_authorization_grant_enabled and not isinstance(oauth2_device_authorization_grant_enabled, bool):
            raise TypeError("Expected argument 'oauth2_device_authorization_grant_enabled' to be a bool")
        pulumi.set(__self__, "oauth2_device_authorization_grant_enabled", oauth2_device_authorization_grant_enabled)
        if oauth2_device_code_lifespan and not isinstance(oauth2_device_code_lifespan, str):
            raise TypeError("Expected argument 'oauth2_device_code_lifespan' to be a str")
        pulumi.set(__self__, "oauth2_device_code_lifespan", oauth2_device_code_lifespan)
        if oauth2_device_polling_interval and not isinstance(oauth2_device_polling_interval, str):
            raise TypeError("Expected argument 'oauth2_device_polling_interval' to be a str")
        pulumi.set(__self__, "oauth2_device_polling_interval", oauth2_device_polling_interval)
        if pkce_code_challenge_method and not isinstance(pkce_code_challenge_method, str):
            raise TypeError("Expected argument 'pkce_code_challenge_method' to be a str")
        pulumi.set(__self__, "pkce_code_challenge_method", pkce_code_challenge_method)
        if realm_id and not isinstance(realm_id, str):
            raise TypeError("Expected argument 'realm_id' to be a str")
        pulumi.set(__self__, "realm_id", realm_id)
        if resource_server_id and not isinstance(resource_server_id, str):
            raise TypeError("Expected argument 'resource_server_id' to be a str")
        pulumi.set(__self__, "resource_server_id", resource_server_id)
        if root_url and not isinstance(root_url, str):
            raise TypeError("Expected argument 'root_url' to be a str")
        pulumi.set(__self__, "root_url", root_url)
        if service_account_user_id and not isinstance(service_account_user_id, str):
            raise TypeError("Expected argument 'service_account_user_id' to be a str")
        pulumi.set(__self__, "service_account_user_id", service_account_user_id)
        if service_accounts_enabled and not isinstance(service_accounts_enabled, bool):
            raise TypeError("Expected argument 'service_accounts_enabled' to be a bool")
        pulumi.set(__self__, "service_accounts_enabled", service_accounts_enabled)
        if standard_flow_enabled and not isinstance(standard_flow_enabled, bool):
            raise TypeError("Expected argument 'standard_flow_enabled' to be a bool")
        pulumi.set(__self__, "standard_flow_enabled", standard_flow_enabled)
        if use_refresh_tokens and not isinstance(use_refresh_tokens, bool):
            raise TypeError("Expected argument 'use_refresh_tokens' to be a bool")
        pulumi.set(__self__, "use_refresh_tokens", use_refresh_tokens)
        if use_refresh_tokens_client_credentials and not isinstance(use_refresh_tokens_client_credentials, bool):
            raise TypeError("Expected argument 'use_refresh_tokens_client_credentials' to be a bool")
        pulumi.set(__self__, "use_refresh_tokens_client_credentials", use_refresh_tokens_client_credentials)
        if valid_post_logout_redirect_uris and not isinstance(valid_post_logout_redirect_uris, list):
            raise TypeError("Expected argument 'valid_post_logout_redirect_uris' to be a list")
        pulumi.set(__self__, "valid_post_logout_redirect_uris", valid_post_logout_redirect_uris)
        if valid_redirect_uris and not isinstance(valid_redirect_uris, list):
            raise TypeError("Expected argument 'valid_redirect_uris' to be a list")
        pulumi.set(__self__, "valid_redirect_uris", valid_redirect_uris)
        if web_origins and not isinstance(web_origins, list):
            raise TypeError("Expected argument 'web_origins' to be a list")
        pulumi.set(__self__, "web_origins", web_origins)

    @property
    @pulumi.getter(name="accessTokenLifespan")
    def access_token_lifespan(self) -> str:
        return pulumi.get(self, "access_token_lifespan")

    @property
    @pulumi.getter(name="accessType")
    def access_type(self) -> str:
        return pulumi.get(self, "access_type")

    @property
    @pulumi.getter(name="adminUrl")
    def admin_url(self) -> str:
        return pulumi.get(self, "admin_url")

    @property
    @pulumi.getter(name="authenticationFlowBindingOverrides")
    def authentication_flow_binding_overrides(self) -> Sequence['outputs.GetClientAuthenticationFlowBindingOverrideResult']:
        return pulumi.get(self, "authentication_flow_binding_overrides")

    @property
    @pulumi.getter
    def authorizations(self) -> Sequence['outputs.GetClientAuthorizationResult']:
        return pulumi.get(self, "authorizations")

    @property
    @pulumi.getter(name="backchannelLogoutRevokeOfflineSessions")
    def backchannel_logout_revoke_offline_sessions(self) -> bool:
        return pulumi.get(self, "backchannel_logout_revoke_offline_sessions")

    @property
    @pulumi.getter(name="backchannelLogoutSessionRequired")
    def backchannel_logout_session_required(self) -> bool:
        return pulumi.get(self, "backchannel_logout_session_required")

    @property
    @pulumi.getter(name="backchannelLogoutUrl")
    def backchannel_logout_url(self) -> str:
        return pulumi.get(self, "backchannel_logout_url")

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> str:
        return pulumi.get(self, "base_url")

    @property
    @pulumi.getter(name="clientAuthenticatorType")
    def client_authenticator_type(self) -> str:
        return pulumi.get(self, "client_authenticator_type")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientOfflineSessionIdleTimeout")
    def client_offline_session_idle_timeout(self) -> str:
        return pulumi.get(self, "client_offline_session_idle_timeout")

    @property
    @pulumi.getter(name="clientOfflineSessionMaxLifespan")
    def client_offline_session_max_lifespan(self) -> str:
        return pulumi.get(self, "client_offline_session_max_lifespan")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> str:
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="clientSessionIdleTimeout")
    def client_session_idle_timeout(self) -> str:
        return pulumi.get(self, "client_session_idle_timeout")

    @property
    @pulumi.getter(name="clientSessionMaxLifespan")
    def client_session_max_lifespan(self) -> str:
        return pulumi.get(self, "client_session_max_lifespan")

    @property
    @pulumi.getter(name="consentRequired")
    def consent_required(self) -> bool:
        return pulumi.get(self, "consent_required")

    @property
    @pulumi.getter(name="consentScreenText")
    def consent_screen_text(self) -> Optional[str]:
        return pulumi.get(self, "consent_screen_text")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="directAccessGrantsEnabled")
    def direct_access_grants_enabled(self) -> bool:
        return pulumi.get(self, "direct_access_grants_enabled")

    @property
    @pulumi.getter(name="displayOnConsentScreen")
    def display_on_consent_screen(self) -> Optional[bool]:
        return pulumi.get(self, "display_on_consent_screen")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="excludeSessionStateFromAuthResponse")
    def exclude_session_state_from_auth_response(self) -> bool:
        return pulumi.get(self, "exclude_session_state_from_auth_response")

    @property
    @pulumi.getter(name="extraConfig")
    def extra_config(self) -> Mapping[str, Any]:
        return pulumi.get(self, "extra_config")

    @property
    @pulumi.getter(name="frontchannelLogoutEnabled")
    def frontchannel_logout_enabled(self) -> bool:
        return pulumi.get(self, "frontchannel_logout_enabled")

    @property
    @pulumi.getter(name="frontchannelLogoutUrl")
    def frontchannel_logout_url(self) -> str:
        return pulumi.get(self, "frontchannel_logout_url")

    @property
    @pulumi.getter(name="fullScopeAllowed")
    def full_scope_allowed(self) -> bool:
        return pulumi.get(self, "full_scope_allowed")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="implicitFlowEnabled")
    def implicit_flow_enabled(self) -> bool:
        return pulumi.get(self, "implicit_flow_enabled")

    @property
    @pulumi.getter(name="loginTheme")
    def login_theme(self) -> str:
        return pulumi.get(self, "login_theme")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oauth2DeviceAuthorizationGrantEnabled")
    def oauth2_device_authorization_grant_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "oauth2_device_authorization_grant_enabled")

    @property
    @pulumi.getter(name="oauth2DeviceCodeLifespan")
    def oauth2_device_code_lifespan(self) -> Optional[str]:
        return pulumi.get(self, "oauth2_device_code_lifespan")

    @property
    @pulumi.getter(name="oauth2DevicePollingInterval")
    def oauth2_device_polling_interval(self) -> Optional[str]:
        return pulumi.get(self, "oauth2_device_polling_interval")

    @property
    @pulumi.getter(name="pkceCodeChallengeMethod")
    def pkce_code_challenge_method(self) -> str:
        return pulumi.get(self, "pkce_code_challenge_method")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> str:
        return pulumi.get(self, "realm_id")

    @property
    @pulumi.getter(name="resourceServerId")
    def resource_server_id(self) -> str:
        return pulumi.get(self, "resource_server_id")

    @property
    @pulumi.getter(name="rootUrl")
    def root_url(self) -> str:
        return pulumi.get(self, "root_url")

    @property
    @pulumi.getter(name="serviceAccountUserId")
    def service_account_user_id(self) -> str:
        return pulumi.get(self, "service_account_user_id")

    @property
    @pulumi.getter(name="serviceAccountsEnabled")
    def service_accounts_enabled(self) -> bool:
        return pulumi.get(self, "service_accounts_enabled")

    @property
    @pulumi.getter(name="standardFlowEnabled")
    def standard_flow_enabled(self) -> bool:
        return pulumi.get(self, "standard_flow_enabled")

    @property
    @pulumi.getter(name="useRefreshTokens")
    def use_refresh_tokens(self) -> bool:
        return pulumi.get(self, "use_refresh_tokens")

    @property
    @pulumi.getter(name="useRefreshTokensClientCredentials")
    def use_refresh_tokens_client_credentials(self) -> bool:
        return pulumi.get(self, "use_refresh_tokens_client_credentials")

    @property
    @pulumi.getter(name="validPostLogoutRedirectUris")
    def valid_post_logout_redirect_uris(self) -> Sequence[str]:
        return pulumi.get(self, "valid_post_logout_redirect_uris")

    @property
    @pulumi.getter(name="validRedirectUris")
    def valid_redirect_uris(self) -> Sequence[str]:
        return pulumi.get(self, "valid_redirect_uris")

    @property
    @pulumi.getter(name="webOrigins")
    def web_origins(self) -> Sequence[str]:
        return pulumi.get(self, "web_origins")


class AwaitableGetClientResult(GetClientResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientResult(
            access_token_lifespan=self.access_token_lifespan,
            access_type=self.access_type,
            admin_url=self.admin_url,
            authentication_flow_binding_overrides=self.authentication_flow_binding_overrides,
            authorizations=self.authorizations,
            backchannel_logout_revoke_offline_sessions=self.backchannel_logout_revoke_offline_sessions,
            backchannel_logout_session_required=self.backchannel_logout_session_required,
            backchannel_logout_url=self.backchannel_logout_url,
            base_url=self.base_url,
            client_authenticator_type=self.client_authenticator_type,
            client_id=self.client_id,
            client_offline_session_idle_timeout=self.client_offline_session_idle_timeout,
            client_offline_session_max_lifespan=self.client_offline_session_max_lifespan,
            client_secret=self.client_secret,
            client_session_idle_timeout=self.client_session_idle_timeout,
            client_session_max_lifespan=self.client_session_max_lifespan,
            consent_required=self.consent_required,
            consent_screen_text=self.consent_screen_text,
            description=self.description,
            direct_access_grants_enabled=self.direct_access_grants_enabled,
            display_on_consent_screen=self.display_on_consent_screen,
            enabled=self.enabled,
            exclude_session_state_from_auth_response=self.exclude_session_state_from_auth_response,
            extra_config=self.extra_config,
            frontchannel_logout_enabled=self.frontchannel_logout_enabled,
            frontchannel_logout_url=self.frontchannel_logout_url,
            full_scope_allowed=self.full_scope_allowed,
            id=self.id,
            implicit_flow_enabled=self.implicit_flow_enabled,
            login_theme=self.login_theme,
            name=self.name,
            oauth2_device_authorization_grant_enabled=self.oauth2_device_authorization_grant_enabled,
            oauth2_device_code_lifespan=self.oauth2_device_code_lifespan,
            oauth2_device_polling_interval=self.oauth2_device_polling_interval,
            pkce_code_challenge_method=self.pkce_code_challenge_method,
            realm_id=self.realm_id,
            resource_server_id=self.resource_server_id,
            root_url=self.root_url,
            service_account_user_id=self.service_account_user_id,
            service_accounts_enabled=self.service_accounts_enabled,
            standard_flow_enabled=self.standard_flow_enabled,
            use_refresh_tokens=self.use_refresh_tokens,
            use_refresh_tokens_client_credentials=self.use_refresh_tokens_client_credentials,
            valid_post_logout_redirect_uris=self.valid_post_logout_redirect_uris,
            valid_redirect_uris=self.valid_redirect_uris,
            web_origins=self.web_origins)


def get_client(client_id: Optional[str] = None,
               consent_screen_text: Optional[str] = None,
               display_on_consent_screen: Optional[bool] = None,
               extra_config: Optional[Mapping[str, Any]] = None,
               oauth2_device_authorization_grant_enabled: Optional[bool] = None,
               oauth2_device_code_lifespan: Optional[str] = None,
               oauth2_device_polling_interval: Optional[str] = None,
               realm_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientResult:
    """
    ## # openid.Client data source

    This data source can be used to fetch properties of a Keycloak OpenID client for usage with other resources.

    ### Example Usage

    ```python
    import pulumi
    import pulumi_keycloak as keycloak

    realm_management = keycloak.openid.get_client(realm_id="my-realm",
        client_id="realm-management")
    # use the data source
    admin = keycloak.get_role(realm_id="my-realm",
        client_id=realm_management.id,
        name="realm-admin")
    ```

    ### Argument Reference

    The following arguments are supported:

    - `realm_id` - (Required) The realm id.
    - `client_id` - (Required) The client id.

    ### Attributes Reference

    See the docs for the `openid.Client` resource for details on the exported attributes.
    """
    __args__ = dict()
    __args__['clientId'] = client_id
    __args__['consentScreenText'] = consent_screen_text
    __args__['displayOnConsentScreen'] = display_on_consent_screen
    __args__['extraConfig'] = extra_config
    __args__['oauth2DeviceAuthorizationGrantEnabled'] = oauth2_device_authorization_grant_enabled
    __args__['oauth2DeviceCodeLifespan'] = oauth2_device_code_lifespan
    __args__['oauth2DevicePollingInterval'] = oauth2_device_polling_interval
    __args__['realmId'] = realm_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('keycloak:openid/getClient:getClient', __args__, opts=opts, typ=GetClientResult).value

    return AwaitableGetClientResult(
        access_token_lifespan=pulumi.get(__ret__, 'access_token_lifespan'),
        access_type=pulumi.get(__ret__, 'access_type'),
        admin_url=pulumi.get(__ret__, 'admin_url'),
        authentication_flow_binding_overrides=pulumi.get(__ret__, 'authentication_flow_binding_overrides'),
        authorizations=pulumi.get(__ret__, 'authorizations'),
        backchannel_logout_revoke_offline_sessions=pulumi.get(__ret__, 'backchannel_logout_revoke_offline_sessions'),
        backchannel_logout_session_required=pulumi.get(__ret__, 'backchannel_logout_session_required'),
        backchannel_logout_url=pulumi.get(__ret__, 'backchannel_logout_url'),
        base_url=pulumi.get(__ret__, 'base_url'),
        client_authenticator_type=pulumi.get(__ret__, 'client_authenticator_type'),
        client_id=pulumi.get(__ret__, 'client_id'),
        client_offline_session_idle_timeout=pulumi.get(__ret__, 'client_offline_session_idle_timeout'),
        client_offline_session_max_lifespan=pulumi.get(__ret__, 'client_offline_session_max_lifespan'),
        client_secret=pulumi.get(__ret__, 'client_secret'),
        client_session_idle_timeout=pulumi.get(__ret__, 'client_session_idle_timeout'),
        client_session_max_lifespan=pulumi.get(__ret__, 'client_session_max_lifespan'),
        consent_required=pulumi.get(__ret__, 'consent_required'),
        consent_screen_text=pulumi.get(__ret__, 'consent_screen_text'),
        description=pulumi.get(__ret__, 'description'),
        direct_access_grants_enabled=pulumi.get(__ret__, 'direct_access_grants_enabled'),
        display_on_consent_screen=pulumi.get(__ret__, 'display_on_consent_screen'),
        enabled=pulumi.get(__ret__, 'enabled'),
        exclude_session_state_from_auth_response=pulumi.get(__ret__, 'exclude_session_state_from_auth_response'),
        extra_config=pulumi.get(__ret__, 'extra_config'),
        frontchannel_logout_enabled=pulumi.get(__ret__, 'frontchannel_logout_enabled'),
        frontchannel_logout_url=pulumi.get(__ret__, 'frontchannel_logout_url'),
        full_scope_allowed=pulumi.get(__ret__, 'full_scope_allowed'),
        id=pulumi.get(__ret__, 'id'),
        implicit_flow_enabled=pulumi.get(__ret__, 'implicit_flow_enabled'),
        login_theme=pulumi.get(__ret__, 'login_theme'),
        name=pulumi.get(__ret__, 'name'),
        oauth2_device_authorization_grant_enabled=pulumi.get(__ret__, 'oauth2_device_authorization_grant_enabled'),
        oauth2_device_code_lifespan=pulumi.get(__ret__, 'oauth2_device_code_lifespan'),
        oauth2_device_polling_interval=pulumi.get(__ret__, 'oauth2_device_polling_interval'),
        pkce_code_challenge_method=pulumi.get(__ret__, 'pkce_code_challenge_method'),
        realm_id=pulumi.get(__ret__, 'realm_id'),
        resource_server_id=pulumi.get(__ret__, 'resource_server_id'),
        root_url=pulumi.get(__ret__, 'root_url'),
        service_account_user_id=pulumi.get(__ret__, 'service_account_user_id'),
        service_accounts_enabled=pulumi.get(__ret__, 'service_accounts_enabled'),
        standard_flow_enabled=pulumi.get(__ret__, 'standard_flow_enabled'),
        use_refresh_tokens=pulumi.get(__ret__, 'use_refresh_tokens'),
        use_refresh_tokens_client_credentials=pulumi.get(__ret__, 'use_refresh_tokens_client_credentials'),
        valid_post_logout_redirect_uris=pulumi.get(__ret__, 'valid_post_logout_redirect_uris'),
        valid_redirect_uris=pulumi.get(__ret__, 'valid_redirect_uris'),
        web_origins=pulumi.get(__ret__, 'web_origins'))


@_utilities.lift_output_func(get_client)
def get_client_output(client_id: Optional[pulumi.Input[str]] = None,
                      consent_screen_text: Optional[pulumi.Input[Optional[str]]] = None,
                      display_on_consent_screen: Optional[pulumi.Input[Optional[bool]]] = None,
                      extra_config: Optional[pulumi.Input[Optional[Mapping[str, Any]]]] = None,
                      oauth2_device_authorization_grant_enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                      oauth2_device_code_lifespan: Optional[pulumi.Input[Optional[str]]] = None,
                      oauth2_device_polling_interval: Optional[pulumi.Input[Optional[str]]] = None,
                      realm_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClientResult]:
    """
    ## # openid.Client data source

    This data source can be used to fetch properties of a Keycloak OpenID client for usage with other resources.

    ### Example Usage

    ```python
    import pulumi
    import pulumi_keycloak as keycloak

    realm_management = keycloak.openid.get_client(realm_id="my-realm",
        client_id="realm-management")
    # use the data source
    admin = keycloak.get_role(realm_id="my-realm",
        client_id=realm_management.id,
        name="realm-admin")
    ```

    ### Argument Reference

    The following arguments are supported:

    - `realm_id` - (Required) The realm id.
    - `client_id` - (Required) The client id.

    ### Attributes Reference

    See the docs for the `openid.Client` resource for details on the exported attributes.
    """
    ...
