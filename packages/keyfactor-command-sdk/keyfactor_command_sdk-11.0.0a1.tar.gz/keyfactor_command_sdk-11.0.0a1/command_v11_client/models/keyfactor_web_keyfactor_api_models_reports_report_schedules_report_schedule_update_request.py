from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
    from ..models.keyfactor_web_keyfactor_api_models_reports_report_schedules_report_schedule_update_request_runtime_parameters import (
        KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleUpdateRequestRuntimeParameters,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleUpdateRequest:
    """
    Attributes:
        id (int):
        report_format (str):
        runtime_parameters
            (KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleUpdateRequestRuntimeParameters):
        send_report (Union[Unset, bool]):
        save_report (Union[Unset, bool]):
        save_report_path (Union[Unset, None, str]):
        keyfactor_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        certificate_collection_id (Union[Unset, None, int]):
        email_recipients (Union[Unset, None, List[str]]):
    """

    id: int
    report_format: str
    runtime_parameters: "KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleUpdateRequestRuntimeParameters"
    send_report: Union[Unset, bool] = UNSET
    save_report: Union[Unset, bool] = UNSET
    save_report_path: Union[Unset, None, str] = UNSET
    keyfactor_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    certificate_collection_id: Union[Unset, None, int] = UNSET
    email_recipients: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        report_format = self.report_format
        runtime_parameters = self.runtime_parameters.to_dict()

        send_report = self.send_report
        save_report = self.save_report
        save_report_path = self.save_report_path
        keyfactor_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.keyfactor_schedule, Unset):
            keyfactor_schedule = self.keyfactor_schedule.to_dict()

        certificate_collection_id = self.certificate_collection_id
        email_recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.email_recipients, Unset):
            if self.email_recipients is None:
                email_recipients = None
            else:
                email_recipients = self.email_recipients

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "reportFormat": report_format,
                "runtimeParameters": runtime_parameters,
            }
        )
        if send_report is not UNSET:
            field_dict["sendReport"] = send_report
        if save_report is not UNSET:
            field_dict["saveReport"] = save_report
        if save_report_path is not UNSET:
            field_dict["saveReportPath"] = save_report_path
        if keyfactor_schedule is not UNSET:
            field_dict["keyfactorSchedule"] = keyfactor_schedule
        if certificate_collection_id is not UNSET:
            field_dict["certificateCollectionId"] = certificate_collection_id
        if email_recipients is not UNSET:
            field_dict["emailRecipients"] = email_recipients

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
        from ..models.keyfactor_web_keyfactor_api_models_reports_report_schedules_report_schedule_update_request_runtime_parameters import (
            KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleUpdateRequestRuntimeParameters,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        report_format = d.pop("reportFormat")

        runtime_parameters = (
            KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleUpdateRequestRuntimeParameters.from_dict(
                d.pop("runtimeParameters")
            )
        )

        send_report = d.pop("sendReport", UNSET)

        save_report = d.pop("saveReport", UNSET)

        save_report_path = d.pop("saveReportPath", UNSET)

        _keyfactor_schedule = d.pop("keyfactorSchedule", UNSET)
        keyfactor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_keyfactor_schedule, Unset):
            keyfactor_schedule = UNSET
        else:
            keyfactor_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_keyfactor_schedule)

        certificate_collection_id = d.pop("certificateCollectionId", UNSET)

        email_recipients = cast(List[str], d.pop("emailRecipients", UNSET))

        keyfactor_web_keyfactor_api_models_reports_report_schedules_report_schedule_update_request = cls(
            id=id,
            report_format=report_format,
            runtime_parameters=runtime_parameters,
            send_report=send_report,
            save_report=save_report,
            save_report_path=save_report_path,
            keyfactor_schedule=keyfactor_schedule,
            certificate_collection_id=certificate_collection_id,
            email_recipients=email_recipients,
        )

        return keyfactor_web_keyfactor_api_models_reports_report_schedules_report_schedule_update_request
