from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData")


@_attrs_define
class CSSCMSDataModelModelsTemplatesAlgorithmsAlgorithmData:
    """
    Attributes:
        bit_lengths (Union[Unset, None, List[int]]):
        curves (Union[Unset, None, List[str]]):
    """

    bit_lengths: Union[Unset, None, List[int]] = UNSET
    curves: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        bit_lengths: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.bit_lengths, Unset):
            if self.bit_lengths is None:
                bit_lengths = None
            else:
                bit_lengths = self.bit_lengths

        curves: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.curves, Unset):
            if self.curves is None:
                curves = None
            else:
                curves = self.curves

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if bit_lengths is not UNSET:
            field_dict["bitLengths"] = bit_lengths
        if curves is not UNSET:
            field_dict["curves"] = curves

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        bit_lengths = cast(List[int], d.pop("bitLengths", UNSET))

        curves = cast(List[str], d.pop("curves", UNSET))

        csscms_data_model_models_templates_algorithms_algorithm_data = cls(
            bit_lengths=bit_lengths,
            curves=curves,
        )

        return csscms_data_model_models_templates_algorithms_algorithm_data
