from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsOrchestratorJobsBulkOrchestratorJobPair")


@_attrs_define
class CSSCMSDataModelModelsOrchestratorJobsBulkOrchestratorJobPair:
    """
    Attributes:
        job_id (Union[Unset, str]):
        orchestrator_id (Union[Unset, str]):
    """

    job_id: Union[Unset, str] = UNSET
    orchestrator_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        orchestrator_id = self.orchestrator_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if orchestrator_id is not UNSET:
            field_dict["orchestratorId"] = orchestrator_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        job_id = d.pop("jobId", UNSET)

        orchestrator_id = d.pop("orchestratorId", UNSET)

        csscms_data_model_models_orchestrator_jobs_bulk_orchestrator_job_pair = cls(
            job_id=job_id,
            orchestrator_id=orchestrator_id,
        )

        return csscms_data_model_models_orchestrator_jobs_bulk_orchestrator_job_pair
