import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_orchestrators_common_enums_orchestrator_job_status_job_result import (
    KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobResult,
)
from ..models.keyfactor_orchestrators_common_enums_orchestrator_job_status_job_status import (
    KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateStoresJobHistoryResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateStoresJobHistoryResponse:
    """
    Attributes:
        job_history_id (Union[Unset, int]):
        agent_machine (Union[Unset, None, str]):
        job_id (Union[Unset, str]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        job_type (Union[Unset, None, str]):
        operation_start (Union[Unset, datetime.datetime]):
        operation_end (Union[Unset, None, datetime.datetime]):
        message (Union[Unset, None, str]):
        result (Union[Unset, KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobResult]):
        status (Union[Unset, KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobStatus]):
        store_path (Union[Unset, None, str]):
        client_machine (Union[Unset, None, str]):
    """

    job_history_id: Union[Unset, int] = UNSET
    agent_machine: Union[Unset, None, str] = UNSET
    job_id: Union[Unset, str] = UNSET
    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    job_type: Union[Unset, None, str] = UNSET
    operation_start: Union[Unset, datetime.datetime] = UNSET
    operation_end: Union[Unset, None, datetime.datetime] = UNSET
    message: Union[Unset, None, str] = UNSET
    result: Union[Unset, KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobResult] = UNSET
    status: Union[Unset, KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobStatus] = UNSET
    store_path: Union[Unset, None, str] = UNSET
    client_machine: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        job_history_id = self.job_history_id
        agent_machine = self.agent_machine
        job_id = self.job_id
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        job_type = self.job_type
        operation_start: Union[Unset, str] = UNSET
        if not isinstance(self.operation_start, Unset):
            operation_start = self.operation_start.isoformat()[:-6]+'Z'

        operation_end: Union[Unset, None, str] = UNSET
        if not isinstance(self.operation_end, Unset):
            operation_end = self.operation_end.isoformat()[:-6]+'Z' if self.operation_end else None

        message = self.message
        result: Union[Unset, int] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        store_path = self.store_path
        client_machine = self.client_machine

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if job_history_id is not UNSET:
            field_dict["jobHistoryId"] = job_history_id
        if agent_machine is not UNSET:
            field_dict["agentMachine"] = agent_machine
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if operation_start is not UNSET:
            field_dict["operationStart"] = operation_start
        if operation_end is not UNSET:
            field_dict["operationEnd"] = operation_end
        if message is not UNSET:
            field_dict["message"] = message
        if result is not UNSET:
            field_dict["result"] = result
        if status is not UNSET:
            field_dict["status"] = status
        if store_path is not UNSET:
            field_dict["storePath"] = store_path
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        job_history_id = d.pop("jobHistoryId", UNSET)

        agent_machine = d.pop("agentMachine", UNSET)

        job_id = d.pop("jobId", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        job_type = d.pop("jobType", UNSET)

        _operation_start = d.pop("operationStart", UNSET)
        operation_start: Union[Unset, datetime.datetime]
        if isinstance(_operation_start, Unset):
            operation_start = UNSET
        else:
            operation_start = isoparse(_operation_start)

        _operation_end = d.pop("operationEnd", UNSET)
        operation_end: Union[Unset, None, datetime.datetime]
        if _operation_end is None:
            operation_end = None
        elif isinstance(_operation_end, Unset):
            operation_end = UNSET
        else:
            operation_end = isoparse(_operation_end)

        message = d.pop("message", UNSET)

        _result = d.pop("result", UNSET)
        result: Union[Unset, KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobResult(_result)

        _status = d.pop("status", UNSET)
        status: Union[Unset, KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = KeyfactorOrchestratorsCommonEnumsOrchestratorJobStatusJobStatus(_status)

        store_path = d.pop("storePath", UNSET)

        client_machine = d.pop("clientMachine", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_stores_job_history_response = cls(
            job_history_id=job_history_id,
            agent_machine=agent_machine,
            job_id=job_id,
            schedule=schedule,
            job_type=job_type,
            operation_start=operation_start,
            operation_end=operation_end,
            message=message,
            result=result,
            status=status,
            store_path=store_path,
            client_machine=client_machine,
        )

        return keyfactor_web_keyfactor_api_models_certificate_stores_job_history_response
