from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreCreateServerRequest")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreCreateServerRequest:
    """
    Attributes:
        username (CSSCMSDataModelModelsKeyfactorAPISecret):
        password (CSSCMSDataModelModelsKeyfactorAPISecret):
        use_ssl (bool):
        server_type (int):
        name (str):
        container (Union[Unset, None, int]):
    """

    username: "CSSCMSDataModelModelsKeyfactorAPISecret"
    password: "CSSCMSDataModelModelsKeyfactorAPISecret"
    use_ssl: bool
    server_type: int
    name: str
    container: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        username = self.username.to_dict()

        password = self.password.to_dict()

        use_ssl = self.use_ssl
        server_type = self.server_type
        name = self.name
        container = self.container

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "username": username,
                "password": password,
                "useSSL": use_ssl,
                "serverType": server_type,
                "name": name,
            }
        )
        if container is not UNSET:
            field_dict["container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        username = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(d.pop("username"))

        password = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(d.pop("password"))

        use_ssl = d.pop("useSSL")

        server_type = d.pop("serverType")

        name = d.pop("name")

        container = d.pop("container", UNSET)

        csscms_data_model_models_certificate_store_create_server_request = cls(
            username=username,
            password=password,
            use_ssl=use_ssl,
            server_type=server_type,
            name=name,
            container=container,
        )

        return csscms_data_model_models_certificate_store_create_server_request
