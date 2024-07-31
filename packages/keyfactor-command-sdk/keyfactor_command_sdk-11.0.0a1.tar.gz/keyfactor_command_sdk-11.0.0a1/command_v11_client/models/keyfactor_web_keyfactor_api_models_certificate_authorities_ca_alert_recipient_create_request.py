from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCAAlertRecipientCreateRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCAAlertRecipientCreateRequest:
    """
    Attributes:
        emails (List[str]):
    """

    emails: List[str]

    def to_dict(self) -> Dict[str, Any]:
        emails = self.emails

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "emails": emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        emails = cast(List[str], d.pop("emails"))

        keyfactor_web_keyfactor_api_models_certificate_authorities_ca_alert_recipient_create_request = cls(
            emails=emails,
        )

        return keyfactor_web_keyfactor_api_models_certificate_authorities_ca_alert_recipient_create_request
