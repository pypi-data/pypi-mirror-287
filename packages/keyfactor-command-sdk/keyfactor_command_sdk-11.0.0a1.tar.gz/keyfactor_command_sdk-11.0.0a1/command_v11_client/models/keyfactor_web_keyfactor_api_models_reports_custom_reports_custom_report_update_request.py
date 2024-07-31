from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsReportsCustomReportsCustomReportUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsReportsCustomReportsCustomReportUpdateRequest:
    """
    Attributes:
        id (int):
        custom_url (str):
        display_name (str):
        description (str):
        in_navigator (bool):
        favorite (bool):
    """

    id: int
    custom_url: str
    display_name: str
    description: str
    in_navigator: bool
    favorite: bool

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        custom_url = self.custom_url
        display_name = self.display_name
        description = self.description
        in_navigator = self.in_navigator
        favorite = self.favorite

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "customURL": custom_url,
                "displayName": display_name,
                "description": description,
                "inNavigator": in_navigator,
                "favorite": favorite,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        custom_url = d.pop("customURL")

        display_name = d.pop("displayName")

        description = d.pop("description")

        in_navigator = d.pop("inNavigator")

        favorite = d.pop("favorite")

        keyfactor_web_keyfactor_api_models_reports_custom_reports_custom_report_update_request = cls(
            id=id,
            custom_url=custom_url,
            display_name=display_name,
            description=description,
            in_navigator=in_navigator,
            favorite=favorite,
        )

        return keyfactor_web_keyfactor_api_models_reports_custom_reports_custom_report_update_request
