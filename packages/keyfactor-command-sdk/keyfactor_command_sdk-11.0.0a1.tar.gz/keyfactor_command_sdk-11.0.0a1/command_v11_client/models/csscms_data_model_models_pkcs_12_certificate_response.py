from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_private_key_status import CSSCMSDataModelEnumsPrivateKeyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_pkcs_12_certificate_response_enrollment_context import (
        CSSCMSDataModelModelsPkcs12CertificateResponseEnrollmentContext,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsPkcs12CertificateResponse")


@_attrs_define
class CSSCMSDataModelModelsPkcs12CertificateResponse:
    """
    Attributes:
        keyfactor_request_id (Union[Unset, int]):
        request_disposition (Union[Unset, None, str]):
        disposition_message (Union[Unset, None, str]):
        enrollment_context (Union[Unset, None, CSSCMSDataModelModelsPkcs12CertificateResponseEnrollmentContext]):
        url (Union[Unset, None, str]):
        keyfactor_id (Union[Unset, int]):
        pkcs_12_blob (Union[Unset, None, str]):
        password (Union[Unset, None, str]):
        key_status (Union[Unset, CSSCMSDataModelEnumsPrivateKeyStatus]):
        workflow_instance_id (Union[Unset, str]):
        workflow_reference_id (Union[Unset, int]):
        store_ids_invalid_for_renewal (Union[Unset, None, List[str]]):
    """

    keyfactor_request_id: Union[Unset, int] = UNSET
    request_disposition: Union[Unset, None, str] = UNSET
    disposition_message: Union[Unset, None, str] = UNSET
    enrollment_context: Union[Unset, None, "CSSCMSDataModelModelsPkcs12CertificateResponseEnrollmentContext"] = UNSET
    url: Union[Unset, None, str] = UNSET
    keyfactor_id: Union[Unset, int] = UNSET
    pkcs_12_blob: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET
    key_status: Union[Unset, CSSCMSDataModelEnumsPrivateKeyStatus] = UNSET
    workflow_instance_id: Union[Unset, str] = UNSET
    workflow_reference_id: Union[Unset, int] = UNSET
    store_ids_invalid_for_renewal: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyfactor_request_id = self.keyfactor_request_id
        request_disposition = self.request_disposition
        disposition_message = self.disposition_message
        enrollment_context: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.enrollment_context, Unset):
            enrollment_context = self.enrollment_context.to_dict() if self.enrollment_context else None

        url = self.url
        keyfactor_id = self.keyfactor_id
        pkcs_12_blob = self.pkcs_12_blob
        password = self.password
        key_status: Union[Unset, int] = UNSET
        if not isinstance(self.key_status, Unset):
            key_status = self.key_status.value

        workflow_instance_id = self.workflow_instance_id
        workflow_reference_id = self.workflow_reference_id
        store_ids_invalid_for_renewal: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.store_ids_invalid_for_renewal, Unset):
            if self.store_ids_invalid_for_renewal is None:
                store_ids_invalid_for_renewal = None
            else:
                store_ids_invalid_for_renewal = self.store_ids_invalid_for_renewal

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
            field_dict["keyfactorId"] = keyfactor_id
        if pkcs_12_blob is not UNSET:
            field_dict["pkcs12Blob"] = pkcs_12_blob
        if password is not UNSET:
            field_dict["password"] = password
        if key_status is not UNSET:
            field_dict["keyStatus"] = key_status
        if workflow_instance_id is not UNSET:
            field_dict["workflowInstanceId"] = workflow_instance_id
        if workflow_reference_id is not UNSET:
            field_dict["workflowReferenceId"] = workflow_reference_id
        if store_ids_invalid_for_renewal is not UNSET:
            field_dict["storeIdsInvalidForRenewal"] = store_ids_invalid_for_renewal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_pkcs_12_certificate_response_enrollment_context import (
            CSSCMSDataModelModelsPkcs12CertificateResponseEnrollmentContext,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        keyfactor_request_id = d.pop("keyfactorRequestId", UNSET)

        request_disposition = d.pop("requestDisposition", UNSET)

        disposition_message = d.pop("dispositionMessage", UNSET)

        _enrollment_context = d.pop("enrollmentContext", UNSET)
        enrollment_context: Union[Unset, None, CSSCMSDataModelModelsPkcs12CertificateResponseEnrollmentContext]
        if _enrollment_context is None:
            enrollment_context = None
        elif isinstance(_enrollment_context, Unset):
            enrollment_context = UNSET
        else:
            enrollment_context = CSSCMSDataModelModelsPkcs12CertificateResponseEnrollmentContext.from_dict(
                _enrollment_context
            )

        url = d.pop("url", UNSET)

        keyfactor_id = d.pop("keyfactorId", UNSET)

        pkcs_12_blob = d.pop("pkcs12Blob", UNSET)

        password = d.pop("password", UNSET)

        _key_status = d.pop("keyStatus", UNSET)
        key_status: Union[Unset, CSSCMSDataModelEnumsPrivateKeyStatus]
        if isinstance(_key_status, Unset):
            key_status = UNSET
        else:
            key_status = CSSCMSDataModelEnumsPrivateKeyStatus(_key_status)

        workflow_instance_id = d.pop("workflowInstanceId", UNSET)

        workflow_reference_id = d.pop("workflowReferenceId", UNSET)

        store_ids_invalid_for_renewal = cast(List[str], d.pop("storeIdsInvalidForRenewal", UNSET))

        csscms_data_model_models_pkcs_12_certificate_response = cls(
            keyfactor_request_id=keyfactor_request_id,
            request_disposition=request_disposition,
            disposition_message=disposition_message,
            enrollment_context=enrollment_context,
            url=url,
            keyfactor_id=keyfactor_id,
            pkcs_12_blob=pkcs_12_blob,
            password=password,
            key_status=key_status,
            workflow_instance_id=workflow_instance_id,
            workflow_reference_id=workflow_reference_id,
            store_ids_invalid_for_renewal=store_ids_invalid_for_renewal,
        )

        return csscms_data_model_models_pkcs_12_certificate_response
