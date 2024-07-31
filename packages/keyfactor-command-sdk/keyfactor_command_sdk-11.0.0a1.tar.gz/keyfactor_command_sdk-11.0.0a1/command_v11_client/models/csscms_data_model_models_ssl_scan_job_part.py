import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.csscms_core_enums_ssl_scan_job_status import CSSCMSCoreEnumsSslScanJobStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssl_scan_job_part_definition import (
        CSSCMSDataModelModelsSSLScanJobPartDefinition,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSSLScanJobPart")


@_attrs_define
class CSSCMSDataModelModelsSSLScanJobPart:
    """
    Attributes:
        scan_job_part_id (Union[Unset, str]):
        logical_scan_job_id (Union[Unset, str]):
        agent_job_id (Union[Unset, str]):
        estimated_endpoint_count (Union[Unset, None, int]):
        status (Union[Unset, CSSCMSCoreEnumsSslScanJobStatus]):
        stat_total_endpoint_count (Union[Unset, None, int]):
        stat_timed_out_connecting_count (Union[Unset, None, int]):
        stat_connection_refused_count (Union[Unset, None, int]):
        stat_timed_out_downloading_count (Union[Unset, None, int]):
        stat_exception_downloading_count (Union[Unset, None, int]):
        stat_not_ssl_count (Union[Unset, None, int]):
        stat_bad_ssl_handshake_count (Union[Unset, None, int]):
        stat_certificate_found_count (Union[Unset, None, int]):
        stat_no_certificate_count (Union[Unset, None, int]):
        scan_job_part_definitions (Union[Unset, None, List['CSSCMSDataModelModelsSSLScanJobPartDefinition']]):
        start_time (Union[Unset, None, datetime.datetime]):
        end_time (Union[Unset, None, datetime.datetime]):
    """

    scan_job_part_id: Union[Unset, str] = UNSET
    logical_scan_job_id: Union[Unset, str] = UNSET
    agent_job_id: Union[Unset, str] = UNSET
    estimated_endpoint_count: Union[Unset, None, int] = UNSET
    status: Union[Unset, CSSCMSCoreEnumsSslScanJobStatus] = UNSET
    stat_total_endpoint_count: Union[Unset, None, int] = UNSET
    stat_timed_out_connecting_count: Union[Unset, None, int] = UNSET
    stat_connection_refused_count: Union[Unset, None, int] = UNSET
    stat_timed_out_downloading_count: Union[Unset, None, int] = UNSET
    stat_exception_downloading_count: Union[Unset, None, int] = UNSET
    stat_not_ssl_count: Union[Unset, None, int] = UNSET
    stat_bad_ssl_handshake_count: Union[Unset, None, int] = UNSET
    stat_certificate_found_count: Union[Unset, None, int] = UNSET
    stat_no_certificate_count: Union[Unset, None, int] = UNSET
    scan_job_part_definitions: Union[Unset, None, List["CSSCMSDataModelModelsSSLScanJobPartDefinition"]] = UNSET
    start_time: Union[Unset, None, datetime.datetime] = UNSET
    end_time: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        scan_job_part_id = self.scan_job_part_id
        logical_scan_job_id = self.logical_scan_job_id
        agent_job_id = self.agent_job_id
        estimated_endpoint_count = self.estimated_endpoint_count
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        stat_total_endpoint_count = self.stat_total_endpoint_count
        stat_timed_out_connecting_count = self.stat_timed_out_connecting_count
        stat_connection_refused_count = self.stat_connection_refused_count
        stat_timed_out_downloading_count = self.stat_timed_out_downloading_count
        stat_exception_downloading_count = self.stat_exception_downloading_count
        stat_not_ssl_count = self.stat_not_ssl_count
        stat_bad_ssl_handshake_count = self.stat_bad_ssl_handshake_count
        stat_certificate_found_count = self.stat_certificate_found_count
        stat_no_certificate_count = self.stat_no_certificate_count
        scan_job_part_definitions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scan_job_part_definitions, Unset):
            if self.scan_job_part_definitions is None:
                scan_job_part_definitions = None
            else:
                scan_job_part_definitions = []
                for scan_job_part_definitions_item_data in self.scan_job_part_definitions:
                    scan_job_part_definitions_item = scan_job_part_definitions_item_data.to_dict()

                    scan_job_part_definitions.append(scan_job_part_definitions_item)

        start_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()[:-6]+'Z' if self.start_time else None

        end_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()[:-6]+'Z' if self.end_time else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if scan_job_part_id is not UNSET:
            field_dict["scanJobPartId"] = scan_job_part_id
        if logical_scan_job_id is not UNSET:
            field_dict["logicalScanJobId"] = logical_scan_job_id
        if agent_job_id is not UNSET:
            field_dict["agentJobId"] = agent_job_id
        if estimated_endpoint_count is not UNSET:
            field_dict["estimatedEndpointCount"] = estimated_endpoint_count
        if status is not UNSET:
            field_dict["status"] = status
        if stat_total_endpoint_count is not UNSET:
            field_dict["statTotalEndpointCount"] = stat_total_endpoint_count
        if stat_timed_out_connecting_count is not UNSET:
            field_dict["statTimedOutConnectingCount"] = stat_timed_out_connecting_count
        if stat_connection_refused_count is not UNSET:
            field_dict["statConnectionRefusedCount"] = stat_connection_refused_count
        if stat_timed_out_downloading_count is not UNSET:
            field_dict["statTimedOutDownloadingCount"] = stat_timed_out_downloading_count
        if stat_exception_downloading_count is not UNSET:
            field_dict["statExceptionDownloadingCount"] = stat_exception_downloading_count
        if stat_not_ssl_count is not UNSET:
            field_dict["statNotSslCount"] = stat_not_ssl_count
        if stat_bad_ssl_handshake_count is not UNSET:
            field_dict["statBadSslHandshakeCount"] = stat_bad_ssl_handshake_count
        if stat_certificate_found_count is not UNSET:
            field_dict["statCertificateFoundCount"] = stat_certificate_found_count
        if stat_no_certificate_count is not UNSET:
            field_dict["statNoCertificateCount"] = stat_no_certificate_count
        if scan_job_part_definitions is not UNSET:
            field_dict["scanJobPartDefinitions"] = scan_job_part_definitions
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssl_scan_job_part_definition import (
            CSSCMSDataModelModelsSSLScanJobPartDefinition,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        scan_job_part_id = d.pop("scanJobPartId", UNSET)

        logical_scan_job_id = d.pop("logicalScanJobId", UNSET)

        agent_job_id = d.pop("agentJobId", UNSET)

        estimated_endpoint_count = d.pop("estimatedEndpointCount", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CSSCMSCoreEnumsSslScanJobStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CSSCMSCoreEnumsSslScanJobStatus(_status)

        stat_total_endpoint_count = d.pop("statTotalEndpointCount", UNSET)

        stat_timed_out_connecting_count = d.pop("statTimedOutConnectingCount", UNSET)

        stat_connection_refused_count = d.pop("statConnectionRefusedCount", UNSET)

        stat_timed_out_downloading_count = d.pop("statTimedOutDownloadingCount", UNSET)

        stat_exception_downloading_count = d.pop("statExceptionDownloadingCount", UNSET)

        stat_not_ssl_count = d.pop("statNotSslCount", UNSET)

        stat_bad_ssl_handshake_count = d.pop("statBadSslHandshakeCount", UNSET)

        stat_certificate_found_count = d.pop("statCertificateFoundCount", UNSET)

        stat_no_certificate_count = d.pop("statNoCertificateCount", UNSET)

        scan_job_part_definitions = []
        _scan_job_part_definitions = d.pop("scanJobPartDefinitions", UNSET)
        for scan_job_part_definitions_item_data in _scan_job_part_definitions or []:
            scan_job_part_definitions_item = CSSCMSDataModelModelsSSLScanJobPartDefinition.from_dict(
                scan_job_part_definitions_item_data
            )

            scan_job_part_definitions.append(scan_job_part_definitions_item)

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

        csscms_data_model_models_ssl_scan_job_part = cls(
            scan_job_part_id=scan_job_part_id,
            logical_scan_job_id=logical_scan_job_id,
            agent_job_id=agent_job_id,
            estimated_endpoint_count=estimated_endpoint_count,
            status=status,
            stat_total_endpoint_count=stat_total_endpoint_count,
            stat_timed_out_connecting_count=stat_timed_out_connecting_count,
            stat_connection_refused_count=stat_connection_refused_count,
            stat_timed_out_downloading_count=stat_timed_out_downloading_count,
            stat_exception_downloading_count=stat_exception_downloading_count,
            stat_not_ssl_count=stat_not_ssl_count,
            stat_bad_ssl_handshake_count=stat_bad_ssl_handshake_count,
            stat_certificate_found_count=stat_certificate_found_count,
            stat_no_certificate_count=stat_no_certificate_count,
            scan_job_part_definitions=scan_job_part_definitions,
            start_time=start_time,
            end_time=end_time,
        )

        return csscms_data_model_models_ssl_scan_job_part
