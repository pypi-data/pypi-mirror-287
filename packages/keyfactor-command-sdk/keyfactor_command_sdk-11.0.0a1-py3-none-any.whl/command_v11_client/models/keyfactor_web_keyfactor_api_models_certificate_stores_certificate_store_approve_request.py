from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest:
    """
    Attributes:
        id (Union[Unset, str]):
        container_id (Union[Unset, None, int]):
        cert_store_type (Union[Unset, int]):
        properties (Union[Unset, None, str]):
        password (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
    """

    id: Union[Unset, str] = UNSET
    container_id: Union[Unset, None, int] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    properties: Union[Unset, None, str] = UNSET
    password: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        container_id = self.container_id
        cert_store_type = self.cert_store_type
        properties = self.properties
        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if container_id is not UNSET:
            field_dict["containerId"] = container_id
        if cert_store_type is not UNSET:
            field_dict["certStoreType"] = cert_store_type
        if properties is not UNSET:
            field_dict["properties"] = properties
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        container_id = d.pop("containerId", UNSET)

        cert_store_type = d.pop("certStoreType", UNSET)

        properties = d.pop("properties", UNSET)

        _password = d.pop("password", UNSET)
        password: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_password)

        keyfactor_web_keyfactor_api_models_certificate_stores_certificate_store_approve_request = cls(
            id=id,
            container_id=container_id,
            cert_store_type=cert_store_type,
            properties=properties,
            password=password,
        )

        return keyfactor_web_keyfactor_api_models_certificate_stores_certificate_store_approve_request
