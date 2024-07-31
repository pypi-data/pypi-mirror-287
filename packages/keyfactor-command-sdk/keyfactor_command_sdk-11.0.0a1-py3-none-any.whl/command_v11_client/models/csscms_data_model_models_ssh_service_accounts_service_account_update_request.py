from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_keys_key_update_request import (
        CSSCMSDataModelModelsSSHKeysKeyUpdateRequest,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHServiceAccountsServiceAccountUpdateRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHServiceAccountsServiceAccountUpdateRequest:
    """
    Attributes:
        key_update_request (CSSCMSDataModelModelsSSHKeysKeyUpdateRequest):
        id (int):
    """

    key_update_request: "CSSCMSDataModelModelsSSHKeysKeyUpdateRequest"
    id: int

    def to_dict(self) -> Dict[str, Any]:
        key_update_request = self.key_update_request.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "keyUpdateRequest": key_update_request,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_keys_key_update_request import (
            CSSCMSDataModelModelsSSHKeysKeyUpdateRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        key_update_request = CSSCMSDataModelModelsSSHKeysKeyUpdateRequest.from_dict(d.pop("keyUpdateRequest"))

        id = d.pop("id")

        csscms_data_model_models_ssh_service_accounts_service_account_update_request = cls(
            key_update_request=key_update_request,
            id=id,
        )

        return csscms_data_model_models_ssh_service_accounts_service_account_update_request
