from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedCustomer")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedCustomer:
    """
    Attributes:
        name (Union[Unset, None, str]):
        id (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        keyfactor_web_keyfactor_api_models_license_license_response_licensed_customer = cls(
            name=name,
            id=id,
        )

        return keyfactor_web_keyfactor_api_models_license_license_response_licensed_customer
