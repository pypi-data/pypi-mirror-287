from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHLogonsLogonCreationRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHLogonsLogonCreationRequest:
    """
    Attributes:
        username (str):
        server_id (int):
        user_ids (Union[Unset, None, List[int]]):
    """

    username: str
    server_id: int
    user_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        server_id = self.server_id
        user_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.user_ids, Unset):
            if self.user_ids is None:
                user_ids = None
            else:
                user_ids = self.user_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "username": username,
                "serverId": server_id,
            }
        )
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        username = d.pop("username")

        server_id = d.pop("serverId")

        user_ids = cast(List[int], d.pop("userIds", UNSET))

        csscms_data_model_models_ssh_logons_logon_creation_request = cls(
            username=username,
            server_id=server_id,
            user_ids=user_ids,
        )

        return csscms_data_model_models_ssh_logons_logon_creation_request
