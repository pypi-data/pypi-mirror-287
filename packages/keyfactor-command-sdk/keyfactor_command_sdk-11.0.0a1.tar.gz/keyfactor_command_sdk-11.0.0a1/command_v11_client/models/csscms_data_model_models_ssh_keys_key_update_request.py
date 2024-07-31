from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHKeysKeyUpdateRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHKeysKeyUpdateRequest:
    """
    Attributes:
        id (int):
        email (str):
        comment (Union[Unset, None, str]):
    """

    id: int
    email: str
    comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email = self.email
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "email": email,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        email = d.pop("email")

        comment = d.pop("comment", UNSET)

        csscms_data_model_models_ssh_keys_key_update_request = cls(
            id=id,
            email=email,
            comment=comment,
        )

        return csscms_data_model_models_ssh_keys_key_update_request
