from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorJobsRescheduleJobRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorJobsRescheduleJobRequest:
    """Class representing orchestrator jobs to be rescheduled

    Attributes:
        job_audit_ids (Union[Unset, None, List[int]]): List of orchestrator job audit ids to be rescheduled
        query (Union[Unset, None, str]): Query identifying orchestrator jobs to be rescheduled
    """

    job_audit_ids: Union[Unset, None, List[int]] = UNSET
    query: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        job_audit_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.job_audit_ids, Unset):
            if self.job_audit_ids is None:
                job_audit_ids = None
            else:
                job_audit_ids = self.job_audit_ids

        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if job_audit_ids is not UNSET:
            field_dict["jobAuditIds"] = job_audit_ids
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        job_audit_ids = cast(List[int], d.pop("jobAuditIds", UNSET))

        query = d.pop("query", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrator_jobs_reschedule_job_request = cls(
            job_audit_ids=job_audit_ids,
            query=query,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_jobs_reschedule_job_request
