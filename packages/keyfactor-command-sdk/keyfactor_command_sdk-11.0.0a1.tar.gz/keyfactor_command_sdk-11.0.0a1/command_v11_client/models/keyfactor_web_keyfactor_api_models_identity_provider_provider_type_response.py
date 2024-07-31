from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_identity_provider_provider_type_parameter_response import (
        KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, None, str]):
        type_parameters (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterResponse']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    type_parameters: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterResponse"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type_parameters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.type_parameters, Unset):
            if self.type_parameters is None:
                type_parameters = None
            else:
                type_parameters = []
                for type_parameters_item_data in self.type_parameters:
                    type_parameters_item = type_parameters_item_data.to_dict()

                    type_parameters.append(type_parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_parameters is not UNSET:
            field_dict["typeParameters"] = type_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_identity_provider_provider_type_parameter_response import (
            KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_parameters = []
        _type_parameters = d.pop("typeParameters", UNSET)
        for type_parameters_item_data in _type_parameters or []:
            type_parameters_item = (
                KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterResponse.from_dict(
                    type_parameters_item_data
                )
            )

            type_parameters.append(type_parameters_item)

        keyfactor_web_keyfactor_api_models_identity_provider_provider_type_response = cls(
            id=id,
            name=name,
            type_parameters=type_parameters,
        )

        return keyfactor_web_keyfactor_api_models_identity_provider_provider_type_response
