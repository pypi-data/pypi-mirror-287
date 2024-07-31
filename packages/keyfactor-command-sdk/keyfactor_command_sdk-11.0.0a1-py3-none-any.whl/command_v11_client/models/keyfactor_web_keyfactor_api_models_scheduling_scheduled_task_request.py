import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.csscms_core_enums_scheduled_task_type import CSSCMSCoreEnumsScheduledTaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSchedulingScheduledTaskRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSchedulingScheduledTaskRequest:
    """
    Attributes:
        schedule_type (CSSCMSCoreEnumsScheduledTaskType):
        id (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        interval (Union[Unset, None, int]):
        time_of_day (Union[Unset, None, datetime.datetime]):
    """

    schedule_type: CSSCMSCoreEnumsScheduledTaskType
    id: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    interval: Union[Unset, None, int] = UNSET
    time_of_day: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        schedule_type = self.schedule_type.value

        id = self.id
        enabled = self.enabled
        interval = self.interval
        time_of_day: Union[Unset, None, str] = UNSET
        if not isinstance(self.time_of_day, Unset):
            time_of_day = self.time_of_day.isoformat()[:-6]+'Z' if self.time_of_day else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "scheduleType": schedule_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if interval is not UNSET:
            field_dict["interval"] = interval
        if time_of_day is not UNSET:
            field_dict["timeOfDay"] = time_of_day

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        schedule_type = CSSCMSCoreEnumsScheduledTaskType(d.pop("scheduleType"))

        id = d.pop("id", UNSET)

        enabled = d.pop("enabled", UNSET)

        interval = d.pop("interval", UNSET)

        _time_of_day = d.pop("timeOfDay", UNSET)
        time_of_day: Union[Unset, None, datetime.datetime]
        if _time_of_day is None:
            time_of_day = None
        elif isinstance(_time_of_day, Unset):
            time_of_day = UNSET
        else:
            time_of_day = isoparse(_time_of_day)

        keyfactor_web_keyfactor_api_models_scheduling_scheduled_task_request = cls(
            schedule_type=schedule_type,
            id=id,
            enabled=enabled,
            interval=interval,
            time_of_day=time_of_day,
        )

        return keyfactor_web_keyfactor_api_models_scheduling_scheduled_task_request
