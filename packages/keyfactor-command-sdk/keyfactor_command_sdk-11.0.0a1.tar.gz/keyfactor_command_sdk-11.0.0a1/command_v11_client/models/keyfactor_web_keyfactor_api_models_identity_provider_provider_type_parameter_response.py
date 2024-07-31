from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_identity_provider_data_type import CSSCMSDataModelEnumsIdentityProviderDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        data_type (Union[Unset, CSSCMSDataModelEnumsIdentityProviderDataType]):
        required (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    data_type: Union[Unset, CSSCMSDataModelEnumsIdentityProviderDataType] = UNSET
    required: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        display_name = self.display_name
        data_type: Union[Unset, int] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, CSSCMSDataModelEnumsIdentityProviderDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = CSSCMSDataModelEnumsIdentityProviderDataType(_data_type)

        required = d.pop("required", UNSET)

        keyfactor_web_keyfactor_api_models_identity_provider_provider_type_parameter_response = cls(
            id=id,
            name=name,
            display_name=display_name,
            data_type=data_type,
            required=required,
        )

        return keyfactor_web_keyfactor_api_models_identity_provider_provider_type_parameter_response
