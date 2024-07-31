from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_response import (
        KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsWorkflowTypeQueryResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsWorkflowTypeQueryResponse:
    """
    Attributes:
        workflow_type (Union[Unset, None, str]):
        key_type (Union[Unset, None, str]):
        context_parameters (Union[Unset, None, List[str]]):
        built_in_steps (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponse']]):
    """

    workflow_type: Union[Unset, None, str] = UNSET
    key_type: Union[Unset, None, str] = UNSET
    context_parameters: Union[Unset, None, List[str]] = UNSET
    built_in_steps: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponse"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        workflow_type = self.workflow_type
        key_type = self.key_type
        context_parameters: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.context_parameters, Unset):
            if self.context_parameters is None:
                context_parameters = None
            else:
                context_parameters = self.context_parameters

        built_in_steps: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.built_in_steps, Unset):
            if self.built_in_steps is None:
                built_in_steps = None
            else:
                built_in_steps = []
                for built_in_steps_item_data in self.built_in_steps:
                    built_in_steps_item = built_in_steps_item_data.to_dict()

                    built_in_steps.append(built_in_steps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if workflow_type is not UNSET:
            field_dict["workflowType"] = workflow_type
        if key_type is not UNSET:
            field_dict["keyType"] = key_type
        if context_parameters is not UNSET:
            field_dict["contextParameters"] = context_parameters
        if built_in_steps is not UNSET:
            field_dict["builtInSteps"] = built_in_steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_available_step_response import (
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        workflow_type = d.pop("workflowType", UNSET)

        key_type = d.pop("keyType", UNSET)

        context_parameters = cast(List[str], d.pop("contextParameters", UNSET))

        built_in_steps = []
        _built_in_steps = d.pop("builtInSteps", UNSET)
        for built_in_steps_item_data in _built_in_steps or []:
            built_in_steps_item = KeyfactorWebKeyfactorApiModelsWorkflowsAvailableStepResponse.from_dict(
                built_in_steps_item_data
            )

            built_in_steps.append(built_in_steps_item)

        keyfactor_web_keyfactor_api_models_workflows_workflow_type_query_response = cls(
            workflow_type=workflow_type,
            key_type=key_type,
            context_parameters=context_parameters,
            built_in_steps=built_in_steps,
        )

        return keyfactor_web_keyfactor_api_models_workflows_workflow_type_query_response
