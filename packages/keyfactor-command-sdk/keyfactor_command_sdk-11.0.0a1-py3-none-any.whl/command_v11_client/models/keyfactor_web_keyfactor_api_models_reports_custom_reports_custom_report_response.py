from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsReportsCustomReportsCustomReportResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsReportsCustomReportsCustomReportResponse:
    """
    Attributes:
        custom_url (Union[Unset, None, str]):
        id (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        in_navigator (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
    """

    custom_url: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    in_navigator: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        custom_url = self.custom_url
        id = self.id
        display_name = self.display_name
        description = self.description
        in_navigator = self.in_navigator
        favorite = self.favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if custom_url is not UNSET:
            field_dict["customURL"] = custom_url
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if in_navigator is not UNSET:
            field_dict["inNavigator"] = in_navigator
        if favorite is not UNSET:
            field_dict["favorite"] = favorite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        custom_url = d.pop("customURL", UNSET)

        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        in_navigator = d.pop("inNavigator", UNSET)

        favorite = d.pop("favorite", UNSET)

        keyfactor_web_keyfactor_api_models_reports_custom_reports_custom_report_response = cls(
            custom_url=custom_url,
            id=id,
            display_name=display_name,
            description=description,
            in_navigator=in_navigator,
            favorite=favorite,
        )

        return keyfactor_web_keyfactor_api_models_reports_custom_reports_custom_report_response
