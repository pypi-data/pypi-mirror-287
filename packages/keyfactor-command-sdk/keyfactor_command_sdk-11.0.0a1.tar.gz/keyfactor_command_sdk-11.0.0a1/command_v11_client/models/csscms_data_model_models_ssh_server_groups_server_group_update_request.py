from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHServerGroupsServerGroupUpdateRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHServerGroupsServerGroupUpdateRequest:
    """
    Attributes:
        id (str):
        owner_name (str):
        group_name (str):
        under_management (bool):
        sync_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
    """

    id: str
    owner_name: str
    group_name: str
    under_management: bool
    sync_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        owner_name = self.owner_name
        group_name = self.group_name
        under_management = self.under_management
        sync_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sync_schedule, Unset):
            sync_schedule = self.sync_schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "ownerName": owner_name,
                "groupName": group_name,
                "underManagement": under_management,
            }
        )
        if sync_schedule is not UNSET:
            field_dict["syncSchedule"] = sync_schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        owner_name = d.pop("ownerName")

        group_name = d.pop("groupName")

        under_management = d.pop("underManagement")

        _sync_schedule = d.pop("syncSchedule", UNSET)
        sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_sync_schedule, Unset):
            sync_schedule = UNSET
        else:
            sync_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_sync_schedule)

        csscms_data_model_models_ssh_server_groups_server_group_update_request = cls(
            id=id,
            owner_name=owner_name,
            group_name=group_name,
            under_management=under_management,
            sync_schedule=sync_schedule,
        )

        return csscms_data_model_models_ssh_server_groups_server_group_update_request
