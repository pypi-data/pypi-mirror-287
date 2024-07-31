from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepSignalResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepSignalResponse:
    """
    Attributes:
        role_ids (Union[Unset, None, List[int]]): The roles that are allowed to send this signal.
        signal_name (Union[Unset, None, str]):
    """

    role_ids: Union[Unset, None, List[int]] = UNSET
    signal_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        role_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.role_ids, Unset):
            if self.role_ids is None:
                role_ids = None
            else:
                role_ids = self.role_ids

        signal_name = self.signal_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if role_ids is not UNSET:
            field_dict["roleIds"] = role_ids
        if signal_name is not UNSET:
            field_dict["signalName"] = signal_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        role_ids = cast(List[int], d.pop("roleIds", UNSET))

        signal_name = d.pop("signalName", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_definition_step_signal_response = cls(
            role_ids=role_ids,
            signal_name=signal_name,
        )

        return keyfactor_web_keyfactor_api_models_workflows_definition_step_signal_response
