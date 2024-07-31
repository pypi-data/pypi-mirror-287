from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_identity_provider_data_type import CSSCMSDataModelEnumsIdentityProviderDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterValueResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsIdentityProviderProviderTypeParameterValueResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        required (Union[Unset, bool]):
        data_type (Union[Unset, CSSCMSDataModelEnumsIdentityProviderDataType]):
        value (Union[Unset, None, str]):
        secret_value (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    required: Union[Unset, bool] = UNSET
    data_type: Union[Unset, CSSCMSDataModelEnumsIdentityProviderDataType] = UNSET
    value: Union[Unset, None, str] = UNSET
    secret_value: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        display_name = self.display_name
        required = self.required
        data_type: Union[Unset, int] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        value = self.value
        secret_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.secret_value, Unset):
            secret_value = self.secret_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if required is not UNSET:
            field_dict["required"] = required
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if value is not UNSET:
            field_dict["value"] = value
        if secret_value is not UNSET:
            field_dict["secretValue"] = secret_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        required = d.pop("required", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, CSSCMSDataModelEnumsIdentityProviderDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = CSSCMSDataModelEnumsIdentityProviderDataType(_data_type)

        value = d.pop("value", UNSET)

        _secret_value = d.pop("secretValue", UNSET)
        secret_value: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_secret_value, Unset):
            secret_value = UNSET
        else:
            secret_value = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_secret_value)

        keyfactor_web_keyfactor_api_models_identity_provider_provider_type_parameter_value_response = cls(
            id=id,
            name=name,
            display_name=display_name,
            required=required,
            data_type=data_type,
            value=value,
            secret_value=secret_value,
        )

        return keyfactor_web_keyfactor_api_models_identity_provider_provider_type_parameter_value_response
