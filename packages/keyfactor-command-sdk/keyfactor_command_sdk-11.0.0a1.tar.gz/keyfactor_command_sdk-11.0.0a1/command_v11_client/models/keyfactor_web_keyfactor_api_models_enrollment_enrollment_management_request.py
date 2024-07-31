import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_enrollment_management_store_request import (
        KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequest,
    )
    from ..models.keyfactor_web_keyfactor_api_models_enrollment_management_store_type_request import (
        KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreTypeRequest,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsEnrollmentEnrollmentManagementRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsEnrollmentEnrollmentManagementRequest:
    """
    Attributes:
        password (str):
        stores (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequest']]): The stores
            to add the certificate to. Values in this collection will take precedence over values in
            CSS.CMS.Data.Model.Models.Enrollment.SpecificEnrollmentManagementRequest.StoreTypes.
        store_ids (Union[Unset, None, List[str]]):
        store_types (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreTypeRequest']]):
        certificate_id (Union[Unset, int]):
        request_id (Union[Unset, int]):
        job_time (Union[Unset, datetime.datetime]):
    """

    password: str
    stores: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequest"]] = UNSET
    store_ids: Union[Unset, None, List[str]] = UNSET
    store_types: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreTypeRequest"]] = UNSET
    certificate_id: Union[Unset, int] = UNSET
    request_id: Union[Unset, int] = UNSET
    job_time: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        stores: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stores, Unset):
            if self.stores is None:
                stores = None
            else:
                stores = []
                for stores_item_data in self.stores:
                    stores_item = stores_item_data.to_dict()

                    stores.append(stores_item)

        store_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.store_ids, Unset):
            if self.store_ids is None:
                store_ids = None
            else:
                store_ids = self.store_ids

        store_types: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.store_types, Unset):
            if self.store_types is None:
                store_types = None
            else:
                store_types = []
                for store_types_item_data in self.store_types:
                    store_types_item = store_types_item_data.to_dict()

                    store_types.append(store_types_item)

        certificate_id = self.certificate_id
        request_id = self.request_id
        job_time: Union[Unset, str] = UNSET
        if not isinstance(self.job_time, Unset):
            job_time = self.job_time.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "password": password,
            }
        )
        if stores is not UNSET:
            field_dict["stores"] = stores
        if store_ids is not UNSET:
            field_dict["storeIds"] = store_ids
        if store_types is not UNSET:
            field_dict["storeTypes"] = store_types
        if certificate_id is not UNSET:
            field_dict["certificateId"] = certificate_id
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if job_time is not UNSET:
            field_dict["jobTime"] = job_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_enrollment_management_store_request import (
            KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequest,
        )
        from ..models.keyfactor_web_keyfactor_api_models_enrollment_management_store_type_request import (
            KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreTypeRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        password = d.pop("password")

        stores = []
        _stores = d.pop("stores", UNSET)
        for stores_item_data in _stores or []:
            stores_item = KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequest.from_dict(stores_item_data)

            stores.append(stores_item)

        store_ids = cast(List[str], d.pop("storeIds", UNSET))

        store_types = []
        _store_types = d.pop("storeTypes", UNSET)
        for store_types_item_data in _store_types or []:
            store_types_item = KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreTypeRequest.from_dict(
                store_types_item_data
            )

            store_types.append(store_types_item)

        certificate_id = d.pop("certificateId", UNSET)

        request_id = d.pop("requestId", UNSET)

        _job_time = d.pop("jobTime", UNSET)
        job_time: Union[Unset, datetime.datetime]
        if isinstance(_job_time, Unset):
            job_time = UNSET
        else:
            job_time = isoparse(_job_time)

        keyfactor_web_keyfactor_api_models_enrollment_enrollment_management_request = cls(
            password=password,
            stores=stores,
            store_ids=store_ids,
            store_types=store_types,
            certificate_id=certificate_id,
            request_id=request_id,
            job_time=job_time,
        )

        return keyfactor_web_keyfactor_api_models_enrollment_enrollment_management_request
