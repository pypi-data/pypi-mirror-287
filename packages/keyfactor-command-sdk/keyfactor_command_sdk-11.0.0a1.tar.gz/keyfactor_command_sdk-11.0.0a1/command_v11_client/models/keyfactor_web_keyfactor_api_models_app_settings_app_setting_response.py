from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        short_name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
        value_type (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    short_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET
    value_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        short_name = self.short_name
        description = self.description
        value = self.value
        value_type = self.value_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if description is not UNSET:
            field_dict["description"] = description
        if value is not UNSET:
            field_dict["value"] = value
        if value_type is not UNSET:
            field_dict["valueType"] = value_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        short_name = d.pop("shortName", UNSET)

        description = d.pop("description", UNSET)

        value = d.pop("value", UNSET)

        value_type = d.pop("valueType", UNSET)

        keyfactor_web_keyfactor_api_models_app_settings_app_setting_response = cls(
            id=id,
            display_name=display_name,
            short_name=short_name,
            description=description,
            value=value,
            value_type=value_type,
        )

        return keyfactor_web_keyfactor_api_models_app_settings_app_setting_response
