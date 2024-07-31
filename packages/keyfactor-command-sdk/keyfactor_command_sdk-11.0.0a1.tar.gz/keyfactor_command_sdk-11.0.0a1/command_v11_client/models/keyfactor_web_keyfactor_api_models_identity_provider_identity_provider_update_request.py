from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_identity_provider_identity_provider_parameter_update_request import (
        KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderParameterUpdateRequest,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderUpdateRequest:
    """
    Attributes:
        authentication_scheme (str):
        display_name (str):
        parameters (Union[Unset, KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderParameterUpdateRequest]):
    """

    authentication_scheme: str
    display_name: str
    parameters: Union[
        Unset, "KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderParameterUpdateRequest"
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        authentication_scheme = self.authentication_scheme
        display_name = self.display_name
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "authenticationScheme": authentication_scheme,
                "displayName": display_name,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_identity_provider_identity_provider_parameter_update_request import (
            KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderParameterUpdateRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        authentication_scheme = d.pop("authenticationScheme")

        display_name = d.pop("displayName")

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderParameterUpdateRequest]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderParameterUpdateRequest.from_dict(
                _parameters
            )

        keyfactor_web_keyfactor_api_models_identity_provider_identity_provider_update_request = cls(
            authentication_scheme=authentication_scheme,
            display_name=display_name,
            parameters=parameters,
        )

        return keyfactor_web_keyfactor_api_models_identity_provider_identity_provider_update_request
