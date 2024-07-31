from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest:
    """
    Attributes:
        id (Union[Unset, int]):
        value (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        keyfactor_web_keyfactor_api_models_app_settings_app_setting_update_bulk_request = cls(
            id=id,
            value=value,
        )

        return keyfactor_web_keyfactor_api_models_app_settings_app_setting_update_bulk_request
