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
    'GetClientServiceAccountUserResult',
    'AwaitableGetClientServiceAccountUserResult',
    'get_client_service_account_user',
    'get_client_service_account_user_output',
]

@pulumi.output_type
class GetClientServiceAccountUserResult:
    """
    A collection of values returned by getClientServiceAccountUser.
    """
    def __init__(__self__, attributes=None, client_id=None, email=None, email_verified=None, enabled=None, federated_identities=None, first_name=None, id=None, last_name=None, realm_id=None, required_actions=None, username=None):
        if attributes and not isinstance(attributes, dict):
            raise TypeError("Expected argument 'attributes' to be a dict")
        pulumi.set(__self__, "attributes", attributes)
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if email_verified and not isinstance(email_verified, bool):
            raise TypeError("Expected argument 'email_verified' to be a bool")
        pulumi.set(__self__, "email_verified", email_verified)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if federated_identities and not isinstance(federated_identities, list):
            raise TypeError("Expected argument 'federated_identities' to be a list")
        pulumi.set(__self__, "federated_identities", federated_identities)
        if first_name and not isinstance(first_name, str):
            raise TypeError("Expected argument 'first_name' to be a str")
        pulumi.set(__self__, "first_name", first_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_name and not isinstance(last_name, str):
            raise TypeError("Expected argument 'last_name' to be a str")
        pulumi.set(__self__, "last_name", last_name)
        if realm_id and not isinstance(realm_id, str):
            raise TypeError("Expected argument 'realm_id' to be a str")
        pulumi.set(__self__, "realm_id", realm_id)
        if required_actions and not isinstance(required_actions, list):
            raise TypeError("Expected argument 'required_actions' to be a list")
        pulumi.set(__self__, "required_actions", required_actions)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def attributes(self) -> Mapping[str, Any]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter
    def email(self) -> str:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="emailVerified")
    def email_verified(self) -> bool:
        return pulumi.get(self, "email_verified")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="federatedIdentities")
    def federated_identities(self) -> Sequence['outputs.GetClientServiceAccountUserFederatedIdentityResult']:
        return pulumi.get(self, "federated_identities")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> str:
        return pulumi.get(self, "realm_id")

    @property
    @pulumi.getter(name="requiredActions")
    def required_actions(self) -> Sequence[str]:
        return pulumi.get(self, "required_actions")

    @property
    @pulumi.getter
    def username(self) -> str:
        return pulumi.get(self, "username")


class AwaitableGetClientServiceAccountUserResult(GetClientServiceAccountUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientServiceAccountUserResult(
            attributes=self.attributes,
            client_id=self.client_id,
            email=self.email,
            email_verified=self.email_verified,
            enabled=self.enabled,
            federated_identities=self.federated_identities,
            first_name=self.first_name,
            id=self.id,
            last_name=self.last_name,
            realm_id=self.realm_id,
            required_actions=self.required_actions,
            username=self.username)


def get_client_service_account_user(client_id: Optional[str] = None,
                                    realm_id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientServiceAccountUserResult:
    """
    This data source can be used to fetch information about the service account user that is associated with an OpenID client
    that has service accounts enabled.

    ## Example Usage

    In this example, we'll create an OpenID client with service accounts enabled. This causes Keycloak to create a special user
    that represents the service account. We'll use this data source to grab this user's ID in order to assign some roles to this
    user, using the `UserRoles` resource.

    ```python
    import pulumi
    import pulumi_keycloak as keycloak

    realm = keycloak.Realm("realm",
        realm="my-realm",
        enabled=True)
    client = keycloak.openid.Client("client",
        realm_id=realm.id,
        client_id="client",
        name="client",
        access_type="CONFIDENTIAL",
        service_accounts_enabled=True)
    service_account_user = keycloak.openid.get_client_service_account_user_output(realm_id=realm.id,
        client_id=client.id)
    offline_access = keycloak.get_role_output(realm_id=realm.id,
        name="offline_access")
    service_account_user_roles = keycloak.UserRoles("service_account_user_roles",
        realm_id=realm.id,
        user_id=service_account_user.id,
        role_ids=[offline_access.id])
    ```


    :param str client_id: The ID of the OpenID client with service accounts enabled.
    :param str realm_id: The realm that the OpenID client exists within.
    """
    __args__ = dict()
    __args__['clientId'] = client_id
    __args__['realmId'] = realm_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('keycloak:openid/getClientServiceAccountUser:getClientServiceAccountUser', __args__, opts=opts, typ=GetClientServiceAccountUserResult).value

    return AwaitableGetClientServiceAccountUserResult(
        attributes=pulumi.get(__ret__, 'attributes'),
        client_id=pulumi.get(__ret__, 'client_id'),
        email=pulumi.get(__ret__, 'email'),
        email_verified=pulumi.get(__ret__, 'email_verified'),
        enabled=pulumi.get(__ret__, 'enabled'),
        federated_identities=pulumi.get(__ret__, 'federated_identities'),
        first_name=pulumi.get(__ret__, 'first_name'),
        id=pulumi.get(__ret__, 'id'),
        last_name=pulumi.get(__ret__, 'last_name'),
        realm_id=pulumi.get(__ret__, 'realm_id'),
        required_actions=pulumi.get(__ret__, 'required_actions'),
        username=pulumi.get(__ret__, 'username'))


@_utilities.lift_output_func(get_client_service_account_user)
def get_client_service_account_user_output(client_id: Optional[pulumi.Input[str]] = None,
                                           realm_id: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClientServiceAccountUserResult]:
    """
    This data source can be used to fetch information about the service account user that is associated with an OpenID client
    that has service accounts enabled.

    ## Example Usage

    In this example, we'll create an OpenID client with service accounts enabled. This causes Keycloak to create a special user
    that represents the service account. We'll use this data source to grab this user's ID in order to assign some roles to this
    user, using the `UserRoles` resource.

    ```python
    import pulumi
    import pulumi_keycloak as keycloak

    realm = keycloak.Realm("realm",
        realm="my-realm",
        enabled=True)
    client = keycloak.openid.Client("client",
        realm_id=realm.id,
        client_id="client",
        name="client",
        access_type="CONFIDENTIAL",
        service_accounts_enabled=True)
    service_account_user = keycloak.openid.get_client_service_account_user_output(realm_id=realm.id,
        client_id=client.id)
    offline_access = keycloak.get_role_output(realm_id=realm.id,
        name="offline_access")
    service_account_user_roles = keycloak.UserRoles("service_account_user_roles",
        realm_id=realm.id,
        user_id=service_account_user.id,
        role_ids=[offline_access.id])
    ```


    :param str client_id: The ID of the OpenID client with service accounts enabled.
    :param str realm_id: The realm that the OpenID client exists within.
    """
    ...
