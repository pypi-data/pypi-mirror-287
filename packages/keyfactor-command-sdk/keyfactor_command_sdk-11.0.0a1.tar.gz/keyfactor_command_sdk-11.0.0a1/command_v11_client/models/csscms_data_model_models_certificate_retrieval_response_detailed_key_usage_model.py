from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateRetrievalResponseDetailedKeyUsageModel")


@_attrs_define
class CSSCMSDataModelModelsCertificateRetrievalResponseDetailedKeyUsageModel:
    """
    Attributes:
        crl_sign (Union[Unset, bool]):
        data_encipherment (Union[Unset, bool]):
        decipher_only (Union[Unset, bool]):
        digital_signature (Union[Unset, bool]):
        encipher_only (Union[Unset, bool]):
        key_agreement (Union[Unset, bool]):
        key_cert_sign (Union[Unset, bool]):
        key_encipherment (Union[Unset, bool]):
        non_repudiation (Union[Unset, bool]):
        hex_code (Union[Unset, None, str]):
    """

    crl_sign: Union[Unset, bool] = UNSET
    data_encipherment: Union[Unset, bool] = UNSET
    decipher_only: Union[Unset, bool] = UNSET
    digital_signature: Union[Unset, bool] = UNSET
    encipher_only: Union[Unset, bool] = UNSET
    key_agreement: Union[Unset, bool] = UNSET
    key_cert_sign: Union[Unset, bool] = UNSET
    key_encipherment: Union[Unset, bool] = UNSET
    non_repudiation: Union[Unset, bool] = UNSET
    hex_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        crl_sign = self.crl_sign
        data_encipherment = self.data_encipherment
        decipher_only = self.decipher_only
        digital_signature = self.digital_signature
        encipher_only = self.encipher_only
        key_agreement = self.key_agreement
        key_cert_sign = self.key_cert_sign
        key_encipherment = self.key_encipherment
        non_repudiation = self.non_repudiation
        hex_code = self.hex_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if crl_sign is not UNSET:
            field_dict["crlSign"] = crl_sign
        if data_encipherment is not UNSET:
            field_dict["dataEncipherment"] = data_encipherment
        if decipher_only is not UNSET:
            field_dict["decipherOnly"] = decipher_only
        if digital_signature is not UNSET:
            field_dict["digitalSignature"] = digital_signature
        if encipher_only is not UNSET:
            field_dict["encipherOnly"] = encipher_only
        if key_agreement is not UNSET:
            field_dict["keyAgreement"] = key_agreement
        if key_cert_sign is not UNSET:
            field_dict["keyCertSign"] = key_cert_sign
        if key_encipherment is not UNSET:
            field_dict["keyEncipherment"] = key_encipherment
        if non_repudiation is not UNSET:
            field_dict["nonRepudiation"] = non_repudiation
        if hex_code is not UNSET:
            field_dict["hexCode"] = hex_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None:
            return None
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        crl_sign = d.pop("crlSign", UNSET)

        data_encipherment = d.pop("dataEncipherment", UNSET)

        decipher_only = d.pop("decipherOnly", UNSET)

        digital_signature = d.pop("digitalSignature", UNSET)

        encipher_only = d.pop("encipherOnly", UNSET)

        key_agreement = d.pop("keyAgreement", UNSET)

        key_cert_sign = d.pop("keyCertSign", UNSET)

        key_encipherment = d.pop("keyEncipherment", UNSET)

        non_repudiation = d.pop("nonRepudiation", UNSET)

        hex_code = d.pop("hexCode", UNSET)

        csscms_data_model_models_certificate_retrieval_response_detailed_key_usage_model = cls(
            crl_sign=crl_sign,
            data_encipherment=data_encipherment,
            decipher_only=decipher_only,
            digital_signature=digital_signature,
            encipher_only=encipher_only,
            key_agreement=key_agreement,
            key_cert_sign=key_cert_sign,
            key_encipherment=key_encipherment,
            non_repudiation=non_repudiation,
            hex_code=hex_code,
        )

        return csscms_data_model_models_certificate_retrieval_response_detailed_key_usage_model
