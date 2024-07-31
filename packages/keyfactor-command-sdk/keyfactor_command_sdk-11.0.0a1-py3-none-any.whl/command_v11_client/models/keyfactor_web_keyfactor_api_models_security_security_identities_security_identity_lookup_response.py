from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentitiesSecurityIdentityLookupResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecuritySecurityIdentitiesSecurityIdentityLookupResponse:
    """A public DTO representing the result of a security identity lookup.

    Attributes:
        valid (Union[Unset, bool]): Whether or not the identity is valid.
    """

    valid: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        valid = self.valid

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        valid = d.pop("valid", UNSET)

        keyfactor_web_keyfactor_api_models_security_security_identities_security_identity_lookup_response = cls(
            valid=valid,
        )

        return keyfactor_web_keyfactor_api_models_security_security_identities_security_identity_lookup_response
