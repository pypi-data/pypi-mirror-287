from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentCreationRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentCreationRequest:
    """
    Attributes:
        agent_id (Union[Unset, str]):
        enable_discover (Union[Unset, bool]):
        enable_monitor (Union[Unset, bool]):
    """

    agent_id: Union[Unset, str] = UNSET
    enable_discover: Union[Unset, bool] = UNSET
    enable_monitor: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id
        enable_discover = self.enable_discover
        enable_monitor = self.enable_monitor

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if enable_discover is not UNSET:
            field_dict["enableDiscover"] = enable_discover
        if enable_monitor is not UNSET:
            field_dict["enableMonitor"] = enable_monitor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        agent_id = d.pop("agentId", UNSET)

        enable_discover = d.pop("enableDiscover", UNSET)

        enable_monitor = d.pop("enableMonitor", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_agent_creation_request = cls(
            agent_id=agent_id,
            enable_discover=enable_discover,
            enable_monitor=enable_monitor,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_agent_creation_request
