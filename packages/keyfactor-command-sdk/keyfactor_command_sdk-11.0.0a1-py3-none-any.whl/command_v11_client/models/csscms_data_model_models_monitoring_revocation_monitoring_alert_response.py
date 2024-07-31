from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsMonitoringRevocationMonitoringAlertResponse")


@_attrs_define
class CSSCMSDataModelModelsMonitoringRevocationMonitoringAlertResponse:
    """
    Attributes:
        subject (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        recipients (Union[Unset, None, List[str]]):
    """

    subject: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    recipients: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        message = self.message
        recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            if self.recipients is None:
                recipients = None
            else:
                recipients = self.recipients

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message is not UNSET:
            field_dict["message"] = message
        if recipients is not UNSET:
            field_dict["recipients"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        subject = d.pop("subject", UNSET)

        message = d.pop("message", UNSET)

        recipients = cast(List[str], d.pop("recipients", UNSET))

        csscms_data_model_models_monitoring_revocation_monitoring_alert_response = cls(
            subject=subject,
            message=message,
            recipients=recipients,
        )

        return csscms_data_model_models_monitoring_revocation_monitoring_alert_response
