from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_validation_response_results import (
        CSSCMSDataModelModelsCertificateValidationResponseResults,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateValidationResponse")


@_attrs_define
class CSSCMSDataModelModelsCertificateValidationResponse:
    """
    Attributes:
        valid (Union[Unset, bool]):
        results (Union[Unset, None, CSSCMSDataModelModelsCertificateValidationResponseResults]):
    """

    valid: Union[Unset, bool] = UNSET
    results: Union[Unset, None, "CSSCMSDataModelModelsCertificateValidationResponseResults"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        valid = self.valid
        results: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict() if self.results else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if valid is not UNSET:
            field_dict["valid"] = valid
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_validation_response_results import (
            CSSCMSDataModelModelsCertificateValidationResponseResults,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        valid = d.pop("valid", UNSET)

        _results = d.pop("results", UNSET)
        results: Union[Unset, None, CSSCMSDataModelModelsCertificateValidationResponseResults]
        if _results is None:
            results = None
        elif isinstance(_results, Unset):
            results = UNSET
        else:
            results = CSSCMSDataModelModelsCertificateValidationResponseResults.from_dict(_results)

        csscms_data_model_models_certificate_validation_response = cls(
            valid=valid,
            results=results,
        )

        return csscms_data_model_models_certificate_validation_response
