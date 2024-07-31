import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_pki_enums_revoke_code import KeyfactorPKIEnumsRevokeCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsRevokeCertificateRequest")


@_attrs_define
class CSSCMSDataModelModelsRevokeCertificateRequest:
    """
    Attributes:
        certificate_ids (Union[Unset, None, List[int]]):
        reason (Union[Unset, KeyfactorPKIEnumsRevokeCode]):
        comment (Union[Unset, None, str]):
        effective_date (Union[Unset, datetime.datetime]):
        collection_id (Union[Unset, None, int]):
    """

    certificate_ids: Union[Unset, None, List[int]] = UNSET
    reason: Union[Unset, KeyfactorPKIEnumsRevokeCode] = UNSET
    comment: Union[Unset, None, str] = UNSET
    effective_date: Union[Unset, datetime.datetime] = UNSET
    collection_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.certificate_ids, Unset):
            if self.certificate_ids is None:
                certificate_ids = None
            else:
                certificate_ids = self.certificate_ids

        reason: Union[Unset, int] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        comment = self.comment
        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()[:-6]+'Z'

        collection_id = self.collection_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if certificate_ids is not UNSET:
            field_dict["certificateIds"] = certificate_ids
        if reason is not UNSET:
            field_dict["reason"] = reason
        if comment is not UNSET:
            field_dict["comment"] = comment
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        certificate_ids = cast(List[int], d.pop("certificateIds", UNSET))

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, KeyfactorPKIEnumsRevokeCode]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = KeyfactorPKIEnumsRevokeCode(_reason)

        comment = d.pop("comment", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.datetime]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date)

        collection_id = d.pop("collectionId", UNSET)

        csscms_data_model_models_revoke_certificate_request = cls(
            certificate_ids=certificate_ids,
            reason=reason,
            comment=comment,
            effective_date=effective_date,
            collection_id=collection_id,
        )

        return csscms_data_model_models_revoke_certificate_request
