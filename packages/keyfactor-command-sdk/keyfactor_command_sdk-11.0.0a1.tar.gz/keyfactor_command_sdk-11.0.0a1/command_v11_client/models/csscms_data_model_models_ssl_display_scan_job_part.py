import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.csscms_core_enums_ssl_scan_job_status import CSSCMSCoreEnumsSslScanJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSLDisplayScanJobPart")


@_attrs_define
class CSSCMSDataModelModelsSSLDisplayScanJobPart:
    """
    Attributes:
        scan_job_part_id (Union[Unset, str]):
        agent (Union[Unset, None, str]):
        status (Union[Unset, CSSCMSCoreEnumsSslScanJobStatus]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
        endpoint_count (Union[Unset, None, int]):
    """

    scan_job_part_id: Union[Unset, str] = UNSET
    agent: Union[Unset, None, str] = UNSET
    status: Union[Unset, CSSCMSCoreEnumsSslScanJobStatus] = UNSET
    start_time: Union[Unset, None, datetime.datetime] = UNSET
    end_time: Union[Unset, None, datetime.datetime] = UNSET
    endpoint_count: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        scan_job_part_id = self.scan_job_part_id
        agent = self.agent
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()[:-6]+'Z' if self.start_time else None

        end_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()[:-6]+'Z' if self.end_time else None

        endpoint_count = self.endpoint_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if scan_job_part_id is not UNSET:
            field_dict["scanJobPartId"] = scan_job_part_id
        if agent is not UNSET:
            field_dict["agent"] = agent
        if status is not UNSET:
            field_dict["status"] = status
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if endpoint_count is not UNSET:
            field_dict["endpointCount"] = endpoint_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        scan_job_part_id = d.pop("scanJobPartId", UNSET)

        agent = d.pop("agent", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CSSCMSCoreEnumsSslScanJobStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CSSCMSCoreEnumsSslScanJobStatus(_status)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, None, datetime.datetime]
        if _start_time is None:
            start_time = None
        elif isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, None, datetime.datetime]
        if _end_time is None:
            end_time = None
        elif isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        endpoint_count = d.pop("endpointCount", UNSET)

        csscms_data_model_models_ssl_display_scan_job_part = cls(
            scan_job_part_id=scan_job_part_id,
            agent=agent,
            status=status,
            start_time=start_time,
            end_time=end_time,
            endpoint_count=endpoint_count,
        )

        return csscms_data_model_models_ssl_display_scan_job_part
