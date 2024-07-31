from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentRegexResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentRegexResponse:
    """
    Attributes:
        subject_part (Union[Unset, None, str]): The subject part to apply the regular expression to.
        regex (Union[Unset, None, str]): The regular expression to apply to the subject part.
        error (Union[Unset, None, str]): The error message to show when the regex validation fails.
    """

    subject_part: Union[Unset, None, str] = UNSET
    regex: Union[Unset, None, str] = UNSET
    error: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject_part = self.subject_part
        regex = self.regex
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subject_part is not UNSET:
            field_dict["subjectPart"] = subject_part
        if regex is not UNSET:
            field_dict["regex"] = regex
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        subject_part = d.pop("subjectPart", UNSET)

        regex = d.pop("regex", UNSET)

        error = d.pop("error", UNSET)

        keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_regex_response = cls(
            subject_part=subject_part,
            regex=regex,
            error=error,
        )

        return keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_regex_response
