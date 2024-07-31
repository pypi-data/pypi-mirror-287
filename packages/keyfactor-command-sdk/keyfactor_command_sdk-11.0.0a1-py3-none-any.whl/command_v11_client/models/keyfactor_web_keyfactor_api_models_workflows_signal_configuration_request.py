from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsSignalConfigurationRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsSignalConfigurationRequest:
    """
    Attributes:
        signal_name (Union[Unset, None, str]): The name of the signal.
        role_ids (Union[Unset, None, List[int]]): The roles that are allowed to send the signal.
    """

    signal_name: Union[Unset, None, str] = UNSET
    role_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        signal_name = self.signal_name
        role_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.role_ids, Unset):
            if self.role_ids is None:
                role_ids = None
            else:
                role_ids = self.role_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if signal_name is not UNSET:
            field_dict["signalName"] = signal_name
        if role_ids is not UNSET:
            field_dict["roleIds"] = role_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        signal_name = d.pop("signalName", UNSET)

        role_ids = cast(List[int], d.pop("roleIds", UNSET))

        keyfactor_web_keyfactor_api_models_workflows_signal_configuration_request = cls(
            signal_name=signal_name,
            role_ids=role_ids,
        )

        return keyfactor_web_keyfactor_api_models_workflows_signal_configuration_request
