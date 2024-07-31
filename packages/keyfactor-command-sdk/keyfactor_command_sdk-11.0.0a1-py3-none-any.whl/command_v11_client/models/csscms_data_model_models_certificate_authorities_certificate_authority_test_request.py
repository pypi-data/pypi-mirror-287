from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_core_enums_certificate_authority_type import CSSCMSCoreEnumsCertificateAuthorityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateAuthoritiesCertificateAuthorityTestRequest")


@_attrs_define
class CSSCMSDataModelModelsCertificateAuthoritiesCertificateAuthorityTestRequest:
    """
    Attributes:
        id (Union[Unset, int]):
        ca_type (Union[Unset, CSSCMSCoreEnumsCertificateAuthorityType]):
        explicit_credentials (Union[Unset, bool]):
        explicit_password (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        explicit_user (Union[Unset, None, str]):
        auth_certificate_password (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        auth_certificate (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        logical_name (Union[Unset, None, str]):
        host_name (Union[Unset, None, str]):
        forest_root (Union[Unset, None, str]):
        configuration_tenant (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    ca_type: Union[Unset, CSSCMSCoreEnumsCertificateAuthorityType] = UNSET
    explicit_credentials: Union[Unset, bool] = UNSET
    explicit_password: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    explicit_user: Union[Unset, None, str] = UNSET
    auth_certificate_password: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    auth_certificate: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    logical_name: Union[Unset, None, str] = UNSET
    host_name: Union[Unset, None, str] = UNSET
    forest_root: Union[Unset, None, str] = UNSET
    configuration_tenant: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        ca_type: Union[Unset, int] = UNSET
        if not isinstance(self.ca_type, Unset):
            ca_type = self.ca_type.value

        explicit_credentials = self.explicit_credentials
        explicit_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.explicit_password, Unset):
            explicit_password = self.explicit_password.to_dict()

        explicit_user = self.explicit_user
        auth_certificate_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_certificate_password, Unset):
            auth_certificate_password = self.auth_certificate_password.to_dict()

        auth_certificate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_certificate, Unset):
            auth_certificate = self.auth_certificate.to_dict()

        logical_name = self.logical_name
        host_name = self.host_name
        forest_root = self.forest_root
        configuration_tenant = self.configuration_tenant

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ca_type is not UNSET:
            field_dict["caType"] = ca_type
        if explicit_credentials is not UNSET:
            field_dict["explicitCredentials"] = explicit_credentials
        if explicit_password is not UNSET:
            field_dict["explicitPassword"] = explicit_password
        if explicit_user is not UNSET:
            field_dict["explicitUser"] = explicit_user
        if auth_certificate_password is not UNSET:
            field_dict["authCertificatePassword"] = auth_certificate_password
        if auth_certificate is not UNSET:
            field_dict["authCertificate"] = auth_certificate
        if logical_name is not UNSET:
            field_dict["logicalName"] = logical_name
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if forest_root is not UNSET:
            field_dict["forestRoot"] = forest_root
        if configuration_tenant is not UNSET:
            field_dict["configurationTenant"] = configuration_tenant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        _ca_type = d.pop("caType", UNSET)
        ca_type: Union[Unset, CSSCMSCoreEnumsCertificateAuthorityType]
        if isinstance(_ca_type, Unset):
            ca_type = UNSET
        else:
            ca_type = CSSCMSCoreEnumsCertificateAuthorityType(_ca_type)

        explicit_credentials = d.pop("explicitCredentials", UNSET)

        _explicit_password = d.pop("explicitPassword", UNSET)
        explicit_password: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_explicit_password, Unset):
            explicit_password = UNSET
        else:
            explicit_password = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_explicit_password)

        explicit_user = d.pop("explicitUser", UNSET)

        _auth_certificate_password = d.pop("authCertificatePassword", UNSET)
        auth_certificate_password: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_auth_certificate_password, Unset):
            auth_certificate_password = UNSET
        else:
            auth_certificate_password = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_auth_certificate_password)

        _auth_certificate = d.pop("authCertificate", UNSET)
        auth_certificate: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_auth_certificate, Unset):
            auth_certificate = UNSET
        else:
            auth_certificate = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_auth_certificate)

        logical_name = d.pop("logicalName", UNSET)

        host_name = d.pop("hostName", UNSET)

        forest_root = d.pop("forestRoot", UNSET)

        configuration_tenant = d.pop("configurationTenant", UNSET)

        csscms_data_model_models_certificate_authorities_certificate_authority_test_request = cls(
            id=id,
            ca_type=ca_type,
            explicit_credentials=explicit_credentials,
            explicit_password=explicit_password,
            explicit_user=explicit_user,
            auth_certificate_password=auth_certificate_password,
            auth_certificate=auth_certificate,
            logical_name=logical_name,
            host_name=host_name,
            forest_root=forest_root,
            configuration_tenant=configuration_tenant,
        )

        return csscms_data_model_models_certificate_authorities_certificate_authority_test_request
