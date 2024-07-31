from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
        CSSCMSDataModelModelsSSHUsersSshUserResponse,
    )
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHServersServerResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHServersServerResponse:
    """
    Attributes:
        id (Union[Unset, None, int]):
        agent_id (Union[Unset, None, str]):
        hostname (Union[Unset, None, str]):
        server_group_id (Union[Unset, None, str]):
        sync_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        under_management (Union[Unset, bool]):
        owner (Union[Unset, CSSCMSDataModelModelsSSHUsersSshUserResponse]):
        group_name (Union[Unset, None, str]):
        orchestrator (Union[Unset, None, str]):
        port (Union[Unset, None, int]):
    """

    id: Union[Unset, None, int] = UNSET
    agent_id: Union[Unset, None, str] = UNSET
    hostname: Union[Unset, None, str] = UNSET
    server_group_id: Union[Unset, None, str] = UNSET
    sync_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    under_management: Union[Unset, bool] = UNSET
    owner: Union[Unset, "CSSCMSDataModelModelsSSHUsersSshUserResponse"] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    orchestrator: Union[Unset, None, str] = UNSET
    port: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        agent_id = self.agent_id
        hostname = self.hostname
        server_group_id = self.server_group_id
        sync_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sync_schedule, Unset):
            sync_schedule = self.sync_schedule.to_dict()

        under_management = self.under_management
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        group_name = self.group_name
        orchestrator = self.orchestrator
        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if server_group_id is not UNSET:
            field_dict["serverGroupId"] = server_group_id
        if sync_schedule is not UNSET:
            field_dict["syncSchedule"] = sync_schedule
        if under_management is not UNSET:
            field_dict["underManagement"] = under_management
        if owner is not UNSET:
            field_dict["owner"] = owner
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if orchestrator is not UNSET:
            field_dict["orchestrator"] = orchestrator
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
            CSSCMSDataModelModelsSSHUsersSshUserResponse,
        )
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        agent_id = d.pop("agentId", UNSET)

        hostname = d.pop("hostname", UNSET)

        server_group_id = d.pop("serverGroupId", UNSET)

        _sync_schedule = d.pop("syncSchedule", UNSET)
        sync_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_sync_schedule, Unset):
            sync_schedule = UNSET
        else:
            sync_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_sync_schedule)

        under_management = d.pop("underManagement", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, CSSCMSDataModelModelsSSHUsersSshUserResponse]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = CSSCMSDataModelModelsSSHUsersSshUserResponse.from_dict(_owner)

        group_name = d.pop("groupName", UNSET)

        orchestrator = d.pop("orchestrator", UNSET)

        port = d.pop("port", UNSET)

        csscms_data_model_models_ssh_servers_server_response = cls(
            id=id,
            agent_id=agent_id,
            hostname=hostname,
            server_group_id=server_group_id,
            sync_schedule=sync_schedule,
            under_management=under_management,
            owner=owner,
            group_name=group_name,
            orchestrator=orchestrator,
            port=port,
        )

        return csscms_data_model_models_ssh_servers_server_response
