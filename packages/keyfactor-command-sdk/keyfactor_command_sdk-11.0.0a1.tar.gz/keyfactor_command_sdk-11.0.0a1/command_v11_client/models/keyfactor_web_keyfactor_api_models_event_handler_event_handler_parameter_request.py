from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest:
    """
    Attributes:
        key (str):
        default_value (str):
        parameter_type (str):
    """

    key: str
    default_value: str
    parameter_type: str

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        default_value = self.default_value
        parameter_type = self.parameter_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "key": key,
                "defaultValue": default_value,
                "parameterType": parameter_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        key = d.pop("key")

        default_value = d.pop("defaultValue")

        parameter_type = d.pop("parameterType")

        keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_request = cls(
            key=key,
            default_value=default_value,
            parameter_type=parameter_type,
        )

        return keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_request
