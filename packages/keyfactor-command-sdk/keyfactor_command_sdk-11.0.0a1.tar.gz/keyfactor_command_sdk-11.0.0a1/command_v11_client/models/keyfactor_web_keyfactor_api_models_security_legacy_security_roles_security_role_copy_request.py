from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleCopyRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleCopyRequest:
    """ """

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        src_dict.copy()
        keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_role_copy_request = cls()

        return keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_role_copy_request
