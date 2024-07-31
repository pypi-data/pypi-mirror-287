from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsEventHandlerRegistrationEventHandlerRegistrationUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsEventHandlerRegistrationEventHandlerRegistrationUpdateRequest:
    """
    Attributes:
        display_name (Union[Unset, None, str]):
        enabled (Union[Unset, bool]):
    """

    display_name: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        display_name = d.pop("displayName", UNSET)

        enabled = d.pop("enabled", UNSET)

        keyfactor_web_keyfactor_api_models_event_handler_registration_event_handler_registration_update_request = cls(
            display_name=display_name,
            enabled=enabled,
        )

        return keyfactor_web_keyfactor_api_models_event_handler_registration_event_handler_registration_update_request
