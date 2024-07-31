from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadataInput")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadataInput:
    """ """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        csscms_data_model_models_enrollment_csr_enrollment_request_metadata_input = cls()

        csscms_data_model_models_enrollment_csr_enrollment_request_metadata_input.additional_properties = d
        return csscms_data_model_models_enrollment_csr_enrollment_request_metadata_input

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
