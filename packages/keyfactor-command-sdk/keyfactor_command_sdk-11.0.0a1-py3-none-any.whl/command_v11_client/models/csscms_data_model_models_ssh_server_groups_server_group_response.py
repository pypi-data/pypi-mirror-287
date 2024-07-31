from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
        CSSCMSDataModelModelsSSHUsersSshUserResponse,
    )
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHServerGroupsServerGroupResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHServerGroupsServerGroupResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        owner (Union[Unset, CSSCMSDataModelModelsSSHUsersSshUserResponse]):
        group_name (Union[Unset, None, str]):
        sync_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        under_management (Union[Unset, bool]):
        server_count (Union[Unset, None, int]):
    """

    id: Union[Unset, str] = UNSET
    owner: Union[Unset, "CSSCMSDataModelModelsSSHUsersSshUserResponse"] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    sync_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    under_management: Union[Unset, bool] = UNSET
    server_count: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        group_name = self.group_name
        sync_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sync_schedule, Unset):
            sync_schedule = self.sync_schedule.to_dict()

        under_management = self.under_management
        server_count = self.server_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if owner is not UNSET:
            field_dict["owner"] = owner
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if sync_schedule is not UNSET:
            field_dict["syncSchedule"] = sync_schedule
        if under_management is not UNSET:
            field_dict["underManagement"] = under_management
        if server_count is not UNSET:
            field_dict["serverCount"] = server_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
            CSSCMSDataModelModelsSSHUsersSshUserResponse,
        )
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, CSSCMSDataModelModelsSSHUsersSshUserResponse]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = CSSCMSDataModelModelsSSHUsersSshUserResponse.from_dict(_owner)

        group_name = d.pop("groupName", UNSET)

        _sync_schedule = d.pop("syncSchedule", UNSET)
        sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_sync_schedule, Unset):
            sync_schedule = UNSET
        else:
            sync_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_sync_schedule)

        under_management = d.pop("underManagement", UNSET)

        server_count = d.pop("serverCount", UNSET)

        csscms_data_model_models_ssh_server_groups_server_group_response = cls(
            id=id,
            owner=owner,
            group_name=group_name,
            sync_schedule=sync_schedule,
            under_management=under_management,
            server_count=server_count,
        )

        return csscms_data_model_models_ssh_server_groups_server_group_response
