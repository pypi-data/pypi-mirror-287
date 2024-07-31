from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_duplicate_subject_type import CSSCMSCoreEnumsDuplicateSubjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionCreateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionCreateRequest:
    """
    Attributes:
        name (str):
        description (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        duplication_field (Union[Unset, CSSCMSCoreEnumsDuplicateSubjectType]):
        show_on_dashboard (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
        copy_from_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
    """

    name: str
    description: Union[Unset, None, str] = UNSET
    query: Union[Unset, None, str] = UNSET
    duplication_field: Union[Unset, CSSCMSCoreEnumsDuplicateSubjectType] = UNSET
    show_on_dashboard: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    copy_from_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        query = self.query
        duplication_field: Union[Unset, int] = UNSET
        if not isinstance(self.duplication_field, Unset):
            duplication_field = self.duplication_field.value

        show_on_dashboard = self.show_on_dashboard
        favorite = self.favorite
        copy_from_id = self.copy_from_id
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if query is not UNSET:
            field_dict["query"] = query
        if duplication_field is not UNSET:
            field_dict["duplicationField"] = duplication_field
        if show_on_dashboard is not UNSET:
            field_dict["showOnDashboard"] = show_on_dashboard
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if copy_from_id is not UNSET:
            field_dict["copyFromId"] = copy_from_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name")

        description = d.pop("description", UNSET)

        query = d.pop("query", UNSET)

        _duplication_field = d.pop("duplicationField", UNSET)
        duplication_field: Union[Unset, CSSCMSCoreEnumsDuplicateSubjectType]
        if isinstance(_duplication_field, Unset):
            duplication_field = UNSET
        else:
            duplication_field = CSSCMSCoreEnumsDuplicateSubjectType(_duplication_field)

        show_on_dashboard = d.pop("showOnDashboard", UNSET)

        favorite = d.pop("favorite", UNSET)

        copy_from_id = d.pop("copyFromId", UNSET)

        id = d.pop("id", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_create_request = cls(
            name=name,
            description=description,
            query=query,
            duplication_field=duplication_field,
            show_on_dashboard=show_on_dashboard,
            favorite=favorite,
            copy_from_id=copy_from_id,
            id=id,
        )

        return keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_create_request
