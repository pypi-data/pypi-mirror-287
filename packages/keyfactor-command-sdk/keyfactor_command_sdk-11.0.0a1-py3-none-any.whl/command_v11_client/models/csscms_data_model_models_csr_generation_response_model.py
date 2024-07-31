from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCSRGenerationResponseModel")


@_attrs_define
class CSSCMSDataModelModelsCSRGenerationResponseModel:
    """
    Attributes:
        csr_file_path (Union[Unset, None, str]):
        csr_text (Union[Unset, None, str]):
    """

    csr_file_path: Union[Unset, None, str] = UNSET
    csr_text: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        csr_file_path = self.csr_file_path
        csr_text = self.csr_text

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if csr_file_path is not UNSET:
            field_dict["csrFilePath"] = csr_file_path
        if csr_text is not UNSET:
            field_dict["csrText"] = csr_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        csr_file_path = d.pop("csrFilePath", UNSET)

        csr_text = d.pop("csrText", UNSET)

        csscms_data_model_models_csr_generation_response_model = cls(
            csr_file_path=csr_file_path,
            csr_text=csr_text,
        )

        return csscms_data_model_models_csr_generation_response_model
