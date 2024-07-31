from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_ssh_keys_key_generation_request import (
        CSSCMSDataModelModelsSSHKeysKeyGenerationRequest,
    )
    from ..models.csscms_data_model_models_ssh_service_accounts_service_account_user_creation_request import (
        CSSCMSDataModelModelsSSHServiceAccountsServiceAccountUserCreationRequest,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsSSHServiceAccountsServiceAccountCreationRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHServiceAccountsServiceAccountCreationRequest:
    """
    Attributes:
        key_generation_request (CSSCMSDataModelModelsSSHKeysKeyGenerationRequest):
        user (CSSCMSDataModelModelsSSHServiceAccountsServiceAccountUserCreationRequest):
        client_hostname (str):
        server_group_id (str):
    """

    key_generation_request: "CSSCMSDataModelModelsSSHKeysKeyGenerationRequest"
    user: "CSSCMSDataModelModelsSSHServiceAccountsServiceAccountUserCreationRequest"
    client_hostname: str
    server_group_id: str

    def to_dict(self) -> Dict[str, Any]:
        key_generation_request = self.key_generation_request.to_dict()

        user = self.user.to_dict()

        client_hostname = self.client_hostname
        server_group_id = self.server_group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "keyGenerationRequest": key_generation_request,
                "user": user,
                "clientHostname": client_hostname,
                "serverGroupId": server_group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_ssh_keys_key_generation_request import (
            CSSCMSDataModelModelsSSHKeysKeyGenerationRequest,
        )
        from ..models.csscms_data_model_models_ssh_service_accounts_service_account_user_creation_request import (
            CSSCMSDataModelModelsSSHServiceAccountsServiceAccountUserCreationRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        key_generation_request = CSSCMSDataModelModelsSSHKeysKeyGenerationRequest.from_dict(
            d.pop("keyGenerationRequest")
        )

        user = CSSCMSDataModelModelsSSHServiceAccountsServiceAccountUserCreationRequest.from_dict(d.pop("user"))

        client_hostname = d.pop("clientHostname")

        server_group_id = d.pop("serverGroupId")

        csscms_data_model_models_ssh_service_accounts_service_account_creation_request = cls(
            key_generation_request=key_generation_request,
            user=user,
            client_hostname=client_hostname,
            server_group_id=server_group_id,
        )

        return csscms_data_model_models_ssh_service_accounts_service_account_creation_request
