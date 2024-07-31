from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_enrollment_csr_enrollment_response_metadata import (
        CSSCMSDataModelModelsEnrollmentCSREnrollmentResponseMetadata,
    )
    from ..models.csscms_data_model_models_pkcs_10_certificate_response import (
        CSSCMSDataModelModelsPkcs10CertificateResponse,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse:
    """
    Attributes:
        certificate_information (Union[Unset, CSSCMSDataModelModelsPkcs10CertificateResponse]):
        metadata (Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponseMetadata]):
    """

    certificate_information: Union[Unset, "CSSCMSDataModelModelsPkcs10CertificateResponse"] = UNSET
    metadata: Union[Unset, None, "CSSCMSDataModelModelsEnrollmentCSREnrollmentResponseMetadata"] = UNSET

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
        from ..models.csscms_data_model_models_enrollment_csr_enrollment_response_metadata import (
            CSSCMSDataModelModelsEnrollmentCSREnrollmentResponseMetadata,
        )
        from ..models.csscms_data_model_models_pkcs_10_certificate_response import (
            CSSCMSDataModelModelsPkcs10CertificateResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _certificate_information = d.pop("certificateInformation", UNSET)
        certificate_information: Union[Unset, CSSCMSDataModelModelsPkcs10CertificateResponse]
        if isinstance(_certificate_information, Unset):
            certificate_information = UNSET
        else:
            certificate_information = CSSCMSDataModelModelsPkcs10CertificateResponse.from_dict(_certificate_information)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponseMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CSSCMSDataModelModelsEnrollmentCSREnrollmentResponseMetadata.from_dict(_metadata)

        csscms_data_model_models_enrollment_csr_enrollment_response = cls(
            certificate_information=certificate_information,
            metadata=metadata,
        )

        return csscms_data_model_models_enrollment_csr_enrollment_response
