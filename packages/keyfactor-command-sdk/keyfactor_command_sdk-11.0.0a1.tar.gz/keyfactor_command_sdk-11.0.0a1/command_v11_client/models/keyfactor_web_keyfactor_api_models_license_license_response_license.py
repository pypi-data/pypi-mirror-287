import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_license_license_response_licensed_customer import (
        KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedCustomer,
    )
    from ..models.keyfactor_web_keyfactor_api_models_license_license_response_licensed_product import (
        KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedProduct,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicense")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicense:
    """
    Attributes:
        license_id (Union[Unset, None, str]):
        customer (Union[Unset, KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedCustomer]):
        issued_date (Union[Unset, datetime.datetime]):
        expiration_date (Union[Unset, None, datetime.datetime]):
        licensed_products (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedProduct']]):
    """

    license_id: Union[Unset, None, str] = UNSET
    customer: Union[Unset, "KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedCustomer"] = UNSET
    issued_date: Union[Unset, datetime.datetime] = UNSET
    expiration_date: Union[Unset, None, datetime.datetime] = UNSET
    licensed_products: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedProduct"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        license_id = self.license_id
        customer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        issued_date: Union[Unset, str] = UNSET
        if not isinstance(self.issued_date, Unset):
            issued_date = self.issued_date.isoformat()[:-6]+'Z'

        expiration_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()[:-6]+'Z' if self.expiration_date else None

        licensed_products: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licensed_products, Unset):
            if self.licensed_products is None:
                licensed_products = None
            else:
                licensed_products = []
                for licensed_products_item_data in self.licensed_products:
                    licensed_products_item = licensed_products_item_data.to_dict()

                    licensed_products.append(licensed_products_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if customer is not UNSET:
            field_dict["customer"] = customer
        if issued_date is not UNSET:
            field_dict["issuedDate"] = issued_date
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if licensed_products is not UNSET:
            field_dict["licensedProducts"] = licensed_products

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_license_license_response_licensed_customer import (
            KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedCustomer,
        )
        from ..models.keyfactor_web_keyfactor_api_models_license_license_response_licensed_product import (
            KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedProduct,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        license_id = d.pop("licenseId", UNSET)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedCustomer]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedCustomer.from_dict(_customer)

        _issued_date = d.pop("issuedDate", UNSET)
        issued_date: Union[Unset, datetime.datetime]
        if isinstance(_issued_date, Unset):
            issued_date = UNSET
        else:
            issued_date = isoparse(_issued_date)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, None, datetime.datetime]
        if _expiration_date is None:
            expiration_date = None
        elif isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        licensed_products = []
        _licensed_products = d.pop("licensedProducts", UNSET)
        for licensed_products_item_data in _licensed_products or []:
            licensed_products_item = KeyfactorWebKeyfactorApiModelsLicenseLicenseResponseLicensedProduct.from_dict(
                licensed_products_item_data
            )

            licensed_products.append(licensed_products_item)

        keyfactor_web_keyfactor_api_models_license_license_response_license = cls(
            license_id=license_id,
            customer=customer,
            issued_date=issued_date,
            expiration_date=expiration_date,
            licensed_products=licensed_products,
        )

        return keyfactor_web_keyfactor_api_models_license_license_response_license
