from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse:
    """
    Attributes:
        subject (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        recipient (Union[Unset, None, str]):
    """

    subject: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    recipient: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        message = self.message
        recipient = self.recipient

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message is not UNSET:
            field_dict["message"] = message
        if recipient is not UNSET:
            field_dict["recipient"] = recipient

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        subject = d.pop("subject", UNSET)

        message = d.pop("message", UNSET)

        recipient = d.pop("recipient", UNSET)

        keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_response = cls(
            subject=subject,
            message=message,
            recipient=recipient,
        )

        return keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_response
