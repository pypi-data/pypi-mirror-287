from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_models_interval_model import KeyfactorCommonSchedulingModelsIntervalModel
    from ..models.keyfactor_common_scheduling_models_monthly_model import KeyfactorCommonSchedulingModelsMonthlyModel
    from ..models.keyfactor_common_scheduling_models_time_model import KeyfactorCommonSchedulingModelsTimeModel
    from ..models.keyfactor_common_scheduling_models_weekly_model import KeyfactorCommonSchedulingModelsWeeklyModel


T = TypeVar("T", bound="KeyfactorCommonSchedulingKeyfactorSchedule")


@_attrs_define
class KeyfactorCommonSchedulingKeyfactorSchedule:
    """
    Attributes:
        immediate (Union[Unset, None, bool]):
        interval (Union[Unset, KeyfactorCommonSchedulingModelsIntervalModel]):
        daily (Union[Unset, KeyfactorCommonSchedulingModelsTimeModel]):
        weekly (Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]):
        monthly (Union[Unset, KeyfactorCommonSchedulingModelsMonthlyModel]):
        exactly_once (Union[Unset, KeyfactorCommonSchedulingModelsTimeModel]):
        schedule (Union[Unset, None, str]):
        is_empty (Union[Unset, bool]):
    """

    immediate: Union[Unset, None, bool] = UNSET
    interval: Union[Unset, "KeyfactorCommonSchedulingModelsIntervalModel"] = UNSET
    daily: Union[Unset, "KeyfactorCommonSchedulingModelsTimeModel"] = UNSET
    weekly: Union[Unset, "KeyfactorCommonSchedulingModelsWeeklyModel"] = UNSET
    monthly: Union[Unset, "KeyfactorCommonSchedulingModelsMonthlyModel"] = UNSET
    exactly_once: Union[Unset, "KeyfactorCommonSchedulingModelsTimeModel"] = UNSET
    schedule: Union[Unset, None, str] = UNSET
    is_empty: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        immediate = self.immediate
        interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.to_dict()

        daily: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.daily, Unset):
            daily = self.daily.to_dict()

        weekly: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weekly, Unset):
            weekly = self.weekly.to_dict()

        monthly: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.monthly, Unset):
            monthly = self.monthly.to_dict()

        exactly_once: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.exactly_once, Unset):
            exactly_once = self.exactly_once.to_dict()

        schedule = self.schedule
        is_empty = self.is_empty

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if immediate is not UNSET:
            field_dict["immediate"] = immediate
        if interval is not UNSET:
            field_dict["interval"] = interval
        if daily is not UNSET:
            field_dict["daily"] = daily
        if weekly is not UNSET:
            field_dict["weekly"] = weekly
        if monthly is not UNSET:
            field_dict["monthly"] = monthly
        if exactly_once is not UNSET:
            field_dict["exactlyOnce"] = exactly_once
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if is_empty is not UNSET:
            field_dict["isEmpty"] = is_empty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_models_interval_model import (
            KeyfactorCommonSchedulingModelsIntervalModel,
        )
        from ..models.keyfactor_common_scheduling_models_monthly_model import (
            KeyfactorCommonSchedulingModelsMonthlyModel,
        )
        from ..models.keyfactor_common_scheduling_models_time_model import KeyfactorCommonSchedulingModelsTimeModel
        from ..models.keyfactor_common_scheduling_models_weekly_model import KeyfactorCommonSchedulingModelsWeeklyModel

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        immediate = d.pop("immediate", UNSET)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, KeyfactorCommonSchedulingModelsIntervalModel]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = KeyfactorCommonSchedulingModelsIntervalModel.from_dict(_interval)

        _daily = d.pop("daily", UNSET)
        daily: Union[Unset, KeyfactorCommonSchedulingModelsTimeModel]
        if isinstance(_daily, Unset):
            daily = UNSET
        else:
            daily = KeyfactorCommonSchedulingModelsTimeModel.from_dict(_daily)

        _weekly = d.pop("weekly", UNSET)
        weekly: Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]
        if isinstance(_weekly, Unset):
            weekly = UNSET
        else:
            weekly = KeyfactorCommonSchedulingModelsWeeklyModel.from_dict(_weekly)

        _monthly = d.pop("monthly", UNSET)
        monthly: Union[Unset, KeyfactorCommonSchedulingModelsMonthlyModel]
        if isinstance(_monthly, Unset):
            monthly = UNSET
        else:
            monthly = KeyfactorCommonSchedulingModelsMonthlyModel.from_dict(_monthly)

        _exactly_once = d.pop("exactlyOnce", UNSET)
        exactly_once: Union[Unset, KeyfactorCommonSchedulingModelsTimeModel]
        if isinstance(_exactly_once, Unset):
            exactly_once = UNSET
        else:
            exactly_once = KeyfactorCommonSchedulingModelsTimeModel.from_dict(_exactly_once)

        schedule = d.pop("schedule", UNSET)

        is_empty = d.pop("isEmpty", UNSET)

        keyfactor_common_scheduling_keyfactor_schedule = cls(
            immediate=immediate,
            interval=interval,
            daily=daily,
            weekly=weekly,
            monthly=monthly,
            exactly_once=exactly_once,
            schedule=schedule,
            is_empty=is_empty,
        )

        return keyfactor_common_scheduling_keyfactor_schedule
