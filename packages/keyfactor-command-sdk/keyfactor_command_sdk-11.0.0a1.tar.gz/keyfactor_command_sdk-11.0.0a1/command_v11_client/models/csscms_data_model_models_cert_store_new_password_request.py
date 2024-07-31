from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CSSCMSDataModelModelsCertStoreNewPasswordRequest")


@_attrs_define
class CSSCMSDataModelModelsCertStoreNewPasswordRequest:
    """
    Attributes:
        cert_store_id (str):
        new_password (Any):
    """

    cert_store_id: str
    new_password: Any

    def to_dict(self) -> Dict[str, Any]:
        cert_store_id = self.cert_store_id
        new_password = self.new_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "certStoreId": cert_store_id,
                "newPassword": new_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        cert_store_id = d.pop("certStoreId")

        new_password = d.pop("newPassword")

        csscms_data_model_models_cert_store_new_password_request = cls(
            cert_store_id=cert_store_id,
            new_password=new_password,
        )

        return csscms_data_model_models_cert_store_new_password_request
