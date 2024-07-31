from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_data_type import CSSCMSDataModelEnumsDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobTypeFieldResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobTypeFieldResponse:
    """
    Attributes:
        name (Union[Unset, None, str]):
        type (Union[Unset, CSSCMSDataModelEnumsDataType]):
        default_value (Union[Unset, None, str]):
        required (Union[Unset, bool]):
    """

    name: Union[Unset, None, str] = UNSET
    type: Union[Unset, CSSCMSDataModelEnumsDataType] = UNSET
    default_value: Union[Unset, None, str] = UNSET
    required: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        default_value = self.default_value
        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CSSCMSDataModelEnumsDataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CSSCMSDataModelEnumsDataType(_type)

        default_value = d.pop("defaultValue", UNSET)

        required = d.pop("required", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrator_jobs_job_type_field_response = cls(
            name=name,
            type=type,
            default_value=default_value,
            required=required,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_jobs_job_type_field_response
