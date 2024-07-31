from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest:
    """
    Attributes:
        ids (Union[Unset, None, List[int]]):
    """

    ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.ids, Unset):
            if self.ids is None:
                ids = None
            else:
                ids = self.ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        ids = cast(List[int], d.pop("ids", UNSET))

        keyfactor_web_keyfactor_api_models_security_legacy_security_roles_role_identities_request = cls(
            ids=ids,
        )

        return keyfactor_web_keyfactor_api_models_security_legacy_security_roles_role_identities_request
