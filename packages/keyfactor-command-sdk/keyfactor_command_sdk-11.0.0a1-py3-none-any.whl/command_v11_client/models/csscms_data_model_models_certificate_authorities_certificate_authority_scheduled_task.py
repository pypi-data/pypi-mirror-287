import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_platform_extensions_ca_sync_type import KeyfactorPlatformExtensionsCASyncType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateAuthoritiesCertificateAuthorityScheduledTask")


@_attrs_define
class CSSCMSDataModelModelsCertificateAuthoritiesCertificateAuthorityScheduledTask:
    """
    Attributes:
        id (Union[Unset, int]):
        certificate_authority_id (Union[Unset, int]):
        schedule (Union[Unset, None, str]):
        scan_type (Union[Unset, KeyfactorPlatformExtensionsCASyncType]):
        sync_enabled (Union[Unset, bool]):
        last_scan_time (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    certificate_authority_id: Union[Unset, int] = UNSET
    schedule: Union[Unset, None, str] = UNSET
    scan_type: Union[Unset, KeyfactorPlatformExtensionsCASyncType] = UNSET
    sync_enabled: Union[Unset, bool] = UNSET
    last_scan_time: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        certificate_authority_id = self.certificate_authority_id
        schedule = self.schedule
        scan_type: Union[Unset, int] = UNSET
        if not isinstance(self.scan_type, Unset):
            scan_type = self.scan_type.value

        sync_enabled = self.sync_enabled
        last_scan_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_scan_time, Unset):
            last_scan_time = self.last_scan_time.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if certificate_authority_id is not UNSET:
            field_dict["certificateAuthorityId"] = certificate_authority_id
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if scan_type is not UNSET:
            field_dict["scanType"] = scan_type
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if last_scan_time is not UNSET:
            field_dict["lastScanTime"] = last_scan_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        certificate_authority_id = d.pop("certificateAuthorityId", UNSET)

        schedule = d.pop("schedule", UNSET)

        _scan_type = d.pop("scanType", UNSET)
        scan_type: Union[Unset, KeyfactorPlatformExtensionsCASyncType]
        if isinstance(_scan_type, Unset):
            scan_type = UNSET
        else:
            scan_type = KeyfactorPlatformExtensionsCASyncType(_scan_type)

        sync_enabled = d.pop("syncEnabled", UNSET)

        _last_scan_time = d.pop("lastScanTime", UNSET)
        last_scan_time: Union[Unset, datetime.datetime]
        if isinstance(_last_scan_time, Unset):
            last_scan_time = UNSET
        else:
            last_scan_time = isoparse(_last_scan_time)

        csscms_data_model_models_certificate_authorities_certificate_authority_scheduled_task = cls(
            id=id,
            certificate_authority_id=certificate_authority_id,
            schedule=schedule,
            scan_type=scan_type,
            sync_enabled=sync_enabled,
            last_scan_time=last_scan_time,
        )

        return csscms_data_model_models_certificate_authorities_certificate_authority_scheduled_task
