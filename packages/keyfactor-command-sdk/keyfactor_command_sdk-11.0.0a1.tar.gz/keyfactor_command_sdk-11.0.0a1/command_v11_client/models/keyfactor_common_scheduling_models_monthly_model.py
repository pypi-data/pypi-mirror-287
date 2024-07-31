import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorCommonSchedulingModelsMonthlyModel")


@_attrs_define
class KeyfactorCommonSchedulingModelsMonthlyModel:
    """
    Attributes:
        time (Union[Unset, datetime.datetime]):
        day (Union[Unset, int]):
    """

    time: Union[Unset, datetime.datetime] = UNSET
    day: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()[:-6]+'Z'

        day = self.day

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if day is not UNSET:
            field_dict["day"] = day

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

        day = d.pop("day", UNSET)

        keyfactor_common_scheduling_models_monthly_model = cls(
            time=time,
            day=day,
        )

        return keyfactor_common_scheduling_models_monthly_model
