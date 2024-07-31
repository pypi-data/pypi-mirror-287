import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_pki_enums_certificate_state import KeyfactorPKIEnumsCertificateState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_workflow_certificate_request_cert_store_model import (
        CSSCMSDataModelModelsWorkflowCertificateRequestCertStoreModel,
    )
    from ..models.keyfactor_web_keyfactor_api_models_certificates_cert_request_response_model_metadata import (
        KeyfactorWebKeyfactorApiModelsCertificatesCertRequestResponseModelMetadata,
    )
    from ..models.keyfactor_web_keyfactor_api_models_certificates_subject_alternative_name import (
        KeyfactorWebKeyfactorApiModelsCertificatesSubjectAlternativeName,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificatesCertRequestResponseModel")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificatesCertRequestResponseModel:
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
        metadata (Union[Unset, None, KeyfactorWebKeyfactorApiModelsCertificatesCertRequestResponseModelMetadata]):
        denial_comment (Union[Unset, None, str]):
        key_length (Union[Unset, None, str]):
        sa_ns (Union[Unset, None, List[str]]):
        cert_stores (Union[Unset, None, List['CSSCMSDataModelModelsWorkflowCertificateRequestCertStoreModel']]):
        curve (Union[Unset, None, str]):
        subject_alt_names (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsCertificatesSubjectAlternativeName']]):
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
    metadata: Union[Unset, None, "KeyfactorWebKeyfactorApiModelsCertificatesCertRequestResponseModelMetadata"] = UNSET
    denial_comment: Union[Unset, None, str] = UNSET
    key_length: Union[Unset, None, str] = UNSET
    sa_ns: Union[Unset, None, List[str]] = UNSET
    cert_stores: Union[Unset, None, List["CSSCMSDataModelModelsWorkflowCertificateRequestCertStoreModel"]] = UNSET
    curve: Union[Unset, None, str] = UNSET
    subject_alt_names: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsCertificatesSubjectAlternativeName"]
    ] = UNSET

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

        denial_comment = self.denial_comment
        key_length = self.key_length
        sa_ns: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.sa_ns, Unset):
            if self.sa_ns is None:
                sa_ns = None
            else:
                sa_ns = self.sa_ns

        cert_stores: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cert_stores, Unset):
            if self.cert_stores is None:
                cert_stores = None
            else:
                cert_stores = []
                for cert_stores_item_data in self.cert_stores:
                    cert_stores_item = cert_stores_item_data.to_dict()

                    cert_stores.append(cert_stores_item)

        curve = self.curve
        subject_alt_names: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subject_alt_names, Unset):
            if self.subject_alt_names is None:
                subject_alt_names = None
            else:
                subject_alt_names = []
                for subject_alt_names_item_data in self.subject_alt_names:
                    subject_alt_names_item = subject_alt_names_item_data.to_dict()

                    subject_alt_names.append(subject_alt_names_item)

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
        if denial_comment is not UNSET:
            field_dict["denialComment"] = denial_comment
        if key_length is not UNSET:
            field_dict["keyLength"] = key_length
        if sa_ns is not UNSET:
            field_dict["saNs"] = sa_ns
        if cert_stores is not UNSET:
            field_dict["certStores"] = cert_stores
        if curve is not UNSET:
            field_dict["curve"] = curve
        if subject_alt_names is not UNSET:
            field_dict["subjectAltNames"] = subject_alt_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_workflow_certificate_request_cert_store_model import (
            CSSCMSDataModelModelsWorkflowCertificateRequestCertStoreModel,
        )
        from ..models.keyfactor_web_keyfactor_api_models_certificates_cert_request_response_model_metadata import (
            KeyfactorWebKeyfactorApiModelsCertificatesCertRequestResponseModelMetadata,
        )
        from ..models.keyfactor_web_keyfactor_api_models_certificates_subject_alternative_name import (
            KeyfactorWebKeyfactorApiModelsCertificatesSubjectAlternativeName,
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
        metadata: Union[Unset, None, KeyfactorWebKeyfactorApiModelsCertificatesCertRequestResponseModelMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = KeyfactorWebKeyfactorApiModelsCertificatesCertRequestResponseModelMetadata.from_dict(_metadata)

        denial_comment = d.pop("denialComment", UNSET)

        key_length = d.pop("keyLength", UNSET)

        sa_ns = cast(List[str], d.pop("saNs", UNSET))

        cert_stores = []
        _cert_stores = d.pop("certStores", UNSET)
        for cert_stores_item_data in _cert_stores or []:
            cert_stores_item = CSSCMSDataModelModelsWorkflowCertificateRequestCertStoreModel.from_dict(
                cert_stores_item_data
            )

            cert_stores.append(cert_stores_item)

        curve = d.pop("curve", UNSET)

        subject_alt_names = []
        _subject_alt_names = d.pop("subjectAltNames", UNSET)
        for subject_alt_names_item_data in _subject_alt_names or []:
            subject_alt_names_item = KeyfactorWebKeyfactorApiModelsCertificatesSubjectAlternativeName.from_dict(
                subject_alt_names_item_data
            )

            subject_alt_names.append(subject_alt_names_item)

        keyfactor_web_keyfactor_api_models_certificates_cert_request_response_model = cls(
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
            denial_comment=denial_comment,
            key_length=key_length,
            sa_ns=sa_ns,
            cert_stores=cert_stores,
            curve=curve,
            subject_alt_names=subject_alt_names,
        )

        return keyfactor_web_keyfactor_api_models_certificates_cert_request_response_model
