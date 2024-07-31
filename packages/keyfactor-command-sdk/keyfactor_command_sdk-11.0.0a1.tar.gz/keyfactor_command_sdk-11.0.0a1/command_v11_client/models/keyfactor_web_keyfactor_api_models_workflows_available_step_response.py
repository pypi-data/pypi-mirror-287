from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_response_configuration_parameters_definition import (
        KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition,
    )
    from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_response_signals_definition import (
        KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponse:
    """
    Attributes:
        display_name (Union[Unset, None, str]): The display name of the step.
        extension_name (Union[Unset, None, str]): The name of the extension.
        outputs (Union[Unset, None, List[str]]): The possible outputs of the step.
        configuration_parameters_definition (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition]):
        signals_definition (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition]):
    """

    display_name: Union[Unset, None, str] = UNSET
    extension_name: Union[Unset, None, str] = UNSET
    outputs: Union[Unset, None, List[str]] = UNSET
    configuration_parameters_definition: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition"
    ] = UNSET
    signals_definition: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition"
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        extension_name = self.extension_name
        outputs: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.outputs, Unset):
            if self.outputs is None:
                outputs = None
            else:
                outputs = self.outputs

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
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if configuration_parameters_definition is not UNSET:
            field_dict["configurationParametersDefinition"] = configuration_parameters_definition
        if signals_definition is not UNSET:
            field_dict["signalsDefinition"] = signals_definition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_response_configuration_parameters_definition import (
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition,
        )
        from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_response_signals_definition import (
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        display_name = d.pop("displayName", UNSET)

        extension_name = d.pop("extensionName", UNSET)

        outputs = cast(List[str], d.pop("outputs", UNSET))

        _configuration_parameters_definition = d.pop("configurationParametersDefinition", UNSET)
        configuration_parameters_definition: Union[
            Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition
        ]
        if _configuration_parameters_definition is None:
            configuration_parameters_definition = None
        elif isinstance(_configuration_parameters_definition, Unset):
            configuration_parameters_definition = UNSET
        else:
            configuration_parameters_definition = (
                KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseConfigurationParametersDefinition.from_dict(
                    _configuration_parameters_definition
                )
            )

        _signals_definition = d.pop("signalsDefinition", UNSET)
        signals_definition: Union[
            Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition
        ]
        if _signals_definition is None:
            signals_definition = None
        elif isinstance(_signals_definition, Unset):
            signals_definition = UNSET
        else:
            signals_definition = (
                KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponseSignalsDefinition.from_dict(
                    _signals_definition
                )
            )

        keyfactor_web_keyfactor_api_models_workflows_available_step_response = cls(
            display_name=display_name,
            extension_name=extension_name,
            outputs=outputs,
            configuration_parameters_definition=configuration_parameters_definition,
            signals_definition=signals_definition,
        )

        return keyfactor_web_keyfactor_api_models_workflows_available_step_response
