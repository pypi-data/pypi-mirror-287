from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsAvailableSignalResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsAvailableSignalResponse:
    """
    Attributes:
        signal_name (Union[Unset, None, str]): The name of the signal.
        step_signal_id (Union[Unset, str]): The signal Id.
        signal_received (Union[Unset, bool]): Whether or not the signal has been received.
    """

    signal_name: Union[Unset, None, str] = UNSET
    step_signal_id: Union[Unset, str] = UNSET
    signal_received: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        signal_name = self.signal_name
        step_signal_id = self.step_signal_id
        signal_received = self.signal_received

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if signal_name is not UNSET:
            field_dict["signalName"] = signal_name
        if step_signal_id is not UNSET:
            field_dict["stepSignalId"] = step_signal_id
        if signal_received is not UNSET:
            field_dict["signalReceived"] = signal_received

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        signal_name = d.pop("signalName", UNSET)

        step_signal_id = d.pop("stepSignalId", UNSET)

        signal_received = d.pop("signalReceived", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_available_signal_response = cls(
            signal_name=signal_name,
            step_signal_id=step_signal_id,
            signal_received=signal_received,
        )

        return keyfactor_web_keyfactor_api_models_workflows_available_signal_response
