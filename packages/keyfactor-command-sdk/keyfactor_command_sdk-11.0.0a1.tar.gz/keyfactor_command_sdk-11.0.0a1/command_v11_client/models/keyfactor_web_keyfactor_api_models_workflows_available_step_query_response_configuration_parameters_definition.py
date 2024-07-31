from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_parameter_definition_response import (
        KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponse,
    )


T = TypeVar(
    "T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition"
)


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition:
    """ """

    additional_properties: Dict[
        str, "KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponse"
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_parameter_definition_response import (
            KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        keyfactor_web_keyfactor_api_models_workflows_available_step_query_response_configuration_parameters_definition = (
            cls()
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponse.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        keyfactor_web_keyfactor_api_models_workflows_available_step_query_response_configuration_parameters_definition.additional_properties = (
            additional_properties
        )
        return keyfactor_web_keyfactor_api_models_workflows_available_step_query_response_configuration_parameters_definition

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponse":
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: "KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponse"
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
