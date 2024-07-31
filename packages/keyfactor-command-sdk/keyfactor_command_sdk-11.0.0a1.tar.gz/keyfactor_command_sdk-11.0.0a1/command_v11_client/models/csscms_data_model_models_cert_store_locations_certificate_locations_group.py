from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_cert_store_locations_certificate_store_locations_detail import (
        CSSCMSDataModelModelsCertStoreLocationsCertificateStoreLocationsDetail,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsCertStoreLocationsCertificateLocationsGroup")


@_attrs_define
class CSSCMSDataModelModelsCertStoreLocationsCertificateLocationsGroup:
    """
    Attributes:
        store_type (Union[Unset, None, str]):
        store_type_id (Union[Unset, int]):
        store_count (Union[Unset, int]):
        locations (Union[Unset, None, List['CSSCMSDataModelModelsCertStoreLocationsCertificateStoreLocationsDetail']]):
    """

    store_type: Union[Unset, None, str] = UNSET
    store_type_id: Union[Unset, int] = UNSET
    store_count: Union[Unset, int] = UNSET
    locations: Union[
        Unset, None, List["CSSCMSDataModelModelsCertStoreLocationsCertificateStoreLocationsDetail"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_type = self.store_type
        store_type_id = self.store_type_id
        store_count = self.store_count
        locations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            if self.locations is None:
                locations = None
            else:
                locations = []
                for locations_item_data in self.locations:
                    locations_item = locations_item_data.to_dict()

                    locations.append(locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if store_type_id is not UNSET:
            field_dict["storeTypeId"] = store_type_id
        if store_count is not UNSET:
            field_dict["storeCount"] = store_count
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_cert_store_locations_certificate_store_locations_detail import (
            CSSCMSDataModelModelsCertStoreLocationsCertificateStoreLocationsDetail,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        store_type = d.pop("storeType", UNSET)

        store_type_id = d.pop("storeTypeId", UNSET)

        store_count = d.pop("storeCount", UNSET)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = CSSCMSDataModelModelsCertStoreLocationsCertificateStoreLocationsDetail.from_dict(
                locations_item_data
            )

            locations.append(locations_item)

        csscms_data_model_models_cert_store_locations_certificate_locations_group = cls(
            store_type=store_type,
            store_type_id=store_type_id,
            store_count=store_count,
            locations=locations,
        )

        return csscms_data_model_models_cert_store_locations_certificate_locations_group
