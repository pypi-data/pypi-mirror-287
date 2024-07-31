from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.keyfactor_pkipki_constants_x509_subject_alt_name_element_type import (
    KeyfactorPKIPKIConstantsX509SubjectAltNameElementType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSubjectAlternativeName")


@_attrs_define
class CSSCMSDataModelModelsSubjectAlternativeName:
    """
    Attributes:
        id (Union[Unset, int]):
        value (Union[Unset, None, str]):
        type (Union[Unset, KeyfactorPKIPKIConstantsX509SubjectAltNameElementType]):
        value_hash (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    value: Union[Unset, None, str] = UNSET
    type: Union[Unset, KeyfactorPKIPKIConstantsX509SubjectAltNameElementType] = UNSET
    value_hash: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        value_hash = self.value_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if type is not UNSET:
            field_dict["type"] = type
        if value_hash is not UNSET:
            field_dict["valueHash"] = value_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, KeyfactorPKIPKIConstantsX509SubjectAltNameElementType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = KeyfactorPKIPKIConstantsX509SubjectAltNameElementType(_type)

        value_hash = d.pop("valueHash", UNSET)

        csscms_data_model_models_subject_alternative_name = cls(
            id=id,
            value=value,
            type=type,
            value_hash=value_hash,
        )

        return csscms_data_model_models_subject_alternative_name
