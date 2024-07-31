import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.system_day_of_week import SystemDayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorCommonSchedulingModelsWeeklyModel")


@_attrs_define
class KeyfactorCommonSchedulingModelsWeeklyModel:
    """
    Attributes:
        time (Union[Unset, datetime.datetime]):
        days (Union[Unset, None, List[SystemDayOfWeek]]):
    """

    time: Union[Unset, datetime.datetime] = UNSET
    days: Union[Unset, None, List[SystemDayOfWeek]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()[:-6]+'Z'

        days: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.days, Unset):
            if self.days is None:
                days = None
            else:
                days = []
                for days_item_data in self.days:
                    days_item = days_item_data.value

                    days.append(days_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        days = []
        _days = d.pop("days", UNSET)
        for days_item_data in _days or []:
            days_item = SystemDayOfWeek(days_item_data)

            days.append(days_item)

        keyfactor_common_scheduling_models_weekly_model = cls(
            time=time,
            days=days,
        )

        return keyfactor_common_scheduling_models_weekly_model
