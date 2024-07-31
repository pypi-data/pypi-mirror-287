from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
    from ..models.keyfactor_web_keyfactor_api_models_reports_report_schedules_report_schedule_response_runtime_parameters import (
        KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleResponseRuntimeParameters,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        send_report (Union[Unset, bool]):
        save_report (Union[Unset, bool]):
        save_report_path (Union[Unset, None, str]):
        report_format (Union[Unset, None, str]):
        keyfactor_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        certificate_collection_id (Union[Unset, int]):
        email_recipients (Union[Unset, None, List[str]]):
        runtime_parameters (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleResponseRuntimeParameters]):
    """

    id: Union[Unset, int] = UNSET
    send_report: Union[Unset, bool] = UNSET
    save_report: Union[Unset, bool] = UNSET
    save_report_path: Union[Unset, None, str] = UNSET
    report_format: Union[Unset, None, str] = UNSET
    keyfactor_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    certificate_collection_id: Union[Unset, int] = UNSET
    email_recipients: Union[Unset, None, List[str]] = UNSET
    runtime_parameters: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleResponseRuntimeParameters"
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        send_report = self.send_report
        save_report = self.save_report
        save_report_path = self.save_report_path
        report_format = self.report_format
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

        runtime_parameters: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.runtime_parameters, Unset):
            runtime_parameters = self.runtime_parameters.to_dict() if self.runtime_parameters else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if send_report is not UNSET:
            field_dict["sendReport"] = send_report
        if save_report is not UNSET:
            field_dict["saveReport"] = save_report
        if save_report_path is not UNSET:
            field_dict["saveReportPath"] = save_report_path
        if report_format is not UNSET:
            field_dict["reportFormat"] = report_format
        if keyfactor_schedule is not UNSET:
            field_dict["keyfactorSchedule"] = keyfactor_schedule
        if certificate_collection_id is not UNSET:
            field_dict["certificateCollectionId"] = certificate_collection_id
        if email_recipients is not UNSET:
            field_dict["emailRecipients"] = email_recipients
        if runtime_parameters is not UNSET:
            field_dict["runtimeParameters"] = runtime_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
        from ..models.keyfactor_web_keyfactor_api_models_reports_report_schedules_report_schedule_response_runtime_parameters import (
            KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleResponseRuntimeParameters,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        send_report = d.pop("sendReport", UNSET)

        save_report = d.pop("saveReport", UNSET)

        save_report_path = d.pop("saveReportPath", UNSET)

        report_format = d.pop("reportFormat", UNSET)

        _keyfactor_schedule = d.pop("keyfactorSchedule", UNSET)
        keyfactor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_keyfactor_schedule, Unset):
            keyfactor_schedule = UNSET
        else:
            keyfactor_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_keyfactor_schedule)

        certificate_collection_id = d.pop("certificateCollectionId", UNSET)

        email_recipients = cast(List[str], d.pop("emailRecipients", UNSET))

        _runtime_parameters = d.pop("runtimeParameters", UNSET)
        runtime_parameters: Union[
            Unset, None, KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleResponseRuntimeParameters
        ]
        if _runtime_parameters is None:
            runtime_parameters = None
        elif isinstance(_runtime_parameters, Unset):
            runtime_parameters = UNSET
        else:
            runtime_parameters = (
                KeyfactorWebKeyfactorApiModelsReportsReportSchedulesReportScheduleResponseRuntimeParameters.from_dict(
                    _runtime_parameters
                )
            )

        keyfactor_web_keyfactor_api_models_reports_report_schedules_report_schedule_response = cls(
            id=id,
            send_report=send_report,
            save_report=save_report,
            save_report_path=save_report_path,
            report_format=report_format,
            keyfactor_schedule=keyfactor_schedule,
            certificate_collection_id=certificate_collection_id,
            email_recipients=email_recipients,
            runtime_parameters=runtime_parameters,
        )

        return keyfactor_web_keyfactor_api_models_reports_report_schedules_report_schedule_response
