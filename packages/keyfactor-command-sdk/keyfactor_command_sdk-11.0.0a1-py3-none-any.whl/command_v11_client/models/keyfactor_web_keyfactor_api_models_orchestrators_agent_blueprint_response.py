import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse:
    """
    Attributes:
        agent_blueprint_id (Union[Unset, str]):
        name (Union[Unset, None, str]):
        required_capabilities (Union[Unset, None, List[str]]):
        last_modified (Union[Unset, datetime.datetime]):
    """

    agent_blueprint_id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    required_capabilities: Union[Unset, None, List[str]] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_blueprint_id = self.agent_blueprint_id
        name = self.name
        required_capabilities: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.required_capabilities, Unset):
            if self.required_capabilities is None:
                required_capabilities = None
            else:
                required_capabilities = self.required_capabilities

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agent_blueprint_id is not UNSET:
            field_dict["agentBlueprintId"] = agent_blueprint_id
        if name is not UNSET:
            field_dict["name"] = name
        if required_capabilities is not UNSET:
            field_dict["requiredCapabilities"] = required_capabilities
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        agent_blueprint_id = d.pop("agentBlueprintId", UNSET)

        name = d.pop("name", UNSET)

        required_capabilities = cast(List[str], d.pop("requiredCapabilities", UNSET))

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        keyfactor_web_keyfactor_api_models_orchestrators_agent_blueprint_response = cls(
            agent_blueprint_id=agent_blueprint_id,
            name=name,
            required_capabilities=required_capabilities,
            last_modified=last_modified,
        )

        return keyfactor_web_keyfactor_api_models_orchestrators_agent_blueprint_response
