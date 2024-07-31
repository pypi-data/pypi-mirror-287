from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_templates_algorithms_key_info import (
        CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesTemplatePolicyRequestResponseModel")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesTemplatePolicyRequestResponseModel:
    """
    Attributes:
        template_id (Union[Unset, int]):
        allow_key_reuse (Union[Unset, None, bool]):
        allow_wildcards (Union[Unset, None, bool]):
        rfc_enforcement (Union[Unset, None, bool]):
        key_info (Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo]):
    """

    template_id: Union[Unset, int] = UNSET
    allow_key_reuse: Union[Unset, None, bool] = UNSET
    allow_wildcards: Union[Unset, None, bool] = UNSET
    rfc_enforcement: Union[Unset, None, bool] = UNSET
    key_info: Union[Unset, "CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        template_id = self.template_id
        allow_key_reuse = self.allow_key_reuse
        allow_wildcards = self.allow_wildcards
        rfc_enforcement = self.rfc_enforcement
        key_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if allow_key_reuse is not UNSET:
            field_dict["allowKeyReuse"] = allow_key_reuse
        if allow_wildcards is not UNSET:
            field_dict["allowWildcards"] = allow_wildcards
        if rfc_enforcement is not UNSET:
            field_dict["rfcEnforcement"] = rfc_enforcement
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_templates_algorithms_key_info import (
            CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        template_id = d.pop("templateId", UNSET)

        allow_key_reuse = d.pop("allowKeyReuse", UNSET)

        allow_wildcards = d.pop("allowWildcards", UNSET)

        rfc_enforcement = d.pop("rfcEnforcement", UNSET)

        _key_info = d.pop("keyInfo", UNSET)
        key_info: Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo]
        if isinstance(_key_info, Unset):
            key_info = UNSET
        else:
            key_info = CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo.from_dict(_key_info)

        keyfactor_web_keyfactor_api_models_templates_template_policy_request_response_model = cls(
            template_id=template_id,
            allow_key_reuse=allow_key_reuse,
            allow_wildcards=allow_wildcards,
            rfc_enforcement=rfc_enforcement,
            key_info=key_info,
        )

        return keyfactor_web_keyfactor_api_models_templates_template_policy_request_response_model
