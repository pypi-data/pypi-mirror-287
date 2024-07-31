from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_alert_build_result import CSSCMSDataModelEnumsAlertBuildResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_response import (
        KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertTestResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertTestResponse:
    """
    Attributes:
        pending_alerts (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertResponse']]):
        alert_build_result (Union[Unset, CSSCMSDataModelEnumsAlertBuildResult]):
    """

    pending_alerts: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertResponse"]] = UNSET
    alert_build_result: Union[Unset, CSSCMSDataModelEnumsAlertBuildResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        pending_alerts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pending_alerts, Unset):
            if self.pending_alerts is None:
                pending_alerts = None
            else:
                pending_alerts = []
                for pending_alerts_item_data in self.pending_alerts:
                    pending_alerts_item = pending_alerts_item_data.to_dict()

                    pending_alerts.append(pending_alerts_item)

        alert_build_result: Union[Unset, int] = UNSET
        if not isinstance(self.alert_build_result, Unset):
            alert_build_result = self.alert_build_result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if pending_alerts is not UNSET:
            field_dict["pendingAlerts"] = pending_alerts
        if alert_build_result is not UNSET:
            field_dict["alertBuildResult"] = alert_build_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_response import (
            KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        pending_alerts = []
        _pending_alerts = d.pop("pendingAlerts", UNSET)
        for pending_alerts_item_data in _pending_alerts or []:
            pending_alerts_item = KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertResponse.from_dict(
                pending_alerts_item_data
            )

            pending_alerts.append(pending_alerts_item)

        _alert_build_result = d.pop("alertBuildResult", UNSET)
        alert_build_result: Union[Unset, CSSCMSDataModelEnumsAlertBuildResult]
        if isinstance(_alert_build_result, Unset):
            alert_build_result = UNSET
        else:
            alert_build_result = CSSCMSDataModelEnumsAlertBuildResult(_alert_build_result)

        keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_test_response = cls(
            pending_alerts=pending_alerts,
            alert_build_result=alert_build_result,
        )

        return keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_test_response
