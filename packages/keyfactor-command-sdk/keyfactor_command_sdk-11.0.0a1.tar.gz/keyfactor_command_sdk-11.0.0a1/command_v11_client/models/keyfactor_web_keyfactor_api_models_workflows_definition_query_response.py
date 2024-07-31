from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionQueryResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionQueryResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        display_name (Union[Unset, None, str]):
        key (Union[Unset, None, str]):
        key_display_name (Union[Unset, None, str]):
        workflow_type (Union[Unset, None, str]):
        draft_version (Union[Unset, int]):
        published_version (Union[Unset, None, int]):
    """

    id: Union[Unset, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    key: Union[Unset, None, str] = UNSET
    key_display_name: Union[Unset, None, str] = UNSET
    workflow_type: Union[Unset, None, str] = UNSET
    draft_version: Union[Unset, int] = UNSET
    published_version: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        key = self.key
        key_display_name = self.key_display_name
        workflow_type = self.workflow_type
        draft_version = self.draft_version
        published_version = self.published_version

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if key is not UNSET:
            field_dict["key"] = key
        if key_display_name is not UNSET:
            field_dict["keyDisplayName"] = key_display_name
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type
        if draft_version is not UNSET:
            field_dict["draftVersion"] = draft_version
        if published_version is not UNSET:
            field_dict["publishedVersion"] = published_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        key = d.pop("key", UNSET)

        key_display_name = d.pop("keyDisplayName", UNSET)

        workflow_type = d.pop("workflowType", UNSET)

        draft_version = d.pop("draftVersion", UNSET)

        published_version = d.pop("publishedVersion", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_definition_query_response = cls(
            id=id,
            display_name=display_name,
            key=key,
            key_display_name=key_display_name,
            workflow_type=workflow_type,
            draft_version=draft_version,
            published_version=published_version,
        )

        return keyfactor_web_keyfactor_api_models_workflows_definition_query_response
