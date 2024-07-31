from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_enrollment_pfx_enrollment_response_metadata import (
        CSSCMSDataModelModelsEnrollmentPFXEnrollmentResponseMetadata,
    )
    from ..models.csscms_data_model_models_pkcs_12_certificate_response import (
        CSSCMSDataModelModelsPkcs12CertificateResponse,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentPFXEnrollmentResponse")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentPFXEnrollmentResponse:
    """
    Attributes:
        certificate_information (Union[Unset, CSSCMSDataModelModelsPkcs12CertificateResponse]):
        metadata (Union[Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentResponseMetadata]):
    """

    certificate_information: Union[Unset, "CSSCMSDataModelModelsPkcs12CertificateResponse"] = UNSET
    metadata: Union[Unset, None, "CSSCMSDataModelModelsEnrollmentPFXEnrollmentResponseMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate_information: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.certificate_information, Unset):
            certificate_information = self.certificate_information.to_dict()

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if certificate_information is not UNSET:
            field_dict["certificateInformation"] = certificate_information
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_enrollment_pfx_enrollment_response_metadata import (
            CSSCMSDataModelModelsEnrollmentPFXEnrollmentResponseMetadata,
        )
        from ..models.csscms_data_model_models_pkcs_12_certificate_response import (
            CSSCMSDataModelModelsPkcs12CertificateResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _certificate_information = d.pop("certificateInformation", UNSET)
        certificate_information: Union[Unset, CSSCMSDataModelModelsPkcs12CertificateResponse]
        if isinstance(_certificate_information, Unset):
            certificate_information = UNSET
        else:
            certificate_information = CSSCMSDataModelModelsPkcs12CertificateResponse.from_dict(_certificate_information)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentResponseMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CSSCMSDataModelModelsEnrollmentPFXEnrollmentResponseMetadata.from_dict(_metadata)

        csscms_data_model_models_enrollment_pfx_enrollment_response = cls(
            certificate_information=certificate_information,
            metadata=metadata,
        )

        return csscms_data_model_models_enrollment_pfx_enrollment_response
