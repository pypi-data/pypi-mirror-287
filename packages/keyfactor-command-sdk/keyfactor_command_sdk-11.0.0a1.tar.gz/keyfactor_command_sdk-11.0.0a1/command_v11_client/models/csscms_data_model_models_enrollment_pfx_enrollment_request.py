import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_pki_enums_certificate_collection_order import KeyfactorPKIEnumsCertificateCollectionOrder
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_additional_enrollment_fields import (
        CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields,
    )
    from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_additional_enrollment_fields_input import (
        CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFieldsInput,
    )
    from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_metadata import (
        CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadata,
    )
    from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_metadata_input import (
        CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadataInput,
    )
    from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_sa_ns import (
        CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestSaNs,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequest")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequest:
    """
    Attributes:
        template (Union[Unset, None, str]):
        sa_ns (Union[Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestSaNs]):
        certificate_authority (Union[Unset, None, str]):
        include_chain (Union[Unset, bool]):
        metadata_input (Union[Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadataInput]):
        additional_enrollment_fields_input (Union[Unset, None,
            CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFieldsInput]):
        timestamp (Union[Unset, datetime.datetime]):
        metadata (Union[Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadata]):
        additional_enrollment_fields (Union[Unset, None,
            CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields]):
        custom_friendly_name (Union[Unset, None, str]):
        password (Union[Unset, None, str]):
        populate_missing_values_from_ad (Union[Unset, bool]):
        subject (Union[Unset, None, str]):
        renewal_certificate_id (Union[Unset, None, int]):
        chain_order (Union[Unset, None, str]):
        certificate_collection_order (Union[Unset, KeyfactorPKIEnumsCertificateCollectionOrder]):
        use_legacy_encryption (Union[Unset, None, bool]):
        key_type (Union[Unset, None, str]):
        key_length (Union[Unset, int]):
        curve (Union[Unset, None, str]):
    """

    template: Union[Unset, None, str] = UNSET
    sa_ns: Union[Unset, None, "CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestSaNs"] = UNSET
    certificate_authority: Union[Unset, None, str] = UNSET
    include_chain: Union[Unset, bool] = UNSET
    metadata_input: Union[Unset, None, "CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadataInput"] = UNSET
    additional_enrollment_fields_input: Union[
        Unset, None, "CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFieldsInput"
    ] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    metadata: Union[Unset, None, "CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadata"] = UNSET
    additional_enrollment_fields: Union[
        Unset, None, "CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields"
    ] = UNSET
    custom_friendly_name: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET
    populate_missing_values_from_ad: Union[Unset, bool] = UNSET
    subject: Union[Unset, None, str] = UNSET
    renewal_certificate_id: Union[Unset, None, int] = UNSET
    chain_order: Union[Unset, None, str] = UNSET
    certificate_collection_order: Union[Unset, KeyfactorPKIEnumsCertificateCollectionOrder] = UNSET
    use_legacy_encryption: Union[Unset, None, bool] = UNSET
    key_type: Union[Unset, None, str] = UNSET
    key_length: Union[Unset, int] = UNSET
    curve: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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

        custom_friendly_name = self.custom_friendly_name
        password = self.password
        populate_missing_values_from_ad = self.populate_missing_values_from_ad
        subject = self.subject
        renewal_certificate_id = self.renewal_certificate_id
        chain_order = self.chain_order
        certificate_collection_order: Union[Unset, int] = UNSET
        if not isinstance(self.certificate_collection_order, Unset):
            certificate_collection_order = self.certificate_collection_order.value

        use_legacy_encryption = self.use_legacy_encryption
        key_type = self.key_type
        key_length = self.key_length
        curve = self.curve

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
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
        if custom_friendly_name is not UNSET:
            field_dict["customFriendlyName"] = custom_friendly_name
        if password is not UNSET:
            field_dict["password"] = password
        if populate_missing_values_from_ad is not UNSET:
            field_dict["populateMissingValuesFromAD"] = populate_missing_values_from_ad
        if subject is not UNSET:
            field_dict["subject"] = subject
        if renewal_certificate_id is not UNSET:
            field_dict["renewalCertificateId"] = renewal_certificate_id
        if chain_order is not UNSET:
            field_dict["chainOrder"] = chain_order
        if certificate_collection_order is not UNSET:
            field_dict["certificateCollectionOrder"] = certificate_collection_order
        if use_legacy_encryption is not UNSET:
            field_dict["useLegacyEncryption"] = use_legacy_encryption
        if key_type is not UNSET:
            field_dict["keyType"] = key_type
        if key_length is not UNSET:
            field_dict["keyLength"] = key_length
        if curve is not UNSET:
            field_dict["curve"] = curve

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_additional_enrollment_fields import (
            CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields,
        )
        from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_additional_enrollment_fields_input import (
            CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFieldsInput,
        )
        from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_metadata import (
            CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadata,
        )
        from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_metadata_input import (
            CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadataInput,
        )
        from ..models.csscms_data_model_models_enrollment_pfx_enrollment_request_sa_ns import (
            CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestSaNs,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        template = d.pop("template", UNSET)

        _sa_ns = d.pop("saNs", UNSET)
        sa_ns: Union[Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestSaNs]
        if _sa_ns is None:
            sa_ns = None
        elif isinstance(_sa_ns, Unset):
            sa_ns = UNSET
        else:
            sa_ns = CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestSaNs.from_dict(_sa_ns)

        certificate_authority = d.pop("certificateAuthority", UNSET)

        include_chain = d.pop("includeChain", UNSET)

        _metadata_input = d.pop("metadataInput", UNSET)
        metadata_input: Union[Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadataInput]
        if _metadata_input is None:
            metadata_input = None
        elif isinstance(_metadata_input, Unset):
            metadata_input = UNSET
        else:
            metadata_input = CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadataInput.from_dict(_metadata_input)

        _additional_enrollment_fields_input = d.pop("additionalEnrollmentFieldsInput", UNSET)
        additional_enrollment_fields_input: Union[
            Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFieldsInput
        ]
        if _additional_enrollment_fields_input is None:
            additional_enrollment_fields_input = None
        elif isinstance(_additional_enrollment_fields_input, Unset):
            additional_enrollment_fields_input = UNSET
        else:
            additional_enrollment_fields_input = (
                CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFieldsInput.from_dict(
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
        metadata: Union[Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestMetadata.from_dict(_metadata)

        _additional_enrollment_fields = d.pop("additionalEnrollmentFields", UNSET)
        additional_enrollment_fields: Union[
            Unset, None, CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields
        ]
        if _additional_enrollment_fields is None:
            additional_enrollment_fields = None
        elif isinstance(_additional_enrollment_fields, Unset):
            additional_enrollment_fields = UNSET
        else:
            additional_enrollment_fields = (
                CSSCMSDataModelModelsEnrollmentPFXEnrollmentRequestAdditionalEnrollmentFields.from_dict(
                    _additional_enrollment_fields
                )
            )

        custom_friendly_name = d.pop("customFriendlyName", UNSET)

        password = d.pop("password", UNSET)

        populate_missing_values_from_ad = d.pop("populateMissingValuesFromAD", UNSET)

        subject = d.pop("subject", UNSET)

        renewal_certificate_id = d.pop("renewalCertificateId", UNSET)

        chain_order = d.pop("chainOrder", UNSET)

        _certificate_collection_order = d.pop("certificateCollectionOrder", UNSET)
        certificate_collection_order: Union[Unset, KeyfactorPKIEnumsCertificateCollectionOrder]
        if isinstance(_certificate_collection_order, Unset):
            certificate_collection_order = UNSET
        else:
            certificate_collection_order = KeyfactorPKIEnumsCertificateCollectionOrder(_certificate_collection_order)

        use_legacy_encryption = d.pop("useLegacyEncryption", UNSET)

        key_type = d.pop("keyType", UNSET)

        key_length = d.pop("keyLength", UNSET)

        curve = d.pop("curve", UNSET)

        csscms_data_model_models_enrollment_pfx_enrollment_request = cls(
            template=template,
            sa_ns=sa_ns,
            certificate_authority=certificate_authority,
            include_chain=include_chain,
            metadata_input=metadata_input,
            additional_enrollment_fields_input=additional_enrollment_fields_input,
            timestamp=timestamp,
            metadata=metadata,
            additional_enrollment_fields=additional_enrollment_fields,
            custom_friendly_name=custom_friendly_name,
            password=password,
            populate_missing_values_from_ad=populate_missing_values_from_ad,
            subject=subject,
            renewal_certificate_id=renewal_certificate_id,
            chain_order=chain_order,
            certificate_collection_order=certificate_collection_order,
            use_legacy_encryption=use_legacy_encryption,
            key_type=key_type,
            key_length=key_length,
            curve=curve,
        )

        return csscms_data_model_models_enrollment_pfx_enrollment_request
