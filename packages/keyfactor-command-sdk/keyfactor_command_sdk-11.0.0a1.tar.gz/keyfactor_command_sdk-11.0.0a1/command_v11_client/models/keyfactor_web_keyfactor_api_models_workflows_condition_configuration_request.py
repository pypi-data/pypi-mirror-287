from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsConditionConfigurationRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsConditionConfigurationRequest:
    """Information about the configuration of a workflow condition.

    Attributes:
        value (Union[Unset, None, str]): The value to compare to true when evaluating conditions.
    """

    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        value = d.pop("value", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_condition_configuration_request = cls(
            value=value,
        )

        return keyfactor_web_keyfactor_api_models_workflows_condition_configuration_request
