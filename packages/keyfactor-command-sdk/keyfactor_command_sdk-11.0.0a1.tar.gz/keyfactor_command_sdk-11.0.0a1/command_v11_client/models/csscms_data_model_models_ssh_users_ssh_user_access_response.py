from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_keys_key_response import CSSCMSDataModelModelsSSHKeysKeyResponse
    from ..models.csscms_data_model_models_ssh_logons_logon_response import CSSCMSDataModelModelsSSHLogonsLogonResponse


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHUsersSshUserAccessResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHUsersSshUserAccessResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        key (Union[Unset, CSSCMSDataModelModelsSSHKeysKeyResponse]):
        username (Union[Unset, None, str]):
        access (Union[Unset, None, List['CSSCMSDataModelModelsSSHLogonsLogonResponse']]):
        is_group (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    key: Union[Unset, "CSSCMSDataModelModelsSSHKeysKeyResponse"] = UNSET
    username: Union[Unset, None, str] = UNSET
    access: Union[Unset, None, List["CSSCMSDataModelModelsSSHLogonsLogonResponse"]] = UNSET
    is_group: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        username = self.username
        access: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access, Unset):
            if self.access is None:
                access = None
            else:
                access = []
                for access_item_data in self.access:
                    access_item = access_item_data.to_dict()

                    access.append(access_item)

        is_group = self.is_group

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if username is not UNSET:
            field_dict["username"] = username
        if access is not UNSET:
            field_dict["access"] = access
        if is_group is not UNSET:
            field_dict["isGroup"] = is_group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_keys_key_response import CSSCMSDataModelModelsSSHKeysKeyResponse
        from ..models.csscms_data_model_models_ssh_logons_logon_response import (
            CSSCMSDataModelModelsSSHLogonsLogonResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        _key = d.pop("key", UNSET)
        key: Union[Unset, CSSCMSDataModelModelsSSHKeysKeyResponse]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = CSSCMSDataModelModelsSSHKeysKeyResponse.from_dict(_key)

        username = d.pop("username", UNSET)

        access = []
        _access = d.pop("access", UNSET)
        for access_item_data in _access or []:
            access_item = CSSCMSDataModelModelsSSHLogonsLogonResponse.from_dict(access_item_data)

            access.append(access_item)

        is_group = d.pop("isGroup", UNSET)

        csscms_data_model_models_ssh_users_ssh_user_access_response = cls(
            id=id,
            key=key,
            username=username,
            access=access,
            is_group=is_group,
        )

        return csscms_data_model_models_ssh_users_ssh_user_access_response
