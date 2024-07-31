from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsTemplatesTemplateRegex")


@_attrs_define
class CSSCMSDataModelModelsTemplatesTemplateRegex:
    """
    Attributes:
        template_id (Union[Unset, int]):
        subject_part (Union[Unset, None, str]):
        regex (Union[Unset, None, str]):
        error (Union[Unset, None, str]):
    """

    template_id: Union[Unset, int] = UNSET
    subject_part: Union[Unset, None, str] = UNSET
    regex: Union[Unset, None, str] = UNSET
    error: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        template_id = self.template_id
        subject_part = self.subject_part
        regex = self.regex
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
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
        template_id = d.pop("templateId", UNSET)

        subject_part = d.pop("subjectPart", UNSET)

        regex = d.pop("regex", UNSET)

        error = d.pop("error", UNSET)

        csscms_data_model_models_templates_template_regex = cls(
            template_id=template_id,
            subject_part=subject_part,
            regex=regex,
            error=error,
        )

        return csscms_data_model_models_templates_template_regex
