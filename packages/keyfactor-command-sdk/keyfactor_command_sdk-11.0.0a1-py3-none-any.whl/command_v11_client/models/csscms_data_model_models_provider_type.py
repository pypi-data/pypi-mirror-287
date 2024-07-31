from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_provider_type_param import CSSCMSDataModelModelsProviderTypeParam


T = TypeVar("T", bound="CSSCMSDataModelModelsProviderType")


@_attrs_define
class CSSCMSDataModelModelsProviderType:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, None, str]):
        provider_type_params (Union[Unset, None, List['CSSCMSDataModelModelsProviderTypeParam']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    provider_type_params: Union[Unset, None, List["CSSCMSDataModelModelsProviderTypeParam"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        provider_type_params: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.provider_type_params, Unset):
            if self.provider_type_params is None:
                provider_type_params = None
            else:
                provider_type_params = []
                for provider_type_params_item_data in self.provider_type_params:
                    provider_type_params_item = provider_type_params_item_data.to_dict()

                    provider_type_params.append(provider_type_params_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if provider_type_params is not UNSET:
            field_dict["providerTypeParams"] = provider_type_params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_provider_type_param import CSSCMSDataModelModelsProviderTypeParam

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        provider_type_params = []
        _provider_type_params = d.pop("providerTypeParams", UNSET)
        for provider_type_params_item_data in _provider_type_params or []:
            provider_type_params_item = CSSCMSDataModelModelsProviderTypeParam.from_dict(provider_type_params_item_data)

            provider_type_params.append(provider_type_params_item)

        csscms_data_model_models_provider_type = cls(
            id=id,
            name=name,
            provider_type_params=provider_type_params,
        )

        return csscms_data_model_models_provider_type
