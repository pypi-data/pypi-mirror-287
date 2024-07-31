from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateRetrievalResponseCRLDistributionPointModel")


@_attrs_define
class CSSCMSDataModelModelsCertificateRetrievalResponseCRLDistributionPointModel:
    """
    Attributes:
        id (Union[Unset, int]):
        url (Union[Unset, None, str]):
        url_hash (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    url: Union[Unset, None, str] = UNSET
    url_hash: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        url_hash = self.url_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if url_hash is not UNSET:
            field_dict["urlHash"] = url_hash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        url_hash = d.pop("urlHash", UNSET)

        csscms_data_model_models_certificate_retrieval_response_crl_distribution_point_model = cls(
            id=id,
            url=url,
            url_hash=url_hash,
        )

        return csscms_data_model_models_certificate_retrieval_response_crl_distribution_point_model
