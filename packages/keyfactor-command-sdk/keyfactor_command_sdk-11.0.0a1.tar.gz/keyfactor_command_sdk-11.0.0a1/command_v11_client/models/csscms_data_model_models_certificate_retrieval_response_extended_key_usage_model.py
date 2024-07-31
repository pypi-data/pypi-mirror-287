from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateRetrievalResponseExtendedKeyUsageModel")


@_attrs_define
class CSSCMSDataModelModelsCertificateRetrievalResponseExtendedKeyUsageModel:
    """
    Attributes:
        id (Union[Unset, int]):
        oid (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    oid: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        oid = self.oid
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if oid is not UNSET:
            field_dict["oid"] = oid
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        oid = d.pop("oid", UNSET)

        display_name = d.pop("displayName", UNSET)

        csscms_data_model_models_certificate_retrieval_response_extended_key_usage_model = cls(
            id=id,
            oid=oid,
            display_name=display_name,
        )

        return csscms_data_model_models_certificate_retrieval_response_extended_key_usage_model
