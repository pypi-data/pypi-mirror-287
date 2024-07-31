from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_response import (
        KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_security_security_identity_permissions_permission_roles_pair_response import (
        KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse,
    )


T = TypeVar(
    "T", bound="KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsSecurityIdentityPermissionsResponse"
)


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsSecurityIdentityPermissionsResponse:
    """
    Attributes:
        claim (Union[Unset, KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionResponse]):
        identity (Union[Unset, None, str]):
        secured_area_permissions (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse']]):
        collection_permissions (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse']]):
        container_permissions (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse']]):
        pam_provider_permissions (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse']]):
        identity_provider_permissions (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse']]):
        pam_permissions (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse']]):
    """

    claim: Union[Unset, "KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionResponse"] = UNSET
    identity: Union[Unset, None, str] = UNSET
    secured_area_permissions: Union[
        Unset,
        None,
        List["KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse"],
    ] = UNSET
    collection_permissions: Union[
        Unset,
        None,
        List["KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse"],
    ] = UNSET
    container_permissions: Union[
        Unset,
        None,
        List["KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse"],
    ] = UNSET
    pam_provider_permissions: Union[
        Unset,
        None,
        List["KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse"],
    ] = UNSET
    identity_provider_permissions: Union[
        Unset,
        None,
        List["KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse"],
    ] = UNSET
    pam_permissions: Union[
        Unset,
        None,
        List["KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse"],
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        claim: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.claim, Unset):
            claim = self.claim.to_dict()

        identity = self.identity
        secured_area_permissions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.secured_area_permissions, Unset):
            if self.secured_area_permissions is None:
                secured_area_permissions = None
            else:
                secured_area_permissions = []
                for secured_area_permissions_item_data in self.secured_area_permissions:
                    secured_area_permissions_item = secured_area_permissions_item_data.to_dict()

                    secured_area_permissions.append(secured_area_permissions_item)

        collection_permissions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.collection_permissions, Unset):
            if self.collection_permissions is None:
                collection_permissions = None
            else:
                collection_permissions = []
                for collection_permissions_item_data in self.collection_permissions:
                    collection_permissions_item = collection_permissions_item_data.to_dict()

                    collection_permissions.append(collection_permissions_item)

        container_permissions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.container_permissions, Unset):
            if self.container_permissions is None:
                container_permissions = None
            else:
                container_permissions = []
                for container_permissions_item_data in self.container_permissions:
                    container_permissions_item = container_permissions_item_data.to_dict()

                    container_permissions.append(container_permissions_item)

        pam_provider_permissions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pam_provider_permissions, Unset):
            if self.pam_provider_permissions is None:
                pam_provider_permissions = None
            else:
                pam_provider_permissions = []
                for pam_provider_permissions_item_data in self.pam_provider_permissions:
                    pam_provider_permissions_item = pam_provider_permissions_item_data.to_dict()

                    pam_provider_permissions.append(pam_provider_permissions_item)

        identity_provider_permissions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identity_provider_permissions, Unset):
            if self.identity_provider_permissions is None:
                identity_provider_permissions = None
            else:
                identity_provider_permissions = []
                for identity_provider_permissions_item_data in self.identity_provider_permissions:
                    identity_provider_permissions_item = identity_provider_permissions_item_data.to_dict()

                    identity_provider_permissions.append(identity_provider_permissions_item)

        pam_permissions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pam_permissions, Unset):
            if self.pam_permissions is None:
                pam_permissions = None
            else:
                pam_permissions = []
                for pam_permissions_item_data in self.pam_permissions:
                    pam_permissions_item = pam_permissions_item_data.to_dict()

                    pam_permissions.append(pam_permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if claim is not UNSET:
            field_dict["claim"] = claim
        if identity is not UNSET:
            field_dict["identity"] = identity
        if secured_area_permissions is not UNSET:
            field_dict["securedAreaPermissions"] = secured_area_permissions
        if collection_permissions is not UNSET:
            field_dict["collectionPermissions"] = collection_permissions
        if container_permissions is not UNSET:
            field_dict["containerPermissions"] = container_permissions
        if pam_provider_permissions is not UNSET:
            field_dict["pamProviderPermissions"] = pam_provider_permissions
        if identity_provider_permissions is not UNSET:
            field_dict["identityProviderPermissions"] = identity_provider_permissions
        if pam_permissions is not UNSET:
            field_dict["pamPermissions"] = pam_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_security_role_claim_definitions_role_claim_definition_response import (
            KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionResponse,
        )
        from ..models.keyfactor_web_keyfactor_api_models_security_security_identity_permissions_permission_roles_pair_response import (
            KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _claim = d.pop("claim", UNSET)
        claim: Union[Unset, KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionResponse]
        if isinstance(_claim, Unset):
            claim = UNSET
        else:
            claim = KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsRoleClaimDefinitionResponse.from_dict(
                _claim
            )

        identity = d.pop("identity", UNSET)

        secured_area_permissions = []
        _secured_area_permissions = d.pop("securedAreaPermissions", UNSET)
        for secured_area_permissions_item_data in _secured_area_permissions or []:
            secured_area_permissions_item = (
                KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse.from_dict(
                    secured_area_permissions_item_data
                )
            )

            secured_area_permissions.append(secured_area_permissions_item)

        collection_permissions = []
        _collection_permissions = d.pop("collectionPermissions", UNSET)
        for collection_permissions_item_data in _collection_permissions or []:
            collection_permissions_item = (
                KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse.from_dict(
                    collection_permissions_item_data
                )
            )

            collection_permissions.append(collection_permissions_item)

        container_permissions = []
        _container_permissions = d.pop("containerPermissions", UNSET)
        for container_permissions_item_data in _container_permissions or []:
            container_permissions_item = (
                KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse.from_dict(
                    container_permissions_item_data
                )
            )

            container_permissions.append(container_permissions_item)

        pam_provider_permissions = []
        _pam_provider_permissions = d.pop("pamProviderPermissions", UNSET)
        for pam_provider_permissions_item_data in _pam_provider_permissions or []:
            pam_provider_permissions_item = (
                KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse.from_dict(
                    pam_provider_permissions_item_data
                )
            )

            pam_provider_permissions.append(pam_provider_permissions_item)

        identity_provider_permissions = []
        _identity_provider_permissions = d.pop("identityProviderPermissions", UNSET)
        for identity_provider_permissions_item_data in _identity_provider_permissions or []:
            identity_provider_permissions_item = (
                KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse.from_dict(
                    identity_provider_permissions_item_data
                )
            )

            identity_provider_permissions.append(identity_provider_permissions_item)

        pam_permissions = []
        _pam_permissions = d.pop("pamPermissions", UNSET)
        for pam_permissions_item_data in _pam_permissions or []:
            pam_permissions_item = (
                KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentityPermissionsPermissionRolesPairResponse.from_dict(
                    pam_permissions_item_data
                )
            )

            pam_permissions.append(pam_permissions_item)

        keyfactor_web_keyfactor_api_models_security_security_identity_permissions_security_identity_permissions_response = cls(
            claim=claim,
            identity=identity,
            secured_area_permissions=secured_area_permissions,
            collection_permissions=collection_permissions,
            container_permissions=container_permissions,
            pam_provider_permissions=pam_provider_permissions,
            identity_provider_permissions=identity_provider_permissions,
            pam_permissions=pam_permissions,
        )

        return keyfactor_web_keyfactor_api_models_security_security_identity_permissions_security_identity_permissions_response
