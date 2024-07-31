from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateCollectionsAssignableQueryRole")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateCollectionsAssignableQueryRole:
    """
    Attributes:
        role_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
    """

    role_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        role_id = self.role_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        role_id = d.pop("roleId", UNSET)

        name = d.pop("name", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_collections_assignable_query_role = cls(
            role_id=role_id,
            name=name,
        )

        return keyfactor_web_keyfactor_api_models_certificate_collections_assignable_query_role
