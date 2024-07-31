from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_pkcs_10_certificate_response_enrollment_context import (
        CSSCMSDataModelModelsPkcs10CertificateResponseEnrollmentContext,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsPkcs10CertificateResponse")


@_attrs_define
class CSSCMSDataModelModelsPkcs10CertificateResponse:
    """
    Attributes:
        keyfactor_request_id (Union[Unset, int]):
        request_disposition (Union[Unset, None, str]):
        disposition_message (Union[Unset, None, str]):
        enrollment_context (Union[Unset, None, CSSCMSDataModelModelsPkcs10CertificateResponseEnrollmentContext]):
        url (Union[Unset, None, str]):
        keyfactor_id (Union[Unset, int]):
        certificates (Union[Unset, None, List[str]]):
        workflow_instance_id (Union[Unset, str]):
        workflow_reference_id (Union[Unset, int]):
    """

    keyfactor_request_id: Union[Unset, int] = UNSET
    request_disposition: Union[Unset, None, str] = UNSET
    disposition_message: Union[Unset, None, str] = UNSET
    enrollment_context: Union[Unset, None, "CSSCMSDataModelModelsPkcs10CertificateResponseEnrollmentContext"] = UNSET
    url: Union[Unset, None, str] = UNSET
    keyfactor_id: Union[Unset, int] = UNSET
    certificates: Union[Unset, None, List[str]] = UNSET
    workflow_instance_id: Union[Unset, str] = UNSET
    workflow_reference_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyfactor_request_id = self.keyfactor_request_id
        request_disposition = self.request_disposition
        disposition_message = self.disposition_message
        enrollment_context: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.enrollment_context, Unset):
            enrollment_context = self.enrollment_context.to_dict() if self.enrollment_context else None

        url = self.url
        keyfactor_id = self.keyfactor_id
        certificates: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.certificates, Unset):
            if self.certificates is None:
                certificates = None
            else:
                certificates = self.certificates

        workflow_instance_id = self.workflow_instance_id
        workflow_reference_id = self.workflow_reference_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keyfactor_request_id is not UNSET:
            field_dict["keyfactorRequestId"] = keyfactor_request_id
        if request_disposition is not UNSET:
            field_dict["requestDisposition"] = request_disposition
        if disposition_message is not UNSET:
            field_dict["dispositionMessage"] = disposition_message
        if enrollment_context is not UNSET:
            field_dict["enrollmentContext"] = enrollment_context
        if url is not UNSET:
            field_dict["url"] = url
        if keyfactor_id is not UNSET:
            field_dict["keyfactorID"] = keyfactor_id
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if workflow_instance_id is not UNSET:
            field_dict["workflowInstanceId"] = workflow_instance_id
        if workflow_reference_id is not UNSET:
            field_dict["workflowReferenceId"] = workflow_reference_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_pkcs_10_certificate_response_enrollment_context import (
            CSSCMSDataModelModelsPkcs10CertificateResponseEnrollmentContext,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        keyfactor_request_id = d.pop("keyfactorRequestId", UNSET)

        request_disposition = d.pop("requestDisposition", UNSET)

        disposition_message = d.pop("dispositionMessage", UNSET)

        _enrollment_context = d.pop("enrollmentContext", UNSET)
        enrollment_context: Union[Unset, None, CSSCMSDataModelModelsPkcs10CertificateResponseEnrollmentContext]
        if _enrollment_context is None:
            enrollment_context = None
        elif isinstance(_enrollment_context, Unset):
            enrollment_context = UNSET
        else:
            enrollment_context = CSSCMSDataModelModelsPkcs10CertificateResponseEnrollmentContext.from_dict(
                _enrollment_context
            )

        url = d.pop("url", UNSET)

        keyfactor_id = d.pop("keyfactorID", UNSET)

        certificates = cast(List[str], d.pop("certificates", UNSET))

        workflow_instance_id = d.pop("workflowInstanceId", UNSET)

        workflow_reference_id = d.pop("workflowReferenceId", UNSET)

        csscms_data_model_models_pkcs_10_certificate_response = cls(
            keyfactor_request_id=keyfactor_request_id,
            request_disposition=request_disposition,
            disposition_message=disposition_message,
            enrollment_context=enrollment_context,
            url=url,
            keyfactor_id=keyfactor_id,
            certificates=certificates,
            workflow_instance_id=workflow_instance_id,
            workflow_reference_id=workflow_reference_id,
        )

        return csscms_data_model_models_pkcs_10_certificate_response
