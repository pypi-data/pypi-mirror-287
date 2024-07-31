import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_pki_enums_certificate_state import KeyfactorPKIEnumsCertificateState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_workflow_certificate_request_model_metadata import (
        CSSCMSDataModelModelsWorkflowCertificateRequestModelMetadata,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsWorkflowCertificateRequestModel")


@_attrs_define
class CSSCMSDataModelModelsWorkflowCertificateRequestModel:
    """
    Attributes:
        id (Union[Unset, int]):
        ca_request_id (Union[Unset, None, str]):
        common_name (Union[Unset, None, str]):
        distinguished_name (Union[Unset, None, str]):
        submission_date (Union[Unset, None, datetime.datetime]):
        certificate_authority (Union[Unset, None, str]):
        template (Union[Unset, None, str]):
        requester (Union[Unset, None, str]):
        state (Union[Unset, KeyfactorPKIEnumsCertificateState]):
        state_string (Union[Unset, None, str]):
        metadata (Union[Unset, None, CSSCMSDataModelModelsWorkflowCertificateRequestModelMetadata]):
    """

    id: Union[Unset, int] = UNSET
    ca_request_id: Union[Unset, None, str] = UNSET
    common_name: Union[Unset, None, str] = UNSET
    distinguished_name: Union[Unset, None, str] = UNSET
    submission_date: Union[Unset, None, datetime.datetime] = UNSET
    certificate_authority: Union[Unset, None, str] = UNSET
    template: Union[Unset, None, str] = UNSET
    requester: Union[Unset, None, str] = UNSET
    state: Union[Unset, KeyfactorPKIEnumsCertificateState] = UNSET
    state_string: Union[Unset, None, str] = UNSET
    metadata: Union[Unset, None, "CSSCMSDataModelModelsWorkflowCertificateRequestModelMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        ca_request_id = self.ca_request_id
        common_name = self.common_name
        distinguished_name = self.distinguished_name
        submission_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.submission_date, Unset):
            submission_date = self.submission_date.isoformat()[:-6]+'Z' if self.submission_date else None

        certificate_authority = self.certificate_authority
        template = self.template
        requester = self.requester
        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        state_string = self.state_string
        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ca_request_id is not UNSET:
            field_dict["caRequestId"] = ca_request_id
        if common_name is not UNSET:
            field_dict["commonName"] = common_name
        if distinguished_name is not UNSET:
            field_dict["distinguishedName"] = distinguished_name
        if submission_date is not UNSET:
            field_dict["submissionDate"] = submission_date
        if certificate_authority is not UNSET:
            field_dict["certificateAuthority"] = certificate_authority
        if template is not UNSET:
            field_dict["template"] = template
        if requester is not UNSET:
            field_dict["requester"] = requester
        if state is not UNSET:
            field_dict["state"] = state
        if state_string is not UNSET:
            field_dict["stateString"] = state_string
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_workflow_certificate_request_model_metadata import (
            CSSCMSDataModelModelsWorkflowCertificateRequestModelMetadata,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        ca_request_id = d.pop("caRequestId", UNSET)

        common_name = d.pop("commonName", UNSET)

        distinguished_name = d.pop("distinguishedName", UNSET)

        _submission_date = d.pop("submissionDate", UNSET)
        submission_date: Union[Unset, None, datetime.datetime]
        if _submission_date is None:
            submission_date = None
        elif isinstance(_submission_date, Unset):
            submission_date = UNSET
        else:
            submission_date = isoparse(_submission_date)

        certificate_authority = d.pop("certificateAuthority", UNSET)

        template = d.pop("template", UNSET)

        requester = d.pop("requester", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, KeyfactorPKIEnumsCertificateState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = KeyfactorPKIEnumsCertificateState(_state)

        state_string = d.pop("stateString", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CSSCMSDataModelModelsWorkflowCertificateRequestModelMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CSSCMSDataModelModelsWorkflowCertificateRequestModelMetadata.from_dict(_metadata)

        csscms_data_model_models_workflow_certificate_request_model = cls(
            id=id,
            ca_request_id=ca_request_id,
            common_name=common_name,
            distinguished_name=distinguished_name,
            submission_date=submission_date,
            certificate_authority=certificate_authority,
            template=template,
            requester=requester,
            state=state,
            state_string=state_string,
            metadata=metadata,
        )

        return csscms_data_model_models_workflow_certificate_request_model
