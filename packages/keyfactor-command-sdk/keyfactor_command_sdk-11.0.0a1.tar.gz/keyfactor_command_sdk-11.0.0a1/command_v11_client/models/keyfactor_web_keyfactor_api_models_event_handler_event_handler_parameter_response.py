from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        key (Union[Unset, None, str]):
        default_value (Union[Unset, None, str]):
        parameter_type (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    key: Union[Unset, None, str] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    parameter_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key = self.key
        default_value = self.default_value
        parameter_type = self.parameter_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if parameter_type is not UNSET:
            field_dict["parameterType"] = parameter_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        parameter_type = d.pop("parameterType", UNSET)

        keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_response = cls(
            id=id,
            key=key,
            default_value=default_value,
            parameter_type=parameter_type,
        )

        return keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_response
