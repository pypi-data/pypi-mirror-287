from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCRLRequestModel")


@_attrs_define
class CSSCMSDataModelModelsCRLRequestModel:
    """
    Attributes:
        certificate_authority_logical_name (str):
        certificate_authority_host_name (Union[Unset, None, str]):
    """

    certificate_authority_logical_name: str
    certificate_authority_host_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate_authority_logical_name = self.certificate_authority_logical_name
        certificate_authority_host_name = self.certificate_authority_host_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "certificateAuthorityLogicalName": certificate_authority_logical_name,
            }
        )
        if certificate_authority_host_name is not UNSET:
            field_dict["certificateAuthorityHostName"] = certificate_authority_host_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        certificate_authority_logical_name = d.pop("certificateAuthorityLogicalName")

        certificate_authority_host_name = d.pop("certificateAuthorityHostName", UNSET)

        csscms_data_model_models_crl_request_model = cls(
            certificate_authority_logical_name=certificate_authority_logical_name,
            certificate_authority_host_name=certificate_authority_host_name,
        )

        return csscms_data_model_models_crl_request_model
