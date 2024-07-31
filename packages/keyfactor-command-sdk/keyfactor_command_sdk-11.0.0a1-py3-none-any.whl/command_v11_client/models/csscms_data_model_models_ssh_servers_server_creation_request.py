from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHServersServerCreationRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHServersServerCreationRequest:
    """
    Attributes:
        agent_id (str):
        hostname (str):
        server_group_id (str):
        under_management (Union[Unset, None, bool]):
        port (Union[Unset, None, int]):
    """

    agent_id: str
    hostname: str
    server_group_id: str
    under_management: Union[Unset, None, bool] = UNSET
    port: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id
        hostname = self.hostname
        server_group_id = self.server_group_id
        under_management = self.under_management
        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "agentId": agent_id,
                "hostname": hostname,
                "serverGroupId": server_group_id,
            }
        )
        if under_management is not UNSET:
            field_dict["underManagement"] = under_management
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        agent_id = d.pop("agentId")

        hostname = d.pop("hostname")

        server_group_id = d.pop("serverGroupId")

        under_management = d.pop("underManagement", UNSET)

        port = d.pop("port", UNSET)

        csscms_data_model_models_ssh_servers_server_creation_request = cls(
            agent_id=agent_id,
            hostname=hostname,
            server_group_id=server_group_id,
            under_management=under_management,
            port=port,
        )

        return csscms_data_model_models_ssh_servers_server_creation_request
