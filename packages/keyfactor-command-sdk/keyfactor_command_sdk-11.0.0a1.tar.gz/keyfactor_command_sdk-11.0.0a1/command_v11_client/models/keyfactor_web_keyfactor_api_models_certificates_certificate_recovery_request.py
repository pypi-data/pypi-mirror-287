from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest:
    """
    Attributes:
        password (str):
        cert_id (Union[Unset, None, int]):
        serial_number (Union[Unset, None, str]):
        issuer_dn (Union[Unset, None, str]):
        thumbprint (Union[Unset, None, str]):
        include_chain (Union[Unset, bool]):
        chain_order (Union[Unset, None, str]):
        use_legacy_encryption (Union[Unset, None, bool]):
    """

    password: str
    cert_id: Union[Unset, None, int] = UNSET
    serial_number: Union[Unset, None, str] = UNSET
    issuer_dn: Union[Unset, None, str] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET
    include_chain: Union[Unset, bool] = UNSET
    chain_order: Union[Unset, None, str] = UNSET
    use_legacy_encryption: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        cert_id = self.cert_id
        serial_number = self.serial_number
        issuer_dn = self.issuer_dn
        thumbprint = self.thumbprint
        include_chain = self.include_chain
        chain_order = self.chain_order
        use_legacy_encryption = self.use_legacy_encryption

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "password": password,
            }
        )
        if cert_id is not UNSET:
            field_dict["certID"] = cert_id
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if issuer_dn is not UNSET:
            field_dict["issuerDN"] = issuer_dn
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if include_chain is not UNSET:
            field_dict["includeChain"] = include_chain
        if chain_order is not UNSET:
            field_dict["chainOrder"] = chain_order
        if use_legacy_encryption is not UNSET:
            field_dict["useLegacyEncryption"] = use_legacy_encryption

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        password = d.pop("password")

        cert_id = d.pop("certID", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        issuer_dn = d.pop("issuerDN", UNSET)

        thumbprint = d.pop("thumbprint", UNSET)

        include_chain = d.pop("includeChain", UNSET)

        chain_order = d.pop("chainOrder", UNSET)

        use_legacy_encryption = d.pop("useLegacyEncryption", UNSET)

        keyfactor_web_keyfactor_api_models_certificates_certificate_recovery_request = cls(
            password=password,
            cert_id=cert_id,
            serial_number=serial_number,
            issuer_dn=issuer_dn,
            thumbprint=thumbprint,
            include_chain=include_chain,
            chain_order=chain_order,
            use_legacy_encryption=use_legacy_encryption,
        )

        return keyfactor_web_keyfactor_api_models_certificates_certificate_recovery_request
