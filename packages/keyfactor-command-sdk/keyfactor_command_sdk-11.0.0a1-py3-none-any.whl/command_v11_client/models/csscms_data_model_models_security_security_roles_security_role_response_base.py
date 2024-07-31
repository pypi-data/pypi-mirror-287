from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSecuritySecurityRolesSecurityRoleResponseBase")


@_attrs_define
class CSSCMSDataModelModelsSecuritySecurityRolesSecurityRoleResponseBase:
    """
    Attributes:
        name (Union[Unset, None, str]):
        permissions (Union[Unset, None, List[str]]):
    """

    name: Union[Unset, None, str] = UNSET
    permissions: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name", UNSET)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        csscms_data_model_models_security_security_roles_security_role_response_base = cls(
            name=name,
            permissions=permissions,
        )

        return csscms_data_model_models_security_security_roles_security_role_response_base
