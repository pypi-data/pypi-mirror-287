from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_templates_global_global_template_default_request import (
        KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateDefaultRequest,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_global_global_template_policy_request import (
        KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplatePolicyRequest,
    )
    from ..models.keyfactor_web_keyfactor_api_models_templates_global_global_template_regex_request import (
        KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateRegexRequest,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateSettingsRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateSettingsRequest:
    """
    Attributes:
        template_regexes (List['KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateRegexRequest']): The regular
            expressions to use for validation during enrollment.
        template_defaults (List['KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateDefaultRequest']): The
            default values to use during enrollment.
        template_policy (KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplatePolicyRequest):
    """

    template_regexes: List["KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateRegexRequest"]
    template_defaults: List["KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateDefaultRequest"]
    template_policy: "KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplatePolicyRequest"

    def to_dict(self) -> Dict[str, Any]:
        template_regexes = []
        for template_regexes_item_data in self.template_regexes:
            template_regexes_item = template_regexes_item_data.to_dict()

            template_regexes.append(template_regexes_item)

        template_defaults = []
        for template_defaults_item_data in self.template_defaults:
            template_defaults_item = template_defaults_item_data.to_dict()

            template_defaults.append(template_defaults_item)

        template_policy = self.template_policy.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "templateRegexes": template_regexes,
                "templateDefaults": template_defaults,
                "templatePolicy": template_policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_templates_global_global_template_default_request import (
            KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateDefaultRequest,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_global_global_template_policy_request import (
            KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplatePolicyRequest,
        )
        from ..models.keyfactor_web_keyfactor_api_models_templates_global_global_template_regex_request import (
            KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateRegexRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        template_regexes = []
        _template_regexes = d.pop("templateRegexes")
        for template_regexes_item_data in _template_regexes:
            template_regexes_item = KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateRegexRequest.from_dict(
                template_regexes_item_data
            )

            template_regexes.append(template_regexes_item)

        template_defaults = []
        _template_defaults = d.pop("templateDefaults")
        for template_defaults_item_data in _template_defaults:
            template_defaults_item = (
                KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplateDefaultRequest.from_dict(
                    template_defaults_item_data
                )
            )

            template_defaults.append(template_defaults_item)

        template_policy = KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplatePolicyRequest.from_dict(
            d.pop("templatePolicy")
        )

        keyfactor_web_keyfactor_api_models_templates_global_global_template_settings_request = cls(
            template_regexes=template_regexes,
            template_defaults=template_defaults,
            template_policy=template_policy,
        )

        return keyfactor_web_keyfactor_api_models_templates_global_global_template_settings_request
