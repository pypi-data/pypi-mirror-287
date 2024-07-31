from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CSSCMSDataModelModelsPkcs10CertificateResponseEnrollmentContext")


@_attrs_define
class CSSCMSDataModelModelsPkcs10CertificateResponseEnrollmentContext:
    """ """

    additional_properties: Dict[str, Optional[str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        csscms_data_model_models_pkcs_10_certificate_response_enrollment_context = cls()

        csscms_data_model_models_pkcs_10_certificate_response_enrollment_context.additional_properties = d
        return csscms_data_model_models_pkcs_10_certificate_response_enrollment_context

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Optional[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Optional[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
