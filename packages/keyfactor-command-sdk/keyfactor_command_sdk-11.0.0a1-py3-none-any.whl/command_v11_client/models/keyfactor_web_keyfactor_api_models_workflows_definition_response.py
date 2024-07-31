from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_definition_step_response import (
        KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        display_name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        key_display_name (Union[Unset, None, str]):
        is_published (Union[Unset, bool]):
        workflow_type (Union[Unset, None, str]):
        steps (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepResponse']]):
        draft_version (Union[Unset, int]):
        published_version (Union[Unset, None, int]):
    """

    id: Union[Unset, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    key_display_name: Union[Unset, None, str] = UNSET
    is_published: Union[Unset, bool] = UNSET
    workflow_type: Union[Unset, None, str] = UNSET
    steps: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepResponse"]] = UNSET
    draft_version: Union[Unset, int] = UNSET
    published_version: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        description = self.description
        key = self.key
        key_display_name = self.key_display_name
        is_published = self.is_published
        workflow_type = self.workflow_type
        steps: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            if self.steps is None:
                steps = None
            else:
                steps = []
                for steps_item_data in self.steps:
                    steps_item = steps_item_data.to_dict()

                    steps.append(steps_item)

        draft_version = self.draft_version
        published_version = self.published_version

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if key is not UNSET:
            field_dict["key"] = key
        if key_display_name is not UNSET:
            field_dict["keyDisplayName"] = key_display_name
        if is_published is not UNSET:
            field_dict["isPublished"] = is_published
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type
        if steps is not UNSET:
            field_dict["steps"] = steps
        if draft_version is not UNSET:
            field_dict["draftVersion"] = draft_version
        if published_version is not UNSET:
            field_dict["publishedVersion"] = published_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_definition_step_response import (
            KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        key = d.pop("key", UNSET)

        key_display_name = d.pop("keyDisplayName", UNSET)

        is_published = d.pop("isPublished", UNSET)

        workflow_type = d.pop("workflowType", UNSET)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepResponse.from_dict(steps_item_data)

            steps.append(steps_item)

        draft_version = d.pop("draftVersion", UNSET)

        published_version = d.pop("publishedVersion", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_definition_response = cls(
            id=id,
            display_name=display_name,
            description=description,
            key=key,
            key_display_name=key_display_name,
            is_published=is_published,
            workflow_type=workflow_type,
            steps=steps,
            draft_version=draft_version,
            published_version=published_version,
        )

        return keyfactor_web_keyfactor_api_models_workflows_definition_response
