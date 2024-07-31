from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentRenewalResponse")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentRenewalResponse:
    """
    Attributes:
        keyfactor_id (Union[Unset, int]):
        keyfactor_request_id (Union[Unset, int]):
        thumbprint (Union[Unset, None, str]):
        serial_number (Union[Unset, None, str]):
        issuer_dn (Union[Unset, None, str]):
        request_disposition (Union[Unset, None, str]):
        disposition_message (Union[Unset, None, str]):
        password (Union[Unset, None, str]):
    """

    keyfactor_id: Union[Unset, int] = UNSET
    keyfactor_request_id: Union[Unset, int] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET
    serial_number: Union[Unset, None, str] = UNSET
    issuer_dn: Union[Unset, None, str] = UNSET
    request_disposition: Union[Unset, None, str] = UNSET
    disposition_message: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyfactor_id = self.keyfactor_id
        keyfactor_request_id = self.keyfactor_request_id
        thumbprint = self.thumbprint
        serial_number = self.serial_number
        issuer_dn = self.issuer_dn
        request_disposition = self.request_disposition
        disposition_message = self.disposition_message
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keyfactor_id is not UNSET:
            field_dict["keyfactorId"] = keyfactor_id
        if keyfactor_request_id is not UNSET:
            field_dict["keyfactorRequestId"] = keyfactor_request_id
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if issuer_dn is not UNSET:
            field_dict["issuerDN"] = issuer_dn
        if request_disposition is not UNSET:
            field_dict["requestDisposition"] = request_disposition
        if disposition_message is not UNSET:
            field_dict["dispositionMessage"] = disposition_message
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        keyfactor_id = d.pop("keyfactorId", UNSET)

        keyfactor_request_id = d.pop("keyfactorRequestId", UNSET)

        thumbprint = d.pop("thumbprint", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        issuer_dn = d.pop("issuerDN", UNSET)

        request_disposition = d.pop("requestDisposition", UNSET)

        disposition_message = d.pop("dispositionMessage", UNSET)

        password = d.pop("password", UNSET)

        csscms_data_model_models_enrollment_renewal_response = cls(
            keyfactor_id=keyfactor_id,
            keyfactor_request_id=keyfactor_request_id,
            thumbprint=thumbprint,
            serial_number=serial_number,
            issuer_dn=issuer_dn,
            request_disposition=request_disposition,
            disposition_message=disposition_message,
            password=password,
        )

        return csscms_data_model_models_enrollment_renewal_response
