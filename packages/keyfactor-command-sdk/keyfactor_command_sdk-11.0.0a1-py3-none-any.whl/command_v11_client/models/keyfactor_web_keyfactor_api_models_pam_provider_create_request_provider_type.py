from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestProviderType")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestProviderType:
    """
    Attributes:
        id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        keyfactor_web_keyfactor_api_models_pam_provider_create_request_provider_type = cls(
            id=id,
        )

        return keyfactor_web_keyfactor_api_models_pam_provider_create_request_provider_type
