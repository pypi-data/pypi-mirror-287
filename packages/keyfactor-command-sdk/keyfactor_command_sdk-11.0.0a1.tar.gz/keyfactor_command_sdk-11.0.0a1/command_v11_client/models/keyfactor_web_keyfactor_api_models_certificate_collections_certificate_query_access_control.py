from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_permissions_web_console_area_permission import CSSCMSCorePermissionsWebConsoleAreaPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateQueryAccessControl")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateQueryAccessControl:
    """
    Attributes:
        role_id (Union[Unset, int]):
        area_permissions (Union[Unset, None, List[CSSCMSCorePermissionsWebConsoleAreaPermission]]):
    """

    role_id: Union[Unset, int] = UNSET
    area_permissions: Union[Unset, None, List[CSSCMSCorePermissionsWebConsoleAreaPermission]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        role_id = self.role_id
        area_permissions: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.area_permissions, Unset):
            if self.area_permissions is None:
                area_permissions = None
            else:
                area_permissions = []
                for area_permissions_item_data in self.area_permissions:
                    area_permissions_item = area_permissions_item_data.value

                    area_permissions.append(area_permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if area_permissions is not UNSET:
            field_dict["areaPermissions"] = area_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        role_id = d.pop("roleId", UNSET)

        area_permissions = []
        _area_permissions = d.pop("areaPermissions", UNSET)
        for area_permissions_item_data in _area_permissions or []:
            area_permissions_item = CSSCMSCorePermissionsWebConsoleAreaPermission(area_permissions_item_data)

            area_permissions.append(area_permissions_item)

        keyfactor_web_keyfactor_api_models_certificate_collections_certificate_query_access_control = cls(
            role_id=role_id,
            area_permissions=area_permissions,
        )

        return keyfactor_web_keyfactor_api_models_certificate_collections_certificate_query_access_control
