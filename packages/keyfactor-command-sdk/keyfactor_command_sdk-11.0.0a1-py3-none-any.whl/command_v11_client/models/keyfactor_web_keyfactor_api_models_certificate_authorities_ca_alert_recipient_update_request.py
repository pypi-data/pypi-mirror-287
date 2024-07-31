from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCAAlertRecipientUpdateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCAAlertRecipientUpdateRequest:
    """
    Attributes:
        email (str):
    """

    email: str

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        email = d.pop("email")

        keyfactor_web_keyfactor_api_models_certificate_authorities_ca_alert_recipient_update_request = cls(
            email=email,
        )

        return keyfactor_web_keyfactor_api_models_certificate_authorities_ca_alert_recipient_update_request
