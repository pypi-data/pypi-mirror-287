from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        permission_set_id (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    permission_set_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        permission_set_id = self.permission_set_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if permission_set_id is not UNSET:
            field_dict["permissionSetId"] = permission_set_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        permission_set_id = d.pop("permissionSetId", UNSET)

        keyfactor_web_keyfactor_api_models_security_role_claim_definitions_security_role_for_claim_response = cls(
            id=id,
            name=name,
            description=description,
            permission_set_id=permission_set_id,
        )

        return keyfactor_web_keyfactor_api_models_security_role_claim_definitions_security_role_for_claim_response
