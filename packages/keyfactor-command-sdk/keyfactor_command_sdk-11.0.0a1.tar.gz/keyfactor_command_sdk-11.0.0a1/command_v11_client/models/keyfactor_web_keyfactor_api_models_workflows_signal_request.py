from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_signal_request_data import (
        KeyfactorWebKeyfactorApiModelsWorkflowsSignalRequestData,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsSignalRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsSignalRequest:
    """
    Attributes:
        signal_key (Union[Unset, None, str]): The signal key. This is expected to be in a format like
            "STEP_NAME.SIGNAL_NAME"
        data (Union[Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsSignalRequestData]): Arbitrary data to associate
            with the signal.
    """

    signal_key: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsSignalRequestData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        signal_key = self.signal_key
        data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict() if self.data else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if signal_key is not UNSET:
            field_dict["signalKey"] = signal_key
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_signal_request_data import (
            KeyfactorWebKeyfactorApiModelsWorkflowsSignalRequestData,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        signal_key = d.pop("signalKey", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsSignalRequestData]
        if _data is None:
            data = None
        elif isinstance(_data, Unset):
            data = UNSET
        else:
            data = KeyfactorWebKeyfactorApiModelsWorkflowsSignalRequestData.from_dict(_data)

        keyfactor_web_keyfactor_api_models_workflows_signal_request = cls(
            signal_key=signal_key,
            data=data,
        )

        return keyfactor_web_keyfactor_api_models_workflows_signal_request
