import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
    from ..models.keyfactor_web_keyfactor_api_models_orchestrator_jobs_job_field_response import (
        KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobResponse:
    """
    Attributes:
        job_type_name (Union[Unset, None, str]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        job_fields (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse']]):
        request_timestamp (Union[Unset, datetime.datetime]):
        job_id (Union[Unset, str]):
        orchestrator_id (Union[Unset, str]):
    """

    job_type_name: Union[Unset, None, str] = UNSET
    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    job_fields: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse"]] = UNSET
    request_timestamp: Union[Unset, datetime.datetime] = UNSET
    job_id: Union[Unset, str] = UNSET
    orchestrator_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        job_type_name = self.job_type_name
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        job_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_fields, Unset):
            if self.job_fields is None:
                job_fields = None
            else:
                job_fields = []
                for job_fields_item_data in self.job_fields:
                    job_fields_item = job_fields_item_data.to_dict()

                    job_fields.append(job_fields_item)

        request_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.request_timestamp, Unset):
            request_timestamp = self.request_timestamp.isoformat()[:-6]+'Z'

        job_id = self.job_id
        orchestrator_id = self.orchestrator_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if job_type_name is not UNSET:
            field_dict["jobTypeName"] = job_type_name
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if job_fields is not UNSET:
            field_dict["jobFields"] = job_fields
        if request_timestamp is not UNSET:
            field_dict["requestTimestamp"] = request_timestamp
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if orchestrator_id is not UNSET:
            field_dict["orchestratorId"] = orchestrator_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
        from ..models.keyfactor_web_keyfactor_api_models_orchestrator_jobs_job_field_response import (
            KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        job_type_name = d.pop("jobTypeName", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        job_fields = []
        _job_fields = d.pop("jobFields", UNSET)
        for job_fields_item_data in _job_fields or []:
            job_fields_item = KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse.from_dict(
                job_fields_item_data
            )

            job_fields.append(job_fields_item)

        _request_timestamp = d.pop("requestTimestamp", UNSET)
        request_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_request_timestamp, Unset):
            request_timestamp = UNSET
        else:
            request_timestamp = isoparse(_request_timestamp)

        job_id = d.pop("jobId", UNSET)

        orchestrator_id = d.pop("orchestratorId", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrator_jobs_job_response = cls(
            job_type_name=job_type_name,
            schedule=schedule,
            job_fields=job_fields,
            request_timestamp=request_timestamp,
            job_id=job_id,
            orchestrator_id=orchestrator_id,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_jobs_job_response
