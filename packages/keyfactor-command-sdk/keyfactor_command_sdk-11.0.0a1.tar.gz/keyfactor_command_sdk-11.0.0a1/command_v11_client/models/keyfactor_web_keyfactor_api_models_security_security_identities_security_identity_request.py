from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentitiesSecurityIdentityRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentitiesSecurityIdentityRequest:
    """Model for requesting a security identity.

    Attributes:
        account_name (str): The username of the security identity.
    """

    account_name: str

    def to_dict(self) -> Dict[str, Any]:
        account_name = self.account_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "accountName": account_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        account_name = d.pop("accountName")

        keyfactor_web_keyfactor_api_models_security_security_identities_security_identity_request = cls(
            account_name=account_name,
        )

        return keyfactor_web_keyfactor_api_models_security_security_identities_security_identity_request
