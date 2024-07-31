import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedFeature")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedFeature:
    """
    Attributes:
        feature_id (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        enabled (Union[Unset, bool]):
        quantity (Union[Unset, None, int]):
        expiration_date (Union[Unset, None, datetime.datetime]):
    """

    feature_id: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    quantity: Union[Unset, None, int] = UNSET
    expiration_date: Union[Unset, None, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        feature_id = self.feature_id
        display_name = self.display_name
        enabled = self.enabled
        quantity = self.quantity
        expiration_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()[:-6]+'Z' if self.expiration_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if feature_id is not UNSET:
            field_dict["featureID"] = feature_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        feature_id = d.pop("featureID", UNSET)

        display_name = d.pop("displayName", UNSET)

        enabled = d.pop("enabled", UNSET)

        quantity = d.pop("quantity", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, None, datetime.datetime]
        if _expiration_date is None:
            expiration_date = None
        elif isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        keyfactor_web_keyfactor_api_models_license_license_response_licensed_feature = cls(
            feature_id=feature_id,
            display_name=display_name,
            enabled=enabled,
            quantity=quantity,
            expiration_date=expiration_date,
        )

        return keyfactor_web_keyfactor_api_models_license_license_response_licensed_feature
