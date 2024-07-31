from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsReportParametersRequest")


@_attrs_define
class CSSCMSDataModelModelsReportParametersRequest:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        default_value (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    default_value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        description = self.description
        default_value = self.default_value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        csscms_data_model_models_report_parameters_request = cls(
            id=id,
            display_name=display_name,
            description=description,
            default_value=default_value,
        )

        return csscms_data_model_models_report_parameters_request
