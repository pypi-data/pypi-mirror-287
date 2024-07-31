from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_location_specifier import (
        CSSCMSDataModelModelsCertificateLocationSpecifier,
    )
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateStoresRemoveCertificateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateStoresRemoveCertificateRequest:
    """
    Attributes:
        certificate_stores (List['CSSCMSDataModelModelsCertificateLocationSpecifier']):
        schedule (KeyfactorCommonSchedulingKeyfactorSchedule):
        collection_id (Union[Unset, None, int]):
    """

    certificate_stores: List["CSSCMSDataModelModelsCertificateLocationSpecifier"]
    schedule: "KeyfactorCommonSchedulingKeyfactorSchedule"
    collection_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate_stores = []
        for certificate_stores_item_data in self.certificate_stores:
            certificate_stores_item = certificate_stores_item_data.to_dict()

            certificate_stores.append(certificate_stores_item)

        schedule = self.schedule.to_dict()

        collection_id = self.collection_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "certificateStores": certificate_stores,
                "schedule": schedule,
            }
        )
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_location_specifier import (
            CSSCMSDataModelModelsCertificateLocationSpecifier,
        )
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        certificate_stores = []
        _certificate_stores = d.pop("certificateStores")
        for certificate_stores_item_data in _certificate_stores:
            certificate_stores_item = CSSCMSDataModelModelsCertificateLocationSpecifier.from_dict(
                certificate_stores_item_data
            )

            certificate_stores.append(certificate_stores_item)

        schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(d.pop("schedule"))

        collection_id = d.pop("collectionId", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_stores_remove_certificate_request = cls(
            certificate_stores=certificate_stores,
            schedule=schedule,
            collection_id=collection_id,
        )

        return keyfactor_web_keyfactor_api_models_certificate_stores_remove_certificate_request
