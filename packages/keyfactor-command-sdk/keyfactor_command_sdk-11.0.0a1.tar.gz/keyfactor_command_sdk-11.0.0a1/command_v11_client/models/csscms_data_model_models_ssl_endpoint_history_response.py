import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_orchestrators_common_enums_ssl_endpoint_status import (
    KeyfactorOrchestratorsCommonEnumsSslEndpointStatus,
)
from ..models.keyfactor_orchestrators_common_enums_ssl_job_type import KeyfactorOrchestratorsCommonEnumsSslJobType
from ..models.keyfactor_orchestrators_common_enums_ssl_probe_type import KeyfactorOrchestratorsCommonEnumsSslProbeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssl_endpoint_history_response_certificate_model import (
        CSSCMSDataModelModelsSSLEndpointHistoryResponseCertificateModel,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSSLEndpointHistoryResponse")


@_attrs_define
class CSSCMSDataModelModelsSSLEndpointHistoryResponse:
    """
    Attributes:
        history_id (Union[Unset, str]):
        endpoint_id (Union[Unset, str]):
        audit_id (Union[Unset, int]):
        timestamp (Union[Unset, datetime.datetime]):
        status (Union[Unset, KeyfactorOrchestratorsCommonEnumsSslEndpointStatus]):
        job_type (Union[Unset, KeyfactorOrchestratorsCommonEnumsSslJobType]):
        probe_type (Union[Unset, KeyfactorOrchestratorsCommonEnumsSslProbeType]):
        reverse_dns (Union[Unset, None, str]):
        history_certificates (Union[Unset, None,
            List['CSSCMSDataModelModelsSSLEndpointHistoryResponseCertificateModel']]):
    """

    history_id: Union[Unset, str] = UNSET
    endpoint_id: Union[Unset, str] = UNSET
    audit_id: Union[Unset, int] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, KeyfactorOrchestratorsCommonEnumsSslEndpointStatus] = UNSET
    job_type: Union[Unset, KeyfactorOrchestratorsCommonEnumsSslJobType] = UNSET
    probe_type: Union[Unset, KeyfactorOrchestratorsCommonEnumsSslProbeType] = UNSET
    reverse_dns: Union[Unset, None, str] = UNSET
    history_certificates: Union[
        Unset, None, List["CSSCMSDataModelModelsSSLEndpointHistoryResponseCertificateModel"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        history_id = self.history_id
        endpoint_id = self.endpoint_id
        audit_id = self.audit_id
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()[:-6]+'Z'

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        job_type: Union[Unset, int] = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        probe_type: Union[Unset, int] = UNSET
        if not isinstance(self.probe_type, Unset):
            probe_type = self.probe_type.value

        reverse_dns = self.reverse_dns
        history_certificates: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history_certificates, Unset):
            if self.history_certificates is None:
                history_certificates = None
            else:
                history_certificates = []
                for history_certificates_item_data in self.history_certificates:
                    history_certificates_item = history_certificates_item_data.to_dict()

                    history_certificates.append(history_certificates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if history_id is not UNSET:
            field_dict["historyId"] = history_id
        if endpoint_id is not UNSET:
            field_dict["endpointId"] = endpoint_id
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if status is not UNSET:
            field_dict["status"] = status
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if probe_type is not UNSET:
            field_dict["probeType"] = probe_type
        if reverse_dns is not UNSET:
            field_dict["reverseDNS"] = reverse_dns
        if history_certificates is not UNSET:
            field_dict["historyCertificates"] = history_certificates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssl_endpoint_history_response_certificate_model import (
            CSSCMSDataModelModelsSSLEndpointHistoryResponseCertificateModel,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        history_id = d.pop("historyId", UNSET)

        endpoint_id = d.pop("endpointId", UNSET)

        audit_id = d.pop("auditId", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _status = d.pop("status", UNSET)
        status: Union[Unset, KeyfactorOrchestratorsCommonEnumsSslEndpointStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = KeyfactorOrchestratorsCommonEnumsSslEndpointStatus(_status)

        _job_type = d.pop("jobType", UNSET)
        job_type: Union[Unset, KeyfactorOrchestratorsCommonEnumsSslJobType]
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = KeyfactorOrchestratorsCommonEnumsSslJobType(_job_type)

        _probe_type = d.pop("probeType", UNSET)
        probe_type: Union[Unset, KeyfactorOrchestratorsCommonEnumsSslProbeType]
        if isinstance(_probe_type, Unset):
            probe_type = UNSET
        else:
            probe_type = KeyfactorOrchestratorsCommonEnumsSslProbeType(_probe_type)

        reverse_dns = d.pop("reverseDNS", UNSET)

        history_certificates = []
        _history_certificates = d.pop("historyCertificates", UNSET)
        for history_certificates_item_data in _history_certificates or []:
            history_certificates_item = CSSCMSDataModelModelsSSLEndpointHistoryResponseCertificateModel.from_dict(
                history_certificates_item_data
            )

            history_certificates.append(history_certificates_item)

        csscms_data_model_models_ssl_endpoint_history_response = cls(
            history_id=history_id,
            endpoint_id=endpoint_id,
            audit_id=audit_id,
            timestamp=timestamp,
            status=status,
            job_type=job_type,
            probe_type=probe_type,
            reverse_dns=reverse_dns,
            history_certificates=history_certificates,
        )

        return csscms_data_model_models_ssl_endpoint_history_response
