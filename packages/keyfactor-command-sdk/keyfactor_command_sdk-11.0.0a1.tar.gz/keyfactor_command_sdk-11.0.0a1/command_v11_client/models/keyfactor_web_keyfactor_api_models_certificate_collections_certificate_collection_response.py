from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_duplicate_subject_type import CSSCMSCoreEnumsDuplicateSubjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        content (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        duplication_field (Union[Unset, CSSCMSCoreEnumsDuplicateSubjectType]):
        show_on_dashboard (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    content: Union[Unset, None, str] = UNSET
    query: Union[Unset, None, str] = UNSET
    duplication_field: Union[Unset, CSSCMSCoreEnumsDuplicateSubjectType] = UNSET
    show_on_dashboard: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        content = self.content
        query = self.query
        duplication_field: Union[Unset, int] = UNSET
        if not isinstance(self.duplication_field, Unset):
            duplication_field = self.duplication_field.value

        show_on_dashboard = self.show_on_dashboard
        favorite = self.favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if content is not UNSET:
            field_dict["content"] = content
        if query is not UNSET:
            field_dict["query"] = query
        if duplication_field is not UNSET:
            field_dict["duplicationField"] = duplication_field
        if show_on_dashboard is not UNSET:
            field_dict["showOnDashboard"] = show_on_dashboard
        if favorite is not UNSET:
            field_dict["favorite"] = favorite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        content = d.pop("content", UNSET)

        query = d.pop("query", UNSET)

        _duplication_field = d.pop("duplicationField", UNSET)
        duplication_field: Union[Unset, CSSCMSCoreEnumsDuplicateSubjectType]
        if isinstance(_duplication_field, Unset):
            duplication_field = UNSET
        else:
            duplication_field = CSSCMSCoreEnumsDuplicateSubjectType(_duplication_field)

        show_on_dashboard = d.pop("showOnDashboard", UNSET)

        favorite = d.pop("favorite", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_response = cls(
            id=id,
            name=name,
            description=description,
            content=content,
            query=query,
            duplication_field=duplication_field,
            show_on_dashboard=show_on_dashboard,
            favorite=favorite,
        )

        return keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_response
