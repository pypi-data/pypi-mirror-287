from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

from ..models.csscms_core_enums_claim_type import CSSCMSCoreEnumsClaimType

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionCreationRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionCreationRequest:
    """
    Attributes:
        claim_type (CSSCMSCoreEnumsClaimType):
        claim_value (str):
        provider_authentication_scheme (str):
        description (str):
    """

    claim_type: CSSCMSCoreEnumsClaimType
    claim_value: str
    provider_authentication_scheme: str
    description: str

    def to_dict(self) -> Dict[str, Any]:
        claim_type = self.claim_type.value

        claim_value = self.claim_value
        provider_authentication_scheme = self.provider_authentication_scheme
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "claimType": claim_type,
                "claimValue": claim_value,
                "providerAuthenticationScheme": provider_authentication_scheme,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        claim_type = CSSCMSCoreEnumsClaimType(d.pop("claimType"))

        claim_value = d.pop("claimValue")

        provider_authentication_scheme = d.pop("providerAuthenticationScheme")

        description = d.pop("description")

        keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_creation_request = cls(
            claim_type=claim_type,
            claim_value=claim_value,
            provider_authentication_scheme=provider_authentication_scheme,
            description=description,
        )

        return keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_creation_request
