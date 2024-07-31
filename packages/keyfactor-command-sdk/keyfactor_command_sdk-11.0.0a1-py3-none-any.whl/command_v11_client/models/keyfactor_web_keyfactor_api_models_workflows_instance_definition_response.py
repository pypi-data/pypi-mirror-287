from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        display_name (Union[Unset, None, str]):
        version (Union[Unset, int]):
        workflow_type (Union[Unset, None, str]):
    """

    id: Union[Unset, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    version: Union[Unset, int] = UNSET
    workflow_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        version = self.version
        workflow_type = self.workflow_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if version is not UNSET:
            field_dict["version"] = version
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        version = d.pop("version", UNSET)

        workflow_type = d.pop("workflowType", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_instance_definition_response = cls(
            id=id,
            display_name=display_name,
            version=version,
            workflow_type=workflow_type,
        )

        return keyfactor_web_keyfactor_api_models_workflows_instance_definition_response
