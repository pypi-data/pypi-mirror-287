from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_access_logon_user_access_request import (
        CSSCMSDataModelModelsSSHAccessLogonUserAccessRequest,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHAccessServerAccessRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHAccessServerAccessRequest:
    """
    Attributes:
        server_id (int):
        logon_users (List['CSSCMSDataModelModelsSSHAccessLogonUserAccessRequest']):
    """

    server_id: int
    logon_users: List["CSSCMSDataModelModelsSSHAccessLogonUserAccessRequest"]

    def to_dict(self) -> Dict[str, Any]:
        server_id = self.server_id
        logon_users = []
        for logon_users_item_data in self.logon_users:
            logon_users_item = logon_users_item_data.to_dict()

            logon_users.append(logon_users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "serverId": server_id,
                "logonUsers": logon_users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_access_logon_user_access_request import (
            CSSCMSDataModelModelsSSHAccessLogonUserAccessRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        server_id = d.pop("serverId")

        logon_users = []
        _logon_users = d.pop("logonUsers")
        for logon_users_item_data in _logon_users:
            logon_users_item = CSSCMSDataModelModelsSSHAccessLogonUserAccessRequest.from_dict(logon_users_item_data)

            logon_users.append(logon_users_item)

        csscms_data_model_models_ssh_access_server_access_request = cls(
            server_id=server_id,
            logon_users=logon_users,
        )

        return csscms_data_model_models_ssh_access_server_access_request
