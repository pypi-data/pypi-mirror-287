from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_data_type import CSSCMSDataModelEnumsDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsOrchestratorJobsJobTypeFieldRequest")


@_attrs_define
class CSSCMSDataModelModelsOrchestratorJobsJobTypeFieldRequest:
    """
    Attributes:
        name (str):
        type (CSSCMSDataModelEnumsDataType):
        default_value (Union[Unset, None, str]):
        required (Union[Unset, bool]):
    """

    name: str
    type: CSSCMSDataModelEnumsDataType
    default_value: Union[Unset, None, str] = UNSET
    required: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        default_value = self.default_value
        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name")

        type = CSSCMSDataModelEnumsDataType(d.pop("type"))

        default_value = d.pop("defaultValue", UNSET)

        required = d.pop("required", UNSET)

        csscms_data_model_models_orchestrator_jobs_job_type_field_request = cls(
            name=name,
            type=type,
            default_value=default_value,
            required=required,
        )

        return csscms_data_model_models_orchestrator_jobs_job_type_field_request
