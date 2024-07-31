from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsAlertScheduleAlertScheduleRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsAlertScheduleAlertScheduleRequest:
    """
    Attributes:
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
    """

    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        keyfactor_web_keyfactor_api_models_alerts_alert_schedule_alert_schedule_request = cls(
            schedule=schedule,
        )

        return keyfactor_web_keyfactor_api_models_alerts_alert_schedule_alert_schedule_request
