from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_pam_provider_type_parameter_response import (
        KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsPAMProviderTypeResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsPAMProviderTypeResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, None, str]):
        parameters (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    parameters: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
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
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_pam_provider_type_parameter_response import (
            KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for parameters_item_data in _parameters or []:
            parameters_item = KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse.from_dict(
                parameters_item_data
            )

            parameters.append(parameters_item)

        keyfactor_web_keyfactor_api_models_pam_provider_type_response = cls(
            id=id,
            name=name,
            parameters=parameters,
        )

        return keyfactor_web_keyfactor_api_models_pam_provider_type_response
