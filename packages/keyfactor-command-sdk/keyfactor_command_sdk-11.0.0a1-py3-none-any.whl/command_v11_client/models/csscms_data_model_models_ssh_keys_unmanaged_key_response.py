import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHKeysUnmanagedKeyResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHKeysUnmanagedKeyResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        fingerprint (Union[Unset, None, str]):
        public_key (Union[Unset, None, str]):
        private_key (Union[Unset, None, str]):
        key_type (Union[Unset, None, str]):
        key_length (Union[Unset, int]):
        discovered_date (Union[Unset, None, datetime.datetime]):
        email (Union[Unset, None, str]):
        comments (Union[Unset, None, List[str]]):
        username (Union[Unset, None, str]):
        logon_count (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    fingerprint: Union[Unset, None, str] = UNSET
    public_key: Union[Unset, None, str] = UNSET
    private_key: Union[Unset, None, str] = UNSET
    key_type: Union[Unset, None, str] = UNSET
    key_length: Union[Unset, int] = UNSET
    discovered_date: Union[Unset, None, datetime.datetime] = UNSET
    email: Union[Unset, None, str] = UNSET
    comments: Union[Unset, None, List[str]] = UNSET
    username: Union[Unset, None, str] = UNSET
    logon_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        fingerprint = self.fingerprint
        public_key = self.public_key
        private_key = self.private_key
        key_type = self.key_type
        key_length = self.key_length
        discovered_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.discovered_date, Unset):
            discovered_date = self.discovered_date.isoformat()[:-6]+'Z' if self.discovered_date else None

        email = self.email
        comments: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.comments, Unset):
            if self.comments is None:
                comments = None
            else:
                comments = self.comments

        username = self.username
        logon_count = self.logon_count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if key_type is not UNSET:
            field_dict["keyType"] = key_type
        if key_length is not UNSET:
            field_dict["keyLength"] = key_length
        if discovered_date is not UNSET:
            field_dict["discoveredDate"] = discovered_date
        if email is not UNSET:
            field_dict["email"] = email
        if comments is not UNSET:
            field_dict["comments"] = comments
        if username is not UNSET:
            field_dict["username"] = username
        if logon_count is not UNSET:
            field_dict["logonCount"] = logon_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        public_key = d.pop("publicKey", UNSET)

        private_key = d.pop("privateKey", UNSET)

        key_type = d.pop("keyType", UNSET)

        key_length = d.pop("keyLength", UNSET)

        _discovered_date = d.pop("discoveredDate", UNSET)
        discovered_date: Union[Unset, None, datetime.datetime]
        if _discovered_date is None:
            discovered_date = None
        elif isinstance(_discovered_date, Unset):
            discovered_date = UNSET
        else:
            discovered_date = isoparse(_discovered_date)

        email = d.pop("email", UNSET)

        comments = cast(List[str], d.pop("comments", UNSET))

        username = d.pop("username", UNSET)

        logon_count = d.pop("logonCount", UNSET)

        csscms_data_model_models_ssh_keys_unmanaged_key_response = cls(
            id=id,
            fingerprint=fingerprint,
            public_key=public_key,
            private_key=private_key,
            key_type=key_type,
            key_length=key_length,
            discovered_date=discovered_date,
            email=email,
            comments=comments,
            username=username,
            logon_count=logon_count,
        )

        return csscms_data_model_models_ssh_keys_unmanaged_key_response
