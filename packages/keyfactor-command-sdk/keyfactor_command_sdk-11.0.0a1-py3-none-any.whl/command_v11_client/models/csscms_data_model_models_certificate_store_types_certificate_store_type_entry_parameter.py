from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_cert_store_entry_parameter_type import CSSCMSCoreEnumsCertStoreEntryParameterType
from ..models.csscms_core_enums_entry_parameter_usage_flags import CSSCMSCoreEnumsEntryParameterUsageFlags
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter:
    """
    Attributes:
        store_type_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        type (Union[Unset, CSSCMSCoreEnumsCertStoreEntryParameterType]):
        required_when (Union[Unset, CSSCMSCoreEnumsEntryParameterUsageFlags]):
        depends_on (Union[Unset, None, str]):
        default_value (Union[Unset, None, str]):
        options (Union[Unset, None, str]):
    """

    store_type_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    type: Union[Unset, CSSCMSCoreEnumsCertStoreEntryParameterType] = UNSET
    required_when: Union[Unset, CSSCMSCoreEnumsEntryParameterUsageFlags] = UNSET
    depends_on: Union[Unset, None, str] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    options: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_type_id = self.store_type_id
        name = self.name
        display_name = self.display_name
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        required_when: Union[Unset, int] = UNSET
        if not isinstance(self.required_when, Unset):
            required_when = self.required_when.value

        depends_on = self.depends_on
        default_value = self.default_value
        options = self.options

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
        if required_when is not UNSET:
            field_dict["requiredWhen"] = required_when
        if depends_on is not UNSET:
            field_dict["dependsOn"] = depends_on
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        store_type_id = d.pop("storeTypeId", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CSSCMSCoreEnumsCertStoreEntryParameterType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CSSCMSCoreEnumsCertStoreEntryParameterType(_type)

        _required_when = d.pop("requiredWhen", UNSET)
        required_when: Union[Unset, CSSCMSCoreEnumsEntryParameterUsageFlags]
        if isinstance(_required_when, Unset):
            required_when = UNSET
        else:
            required_when = CSSCMSCoreEnumsEntryParameterUsageFlags(_required_when)

        depends_on = d.pop("dependsOn", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        options = d.pop("options", UNSET)

        csscms_data_model_models_certificate_store_types_certificate_store_type_entry_parameter = cls(
            store_type_id=store_type_id,
            name=name,
            display_name=display_name,
            type=type,
            required_when=required_when,
            depends_on=depends_on,
            default_value=default_value,
            options=options,
        )

        return csscms_data_model_models_certificate_store_types_certificate_store_type_entry_parameter
