from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsPamProviderPermissionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsPamProviderPermissionResponse:
    """
    Attributes:
        pam_provider_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        permissions (Union[Unset, None, List[str]]):
    """

    pam_provider_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    permissions: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        pam_provider_id = self.pam_provider_id
        name = self.name
        permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if pam_provider_id is not UNSET:
            field_dict["pamProviderId"] = pam_provider_id
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        pam_provider_id = d.pop("pamProviderId", UNSET)

        name = d.pop("name", UNSET)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        keyfactor_web_keyfactor_api_models_security_security_role_permissions_pam_provider_permission_response = cls(
            pam_provider_id=pam_provider_id,
            name=name,
            permissions=permissions,
        )

        return keyfactor_web_keyfactor_api_models_security_security_role_permissions_pam_provider_permission_response
