from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_agent_get_response import (
        KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentGetResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolGetResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolGetResponse:
    """
    Attributes:
        agent_pool_id (Union[Unset, str]):
        name (Union[Unset, None, str]):
        discover_agents_count (Union[Unset, int]):
        monitor_agents_count (Union[Unset, int]):
        agents (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentGetResponse']]):
    """

    agent_pool_id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    discover_agents_count: Union[Unset, int] = UNSET
    monitor_agents_count: Union[Unset, int] = UNSET
    agents: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentGetResponse"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_pool_id = self.agent_pool_id
        name = self.name
        discover_agents_count = self.discover_agents_count
        monitor_agents_count = self.monitor_agents_count
        agents: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.agents, Unset):
            if self.agents is None:
                agents = None
            else:
                agents = []
                for agents_item_data in self.agents:
                    agents_item = agents_item_data.to_dict()

                    agents.append(agents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agent_pool_id is not UNSET:
            field_dict["agentPoolId"] = agent_pool_id
        if name is not UNSET:
            field_dict["name"] = name
        if discover_agents_count is not UNSET:
            field_dict["discoverAgentsCount"] = discover_agents_count
        if monitor_agents_count is not UNSET:
            field_dict["monitorAgentsCount"] = monitor_agents_count
        if agents is not UNSET:
            field_dict["agents"] = agents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_agent_get_response import (
            KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentGetResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        agent_pool_id = d.pop("agentPoolId", UNSET)

        name = d.pop("name", UNSET)

        discover_agents_count = d.pop("discoverAgentsCount", UNSET)

        monitor_agents_count = d.pop("monitorAgentsCount", UNSET)

        agents = []
        _agents = d.pop("agents", UNSET)
        for agents_item_data in _agents or []:
            agents_item = KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentGetResponse.from_dict(
                agents_item_data
            )

            agents.append(agents_item)

        keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_get_response = cls(
            agent_pool_id=agent_pool_id,
            name=name,
            discover_agents_count=discover_agents_count,
            monitor_agents_count=monitor_agents_count,
            agents=agents,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_get_response
