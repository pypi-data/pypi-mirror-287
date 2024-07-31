from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsWorkflowProcessedCertificateRequest")


@_attrs_define
class CSSCMSDataModelModelsWorkflowProcessedCertificateRequest:
    """
    Attributes:
        ca_row_id (Union[Unset, None, int]):
        ca_request_id (Union[Unset, None, str]):
        ca_host (Union[Unset, None, str]):
        ca_logical_name (Union[Unset, None, str]):
        keyfactor_request_id (Union[Unset, int]):
        comment (Union[Unset, None, str]):
    """

    ca_row_id: Union[Unset, None, int] = UNSET
    ca_request_id: Union[Unset, None, str] = UNSET
    ca_host: Union[Unset, None, str] = UNSET
    ca_logical_name: Union[Unset, None, str] = UNSET
    keyfactor_request_id: Union[Unset, int] = UNSET
    comment: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        ca_row_id = self.ca_row_id
        ca_request_id = self.ca_request_id
        ca_host = self.ca_host
        ca_logical_name = self.ca_logical_name
        keyfactor_request_id = self.keyfactor_request_id
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if ca_row_id is not UNSET:
            field_dict["caRowId"] = ca_row_id
        if ca_request_id is not UNSET:
            field_dict["caRequestId"] = ca_request_id
        if ca_host is not UNSET:
            field_dict["caHost"] = ca_host
        if ca_logical_name is not UNSET:
            field_dict["caLogicalName"] = ca_logical_name
        if keyfactor_request_id is not UNSET:
            field_dict["keyfactorRequestId"] = keyfactor_request_id
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        ca_row_id = d.pop("caRowId", UNSET)

        ca_request_id = d.pop("caRequestId", UNSET)

        ca_host = d.pop("caHost", UNSET)

        ca_logical_name = d.pop("caLogicalName", UNSET)

        keyfactor_request_id = d.pop("keyfactorRequestId", UNSET)

        comment = d.pop("comment", UNSET)

        csscms_data_model_models_workflow_processed_certificate_request = cls(
            ca_row_id=ca_row_id,
            ca_request_id=ca_request_id,
            ca_host=ca_host,
            ca_logical_name=ca_logical_name,
            keyfactor_request_id=keyfactor_request_id,
            comment=comment,
        )

        return csscms_data_model_models_workflow_processed_certificate_request
