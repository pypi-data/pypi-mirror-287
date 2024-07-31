from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_default_response import (
        KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentDefaultResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_policy_response import (
        KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentPolicyResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_regex_response import (
        KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentRegexResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse:
    """
    Attributes:
        template_regexes (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentRegexResponse']]): The regular
            expressions to use for validation during enrollment.
        template_defaults (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentDefaultResponse']]): The default values
            to use during enrollment.
        template_policy (Union[Unset,
            KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentPolicyResponse]):
    """

    template_regexes: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentRegexResponse"]
    ] = UNSET
    template_defaults: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentDefaultResponse"]
    ] = UNSET
    template_policy: Union[
        Unset, "KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentPolicyResponse"
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if template_regexes is not UNSET:
            field_dict["templateRegexes"] = template_regexes
        if template_defaults is not UNSET:
            field_dict["templateDefaults"] = template_defaults
        if template_policy is not UNSET:
            field_dict["templatePolicy"] = template_policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_default_response import (
            KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentDefaultResponse,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_policy_response import (
            KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentPolicyResponse,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_regex_response import (
            KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentRegexResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        template_regexes = []
        _template_regexes = d.pop("templateRegexes", UNSET)
        for template_regexes_item_data in _template_regexes or []:
            template_regexes_item = (
                KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentRegexResponse.from_dict(
                    template_regexes_item_data
                )
            )

            template_regexes.append(template_regexes_item)

        template_defaults = []
        _template_defaults = d.pop("templateDefaults", UNSET)
        for template_defaults_item_data in _template_defaults or []:
            template_defaults_item = (
                KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentDefaultResponse.from_dict(
                    template_defaults_item_data
                )
            )

            template_defaults.append(template_defaults_item)

        _template_policy = d.pop("templatePolicy", UNSET)
        template_policy: Union[Unset, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentPolicyResponse]
        if isinstance(_template_policy, Unset):
            template_policy = UNSET
        else:
            template_policy = (
                KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentPolicyResponse.from_dict(
                    _template_policy
                )
            )

        keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_settings_response = cls(
            template_regexes=template_regexes,
            template_defaults=template_defaults,
            template_policy=template_policy,
        )

        return keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_settings_response
