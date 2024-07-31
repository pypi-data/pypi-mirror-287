from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHUsersSshUserUpdateRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHUsersSshUserUpdateRequest:
    """
    Attributes:
        id (int):
        logon_ids (Union[Unset, None, List[int]]):
    """

    id: int
    logon_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        logon_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.logon_ids, Unset):
            if self.logon_ids is None:
                logon_ids = None
            else:
                logon_ids = self.logon_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if logon_ids is not UNSET:
            field_dict["logonIds"] = logon_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        logon_ids = cast(List[int], d.pop("logonIds", UNSET))

        csscms_data_model_models_ssh_users_ssh_user_update_request = cls(
            id=id,
            logon_ids=logon_ids,
        )

        return csscms_data_model_models_ssh_users_ssh_user_update_request
