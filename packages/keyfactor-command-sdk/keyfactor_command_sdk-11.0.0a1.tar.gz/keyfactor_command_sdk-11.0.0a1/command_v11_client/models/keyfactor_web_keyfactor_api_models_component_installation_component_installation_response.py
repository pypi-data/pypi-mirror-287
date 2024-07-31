from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsComponentInstallationComponentInstallationResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsComponentInstallationComponentInstallationResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        machine (Union[Unset, None, str]):
        version (Union[Unset, None, str]):
        components (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    machine: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET
    components: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        machine = self.machine
        version = self.version
        components = self.components

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if machine is not UNSET:
            field_dict["machine"] = machine
        if version is not UNSET:
            field_dict["version"] = version
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        machine = d.pop("machine", UNSET)

        version = d.pop("version", UNSET)

        components = d.pop("components", UNSET)

        keyfactor_web_keyfactor_api_models_component_installation_component_installation_response = cls(
            id=id,
            machine=machine,
            version=version,
            components=components,
        )

        return keyfactor_web_keyfactor_api_models_component_installation_component_installation_response
