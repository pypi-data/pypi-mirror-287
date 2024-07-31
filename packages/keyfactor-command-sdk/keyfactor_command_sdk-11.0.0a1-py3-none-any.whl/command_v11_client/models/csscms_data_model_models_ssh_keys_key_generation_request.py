from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_ssh_key_algorithm import CSSCMSDataModelEnumsSshKeyAlgorithm
from ..models.csscms_data_model_enums_ssh_private_key_format import CSSCMSDataModelEnumsSshPrivateKeyFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSHKeysKeyGenerationRequest")


@_attrs_define
class CSSCMSDataModelModelsSSHKeysKeyGenerationRequest:
    """
    Attributes:
        key_type (str):
        private_key_format (str):
        key_length (int):
        email (str):
        password (str):
        key_type_enum (Union[Unset, CSSCMSDataModelEnumsSshKeyAlgorithm]):
        private_key_format_enum (Union[Unset, CSSCMSDataModelEnumsSshPrivateKeyFormat]):
        comment (Union[Unset, None, str]):
    """

    key_type: str
    private_key_format: str
    key_length: int
    email: str
    password: str
    key_type_enum: Union[Unset, CSSCMSDataModelEnumsSshKeyAlgorithm] = UNSET
    private_key_format_enum: Union[Unset, CSSCMSDataModelEnumsSshPrivateKeyFormat] = UNSET
    comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        key_type = self.key_type
        private_key_format = self.private_key_format
        key_length = self.key_length
        email = self.email
        password = self.password
        key_type_enum: Union[Unset, int] = UNSET
        if not isinstance(self.key_type_enum, Unset):
            key_type_enum = self.key_type_enum.value

        private_key_format_enum: Union[Unset, int] = UNSET
        if not isinstance(self.private_key_format_enum, Unset):
            private_key_format_enum = self.private_key_format_enum.value

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "keyType": key_type,
                "privateKeyFormat": private_key_format,
                "keyLength": key_length,
                "email": email,
                "password": password,
            }
        )
        if key_type_enum is not UNSET:
            field_dict["keyTypeEnum"] = key_type_enum
        if private_key_format_enum is not UNSET:
            field_dict["privateKeyFormatEnum"] = private_key_format_enum
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        key_type = d.pop("keyType")

        private_key_format = d.pop("privateKeyFormat")

        key_length = d.pop("keyLength")

        email = d.pop("email")

        password = d.pop("password")

        _key_type_enum = d.pop("keyTypeEnum", UNSET)
        key_type_enum: Union[Unset, CSSCMSDataModelEnumsSshKeyAlgorithm]
        if isinstance(_key_type_enum, Unset):
            key_type_enum = UNSET
        else:
            key_type_enum = CSSCMSDataModelEnumsSshKeyAlgorithm(_key_type_enum)

        _private_key_format_enum = d.pop("privateKeyFormatEnum", UNSET)
        private_key_format_enum: Union[Unset, CSSCMSDataModelEnumsSshPrivateKeyFormat]
        if isinstance(_private_key_format_enum, Unset):
            private_key_format_enum = UNSET
        else:
            private_key_format_enum = CSSCMSDataModelEnumsSshPrivateKeyFormat(_private_key_format_enum)

        comment = d.pop("comment", UNSET)

        csscms_data_model_models_ssh_keys_key_generation_request = cls(
            key_type=key_type,
            private_key_format=private_key_format,
            key_length=key_length,
            email=email,
            password=password,
            key_type_enum=key_type_enum,
            private_key_format_enum=private_key_format_enum,
            comment=comment,
        )

        return csscms_data_model_models_ssh_keys_key_generation_request
