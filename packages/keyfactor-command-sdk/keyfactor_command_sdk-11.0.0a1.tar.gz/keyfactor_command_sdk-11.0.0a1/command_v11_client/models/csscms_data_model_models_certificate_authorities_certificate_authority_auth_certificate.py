import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateAuthoritiesCertificateAuthorityAuthCertificate")


@_attrs_define
class CSSCMSDataModelModelsCertificateAuthoritiesCertificateAuthorityAuthCertificate:
    """
    Attributes:
        issued_dn (Union[Unset, None, str]):
        issuer_dn (Union[Unset, None, str]):
        thumbprint (Union[Unset, None, str]):
        expiration_date (Union[Unset, datetime.datetime]):
    """

    issued_dn: Union[Unset, None, str] = UNSET
    issuer_dn: Union[Unset, None, str] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        issued_dn = self.issued_dn
        issuer_dn = self.issuer_dn
        thumbprint = self.thumbprint
        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if issued_dn is not UNSET:
            field_dict["issuedDN"] = issued_dn
        if issuer_dn is not UNSET:
            field_dict["issuerDN"] = issuer_dn
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        issued_dn = d.pop("issuedDN", UNSET)

        issuer_dn = d.pop("issuerDN", UNSET)

        thumbprint = d.pop("thumbprint", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        csscms_data_model_models_certificate_authorities_certificate_authority_auth_certificate = cls(
            issued_dn=issued_dn,
            issuer_dn=issuer_dn,
            thumbprint=thumbprint,
            expiration_date=expiration_date,
        )

        return csscms_data_model_models_certificate_authorities_certificate_authority_auth_certificate
