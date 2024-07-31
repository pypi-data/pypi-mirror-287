from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorJobsCustomJobResultDataResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorJobsCustomJobResultDataResponse:
    """
    Attributes:
        job_history_id (Union[Unset, int]):
        data (Union[Unset, None, str]):
    """

    job_history_id: Union[Unset, int] = UNSET
    data: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        job_history_id = self.job_history_id
        data = self.data

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if job_history_id is not UNSET:
            field_dict["jobHistoryId"] = job_history_id
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        job_history_id = d.pop("jobHistoryId", UNSET)

        data = d.pop("data", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrator_jobs_custom_job_result_data_response = cls(
            job_history_id=job_history_id,
            data=data,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_jobs_custom_job_result_data_response
