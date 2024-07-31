from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_pam_provider_type_param_value import (
        CSSCMSDataModelModelsPamProviderTypeParamValue,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsKeyfactorSecret")


@_attrs_define
class CSSCMSDataModelModelsKeyfactorSecret:
    """
    Attributes:
        value (Union[Unset, Any]):
        secret_type_guid (Union[Unset, str]):
        instance_id (Union[Unset, None, int]):
        instance_guid (Union[Unset, None, str]):
        provider_type_parameter_values (Union[Unset, None, List['CSSCMSDataModelModelsPamProviderTypeParamValue']]):
        provider_id (Union[Unset, None, int]):
        is_managed (Union[Unset, bool]):
    """

    value: Union[Unset, Any] = UNSET
    secret_type_guid: Union[Unset, str] = UNSET
    instance_id: Union[Unset, None, int] = UNSET
    instance_guid: Union[Unset, None, str] = UNSET
    provider_type_parameter_values: Union[Unset, None, List["CSSCMSDataModelModelsPamProviderTypeParamValue"]] = UNSET
    provider_id: Union[Unset, None, int] = UNSET
    is_managed: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        secret_type_guid = self.secret_type_guid
        instance_id = self.instance_id
        instance_guid = self.instance_guid
        provider_type_parameter_values: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.provider_type_parameter_values, Unset):
            if self.provider_type_parameter_values is None:
                provider_type_parameter_values = None
            else:
                provider_type_parameter_values = []
                for provider_type_parameter_values_item_data in self.provider_type_parameter_values:
                    provider_type_parameter_values_item = provider_type_parameter_values_item_data.to_dict()

                    provider_type_parameter_values.append(provider_type_parameter_values_item)

        provider_id = self.provider_id
        is_managed = self.is_managed

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if secret_type_guid is not UNSET:
            field_dict["secretTypeGuid"] = secret_type_guid
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if instance_guid is not UNSET:
            field_dict["instanceGuid"] = instance_guid
        if provider_type_parameter_values is not UNSET:
            field_dict["providerTypeParameterValues"] = provider_type_parameter_values
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if is_managed is not UNSET:
            field_dict["isManaged"] = is_managed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_pam_provider_type_param_value import (
            CSSCMSDataModelModelsPamProviderTypeParamValue,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        value = d.pop("value", UNSET)

        secret_type_guid = d.pop("secretTypeGuid", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        instance_guid = d.pop("instanceGuid", UNSET)

        provider_type_parameter_values = []
        _provider_type_parameter_values = d.pop("providerTypeParameterValues", UNSET)
        for provider_type_parameter_values_item_data in _provider_type_parameter_values or []:
            provider_type_parameter_values_item = CSSCMSDataModelModelsPamProviderTypeParamValue.from_dict(
                provider_type_parameter_values_item_data
            )

            provider_type_parameter_values.append(provider_type_parameter_values_item)

        provider_id = d.pop("providerId", UNSET)

        is_managed = d.pop("isManaged", UNSET)

        csscms_data_model_models_keyfactor_secret = cls(
            value=value,
            secret_type_guid=secret_type_guid,
            instance_id=instance_id,
            instance_guid=instance_guid,
            provider_type_parameter_values=provider_type_parameter_values,
            provider_id=provider_id,
            is_managed=is_managed,
        )

        return csscms_data_model_models_keyfactor_secret
