from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesValidSubjectPartResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesValidSubjectPartResponse:
    """
    Attributes:
        subject_part (Union[Unset, None, str]):
        subject_part_name (Union[Unset, None, str]):
    """

    subject_part: Union[Unset, None, str] = UNSET
    subject_part_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject_part = self.subject_part
        subject_part_name = self.subject_part_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subject_part is not UNSET:
            field_dict["subjectPart"] = subject_part
        if subject_part_name is not UNSET:
            field_dict["subjectPartName"] = subject_part_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        subject_part = d.pop("subjectPart", UNSET)

        subject_part_name = d.pop("subjectPartName", UNSET)

        keyfactor_web_keyfactor_api_models_templates_valid_subject_part_response = cls(
            subject_part=subject_part,
            subject_part_name=subject_part_name,
        )

        return keyfactor_web_keyfactor_api_models_templates_valid_subject_part_response
