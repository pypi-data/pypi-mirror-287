from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
    from ..models.keyfactor_web_keyfactor_api_models_monitoring_dashboard_request import (
        KeyfactorWebKeyfactorApiModelsMonitoringDashboardRequest,
    )
    from ..models.keyfactor_web_keyfactor_api_models_monitoring_email_request import (
        KeyfactorWebKeyfactorApiModelsMonitoringEmailRequest,
    )
    from ..models.keyfactor_web_keyfactor_api_models_monitoring_ocsp_parameters_request import (
        KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersRequest,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringCreationRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringCreationRequest:
    """
    Attributes:
        name (str):
        endpoint_type (str):
        location (str):
        dashboard (KeyfactorWebKeyfactorApiModelsMonitoringDashboardRequest):
        email (Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringEmailRequest]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        ocsp_parameters (Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersRequest]):
    """

    name: str
    endpoint_type: str
    location: str
    dashboard: "KeyfactorWebKeyfactorApiModelsMonitoringDashboardRequest"
    email: Union[Unset, "KeyfactorWebKeyfactorApiModelsMonitoringEmailRequest"] = UNSET
    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    ocsp_parameters: Union[Unset, "KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersRequest"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        endpoint_type = self.endpoint_type
        location = self.location
        dashboard = self.dashboard.to_dict()

        email: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        ocsp_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ocsp_parameters, Unset):
            ocsp_parameters = self.ocsp_parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "endpointType": endpoint_type,
                "location": location,
                "dashboard": dashboard,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if ocsp_parameters is not UNSET:
            field_dict["ocspParameters"] = ocsp_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
        from ..models.keyfactor_web_keyfactor_api_models_monitoring_dashboard_request import (
            KeyfactorWebKeyfactorApiModelsMonitoringDashboardRequest,
        )
        from ..models.keyfactor_web_keyfactor_api_models_monitoring_email_request import (
            KeyfactorWebKeyfactorApiModelsMonitoringEmailRequest,
        )
        from ..models.keyfactor_web_keyfactor_api_models_monitoring_ocsp_parameters_request import (
            KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name")

        endpoint_type = d.pop("endpointType")

        location = d.pop("location")

        dashboard = KeyfactorWebKeyfactorApiModelsMonitoringDashboardRequest.from_dict(d.pop("dashboard"))

        _email = d.pop("email", UNSET)
        email: Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringEmailRequest]
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = KeyfactorWebKeyfactorApiModelsMonitoringEmailRequest.from_dict(_email)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        _ocsp_parameters = d.pop("ocspParameters", UNSET)
        ocsp_parameters: Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersRequest]
        if isinstance(_ocsp_parameters, Unset):
            ocsp_parameters = UNSET
        else:
            ocsp_parameters = KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersRequest.from_dict(_ocsp_parameters)

        keyfactor_web_keyfactor_api_models_monitoring_revocation_monitoring_creation_request = cls(
            name=name,
            endpoint_type=endpoint_type,
            location=location,
            dashboard=dashboard,
            email=email,
            schedule=schedule,
            ocsp_parameters=ocsp_parameters,
        )

        return keyfactor_web_keyfactor_api_models_monitoring_revocation_monitoring_creation_request
