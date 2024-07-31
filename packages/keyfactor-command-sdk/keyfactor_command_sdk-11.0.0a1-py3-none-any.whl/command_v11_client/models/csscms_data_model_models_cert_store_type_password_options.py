from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_cert_store_types_password_styles import (
    CSSCMSDataModelEnumsCertStoreTypesPasswordStyles,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertStoreTypePasswordOptions")


@_attrs_define
class CSSCMSDataModelModelsCertStoreTypePasswordOptions:
    """
    Attributes:
        entry_supported (Union[Unset, bool]):
        store_required (Union[Unset, bool]):
        style (Union[Unset, CSSCMSDataModelEnumsCertStoreTypesPasswordStyles]):
    """

    entry_supported: Union[Unset, bool] = UNSET
    store_required: Union[Unset, bool] = UNSET
    style: Union[Unset, CSSCMSDataModelEnumsCertStoreTypesPasswordStyles] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        entry_supported = self.entry_supported
        store_required = self.store_required
        style: Union[Unset, int] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if entry_supported is not UNSET:
            field_dict["entrySupported"] = entry_supported
        if store_required is not UNSET:
            field_dict["storeRequired"] = store_required
        if style is not UNSET:
            field_dict["style"] = style

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        entry_supported = d.pop("entrySupported", UNSET)

        store_required = d.pop("storeRequired", UNSET)

        _style = d.pop("style", UNSET)
        style: Union[Unset, CSSCMSDataModelEnumsCertStoreTypesPasswordStyles]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = CSSCMSDataModelEnumsCertStoreTypesPasswordStyles(_style)

        csscms_data_model_models_cert_store_type_password_options = cls(
            entry_supported=entry_supported,
            store_required=store_required,
            style=style,
        )

        return csscms_data_model_models_cert_store_type_password_options
