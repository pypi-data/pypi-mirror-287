from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.keyfactor_workflows_data_type import KeyfactorWorkflowsDataType
from ..models.keyfactor_workflows_input_control_type import KeyfactorWorkflowsInputControlType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_parameter_definition_response_depends_on import (
        KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn,
    )
    from ..models.keyfactor_web_keyfactor_api_models_workflows_parameter_definition_response_potential_values import (
        KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponse:
    """
    Attributes:
        display_name (Union[Unset, None, str]):
        parameter_type (Union[Unset, KeyfactorWorkflowsDataType]):
        required (Union[Unset, bool]):
        default_value (Union[Unset, None, str]):
        control_type (Union[Unset, KeyfactorWorkflowsInputControlType]):
        potential_values (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues]):
        support_token_replacement (Union[Unset, bool]):
        depends_on (Union[Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn]):
    """

    display_name: Union[Unset, None, str] = UNSET
    parameter_type: Union[Unset, KeyfactorWorkflowsDataType] = UNSET
    required: Union[Unset, bool] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    control_type: Union[Unset, KeyfactorWorkflowsInputControlType] = UNSET
    potential_values: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues"
    ] = UNSET
    support_token_replacement: Union[Unset, bool] = UNSET
    depends_on: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn"
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        parameter_type: Union[Unset, int] = UNSET
        if not isinstance(self.parameter_type, Unset):
            parameter_type = self.parameter_type.value

        required = self.required
        default_value = self.default_value
        control_type: Union[Unset, int] = UNSET
        if not isinstance(self.control_type, Unset):
            control_type = self.control_type.value

        potential_values: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.potential_values, Unset):
            potential_values = self.potential_values.to_dict() if self.potential_values else None

        support_token_replacement = self.support_token_replacement
        depends_on: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.depends_on, Unset):
            depends_on = self.depends_on.to_dict() if self.depends_on else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if parameter_type is not UNSET:
            field_dict["parameterType"] = parameter_type
        if required is not UNSET:
            field_dict["required"] = required
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if control_type is not UNSET:
            field_dict["controlType"] = control_type
        if potential_values is not UNSET:
            field_dict["potentialValues"] = potential_values
        if support_token_replacement is not UNSET:
            field_dict["supportTokenReplacement"] = support_token_replacement
        if depends_on is not UNSET:
            field_dict["dependsOn"] = depends_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_parameter_definition_response_depends_on import (
            KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn,
        )
        from ..models.keyfactor_web_keyfactor_api_models_workflows_parameter_definition_response_potential_values import (
            KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        display_name = d.pop("displayName", UNSET)

        _parameter_type = d.pop("parameterType", UNSET)
        parameter_type: Union[Unset, KeyfactorWorkflowsDataType]
        if isinstance(_parameter_type, Unset):
            parameter_type = UNSET
        else:
            parameter_type = KeyfactorWorkflowsDataType(_parameter_type)

        required = d.pop("required", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        _control_type = d.pop("controlType", UNSET)
        control_type: Union[Unset, KeyfactorWorkflowsInputControlType]
        if isinstance(_control_type, Unset):
            control_type = UNSET
        else:
            control_type = KeyfactorWorkflowsInputControlType(_control_type)

        _potential_values = d.pop("potentialValues", UNSET)
        potential_values: Union[
            Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues
        ]
        if _potential_values is None:
            potential_values = None
        elif isinstance(_potential_values, Unset):
            potential_values = UNSET
        else:
            potential_values = (
                KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponsePotentialValues.from_dict(
                    _potential_values
                )
            )

        support_token_replacement = d.pop("supportTokenReplacement", UNSET)

        _depends_on = d.pop("dependsOn", UNSET)
        depends_on: Union[Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn]
        if _depends_on is None:
            depends_on = None
        elif isinstance(_depends_on, Unset):
            depends_on = UNSET
        else:
            depends_on = KeyfactorWebKeyfactorApiModelsWorkflowsParameterDefinitionResponseDependsOn.from_dict(
                _depends_on
            )

        keyfactor_web_keyfactor_api_models_workflows_parameter_definition_response = cls(
            display_name=display_name,
            parameter_type=parameter_type,
            required=required,
            default_value=default_value,
            control_type=control_type,
            potential_values=potential_values,
            support_token_replacement=support_token_replacement,
            depends_on=depends_on,
        )

        return keyfactor_web_keyfactor_api_models_workflows_parameter_definition_response
