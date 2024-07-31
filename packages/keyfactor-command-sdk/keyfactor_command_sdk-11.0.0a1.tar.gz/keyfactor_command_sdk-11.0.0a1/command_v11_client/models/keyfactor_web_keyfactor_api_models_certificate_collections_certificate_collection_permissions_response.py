from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_certificate_collections_assignable_query_role import (
        KeyfactorWebKeyfactorApiModelsCertificateCollectionsAssignableQueryRole,
    )
    from ..models.keyfactor_web_keyfactor_api_models_certificate_collections_certificate_query_access_control import (
        KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateQueryAccessControl,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionPermissionsResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionPermissionsResponse:
    """
    Attributes:
        query_id (Union[Unset, int]):
        access_control_list (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateQueryAccessControl']]):
        assignable_roles (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsCertificateCollectionsAssignableQueryRole']]):
    """

    query_id: Union[Unset, int] = UNSET
    access_control_list: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateQueryAccessControl"]
    ] = UNSET
    assignable_roles: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsCertificateCollectionsAssignableQueryRole"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        query_id = self.query_id
        access_control_list: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access_control_list, Unset):
            if self.access_control_list is None:
                access_control_list = None
            else:
                access_control_list = []
                for access_control_list_item_data in self.access_control_list:
                    access_control_list_item = access_control_list_item_data.to_dict()

                    access_control_list.append(access_control_list_item)

        assignable_roles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assignable_roles, Unset):
            if self.assignable_roles is None:
                assignable_roles = None
            else:
                assignable_roles = []
                for assignable_roles_item_data in self.assignable_roles:
                    assignable_roles_item = assignable_roles_item_data.to_dict()

                    assignable_roles.append(assignable_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if query_id is not UNSET:
            field_dict["queryId"] = query_id
        if access_control_list is not UNSET:
            field_dict["accessControlList"] = access_control_list
        if assignable_roles is not UNSET:
            field_dict["assignableRoles"] = assignable_roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_certificate_collections_assignable_query_role import (
            KeyfactorWebKeyfactorApiModelsCertificateCollectionsAssignableQueryRole,
        )
        from ..models.keyfactor_web_keyfactor_api_models_certificate_collections_certificate_query_access_control import (
            KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateQueryAccessControl,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        query_id = d.pop("queryId", UNSET)

        access_control_list = []
        _access_control_list = d.pop("accessControlList", UNSET)
        for access_control_list_item_data in _access_control_list or []:
            access_control_list_item = (
                KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateQueryAccessControl.from_dict(
                    access_control_list_item_data
                )
            )

            access_control_list.append(access_control_list_item)

        assignable_roles = []
        _assignable_roles = d.pop("assignableRoles", UNSET)
        for assignable_roles_item_data in _assignable_roles or []:
            assignable_roles_item = KeyfactorWebKeyfactorApiModelsCertificateCollectionsAssignableQueryRole.from_dict(
                assignable_roles_item_data
            )

            assignable_roles.append(assignable_roles_item)

        keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_permissions_response = cls(
            query_id=query_id,
            access_control_list=access_control_list,
            assignable_roles=assignable_roles,
        )

        return keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_permissions_response
