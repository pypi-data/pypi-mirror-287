from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_keys_key_response import CSSCMSDataModelModelsSSHKeysKeyResponse


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHUsersSshUserResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHUsersSshUserResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        key (Union[Unset, CSSCMSDataModelModelsSSHKeysKeyResponse]):
        username (Union[Unset, None, str]):
        logon_ids (Union[Unset, None, List[int]]):
    """

    id: Union[Unset, int] = UNSET
    key: Union[Unset, "CSSCMSDataModelModelsSSHKeysKeyResponse"] = UNSET
    username: Union[Unset, None, str] = UNSET
    logon_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        username = self.username
        logon_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.logon_ids, Unset):
            if self.logon_ids is None:
                logon_ids = None
            else:
                logon_ids = self.logon_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if username is not UNSET:
            field_dict["username"] = username
        if logon_ids is not UNSET:
            field_dict["logonIds"] = logon_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_keys_key_response import CSSCMSDataModelModelsSSHKeysKeyResponse

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        _key = d.pop("key", UNSET)
        key: Union[Unset, CSSCMSDataModelModelsSSHKeysKeyResponse]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = CSSCMSDataModelModelsSSHKeysKeyResponse.from_dict(_key)

        username = d.pop("username", UNSET)

        logon_ids = cast(List[int], d.pop("logonIds", UNSET))

        csscms_data_model_models_ssh_users_ssh_user_response = cls(
            id=id,
            key=key,
            username=username,
            logon_ids=logon_ids,
        )

        return csscms_data_model_models_ssh_users_ssh_user_response
