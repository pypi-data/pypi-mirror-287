from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.csscms_core_enums_template_enrollment_field_type import CSSCMSCoreEnumsTemplateEnrollmentFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesTemplateEnrollmentFieldRequestResponseModel")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesTemplateEnrollmentFieldRequestResponseModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        options (Union[Unset, None, List[str]]):
        data_type (Union[Unset, CSSCMSCoreEnumsTemplateEnrollmentFieldType]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    options: Union[Unset, None, List[str]] = UNSET
    data_type: Union[Unset, CSSCMSCoreEnumsTemplateEnrollmentFieldType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        options: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.options, Unset):
            if self.options is None:
                options = None
            else:
                options = self.options

        data_type: Union[Unset, int] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options
        if data_type is not UNSET:
            field_dict["dataType"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        options = cast(List[str], d.pop("options", UNSET))

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, CSSCMSCoreEnumsTemplateEnrollmentFieldType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = CSSCMSCoreEnumsTemplateEnrollmentFieldType(_data_type)

        keyfactor_web_keyfactor_api_models_templates_template_enrollment_field_request_response_model = cls(
            id=id,
            name=name,
            options=options,
            data_type=data_type,
        )

        return keyfactor_web_keyfactor_api_models_templates_template_enrollment_field_request_response_model
