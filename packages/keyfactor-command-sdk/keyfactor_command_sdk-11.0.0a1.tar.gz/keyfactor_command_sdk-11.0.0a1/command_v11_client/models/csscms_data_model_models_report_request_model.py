from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsReportRequestModel")


@_attrs_define
class CSSCMSDataModelModelsReportRequestModel:
    """
    Attributes:
        id (Union[Unset, None, int]):
        in_navigator (Union[Unset, None, bool]):
        favorite (Union[Unset, None, bool]):
        remove_duplicates (Union[Unset, None, bool]):
    """

    id: Union[Unset, None, int] = UNSET
    in_navigator: Union[Unset, None, bool] = UNSET
    favorite: Union[Unset, None, bool] = UNSET
    remove_duplicates: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        in_navigator = self.in_navigator
        favorite = self.favorite
        remove_duplicates = self.remove_duplicates

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if in_navigator is not UNSET:
            field_dict["inNavigator"] = in_navigator
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if remove_duplicates is not UNSET:
            field_dict["removeDuplicates"] = remove_duplicates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        in_navigator = d.pop("inNavigator", UNSET)

        favorite = d.pop("favorite", UNSET)

        remove_duplicates = d.pop("removeDuplicates", UNSET)

        csscms_data_model_models_report_request_model = cls(
            id=id,
            in_navigator=in_navigator,
            favorite=favorite,
            remove_duplicates=remove_duplicates,
        )

        return csscms_data_model_models_report_request_model
