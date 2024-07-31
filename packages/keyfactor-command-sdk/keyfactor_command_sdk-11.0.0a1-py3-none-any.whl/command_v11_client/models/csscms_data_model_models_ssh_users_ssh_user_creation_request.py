from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHUsersSshUserCreationRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHUsersSshUserCreationRequest:
    """
    Attributes:
        username (str):
        logon_ids (Union[Unset, None, List[int]]):
    """

    username: str
    logon_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        logon_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.logon_ids, Unset):
            if self.logon_ids is None:
                logon_ids = None
            else:
                logon_ids = self.logon_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "username": username,
            }
        )
        if logon_ids is not UNSET:
            field_dict["logonIds"] = logon_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        username = d.pop("username")

        logon_ids = cast(List[int], d.pop("logonIds", UNSET))

        csscms_data_model_models_ssh_users_ssh_user_creation_request = cls(
            username=username,
            logon_ids=logon_ids,
        )

        return csscms_data_model_models_ssh_users_ssh_user_creation_request
