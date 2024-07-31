import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_orchestrator_jobs_bulk_orchestrator_job_pair import (
        CSSCMSDataModelModelsOrchestratorJobsBulkOrchestratorJobPair,
    )
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
    from ..models.keyfactor_web_keyfactor_api_models_orchestrator_jobs_job_field_response import (
        KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorJobsBulkJobResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorJobsBulkJobResponse:
    """
    Attributes:
        job_type_name (Union[Unset, None, str]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        job_fields (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse']]):
        request_timestamp (Union[Unset, datetime.datetime]):
        orchestrator_job_pairs (Union[Unset, None,
            List['CSSCMSDataModelModelsOrchestratorJobsBulkOrchestratorJobPair']]):
        failed_orchestrator_ids (Union[Unset, None, List[str]]):
    """

    job_type_name: Union[Unset, None, str] = UNSET
    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    job_fields: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsOrchestratorJobsJobFieldResponse"]] = UNSET
    request_timestamp: Union[Unset, datetime.datetime] = UNSET
    orchestrator_job_pairs: Union[
        Unset, None, List["CSSCMSDataModelModelsOrchestratorJobsBulkOrchestratorJobPair"]
    ] = UNSET
    failed_orchestrator_ids: Union[Unset, None, List[str]] = UNSET

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

        orchestrator_job_pairs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orchestrator_job_pairs, Unset):
            if self.orchestrator_job_pairs is None:
                orchestrator_job_pairs = None
            else:
                orchestrator_job_pairs = []
                for orchestrator_job_pairs_item_data in self.orchestrator_job_pairs:
                    orchestrator_job_pairs_item = orchestrator_job_pairs_item_data.to_dict()

                    orchestrator_job_pairs.append(orchestrator_job_pairs_item)

        failed_orchestrator_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.failed_orchestrator_ids, Unset):
            if self.failed_orchestrator_ids is None:
                failed_orchestrator_ids = None
            else:
                failed_orchestrator_ids = self.failed_orchestrator_ids

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
        if orchestrator_job_pairs is not UNSET:
            field_dict["orchestratorJobPairs"] = orchestrator_job_pairs
        if failed_orchestrator_ids is not UNSET:
            field_dict["failedOrchestratorIds"] = failed_orchestrator_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_orchestrator_jobs_bulk_orchestrator_job_pair import (
            CSSCMSDataModelModelsOrchestratorJobsBulkOrchestratorJobPair,
        )
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

        orchestrator_job_pairs = []
        _orchestrator_job_pairs = d.pop("orchestratorJobPairs", UNSET)
        for orchestrator_job_pairs_item_data in _orchestrator_job_pairs or []:
            orchestrator_job_pairs_item = CSSCMSDataModelModelsOrchestratorJobsBulkOrchestratorJobPair.from_dict(
                orchestrator_job_pairs_item_data
            )

            orchestrator_job_pairs.append(orchestrator_job_pairs_item)

        failed_orchestrator_ids = cast(List[str], d.pop("failedOrchestratorIds", UNSET))

        keyfactor_web_keyfactor_api_models_orchestrator_jobs_bulk_job_response = cls(
            job_type_name=job_type_name,
            schedule=schedule,
            job_fields=job_fields,
            request_timestamp=request_timestamp,
            orchestrator_job_pairs=orchestrator_job_pairs,
            failed_orchestrator_ids=failed_orchestrator_ids,
        )

        return keyfactor_web_keyfactor_api_models_orchestrator_jobs_bulk_job_response
