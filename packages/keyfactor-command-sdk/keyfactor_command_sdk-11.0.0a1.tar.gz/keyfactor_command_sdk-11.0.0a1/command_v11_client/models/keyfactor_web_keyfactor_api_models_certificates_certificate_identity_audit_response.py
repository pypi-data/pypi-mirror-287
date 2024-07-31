from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_certificates_certificate_identity_audit_response_certificate_permission import (
        KeyfactorWebKeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificatesCertificateIdentityAuditResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificatesCertificateIdentityAuditResponse:
    """Represents an account with a list of permission granted to it on a given certificate by either a role or collection

    Attributes:
        id (Union[Unset, int]): Id of the account represented by the audit response
        account_name (Union[Unset, None, str]): Name of the account represented by the audit response
        identity_type (Union[Unset, None, str]): The type of account represented by the audit response (User or Group)
        sid (Union[Unset, None, str]): The SID of the account represented by the audit reponse
        permissions (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission']]):
            Permissions granted to the account represented by the audit reponse on the specified certifcate
    """

    id: Union[Unset, int] = UNSET
    account_name: Union[Unset, None, str] = UNSET
    identity_type: Union[Unset, None, str] = UNSET
    sid: Union[Unset, None, str] = UNSET
    permissions: Union[
        Unset,
        None,
        List["KeyfactorWebKeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission"],
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account_name = self.account_name
        identity_type = self.identity_type
        sid = self.sid
        permissions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = []
                for permissions_item_data in self.permissions:
                    permissions_item = permissions_item_data.to_dict()

                    permissions.append(permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if identity_type is not UNSET:
            field_dict["identityType"] = identity_type
        if sid is not UNSET:
            field_dict["sid"] = sid
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_certificates_certificate_identity_audit_response_certificate_permission import (
            KeyfactorWebKeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        account_name = d.pop("accountName", UNSET)

        identity_type = d.pop("identityType", UNSET)

        sid = d.pop("sid", UNSET)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = KeyfactorWebKeyfactorApiModelsCertificatesCertificateIdentityAuditResponseCertificatePermission.from_dict(
                permissions_item_data
            )

            permissions.append(permissions_item)

        keyfactor_web_keyfactor_api_models_certificates_certificate_identity_audit_response = cls(
            id=id,
            account_name=account_name,
            identity_type=identity_type,
            sid=sid,
            permissions=permissions,
        )

        return keyfactor_web_keyfactor_api_models_certificates_certificate_identity_audit_response
