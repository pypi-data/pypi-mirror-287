from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_signal_definition_response_input_parameters import (
        KeyfactorWebKeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsSignalDefinitionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsSignalDefinitionResponse:
    """
    Attributes:
        input_parameters (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters]):
    """

    input_parameters: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters"
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        input_parameters: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.input_parameters, Unset):
            input_parameters = self.input_parameters.to_dict() if self.input_parameters else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if input_parameters is not UNSET:
            field_dict["inputParameters"] = input_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_signal_definition_response_input_parameters import (
            KeyfactorWebKeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _input_parameters = d.pop("inputParameters", UNSET)
        input_parameters: Union[
            Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters
        ]
        if _input_parameters is None:
            input_parameters = None
        elif isinstance(_input_parameters, Unset):
            input_parameters = UNSET
        else:
            input_parameters = KeyfactorWebKeyfactorApiModelsWorkflowsSignalDefinitionResponseInputParameters.from_dict(
                _input_parameters
            )

        keyfactor_web_keyfactor_api_models_workflows_signal_definition_response = cls(
            input_parameters=input_parameters,
        )

        return keyfactor_web_keyfactor_api_models_workflows_signal_definition_response
