from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsMacEnrollmentMacEnrollmentAPIModel")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsMacEnrollmentMacEnrollmentAPIModel:
    """
    Attributes:
        id (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        interval (Union[Unset, int]):
        use_metadata (Union[Unset, bool]):
        metadata_field (Union[Unset, None, str]):
        metadata_value (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    interval: Union[Unset, int] = UNSET
    use_metadata: Union[Unset, bool] = UNSET
    metadata_field: Union[Unset, None, str] = UNSET
    metadata_value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        enabled = self.enabled
        interval = self.interval
        use_metadata = self.use_metadata
        metadata_field = self.metadata_field
        metadata_value = self.metadata_value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if interval is not UNSET:
            field_dict["interval"] = interval
        if use_metadata is not UNSET:
            field_dict["useMetadata"] = use_metadata
        if metadata_field is not UNSET:
            field_dict["metadataField"] = metadata_field
        if metadata_value is not UNSET:
            field_dict["metadataValue"] = metadata_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        enabled = d.pop("enabled", UNSET)

        interval = d.pop("interval", UNSET)

        use_metadata = d.pop("useMetadata", UNSET)

        metadata_field = d.pop("metadataField", UNSET)

        metadata_value = d.pop("metadataValue", UNSET)

        keyfactor_web_keyfactor_api_models_mac_enrollment_mac_enrollment_api_model = cls(
            id=id,
            enabled=enabled,
            interval=interval,
            use_metadata=use_metadata,
            metadata_field=metadata_field,
            metadata_value=metadata_value,
        )

        return keyfactor_web_keyfactor_api_models_mac_enrollment_mac_enrollment_api_model
