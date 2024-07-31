from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_security_identities_security_identity_identifier import (
        CSSCMSDataModelModelsSecurityIdentitiesSecurityIdentityIdentifier,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleCreationRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleCreationRequest:
    """
    Attributes:
        name (str): The name of the security role to create
        description (str): The description to be used on the created security role
        enabled (Union[Unset, bool]): Whether or not the security role should be enabled
        private (Union[Unset, bool]): Whether or not the security role should be private
        permissions (Union[Unset, None, List[str]]): The permissions to include in the role. These must be supplied in
            the format "Area:Permission"
        permission_set_id (Union[Unset, str]): The Id of the permission set the role belongs to.
        identities (Union[Unset, None, List['CSSCMSDataModelModelsSecurityIdentitiesSecurityIdentityIdentifier']]): The
            Keyfactor identities to assign to the created role
    """

    name: str
    description: str
    enabled: Union[Unset, bool] = UNSET
    private: Union[Unset, bool] = UNSET
    permissions: Union[Unset, None, List[str]] = UNSET
    permission_set_id: Union[Unset, str] = UNSET
    identities: Union[Unset, None, List["CSSCMSDataModelModelsSecurityIdentitiesSecurityIdentityIdentifier"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        enabled = self.enabled
        private = self.private
        permissions: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = self.permissions

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
        field_dict.update(
            {
                "name": name,
                "description": description,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if private is not UNSET:
            field_dict["private"] = private
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if permission_set_id is not UNSET:
            field_dict["permissionSetId"] = permission_set_id
        if identities is not UNSET:
            field_dict["identities"] = identities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_security_identities_security_identity_identifier import (
            CSSCMSDataModelModelsSecurityIdentitiesSecurityIdentityIdentifier,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name")

        description = d.pop("description")

        enabled = d.pop("enabled", UNSET)

        private = d.pop("private", UNSET)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        permission_set_id = d.pop("permissionSetId", UNSET)

        identities = []
        _identities = d.pop("identities", UNSET)
        for identities_item_data in _identities or []:
            identities_item = CSSCMSDataModelModelsSecurityIdentitiesSecurityIdentityIdentifier.from_dict(
                identities_item_data
            )

            identities.append(identities_item)

        keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_role_creation_request = cls(
            name=name,
            description=description,
            enabled=enabled,
            private=private,
            permissions=permissions,
            permission_set_id=permission_set_id,
            identities=identities,
        )

        return keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_role_creation_request
