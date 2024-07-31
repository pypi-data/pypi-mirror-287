from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest:
    """
    Attributes:
        name (str): The name of the permission set.
        permissions (List[str]): The permissions within the set.
    """

    name: str
    permissions: List[str]

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name")

        permissions = cast(List[str], d.pop("permissions"))

        keyfactor_web_keyfactor_api_models_permission_sets_permission_set_create_request = cls(
            name=name,
            permissions=permissions,
        )

        return keyfactor_web_keyfactor_api_models_permission_sets_permission_set_create_request
