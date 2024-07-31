from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionListResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionListResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        content (Union[Unset, None, str]):
        duplication_field (Union[Unset, None, str]):
        favorite (Union[Unset, bool]):
        show_on_dashboard (Union[Unset, bool]):
        has_query_permissions (Union[Unset, bool]):
        description (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    content: Union[Unset, None, str] = UNSET
    duplication_field: Union[Unset, None, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    show_on_dashboard: Union[Unset, bool] = UNSET
    has_query_permissions: Union[Unset, bool] = UNSET
    description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        content = self.content
        duplication_field = self.duplication_field
        favorite = self.favorite
        show_on_dashboard = self.show_on_dashboard
        has_query_permissions = self.has_query_permissions
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if content is not UNSET:
            field_dict["content"] = content
        if duplication_field is not UNSET:
            field_dict["duplicationField"] = duplication_field
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if show_on_dashboard is not UNSET:
            field_dict["showOnDashboard"] = show_on_dashboard
        if has_query_permissions is not UNSET:
            field_dict["hasQueryPermissions"] = has_query_permissions
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        content = d.pop("content", UNSET)

        duplication_field = d.pop("duplicationField", UNSET)

        favorite = d.pop("favorite", UNSET)

        show_on_dashboard = d.pop("showOnDashboard", UNSET)

        has_query_permissions = d.pop("hasQueryPermissions", UNSET)

        description = d.pop("description", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_list_response = cls(
            id=id,
            name=name,
            content=content,
            duplication_field=duplication_field,
            favorite=favorite,
            show_on_dashboard=show_on_dashboard,
            has_query_permissions=has_query_permissions,
            description=description,
        )

        return keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_list_response
