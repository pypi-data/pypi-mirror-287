from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.csscms_core_enums_enrollment_type import CSSCMSCoreEnumsEnrollmentType
from ..models.csscms_core_enums_key_retention_policy import CSSCMSCoreEnumsKeyRetentionPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_templates_extended_key_usage_response_model import (
        KeyfactorWebKeyfactorApiModelsTemplatesExtendedKeyUsageResponseModel,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_key_algorithms_response_model import (
        KeyfactorWebKeyfactorApiModelsTemplatesKeyAlgorithmsResponseModel,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_template_default_request_response_model import (
        KeyfactorWebKeyfactorApiModelsTemplatesTemplateDefaultRequestResponseModel,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_template_enrollment_field_request_response_model import (
        KeyfactorWebKeyfactorApiModelsTemplatesTemplateEnrollmentFieldRequestResponseModel,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_template_metadata_field_request_response_model import (
        KeyfactorWebKeyfactorApiModelsTemplatesTemplateMetadataFieldRequestResponseModel,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_template_policy_request_response_model import (
        KeyfactorWebKeyfactorApiModelsTemplatesTemplatePolicyRequestResponseModel,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_template_regex_request_response_model import (
        KeyfactorWebKeyfactorApiModelsTemplatesTemplateRegexRequestResponseModel,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesTemplateRetrievalResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesTemplateRetrievalResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        common_name (Union[Unset, None, str]):
        template_name (Union[Unset, None, str]):
        oid (Union[Unset, None, str]):
        key_size (Union[Unset, None, str]):
        key_type (Union[Unset, None, str]):
        forest_root (Union[Unset, None, str]):
        configuration_tenant (Union[Unset, None, str]):
        friendly_name (Union[Unset, None, str]):
        key_retention (Union[Unset, CSSCMSCoreEnumsKeyRetentionPolicy]):
        key_retention_days (Union[Unset, None, int]):
        key_archival (Union[Unset, bool]):
        enrollment_fields (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsTemplatesTemplateEnrollmentFieldRequestResponseModel']]):
        metadata_fields (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsTemplatesTemplateMetadataFieldRequestResponseModel']]):
        allowed_enrollment_types (Union[Unset, CSSCMSCoreEnumsEnrollmentType]):
        template_regexes (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsTemplatesTemplateRegexRequestResponseModel']]):
        template_defaults (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsTemplatesTemplateDefaultRequestResponseModel']]):
        template_policy (Union[Unset, KeyfactorWebKeyfactorApiModelsTemplatesTemplatePolicyRequestResponseModel]):
        key_algorithms (Union[Unset, KeyfactorWebKeyfactorApiModelsTemplatesKeyAlgorithmsResponseModel]):
        use_allowed_requesters (Union[Unset, bool]):
        allowed_requesters (Union[Unset, None, List[str]]):
        display_name (Union[Unset, None, str]):
        rfc_enforcement (Union[Unset, bool]):
        requires_approval (Union[Unset, bool]):
        key_usage (Union[Unset, int]):
        extended_key_usages (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsTemplatesExtendedKeyUsageResponseModel']]):
        curve (Union[Unset, None, str]):
        allow_one_click_renewals (Union[Unset, bool]):
        key_types (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    common_name: Union[Unset, None, str] = UNSET
    template_name: Union[Unset, None, str] = UNSET
    oid: Union[Unset, None, str] = UNSET
    key_size: Union[Unset, None, str] = UNSET
    key_type: Union[Unset, None, str] = UNSET
    forest_root: Union[Unset, None, str] = UNSET
    configuration_tenant: Union[Unset, None, str] = UNSET
    friendly_name: Union[Unset, None, str] = UNSET
    key_retention: Union[Unset, CSSCMSCoreEnumsKeyRetentionPolicy] = UNSET
    key_retention_days: Union[Unset, None, int] = UNSET
    key_archival: Union[Unset, bool] = UNSET
    enrollment_fields: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsTemplatesTemplateEnrollmentFieldRequestResponseModel"]
    ] = UNSET
    metadata_fields: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsTemplatesTemplateMetadataFieldRequestResponseModel"]
    ] = UNSET
    allowed_enrollment_types: Union[Unset, CSSCMSCoreEnumsEnrollmentType] = UNSET
    template_regexes: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsTemplatesTemplateRegexRequestResponseModel"]
    ] = UNSET
    template_defaults: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsTemplatesTemplateDefaultRequestResponseModel"]
    ] = UNSET
    template_policy: Union[Unset, "KeyfactorWebKeyfactorApiModelsTemplatesTemplatePolicyRequestResponseModel"] = UNSET
    key_algorithms: Union[Unset, "KeyfactorWebKeyfactorApiModelsTemplatesKeyAlgorithmsResponseModel"] = UNSET
    use_allowed_requesters: Union[Unset, bool] = UNSET
    allowed_requesters: Union[Unset, None, List[str]] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET
    requires_approval: Union[Unset, bool] = UNSET
    key_usage: Union[Unset, int] = UNSET
    extended_key_usages: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsTemplatesExtendedKeyUsageResponseModel"]
    ] = UNSET
    curve: Union[Unset, None, str] = UNSET
    allow_one_click_renewals: Union[Unset, bool] = UNSET
    key_types: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        common_name = self.common_name
        template_name = self.template_name
        oid = self.oid
        key_size = self.key_size
        key_type = self.key_type
        forest_root = self.forest_root
        configuration_tenant = self.configuration_tenant
        friendly_name = self.friendly_name
        key_retention: Union[Unset, int] = UNSET
        if not isinstance(self.key_retention, Unset):
            key_retention = self.key_retention.value

        key_retention_days = self.key_retention_days
        key_archival = self.key_archival
        enrollment_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.enrollment_fields, Unset):
            if self.enrollment_fields is None:
                enrollment_fields = None
            else:
                enrollment_fields = []
                for enrollment_fields_item_data in self.enrollment_fields:
                    enrollment_fields_item = enrollment_fields_item_data.to_dict()

                    enrollment_fields.append(enrollment_fields_item)

        metadata_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_fields, Unset):
            if self.metadata_fields is None:
                metadata_fields = None
            else:
                metadata_fields = []
                for metadata_fields_item_data in self.metadata_fields:
                    metadata_fields_item = metadata_fields_item_data.to_dict()

                    metadata_fields.append(metadata_fields_item)

        allowed_enrollment_types: Union[Unset, int] = UNSET
        if not isinstance(self.allowed_enrollment_types, Unset):
            allowed_enrollment_types = self.allowed_enrollment_types.value

        template_regexes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.template_regexes, Unset):
            if self.template_regexes is None:
                template_regexes = None
            else:
                template_regexes = []
                for template_regexes_item_data in self.template_regexes:
                    template_regexes_item = template_regexes_item_data.to_dict()

                    template_regexes.append(template_regexes_item)

        template_defaults: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.template_defaults, Unset):
            if self.template_defaults is None:
                template_defaults = None
            else:
                template_defaults = []
                for template_defaults_item_data in self.template_defaults:
                    template_defaults_item = template_defaults_item_data.to_dict()

                    template_defaults.append(template_defaults_item)

        template_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template_policy, Unset):
            template_policy = self.template_policy.to_dict()

        key_algorithms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_algorithms, Unset):
            key_algorithms = self.key_algorithms.to_dict()

        use_allowed_requesters = self.use_allowed_requesters
        allowed_requesters: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.allowed_requesters, Unset):
            if self.allowed_requesters is None:
                allowed_requesters = None
            else:
                allowed_requesters = self.allowed_requesters

        display_name = self.display_name
        rfc_enforcement = self.rfc_enforcement
        requires_approval = self.requires_approval
        key_usage = self.key_usage
        extended_key_usages: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extended_key_usages, Unset):
            if self.extended_key_usages is None:
                extended_key_usages = None
            else:
                extended_key_usages = []
                for extended_key_usages_item_data in self.extended_key_usages:
                    extended_key_usages_item = extended_key_usages_item_data.to_dict()

                    extended_key_usages.append(extended_key_usages_item)

        curve = self.curve
        allow_one_click_renewals = self.allow_one_click_renewals
        key_types = self.key_types

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if common_name is not UNSET:
            field_dict["commonName"] = common_name
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if oid is not UNSET:
            field_dict["oid"] = oid
        if key_size is not UNSET:
            field_dict["keySize"] = key_size
        if key_type is not UNSET:
            field_dict["keyType"] = key_type
        if forest_root is not UNSET:
            field_dict["forestRoot"] = forest_root
        if configuration_tenant is not UNSET:
            field_dict["configurationTenant"] = configuration_tenant
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if key_retention is not UNSET:
            field_dict["keyRetention"] = key_retention
        if key_retention_days is not UNSET:
            field_dict["keyRetentionDays"] = key_retention_days
        if key_archival is not UNSET:
            field_dict["keyArchival"] = key_archival
        if enrollment_fields is not UNSET:
            field_dict["enrollmentFields"] = enrollment_fields
        if metadata_fields is not UNSET:
            field_dict["metadataFields"] = metadata_fields
        if allowed_enrollment_types is not UNSET:
            field_dict["allowedEnrollmentTypes"] = allowed_enrollment_types
        if template_regexes is not UNSET:
            field_dict["templateRegexes"] = template_regexes
        if template_defaults is not UNSET:
            field_dict["templateDefaults"] = template_defaults
        if template_policy is not UNSET:
            field_dict["templatePolicy"] = template_policy
        if key_algorithms is not UNSET:
            field_dict["keyAlgorithms"] = key_algorithms
        if use_allowed_requesters is not UNSET:
            field_dict["useAllowedRequesters"] = use_allowed_requesters
        if allowed_requesters is not UNSET:
            field_dict["allowedRequesters"] = allowed_requesters
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if rfc_enforcement is not UNSET:
            field_dict["rfcEnforcement"] = rfc_enforcement
        if requires_approval is not UNSET:
            field_dict["requiresApproval"] = requires_approval
        if key_usage is not UNSET:
            field_dict["keyUsage"] = key_usage
        if extended_key_usages is not UNSET:
            field_dict["extendedKeyUsages"] = extended_key_usages
        if curve is not UNSET:
            field_dict["curve"] = curve
        if allow_one_click_renewals is not UNSET:
            field_dict["allowOneClickRenewals"] = allow_one_click_renewals
        if key_types is not UNSET:
            field_dict["keyTypes"] = key_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_templates_extended_key_usage_response_model import (
            KeyfactorWebKeyfactorApiModelsTemplatesExtendedKeyUsageResponseModel,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_key_algorithms_response_model import (
            KeyfactorWebKeyfactorApiModelsTemplatesKeyAlgorithmsResponseModel,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_template_default_request_response_model import (
            KeyfactorWebKeyfactorApiModelsTemplatesTemplateDefaultRequestResponseModel,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_template_enrollment_field_request_response_model import (
            KeyfactorWebKeyfactorApiModelsTemplatesTemplateEnrollmentFieldRequestResponseModel,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_template_metadata_field_request_response_model import (
            KeyfactorWebKeyfactorApiModelsTemplatesTemplateMetadataFieldRequestResponseModel,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_template_policy_request_response_model import (
            KeyfactorWebKeyfactorApiModelsTemplatesTemplatePolicyRequestResponseModel,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_template_regex_request_response_model import (
            KeyfactorWebKeyfactorApiModelsTemplatesTemplateRegexRequestResponseModel,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        common_name = d.pop("commonName", UNSET)

        template_name = d.pop("templateName", UNSET)

        oid = d.pop("oid", UNSET)

        key_size = d.pop("keySize", UNSET)

        key_type = d.pop("keyType", UNSET)

        forest_root = d.pop("forestRoot", UNSET)

        configuration_tenant = d.pop("configurationTenant", UNSET)

        friendly_name = d.pop("friendlyName", UNSET)

        _key_retention = d.pop("keyRetention", UNSET)
        key_retention: Union[Unset, CSSCMSCoreEnumsKeyRetentionPolicy]
        if isinstance(_key_retention, Unset):
            key_retention = UNSET
        else:
            key_retention = CSSCMSCoreEnumsKeyRetentionPolicy(_key_retention)

        key_retention_days = d.pop("keyRetentionDays", UNSET)

        key_archival = d.pop("keyArchival", UNSET)

        enrollment_fields = []
        _enrollment_fields = d.pop("enrollmentFields", UNSET)
        for enrollment_fields_item_data in _enrollment_fields or []:
            enrollment_fields_item = (
                KeyfactorWebKeyfactorApiModelsTemplatesTemplateEnrollmentFieldRequestResponseModel.from_dict(
                    enrollment_fields_item_data
                )
            )

            enrollment_fields.append(enrollment_fields_item)

        metadata_fields = []
        _metadata_fields = d.pop("metadataFields", UNSET)
        for metadata_fields_item_data in _metadata_fields or []:
            metadata_fields_item = (
                KeyfactorWebKeyfactorApiModelsTemplatesTemplateMetadataFieldRequestResponseModel.from_dict(
                    metadata_fields_item_data
                )
            )

            metadata_fields.append(metadata_fields_item)

        _allowed_enrollment_types = d.pop("allowedEnrollmentTypes", UNSET)
        allowed_enrollment_types: Union[Unset, CSSCMSCoreEnumsEnrollmentType]
        if isinstance(_allowed_enrollment_types, Unset):
            allowed_enrollment_types = UNSET
        else:
            allowed_enrollment_types = CSSCMSCoreEnumsEnrollmentType(_allowed_enrollment_types)

        template_regexes = []
        _template_regexes = d.pop("templateRegexes", UNSET)
        for template_regexes_item_data in _template_regexes or []:
            template_regexes_item = KeyfactorWebKeyfactorApiModelsTemplatesTemplateRegexRequestResponseModel.from_dict(
                template_regexes_item_data
            )

            template_regexes.append(template_regexes_item)

        template_defaults = []
        _template_defaults = d.pop("templateDefaults", UNSET)
        for template_defaults_item_data in _template_defaults or []:
            template_defaults_item = (
                KeyfactorWebKeyfactorApiModelsTemplatesTemplateDefaultRequestResponseModel.from_dict(
                    template_defaults_item_data
                )
            )

            template_defaults.append(template_defaults_item)

        _template_policy = d.pop("templatePolicy", UNSET)
        template_policy: Union[Unset, KeyfactorWebKeyfactorApiModelsTemplatesTemplatePolicyRequestResponseModel]
        if isinstance(_template_policy, Unset):
            template_policy = UNSET
        else:
            template_policy = KeyfactorWebKeyfactorApiModelsTemplatesTemplatePolicyRequestResponseModel.from_dict(
                _template_policy
            )

        _key_algorithms = d.pop("keyAlgorithms", UNSET)
        key_algorithms: Union[Unset, KeyfactorWebKeyfactorApiModelsTemplatesKeyAlgorithmsResponseModel]
        if isinstance(_key_algorithms, Unset):
            key_algorithms = UNSET
        else:
            key_algorithms = KeyfactorWebKeyfactorApiModelsTemplatesKeyAlgorithmsResponseModel.from_dict(
                _key_algorithms
            )

        use_allowed_requesters = d.pop("useAllowedRequesters", UNSET)

        allowed_requesters = cast(List[str], d.pop("allowedRequesters", UNSET))

        display_name = d.pop("displayName", UNSET)

        rfc_enforcement = d.pop("rfcEnforcement", UNSET)

        requires_approval = d.pop("requiresApproval", UNSET)

        key_usage = d.pop("keyUsage", UNSET)

        extended_key_usages = []
        _extended_key_usages = d.pop("extendedKeyUsages", UNSET)
        for extended_key_usages_item_data in _extended_key_usages or []:
            extended_key_usages_item = KeyfactorWebKeyfactorApiModelsTemplatesExtendedKeyUsageResponseModel.from_dict(
                extended_key_usages_item_data
            )

            extended_key_usages.append(extended_key_usages_item)

        curve = d.pop("curve", UNSET)

        allow_one_click_renewals = d.pop("allowOneClickRenewals", UNSET)

        key_types = d.pop("keyTypes", UNSET)

        keyfactor_web_keyfactor_api_models_templates_template_retrieval_response = cls(
            id=id,
            common_name=common_name,
            template_name=template_name,
            oid=oid,
            key_size=key_size,
            key_type=key_type,
            forest_root=forest_root,
            configuration_tenant=configuration_tenant,
            friendly_name=friendly_name,
            key_retention=key_retention,
            key_retention_days=key_retention_days,
            key_archival=key_archival,
            enrollment_fields=enrollment_fields,
            metadata_fields=metadata_fields,
            allowed_enrollment_types=allowed_enrollment_types,
            template_regexes=template_regexes,
            template_defaults=template_defaults,
            template_policy=template_policy,
            key_algorithms=key_algorithms,
            use_allowed_requesters=use_allowed_requesters,
            allowed_requesters=allowed_requesters,
            display_name=display_name,
            rfc_enforcement=rfc_enforcement,
            requires_approval=requires_approval,
            key_usage=key_usage,
            extended_key_usages=extended_key_usages,
            curve=curve,
            allow_one_click_renewals=allow_one_click_renewals,
            key_types=key_types,
        )

        return keyfactor_web_keyfactor_api_models_templates_template_retrieval_response
