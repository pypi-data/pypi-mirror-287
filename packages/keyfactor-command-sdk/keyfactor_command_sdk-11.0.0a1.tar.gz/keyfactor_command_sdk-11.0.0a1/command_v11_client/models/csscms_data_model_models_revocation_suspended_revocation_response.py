from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsRevocationSuspendedRevocationResponse")


@_attrs_define
class CSSCMSDataModelModelsRevocationSuspendedRevocationResponse:
    """
    Attributes:
        cert_id (Union[Unset, int]):
        workflow_id (Union[Unset, str]):
        message (Union[Unset, None, str]):
    """

    cert_id: Union[Unset, int] = UNSET
    workflow_id: Union[Unset, str] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        cert_id = self.cert_id
        workflow_id = self.workflow_id
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if cert_id is not UNSET:
            field_dict["certId"] = cert_id
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        cert_id = d.pop("certId", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        message = d.pop("message", UNSET)

        csscms_data_model_models_revocation_suspended_revocation_response = cls(
            cert_id=cert_id,
            workflow_id=workflow_id,
            message=message,
        )

        return csscms_data_model_models_revocation_suspended_revocation_response
