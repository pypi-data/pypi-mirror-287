from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.keyfactor_orchestrators_common_enums_ssl_network_definition_item_type import (
    KeyfactorOrchestratorsCommonEnumsSslNetworkDefinitionItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSLNetworkDefinition")


@_attrs_define
class CSSCMSDataModelModelsSSLNetworkDefinition:
    """
    Attributes:
        item_type (Union[Unset, KeyfactorOrchestratorsCommonEnumsSslNetworkDefinitionItemType]):
        value (Union[Unset, None, str]):
    """

    item_type: Union[Unset, KeyfactorOrchestratorsCommonEnumsSslNetworkDefinitionItemType] = UNSET
    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type: Union[Unset, int] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, KeyfactorOrchestratorsCommonEnumsSslNetworkDefinitionItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = KeyfactorOrchestratorsCommonEnumsSslNetworkDefinitionItemType(_item_type)

        value = d.pop("value", UNSET)

        csscms_data_model_models_ssl_network_definition = cls(
            item_type=item_type,
            value=value,
        )

        return csscms_data_model_models_ssl_network_definition
