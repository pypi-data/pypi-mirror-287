from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_orchestrator_jobs_schedule_job_request_job_fields import (
        CSSCMSDataModelModelsOrchestratorJobsScheduleJobRequestJobFields,
    )
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsOrchestratorJobsScheduleJobRequest")


@_attrs_define
class CSSCMSDataModelModelsOrchestratorJobsScheduleJobRequest:
    """
    Attributes:
        agent_id (str):
        job_type_name (str):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        job_fields (Union[Unset, None, CSSCMSDataModelModelsOrchestratorJobsScheduleJobRequestJobFields]):
    """

    agent_id: str
    job_type_name: str
    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    job_fields: Union[Unset, None, "CSSCMSDataModelModelsOrchestratorJobsScheduleJobRequestJobFields"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id
        job_type_name = self.job_type_name
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        job_fields: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.job_fields, Unset):
            job_fields = self.job_fields.to_dict() if self.job_fields else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "agentId": agent_id,
                "jobTypeName": job_type_name,
            }
        )
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if job_fields is not UNSET:
            field_dict["jobFields"] = job_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_orchestrator_jobs_schedule_job_request_job_fields import (
            CSSCMSDataModelModelsOrchestratorJobsScheduleJobRequestJobFields,
        )
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        agent_id = d.pop("agentId")

        job_type_name = d.pop("jobTypeName")

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        _job_fields = d.pop("jobFields", UNSET)
        job_fields: Union[Unset, None, CSSCMSDataModelModelsOrchestratorJobsScheduleJobRequestJobFields]
        if _job_fields is None:
            job_fields = None
        elif isinstance(_job_fields, Unset):
            job_fields = UNSET
        else:
            job_fields = CSSCMSDataModelModelsOrchestratorJobsScheduleJobRequestJobFields.from_dict(_job_fields)

        csscms_data_model_models_orchestrator_jobs_schedule_job_request = cls(
            agent_id=agent_id,
            job_type_name=job_type_name,
            schedule=schedule,
            job_fields=job_fields,
        )

        return csscms_data_model_models_orchestrator_jobs_schedule_job_request
