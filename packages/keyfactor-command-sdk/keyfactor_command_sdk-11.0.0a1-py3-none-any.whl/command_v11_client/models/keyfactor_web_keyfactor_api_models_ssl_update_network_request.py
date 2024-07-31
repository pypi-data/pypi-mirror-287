from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
    from ..models.keyfactor_common_scheduling_models_weekly_model import KeyfactorCommonSchedulingModelsWeeklyModel
    from ..models.keyfactor_web_keyfactor_api_models_ssl_quiet_hour_request import (
        KeyfactorWebKeyfactorApiModelsSslQuietHourRequest,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSslUpdateNetworkRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSslUpdateNetworkRequest:
    """
    Attributes:
        name (str):
        agent_pool_name (str):
        description (str):
        network_id (str):
        enabled (Union[Unset, bool]):
        discover_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        monitor_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        ssl_alert_recipients (Union[Unset, None, List[str]]):
        auto_monitor (Union[Unset, bool]):
        get_robots (Union[Unset, bool]):
        discover_timeout_ms (Union[Unset, float]):
        monitor_timeout_ms (Union[Unset, float]):
        expiration_alert_days (Union[Unset, float]):
        quiet_hours (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsSslQuietHourRequest']]):
        blackout_start (Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]):
        blackout_end (Union[Unset, KeyfactorCommonSchedulingModelsWeeklyModel]):
    """

    name: str
    agent_pool_name: str
    description: str
    network_id: str
    enabled: Union[Unset, bool] = UNSET
    discover_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    monitor_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    ssl_alert_recipients: Union[Unset, None, List[str]] = UNSET
    auto_monitor: Union[Unset, bool] = UNSET
    get_robots: Union[Unset, bool] = UNSET
    discover_timeout_ms: Union[Unset, float] = UNSET
    monitor_timeout_ms: Union[Unset, float] = UNSET
    expiration_alert_days: Union[Unset, float] = UNSET
    quiet_hours: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsSslQuietHourRequest"]] = UNSET
    blackout_start: Union[Unset, "KeyfactorCommonSchedulingModelsWeeklyModel"] = UNSET
    blackout_end: Union[Unset, "KeyfactorCommonSchedulingModelsWeeklyModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        agent_pool_name = self.agent_pool_name
        description = self.description
        network_id = self.network_id
        enabled = self.enabled
        discover_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discover_schedule, Unset):
            discover_schedule = self.discover_schedule.to_dict()

        monitor_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.monitor_schedule, Unset):
            monitor_schedule = self.monitor_schedule.to_dict()

        ssl_alert_recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.ssl_alert_recipients, Unset):
            if self.ssl_alert_recipients is None:
                ssl_alert_recipients = None
            else:
                ssl_alert_recipients = self.ssl_alert_recipients

        auto_monitor = self.auto_monitor
        get_robots = self.get_robots
        discover_timeout_ms = self.discover_timeout_ms
        monitor_timeout_ms = self.monitor_timeout_ms
        expiration_alert_days = self.expiration_alert_days
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "agentPoolName": agent_pool_name,
                "description": description,
                "networkId": network_id,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if discover_schedule is not UNSET:
            field_dict["discoverSchedule"] = discover_schedule
        if monitor_schedule is not UNSET:
            field_dict["monitorSchedule"] = monitor_schedule
        if ssl_alert_recipients is not UNSET:
            field_dict["sslAlertRecipients"] = ssl_alert_recipients
        if auto_monitor is not UNSET:
            field_dict["autoMonitor"] = auto_monitor
        if get_robots is not UNSET:
            field_dict["getRobots"] = get_robots
        if discover_timeout_ms is not UNSET:
            field_dict["discoverTimeoutMs"] = discover_timeout_ms
        if monitor_timeout_ms is not UNSET:
            field_dict["monitorTimeoutMs"] = monitor_timeout_ms
        if expiration_alert_days is not UNSET:
            field_dict["expirationAlertDays"] = expiration_alert_days
        if quiet_hours is not UNSET:
            field_dict["quietHours"] = quiet_hours
        if blackout_start is not UNSET:
            field_dict["blackoutStart"] = blackout_start
        if blackout_end is not UNSET:
            field_dict["blackoutEnd"] = blackout_end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
        from ..models.keyfactor_common_scheduling_models_weekly_model import KeyfactorCommonSchedulingModelsWeeklyModel
        from ..models.keyfactor_web_keyfactor_api_models_ssl_quiet_hour_request import (
            KeyfactorWebKeyfactorApiModelsSslQuietHourRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name")

        agent_pool_name = d.pop("agentPoolName")

        description = d.pop("description")

        network_id = d.pop("networkId")

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

        ssl_alert_recipients = cast(List[str], d.pop("sslAlertRecipients", UNSET))

        auto_monitor = d.pop("autoMonitor", UNSET)

        get_robots = d.pop("getRobots", UNSET)

        discover_timeout_ms = d.pop("discoverTimeoutMs", UNSET)

        monitor_timeout_ms = d.pop("monitorTimeoutMs", UNSET)

        expiration_alert_days = d.pop("expirationAlertDays", UNSET)

        quiet_hours = []
        _quiet_hours = d.pop("quietHours", UNSET)
        for quiet_hours_item_data in _quiet_hours or []:
            quiet_hours_item = KeyfactorWebKeyfactorApiModelsSslQuietHourRequest.from_dict(quiet_hours_item_data)

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

        keyfactor_web_keyfactor_api_models_ssl_update_network_request = cls(
            name=name,
            agent_pool_name=agent_pool_name,
            description=description,
            network_id=network_id,
            enabled=enabled,
            discover_schedule=discover_schedule,
            monitor_schedule=monitor_schedule,
            ssl_alert_recipients=ssl_alert_recipients,
            auto_monitor=auto_monitor,
            get_robots=get_robots,
            discover_timeout_ms=discover_timeout_ms,
            monitor_timeout_ms=monitor_timeout_ms,
            expiration_alert_days=expiration_alert_days,
            quiet_hours=quiet_hours,
            blackout_start=blackout_start,
            blackout_end=blackout_end,
        )

        return keyfactor_web_keyfactor_api_models_ssl_update_network_request
