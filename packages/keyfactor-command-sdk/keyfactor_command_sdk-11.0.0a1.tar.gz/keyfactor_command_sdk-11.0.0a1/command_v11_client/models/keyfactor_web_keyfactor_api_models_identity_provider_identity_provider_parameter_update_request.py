from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderParameterUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderParameterUpdateRequest:
    """
    Attributes:
        oidc_audience (Union[Unset, None, str]):
        name_claim_type (Union[Unset, None, str]):
        role_claim_type (Union[Unset, None, str]):
        unique_claim_type (Union[Unset, None, str]):
        fallback_unique_claim_type (Union[Unset, None, str]):
        client_id (Union[Unset, None, str]):
        client_secret (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        timeout (Union[Unset, None, str]):
    """

    oidc_audience: Union[Unset, None, str] = UNSET
    name_claim_type: Union[Unset, None, str] = UNSET
    role_claim_type: Union[Unset, None, str] = UNSET
    unique_claim_type: Union[Unset, None, str] = UNSET
    fallback_unique_claim_type: Union[Unset, None, str] = UNSET
    client_id: Union[Unset, None, str] = UNSET
    client_secret: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    timeout: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        oidc_audience = self.oidc_audience
        name_claim_type = self.name_claim_type
        role_claim_type = self.role_claim_type
        unique_claim_type = self.unique_claim_type
        fallback_unique_claim_type = self.fallback_unique_claim_type
        client_id = self.client_id
        client_secret: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client_secret, Unset):
            client_secret = self.client_secret.to_dict()

        timeout = self.timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if oidc_audience is not UNSET:
            field_dict["oidcAudience"] = oidc_audience
        if name_claim_type is not UNSET:
            field_dict["nameClaimType"] = name_claim_type
        if role_claim_type is not UNSET:
            field_dict["roleClaimType"] = role_claim_type
        if unique_claim_type is not UNSET:
            field_dict["uniqueClaimType"] = unique_claim_type
        if fallback_unique_claim_type is not UNSET:
            field_dict["fallbackUniqueClaimType"] = fallback_unique_claim_type
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        oidc_audience = d.pop("oidcAudience", UNSET)

        name_claim_type = d.pop("nameClaimType", UNSET)

        role_claim_type = d.pop("roleClaimType", UNSET)

        unique_claim_type = d.pop("uniqueClaimType", UNSET)

        fallback_unique_claim_type = d.pop("fallbackUniqueClaimType", UNSET)

        client_id = d.pop("clientId", UNSET)

        _client_secret = d.pop("clientSecret", UNSET)
        client_secret: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_client_secret, Unset):
            client_secret = UNSET
        else:
            client_secret = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_client_secret)

        timeout = d.pop("timeout", UNSET)

        keyfactor_web_keyfactor_api_models_identity_provider_identity_provider_parameter_update_request = cls(
            oidc_audience=oidc_audience,
            name_claim_type=name_claim_type,
            role_claim_type=role_claim_type,
            unique_claim_type=unique_claim_type,
            fallback_unique_claim_type=fallback_unique_claim_type,
            client_id=client_id,
            client_secret=client_secret,
            timeout=timeout,
        )

        return keyfactor_web_keyfactor_api_models_identity_provider_identity_provider_parameter_update_request
