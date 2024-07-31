from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificatesAnalyzeCertificateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificatesAnalyzeCertificateRequest:
    """
    Attributes:
        certificate (Union[Unset, None, str]):
        password (Union[Unset, None, str]):
    """

    certificate: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate = self.certificate
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        certificate = d.pop("certificate", UNSET)

        password = d.pop("password", UNSET)

        keyfactor_web_keyfactor_api_models_certificates_analyze_certificate_request = cls(
            certificate=certificate,
            password=password,
        )

        return keyfactor_web_keyfactor_api_models_certificates_analyze_certificate_request
