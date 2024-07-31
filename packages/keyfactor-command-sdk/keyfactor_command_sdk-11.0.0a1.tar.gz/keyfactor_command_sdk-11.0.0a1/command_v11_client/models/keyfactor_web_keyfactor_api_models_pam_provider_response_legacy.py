from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_provider_type import CSSCMSDataModelModelsProviderType
    from ..models.keyfactor_web_keyfactor_api_models_pam_pam_provider_type_param_value_response import (
        KeyfactorWebKeyfactorApiModelsPAMPamProviderTypeParamValueResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsPAMProviderResponseLegacy")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsPAMProviderResponseLegacy:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        area (Union[Unset, int]):
        provider_type (Union[Unset, CSSCMSDataModelModelsProviderType]):
        provider_type_param_values (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsPAMPamProviderTypeParamValueResponse']]):
        secured_area_id (Union[Unset, None, int]):
        remote (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    area: Union[Unset, int] = UNSET
    provider_type: Union[Unset, "CSSCMSDataModelModelsProviderType"] = UNSET
    provider_type_param_values: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsPAMPamProviderTypeParamValueResponse"]
    ] = UNSET
    secured_area_id: Union[Unset, None, int] = UNSET
    remote: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        area = self.area
        provider_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_type, Unset):
            provider_type = self.provider_type.to_dict()

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
        remote = self.remote

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if area is not UNSET:
            field_dict["area"] = area
        if provider_type is not UNSET:
            field_dict["providerType"] = provider_type
        if provider_type_param_values is not UNSET:
            field_dict["providerTypeParamValues"] = provider_type_param_values
        if secured_area_id is not UNSET:
            field_dict["securedAreaId"] = secured_area_id
        if remote is not UNSET:
            field_dict["remote"] = remote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_provider_type import CSSCMSDataModelModelsProviderType
        from ..models.keyfactor_web_keyfactor_api_models_pam_pam_provider_type_param_value_response import (
            KeyfactorWebKeyfactorApiModelsPAMPamProviderTypeParamValueResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        area = d.pop("area", UNSET)

        _provider_type = d.pop("providerType", UNSET)
        provider_type: Union[Unset, CSSCMSDataModelModelsProviderType]
        if isinstance(_provider_type, Unset):
            provider_type = UNSET
        else:
            provider_type = CSSCMSDataModelModelsProviderType.from_dict(_provider_type)

        provider_type_param_values = []
        _provider_type_param_values = d.pop("providerTypeParamValues", UNSET)
        for provider_type_param_values_item_data in _provider_type_param_values or []:
            provider_type_param_values_item = (
                KeyfactorWebKeyfactorApiModelsPAMPamProviderTypeParamValueResponse.from_dict(
                    provider_type_param_values_item_data
                )
            )

            provider_type_param_values.append(provider_type_param_values_item)

        secured_area_id = d.pop("securedAreaId", UNSET)

        remote = d.pop("remote", UNSET)

        keyfactor_web_keyfactor_api_models_pam_provider_response_legacy = cls(
            id=id,
            name=name,
            area=area,
            provider_type=provider_type,
            provider_type_param_values=provider_type_param_values,
            secured_area_id=secured_area_id,
            remote=remote,
        )

        return keyfactor_web_keyfactor_api_models_pam_provider_response_legacy
