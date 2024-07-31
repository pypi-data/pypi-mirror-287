from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_provider_response import (
        KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionProviderResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionQueryResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionQueryResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        description (Union[Unset, None, str]):
        claim_type (Union[Unset, None, str]):
        claim_value (Union[Unset, None, str]):
        provider (Union[Unset,
            KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionProviderResponse]):
    """

    id: Union[Unset, int] = UNSET
    description: Union[Unset, None, str] = UNSET
    claim_type: Union[Unset, None, str] = UNSET
    claim_value: Union[Unset, None, str] = UNSET
    provider: Union[
        Unset, "KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionProviderResponse"
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        description = self.description
        claim_type = self.claim_type
        claim_value = self.claim_value
        provider: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if claim_type is not UNSET:
            field_dict["claimType"] = claim_type
        if claim_value is not UNSET:
            field_dict["claimValue"] = claim_value
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_provider_response import (
            KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionProviderResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        claim_type = d.pop("claimType", UNSET)

        claim_value = d.pop("claimValue", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[
            Unset, KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionProviderResponse
        ]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = (
                KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionProviderResponse.from_dict(
                    _provider
                )
            )

        keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_query_response = cls(
            id=id,
            description=description,
            claim_type=claim_type,
            claim_value=claim_value,
            provider=provider,
        )

        return keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_query_response
