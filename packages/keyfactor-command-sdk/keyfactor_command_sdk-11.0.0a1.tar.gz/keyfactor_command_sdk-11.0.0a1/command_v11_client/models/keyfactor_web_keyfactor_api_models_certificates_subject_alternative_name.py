from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificatesSubjectAlternativeName")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificatesSubjectAlternativeName:
    """
    Attributes:
        value (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
    """

    value: Union[Unset, None, str] = UNSET
    type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        value = d.pop("value", UNSET)

        type = d.pop("type", UNSET)

        keyfactor_web_keyfactor_api_models_certificates_subject_alternative_name = cls(
            value=value,
            type=type,
        )

        return keyfactor_web_keyfactor_api_models_certificates_subject_alternative_name
