from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_pam_provider_type_param_value import (
        CSSCMSDataModelModelsPamProviderTypeParamValue,
    )
    from ..models.csscms_data_model_models_provider_type import CSSCMSDataModelModelsProviderType


T = TypeVar("T", bound="CSSCMSDataModelModelsProvider")


@_attrs_define
class CSSCMSDataModelModelsProvider:
    """
    Attributes:
        name (str):
        provider_type (CSSCMSDataModelModelsProviderType):
        id (Union[Unset, int]):
        area (Union[Unset, int]):
        provider_type_param_values (Union[Unset, None, List['CSSCMSDataModelModelsPamProviderTypeParamValue']]):
        secured_area_id (Union[Unset, None, int]):
        remote (Union[Unset, bool]):
    """

    name: str
    provider_type: "CSSCMSDataModelModelsProviderType"
    id: Union[Unset, int] = UNSET
    area: Union[Unset, int] = UNSET
    provider_type_param_values: Union[Unset, None, List["CSSCMSDataModelModelsPamProviderTypeParamValue"]] = UNSET
    secured_area_id: Union[Unset, None, int] = UNSET
    remote: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        provider_type = self.provider_type.to_dict()

        id = self.id
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
        remote = self.remote

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "providerType": provider_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if area is not UNSET:
            field_dict["area"] = area
        if provider_type_param_values is not UNSET:
            field_dict["providerTypeParamValues"] = provider_type_param_values
        if secured_area_id is not UNSET:
            field_dict["securedAreaId"] = secured_area_id
        if remote is not UNSET:
            field_dict["remote"] = remote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_pam_provider_type_param_value import (
            CSSCMSDataModelModelsPamProviderTypeParamValue,
        )
        from ..models.csscms_data_model_models_provider_type import CSSCMSDataModelModelsProviderType

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name")

        provider_type = CSSCMSDataModelModelsProviderType.from_dict(d.pop("providerType"))

        id = d.pop("id", UNSET)

        area = d.pop("area", UNSET)

        provider_type_param_values = []
        _provider_type_param_values = d.pop("providerTypeParamValues", UNSET)
        for provider_type_param_values_item_data in _provider_type_param_values or []:
            provider_type_param_values_item = CSSCMSDataModelModelsPamProviderTypeParamValue.from_dict(
                provider_type_param_values_item_data
            )

            provider_type_param_values.append(provider_type_param_values_item)

        secured_area_id = d.pop("securedAreaId", UNSET)

        remote = d.pop("remote", UNSET)

        csscms_data_model_models_provider = cls(
            name=name,
            provider_type=provider_type,
            id=id,
            area=area,
            provider_type_param_values=provider_type_param_values,
            secured_area_id=secured_area_id,
            remote=remote,
        )

        return csscms_data_model_models_provider
