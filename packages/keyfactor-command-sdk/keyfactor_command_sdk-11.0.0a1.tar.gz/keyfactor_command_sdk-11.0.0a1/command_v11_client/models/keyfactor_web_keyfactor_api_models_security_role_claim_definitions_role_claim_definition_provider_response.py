from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionProviderResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionProviderResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        authentication_scheme (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
    """

    id: Union[Unset, str] = UNSET
    authentication_scheme: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        authentication_scheme = self.authentication_scheme
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if authentication_scheme is not UNSET:
            field_dict["authenticationScheme"] = authentication_scheme
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        authentication_scheme = d.pop("authenticationScheme", UNSET)

        display_name = d.pop("displayName", UNSET)

        keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_provider_response = (
            cls(
                id=id,
                authentication_scheme=authentication_scheme,
                display_name=display_name,
            )
        )

        return (
            keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_provider_response
        )
