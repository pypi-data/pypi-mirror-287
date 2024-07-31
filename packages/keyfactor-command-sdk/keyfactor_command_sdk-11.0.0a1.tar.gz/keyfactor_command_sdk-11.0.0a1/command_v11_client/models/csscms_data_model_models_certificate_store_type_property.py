from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_certificate_store_type_property_type import (
    CSSCMSCoreEnumsCertificateStoreTypePropertyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreTypeProperty")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreTypeProperty:
    """
    Attributes:
        store_type_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        type (Union[Unset, CSSCMSCoreEnumsCertificateStoreTypePropertyType]):
        depends_on (Union[Unset, None, str]):
        default_value (Union[Unset, None, str]):
        required (Union[Unset, bool]):
    """

    store_type_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    type: Union[Unset, CSSCMSCoreEnumsCertificateStoreTypePropertyType] = UNSET
    depends_on: Union[Unset, None, str] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    required: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_type_id = self.store_type_id
        name = self.name
        display_name = self.display_name
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        depends_on = self.depends_on
        default_value = self.default_value
        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if store_type_id is not UNSET:
            field_dict["storeTypeId"] = store_type_id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if type is not UNSET:
            field_dict["type"] = type
        if depends_on is not UNSET:
            field_dict["dependsOn"] = depends_on
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        store_type_id = d.pop("storeTypeId", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CSSCMSCoreEnumsCertificateStoreTypePropertyType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CSSCMSCoreEnumsCertificateStoreTypePropertyType(_type)

        depends_on = d.pop("dependsOn", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        required = d.pop("required", UNSET)

        csscms_data_model_models_certificate_store_type_property = cls(
            store_type_id=store_type_id,
            name=name,
            display_name=display_name,
            type=type,
            depends_on=depends_on,
            default_value=default_value,
            required=required,
        )

        return csscms_data_model_models_certificate_store_type_property
