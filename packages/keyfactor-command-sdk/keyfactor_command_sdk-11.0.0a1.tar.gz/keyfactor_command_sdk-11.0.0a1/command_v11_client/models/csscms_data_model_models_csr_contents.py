from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CSSCMSDataModelModelsCSRContents")


@_attrs_define
class CSSCMSDataModelModelsCSRContents:
    """
    Attributes:
        csr (str):
    """

    csr: str

    def to_dict(self) -> Dict[str, Any]:
        csr = self.csr

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "csr": csr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        csr = d.pop("csr")

        csscms_data_model_models_csr_contents = cls(
            csr=csr,
        )

        return csscms_data_model_models_csr_contents
