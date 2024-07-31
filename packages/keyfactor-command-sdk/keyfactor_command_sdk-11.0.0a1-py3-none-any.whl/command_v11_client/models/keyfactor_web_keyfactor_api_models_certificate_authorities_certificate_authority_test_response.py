from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCertificateAuthorityTestResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCertificateAuthorityTestResponse:
    """A DTO for CA tests.

    Attributes:
        success (Union[Unset, bool]): Whether the test succeeded or failed.
        message (Union[Unset, None, str]): The message returned by the test.
    """

    success: Union[Unset, bool] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        success = self.success
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_authorities_certificate_authority_test_response = cls(
            success=success,
            message=message,
        )

        return keyfactor_web_keyfactor_api_models_certificate_authorities_certificate_authority_test_response
