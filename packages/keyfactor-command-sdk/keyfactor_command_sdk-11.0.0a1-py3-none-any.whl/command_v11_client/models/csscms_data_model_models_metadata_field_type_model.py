from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_metadata_data_type import CSSCMSCoreEnumsMetadataDataType
from ..models.csscms_core_enums_metadata_type_enrollment import CSSCMSCoreEnumsMetadataTypeEnrollment
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsMetadataFieldTypeModel")


@_attrs_define
class CSSCMSDataModelModelsMetadataFieldTypeModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        data_type (Union[Unset, CSSCMSCoreEnumsMetadataDataType]):
        hint (Union[Unset, None, str]):
        validation (Union[Unset, None, str]):
        enrollment (Union[Unset, CSSCMSCoreEnumsMetadataTypeEnrollment]):
        message (Union[Unset, None, str]):
        options (Union[Unset, None, str]):
        default_value (Union[Unset, None, str]):
        allow_api (Union[Unset, bool]):
        explicit_update (Union[Unset, bool]):
        display_order (Union[Unset, None, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    data_type: Union[Unset, CSSCMSCoreEnumsMetadataDataType] = UNSET
    hint: Union[Unset, None, str] = UNSET
    validation: Union[Unset, None, str] = UNSET
    enrollment: Union[Unset, CSSCMSCoreEnumsMetadataTypeEnrollment] = UNSET
    message: Union[Unset, None, str] = UNSET
    options: Union[Unset, None, str] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    allow_api: Union[Unset, bool] = UNSET
    explicit_update: Union[Unset, bool] = UNSET
    display_order: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        data_type: Union[Unset, int] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        hint = self.hint
        validation = self.validation
        enrollment: Union[Unset, int] = UNSET
        if not isinstance(self.enrollment, Unset):
            enrollment = self.enrollment.value

        message = self.message
        options = self.options
        default_value = self.default_value
        allow_api = self.allow_api
        explicit_update = self.explicit_update
        display_order = self.display_order

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if hint is not UNSET:
            field_dict["hint"] = hint
        if validation is not UNSET:
            field_dict["validation"] = validation
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if message is not UNSET:
            field_dict["message"] = message
        if options is not UNSET:
            field_dict["options"] = options
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if allow_api is not UNSET:
            field_dict["allowAPI"] = allow_api
        if explicit_update is not UNSET:
            field_dict["explicitUpdate"] = explicit_update
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, CSSCMSCoreEnumsMetadataDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = CSSCMSCoreEnumsMetadataDataType(_data_type)

        hint = d.pop("hint", UNSET)

        validation = d.pop("validation", UNSET)

        _enrollment = d.pop("enrollment", UNSET)
        enrollment: Union[Unset, CSSCMSCoreEnumsMetadataTypeEnrollment]
        if isinstance(_enrollment, Unset):
            enrollment = UNSET
        else:
            enrollment = CSSCMSCoreEnumsMetadataTypeEnrollment(_enrollment)

        message = d.pop("message", UNSET)

        options = d.pop("options", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        allow_api = d.pop("allowAPI", UNSET)

        explicit_update = d.pop("explicitUpdate", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        csscms_data_model_models_metadata_field_type_model = cls(
            id=id,
            name=name,
            description=description,
            data_type=data_type,
            hint=hint,
            validation=validation,
            enrollment=enrollment,
            message=message,
            options=options,
            default_value=default_value,
            allow_api=allow_api,
            explicit_update=explicit_update,
            display_order=display_order,
        )

        return csscms_data_model_models_metadata_field_type_model
