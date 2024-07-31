from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_templates_algorithms_algorithm_data import (
        CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo")


@_attrs_define
class CSSCMSDataModelModelsTemplatesAlgorithmsKeyInfo:
    """
    Attributes:
        ecdsa (Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData]):
        rsa (Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData]):
        ed448 (Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData]):
        ed25519 (Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData]):
    """

    ecdsa: Union[Unset, "CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData"] = UNSET
    rsa: Union[Unset, "CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData"] = UNSET
    ed448: Union[Unset, "CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData"] = UNSET
    ed25519: Union[Unset, "CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ecdsa: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ecdsa, Unset):
            ecdsa = self.ecdsa.to_dict()

        rsa: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rsa, Unset):
            rsa = self.rsa.to_dict()

        ed448: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ed448, Unset):
            ed448 = self.ed448.to_dict()

        ed25519: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ed25519, Unset):
            ed25519 = self.ed25519.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ecdsa is not UNSET:
            field_dict["ecdsa"] = ecdsa
        if rsa is not UNSET:
            field_dict["rsa"] = rsa
        if ed448 is not UNSET:
            field_dict["ed448"] = ed448
        if ed25519 is not UNSET:
            field_dict["ed25519"] = ed25519

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_templates_algorithms_algorithm_data import (
            CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _ecdsa = d.pop("ecdsa", UNSET)
        ecdsa: Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData]
        if isinstance(_ecdsa, Unset):
            ecdsa = UNSET
        else:
            ecdsa = CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData.from_dict(_ecdsa)

        _rsa = d.pop("rsa", UNSET)
        rsa: Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData]
        if isinstance(_rsa, Unset):
            rsa = UNSET
        else:
            rsa = CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData.from_dict(_rsa)

        _ed448 = d.pop("ed448", UNSET)
        ed448: Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData]
        if isinstance(_ed448, Unset):
            ed448 = UNSET
        else:
            ed448 = CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData.from_dict(_ed448)

        _ed25519 = d.pop("ed25519", UNSET)
        ed25519: Union[Unset, CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData]
        if isinstance(_ed25519, Unset):
            ed25519 = UNSET
        else:
            ed25519 = CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData.from_dict(_ed25519)

        csscms_data_model_models_templates_algorithms_key_info = cls(
            ecdsa=ecdsa,
            rsa=rsa,
            ed448=ed448,
            ed25519=ed25519,
        )

        return csscms_data_model_models_templates_algorithms_key_info
