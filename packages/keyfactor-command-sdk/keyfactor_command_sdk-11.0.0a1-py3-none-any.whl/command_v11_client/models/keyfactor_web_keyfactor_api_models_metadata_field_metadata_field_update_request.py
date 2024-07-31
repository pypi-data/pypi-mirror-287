from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_metadata_data_type import CSSCMSCoreEnumsMetadataDataType
from ..models.csscms_core_enums_metadata_type_enrollment import CSSCMSCoreEnumsMetadataTypeEnrollment
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsMetadataFieldMetadataFieldUpdateRequest:
    """
    Attributes:
        id (int):
        name (str):
        description (str):
        data_type (CSSCMSCoreEnumsMetadataDataType):
        display_order (int):
        hint (Union[Unset, None, str]):
        validation (Union[Unset, None, str]):
        enrollment (Union[Unset, CSSCMSCoreEnumsMetadataTypeEnrollment]):
        message (Union[Unset, None, str]):
        options (Union[Unset, None, str]):
        default_value (Union[Unset, None, str]):
        allow_api (Union[Unset, bool]):
        explicit_update (Union[Unset, bool]):
    """

    id: int
    name: str
    description: str
    data_type: CSSCMSCoreEnumsMetadataDataType
    display_order: int
    hint: Union[Unset, None, str] = UNSET
    validation: Union[Unset, None, str] = UNSET
    enrollment: Union[Unset, CSSCMSCoreEnumsMetadataTypeEnrollment] = UNSET
    message: Union[Unset, None, str] = UNSET
    options: Union[Unset, None, str] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    allow_api: Union[Unset, bool] = UNSET
    explicit_update: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        data_type = self.data_type.value

        display_order = self.display_order
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "dataType": data_type,
                "displayOrder": display_order,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        data_type = CSSCMSCoreEnumsMetadataDataType(d.pop("dataType"))

        display_order = d.pop("displayOrder")

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

        keyfactor_web_keyfactor_api_models_metadata_field_metadata_field_update_request = cls(
            id=id,
            name=name,
            description=description,
            data_type=data_type,
            display_order=display_order,
            hint=hint,
            validation=validation,
            enrollment=enrollment,
            message=message,
            options=options,
            default_value=default_value,
            allow_api=allow_api,
            explicit_update=explicit_update,
        )

        return keyfactor_web_keyfactor_api_models_metadata_field_metadata_field_update_request
