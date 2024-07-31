from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsMetadataSingleUpdateRequest")


@_attrs_define
class CSSCMSDataModelModelsMetadataSingleUpdateRequest:
    """
    Attributes:
        metadata_name (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
        overwrite_existing (Union[Unset, bool]):
    """

    metadata_name: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET
    overwrite_existing: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        metadata_name = self.metadata_name
        value = self.value
        overwrite_existing = self.overwrite_existing

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if metadata_name is not UNSET:
            field_dict["metadataName"] = metadata_name
        if value is not UNSET:
            field_dict["value"] = value
        if overwrite_existing is not UNSET:
            field_dict["overwriteExisting"] = overwrite_existing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        metadata_name = d.pop("metadataName", UNSET)

        value = d.pop("value", UNSET)

        overwrite_existing = d.pop("overwriteExisting", UNSET)

        csscms_data_model_models_metadata_single_update_request = cls(
            metadata_name=metadata_name,
            value=value,
            overwrite_existing=overwrite_existing,
        )

        return csscms_data_model_models_metadata_single_update_request
