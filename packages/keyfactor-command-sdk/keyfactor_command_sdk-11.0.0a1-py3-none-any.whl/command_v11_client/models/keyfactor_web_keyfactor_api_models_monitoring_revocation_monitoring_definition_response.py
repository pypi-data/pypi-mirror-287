from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
    from ..models.keyfactor_web_keyfactor_api_models_monitoring_dashboard_response import (
        KeyfactorWebKeyfactorApiModelsMonitoringDashboardResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_monitoring_email_response import (
        KeyfactorWebKeyfactorApiModelsMonitoringEmailResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_monitoring_ocsp_parameters_response import (
        KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        endpoint_type (Union[Unset, None, str]):
        location (Union[Unset, None, str]):
        email (Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringEmailResponse]):
        dashboard (Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringDashboardResponse]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        ocsp_parameters (Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersResponse]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    endpoint_type: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    email: Union[Unset, "KeyfactorWebKeyfactorApiModelsMonitoringEmailResponse"] = UNSET
    dashboard: Union[Unset, "KeyfactorWebKeyfactorApiModelsMonitoringDashboardResponse"] = UNSET
    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    ocsp_parameters: Union[Unset, "KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersResponse"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        endpoint_type = self.endpoint_type
        location = self.location
        email: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        dashboard: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dashboard, Unset):
            dashboard = self.dashboard.to_dict()

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        ocsp_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ocsp_parameters, Unset):
            ocsp_parameters = self.ocsp_parameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if endpoint_type is not UNSET:
            field_dict["endpointType"] = endpoint_type
        if location is not UNSET:
            field_dict["location"] = location
        if email is not UNSET:
            field_dict["email"] = email
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if ocsp_parameters is not UNSET:
            field_dict["ocspParameters"] = ocsp_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
        from ..models.keyfactor_web_keyfactor_api_models_monitoring_dashboard_response import (
            KeyfactorWebKeyfactorApiModelsMonitoringDashboardResponse,
        )
        from ..models.keyfactor_web_keyfactor_api_models_monitoring_email_response import (
            KeyfactorWebKeyfactorApiModelsMonitoringEmailResponse,
        )
        from ..models.keyfactor_web_keyfactor_api_models_monitoring_ocsp_parameters_response import (
            KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        endpoint_type = d.pop("endpointType", UNSET)

        location = d.pop("location", UNSET)

        _email = d.pop("email", UNSET)
        email: Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringEmailResponse]
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = KeyfactorWebKeyfactorApiModelsMonitoringEmailResponse.from_dict(_email)

        _dashboard = d.pop("dashboard", UNSET)
        dashboard: Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringDashboardResponse]
        if isinstance(_dashboard, Unset):
            dashboard = UNSET
        else:
            dashboard = KeyfactorWebKeyfactorApiModelsMonitoringDashboardResponse.from_dict(_dashboard)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        _ocsp_parameters = d.pop("ocspParameters", UNSET)
        ocsp_parameters: Union[Unset, KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersResponse]
        if isinstance(_ocsp_parameters, Unset):
            ocsp_parameters = UNSET
        else:
            ocsp_parameters = KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersResponse.from_dict(_ocsp_parameters)

        keyfactor_web_keyfactor_api_models_monitoring_revocation_monitoring_definition_response = cls(
            id=id,
            name=name,
            endpoint_type=endpoint_type,
            location=location,
            email=email,
            dashboard=dashboard,
            schedule=schedule,
            ocsp_parameters=ocsp_parameters,
        )

        return keyfactor_web_keyfactor_api_models_monitoring_revocation_monitoring_definition_response
