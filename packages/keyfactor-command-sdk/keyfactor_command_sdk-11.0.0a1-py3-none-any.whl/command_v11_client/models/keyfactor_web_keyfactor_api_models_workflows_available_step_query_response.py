from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_query_response_configuration_parameters_definition import (
        KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition,
    )
    from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_query_response_signals_definition import (
        KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponse:
    """
    Attributes:
        display_name (Union[Unset, None, str]): The display name of the step.
        extension_name (Union[Unset, None, str]): The extension name of the step.
        supported_workflow_types (Union[Unset, None, List[str]]): The workflow types which this step can be a part of.
        configuration_parameters_definition (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition]):
        signals_definition (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition]):
    """

    display_name: Union[Unset, None, str] = UNSET
    extension_name: Union[Unset, None, str] = UNSET
    supported_workflow_types: Union[Unset, None, List[str]] = UNSET
    configuration_parameters_definition: Union[
        Unset,
        None,
        "KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition",
    ] = UNSET
    signals_definition: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition"
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        extension_name = self.extension_name
        supported_workflow_types: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.supported_workflow_types, Unset):
            if self.supported_workflow_types is None:
                supported_workflow_types = None
            else:
                supported_workflow_types = self.supported_workflow_types

        configuration_parameters_definition: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration_parameters_definition, Unset):
            configuration_parameters_definition = (
                self.configuration_parameters_definition.to_dict() if self.configuration_parameters_definition else None
            )

        signals_definition: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.signals_definition, Unset):
            signals_definition = self.signals_definition.to_dict() if self.signals_definition else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if extension_name is not UNSET:
            field_dict["extensionName"] = extension_name
        if supported_workflow_types is not UNSET:
            field_dict["supportedWorkflowTypes"] = supported_workflow_types
        if configuration_parameters_definition is not UNSET:
            field_dict["configurationParametersDefinition"] = configuration_parameters_definition
        if signals_definition is not UNSET:
            field_dict["signalsDefinition"] = signals_definition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_query_response_configuration_parameters_definition import (
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition,
        )
        from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_query_response_signals_definition import (
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        display_name = d.pop("displayName", UNSET)

        extension_name = d.pop("extensionName", UNSET)

        supported_workflow_types = cast(List[str], d.pop("supportedWorkflowTypes", UNSET))

        _configuration_parameters_definition = d.pop("configurationParametersDefinition", UNSET)
        configuration_parameters_definition: Union[
            Unset,
            None,
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition,
        ]
        if _configuration_parameters_definition is None:
            configuration_parameters_definition = None
        elif isinstance(_configuration_parameters_definition, Unset):
            configuration_parameters_definition = UNSET
        else:
            configuration_parameters_definition = KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseConfigurationParametersDefinition.from_dict(
                _configuration_parameters_definition
            )

        _signals_definition = d.pop("signalsDefinition", UNSET)
        signals_definition: Union[
            Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition
        ]
        if _signals_definition is None:
            signals_definition = None
        elif isinstance(_signals_definition, Unset):
            signals_definition = UNSET
        else:
            signals_definition = (
                KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepQueryResponseSignalsDefinition.from_dict(
                    _signals_definition
                )
            )

        keyfactor_web_keyfactor_api_models_workflows_available_step_query_response = cls(
            display_name=display_name,
            extension_name=extension_name,
            supported_workflow_types=supported_workflow_types,
            configuration_parameters_definition=configuration_parameters_definition,
            signals_definition=signals_definition,
        )

        return keyfactor_web_keyfactor_api_models_workflows_available_step_query_response
