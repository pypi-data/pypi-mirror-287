from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreServerResponse")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreServerResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        use_ssl (Union[Unset, bool]):
        server_type (Union[Unset, int]):
        name (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    use_ssl: Union[Unset, bool] = UNSET
    server_type: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        use_ssl = self.use_ssl
        server_type = self.server_type
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        use_ssl = d.pop("useSSL", UNSET)

        server_type = d.pop("serverType", UNSET)

        name = d.pop("name", UNSET)

        csscms_data_model_models_certificate_store_server_response = cls(
            id=id,
            use_ssl=use_ssl,
            server_type=server_type,
            name=name,
        )

        return csscms_data_model_models_certificate_store_server_response
