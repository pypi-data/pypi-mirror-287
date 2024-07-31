from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHAccessLogonUserAccessRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHAccessLogonUserAccessRequest:
    """
    Attributes:
        logon_name (Union[Unset, None, str]):
        users (Union[Unset, None, List[str]]):
    """

    logon_name: Union[Unset, None, str] = UNSET
    users: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        logon_name = self.logon_name
        users: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.users, Unset):
            if self.users is None:
                users = None
            else:
                users = self.users

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if logon_name is not UNSET:
            field_dict["logonName"] = logon_name
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        logon_name = d.pop("logonName", UNSET)

        users = cast(List[str], d.pop("users", UNSET))

        csscms_data_model_models_ssh_access_logon_user_access_request = cls(
            logon_name=logon_name,
            users=users,
        )

        return csscms_data_model_models_ssh_access_logon_user_access_request
