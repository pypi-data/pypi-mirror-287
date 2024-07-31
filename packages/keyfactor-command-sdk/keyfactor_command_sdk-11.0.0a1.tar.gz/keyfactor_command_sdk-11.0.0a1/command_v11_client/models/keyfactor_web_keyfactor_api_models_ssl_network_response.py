import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.csscms_core_enums_ssl_network_job_status import CSSCMSCoreEnumsSslNetworkJobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
    from ..models.keyfactor_common_scheduling_models_weekly_model import KeyfactorCommonSchedulingModelsWeeklyModel
    from ..models.keyfactor_web_keyfactor_api_models_ssl_quiet_hour_response import (
        KeyfactorWebKeyfactorApiModelsSslQuietHourResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSslNetworkResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSslNetworkResponse:
    """
    Attributes:
        network_id (Union[Unset, str]):
        name (Union[Unset, None, str]):
        agent_pool_name (Union[Unset, None, str]):
        agent_pool_id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        enabled (Union[Unset, bool]):
        discover_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        monitor_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        discover_percent_complete (Union[Unset, float]):
        monitor_percent_complete (Union[Unset, float]):
        discover_status (Union[Unset, CSSCMSCoreEnumsSslNetworkJobStatus]):
        monitor_status (Union[Unset, CSSCMSCoreEnumsSslNetworkJobStatus]):
        discover_last_scanned (Union[Unset, None, datetime.datetime]):
        monitor_last_scanned (Union[Unset, None, datetime.datetime]):
        ssl_alert_recipients (Union[Unset, None, List[str]]):
        get_robots (Union[Unset, bool]):
        discover_timeout_ms (Union[Unset, float]):
        monitor_timeout_ms (Union[Unset, float]):
        expiration_alert_days (Union[Unset, float]):
        discover_job_parts (Union[Unset, int]):
        monitor_job_parts (Union[Unset, int]):
        quiet_hours (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsSslQuietHourResponse']]):
        blackout_start (Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]):
        blackout_end (Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]):
        auto_monitor (Union[Unset, bool]):
    """

    network_id: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    agent_pool_name: Union[Unset, None, str] = UNSET
    agent_pool_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    discover_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    monitor_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    discover_percent_complete: Union[Unset, float] = UNSET
    monitor_percent_complete: Union[Unset, float] = UNSET
    discover_status: Union[Unset, CSSCMSCoreEnumsSslNetworkJobStatus] = UNSET
    monitor_status: Union[Unset, CSSCMSCoreEnumsSslNetworkJobStatus] = UNSET
    discover_last_scanned: Union[Unset, None, datetime.datetime] = UNSET
    monitor_last_scanned: Union[Unset, None, datetime.datetime] = UNSET
    ssl_alert_recipients: Union[Unset, None, List[str]] = UNSET
    get_robots: Union[Unset, bool] = UNSET
    discover_timeout_ms: Union[Unset, float] = UNSET
    monitor_timeout_ms: Union[Unset, float] = UNSET
    expiration_alert_days: Union[Unset, float] = UNSET
    discover_job_parts: Union[Unset, int] = UNSET
    monitor_job_parts: Union[Unset, int] = UNSET
    quiet_hours: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsSslQuietHourResponse"]] = UNSET
    blackout_start: Union[Unset, "KeyfactorCommonSchedulingModelsWeeklyModel"] = UNSET
    blackout_end: Union[Unset, "KeyfactorCommonSchedulingModelsWeeklyModel"] = UNSET
    auto_monitor: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        network_id = self.network_id
        name = self.name
        agent_pool_name = self.agent_pool_name
        agent_pool_id = self.agent_pool_id
        description = self.description
        enabled = self.enabled
        discover_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discover_schedule, Unset):
            discover_schedule = self.discover_schedule.to_dict()

        monitor_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.monitor_schedule, Unset):
            monitor_schedule = self.monitor_schedule.to_dict()

        discover_percent_complete = self.discover_percent_complete
        monitor_percent_complete = self.monitor_percent_complete
        discover_status: Union[Unset, int] = UNSET
        if not isinstance(self.discover_status, Unset):
            discover_status = self.discover_status.value

        monitor_status: Union[Unset, int] = UNSET
        if not isinstance(self.monitor_status, Unset):
            monitor_status = self.monitor_status.value

        discover_last_scanned: Union[Unset, None, str] = UNSET
        if not isinstance(self.discover_last_scanned, Unset):
            discover_last_scanned = self.discover_last_scanned.isoformat()[:-6]+'Z' if self.discover_last_scanned else None

        monitor_last_scanned: Union[Unset, None, str] = UNSET
        if not isinstance(self.monitor_last_scanned, Unset):
            monitor_last_scanned = self.monitor_last_scanned.isoformat()[:-6]+'Z' if self.monitor_last_scanned else None

        ssl_alert_recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.ssl_alert_recipients, Unset):
            if self.ssl_alert_recipients is None:
                ssl_alert_recipients = None
            else:
                ssl_alert_recipients = self.ssl_alert_recipients

        get_robots = self.get_robots
        discover_timeout_ms = self.discover_timeout_ms
        monitor_timeout_ms = self.monitor_timeout_ms
        expiration_alert_days = self.expiration_alert_days
        discover_job_parts = self.discover_job_parts
        monitor_job_parts = self.monitor_job_parts
        quiet_hours: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quiet_hours, Unset):
            if self.quiet_hours is None:
                quiet_hours = None
            else:
                quiet_hours = []
                for quiet_hours_item_data in self.quiet_hours:
                    quiet_hours_item = quiet_hours_item_data.to_dict()

                    quiet_hours.append(quiet_hours_item)

        blackout_start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.blackout_start, Unset):
            blackout_start = self.blackout_start.to_dict()

        blackout_end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.blackout_end, Unset):
            blackout_end = self.blackout_end.to_dict()

        auto_monitor = self.auto_monitor

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if name is not UNSET:
            field_dict["name"] = name
        if agent_pool_name is not UNSET:
            field_dict["agentPoolName"] = agent_pool_name
        if agent_pool_id is not UNSET:
            field_dict["agentPoolId"] = agent_pool_id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if discover_schedule is not UNSET:
            field_dict["discoverSchedule"] = discover_schedule
        if monitor_schedule is not UNSET:
            field_dict["monitorSchedule"] = monitor_schedule
        if discover_percent_complete is not UNSET:
            field_dict["discoverPercentComplete"] = discover_percent_complete
        if monitor_percent_complete is not UNSET:
            field_dict["monitorPercentComplete"] = monitor_percent_complete
        if discover_status is not UNSET:
            field_dict["discoverStatus"] = discover_status
        if monitor_status is not UNSET:
            field_dict["monitorStatus"] = monitor_status
        if discover_last_scanned is not UNSET:
            field_dict["discoverLastScanned"] = discover_last_scanned
        if monitor_last_scanned is not UNSET:
            field_dict["monitorLastScanned"] = monitor_last_scanned
        if ssl_alert_recipients is not UNSET:
            field_dict["sslAlertRecipients"] = ssl_alert_recipients
        if get_robots is not UNSET:
            field_dict["getRobots"] = get_robots
        if discover_timeout_ms is not UNSET:
            field_dict["discoverTimeoutMs"] = discover_timeout_ms
        if monitor_timeout_ms is not UNSET:
            field_dict["monitorTimeoutMs"] = monitor_timeout_ms
        if expiration_alert_days is not UNSET:
            field_dict["expirationAlertDays"] = expiration_alert_days
        if discover_job_parts is not UNSET:
            field_dict["discoverJobParts"] = discover_job_parts
        if monitor_job_parts is not UNSET:
            field_dict["monitorJobParts"] = monitor_job_parts
        if quiet_hours is not UNSET:
            field_dict["quietHours"] = quiet_hours
        if blackout_start is not UNSET:
            field_dict["blackoutStart"] = blackout_start
        if blackout_end is not UNSET:
            field_dict["blackoutEnd"] = blackout_end
        if auto_monitor is not UNSET:
            field_dict["autoMonitor"] = auto_monitor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
        from ..models.keyfactor_common_scheduling_models_weekly_model import KeyfactorCommonSchedulingModelsWeeklyModel
        from ..models.keyfactor_web_keyfactor_api_models_ssl_quiet_hour_response import (
            KeyfactorWebKeyfactorApiModelsSslQuietHourResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        network_id = d.pop("networkId", UNSET)

        name = d.pop("name", UNSET)

        agent_pool_name = d.pop("agentPoolName", UNSET)

        agent_pool_id = d.pop("agentPoolId", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        _discover_schedule = d.pop("discoverSchedule", UNSET)
        discover_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_discover_schedule, Unset):
            discover_schedule = UNSET
        else:
            discover_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_discover_schedule)

        _monitor_schedule = d.pop("monitorSchedule", UNSET)
        monitor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_monitor_schedule, Unset):
            monitor_schedule = UNSET
        else:
            monitor_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_monitor_schedule)

        discover_percent_complete = d.pop("discoverPercentComplete", UNSET)

        monitor_percent_complete = d.pop("monitorPercentComplete", UNSET)

        _discover_status = d.pop("discoverStatus", UNSET)
        discover_status: Union[Unset, CSSCMSCoreEnumsSslNetworkJobStatus]
        if isinstance(_discover_status, Unset):
            discover_status = UNSET
        else:
            discover_status = CSSCMSCoreEnumsSslNetworkJobStatus(_discover_status)

        _monitor_status = d.pop("monitorStatus", UNSET)
        monitor_status: Union[Unset, CSSCMSCoreEnumsSslNetworkJobStatus]
        if isinstance(_monitor_status, Unset):
            monitor_status = UNSET
        else:
            monitor_status = CSSCMSCoreEnumsSslNetworkJobStatus(_monitor_status)

        _discover_last_scanned = d.pop("discoverLastScanned", UNSET)
        discover_last_scanned: Union[Unset, None, datetime.datetime]
        if _discover_last_scanned is None:
            discover_last_scanned = None
        elif isinstance(_discover_last_scanned, Unset):
            discover_last_scanned = UNSET
        else:
            discover_last_scanned = isoparse(_discover_last_scanned)

        _monitor_last_scanned = d.pop("monitorLastScanned", UNSET)
        monitor_last_scanned: Union[Unset, None, datetime.datetime]
        if _monitor_last_scanned is None:
            monitor_last_scanned = None
        elif isinstance(_monitor_last_scanned, Unset):
            monitor_last_scanned = UNSET
        else:
            monitor_last_scanned = isoparse(_monitor_last_scanned)

        ssl_alert_recipients = cast(List[str], d.pop("sslAlertRecipients", UNSET))

        get_robots = d.pop("getRobots", UNSET)

        discover_timeout_ms = d.pop("discoverTimeoutMs", UNSET)

        monitor_timeout_ms = d.pop("monitorTimeoutMs", UNSET)

        expiration_alert_days = d.pop("expirationAlertDays", UNSET)

        discover_job_parts = d.pop("discoverJobParts", UNSET)

        monitor_job_parts = d.pop("monitorJobParts", UNSET)

        quiet_hours = []
        _quiet_hours = d.pop("quietHours", UNSET)
        for quiet_hours_item_data in _quiet_hours or []:
            quiet_hours_item = KeyfactorWebKeyfactorApiModelsSslQuietHourResponse.from_dict(quiet_hours_item_data)

            quiet_hours.append(quiet_hours_item)

        _blackout_start = d.pop("blackoutStart", UNSET)
        blackout_start: Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]
        if isinstance(_blackout_start, Unset):
            blackout_start = UNSET
        else:
            blackout_start = KeyfactorCommonSchedulingModelsWeeklyModel.from_dict(_blackout_start)

        _blackout_end = d.pop("blackoutEnd", UNSET)
        blackout_end: Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]
        if isinstance(_blackout_end, Unset):
            blackout_end = UNSET
        else:
            blackout_end = KeyfactorCommonSchedulingModelsWeeklyModel.from_dict(_blackout_end)

        auto_monitor = d.pop("autoMonitor", UNSET)

        keyfactor_web_keyfactor_api_models_ssl_network_response = cls(
            network_id=network_id,
            name=name,
            agent_pool_name=agent_pool_name,
            agent_pool_id=agent_pool_id,
            description=description,
            enabled=enabled,
            discover_schedule=discover_schedule,
            monitor_schedule=monitor_schedule,
            discover_percent_complete=discover_percent_complete,
            monitor_percent_complete=monitor_percent_complete,
            discover_status=discover_status,
            monitor_status=monitor_status,
            discover_last_scanned=discover_last_scanned,
            monitor_last_scanned=monitor_last_scanned,
            ssl_alert_recipients=ssl_alert_recipients,
            get_robots=get_robots,
            discover_timeout_ms=discover_timeout_ms,
            monitor_timeout_ms=monitor_timeout_ms,
            expiration_alert_days=expiration_alert_days,
            discover_job_parts=discover_job_parts,
            monitor_job_parts=monitor_job_parts,
            quiet_hours=quiet_hours,
            blackout_start=blackout_start,
            blackout_end=blackout_end,
            auto_monitor=auto_monitor,
        )

        return keyfactor_web_keyfactor_api_models_ssl_network_response
