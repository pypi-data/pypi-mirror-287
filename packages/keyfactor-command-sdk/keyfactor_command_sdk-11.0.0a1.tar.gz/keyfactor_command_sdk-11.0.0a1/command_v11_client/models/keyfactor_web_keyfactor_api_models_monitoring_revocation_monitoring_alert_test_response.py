from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_alert_build_result import CSSCMSDataModelEnumsAlertBuildResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_monitoring_revocation_monitoring_alert_response import (
        CSSCMSDataModelModelsMonitoringRevocationMonitoringAlertResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringAlertTestResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringAlertTestResponse:
    """
    Attributes:
        revocation_monitoring_alerts (Union[Unset, None,
            List['CSSCMSDataModelModelsMonitoringRevocationMonitoringAlertResponse']]):
        alert_build_result (Union[Unset, CSSCMSDataModelEnumsAlertBuildResult]):
    """

    revocation_monitoring_alerts: Union[
        Unset, None, List["CSSCMSDataModelModelsMonitoringRevocationMonitoringAlertResponse"]
    ] = UNSET
    alert_build_result: Union[Unset, CSSCMSDataModelEnumsAlertBuildResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        revocation_monitoring_alerts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.revocation_monitoring_alerts, Unset):
            if self.revocation_monitoring_alerts is None:
                revocation_monitoring_alerts = None
            else:
                revocation_monitoring_alerts = []
                for revocation_monitoring_alerts_item_data in self.revocation_monitoring_alerts:
                    revocation_monitoring_alerts_item = revocation_monitoring_alerts_item_data.to_dict()

                    revocation_monitoring_alerts.append(revocation_monitoring_alerts_item)

        alert_build_result: Union[Unset, int] = UNSET
        if not isinstance(self.alert_build_result, Unset):
            alert_build_result = self.alert_build_result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if revocation_monitoring_alerts is not UNSET:
            field_dict["revocationMonitoringAlerts"] = revocation_monitoring_alerts
        if alert_build_result is not UNSET:
            field_dict["alertBuildResult"] = alert_build_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_monitoring_revocation_monitoring_alert_response import (
            CSSCMSDataModelModelsMonitoringRevocationMonitoringAlertResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        revocation_monitoring_alerts = []
        _revocation_monitoring_alerts = d.pop("revocationMonitoringAlerts", UNSET)
        for revocation_monitoring_alerts_item_data in _revocation_monitoring_alerts or []:
            revocation_monitoring_alerts_item = (
                CSSCMSDataModelModelsMonitoringRevocationMonitoringAlertResponse.from_dict(
                    revocation_monitoring_alerts_item_data
                )
            )

            revocation_monitoring_alerts.append(revocation_monitoring_alerts_item)

        _alert_build_result = d.pop("alertBuildResult", UNSET)
        alert_build_result: Union[Unset, CSSCMSDataModelEnumsAlertBuildResult]
        if isinstance(_alert_build_result, Unset):
            alert_build_result = UNSET
        else:
            alert_build_result = CSSCMSDataModelEnumsAlertBuildResult(_alert_build_result)

        keyfactor_web_keyfactor_api_models_monitoring_revocation_monitoring_alert_test_response = cls(
            revocation_monitoring_alerts=revocation_monitoring_alerts,
            alert_build_result=alert_build_result,
        )

        return keyfactor_web_keyfactor_api_models_monitoring_revocation_monitoring_alert_test_response
