from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_license_license_response_license import (
        KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicense,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsLicenseLicenseResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsLicenseLicenseResponse:
    """
    Attributes:
        keyfactor_version (Union[Unset, None, str]):
        license_data (Union[Unset, KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicense]):
    """

    keyfactor_version: Union[Unset, None, str] = UNSET
    license_data: Union[Unset, "KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicense"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyfactor_version = self.keyfactor_version
        license_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_data, Unset):
            license_data = self.license_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keyfactor_version is not UNSET:
            field_dict["keyfactorVersion"] = keyfactor_version
        if license_data is not UNSET:
            field_dict["licenseData"] = license_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_license_license_response_license import (
            KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicense,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        keyfactor_version = d.pop("keyfactorVersion", UNSET)

        _license_data = d.pop("licenseData", UNSET)
        license_data: Union[Unset, KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicense]
        if isinstance(_license_data, Unset):
            license_data = UNSET
        else:
            license_data = KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicense.from_dict(_license_data)

        keyfactor_web_keyfactor_api_models_license_license_response = cls(
            keyfactor_version=keyfactor_version,
            license_data=license_data,
        )

        return keyfactor_web_keyfactor_api_models_license_license_response
