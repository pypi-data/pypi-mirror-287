from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_identity_response import (
        KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityIdentityResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse:
    """A public DTO representing a security identity's role.

    Attributes:
        name (Union[Unset, None, str]): The name of the created role
        permissions (Union[Unset, None, List[str]]): The permissions included in the created security role
        id (Union[Unset, None, int]): The Id of the created role
        description (Union[Unset, None, str]): The description of the created role
        enabled (Union[Unset, None, bool]): A boolean indicating whether or not the created role is enabled
        immutable (Union[Unset, None, bool]): A boolean indicating whther or not the security role will be read-only
        valid (Union[Unset, None, bool]): A boolean that indicates whether or not the Audit XML was able to be verified
        private (Union[Unset, None, bool]): A boolean that indicates whether or not the created security role is private
        permission_set_id (Union[Unset, str]): The Id of the permission set the role belongs to.
        identities (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityIdentityResponse']]): The identities
            assigned to the created security role
    """

    name: Union[Unset, None, str] = UNSET
    permissions: Union[Unset, None, List[str]] = UNSET
    id: Union[Unset, None, int] = UNSET
    description: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, None, bool] = UNSET
    immutable: Union[Unset, None, bool] = UNSET
    valid: Union[Unset, None, bool] = UNSET
    private: Union[Unset, None, bool] = UNSET
    permission_set_id: Union[Unset, str] = UNSET
    identities: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityIdentityResponse"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = self.permissions

        id = self.id
        description = self.description
        enabled = self.enabled
        immutable = self.immutable
        valid = self.valid
        private = self.private
        permission_set_id = self.permission_set_id
        identities: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identities, Unset):
            if self.identities is None:
                identities = None
            else:
                identities = []
                for identities_item_data in self.identities:
                    identities_item = identities_item_data.to_dict()

                    identities.append(identities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if immutable is not UNSET:
            field_dict["immutable"] = immutable
        if valid is not UNSET:
            field_dict["valid"] = valid
        if private is not UNSET:
            field_dict["private"] = private
        if permission_set_id is not UNSET:
            field_dict["permissionSetId"] = permission_set_id
        if identities is not UNSET:
            field_dict["identities"] = identities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_identity_response import (
            KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityIdentityResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name", UNSET)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        immutable = d.pop("immutable", UNSET)

        valid = d.pop("valid", UNSET)

        private = d.pop("private", UNSET)

        permission_set_id = d.pop("permissionSetId", UNSET)

        identities = []
        _identities = d.pop("identities", UNSET)
        for identities_item_data in _identities or []:
            identities_item = (
                KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityIdentityResponse.from_dict(
                    identities_item_data
                )
            )

            identities.append(identities_item)

        keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_role_response = cls(
            name=name,
            permissions=permissions,
            id=id,
            description=description,
            enabled=enabled,
            immutable=immutable,
            valid=valid,
            private=private,
            permission_set_id=permission_set_id,
            identities=identities,
        )

        return keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_role_response
