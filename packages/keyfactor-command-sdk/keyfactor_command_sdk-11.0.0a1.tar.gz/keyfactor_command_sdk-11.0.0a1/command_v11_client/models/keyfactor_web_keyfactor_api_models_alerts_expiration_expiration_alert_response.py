from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertResponse:
    """
    Attributes:
        ca_name (Union[Unset, None, str]):
        ca_row (Union[Unset, int]):
        issued_cn (Union[Unset, None, str]):
        expiry (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        recipients (Union[Unset, None, List[str]]):
        send_date (Union[Unset, None, str]):
    """

    ca_name: Union[Unset, None, str] = UNSET
    ca_row: Union[Unset, int] = UNSET
    issued_cn: Union[Unset, None, str] = UNSET
    expiry: Union[Unset, None, str] = UNSET
    subject: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    recipients: Union[Unset, None, List[str]] = UNSET
    send_date: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ca_name = self.ca_name
        ca_row = self.ca_row
        issued_cn = self.issued_cn
        expiry = self.expiry
        subject = self.subject
        message = self.message
        recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            if self.recipients is None:
                recipients = None
            else:
                recipients = self.recipients

        send_date = self.send_date

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ca_name is not UNSET:
            field_dict["caName"] = ca_name
        if ca_row is not UNSET:
            field_dict["caRow"] = ca_row
        if issued_cn is not UNSET:
            field_dict["issuedCN"] = issued_cn
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message is not UNSET:
            field_dict["message"] = message
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if send_date is not UNSET:
            field_dict["sendDate"] = send_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        ca_name = d.pop("caName", UNSET)

        ca_row = d.pop("caRow", UNSET)

        issued_cn = d.pop("issuedCN", UNSET)

        expiry = d.pop("expiry", UNSET)

        subject = d.pop("subject", UNSET)

        message = d.pop("message", UNSET)

        recipients = cast(List[str], d.pop("recipients", UNSET))

        send_date = d.pop("sendDate", UNSET)

        keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_response = cls(
            ca_name=ca_name,
            ca_row=ca_row,
            issued_cn=issued_cn,
            expiry=expiry,
            subject=subject,
            message=message,
            recipients=recipients,
            send_date=send_date,
        )

        return keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_response
