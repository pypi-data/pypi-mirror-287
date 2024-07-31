from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_script_categories import CSSCMSDataModelEnumsScriptCategories
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsScriptsScriptQueryResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsScriptsScriptQueryResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        categories (Union[Unset, None, List[CSSCMSDataModelEnumsScriptCategories]]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    categories: Union[Unset, None, List[CSSCMSDataModelEnumsScriptCategories]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        categories: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.categories, Unset):
            if self.categories is None:
                categories = None
            else:
                categories = []
                for categories_item_data in self.categories:
                    categories_item = categories_item_data.value

                    categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = CSSCMSDataModelEnumsScriptCategories(categories_item_data)

            categories.append(categories_item)

        keyfactor_web_keyfactor_api_models_scripts_script_query_response = cls(
            id=id,
            name=name,
            categories=categories,
        )

        return keyfactor_web_keyfactor_api_models_scripts_script_query_response
