from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentCSRGenerationRequestSaNs")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentCSRGenerationRequestSaNs:
    """ """

    additional_properties: Dict[str, Optional[List[str]]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if prop is None:
                field_dict[prop_name] = None
            else:
                field_dict[prop_name] = prop

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        csscms_data_model_models_enrollment_csr_generation_request_sa_ns = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(List[str], prop_dict)

            additional_properties[prop_name] = additional_property

        csscms_data_model_models_enrollment_csr_generation_request_sa_ns.additional_properties = additional_properties
        return csscms_data_model_models_enrollment_csr_generation_request_sa_ns

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Optional[List[str]]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Optional[List[str]]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
