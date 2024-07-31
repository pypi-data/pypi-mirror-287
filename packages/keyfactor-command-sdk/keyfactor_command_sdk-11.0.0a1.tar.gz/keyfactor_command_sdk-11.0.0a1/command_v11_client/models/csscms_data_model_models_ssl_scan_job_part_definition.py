from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSLScanJobPartDefinition")


@_attrs_define
class CSSCMSDataModelModelsSSLScanJobPartDefinition:
    """
    Attributes:
        item_type (Union[Unset, int]):
        value (Union[Unset, None, str]):
    """

    item_type: Union[Unset, int] = UNSET
    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        item_type = self.item_type
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
        item_type = d.pop("itemType", UNSET)

        value = d.pop("value", UNSET)

        csscms_data_model_models_ssl_scan_job_part_definition = cls(
            item_type=item_type,
            value=value,
        )

        return csscms_data_model_models_ssl_scan_job_part_definition
