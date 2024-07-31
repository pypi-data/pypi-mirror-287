from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertResponse:
    """
    Attributes:
        subject (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        recipients (Union[Unset, None, List[str]]):
        ca_request_id (Union[Unset, int]):
        common_name (Union[Unset, None, str]):
        logical_name (Union[Unset, None, str]):
    """

    subject: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    recipients: Union[Unset, None, List[str]] = UNSET
    ca_request_id: Union[Unset, int] = UNSET
    common_name: Union[Unset, None, str] = UNSET
    logical_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        message = self.message
        recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            if self.recipients is None:
                recipients = None
            else:
                recipients = self.recipients

        ca_request_id = self.ca_request_id
        common_name = self.common_name
        logical_name = self.logical_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message is not UNSET:
            field_dict["message"] = message
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if ca_request_id is not UNSET:
            field_dict["caRequestId"] = ca_request_id
        if common_name is not UNSET:
            field_dict["commonName"] = common_name
        if logical_name is not UNSET:
            field_dict["logicalName"] = logical_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        subject = d.pop("subject", UNSET)

        message = d.pop("message", UNSET)

        recipients = cast(List[str], d.pop("recipients", UNSET))

        ca_request_id = d.pop("caRequestId", UNSET)

        common_name = d.pop("commonName", UNSET)

        logical_name = d.pop("logicalName", UNSET)

        keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_response = cls(
            subject=subject,
            message=message,
            recipients=recipients,
            ca_request_id=ca_request_id,
            common_name=common_name,
            logical_name=logical_name,
        )

        return keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_response
