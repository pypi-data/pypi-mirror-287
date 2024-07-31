from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionUpdateRequest:
    """
    Attributes:
        display_name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
    """

    display_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_definition_update_request = cls(
            display_name=display_name,
            description=description,
        )

        return keyfactor_web_keyfactor_api_models_workflows_definition_update_request
