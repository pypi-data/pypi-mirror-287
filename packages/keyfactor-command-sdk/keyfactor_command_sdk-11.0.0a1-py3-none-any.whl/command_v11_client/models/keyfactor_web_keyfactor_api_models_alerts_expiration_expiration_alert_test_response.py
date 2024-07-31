from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_alert_build_result import CSSCMSDataModelEnumsAlertBuildResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_response import (
        KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertTestResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertTestResponse:
    """
    Attributes:
        expiration_alerts (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertResponse']]):
        alert_build_result (Union[Unset, CSSCMSDataModelEnumsAlertBuildResult]):
    """

    expiration_alerts: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertResponse"]
    ] = UNSET
    alert_build_result: Union[Unset, CSSCMSDataModelEnumsAlertBuildResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        expiration_alerts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.expiration_alerts, Unset):
            if self.expiration_alerts is None:
                expiration_alerts = None
            else:
                expiration_alerts = []
                for expiration_alerts_item_data in self.expiration_alerts:
                    expiration_alerts_item = expiration_alerts_item_data.to_dict()

                    expiration_alerts.append(expiration_alerts_item)

        alert_build_result: Union[Unset, int] = UNSET
        if not isinstance(self.alert_build_result, Unset):
            alert_build_result = self.alert_build_result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if expiration_alerts is not UNSET:
            field_dict["expirationAlerts"] = expiration_alerts
        if alert_build_result is not UNSET:
            field_dict["alertBuildResult"] = alert_build_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_response import (
            KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        expiration_alerts = []
        _expiration_alerts = d.pop("expirationAlerts", UNSET)
        for expiration_alerts_item_data in _expiration_alerts or []:
            expiration_alerts_item = KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertResponse.from_dict(
                expiration_alerts_item_data
            )

            expiration_alerts.append(expiration_alerts_item)

        _alert_build_result = d.pop("alertBuildResult", UNSET)
        alert_build_result: Union[Unset, CSSCMSDataModelEnumsAlertBuildResult]
        if isinstance(_alert_build_result, Unset):
            alert_build_result = UNSET
        else:
            alert_build_result = CSSCMSDataModelEnumsAlertBuildResult(_alert_build_result)

        keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_test_response = cls(
            expiration_alerts=expiration_alerts,
            alert_build_result=alert_build_result,
        )

        return keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_test_response
