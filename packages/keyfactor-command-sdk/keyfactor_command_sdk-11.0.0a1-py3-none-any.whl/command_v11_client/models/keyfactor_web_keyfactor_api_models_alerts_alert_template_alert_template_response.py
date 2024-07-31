from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        forest_root (Union[Unset, None, str]):
        configuration_tenant (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    forest_root: Union[Unset, None, str] = UNSET
    configuration_tenant: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        forest_root = self.forest_root
        configuration_tenant = self.configuration_tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if forest_root is not UNSET:
            field_dict["forestRoot"] = forest_root
        if configuration_tenant is not UNSET:
            field_dict["configurationTenant"] = configuration_tenant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        forest_root = d.pop("forestRoot", UNSET)

        configuration_tenant = d.pop("configurationTenant", UNSET)

        keyfactor_web_keyfactor_api_models_alerts_alert_template_alert_template_response = cls(
            id=id,
            display_name=display_name,
            forest_root=forest_root,
            configuration_tenant=configuration_tenant,
        )

        return keyfactor_web_keyfactor_api_models_alerts_alert_template_alert_template_response
