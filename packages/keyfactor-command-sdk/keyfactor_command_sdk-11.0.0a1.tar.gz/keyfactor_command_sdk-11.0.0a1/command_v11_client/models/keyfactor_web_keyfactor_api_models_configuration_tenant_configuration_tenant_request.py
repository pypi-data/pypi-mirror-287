from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsConfigurationTenantConfigurationTenantRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsConfigurationTenantConfigurationTenantRequest:
    """
    Attributes:
        configuration_tenant (Union[Unset, None, str]):
    """

    configuration_tenant: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        configuration_tenant = self.configuration_tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if configuration_tenant is not UNSET:
            field_dict["configurationTenant"] = configuration_tenant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        configuration_tenant = d.pop("configurationTenant", UNSET)

        keyfactor_web_keyfactor_api_models_configuration_tenant_configuration_tenant_request = cls(
            configuration_tenant=configuration_tenant,
        )

        return keyfactor_web_keyfactor_api_models_configuration_tenant_configuration_tenant_request
