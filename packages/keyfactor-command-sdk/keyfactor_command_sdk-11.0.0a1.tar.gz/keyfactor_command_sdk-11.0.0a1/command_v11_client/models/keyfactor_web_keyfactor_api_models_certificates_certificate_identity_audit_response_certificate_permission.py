from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="KeyfactorWebKeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission"
)


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission:
    """Represents a permission granted to an account for a certificate

    Attributes:
        name (Union[Unset, None, str]): The name of the permission
        granted_by (Union[Unset, None, List[str]]): A list of roles or collections that grant the given permission
    """

    name: Union[Unset, None, str] = UNSET
    granted_by: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        granted_by: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.granted_by, Unset):
            if self.granted_by is None:
                granted_by = None
            else:
                granted_by = self.granted_by

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if granted_by is not UNSET:
            field_dict["grantedBy"] = granted_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name", UNSET)

        granted_by = cast(List[str], d.pop("grantedBy", UNSET))

        keyfactor_web_keyfactor_api_models_certificates_certificate_identity_audit_response_certificate_permission = (
            cls(
                name=name,
                granted_by=granted_by,
            )
        )

        return (
            keyfactor_web_keyfactor_api_models_certificates_certificate_identity_audit_response_certificate_permission
        )
