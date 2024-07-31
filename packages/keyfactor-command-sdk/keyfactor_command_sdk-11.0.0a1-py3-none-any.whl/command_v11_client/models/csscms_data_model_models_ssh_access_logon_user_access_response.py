from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
        CSSCMSDataModelModelsSSHUsersSshUserResponse,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHAccessLogonUserAccessResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHAccessLogonUserAccessResponse:
    """
    Attributes:
        logon_id (Union[Unset, None, int]):
        logon_name (Union[Unset, None, str]):
        users (Union[Unset, None, List['CSSCMSDataModelModelsSSHUsersSshUserResponse']]):
    """

    logon_id: Union[Unset, None, int] = UNSET
    logon_name: Union[Unset, None, str] = UNSET
    users: Union[Unset, None, List["CSSCMSDataModelModelsSSHUsersSshUserResponse"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        logon_id = self.logon_id
        logon_name = self.logon_name
        users: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            if self.users is None:
                users = None
            else:
                users = []
                for users_item_data in self.users:
                    users_item = users_item_data.to_dict()

                    users.append(users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if logon_id is not UNSET:
            field_dict["logonId"] = logon_id
        if logon_name is not UNSET:
            field_dict["logonName"] = logon_name
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
            CSSCMSDataModelModelsSSHUsersSshUserResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        logon_id = d.pop("logonId", UNSET)

        logon_name = d.pop("logonName", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = CSSCMSDataModelModelsSSHUsersSshUserResponse.from_dict(users_item_data)

            users.append(users_item)

        csscms_data_model_models_ssh_access_logon_user_access_response = cls(
            logon_id=logon_id,
            logon_name=logon_name,
            users=users,
        )

        return csscms_data_model_models_ssh_access_logon_user_access_response
