from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_server_groups_server_group_response import (
        CSSCMSDataModelModelsSSHServerGroupsServerGroupResponse,
    )
    from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
        CSSCMSDataModelModelsSSHUsersSshUserResponse,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHServiceAccountsServiceAccountResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHServiceAccountsServiceAccountResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        client_hostname (Union[Unset, None, str]):
        server_group (Union[Unset, CSSCMSDataModelModelsSSHServerGroupsServerGroupResponse]):
        user (Union[Unset, CSSCMSDataModelModelsSSHUsersSshUserResponse]):
    """

    id: Union[Unset, int] = UNSET
    client_hostname: Union[Unset, None, str] = UNSET
    server_group: Union[Unset, "CSSCMSDataModelModelsSSHServerGroupsServerGroupResponse"] = UNSET
    user: Union[Unset, "CSSCMSDataModelModelsSSHUsersSshUserResponse"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        client_hostname = self.client_hostname
        server_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_group, Unset):
            server_group = self.server_group.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if client_hostname is not UNSET:
            field_dict["clientHostname"] = client_hostname
        if server_group is not UNSET:
            field_dict["serverGroup"] = server_group
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_server_groups_server_group_response import (
            CSSCMSDataModelModelsSSHServerGroupsServerGroupResponse,
        )
        from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
            CSSCMSDataModelModelsSSHUsersSshUserResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        client_hostname = d.pop("clientHostname", UNSET)

        _server_group = d.pop("serverGroup", UNSET)
        server_group: Union[Unset, CSSCMSDataModelModelsSSHServerGroupsServerGroupResponse]
        if isinstance(_server_group, Unset):
            server_group = UNSET
        else:
            server_group = CSSCMSDataModelModelsSSHServerGroupsServerGroupResponse.from_dict(_server_group)

        _user = d.pop("user", UNSET)
        user: Union[Unset, CSSCMSDataModelModelsSSHUsersSshUserResponse]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = CSSCMSDataModelModelsSSHUsersSshUserResponse.from_dict(_user)

        csscms_data_model_models_ssh_service_accounts_service_account_response = cls(
            id=id,
            client_hostname=client_hostname,
            server_group=server_group,
            user=user,
        )

        return csscms_data_model_models_ssh_service_accounts_service_account_response
