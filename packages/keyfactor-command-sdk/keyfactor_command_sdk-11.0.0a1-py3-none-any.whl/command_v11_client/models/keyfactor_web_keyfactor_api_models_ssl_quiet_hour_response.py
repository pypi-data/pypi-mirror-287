import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.system_day_of_week import SystemDayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSslQuietHourResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSslQuietHourResponse:
    """
    Attributes:
        start_day (Union[Unset, SystemDayOfWeek]):
        start_time (Union[Unset, datetime.datetime]):
        end_day (Union[Unset, SystemDayOfWeek]):
        end_time (Union[Unset, datetime.datetime]):
    """

    start_day: Union[Unset, SystemDayOfWeek] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_day: Union[Unset, SystemDayOfWeek] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start_day: Union[Unset, int] = UNSET
        if not isinstance(self.start_day, Unset):
            start_day = self.start_day.value

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()[:-6]+'Z'

        end_day: Union[Unset, int] = UNSET
        if not isinstance(self.end_day, Unset):
            end_day = self.end_day.value

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if start_day is not UNSET:
            field_dict["startDay"] = start_day
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_day is not UNSET:
            field_dict["endDay"] = end_day
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _start_day = d.pop("startDay", UNSET)
        start_day: Union[Unset, SystemDayOfWeek]
        if isinstance(_start_day, Unset):
            start_day = UNSET
        else:
            start_day = SystemDayOfWeek(_start_day)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_day = d.pop("endDay", UNSET)
        end_day: Union[Unset, SystemDayOfWeek]
        if isinstance(_end_day, Unset):
            end_day = UNSET
        else:
            end_day = SystemDayOfWeek(_end_day)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        keyfactor_web_keyfactor_api_models_ssl_quiet_hour_response = cls(
            start_day=start_day,
            start_time=start_time,
            end_day=end_day,
            end_time=end_time,
        )

        return keyfactor_web_keyfactor_api_models_ssl_quiet_hour_response
