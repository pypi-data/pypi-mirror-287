from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_global_permissions_global_permission_response import (
        KeyfactorWebKeyfactorApiModelsGlobalPermissionsGlobalPermissionResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityMyResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityMyResponse:
    """
    Attributes:
        roles (Union[Unset, None, List[str]]):
        global_permissions (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsGlobalPermissionsGlobalPermissionResponse']]):
    """

    roles: Union[Unset, None, List[str]] = UNSET
    global_permissions: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsGlobalPermissionsGlobalPermissionResponse"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        roles: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.roles, Unset):
            if self.roles is None:
                roles = None
            else:
                roles = self.roles

        global_permissions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.global_permissions, Unset):
            if self.global_permissions is None:
                global_permissions = None
            else:
                global_permissions = []
                for global_permissions_item_data in self.global_permissions:
                    global_permissions_item = global_permissions_item_data.to_dict()

                    global_permissions.append(global_permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles
        if global_permissions is not UNSET:
            field_dict["globalPermissions"] = global_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_global_permissions_global_permission_response import (
            KeyfactorWebKeyfactorApiModelsGlobalPermissionsGlobalPermissionResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        roles = cast(List[str], d.pop("roles", UNSET))

        global_permissions = []
        _global_permissions = d.pop("globalPermissions", UNSET)
        for global_permissions_item_data in _global_permissions or []:
            global_permissions_item = KeyfactorWebKeyfactorApiModelsGlobalPermissionsGlobalPermissionResponse.from_dict(
                global_permissions_item_data
            )

            global_permissions.append(global_permissions_item)

        keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_my_response = cls(
            roles=roles,
            global_permissions=global_permissions,
        )

        return keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_my_response
