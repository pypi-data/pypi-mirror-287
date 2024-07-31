from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsCertStoresSchedule")


@_attrs_define
class CSSCMSDataModelModelsCertStoresSchedule:
    """
    Attributes:
        store_ids (List[str]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
    """

    store_ids: List[str]
    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_ids = self.store_ids

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "storeIds": store_ids,
            }
        )
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        store_ids = cast(List[str], d.pop("storeIds"))

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        csscms_data_model_models_cert_stores_schedule = cls(
            store_ids=store_ids,
            schedule=schedule,
        )

        return csscms_data_model_models_cert_stores_schedule
