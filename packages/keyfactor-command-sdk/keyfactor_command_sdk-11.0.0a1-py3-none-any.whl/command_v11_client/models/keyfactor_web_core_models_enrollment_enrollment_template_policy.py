from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_templates_algorithms_key_info import (
        CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo,
    )


T = TypeVar("T", bound="KeyfactorWebCoreModelsEnrollmentEnrollmentTemplatePolicy")


@_attrs_define
class KeyfactorWebCoreModelsEnrollmentEnrollmentTemplatePolicy:
    """
    Attributes:
        key_info (Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo]):
        allow_key_reuse (Union[Unset, bool]):
        allow_wildcards (Union[Unset, bool]):
        rfc_enforcement (Union[Unset, bool]):
    """

    key_info: Union[Unset, "CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo"] = UNSET
    allow_key_reuse: Union[Unset, bool] = UNSET
    allow_wildcards: Union[Unset, bool] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        key_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        allow_key_reuse = self.allow_key_reuse
        allow_wildcards = self.allow_wildcards
        rfc_enforcement = self.rfc_enforcement

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info
        if allow_key_reuse is not UNSET:
            field_dict["allowKeyReuse"] = allow_key_reuse
        if allow_wildcards is not UNSET:
            field_dict["allowWildcards"] = allow_wildcards
        if rfc_enforcement is not UNSET:
            field_dict["rfcEnforcement"] = rfc_enforcement

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_templates_algorithms_key_info import (
            CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _key_info = d.pop("keyInfo", UNSET)
        key_info: Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo]
        if isinstance(_key_info, Unset):
            key_info = UNSET
        else:
            key_info = CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo.from_dict(_key_info)

        allow_key_reuse = d.pop("allowKeyReuse", UNSET)

        allow_wildcards = d.pop("allowWildcards", UNSET)

        rfc_enforcement = d.pop("rfcEnforcement", UNSET)

        keyfactor_web_core_models_enrollment_enrollment_template_policy = cls(
            key_info=key_info,
            allow_key_reuse=allow_key_reuse,
            allow_wildcards=allow_wildcards,
            rfc_enforcement=rfc_enforcement,
        )

        return keyfactor_web_core_models_enrollment_enrollment_template_policy
