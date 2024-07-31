from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionUpdateRequest:
    """
    Attributes:
        id (int):
        description (str):
    """

    id: int
    description: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        description = d.pop("description")

        keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_update_request = cls(
            id=id,
            description=description,
        )

        return keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_update_request
