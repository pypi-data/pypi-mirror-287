import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_additional_enrollment_fields import (
        CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFields,
    )
    from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_additional_enrollment_fields_input import (
        CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFieldsInput,
    )
    from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_metadata import (
        CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadata,
    )
    from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_metadata_input import (
        CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadataInput,
    )
    from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_sa_ns import (
        CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestSaNs,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest:
    """
    Attributes:
        csr (str):
        template (Union[Unset, None, str]):
        sa_ns (Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestSaNs]):
        certificate_authority (Union[Unset, None, str]):
        include_chain (Union[Unset, bool]):
        metadata_input (Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadataInput]):
        additional_enrollment_fields_input (Union[Unset, None,
            CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFieldsInput]):
        timestamp (Union[Unset, datetime.datetime]):
        metadata (Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadata]):
        additional_enrollment_fields (Union[Unset, None,
            CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFields]):
        private_key (Union[Unset, None, str]):
    """

    csr: str
    template: Union[Unset, None, str] = UNSET
    sa_ns: Union[Unset, None, "CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestSaNs"] = UNSET
    certificate_authority: Union[Unset, None, str] = UNSET
    include_chain: Union[Unset, bool] = UNSET
    metadata_input: Union[Unset, None, "CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadataInput"] = UNSET
    additional_enrollment_fields_input: Union[
        Unset, None, "CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFieldsInput"
    ] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    metadata: Union[Unset, None, "CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadata"] = UNSET
    additional_enrollment_fields: Union[
        Unset, None, "CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFields"
    ] = UNSET
    private_key: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        csr = self.csr
        template = self.template
        sa_ns: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sa_ns, Unset):
            sa_ns = self.sa_ns.to_dict() if self.sa_ns else None

        certificate_authority = self.certificate_authority
        include_chain = self.include_chain
        metadata_input: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata_input, Unset):
            metadata_input = self.metadata_input.to_dict() if self.metadata_input else None

        additional_enrollment_fields_input: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_enrollment_fields_input, Unset):
            additional_enrollment_fields_input = (
                self.additional_enrollment_fields_input.to_dict() if self.additional_enrollment_fields_input else None
            )

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()[:-6]+'Z'

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        additional_enrollment_fields: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_enrollment_fields, Unset):
            additional_enrollment_fields = (
                self.additional_enrollment_fields.to_dict() if self.additional_enrollment_fields else None
            )

        private_key = self.private_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "csr": csr,
            }
        )
        if template is not UNSET:
            field_dict["template"] = template
        if sa_ns is not UNSET:
            field_dict["saNs"] = sa_ns
        if certificate_authority is not UNSET:
            field_dict["certificateAuthority"] = certificate_authority
        if include_chain is not UNSET:
            field_dict["includeChain"] = include_chain
        if metadata_input is not UNSET:
            field_dict["metadataInput"] = metadata_input
        if additional_enrollment_fields_input is not UNSET:
            field_dict["additionalEnrollmentFieldsInput"] = additional_enrollment_fields_input
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if additional_enrollment_fields is not UNSET:
            field_dict["additionalEnrollmentFields"] = additional_enrollment_fields
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_additional_enrollment_fields import (
            CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFields,
        )
        from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_additional_enrollment_fields_input import (
            CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFieldsInput,
        )
        from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_metadata import (
            CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadata,
        )
        from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_metadata_input import (
            CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadataInput,
        )
        from ..models.csscms_data_model_models_enrollment_csr_enrollment_request_sa_ns import (
            CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestSaNs,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        csr = d.pop("csr")

        template = d.pop("template", UNSET)

        _sa_ns = d.pop("saNs", UNSET)
        sa_ns: Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestSaNs]
        if _sa_ns is None:
            sa_ns = None
        elif isinstance(_sa_ns, Unset):
            sa_ns = UNSET
        else:
            sa_ns = CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestSaNs.from_dict(_sa_ns)

        certificate_authority = d.pop("certificateAuthority", UNSET)

        include_chain = d.pop("includeChain", UNSET)

        _metadata_input = d.pop("metadataInput", UNSET)
        metadata_input: Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadataInput]
        if _metadata_input is None:
            metadata_input = None
        elif isinstance(_metadata_input, Unset):
            metadata_input = UNSET
        else:
            metadata_input = CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadataInput.from_dict(_metadata_input)

        _additional_enrollment_fields_input = d.pop("additionalEnrollmentFieldsInput", UNSET)
        additional_enrollment_fields_input: Union[
            Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFieldsInput
        ]
        if _additional_enrollment_fields_input is None:
            additional_enrollment_fields_input = None
        elif isinstance(_additional_enrollment_fields_input, Unset):
            additional_enrollment_fields_input = UNSET
        else:
            additional_enrollment_fields_input = (
                CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFieldsInput.from_dict(
                    _additional_enrollment_fields_input
                )
            )

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestMetadata.from_dict(_metadata)

        _additional_enrollment_fields = d.pop("additionalEnrollmentFields", UNSET)
        additional_enrollment_fields: Union[
            Unset, None, CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFields
        ]
        if _additional_enrollment_fields is None:
            additional_enrollment_fields = None
        elif isinstance(_additional_enrollment_fields, Unset):
            additional_enrollment_fields = UNSET
        else:
            additional_enrollment_fields = (
                CSSCMSDataModelModelsEnrollmentCSREnrollmentRequestAdditionalEnrollmentFields.from_dict(
                    _additional_enrollment_fields
                )
            )

        private_key = d.pop("privateKey", UNSET)

        csscms_data_model_models_enrollment_csr_enrollment_request = cls(
            csr=csr,
            template=template,
            sa_ns=sa_ns,
            certificate_authority=certificate_authority,
            include_chain=include_chain,
            metadata_input=metadata_input,
            additional_enrollment_fields_input=additional_enrollment_fields_input,
            timestamp=timestamp,
            metadata=metadata,
            additional_enrollment_fields=additional_enrollment_fields,
            private_key=private_key,
        )

        return csscms_data_model_models_enrollment_csr_enrollment_request
