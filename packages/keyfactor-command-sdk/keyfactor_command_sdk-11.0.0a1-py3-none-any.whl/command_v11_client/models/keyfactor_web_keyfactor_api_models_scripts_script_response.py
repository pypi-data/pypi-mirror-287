from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_script_categories import CSSCMSDataModelEnumsScriptCategories
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsScriptsScriptResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsScriptsScriptResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        contents (Union[Unset, None, str]):
        categories (Union[Unset, None, List[CSSCMSDataModelEnumsScriptCategories]]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    contents: Union[Unset, None, str] = UNSET
    categories: Union[Unset, None, List[CSSCMSDataModelEnumsScriptCategories]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        contents = self.contents
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
        if contents is not UNSET:
            field_dict["contents"] = contents
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        contents = d.pop("contents", UNSET)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = CSSCMSDataModelEnumsScriptCategories(categories_item_data)

            categories.append(categories_item)

        keyfactor_web_keyfactor_api_models_scripts_script_response = cls(
            id=id,
            name=name,
            contents=contents,
            categories=categories,
        )

        return keyfactor_web_keyfactor_api_models_scripts_script_response
