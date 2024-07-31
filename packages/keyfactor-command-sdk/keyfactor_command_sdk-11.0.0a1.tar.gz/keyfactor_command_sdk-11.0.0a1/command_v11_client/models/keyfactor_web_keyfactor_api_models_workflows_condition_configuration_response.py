from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsConditionConfigurationResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsConditionConfigurationResponse:
    """Information about the configuration of a workflow condition.

    Attributes:
        id (Union[Unset, str]): The Id of the condition.
        value (Union[Unset, None, str]): The value to compare to. This value will be compared to a true value.
    """

    id: Union[Unset, str] = UNSET
    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_condition_configuration_response = cls(
            id=id,
            value=value,
        )

        return keyfactor_web_keyfactor_api_models_workflows_condition_configuration_response
