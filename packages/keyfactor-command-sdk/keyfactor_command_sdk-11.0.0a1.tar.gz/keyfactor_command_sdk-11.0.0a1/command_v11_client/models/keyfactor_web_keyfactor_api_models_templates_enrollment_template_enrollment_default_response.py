from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentDefaultResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentDefaultResponse:
    """
    Attributes:
        subject_part (Union[Unset, None, str]): The subject part to apply the default to.
        value (Union[Unset, None, str]): The value to apply by default.
    """

    subject_part: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject_part = self.subject_part
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subject_part is not UNSET:
            field_dict["subjectPart"] = subject_part
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        subject_part = d.pop("subjectPart", UNSET)

        value = d.pop("value", UNSET)

        keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_default_response = cls(
            subject_part=subject_part,
            value=value,
        )

        return keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_default_response
