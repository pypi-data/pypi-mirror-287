import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_import_request_model_metadata import (
        CSSCMSDataModelModelsCertificateImportRequestModelMetadata,
    )
    from ..models.csscms_data_model_models_enrollment_management_store_type import (
        CSSCMSDataModelModelsEnrollmentManagementStoreType,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateImportRequestModel")


@_attrs_define
class CSSCMSDataModelModelsCertificateImportRequestModel:
    """
    Attributes:
        certificate (str):
        password (Union[Unset, None, str]):
        metadata (Union[Unset, None, CSSCMSDataModelModelsCertificateImportRequestModelMetadata]):
        store_ids (Union[Unset, None, List[str]]):
        store_types (Union[Unset, None, List['CSSCMSDataModelModelsEnrollmentManagementStoreType']]):
        schedule (Union[Unset, None, datetime.datetime]):
    """

    certificate: str
    password: Union[Unset, None, str] = UNSET
    metadata: Union[Unset, None, "CSSCMSDataModelModelsCertificateImportRequestModelMetadata"] = UNSET
    store_ids: Union[Unset, None, List[str]] = UNSET
    store_types: Union[Unset, None, List["CSSCMSDataModelModelsEnrollmentManagementStoreType"]] = UNSET
    schedule: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate = self.certificate
        password = self.password
        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

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

        schedule: Union[Unset, None, str] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.isoformat()[:-6]+'Z' if self.schedule else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "certificate": certificate,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if store_ids is not UNSET:
            field_dict["storeIds"] = store_ids
        if store_types is not UNSET:
            field_dict["storeTypes"] = store_types
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_import_request_model_metadata import (
            CSSCMSDataModelModelsCertificateImportRequestModelMetadata,
        )
        from ..models.csscms_data_model_models_enrollment_management_store_type import (
            CSSCMSDataModelModelsEnrollmentManagementStoreType,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        certificate = d.pop("certificate")

        password = d.pop("password", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CSSCMSDataModelModelsCertificateImportRequestModelMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CSSCMSDataModelModelsCertificateImportRequestModelMetadata.from_dict(_metadata)

        store_ids = cast(List[str], d.pop("storeIds", UNSET))

        store_types = []
        _store_types = d.pop("storeTypes", UNSET)
        for store_types_item_data in _store_types or []:
            store_types_item = CSSCMSDataModelModelsEnrollmentManagementStoreType.from_dict(store_types_item_data)

            store_types.append(store_types_item)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, None, datetime.datetime]
        if _schedule is None:
            schedule = None
        elif isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = isoparse(_schedule)

        csscms_data_model_models_certificate_import_request_model = cls(
            certificate=certificate,
            password=password,
            metadata=metadata,
            store_ids=store_ids,
            store_types=store_types,
            schedule=schedule,
        )

        return csscms_data_model_models_certificate_import_request_model
