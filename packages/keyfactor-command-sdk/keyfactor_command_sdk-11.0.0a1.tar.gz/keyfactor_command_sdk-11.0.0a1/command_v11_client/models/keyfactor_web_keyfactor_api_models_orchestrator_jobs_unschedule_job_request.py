from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorJobsUnscheduleJobRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorJobsUnscheduleJobRequest:
    """Class representing orchestrator jobs to be unscheduled

    Attributes:
        job_ids (Union[Unset, None, List[str]]): List of orchestrator job ids to be unscheduled
        query (Union[Unset, None, str]): Query identifying orchestrator jobs to be unscheduled
    """

    job_ids: Union[Unset, None, List[str]] = UNSET
    query: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        job_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.job_ids, Unset):
            if self.job_ids is None:
                job_ids = None
            else:
                job_ids = self.job_ids

        query = self.query

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if job_ids is not UNSET:
            field_dict["jobIds"] = job_ids
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        job_ids = cast(List[str], d.pop("jobIds", UNSET))

        query = d.pop("query", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrator_jobs_unschedule_job_request = cls(
            job_ids=job_ids,
            query=query,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_jobs_unschedule_job_request
