from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_pam_provider_type_parameter_response import (
        KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsPAMPamProviderTypeParamValueResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsPAMPamProviderTypeParamValueResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        value (Union[Unset, None, str]):
        instance_id (Union[Unset, None, int]):
        instance_guid (Union[Unset, None, str]):
        provider_type_param (Union[Unset, KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse]):
    """

    id: Union[Unset, int] = UNSET
    value: Union[Unset, None, str] = UNSET
    instance_id: Union[Unset, None, int] = UNSET
    instance_guid: Union[Unset, None, str] = UNSET
    provider_type_param: Union[Unset, "KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value
        instance_id = self.instance_id
        instance_guid = self.instance_guid
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
        if provider_type_param is not UNSET:
            field_dict["providerTypeParam"] = provider_type_param

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_pam_provider_type_parameter_response import (
            KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        instance_guid = d.pop("instanceGuid", UNSET)

        _provider_type_param = d.pop("providerTypeParam", UNSET)
        provider_type_param: Union[Unset, KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse]
        if isinstance(_provider_type_param, Unset):
            provider_type_param = UNSET
        else:
            provider_type_param = KeyfactorWebKeyfactorApiModelsPAMProviderTypeParameterResponse.from_dict(
                _provider_type_param
            )

        keyfactor_web_keyfactor_api_models_pam_pam_provider_type_param_value_response = cls(
            id=id,
            value=value,
            instance_id=instance_id,
            instance_guid=instance_guid,
            provider_type_param=provider_type_param,
        )

        return keyfactor_web_keyfactor_api_models_pam_pam_provider_type_param_value_response
