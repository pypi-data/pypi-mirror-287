from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_condition_configuration_request import (
        KeyfactorWebKeyfactorApiModelsWorkflowsConditionConfigurationRequest,
    )
    from ..models.keyfactor_web_keyfactor_api_models_workflows_definition_step_request_configuration_parameters import (
        KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters,
    )
    from ..models.keyfactor_web_keyfactor_api_models_workflows_definition_step_request_outputs import (
        KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs,
    )
    from ..models.keyfactor_web_keyfactor_api_models_workflows_signal_configuration_request import (
        KeyfactorWebKeyfactorApiModelsWorkflowsSignalConfigurationRequest,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest:
    """
    Attributes:
        extension_name (Union[Unset, None, str]):
        unique_name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        enabled (Union[Unset, bool]):
        configuration_parameters (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters]):
        signals (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsWorkflowsSignalConfigurationRequest']]):
        conditions (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsWorkflowsConditionConfigurationRequest']]):
        outputs (Union[Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs]):
    """

    extension_name: Union[Unset, None, str] = UNSET
    unique_name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    configuration_parameters: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters"
    ] = UNSET
    signals: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsWorkflowsSignalConfigurationRequest"]] = UNSET
    conditions: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsWorkflowsConditionConfigurationRequest"]] = UNSET
    outputs: Union[Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        extension_name = self.extension_name
        unique_name = self.unique_name
        display_name = self.display_name
        enabled = self.enabled
        configuration_parameters: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration_parameters, Unset):
            configuration_parameters = (
                self.configuration_parameters.to_dict() if self.configuration_parameters else None
            )

        signals: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.signals, Unset):
            if self.signals is None:
                signals = None
            else:
                signals = []
                for signals_item_data in self.signals:
                    signals_item = signals_item_data.to_dict()

                    signals.append(signals_item)

        conditions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            if self.conditions is None:
                conditions = None
            else:
                conditions = []
                for conditions_item_data in self.conditions:
                    conditions_item = conditions_item_data.to_dict()

                    conditions.append(conditions_item)

        outputs: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict() if self.outputs else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if extension_name is not UNSET:
            field_dict["extensionName"] = extension_name
        if unique_name is not UNSET:
            field_dict["uniqueName"] = unique_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if configuration_parameters is not UNSET:
            field_dict["configurationParameters"] = configuration_parameters
        if signals is not UNSET:
            field_dict["signals"] = signals
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if outputs is not UNSET:
            field_dict["outputs"] = outputs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_condition_configuration_request import (
            KeyfactorWebKeyfactorApiModelsWorkflowsConditionConfigurationRequest,
        )
        from ..models.keyfactor_web_keyfactor_api_models_workflows_definition_step_request_configuration_parameters import (
            KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters,
        )
        from ..models.keyfactor_web_keyfactor_api_models_workflows_definition_step_request_outputs import (
            KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs,
        )
        from ..models.keyfactor_web_keyfactor_api_models_workflows_signal_configuration_request import (
            KeyfactorWebKeyfactorApiModelsWorkflowsSignalConfigurationRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        extension_name = d.pop("extensionName", UNSET)

        unique_name = d.pop("uniqueName", UNSET)

        display_name = d.pop("displayName", UNSET)

        enabled = d.pop("enabled", UNSET)

        _configuration_parameters = d.pop("configurationParameters", UNSET)
        configuration_parameters: Union[
            Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters
        ]
        if _configuration_parameters is None:
            configuration_parameters = None
        elif isinstance(_configuration_parameters, Unset):
            configuration_parameters = UNSET
        else:
            configuration_parameters = (
                KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestConfigurationParameters.from_dict(
                    _configuration_parameters
                )
            )

        signals = []
        _signals = d.pop("signals", UNSET)
        for signals_item_data in _signals or []:
            signals_item = KeyfactorWebKeyfactorApiModelsWorkflowsSignalConfigurationRequest.from_dict(
                signals_item_data
            )

            signals.append(signals_item)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = KeyfactorWebKeyfactorApiModelsWorkflowsConditionConfigurationRequest.from_dict(
                conditions_item_data
            )

            conditions.append(conditions_item)

        _outputs = d.pop("outputs", UNSET)
        outputs: Union[Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs]
        if _outputs is None:
            outputs = None
        elif isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequestOutputs.from_dict(_outputs)

        keyfactor_web_keyfactor_api_models_workflows_definition_step_request = cls(
            extension_name=extension_name,
            unique_name=unique_name,
            display_name=display_name,
            enabled=enabled,
            configuration_parameters=configuration_parameters,
            signals=signals,
            conditions=conditions,
            outputs=outputs,
        )

        return keyfactor_web_keyfactor_api_models_workflows_definition_step_request
