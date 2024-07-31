from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_metadata_type_enrollment import CSSCMSCoreEnumsMetadataTypeEnrollment
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesTemplateMetadataFieldRequestResponseModel")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesTemplateMetadataFieldRequestResponseModel:
    """
    Attributes:
        id (Union[Unset, int]):
        default_value (Union[Unset, None, str]):
        metadata_id (Union[Unset, int]):
        validation (Union[Unset, None, str]):
        enrollment (Union[Unset, CSSCMSCoreEnumsMetadataTypeEnrollment]):
        message (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    metadata_id: Union[Unset, int] = UNSET
    validation: Union[Unset, None, str] = UNSET
    enrollment: Union[Unset, CSSCMSCoreEnumsMetadataTypeEnrollment] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        default_value = self.default_value
        metadata_id = self.metadata_id
        validation = self.validation
        enrollment: Union[Unset, int] = UNSET
        if not isinstance(self.enrollment, Unset):
            enrollment = self.enrollment.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if metadata_id is not UNSET:
            field_dict["metadataId"] = metadata_id
        if validation is not UNSET:
            field_dict["validation"] = validation
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        metadata_id = d.pop("metadataId", UNSET)

        validation = d.pop("validation", UNSET)

        _enrollment = d.pop("enrollment", UNSET)
        enrollment: Union[Unset, CSSCMSCoreEnumsMetadataTypeEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = CSSCMSCoreEnumsMetadataTypeEnrollment(_enrollment)

        message = d.pop("message", UNSET)

        keyfactor_web_keyfactor_api_models_templates_template_metadata_field_request_response_model = cls(
            id=id,
            default_value=default_value,
            metadata_id=metadata_id,
            validation=validation,
            enrollment=enrollment,
            message=message,
        )

        return keyfactor_web_keyfactor_api_models_templates_template_metadata_field_request_response_model
