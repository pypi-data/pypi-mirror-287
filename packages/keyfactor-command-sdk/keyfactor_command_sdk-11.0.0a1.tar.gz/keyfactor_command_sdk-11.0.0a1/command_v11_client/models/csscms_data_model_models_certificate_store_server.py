from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_secret import CSSCMSDataModelModelsKeyfactorSecret


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreServer")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreServer:
    """
    Attributes:
        id (Union[Unset, int]):
        username (Union[Unset, CSSCMSDataModelModelsKeyfactorSecret]):
        password (Union[Unset, CSSCMSDataModelModelsKeyfactorSecret]):
        use_ssl (Union[Unset, bool]):
        server_type (Union[Unset, int]):
        name (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    username: Union[Unset, "CSSCMSDataModelModelsKeyfactorSecret"] = UNSET
    password: Union[Unset, "CSSCMSDataModelModelsKeyfactorSecret"] = UNSET
    use_ssl: Union[Unset, bool] = UNSET
    server_type: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.username, Unset):
            username = self.username.to_dict()

        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        use_ssl = self.use_ssl
        server_type = self.server_type
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_secret import CSSCMSDataModelModelsKeyfactorSecret

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        _username = d.pop("username", UNSET)
        username: Union[Unset, CSSCMSDataModelModelsKeyfactorSecret]
        if isinstance(_username, Unset):
            username = UNSET
        else:
            username = CSSCMSDataModelModelsKeyfactorSecret.from_dict(_username)

        _password = d.pop("password", UNSET)
        password: Union[Unset, CSSCMSDataModelModelsKeyfactorSecret]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = CSSCMSDataModelModelsKeyfactorSecret.from_dict(_password)

        use_ssl = d.pop("useSSL", UNSET)

        server_type = d.pop("serverType", UNSET)

        name = d.pop("name", UNSET)

        csscms_data_model_models_certificate_store_server = cls(
            id=id,
            username=username,
            password=password,
            use_ssl=use_ssl,
            server_type=server_type,
            name=name,
        )

        return csscms_data_model_models_certificate_store_server
