from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetUpdateRequest:
    """
    Attributes:
        id (str): The Id of the permission set.
        permissions (List[str]): The permissions within the set.
    """

    id: str
    permissions: List[str]

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        permissions = cast(List[str], d.pop("permissions"))

        keyfactor_web_keyfactor_api_models_permission_sets_permission_set_update_request = cls(
            id=id,
            permissions=permissions,
        )

        return keyfactor_web_keyfactor_api_models_permission_sets_permission_set_update_request
