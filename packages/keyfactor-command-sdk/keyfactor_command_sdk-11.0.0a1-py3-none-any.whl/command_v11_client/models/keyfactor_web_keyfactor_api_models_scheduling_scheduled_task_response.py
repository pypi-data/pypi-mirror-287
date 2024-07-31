import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.csscms_core_enums_scheduled_task_type import CSSCMSCoreEnumsScheduledTaskType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSchedulingScheduledTaskResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSchedulingScheduledTaskResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        schedule (Union[Unset, None, str]):
        schedule_type (Union[Unset, CSSCMSCoreEnumsScheduledTaskType]):
        enabled (Union[Unset, bool]):
        name (Union[Unset, None, str]):
        entity_id (Union[Unset, None, int]):
        last_run (Union[Unset, None, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    schedule: Union[Unset, None, str] = UNSET
    schedule_type: Union[Unset, CSSCMSCoreEnumsScheduledTaskType] = UNSET
    enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, None, str] = UNSET
    entity_id: Union[Unset, None, int] = UNSET
    last_run: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        schedule = self.schedule
        schedule_type: Union[Unset, int] = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        enabled = self.enabled
        name = self.name
        entity_id = self.entity_id
        last_run: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.isoformat()[:-6]+'Z' if self.last_run else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if schedule_type is not UNSET:
            field_dict["scheduleType"] = schedule_type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        schedule = d.pop("schedule", UNSET)

        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, CSSCMSCoreEnumsScheduledTaskType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = CSSCMSCoreEnumsScheduledTaskType(_schedule_type)

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        entity_id = d.pop("entityId", UNSET)

        _last_run = d.pop("lastRun", UNSET)
        last_run: Union[Unset, None, datetime.datetime]
        if _last_run is None:
            last_run = None
        elif isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = isoparse(_last_run)

        keyfactor_web_keyfactor_api_models_scheduling_scheduled_task_response = cls(
            id=id,
            schedule=schedule,
            schedule_type=schedule_type,
            enabled=enabled,
            name=name,
            entity_id=entity_id,
            last_run=last_run,
        )

        return keyfactor_web_keyfactor_api_models_scheduling_scheduled_task_response
