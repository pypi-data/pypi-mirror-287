from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertTestAllRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertTestAllRequest:
    """
    Attributes:
        send_alerts (Union[Unset, bool]):
    """

    send_alerts: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        send_alerts = self.send_alerts

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if send_alerts is not UNSET:
            field_dict["sendAlerts"] = send_alerts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        send_alerts = d.pop("sendAlerts", UNSET)

        keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_test_all_request = cls(
            send_alerts=send_alerts,
        )

        return keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_test_all_request
