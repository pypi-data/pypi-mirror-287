from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_cert_store_locations_certificate_locations_group import (
        CSSCMSDataModelModelsCertStoreLocationsCertificateLocationsGroup,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificatesCertificateLocationsResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificatesCertificateLocationsResponse:
    """
    Attributes:
        details (Union[Unset, None, List['CSSCMSDataModelModelsCertStoreLocationsCertificateLocationsGroup']]):
    """

    details: Union[Unset, None, List["CSSCMSDataModelModelsCertStoreLocationsCertificateLocationsGroup"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        details: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            if self.details is None:
                details = None
            else:
                details = []
                for details_item_data in self.details:
                    details_item = details_item_data.to_dict()

                    details.append(details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_cert_store_locations_certificate_locations_group import (
            CSSCMSDataModelModelsCertStoreLocationsCertificateLocationsGroup,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = CSSCMSDataModelModelsCertStoreLocationsCertificateLocationsGroup.from_dict(details_item_data)

            details.append(details_item)

        keyfactor_web_keyfactor_api_models_certificates_certificate_locations_response = cls(
            details=details,
        )

        return keyfactor_web_keyfactor_api_models_certificates_certificate_locations_response
