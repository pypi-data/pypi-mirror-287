from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_security_security_roles_security_role_response_base import (
        CSSCMSDataModelModelsSecuritySecurityRolesSecurityRoleResponseBase,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSecurityCertificatePermissions")


@_attrs_define
class CSSCMSDataModelModelsSecurityCertificatePermissions:
    """
    Attributes:
        roles (Union[Unset, None, List['CSSCMSDataModelModelsSecuritySecurityRolesSecurityRoleResponseBase']]):
    """

    roles: Union[Unset, None, List["CSSCMSDataModelModelsSecuritySecurityRolesSecurityRoleResponseBase"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        roles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            if self.roles is None:
                roles = None
            else:
                roles = []
                for roles_item_data in self.roles:
                    roles_item = roles_item_data.to_dict()

                    roles.append(roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_security_security_roles_security_role_response_base import (
            CSSCMSDataModelModelsSecuritySecurityRolesSecurityRoleResponseBase,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = CSSCMSDataModelModelsSecuritySecurityRolesSecurityRoleResponseBase.from_dict(roles_item_data)

            roles.append(roles_item)

        csscms_data_model_models_security_certificate_permissions = cls(
            roles=roles,
        )

        return csscms_data_model_models_security_certificate_permissions
