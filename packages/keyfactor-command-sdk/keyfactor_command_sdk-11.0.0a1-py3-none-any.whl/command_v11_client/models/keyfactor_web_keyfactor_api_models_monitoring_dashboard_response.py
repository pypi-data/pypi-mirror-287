from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsMonitoringDashboardResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsMonitoringDashboardResponse:
    """
    Attributes:
        show (Union[Unset, bool]):
        warning_hours (Union[Unset, int]):
    """

    show: Union[Unset, bool] = UNSET
    warning_hours: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        show = self.show
        warning_hours = self.warning_hours

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if show is not UNSET:
            field_dict["show"] = show
        if warning_hours is not UNSET:
            field_dict["warningHours"] = warning_hours

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        show = d.pop("show", UNSET)

        warning_hours = d.pop("warningHours", UNSET)

        keyfactor_web_keyfactor_api_models_monitoring_dashboard_response = cls(
            show=show,
            warning_hours=warning_hours,
        )

        return keyfactor_web_keyfactor_api_models_monitoring_dashboard_response
