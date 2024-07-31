from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreContainerListResponse")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreContainerListResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        overwrite_schedules (Union[Unset, bool]):
        schedule (Union[Unset, None, str]):
        cert_store_type (Union[Unset, int]):
        store_count (Union[Unset, None, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    overwrite_schedules: Union[Unset, bool] = UNSET
    schedule: Union[Unset, None, str] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    store_count: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        overwrite_schedules = self.overwrite_schedules
        schedule = self.schedule
        cert_store_type = self.cert_store_type
        store_count = self.store_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if overwrite_schedules is not UNSET:
            field_dict["overwriteSchedules"] = overwrite_schedules
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if cert_store_type is not UNSET:
            field_dict["certStoreType"] = cert_store_type
        if store_count is not UNSET:
            field_dict["storeCount"] = store_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        overwrite_schedules = d.pop("overwriteSchedules", UNSET)

        schedule = d.pop("schedule", UNSET)

        cert_store_type = d.pop("certStoreType", UNSET)

        store_count = d.pop("storeCount", UNSET)

        csscms_data_model_models_certificate_store_container_list_response = cls(
            id=id,
            name=name,
            overwrite_schedules=overwrite_schedules,
            schedule=schedule,
            cert_store_type=cert_store_type,
            store_count=store_count,
        )

        return csscms_data_model_models_certificate_store_container_list_response
