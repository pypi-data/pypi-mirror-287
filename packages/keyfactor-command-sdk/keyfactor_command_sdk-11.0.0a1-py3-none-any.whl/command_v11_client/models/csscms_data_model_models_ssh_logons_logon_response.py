import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_servers_server_response import (
        CSSCMSDataModelModelsSSHServersServerResponse,
    )
    from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
        CSSCMSDataModelModelsSSHUsersSshUserResponse,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHLogonsLogonResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHLogonsLogonResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        username (Union[Unset, None, str]):
        last_logon (Union[Unset, None, datetime.datetime]):
        server (Union[Unset, CSSCMSDataModelModelsSSHServersServerResponse]):
        key_count (Union[Unset, int]):
        access (Union[Unset, None, List['CSSCMSDataModelModelsSSHUsersSshUserResponse']]):
    """

    id: Union[Unset, int] = UNSET
    username: Union[Unset, None, str] = UNSET
    last_logon: Union[Unset, None, datetime.datetime] = UNSET
    server: Union[Unset, "CSSCMSDataModelModelsSSHServersServerResponse"] = UNSET
    key_count: Union[Unset, int] = UNSET
    access: Union[Unset, None, List["CSSCMSDataModelModelsSSHUsersSshUserResponse"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        last_logon: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_logon, Unset):
            last_logon = self.last_logon.isoformat()[:-6]+'Z' if self.last_logon else None

        server: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        key_count = self.key_count
        access: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access, Unset):
            if self.access is None:
                access = None
            else:
                access = []
                for access_item_data in self.access:
                    access_item = access_item_data.to_dict()

                    access.append(access_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if last_logon is not UNSET:
            field_dict["lastLogon"] = last_logon
        if server is not UNSET:
            field_dict["server"] = server
        if key_count is not UNSET:
            field_dict["keyCount"] = key_count
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_servers_server_response import (
            CSSCMSDataModelModelsSSHServersServerResponse,
        )
        from ..models.csscms_data_model_models_ssh_users_ssh_user_response import (
            CSSCMSDataModelModelsSSHUsersSshUserResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        _last_logon = d.pop("lastLogon", UNSET)
        last_logon: Union[Unset, None, datetime.datetime]
        if _last_logon is None:
            last_logon = None
        elif isinstance(_last_logon, Unset):
            last_logon = UNSET
        else:
            last_logon = isoparse(_last_logon)

        _server = d.pop("server", UNSET)
        server: Union[Unset, CSSCMSDataModelModelsSSHServersServerResponse]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = CSSCMSDataModelModelsSSHServersServerResponse.from_dict(_server)

        key_count = d.pop("keyCount", UNSET)

        access = []
        _access = d.pop("access", UNSET)
        for access_item_data in _access or []:
            access_item = CSSCMSDataModelModelsSSHUsersSshUserResponse.from_dict(access_item_data)

            access.append(access_item)

        csscms_data_model_models_ssh_logons_logon_response = cls(
            id=id,
            username=username,
            last_logon=last_logon,
            server=server,
            key_count=key_count,
            access=access,
        )

        return csscms_data_model_models_ssh_logons_logon_response
