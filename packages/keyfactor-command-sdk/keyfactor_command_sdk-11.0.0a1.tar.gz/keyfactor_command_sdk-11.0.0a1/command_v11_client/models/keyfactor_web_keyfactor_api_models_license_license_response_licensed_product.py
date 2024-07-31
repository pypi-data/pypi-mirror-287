from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_license_license_response_licensed_feature import (
        KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedFeature,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedProduct")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedProduct:
    """
    Attributes:
        product_id (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        major_rev (Union[Unset, None, str]):
        minor_rev (Union[Unset, None, str]):
        licensed_features (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedFeature']]):
    """

    product_id: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    major_rev: Union[Unset, None, str] = UNSET
    minor_rev: Union[Unset, None, str] = UNSET
    licensed_features: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedFeature"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id
        display_name = self.display_name
        major_rev = self.major_rev
        minor_rev = self.minor_rev
        licensed_features: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licensed_features, Unset):
            if self.licensed_features is None:
                licensed_features = None
            else:
                licensed_features = []
                for licensed_features_item_data in self.licensed_features:
                    licensed_features_item = licensed_features_item_data.to_dict()

                    licensed_features.append(licensed_features_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if major_rev is not UNSET:
            field_dict["majorRev"] = major_rev
        if minor_rev is not UNSET:
            field_dict["minorRev"] = minor_rev
        if licensed_features is not UNSET:
            field_dict["licensedFeatures"] = licensed_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_license_license_response_licensed_feature import (
            KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedFeature,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        product_id = d.pop("productId", UNSET)

        display_name = d.pop("displayName", UNSET)

        major_rev = d.pop("majorRev", UNSET)

        minor_rev = d.pop("minorRev", UNSET)

        licensed_features = []
        _licensed_features = d.pop("licensedFeatures", UNSET)
        for licensed_features_item_data in _licensed_features or []:
            licensed_features_item = KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedFeature.from_dict(
                licensed_features_item_data
            )

            licensed_features.append(licensed_features_item)

        keyfactor_web_keyfactor_api_models_license_license_response_licensed_product = cls(
            product_id=product_id,
            display_name=display_name,
            major_rev=major_rev,
            minor_rev=minor_rev,
            licensed_features=licensed_features,
        )

        return keyfactor_web_keyfactor_api_models_license_license_response_licensed_product
