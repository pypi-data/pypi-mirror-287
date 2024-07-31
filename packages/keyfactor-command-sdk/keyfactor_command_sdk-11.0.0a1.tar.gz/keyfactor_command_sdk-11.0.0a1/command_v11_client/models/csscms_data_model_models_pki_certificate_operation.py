from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CSSCMSDataModelModelsPKICertificateOperation")


@_attrs_define
class CSSCMSDataModelModelsPKICertificateOperation:
    """ """

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        csscms_data_model_models_pki_certificate_operation = cls()

        return csscms_data_model_models_pki_certificate_operation
