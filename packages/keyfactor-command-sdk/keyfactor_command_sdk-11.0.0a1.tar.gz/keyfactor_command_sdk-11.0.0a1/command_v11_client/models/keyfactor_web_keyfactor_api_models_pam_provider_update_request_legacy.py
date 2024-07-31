from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_pam_provider_create_request_provider_type import (
        KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestProviderType,
    )
    from ..models.keyfactor_web_keyfactor_api_models_pam_provider_create_request_type_param_value import (
        KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestTypeParamValue,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsPAMProviderUpdateRequestLegacy")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsPAMProviderUpdateRequestLegacy:
    """
    Attributes:
        id (int):
        name (str):
        provider_type (KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestProviderType):
        remote (Union[Unset, bool]):
        area (Union[Unset, int]):
        provider_type_param_values (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestTypeParamValue']]):
        secured_area_id (Union[Unset, None, int]):
    """

    id: int
    name: str
    provider_type: "KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestProviderType"
    remote: Union[Unset, bool] = UNSET
    area: Union[Unset, int] = UNSET
    provider_type_param_values: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestTypeParamValue"]
    ] = UNSET
    secured_area_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        provider_type = self.provider_type.to_dict()

        remote = self.remote
        area = self.area
        provider_type_param_values: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.provider_type_param_values, Unset):
            if self.provider_type_param_values is None:
                provider_type_param_values = None
            else:
                provider_type_param_values = []
                for provider_type_param_values_item_data in self.provider_type_param_values:
                    provider_type_param_values_item = provider_type_param_values_item_data.to_dict()

                    provider_type_param_values.append(provider_type_param_values_item)

        secured_area_id = self.secured_area_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
                "providerType": provider_type,
            }
        )
        if remote is not UNSET:
            field_dict["remote"] = remote
        if area is not UNSET:
            field_dict["area"] = area
        if provider_type_param_values is not UNSET:
            field_dict["providerTypeParamValues"] = provider_type_param_values
        if secured_area_id is not UNSET:
            field_dict["securedAreaId"] = secured_area_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_pam_provider_create_request_provider_type import (
            KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestProviderType,
        )
        from ..models.keyfactor_web_keyfactor_api_models_pam_provider_create_request_type_param_value import (
            KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestTypeParamValue,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        name = d.pop("name")

        provider_type = KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestProviderType.from_dict(
            d.pop("providerType")
        )

        remote = d.pop("remote", UNSET)

        area = d.pop("area", UNSET)

        provider_type_param_values = []
        _provider_type_param_values = d.pop("providerTypeParamValues", UNSET)
        for provider_type_param_values_item_data in _provider_type_param_values or []:
            provider_type_param_values_item = (
                KeyfactorWebKeyfactorApiModelsPAMProviderCreateRequestTypeParamValue.from_dict(
                    provider_type_param_values_item_data
                )
            )

            provider_type_param_values.append(provider_type_param_values_item)

        secured_area_id = d.pop("securedAreaId", UNSET)

        keyfactor_web_keyfactor_api_models_pam_provider_update_request_legacy = cls(
            id=id,
            name=name,
            provider_type=provider_type,
            remote=remote,
            area=area,
            provider_type_param_values=provider_type_param_values,
            secured_area_id=secured_area_id,
        )

        return keyfactor_web_keyfactor_api_models_pam_provider_update_request_legacy
