from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.csscms_core_enums_certificate_authority_type import CSSCMSCoreEnumsCertificateAuthorityType
from ..models.csscms_core_enums_enrollment_type import CSSCMSCoreEnumsEnrollmentType
from ..models.csscms_core_enums_key_retention_policy import CSSCMSCoreEnumsKeyRetentionPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCertificateAuthorityRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateAuthoritiesCertificateAuthorityRequest:
    """
    Attributes:
        id (Union[Unset, int]):
        logical_name (Union[Unset, None, str]):
        host_name (Union[Unset, None, str]):
        delegate (Union[Unset, bool]):
        delegate_enrollment (Union[Unset, bool]):
        forest_root (Union[Unset, None, str]):
        configuration_tenant (Union[Unset, None, str]):
        remote (Union[Unset, bool]):
        agent (Union[Unset, None, str]):
        standalone (Union[Unset, bool]):
        monitor_thresholds (Union[Unset, bool]):
        issuance_max (Union[Unset, None, int]):
        issuance_min (Union[Unset, None, int]):
        failure_max (Union[Unset, None, int]):
        rfc_enforcement (Union[Unset, bool]):
        properties (Union[Unset, None, str]):
        allowed_enrollment_types (Union[Unset, CSSCMSCoreEnumsEnrollmentType]):
        key_retention (Union[Unset, CSSCMSCoreEnumsKeyRetentionPolicy]):
        key_retention_days (Union[Unset, None, int]):
        explicit_credentials (Union[Unset, bool]):
        subscriber_terms (Union[Unset, bool]):
        explicit_user (Union[Unset, None, str]):
        explicit_password (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        use_allowed_requesters (Union[Unset, bool]):
        allowed_requesters (Union[Unset, None, List[str]]):
        full_scan (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        incremental_scan (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        threshold_check (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        auth_certificate_password (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        auth_certificate (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        ca_type (Union[Unset, CSSCMSCoreEnumsCertificateAuthorityType]):
        enforce_unique_dn (Union[Unset, bool]):
        allow_one_click_renewals (Union[Unset, bool]):
        new_end_entity_on_renew_and_reissue (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    logical_name: Union[Unset, None, str] = UNSET
    host_name: Union[Unset, None, str] = UNSET
    delegate: Union[Unset, bool] = UNSET
    delegate_enrollment: Union[Unset, bool] = UNSET
    forest_root: Union[Unset, None, str] = UNSET
    configuration_tenant: Union[Unset, None, str] = UNSET
    remote: Union[Unset, bool] = UNSET
    agent: Union[Unset, None, str] = UNSET
    standalone: Union[Unset, bool] = UNSET
    monitor_thresholds: Union[Unset, bool] = UNSET
    issuance_max: Union[Unset, None, int] = UNSET
    issuance_min: Union[Unset, None, int] = UNSET
    failure_max: Union[Unset, None, int] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET
    properties: Union[Unset, None, str] = UNSET
    allowed_enrollment_types: Union[Unset, CSSCMSCoreEnumsEnrollmentType] = UNSET
    key_retention: Union[Unset, CSSCMSCoreEnumsKeyRetentionPolicy] = UNSET
    key_retention_days: Union[Unset, None, int] = UNSET
    explicit_credentials: Union[Unset, bool] = UNSET
    subscriber_terms: Union[Unset, bool] = UNSET
    explicit_user: Union[Unset, None, str] = UNSET
    explicit_password: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    use_allowed_requesters: Union[Unset, bool] = UNSET
    allowed_requesters: Union[Unset, None, List[str]] = UNSET
    full_scan: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    incremental_scan: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    threshold_check: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    auth_certificate_password: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    auth_certificate: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    ca_type: Union[Unset, CSSCMSCoreEnumsCertificateAuthorityType] = UNSET
    enforce_unique_dn: Union[Unset, bool] = UNSET
    allow_one_click_renewals: Union[Unset, bool] = UNSET
    new_end_entity_on_renew_and_reissue: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        logical_name = self.logical_name
        host_name = self.host_name
        delegate = self.delegate
        delegate_enrollment = self.delegate_enrollment
        forest_root = self.forest_root
        configuration_tenant = self.configuration_tenant
        remote = self.remote
        agent = self.agent
        standalone = self.standalone
        monitor_thresholds = self.monitor_thresholds
        issuance_max = self.issuance_max
        issuance_min = self.issuance_min
        failure_max = self.failure_max
        rfc_enforcement = self.rfc_enforcement
        properties = self.properties
        allowed_enrollment_types: Union[Unset, int] = UNSET
        if not isinstance(self.allowed_enrollment_types, Unset):
            allowed_enrollment_types = self.allowed_enrollment_types.value

        key_retention: Union[Unset, int] = UNSET
        if not isinstance(self.key_retention, Unset):
            key_retention = self.key_retention.value

        key_retention_days = self.key_retention_days
        explicit_credentials = self.explicit_credentials
        subscriber_terms = self.subscriber_terms
        explicit_user = self.explicit_user
        explicit_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.explicit_password, Unset):
            explicit_password = self.explicit_password.to_dict()

        use_allowed_requesters = self.use_allowed_requesters
        allowed_requesters: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.allowed_requesters, Unset):
            if self.allowed_requesters is None:
                allowed_requesters = None
            else:
                allowed_requesters = self.allowed_requesters

        full_scan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full_scan, Unset):
            full_scan = self.full_scan.to_dict()

        incremental_scan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.incremental_scan, Unset):
            incremental_scan = self.incremental_scan.to_dict()

        threshold_check: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.threshold_check, Unset):
            threshold_check = self.threshold_check.to_dict()

        auth_certificate_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_certificate_password, Unset):
            auth_certificate_password = self.auth_certificate_password.to_dict()

        auth_certificate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auth_certificate, Unset):
            auth_certificate = self.auth_certificate.to_dict()

        ca_type: Union[Unset, int] = UNSET
        if not isinstance(self.ca_type, Unset):
            ca_type = self.ca_type.value

        enforce_unique_dn = self.enforce_unique_dn
        allow_one_click_renewals = self.allow_one_click_renewals
        new_end_entity_on_renew_and_reissue = self.new_end_entity_on_renew_and_reissue

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if logical_name is not UNSET:
            field_dict["logicalName"] = logical_name
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if delegate is not UNSET:
            field_dict["delegate"] = delegate
        if delegate_enrollment is not UNSET:
            field_dict["delegateEnrollment"] = delegate_enrollment
        if forest_root is not UNSET:
            field_dict["forestRoot"] = forest_root
        if configuration_tenant is not UNSET:
            field_dict["configurationTenant"] = configuration_tenant
        if remote is not UNSET:
            field_dict["remote"] = remote
        if agent is not UNSET:
            field_dict["agent"] = agent
        if standalone is not UNSET:
            field_dict["standalone"] = standalone
        if monitor_thresholds is not UNSET:
            field_dict["monitorThresholds"] = monitor_thresholds
        if issuance_max is not UNSET:
            field_dict["issuanceMax"] = issuance_max
        if issuance_min is not UNSET:
            field_dict["issuanceMin"] = issuance_min
        if failure_max is not UNSET:
            field_dict["failureMax"] = failure_max
        if rfc_enforcement is not UNSET:
            field_dict["rfcEnforcement"] = rfc_enforcement
        if properties is not UNSET:
            field_dict["properties"] = properties
        if allowed_enrollment_types is not UNSET:
            field_dict["allowedEnrollmentTypes"] = allowed_enrollment_types
        if key_retention is not UNSET:
            field_dict["keyRetention"] = key_retention
        if key_retention_days is not UNSET:
            field_dict["keyRetentionDays"] = key_retention_days
        if explicit_credentials is not UNSET:
            field_dict["explicitCredentials"] = explicit_credentials
        if subscriber_terms is not UNSET:
            field_dict["subscriberTerms"] = subscriber_terms
        if explicit_user is not UNSET:
            field_dict["explicitUser"] = explicit_user
        if explicit_password is not UNSET:
            field_dict["explicitPassword"] = explicit_password
        if use_allowed_requesters is not UNSET:
            field_dict["useAllowedRequesters"] = use_allowed_requesters
        if allowed_requesters is not UNSET:
            field_dict["allowedRequesters"] = allowed_requesters
        if full_scan is not UNSET:
            field_dict["fullScan"] = full_scan
        if incremental_scan is not UNSET:
            field_dict["incrementalScan"] = incremental_scan
        if threshold_check is not UNSET:
            field_dict["thresholdCheck"] = threshold_check
        if auth_certificate_password is not UNSET:
            field_dict["authCertificatePassword"] = auth_certificate_password
        if auth_certificate is not UNSET:
            field_dict["authCertificate"] = auth_certificate
        if ca_type is not UNSET:
            field_dict["caType"] = ca_type
        if enforce_unique_dn is not UNSET:
            field_dict["enforceUniqueDN"] = enforce_unique_dn
        if allow_one_click_renewals is not UNSET:
            field_dict["allowOneClickRenewals"] = allow_one_click_renewals
        if new_end_entity_on_renew_and_reissue is not UNSET:
            field_dict["newEndEntityOnRenewAndReissue"] = new_end_entity_on_renew_and_reissue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        logical_name = d.pop("logicalName", UNSET)

        host_name = d.pop("hostName", UNSET)

        delegate = d.pop("delegate", UNSET)

        delegate_enrollment = d.pop("delegateEnrollment", UNSET)

        forest_root = d.pop("forestRoot", UNSET)

        configuration_tenant = d.pop("configurationTenant", UNSET)

        remote = d.pop("remote", UNSET)

        agent = d.pop("agent", UNSET)

        standalone = d.pop("standalone", UNSET)

        monitor_thresholds = d.pop("monitorThresholds", UNSET)

        issuance_max = d.pop("issuanceMax", UNSET)

        issuance_min = d.pop("issuanceMin", UNSET)

        failure_max = d.pop("failureMax", UNSET)

        rfc_enforcement = d.pop("rfcEnforcement", UNSET)

        properties = d.pop("properties", UNSET)

        _allowed_enrollment_types = d.pop("allowedEnrollmentTypes", UNSET)
        allowed_enrollment_types: Union[Unset, CSSCMSCoreEnumsEnrollmentType]
        if isinstance(_allowed_enrollment_types, Unset):
            allowed_enrollment_types = UNSET
        else:
            allowed_enrollment_types = CSSCMSCoreEnumsEnrollmentType(_allowed_enrollment_types)

        _key_retention = d.pop("keyRetention", UNSET)
        key_retention: Union[Unset, CSSCMSCoreEnumsKeyRetentionPolicy]
        if isinstance(_key_retention, Unset):
            key_retention = UNSET
        else:
            key_retention = CSSCMSCoreEnumsKeyRetentionPolicy(_key_retention)

        key_retention_days = d.pop("keyRetentionDays", UNSET)

        explicit_credentials = d.pop("explicitCredentials", UNSET)

        subscriber_terms = d.pop("subscriberTerms", UNSET)

        explicit_user = d.pop("explicitUser", UNSET)

        _explicit_password = d.pop("explicitPassword", UNSET)
        explicit_password: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_explicit_password, Unset):
            explicit_password = UNSET
        else:
            explicit_password = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_explicit_password)

        use_allowed_requesters = d.pop("useAllowedRequesters", UNSET)

        allowed_requesters = cast(List[str], d.pop("allowedRequesters", UNSET))

        _full_scan = d.pop("fullScan", UNSET)
        full_scan: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_full_scan, Unset):
            full_scan = UNSET
        else:
            full_scan = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_full_scan)

        _incremental_scan = d.pop("incrementalScan", UNSET)
        incremental_scan: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_incremental_scan, Unset):
            incremental_scan = UNSET
        else:
            incremental_scan = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_incremental_scan)

        _threshold_check = d.pop("thresholdCheck", UNSET)
        threshold_check: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_threshold_check, Unset):
            threshold_check = UNSET
        else:
            threshold_check = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_threshold_check)

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

        _ca_type = d.pop("caType", UNSET)
        ca_type: Union[Unset, CSSCMSCoreEnumsCertificateAuthorityType]
        if isinstance(_ca_type, Unset):
            ca_type = UNSET
        else:
            ca_type = CSSCMSCoreEnumsCertificateAuthorityType(_ca_type)

        enforce_unique_dn = d.pop("enforceUniqueDN", UNSET)

        allow_one_click_renewals = d.pop("allowOneClickRenewals", UNSET)

        new_end_entity_on_renew_and_reissue = d.pop("newEndEntityOnRenewAndReissue", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_authorities_certificate_authority_request = cls(
            id=id,
            logical_name=logical_name,
            host_name=host_name,
            delegate=delegate,
            delegate_enrollment=delegate_enrollment,
            forest_root=forest_root,
            configuration_tenant=configuration_tenant,
            remote=remote,
            agent=agent,
            standalone=standalone,
            monitor_thresholds=monitor_thresholds,
            issuance_max=issuance_max,
            issuance_min=issuance_min,
            failure_max=failure_max,
            rfc_enforcement=rfc_enforcement,
            properties=properties,
            allowed_enrollment_types=allowed_enrollment_types,
            key_retention=key_retention,
            key_retention_days=key_retention_days,
            explicit_credentials=explicit_credentials,
            subscriber_terms=subscriber_terms,
            explicit_user=explicit_user,
            explicit_password=explicit_password,
            use_allowed_requesters=use_allowed_requesters,
            allowed_requesters=allowed_requesters,
            full_scan=full_scan,
            incremental_scan=incremental_scan,
            threshold_check=threshold_check,
            auth_certificate_password=auth_certificate_password,
            auth_certificate=auth_certificate,
            ca_type=ca_type,
            enforce_unique_dn=enforce_unique_dn,
            allow_one_click_renewals=allow_one_click_renewals,
            new_end_entity_on_renew_and_reissue=new_end_entity_on_renew_and_reissue,
        )

        return keyfactor_web_keyfactor_api_models_certificate_authorities_certificate_authority_request
