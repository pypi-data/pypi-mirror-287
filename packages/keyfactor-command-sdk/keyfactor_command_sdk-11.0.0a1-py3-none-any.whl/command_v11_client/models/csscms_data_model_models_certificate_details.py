import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_details_metadata import (
        CSSCMSDataModelModelsCertificateDetailsMetadata,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateDetails")


@_attrs_define
class CSSCMSDataModelModelsCertificateDetails:
    """
    Attributes:
        issued_dn (Union[Unset, None, str]):
        issuer_dn (Union[Unset, None, str]):
        thumbprint (Union[Unset, None, str]):
        not_after (Union[Unset, datetime.datetime]):
        not_before (Union[Unset, datetime.datetime]):
        metadata (Union[Unset, None, CSSCMSDataModelModelsCertificateDetailsMetadata]):
        is_end_entity (Union[Unset, bool]):
    """

    issued_dn: Union[Unset, None, str] = UNSET
    issuer_dn: Union[Unset, None, str] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET
    not_after: Union[Unset, datetime.datetime] = UNSET
    not_before: Union[Unset, datetime.datetime] = UNSET
    metadata: Union[Unset, None, "CSSCMSDataModelModelsCertificateDetailsMetadata"] = UNSET
    is_end_entity: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        issued_dn = self.issued_dn
        issuer_dn = self.issuer_dn
        thumbprint = self.thumbprint
        not_after: Union[Unset, str] = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()[:-6]+'Z'

        not_before: Union[Unset, str] = UNSET
        if not isinstance(self.not_before, Unset):
            not_before = self.not_before.isoformat()[:-6]+'Z'

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        is_end_entity = self.is_end_entity

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if issued_dn is not UNSET:
            field_dict["issuedDN"] = issued_dn
        if issuer_dn is not UNSET:
            field_dict["issuerDN"] = issuer_dn
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if not_after is not UNSET:
            field_dict["notAfter"] = not_after
        if not_before is not UNSET:
            field_dict["notBefore"] = not_before
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if is_end_entity is not UNSET:
            field_dict["isEndEntity"] = is_end_entity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_details_metadata import (
            CSSCMSDataModelModelsCertificateDetailsMetadata,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        issued_dn = d.pop("issuedDN", UNSET)

        issuer_dn = d.pop("issuerDN", UNSET)

        thumbprint = d.pop("thumbprint", UNSET)

        _not_after = d.pop("notAfter", UNSET)
        not_after: Union[Unset, datetime.datetime]
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = isoparse(_not_after)

        _not_before = d.pop("notBefore", UNSET)
        not_before: Union[Unset, datetime.datetime]
        if isinstance(_not_before, Unset):
            not_before = UNSET
        else:
            not_before = isoparse(_not_before)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CSSCMSDataModelModelsCertificateDetailsMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CSSCMSDataModelModelsCertificateDetailsMetadata.from_dict(_metadata)

        is_end_entity = d.pop("isEndEntity", UNSET)

        csscms_data_model_models_certificate_details = cls(
            issued_dn=issued_dn,
            issuer_dn=issuer_dn,
            thumbprint=thumbprint,
            not_after=not_after,
            not_before=not_before,
            metadata=metadata,
            is_end_entity=is_end_entity,
        )

        return csscms_data_model_models_certificate_details
