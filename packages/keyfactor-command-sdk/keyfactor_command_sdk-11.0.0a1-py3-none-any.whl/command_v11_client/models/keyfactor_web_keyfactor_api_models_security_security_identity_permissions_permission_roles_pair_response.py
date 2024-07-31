from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse:
    """
    Attributes:
        permission (Union[Unset, None, str]):
        granted_by_roles (Union[Unset, None, List[str]]):
    """

    permission: Union[Unset, None, str] = UNSET
    granted_by_roles: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        permission = self.permission
        granted_by_roles: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.granted_by_roles, Unset):
            if self.granted_by_roles is None:
                granted_by_roles = None
            else:
                granted_by_roles = self.granted_by_roles

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission
        if granted_by_roles is not UNSET:
            field_dict["grantedByRoles"] = granted_by_roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        permission = d.pop("permission", UNSET)

        granted_by_roles = cast(List[str], d.pop("grantedByRoles", UNSET))

        keyfactor_web_keyfactor_api_models_security_security_identity_permissions_permission_roles_pair_response = cls(
            permission=permission,
            granted_by_roles=granted_by_roles,
        )

        return keyfactor_web_keyfactor_api_models_security_security_identity_permissions_permission_roles_pair_response
