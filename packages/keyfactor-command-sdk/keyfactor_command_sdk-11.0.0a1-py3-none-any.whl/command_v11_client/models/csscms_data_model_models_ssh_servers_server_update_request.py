from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHServersServerUpdateRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHServersServerUpdateRequest:
    """
    Attributes:
        id (int):
        under_management (Union[Unset, None, bool]):
        port (Union[Unset, None, int]):
    """

    id: int
    under_management: Union[Unset, None, bool] = UNSET
    port: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        under_management = self.under_management
        port = self.port

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if under_management is not UNSET:
            field_dict["underManagement"] = under_management
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        under_management = d.pop("underManagement", UNSET)

        port = d.pop("port", UNSET)

        csscms_data_model_models_ssh_servers_server_update_request = cls(
            id=id,
            under_management=under_management,
            port=port,
        )

        return csscms_data_model_models_ssh_servers_server_update_request
