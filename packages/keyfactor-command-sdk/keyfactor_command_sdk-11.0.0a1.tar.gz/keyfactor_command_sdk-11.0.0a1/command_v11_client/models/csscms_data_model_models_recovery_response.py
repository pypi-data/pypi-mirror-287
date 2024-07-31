from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsRecoveryResponse")


@_attrs_define
class CSSCMSDataModelModelsRecoveryResponse:
    """
    Attributes:
        pfx (Union[Unset, None, str]):
        file_name (Union[Unset, None, str]):
    """

    pfx: Union[Unset, None, str] = UNSET
    file_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        pfx = self.pfx
        file_name = self.file_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if pfx is not UNSET:
            field_dict["pfx"] = pfx
        if file_name is not UNSET:
            field_dict["fileName"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        pfx = d.pop("pfx", UNSET)

        file_name = d.pop("fileName", UNSET)

        csscms_data_model_models_recovery_response = cls(
            pfx=pfx,
            file_name=file_name,
        )

        return csscms_data_model_models_recovery_response
