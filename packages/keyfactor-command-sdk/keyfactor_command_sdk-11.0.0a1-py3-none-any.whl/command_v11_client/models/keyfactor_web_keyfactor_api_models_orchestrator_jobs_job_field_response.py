from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse:
    """
    Attributes:
        job_type_field (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
    """

    job_type_field: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        job_type_field = self.job_type_field
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if job_type_field is not UNSET:
            field_dict["jobTypeField"] = job_type_field
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        job_type_field = d.pop("jobTypeField", UNSET)

        value = d.pop("value", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrator_jobs_job_field_response = cls(
            job_type_field=job_type_field,
            value=value,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_jobs_job_field_response
