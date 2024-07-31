from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_access_logon_user_access_response import (
        CSSCMSDataModelModelsSSHAccessLogonUserAccessResponse,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHAccessServerGroupAccessResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHAccessServerGroupAccessResponse:
    """
    Attributes:
        server_group_id (Union[Unset, str]):
        logon_users (Union[Unset, None, List['CSSCMSDataModelModelsSSHAccessLogonUserAccessResponse']]):
    """

    server_group_id: Union[Unset, str] = UNSET
    logon_users: Union[Unset, None, List["CSSCMSDataModelModelsSSHAccessLogonUserAccessResponse"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        server_group_id = self.server_group_id
        logon_users: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logon_users, Unset):
            if self.logon_users is None:
                logon_users = None
            else:
                logon_users = []
                for logon_users_item_data in self.logon_users:
                    logon_users_item = logon_users_item_data.to_dict()

                    logon_users.append(logon_users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if server_group_id is not UNSET:
            field_dict["serverGroupId"] = server_group_id
        if logon_users is not UNSET:
            field_dict["logonUsers"] = logon_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_access_logon_user_access_response import (
            CSSCMSDataModelModelsSSHAccessLogonUserAccessResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        server_group_id = d.pop("serverGroupId", UNSET)

        logon_users = []
        _logon_users = d.pop("logonUsers", UNSET)
        for logon_users_item_data in _logon_users or []:
            logon_users_item = CSSCMSDataModelModelsSSHAccessLogonUserAccessResponse.from_dict(logon_users_item_data)

            logon_users.append(logon_users_item)

        csscms_data_model_models_ssh_access_server_group_access_response = cls(
            server_group_id=server_group_id,
            logon_users=logon_users,
        )

        return csscms_data_model_models_ssh_access_server_group_access_response
