from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentGetResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentGetResponse:
    """
    Attributes:
        agent_id (Union[Unset, str]):
        enable_discover (Union[Unset, bool]):
        enable_monitor (Union[Unset, bool]):
        version (Union[Unset, None, str]):
        allows_discover (Union[Unset, bool]):
        allows_monitor (Union[Unset, bool]):
        client_machine (Union[Unset, None, str]):
    """

    agent_id: Union[Unset, str] = UNSET
    enable_discover: Union[Unset, bool] = UNSET
    enable_monitor: Union[Unset, bool] = UNSET
    version: Union[Unset, None, str] = UNSET
    allows_discover: Union[Unset, bool] = UNSET
    allows_monitor: Union[Unset, bool] = UNSET
    client_machine: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id
        enable_discover = self.enable_discover
        enable_monitor = self.enable_monitor
        version = self.version
        allows_discover = self.allows_discover
        allows_monitor = self.allows_monitor
        client_machine = self.client_machine

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if enable_discover is not UNSET:
            field_dict["enableDiscover"] = enable_discover
        if enable_monitor is not UNSET:
            field_dict["enableMonitor"] = enable_monitor
        if version is not UNSET:
            field_dict["version"] = version
        if allows_discover is not UNSET:
            field_dict["allowsDiscover"] = allows_discover
        if allows_monitor is not UNSET:
            field_dict["allowsMonitor"] = allows_monitor
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        agent_id = d.pop("agentId", UNSET)

        enable_discover = d.pop("enableDiscover", UNSET)

        enable_monitor = d.pop("enableMonitor", UNSET)

        version = d.pop("version", UNSET)

        allows_discover = d.pop("allowsDiscover", UNSET)

        allows_monitor = d.pop("allowsMonitor", UNSET)

        client_machine = d.pop("clientMachine", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_agent_get_response = cls(
            agent_id=agent_id,
            enable_discover=enable_discover,
            enable_monitor=enable_monitor,
            version=version,
            allows_discover=allows_discover,
            allows_monitor=allows_monitor,
            client_machine=client_machine,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_agent_get_response
