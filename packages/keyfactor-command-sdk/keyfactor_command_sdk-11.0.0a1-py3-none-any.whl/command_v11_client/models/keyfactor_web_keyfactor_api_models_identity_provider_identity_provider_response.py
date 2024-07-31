from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_identity_provider_provider_type_parameter_value_response import (
        KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterValueResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsIdentityProviderIdentityProviderResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        authentication_scheme (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        type_id (Union[Unset, str]):
        parameters (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterValueResponse']]):
    """

    id: Union[Unset, str] = UNSET
    authentication_scheme: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    type_id: Union[Unset, str] = UNSET
    parameters: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterValueResponse"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        authentication_scheme = self.authentication_scheme
        display_name = self.display_name
        type_id = self.type_id
        parameters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            if self.parameters is None:
                parameters = None
            else:
                parameters = []
                for parameters_item_data in self.parameters:
                    parameters_item = parameters_item_data.to_dict()

                    parameters.append(parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if authentication_scheme is not UNSET:
            field_dict["authenticationScheme"] = authentication_scheme
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if type_id is not UNSET:
            field_dict["typeId"] = type_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_identity_provider_provider_type_parameter_value_response import (
            KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterValueResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        authentication_scheme = d.pop("authenticationScheme", UNSET)

        display_name = d.pop("displayName", UNSET)

        type_id = d.pop("typeId", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = (
                KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterValueResponse.from_dict(
                    parameters_item_data
                )
            )

            parameters.append(parameters_item)

        keyfactor_web_keyfactor_api_models_identity_provider_identity_provider_response = cls(
            id=id,
            authentication_scheme=authentication_scheme,
            display_name=display_name,
            type_id=type_id,
            parameters=parameters,
        )

        return keyfactor_web_keyfactor_api_models_identity_provider_identity_provider_response
