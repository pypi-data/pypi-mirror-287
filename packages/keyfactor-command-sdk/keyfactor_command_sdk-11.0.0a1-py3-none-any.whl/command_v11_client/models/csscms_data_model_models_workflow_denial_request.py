from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsWorkflowDenialRequest")


@_attrs_define
class CSSCMSDataModelModelsWorkflowDenialRequest:
    """
    Attributes:
        comment (Union[Unset, None, str]):
        certificate_request_ids (Union[Unset, None, List[int]]):
    """

    comment: Union[Unset, None, str] = UNSET
    certificate_request_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        comment = self.comment
        certificate_request_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.certificate_request_ids, Unset):
            if self.certificate_request_ids is None:
                certificate_request_ids = None
            else:
                certificate_request_ids = self.certificate_request_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if certificate_request_ids is not UNSET:
            field_dict["certificateRequestIds"] = certificate_request_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        comment = d.pop("comment", UNSET)

        certificate_request_ids = cast(List[int], d.pop("certificateRequestIds", UNSET))

        csscms_data_model_models_workflow_denial_request = cls(
            comment=comment,
            certificate_request_ids=certificate_request_ids,
        )

        return csscms_data_model_models_workflow_denial_request
