from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_report_parameter_type import CSSCMSCoreEnumsReportParameterType
from ..models.csscms_core_enums_report_parameter_visibility import CSSCMSCoreEnumsReportParameterVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsReportParameters")


@_attrs_define
class CSSCMSDataModelModelsReportParameters:
    """
    Attributes:
        id (Union[Unset, int]):
        parameter_name (Union[Unset, None, str]):
        parameter_type (Union[Unset, CSSCMSCoreEnumsReportParameterType]):
        display_name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        default_value (Union[Unset, None, str]):
        display_order (Union[Unset, int]):
        parameter_visibility (Union[Unset, CSSCMSCoreEnumsReportParameterVisibility]):
    """

    id: Union[Unset, int] = UNSET
    parameter_name: Union[Unset, None, str] = UNSET
    parameter_type: Union[Unset, CSSCMSCoreEnumsReportParameterType] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    parameter_visibility: Union[Unset, CSSCMSCoreEnumsReportParameterVisibility] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parameter_name = self.parameter_name
        parameter_type: Union[Unset, int] = UNSET
        if not isinstance(self.parameter_type, Unset):
            parameter_type = self.parameter_type.value

        display_name = self.display_name
        description = self.description
        default_value = self.default_value
        display_order = self.display_order
        parameter_visibility: Union[Unset, int] = UNSET
        if not isinstance(self.parameter_visibility, Unset):
            parameter_visibility = self.parameter_visibility.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parameter_name is not UNSET:
            field_dict["parameterName"] = parameter_name
        if parameter_type is not UNSET:
            field_dict["parameterType"] = parameter_type
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if parameter_visibility is not UNSET:
            field_dict["parameterVisibility"] = parameter_visibility

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        parameter_name = d.pop("parameterName", UNSET)

        _parameter_type = d.pop("parameterType", UNSET)
        parameter_type: Union[Unset, CSSCMSCoreEnumsReportParameterType]
        if isinstance(_parameter_type, Unset):
            parameter_type = UNSET
        else:
            parameter_type = CSSCMSCoreEnumsReportParameterType(_parameter_type)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        _parameter_visibility = d.pop("parameterVisibility", UNSET)
        parameter_visibility: Union[Unset, CSSCMSCoreEnumsReportParameterVisibility]
        if isinstance(_parameter_visibility, Unset):
            parameter_visibility = UNSET
        else:
            parameter_visibility = CSSCMSCoreEnumsReportParameterVisibility(_parameter_visibility)

        csscms_data_model_models_report_parameters = cls(
            id=id,
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            display_name=display_name,
            description=description,
            default_value=default_value,
            display_order=display_order,
            parameter_visibility=parameter_visibility,
        )

        return csscms_data_model_models_report_parameters
