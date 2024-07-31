from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionCreateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionCreateRequest:
    """
    Attributes:
        display_name (Union[Unset, None, str]): Display name of the Definition
        description (Union[Unset, None, str]): Description of the Definition
        key (Union[Unset, None, str]): Key to be used to look up definition when starting a new workflow.
            For enrollment workflowTypes, this should be a template
        workflow_type (Union[Unset, None, str]): The Type of Workflow
    """

    display_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    workflow_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        description = self.description
        key = self.key
        workflow_type = self.workflow_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if key is not UNSET:
            field_dict["key"] = key
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        key = d.pop("key", UNSET)

        workflow_type = d.pop("workflowType", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_definition_create_request = cls(
            display_name=display_name,
            description=description,
            key=key,
            workflow_type=workflow_type,
        )

        return keyfactor_web_keyfactor_api_models_workflows_definition_create_request
