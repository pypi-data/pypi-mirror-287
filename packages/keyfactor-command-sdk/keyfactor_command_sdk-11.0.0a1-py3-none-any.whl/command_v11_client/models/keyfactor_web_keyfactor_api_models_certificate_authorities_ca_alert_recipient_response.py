from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCAAlertRecipientResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCAAlertRecipientResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        email (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    email: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_authorities_ca_alert_recipient_response = cls(
            id=id,
            email=email,
        )

        return keyfactor_web_keyfactor_api_models_certificate_authorities_ca_alert_recipient_response
