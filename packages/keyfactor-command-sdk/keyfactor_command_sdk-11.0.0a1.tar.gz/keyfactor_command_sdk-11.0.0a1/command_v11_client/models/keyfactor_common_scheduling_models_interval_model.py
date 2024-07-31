from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorCommonSchedulingModelsIntervalModel")


@_attrs_define
class KeyfactorCommonSchedulingModelsIntervalModel:
    """
    Attributes:
        minutes (Union[Unset, int]):
    """

    minutes: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        minutes = self.minutes

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if minutes is not UNSET:
            field_dict["minutes"] = minutes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        minutes = d.pop("minutes", UNSET)

        keyfactor_common_scheduling_models_interval_model = cls(
            minutes=minutes,
        )

        return keyfactor_common_scheduling_models_interval_model
