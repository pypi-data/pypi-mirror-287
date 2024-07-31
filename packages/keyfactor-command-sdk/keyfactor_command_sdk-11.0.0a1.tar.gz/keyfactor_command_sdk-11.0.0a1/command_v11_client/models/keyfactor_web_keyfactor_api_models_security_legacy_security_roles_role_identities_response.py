from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        keyfactor_web_keyfactor_api_models_security_legacy_security_roles_role_identities_response = cls(
            id=id,
            name=name,
        )

        return keyfactor_web_keyfactor_api_models_security_legacy_security_roles_role_identities_response
