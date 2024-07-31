from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateDownloadResponse")


@_attrs_define
class CSSCMSDataModelModelsCertificateDownloadResponse:
    """
    Attributes:
        content (Union[Unset, None, str]):
    """

    content: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        content = d.pop("content", UNSET)

        csscms_data_model_models_certificate_download_response = cls(
            content=content,
        )

        return csscms_data_model_models_certificate_download_response
