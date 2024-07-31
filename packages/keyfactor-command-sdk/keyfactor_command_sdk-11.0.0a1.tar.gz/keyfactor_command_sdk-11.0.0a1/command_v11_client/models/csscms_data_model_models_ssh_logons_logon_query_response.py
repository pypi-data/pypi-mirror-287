import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHLogonsLogonQueryResponse")


@_attrs_define
class CSSCMSDataModelModelsSSHLogonsLogonQueryResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        username (Union[Unset, None, str]):
        last_logon (Union[Unset, None, datetime.datetime]):
        server_id (Union[Unset, int]):
        server_name (Union[Unset, None, str]):
        group_name (Union[Unset, None, str]):
        key_count (Union[Unset, int]):
        server_under_management (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    username: Union[Unset, None, str] = UNSET
    last_logon: Union[Unset, None, datetime.datetime] = UNSET
    server_id: Union[Unset, int] = UNSET
    server_name: Union[Unset, None, str] = UNSET
    group_name: Union[Unset, None, str] = UNSET
    key_count: Union[Unset, int] = UNSET
    server_under_management: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        last_logon: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_logon, Unset):
            last_logon = self.last_logon.isoformat()[:-6]+'Z' if self.last_logon else None

        server_id = self.server_id
        server_name = self.server_name
        group_name = self.group_name
        key_count = self.key_count
        server_under_management = self.server_under_management

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if last_logon is not UNSET:
            field_dict["lastLogon"] = last_logon
        if server_id is not UNSET:
            field_dict["serverId"] = server_id
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if key_count is not UNSET:
            field_dict["keyCount"] = key_count
        if server_under_management is not UNSET:
            field_dict["serverUnderManagement"] = server_under_management

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        server_id = d.pop("serverId", UNSET)

        server_name = d.pop("serverName", UNSET)

        group_name = d.pop("groupName", UNSET)

        key_count = d.pop("keyCount", UNSET)

        server_under_management = d.pop("serverUnderManagement", UNSET)

        csscms_data_model_models_ssh_logons_logon_query_response = cls(
            id=id,
            username=username,
            last_logon=last_logon,
            server_id=server_id,
            server_name=server_name,
            group_name=group_name,
            key_count=key_count,
            server_under_management=server_under_management,
        )

        return csscms_data_model_models_ssh_logons_logon_query_response
