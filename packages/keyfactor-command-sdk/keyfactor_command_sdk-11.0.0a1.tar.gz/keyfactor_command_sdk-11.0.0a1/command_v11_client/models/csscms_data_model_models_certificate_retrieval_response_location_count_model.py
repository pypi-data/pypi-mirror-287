from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateRetrievalResponseLocationCountModel")


@_attrs_define
class CSSCMSDataModelModelsCertificateRetrievalResponseLocationCountModel:
    """
    Attributes:
        type (Union[Unset, None, str]):
        count (Union[Unset, int]):
    """

    type: Union[Unset, None, str] = UNSET
    count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        type = d.pop("type", UNSET)

        count = d.pop("count", UNSET)

        csscms_data_model_models_certificate_retrieval_response_location_count_model = cls(
            type=type,
            count=count,
        )

        return csscms_data_model_models_certificate_retrieval_response_location_count_model
