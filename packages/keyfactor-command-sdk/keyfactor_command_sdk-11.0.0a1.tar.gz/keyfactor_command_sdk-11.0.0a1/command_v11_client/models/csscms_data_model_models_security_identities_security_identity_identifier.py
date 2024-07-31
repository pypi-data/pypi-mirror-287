from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSecurityIdentitiesSecurityIdentityIdentifier")


@_attrs_define
class CSSCMSDataModelModelsSecurityIdentitiesSecurityIdentityIdentifier:
    """
    Attributes:
        account_name (Union[Unset, None, str]):
        sid (Union[Unset, None, str]):
    """

    account_name: Union[Unset, None, str] = UNSET
    sid: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        account_name = self.account_name
        sid = self.sid

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if sid is not UNSET:
            field_dict["sid"] = sid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        account_name = d.pop("accountName", UNSET)

        sid = d.pop("sid", UNSET)

        csscms_data_model_models_security_identities_security_identity_identifier = cls(
            account_name=account_name,
            sid=sid,
        )

        return csscms_data_model_models_security_identities_security_identity_identifier
