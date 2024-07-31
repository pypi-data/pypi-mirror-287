from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsOrchestratorJobsJob")


@_attrs_define
class CSSCMSDataModelModelsOrchestratorJobsJob:
    """
    Attributes:
        id (Union[Unset, str]):
        client_machine (Union[Unset, None, str]):
        target (Union[Unset, None, str]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        requested (Union[Unset, None, str]):
        job_type (Union[Unset, None, str]):
    """

    id: Union[Unset, str] = UNSET
    client_machine: Union[Unset, None, str] = UNSET
    target: Union[Unset, None, str] = UNSET
    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    requested: Union[Unset, None, str] = UNSET
    job_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        client_machine = self.client_machine
        target = self.target
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        requested = self.requested
        job_type = self.job_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine
        if target is not UNSET:
            field_dict["target"] = target
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if requested is not UNSET:
            field_dict["requested"] = requested
        if job_type is not UNSET:
            field_dict["jobType"] = job_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        client_machine = d.pop("clientMachine", UNSET)

        target = d.pop("target", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        requested = d.pop("requested", UNSET)

        job_type = d.pop("jobType", UNSET)

        csscms_data_model_models_orchestrator_jobs_job = cls(
            id=id,
            client_machine=client_machine,
            target=target,
            schedule=schedule,
            requested=requested,
            job_type=job_type,
        )

        return csscms_data_model_models_orchestrator_jobs_job
