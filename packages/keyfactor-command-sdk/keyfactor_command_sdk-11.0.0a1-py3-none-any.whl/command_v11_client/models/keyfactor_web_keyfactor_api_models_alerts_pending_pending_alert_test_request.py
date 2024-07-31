from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertTestRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertTestRequest:
    """
    Attributes:
        alert_id (Union[Unset, int]):
        send_alerts (Union[Unset, bool]):
    """

    alert_id: Union[Unset, int] = UNSET
    send_alerts: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        alert_id = self.alert_id
        send_alerts = self.send_alerts

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if alert_id is not UNSET:
            field_dict["alertId"] = alert_id
        if send_alerts is not UNSET:
            field_dict["sendAlerts"] = send_alerts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        alert_id = d.pop("alertId", UNSET)

        send_alerts = d.pop("sendAlerts", UNSET)

        keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_test_request = cls(
            alert_id=alert_id,
            send_alerts=send_alerts,
        )

        return keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_test_request
