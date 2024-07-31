from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_provider import CSSCMSDataModelModelsProvider
    from ..models.csscms_data_model_models_provider_type_param import CSSCMSDataModelModelsProviderTypeParam


T = TypeVar("T", bound="CSSCMSDataModelModelsPamProviderTypeParamValue")


@_attrs_define
class CSSCMSDataModelModelsPamProviderTypeParamValue:
    """
    Attributes:
        id (Union[Unset, int]):
        value (Union[Unset, None, str]):
        instance_id (Union[Unset, None, int]):
        instance_guid (Union[Unset, None, str]):
        provider (Union[Unset, CSSCMSDataModelModelsProvider]):
        provider_type_param (Union[Unset, CSSCMSDataModelModelsProviderTypeParam]):
    """

    id: Union[Unset, int] = UNSET
    value: Union[Unset, None, str] = UNSET
    instance_id: Union[Unset, None, int] = UNSET
    instance_guid: Union[Unset, None, str] = UNSET
    provider: Union[Unset, "CSSCMSDataModelModelsProvider"] = UNSET
    provider_type_param: Union[Unset, "CSSCMSDataModelModelsProviderTypeParam"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value
        instance_id = self.instance_id
        instance_guid = self.instance_guid
        provider: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        provider_type_param: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_type_param, Unset):
            provider_type_param = self.provider_type_param.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if instance_guid is not UNSET:
            field_dict["instanceGuid"] = instance_guid
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_type_param is not UNSET:
            field_dict["providerTypeParam"] = provider_type_param

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_provider import CSSCMSDataModelModelsProvider
        from ..models.csscms_data_model_models_provider_type_param import CSSCMSDataModelModelsProviderTypeParam

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        instance_guid = d.pop("instanceGuid", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CSSCMSDataModelModelsProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = CSSCMSDataModelModelsProvider.from_dict(_provider)

        _provider_type_param = d.pop("providerTypeParam", UNSET)
        provider_type_param: Union[Unset, CSSCMSDataModelModelsProviderTypeParam]
        if isinstance(_provider_type_param, Unset):
            provider_type_param = UNSET
        else:
            provider_type_param = CSSCMSDataModelModelsProviderTypeParam.from_dict(_provider_type_param)

        csscms_data_model_models_pam_provider_type_param_value = cls(
            id=id,
            value=value,
            instance_id=instance_id,
            instance_guid=instance_guid,
            provider=provider,
            provider_type_param=provider_type_param,
        )

        return csscms_data_model_models_pam_provider_type_param_value
