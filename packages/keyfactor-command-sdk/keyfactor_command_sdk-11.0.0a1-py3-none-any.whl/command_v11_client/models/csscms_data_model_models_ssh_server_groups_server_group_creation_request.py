from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHServerGroupsServerGroupCreationRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHServerGroupsServerGroupCreationRequest:
    """
    Attributes:
        owner_name (str):
        group_name (str):
        sync_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        under_management (Union[Unset, bool]):
    """

    owner_name: str
    group_name: str
    sync_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    under_management: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        owner_name = self.owner_name
        group_name = self.group_name
        sync_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sync_schedule, Unset):
            sync_schedule = self.sync_schedule.to_dict()

        under_management = self.under_management

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "ownerName": owner_name,
                "groupName": group_name,
            }
        )
        if sync_schedule is not UNSET:
            field_dict["syncSchedule"] = sync_schedule
        if under_management is not UNSET:
            field_dict["underManagement"] = under_management

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        owner_name = d.pop("ownerName")

        group_name = d.pop("groupName")

        _sync_schedule = d.pop("syncSchedule", UNSET)
        sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_sync_schedule, Unset):
            sync_schedule = UNSET
        else:
            sync_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_sync_schedule)

        under_management = d.pop("underManagement", UNSET)

        csscms_data_model_models_ssh_server_groups_server_group_creation_request = cls(
            owner_name=owner_name,
            group_name=group_name,
            sync_schedule=sync_schedule,
            under_management=under_management,
        )

        return csscms_data_model_models_ssh_server_groups_server_group_creation_request
