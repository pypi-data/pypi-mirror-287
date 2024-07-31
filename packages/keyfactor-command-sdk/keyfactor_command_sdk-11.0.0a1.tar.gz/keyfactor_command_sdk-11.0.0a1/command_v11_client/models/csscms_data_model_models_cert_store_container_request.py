from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_store import CSSCMSDataModelModelsCertificateStore
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsCertStoreContainerRequest")


@_attrs_define
class CSSCMSDataModelModelsCertStoreContainerRequest:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        overwrite_schedules (Union[Unset, bool]):
        schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        cert_store_type (Union[Unset, int]):
        certificate_stores (Union[Unset, None, List['CSSCMSDataModelModelsCertificateStore']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    overwrite_schedules: Union[Unset, bool] = UNSET
    schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    certificate_stores: Union[Unset, None, List["CSSCMSDataModelModelsCertificateStore"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        overwrite_schedules = self.overwrite_schedules
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        cert_store_type = self.cert_store_type
        certificate_stores: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certificate_stores, Unset):
            if self.certificate_stores is None:
                certificate_stores = None
            else:
                certificate_stores = []
                for certificate_stores_item_data in self.certificate_stores:
                    certificate_stores_item = certificate_stores_item_data.to_dict()

                    certificate_stores.append(certificate_stores_item)

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
        if certificate_stores is not UNSET:
            field_dict["certificateStores"] = certificate_stores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_store import CSSCMSDataModelModelsCertificateStore
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        overwrite_schedules = d.pop("overwriteSchedules", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_schedule)

        cert_store_type = d.pop("certStoreType", UNSET)

        certificate_stores = []
        _certificate_stores = d.pop("certificateStores", UNSET)
        for certificate_stores_item_data in _certificate_stores or []:
            certificate_stores_item = CSSCMSDataModelModelsCertificateStore.from_dict(certificate_stores_item_data)

            certificate_stores.append(certificate_stores_item)

        csscms_data_model_models_cert_store_container_request = cls(
            id=id,
            name=name,
            overwrite_schedules=overwrite_schedules,
            schedule=schedule,
            cert_store_type=cert_store_type,
            certificate_stores=certificate_stores,
        )

        return csscms_data_model_models_cert_store_container_request
