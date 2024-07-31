from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebCoreModelsEnrollmentEnrollmentCA")


@_attrs_define
class KeyfactorWebCoreModelsEnrollmentEnrollmentCA:
    """
    Attributes:
        name (Union[Unset, None, str]):
        rfc_enforcement (Union[Unset, bool]):
        subscriber_terms (Union[Unset, bool]):
    """

    name: Union[Unset, None, str] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET
    subscriber_terms: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        rfc_enforcement = self.rfc_enforcement
        subscriber_terms = self.subscriber_terms

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if rfc_enforcement is not UNSET:
            field_dict["rfcEnforcement"] = rfc_enforcement
        if subscriber_terms is not UNSET:
            field_dict["subscriberTerms"] = subscriber_terms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name", UNSET)

        rfc_enforcement = d.pop("rfcEnforcement", UNSET)

        subscriber_terms = d.pop("subscriberTerms", UNSET)

        keyfactor_web_core_models_enrollment_enrollment_ca = cls(
            name=name,
            rfc_enforcement=rfc_enforcement,
            subscriber_terms=subscriber_terms,
        )

        return keyfactor_web_core_models_enrollment_enrollment_ca
