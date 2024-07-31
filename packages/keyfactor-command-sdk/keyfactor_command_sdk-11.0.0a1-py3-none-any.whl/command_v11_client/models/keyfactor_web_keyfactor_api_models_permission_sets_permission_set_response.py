from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse:
    """
    Attributes:
        id (Union[Unset, str]): The Id of the permission set.
        name (Union[Unset, None, str]): The name of the permission set.
        permissions (Union[Unset, None, List[str]]): The permissions within the set.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    permissions: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        keyfactor_web_keyfactor_api_models_permission_sets_permission_set_response = cls(
            id=id,
            name=name,
            permissions=permissions,
        )

        return keyfactor_web_keyfactor_api_models_permission_sets_permission_set_response
