from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_alert_build_result import CSSCMSDataModelEnumsAlertBuildResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_response import (
        KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertTestResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertTestResponse:
    """
    Attributes:
        key_rotation_alerts (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse']]):
        alert_build_result (Union[Unset, CSSCMSDataModelEnumsAlertBuildResult]):
    """

    key_rotation_alerts: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse"]
    ] = UNSET
    alert_build_result: Union[Unset, CSSCMSDataModelEnumsAlertBuildResult] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        key_rotation_alerts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.key_rotation_alerts, Unset):
            if self.key_rotation_alerts is None:
                key_rotation_alerts = None
            else:
                key_rotation_alerts = []
                for key_rotation_alerts_item_data in self.key_rotation_alerts:
                    key_rotation_alerts_item = key_rotation_alerts_item_data.to_dict()

                    key_rotation_alerts.append(key_rotation_alerts_item)

        alert_build_result: Union[Unset, int] = UNSET
        if not isinstance(self.alert_build_result, Unset):
            alert_build_result = self.alert_build_result.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if key_rotation_alerts is not UNSET:
            field_dict["keyRotationAlerts"] = key_rotation_alerts
        if alert_build_result is not UNSET:
            field_dict["alertBuildResult"] = alert_build_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_response import (
            KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        key_rotation_alerts = []
        _key_rotation_alerts = d.pop("keyRotationAlerts", UNSET)
        for key_rotation_alerts_item_data in _key_rotation_alerts or []:
            key_rotation_alerts_item = (
                KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertResponse.from_dict(
                    key_rotation_alerts_item_data
                )
            )

            key_rotation_alerts.append(key_rotation_alerts_item)

        _alert_build_result = d.pop("alertBuildResult", UNSET)
        alert_build_result: Union[Unset, CSSCMSDataModelEnumsAlertBuildResult]
        if isinstance(_alert_build_result, Unset):
            alert_build_result = UNSET
        else:
            alert_build_result = CSSCMSDataModelEnumsAlertBuildResult(_alert_build_result)

        keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_test_response = cls(
            key_rotation_alerts=key_rotation_alerts,
            alert_build_result=alert_build_result,
        )

        return keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_test_response
