from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_agent_creation_request import (
        KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentCreationRequest,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolCreationRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolCreationRequest:
    """
    Attributes:
        name (str):
        agents (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentCreationRequest']]):
    """

    name: str
    agents: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentCreationRequest"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
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
        field_dict.update(
            {
                "name": name,
            }
        )
        if agents is not UNSET:
            field_dict["agents"] = agents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_agent_creation_request import (
            KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentCreationRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name")

        agents = []
        _agents = d.pop("agents", UNSET)
        for agents_item_data in _agents or []:
            agents_item = KeyfactorWebKeyfactorApiModelsOrchestratorPoolsAgentPoolAgentCreationRequest.from_dict(
                agents_item_data
            )

            agents.append(agents_item)

        keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_creation_request = cls(
            name=name,
            agents=agents,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_pools_agent_pool_creation_request
