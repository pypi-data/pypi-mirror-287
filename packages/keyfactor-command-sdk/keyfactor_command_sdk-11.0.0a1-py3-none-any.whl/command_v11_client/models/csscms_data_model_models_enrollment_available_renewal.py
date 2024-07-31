from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_renewal_type import CSSCMSDataModelEnumsRenewalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentAvailableRenewal")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentAvailableRenewal:
    """
    Attributes:
        available_renewal_type (Union[Unset, CSSCMSDataModelEnumsRenewalType]):
        message (Union[Unset, None, str]):
    """

    available_renewal_type: Union[Unset, CSSCMSDataModelEnumsRenewalType] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        available_renewal_type: Union[Unset, int] = UNSET
        if not isinstance(self.available_renewal_type, Unset):
            available_renewal_type = self.available_renewal_type.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if available_renewal_type is not UNSET:
            field_dict["availableRenewalType"] = available_renewal_type
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _available_renewal_type = d.pop("availableRenewalType", UNSET)
        available_renewal_type: Union[Unset, CSSCMSDataModelEnumsRenewalType]
        if isinstance(_available_renewal_type, Unset):
            available_renewal_type = UNSET
        else:
            available_renewal_type = CSSCMSDataModelEnumsRenewalType(_available_renewal_type)

        message = d.pop("message", UNSET)

        csscms_data_model_models_enrollment_available_renewal = cls(
            available_renewal_type=available_renewal_type,
            message=message,
        )

        return csscms_data_model_models_enrollment_available_renewal
