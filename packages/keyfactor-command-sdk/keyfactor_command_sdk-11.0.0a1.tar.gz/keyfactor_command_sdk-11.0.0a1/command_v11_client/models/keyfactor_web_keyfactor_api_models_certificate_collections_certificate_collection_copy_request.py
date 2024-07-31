from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_duplicate_subject_type import CSSCMSCoreEnumsDuplicateSubjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionCopyRequest:
    """
    Attributes:
        name (str):
        copy_from_id (int):
        description (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        duplication_field (Union[Unset, CSSCMSCoreEnumsDuplicateSubjectType]):
        show_on_dashboard (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
    """

    name: str
    copy_from_id: int
    description: Union[Unset, None, str] = UNSET
    query: Union[Unset, None, str] = UNSET
    duplication_field: Union[Unset, CSSCMSCoreEnumsDuplicateSubjectType] = UNSET
    show_on_dashboard: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        copy_from_id = self.copy_from_id
        description = self.description
        query = self.query
        duplication_field: Union[Unset, int] = UNSET
        if not isinstance(self.duplication_field, Unset):
            duplication_field = self.duplication_field.value

        show_on_dashboard = self.show_on_dashboard
        favorite = self.favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "copyFromId": copy_from_id,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name")

        copy_from_id = d.pop("copyFromId")

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

        keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_copy_request = cls(
            name=name,
            copy_from_id=copy_from_id,
            description=description,
            query=query,
            duplication_field=duplication_field,
            show_on_dashboard=show_on_dashboard,
            favorite=favorite,
        )

        return keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_copy_request
