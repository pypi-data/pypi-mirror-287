import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_store_inventory_certificates_metadata import (
        CSSCMSDataModelModelsCertificateStoreInventoryCertificatesMetadata,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreInventoryCertificates")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreInventoryCertificates:
    """
    Attributes:
        id (Union[Unset, int]):
        issued_dn (Union[Unset, None, str]):
        serial_number (Union[Unset, None, str]):
        not_before (Union[Unset, datetime.datetime]):
        not_after (Union[Unset, datetime.datetime]):
        signing_algorithm (Union[Unset, None, str]):
        issuer_dn (Union[Unset, None, str]):
        thumbprint (Union[Unset, None, str]):
        cert_store_inventory_item_id (Union[Unset, int]):
        cert_state (Union[Unset, int]):
        metadata (Union[Unset, None, CSSCMSDataModelModelsCertificateStoreInventoryCertificatesMetadata]):
    """

    id: Union[Unset, int] = UNSET
    issued_dn: Union[Unset, None, str] = UNSET
    serial_number: Union[Unset, None, str] = UNSET
    not_before: Union[Unset, datetime.datetime] = UNSET
    not_after: Union[Unset, datetime.datetime] = UNSET
    signing_algorithm: Union[Unset, None, str] = UNSET
    issuer_dn: Union[Unset, None, str] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET
    cert_store_inventory_item_id: Union[Unset, int] = UNSET
    cert_state: Union[Unset, int] = UNSET
    metadata: Union[Unset, None, "CSSCMSDataModelModelsCertificateStoreInventoryCertificatesMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        issued_dn = self.issued_dn
        serial_number = self.serial_number
        not_before: Union[Unset, str] = UNSET
        if not isinstance(self.not_before, Unset):
            not_before = self.not_before.isoformat()[:-6]+'Z'

        not_after: Union[Unset, str] = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()[:-6]+'Z'

        signing_algorithm = self.signing_algorithm
        issuer_dn = self.issuer_dn
        thumbprint = self.thumbprint
        cert_store_inventory_item_id = self.cert_store_inventory_item_id
        cert_state = self.cert_state
        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if issued_dn is not UNSET:
            field_dict["issuedDN"] = issued_dn
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if not_before is not UNSET:
            field_dict["notBefore"] = not_before
        if not_after is not UNSET:
            field_dict["notAfter"] = not_after
        if signing_algorithm is not UNSET:
            field_dict["signingAlgorithm"] = signing_algorithm
        if issuer_dn is not UNSET:
            field_dict["issuerDN"] = issuer_dn
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if cert_store_inventory_item_id is not UNSET:
            field_dict["certStoreInventoryItemId"] = cert_store_inventory_item_id
        if cert_state is not UNSET:
            field_dict["certState"] = cert_state
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_store_inventory_certificates_metadata import (
            CSSCMSDataModelModelsCertificateStoreInventoryCertificatesMetadata,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        issued_dn = d.pop("issuedDN", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        _not_before = d.pop("notBefore", UNSET)
        not_before: Union[Unset, datetime.datetime]
        if isinstance(_not_before, Unset):
            not_before = UNSET
        else:
            not_before = isoparse(_not_before)

        _not_after = d.pop("notAfter", UNSET)
        not_after: Union[Unset, datetime.datetime]
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = isoparse(_not_after)

        signing_algorithm = d.pop("signingAlgorithm", UNSET)

        issuer_dn = d.pop("issuerDN", UNSET)

        thumbprint = d.pop("thumbprint", UNSET)

        cert_store_inventory_item_id = d.pop("certStoreInventoryItemId", UNSET)

        cert_state = d.pop("certState", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CSSCMSDataModelModelsCertificateStoreInventoryCertificatesMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CSSCMSDataModelModelsCertificateStoreInventoryCertificatesMetadata.from_dict(_metadata)

        csscms_data_model_models_certificate_store_inventory_certificates = cls(
            id=id,
            issued_dn=issued_dn,
            serial_number=serial_number,
            not_before=not_before,
            not_after=not_after,
            signing_algorithm=signing_algorithm,
            issuer_dn=issuer_dn,
            thumbprint=thumbprint,
            cert_store_inventory_item_id=cert_store_inventory_item_id,
            cert_state=cert_state,
            metadata=metadata,
        )

        return csscms_data_model_models_certificate_store_inventory_certificates
