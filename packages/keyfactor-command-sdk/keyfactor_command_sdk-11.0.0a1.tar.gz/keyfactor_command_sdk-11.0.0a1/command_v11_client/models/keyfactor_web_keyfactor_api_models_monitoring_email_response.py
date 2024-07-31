from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsMonitoringEmailResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsMonitoringEmailResponse:
    """
    Attributes:
        enable_reminder (Union[Unset, bool]):
        warning_days (Union[Unset, int]):
        recipients (Union[Unset, None, List[str]]):
    """

    enable_reminder: Union[Unset, bool] = UNSET
    warning_days: Union[Unset, int] = UNSET
    recipients: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enable_reminder = self.enable_reminder
        warning_days = self.warning_days
        recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            if self.recipients is None:
                recipients = None
            else:
                recipients = self.recipients

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enable_reminder is not UNSET:
            field_dict["enableReminder"] = enable_reminder
        if warning_days is not UNSET:
            field_dict["warningDays"] = warning_days
        if recipients is not UNSET:
            field_dict["recipients"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        enable_reminder = d.pop("enableReminder", UNSET)

        warning_days = d.pop("warningDays", UNSET)

        recipients = cast(List[str], d.pop("recipients", UNSET))

        keyfactor_web_keyfactor_api_models_monitoring_email_response = cls(
            enable_reminder=enable_reminder,
            warning_days=warning_days,
            recipients=recipients,
        )

        return keyfactor_web_keyfactor_api_models_monitoring_email_response
