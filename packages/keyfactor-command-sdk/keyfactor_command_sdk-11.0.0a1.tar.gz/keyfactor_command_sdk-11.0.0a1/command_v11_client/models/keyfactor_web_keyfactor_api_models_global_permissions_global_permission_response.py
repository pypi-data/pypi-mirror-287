from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsGlobalPermissionsGlobalPermissionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsGlobalPermissionsGlobalPermissionResponse:
    """
    Attributes:
        area (Union[Unset, None, str]):
        permission (Union[Unset, None, str]):
    """

    area: Union[Unset, None, str] = UNSET
    permission: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        area = self.area
        permission = self.permission

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        area = d.pop("area", UNSET)

        permission = d.pop("permission", UNSET)

        keyfactor_web_keyfactor_api_models_global_permissions_global_permission_response = cls(
            area=area,
            permission=permission,
        )

        return keyfactor_web_keyfactor_api_models_global_permissions_global_permission_response
