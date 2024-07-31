import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHKeysKeyResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHKeysKeyResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        fingerprint (Union[Unset, None, str]):
        public_key (Union[Unset, None, str]):
        private_key (Union[Unset, None, str]):
        key_type (Union[Unset, None, str]):
        key_length (Union[Unset, int]):
        creation_date (Union[Unset, None, datetime.datetime]):
        stale_date (Union[Unset, None, datetime.datetime]):
        email (Union[Unset, None, str]):
        comments (Union[Unset, None, List[str]]):
        logon_count (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    fingerprint: Union[Unset, None, str] = UNSET
    public_key: Union[Unset, None, str] = UNSET
    private_key: Union[Unset, None, str] = UNSET
    key_type: Union[Unset, None, str] = UNSET
    key_length: Union[Unset, int] = UNSET
    creation_date: Union[Unset, None, datetime.datetime] = UNSET
    stale_date: Union[Unset, None, datetime.datetime] = UNSET
    email: Union[Unset, None, str] = UNSET
    comments: Union[Unset, None, List[str]] = UNSET
    logon_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        fingerprint = self.fingerprint
        public_key = self.public_key
        private_key = self.private_key
        key_type = self.key_type
        key_length = self.key_length
        creation_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()[:-6]+'Z' if self.creation_date else None

        stale_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.stale_date, Unset):
            stale_date = self.stale_date.isoformat()[:-6]+'Z' if self.stale_date else None

        email = self.email
        comments: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.comments, Unset):
            if self.comments is None:
                comments = None
            else:
                comments = self.comments

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
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if stale_date is not UNSET:
            field_dict["staleDate"] = stale_date
        if email is not UNSET:
            field_dict["email"] = email
        if comments is not UNSET:
            field_dict["comments"] = comments
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

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, None, datetime.datetime]
        if _creation_date is None:
            creation_date = None
        elif isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _stale_date = d.pop("staleDate", UNSET)
        stale_date: Union[Unset, None, datetime.datetime]
        if _stale_date is None:
            stale_date = None
        elif isinstance(_stale_date, Unset):
            stale_date = UNSET
        else:
            stale_date = isoparse(_stale_date)

        email = d.pop("email", UNSET)

        comments = cast(List[str], d.pop("comments", UNSET))

        logon_count = d.pop("logonCount", UNSET)

        csscms_data_model_models_ssh_keys_key_response = cls(
            id=id,
            fingerprint=fingerprint,
            public_key=public_key,
            private_key=private_key,
            key_type=key_type,
            key_length=key_length,
            creation_date=creation_date,
            stale_date=stale_date,
            email=email,
            comments=comments,
            logon_count=logon_count,
        )

        return csscms_data_model_models_ssh_keys_key_response
