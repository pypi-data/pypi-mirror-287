from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_store_inventory_certificates import (
        CSSCMSDataModelModelsCertificateStoreInventoryCertificates,
    )
    from ..models.csscms_data_model_models_certificate_store_inventory_parameters import (
        CSSCMSDataModelModelsCertificateStoreInventoryParameters,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreInventory")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreInventory:
    """
    Attributes:
        name (Union[Unset, None, str]):
        certificates (Union[Unset, None, List['CSSCMSDataModelModelsCertificateStoreInventoryCertificates']]):
        cert_store_inventory_item_id (Union[Unset, int]):
        parameters (Union[Unset, None, CSSCMSDataModelModelsCertificateStoreInventoryParameters]):
    """

    name: Union[Unset, None, str] = UNSET
    certificates: Union[Unset, None, List["CSSCMSDataModelModelsCertificateStoreInventoryCertificates"]] = UNSET
    cert_store_inventory_item_id: Union[Unset, int] = UNSET
    parameters: Union[Unset, None, "CSSCMSDataModelModelsCertificateStoreInventoryParameters"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        certificates: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certificates, Unset):
            if self.certificates is None:
                certificates = None
            else:
                certificates = []
                for certificates_item_data in self.certificates:
                    certificates_item = certificates_item_data.to_dict()

                    certificates.append(certificates_item)

        cert_store_inventory_item_id = self.cert_store_inventory_item_id
        parameters: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict() if self.parameters else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if cert_store_inventory_item_id is not UNSET:
            field_dict["certStoreInventoryItemId"] = cert_store_inventory_item_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_store_inventory_certificates import (
            CSSCMSDataModelModelsCertificateStoreInventoryCertificates,
        )
        from ..models.csscms_data_model_models_certificate_store_inventory_parameters import (
            CSSCMSDataModelModelsCertificateStoreInventoryParameters,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name", UNSET)

        certificates = []
        _certificates = d.pop("certificates", UNSET)
        for certificates_item_data in _certificates or []:
            certificates_item = CSSCMSDataModelModelsCertificateStoreInventoryCertificates.from_dict(
                certificates_item_data
            )

            certificates.append(certificates_item)

        cert_store_inventory_item_id = d.pop("certStoreInventoryItemId", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, None, CSSCMSDataModelModelsCertificateStoreInventoryParameters]
        if _parameters is None:
            parameters = None
        elif isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = CSSCMSDataModelModelsCertificateStoreInventoryParameters.from_dict(_parameters)

        csscms_data_model_models_certificate_store_inventory = cls(
            name=name,
            certificates=certificates,
            cert_store_inventory_item_id=cert_store_inventory_item_id,
            parameters=parameters,
        )

        return csscms_data_model_models_certificate_store_inventory
