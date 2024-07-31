import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertTestRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertTestRequest:
    """
    Attributes:
        alert_id (Union[Unset, int]):
        evaluation_date (Union[Unset, datetime.datetime]):
        previous_evaluation_date (Union[Unset, datetime.datetime]):
        send_alerts (Union[Unset, bool]):
    """

    alert_id: Union[Unset, int] = UNSET
    evaluation_date: Union[Unset, datetime.datetime] = UNSET
    previous_evaluation_date: Union[Unset, datetime.datetime] = UNSET
    send_alerts: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        alert_id = self.alert_id
        evaluation_date: Union[Unset, str] = UNSET
        if not isinstance(self.evaluation_date, Unset):
            evaluation_date = self.evaluation_date.isoformat()[:-6]+'Z'

        previous_evaluation_date: Union[Unset, str] = UNSET
        if not isinstance(self.previous_evaluation_date, Unset):
            previous_evaluation_date = self.previous_evaluation_date.isoformat()[:-6]+'Z'

        send_alerts = self.send_alerts

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if alert_id is not UNSET:
            field_dict["alertId"] = alert_id
        if evaluation_date is not UNSET:
            field_dict["evaluationDate"] = evaluation_date
        if previous_evaluation_date is not UNSET:
            field_dict["previousEvaluationDate"] = previous_evaluation_date
        if send_alerts is not UNSET:
            field_dict["sendAlerts"] = send_alerts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        alert_id = d.pop("alertId", UNSET)

        _evaluation_date = d.pop("evaluationDate", UNSET)
        evaluation_date: Union[Unset, datetime.datetime]
        if isinstance(_evaluation_date, Unset):
            evaluation_date = UNSET
        else:
            evaluation_date = isoparse(_evaluation_date)

        _previous_evaluation_date = d.pop("previousEvaluationDate", UNSET)
        previous_evaluation_date: Union[Unset, datetime.datetime]
        if isinstance(_previous_evaluation_date, Unset):
            previous_evaluation_date = UNSET
        else:
            previous_evaluation_date = isoparse(_previous_evaluation_date)

        send_alerts = d.pop("sendAlerts", UNSET)

        keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_test_request = cls(
            alert_id=alert_id,
            evaluation_date=evaluation_date,
            previous_evaluation_date=previous_evaluation_date,
            send_alerts=send_alerts,
        )

        return keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_test_request
