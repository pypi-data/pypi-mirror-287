from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_templates_algorithms_key_info import (
        CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplatePolicyRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsTemplatesGlobalGlobalTemplatePolicyRequest:
    """
    Attributes:
        allow_key_reuse (bool): Whether or not keys can be reused.
        allow_wildcards (bool): Whether or not wildcards can be used.
        rfc_enforcement (bool): Whether or not RFC 2818 compliance should be enforced.
        key_info (CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo):
        id (Union[Unset, int]): The ID of the global template policy.
    """

    allow_key_reuse: bool
    allow_wildcards: bool
    rfc_enforcement: bool
    key_info: "CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo"
    id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        allow_key_reuse = self.allow_key_reuse
        allow_wildcards = self.allow_wildcards
        rfc_enforcement = self.rfc_enforcement
        key_info = self.key_info.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "allowKeyReuse": allow_key_reuse,
                "allowWildcards": allow_wildcards,
                "rfcEnforcement": rfc_enforcement,
                "keyInfo": key_info,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_templates_algorithms_key_info import (
            CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        allow_key_reuse = d.pop("allowKeyReuse")

        allow_wildcards = d.pop("allowWildcards")

        rfc_enforcement = d.pop("rfcEnforcement")

        key_info = CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo.from_dict(d.pop("keyInfo"))

        id = d.pop("id", UNSET)

        keyfactor_web_keyfactor_api_models_templates_global_global_template_policy_request = cls(
            allow_key_reuse=allow_key_reuse,
            allow_wildcards=allow_wildcards,
            rfc_enforcement=rfc_enforcement,
            key_info=key_info,
            id=id,
        )

        return keyfactor_web_keyfactor_api_models_templates_global_global_template_policy_request
