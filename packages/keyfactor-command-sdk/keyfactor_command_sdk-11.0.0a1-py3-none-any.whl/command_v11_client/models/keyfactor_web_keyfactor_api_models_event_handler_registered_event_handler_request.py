from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest:
    """
    Attributes:
        id (int):
        use_handler (bool):
    """

    id: int
    use_handler: bool

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        use_handler = self.use_handler

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "useHandler": use_handler,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        use_handler = d.pop("useHandler")

        keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_request = cls(
            id=id,
            use_handler=use_handler,
        )

        return keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_request
