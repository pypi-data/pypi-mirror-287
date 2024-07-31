from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        use_handler (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    use_handler: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        use_handler = self.use_handler

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if use_handler is not UNSET:
            field_dict["useHandler"] = use_handler

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        use_handler = d.pop("useHandler", UNSET)

        keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_response = cls(
            id=id,
            display_name=display_name,
            use_handler=use_handler,
        )

        return keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_response
