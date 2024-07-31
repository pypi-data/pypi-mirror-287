from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_role_response import (
        KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentitiesSecurityIdentityResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentitiesSecurityIdentityResponse:
    """Public DTO for handling responses that include a security identity.

    Attributes:
        id (Union[Unset, int]): The ID of the security identity.
        account_name (Union[Unset, None, str]): The username associated with the account.
        identity_type (Union[Unset, None, str]): The type of the identity.
        roles (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse']]): The roles this identity
            belongs to.
        valid (Union[Unset, None, bool]): Whether or not the identity's role XML is valid.
        sid (Union[Unset, None, str]): The security identifier for the identity.
    """

    id: Union[Unset, int] = UNSET
    account_name: Union[Unset, None, str] = UNSET
    identity_type: Union[Unset, None, str] = UNSET
    roles: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse"]
    ] = UNSET
    valid: Union[Unset, None, bool] = UNSET
    sid: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account_name = self.account_name
        identity_type = self.identity_type
        roles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            if self.roles is None:
                roles = None
            else:
                roles = []
                for roles_item_data in self.roles:
                    roles_item = roles_item_data.to_dict()

                    roles.append(roles_item)

        valid = self.valid
        sid = self.sid

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if identity_type is not UNSET:
            field_dict["identityType"] = identity_type
        if roles is not UNSET:
            field_dict["roles"] = roles
        if valid is not UNSET:
            field_dict["valid"] = valid
        if sid is not UNSET:
            field_dict["sid"] = sid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_role_response import (
            KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        account_name = d.pop("accountName", UNSET)

        identity_type = d.pop("identityType", UNSET)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse.from_dict(
                roles_item_data
            )

            roles.append(roles_item)

        valid = d.pop("valid", UNSET)

        sid = d.pop("sid", UNSET)

        keyfactor_web_keyfactor_api_models_security_security_identities_security_identity_response = cls(
            id=id,
            account_name=account_name,
            identity_type=identity_type,
            roles=roles,
            valid=valid,
            sid=sid,
        )

        return keyfactor_web_keyfactor_api_models_security_security_identities_security_identity_response
