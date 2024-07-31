from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_pam_parameter_data_type import CSSCMSDataModelEnumsPamParameterDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_provider_type import CSSCMSDataModelModelsProviderType


T = TypeVar("T", bound="CSSCMSDataModelModelsProviderTypeParam")


@_attrs_define
class CSSCMSDataModelModelsProviderTypeParam:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        data_type (Union[Unset, CSSCMSDataModelEnumsPamParameterDataType]):
        instance_level (Union[Unset, bool]):
        provider_type (Union[Unset, CSSCMSDataModelModelsProviderType]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    data_type: Union[Unset, CSSCMSDataModelEnumsPamParameterDataType] = UNSET
    instance_level: Union[Unset, bool] = UNSET
    provider_type: Union[Unset, "CSSCMSDataModelModelsProviderType"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        display_name = self.display_name
        data_type: Union[Unset, int] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        instance_level = self.instance_level
        provider_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider_type, Unset):
            provider_type = self.provider_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if instance_level is not UNSET:
            field_dict["instanceLevel"] = instance_level
        if provider_type is not UNSET:
            field_dict["providerType"] = provider_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_provider_type import CSSCMSDataModelModelsProviderType

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, CSSCMSDataModelEnumsPamParameterDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = CSSCMSDataModelEnumsPamParameterDataType(_data_type)

        instance_level = d.pop("instanceLevel", UNSET)

        _provider_type = d.pop("providerType", UNSET)
        provider_type: Union[Unset, CSSCMSDataModelModelsProviderType]
        if isinstance(_provider_type, Unset):
            provider_type = UNSET
        else:
            provider_type = CSSCMSDataModelModelsProviderType.from_dict(_provider_type)

        csscms_data_model_models_provider_type_param = cls(
            id=id,
            name=name,
            display_name=display_name,
            data_type=data_type,
            instance_level=instance_level,
            provider_type=provider_type,
        )

        return csscms_data_model_models_provider_type_param
