from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestProviderTypeParam")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestProviderTypeParam:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        instance_level (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    instance_level: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        display_name = self.display_name
        instance_level = self.instance_level

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if instance_level is not UNSET:
            field_dict["instanceLevel"] = instance_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        instance_level = d.pop("instanceLevel", UNSET)

        keyfactor_web_keyfactor_api_models_pam_provider_create_request_provider_type_param = cls(
            id=id,
            name=name,
            display_name=display_name,
            instance_level=instance_level,
        )

        return keyfactor_web_keyfactor_api_models_pam_provider_create_request_provider_type_param
