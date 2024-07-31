from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_enrollment_csr_generation_request_sa_ns import (
        CSSCMSDataModelModelsEnrollmentCSRGenerationRequestSaNs,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentCSRGenerationRequest")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentCSRGenerationRequest:
    """
    Attributes:
        subject (str):
        key_type (str):
        template (Union[Unset, None, str]):
        sa_ns (Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSRGenerationRequestSaNs]):
        key_length (Union[Unset, int]):
        curve (Union[Unset, None, str]):
    """

    subject: str
    key_type: str
    template: Union[Unset, None, str] = UNSET
    sa_ns: Union[Unset, None, "CSSCMSDataModelModelsEnrollmentCSRGenerationRequestSaNs"] = UNSET
    key_length: Union[Unset, int] = UNSET
    curve: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        key_type = self.key_type
        template = self.template
        sa_ns: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sa_ns, Unset):
            sa_ns = self.sa_ns.to_dict() if self.sa_ns else None

        key_length = self.key_length
        curve = self.curve

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "subject": subject,
                "keyType": key_type,
            }
        )
        if template is not UNSET:
            field_dict["template"] = template
        if sa_ns is not UNSET:
            field_dict["saNs"] = sa_ns
        if key_length is not UNSET:
            field_dict["keyLength"] = key_length
        if curve is not UNSET:
            field_dict["curve"] = curve

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_enrollment_csr_generation_request_sa_ns import (
            CSSCMSDataModelModelsEnrollmentCSRGenerationRequestSaNs,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        subject = d.pop("subject")

        key_type = d.pop("keyType")

        template = d.pop("template", UNSET)

        _sa_ns = d.pop("saNs", UNSET)
        sa_ns: Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSRGenerationRequestSaNs]
        if _sa_ns is None:
            sa_ns = None
        elif isinstance(_sa_ns, Unset):
            sa_ns = UNSET
        else:
            sa_ns = CSSCMSDataModelModelsEnrollmentCSRGenerationRequestSaNs.from_dict(_sa_ns)

        key_length = d.pop("keyLength", UNSET)

        curve = d.pop("curve", UNSET)

        csscms_data_model_models_enrollment_csr_generation_request = cls(
            subject=subject,
            key_type=key_type,
            template=template,
            sa_ns=sa_ns,
            key_length=key_length,
            curve=curve,
        )

        return csscms_data_model_models_enrollment_csr_generation_request
