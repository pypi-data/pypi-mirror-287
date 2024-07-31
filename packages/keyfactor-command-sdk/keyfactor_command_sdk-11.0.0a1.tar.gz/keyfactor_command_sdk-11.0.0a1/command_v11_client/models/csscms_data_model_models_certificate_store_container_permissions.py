from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreContainerPermissions")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreContainerPermissions:
    """
    Attributes:
        security_role_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        permissions (Union[Unset, None, List[str]]):
    """

    security_role_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    permissions: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        security_role_id = self.security_role_id
        name = self.name
        permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if security_role_id is not UNSET:
            field_dict["securityRoleId"] = security_role_id
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        security_role_id = d.pop("securityRoleId", UNSET)

        name = d.pop("name", UNSET)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        csscms_data_model_models_certificate_store_container_permissions = cls(
            security_role_id=security_role_id,
            name=name,
            permissions=permissions,
        )

        return csscms_data_model_models_certificate_store_container_permissions
