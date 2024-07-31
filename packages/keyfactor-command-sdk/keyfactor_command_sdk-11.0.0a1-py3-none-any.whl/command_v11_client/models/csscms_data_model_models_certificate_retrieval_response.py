import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.csscms_core_enums_encryption_key_type import CSSCMSCoreEnumsEncryptionKeyType
from ..models.keyfactor_pki_enums_certificate_state import KeyfactorPKIEnumsCertificateState
from ..models.keyfactor_pki_enums_revoke_code import KeyfactorPKIEnumsRevokeCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_retrieval_response_certificate_store_inventory_item_model import (
        CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel,
    )
    from ..models.csscms_data_model_models_certificate_retrieval_response_certificate_store_location_detail_model import (
        CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel,
    )
    from ..models.csscms_data_model_models_certificate_retrieval_response_crl_distribution_point_model import (
        CSSCMSDataModelModelsCertificateRetrievalResponseCRLDistributionPointModel,
    )
    from ..models.csscms_data_model_models_certificate_retrieval_response_detailed_key_usage_model import (
        CSSCMSDataModelModelsCertificateRetrievalResponseDetailedKeyUsageModel,
    )
    from ..models.csscms_data_model_models_certificate_retrieval_response_extended_key_usage_model import (
        CSSCMSDataModelModelsCertificateRetrievalResponseExtendedKeyUsageModel,
    )
    from ..models.csscms_data_model_models_certificate_retrieval_response_location_count_model import (
        CSSCMSDataModelModelsCertificateRetrievalResponseLocationCountModel,
    )
    from ..models.csscms_data_model_models_certificate_retrieval_response_metadata import (
        CSSCMSDataModelModelsCertificateRetrievalResponseMetadata,
    )
    from ..models.csscms_data_model_models_certificate_retrieval_response_subject_alternative_name_model import (
        CSSCMSDataModelModelsCertificateRetrievalResponseSubjectAlternativeNameModel,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateRetrievalResponse")


@_attrs_define
class CSSCMSDataModelModelsCertificateRetrievalResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        thumbprint (Union[Unset, None, str]):
        serial_number (Union[Unset, None, str]):
        issued_dn (Union[Unset, None, str]):
        issued_cn (Union[Unset, None, str]):
        import_date (Union[Unset, datetime.datetime]):
        not_before (Union[Unset, datetime.datetime]):
        not_after (Union[Unset, datetime.datetime]):
        issuer_dn (Union[Unset, None, str]):
        principal_id (Union[Unset, None, int]):
        template_id (Union[Unset, None, int]):
        cert_state (Union[Unset, KeyfactorPKIEnumsCertificateState]):
        key_size_in_bits (Union[Unset, int]):
        key_type (Union[Unset, CSSCMSCoreEnumsEncryptionKeyType]):
        requester_id (Union[Unset, None, int]):
        issued_ou (Union[Unset, None, str]):
        issued_email (Union[Unset, None, str]):
        key_usage (Union[Unset, None, int]):
        signing_algorithm (Union[Unset, None, str]):
        cert_state_string (Union[Unset, None, str]):
        key_type_string (Union[Unset, None, str]):
        revocation_eff_date (Union[Unset, None, datetime.datetime]):
        revocation_reason (Union[Unset, KeyfactorPKIEnumsRevokeCode]):
        revocation_comment (Union[Unset, None, str]):
        certificate_authority_id (Union[Unset, None, int]):
        certificate_authority_name (Union[Unset, None, str]):
        template_name (Union[Unset, None, str]):
        archived_key (Union[Unset, bool]):
        has_private_key (Union[Unset, bool]):
        principal_name (Union[Unset, None, str]):
        cert_request_id (Union[Unset, None, int]):
        requester_name (Union[Unset, None, str]):
        content_bytes (Union[Unset, None, str]):
        extended_key_usages (Union[Unset, None,
            List['CSSCMSDataModelModelsCertificateRetrievalResponseExtendedKeyUsageModel']]):
        subject_alt_name_elements (Union[Unset, None,
            List['CSSCMSDataModelModelsCertificateRetrievalResponseSubjectAlternativeNameModel']]):
        crl_distribution_points (Union[Unset, None,
            List['CSSCMSDataModelModelsCertificateRetrievalResponseCRLDistributionPointModel']]):
        locations_count (Union[Unset, None,
            List['CSSCMSDataModelModelsCertificateRetrievalResponseLocationCountModel']]):
        ssl_locations (Union[Unset, None,
            List['CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel']]):
        locations (Union[Unset, None,
            List['CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel']]):
        metadata (Union[Unset, None, CSSCMSDataModelModelsCertificateRetrievalResponseMetadata]):
        certificate_key_id (Union[Unset, int]):
        ca_row_index (Union[Unset, None, int]):
        ca_record_id (Union[Unset, None, str]):
        detailed_key_usage (Union[Unset, CSSCMSDataModelModelsCertificateRetrievalResponseDetailedKeyUsageModel]):
        key_recoverable (Union[Unset, bool]):
        curve (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET
    serial_number: Union[Unset, None, str] = UNSET
    issued_dn: Union[Unset, None, str] = UNSET
    issued_cn: Union[Unset, None, str] = UNSET
    import_date: Union[Unset, datetime.datetime] = UNSET
    not_before: Union[Unset, datetime.datetime] = UNSET
    not_after: Union[Unset, datetime.datetime] = UNSET
    issuer_dn: Union[Unset, None, str] = UNSET
    principal_id: Union[Unset, None, int] = UNSET
    template_id: Union[Unset, None, int] = UNSET
    cert_state: Union[Unset, KeyfactorPKIEnumsCertificateState] = UNSET
    key_size_in_bits: Union[Unset, int] = UNSET
    key_type: Union[Unset, CSSCMSCoreEnumsEncryptionKeyType] = UNSET
    requester_id: Union[Unset, None, int] = UNSET
    issued_ou: Union[Unset, None, str] = UNSET
    issued_email: Union[Unset, None, str] = UNSET
    key_usage: Union[Unset, None, int] = UNSET
    signing_algorithm: Union[Unset, None, str] = UNSET
    cert_state_string: Union[Unset, None, str] = UNSET
    key_type_string: Union[Unset, None, str] = UNSET
    revocation_eff_date: Union[Unset, None, datetime.datetime] = UNSET
    revocation_reason: Union[Unset, KeyfactorPKIEnumsRevokeCode] = UNSET
    revocation_comment: Union[Unset, None, str] = UNSET
    certificate_authority_id: Union[Unset, None, int] = UNSET
    certificate_authority_name: Union[Unset, None, str] = UNSET
    template_name: Union[Unset, None, str] = UNSET
    archived_key: Union[Unset, bool] = UNSET
    has_private_key: Union[Unset, bool] = UNSET
    principal_name: Union[Unset, None, str] = UNSET
    cert_request_id: Union[Unset, None, int] = UNSET
    requester_name: Union[Unset, None, str] = UNSET
    content_bytes: Union[Unset, None, str] = UNSET
    extended_key_usages: Union[
        Unset, None, List["CSSCMSDataModelModelsCertificateRetrievalResponseExtendedKeyUsageModel"]
    ] = UNSET
    subject_alt_name_elements: Union[
        Unset, None, List["CSSCMSDataModelModelsCertificateRetrievalResponseSubjectAlternativeNameModel"]
    ] = UNSET
    crl_distribution_points: Union[
        Unset, None, List["CSSCMSDataModelModelsCertificateRetrievalResponseCRLDistributionPointModel"]
    ] = UNSET
    locations_count: Union[
        Unset, None, List["CSSCMSDataModelModelsCertificateRetrievalResponseLocationCountModel"]
    ] = UNSET
    ssl_locations: Union[
        Unset, None, List["CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel"]
    ] = UNSET
    locations: Union[
        Unset, None, List["CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel"]
    ] = UNSET
    metadata: Union[Unset, None, "CSSCMSDataModelModelsCertificateRetrievalResponseMetadata"] = UNSET
    certificate_key_id: Union[Unset, int] = UNSET
    ca_row_index: Union[Unset, None, int] = UNSET
    ca_record_id: Union[Unset, None, str] = UNSET
    detailed_key_usage: Union[Unset, "CSSCMSDataModelModelsCertificateRetrievalResponseDetailedKeyUsageModel"] = UNSET
    key_recoverable: Union[Unset, bool] = UNSET
    curve: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        thumbprint = self.thumbprint
        serial_number = self.serial_number
        issued_dn = self.issued_dn
        issued_cn = self.issued_cn
        import_date: Union[Unset, str] = UNSET
        if not isinstance(self.import_date, Unset):
            import_date = self.import_date.isoformat()[:-6]+'Z'

        not_before: Union[Unset, str] = UNSET
        if not isinstance(self.not_before, Unset):
            not_before = self.not_before.isoformat()[:-6]+'Z'

        not_after: Union[Unset, str] = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()[:-6]+'Z'

        issuer_dn = self.issuer_dn
        principal_id = self.principal_id
        template_id = self.template_id
        cert_state: Union[Unset, int] = UNSET
        if not isinstance(self.cert_state, Unset):
            cert_state = self.cert_state.value

        key_size_in_bits = self.key_size_in_bits
        key_type: Union[Unset, int] = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type.value

        requester_id = self.requester_id
        issued_ou = self.issued_ou
        issued_email = self.issued_email
        key_usage = self.key_usage
        signing_algorithm = self.signing_algorithm
        cert_state_string = self.cert_state_string
        key_type_string = self.key_type_string
        revocation_eff_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.revocation_eff_date, Unset):
            revocation_eff_date = self.revocation_eff_date.isoformat()[:-6]+'Z' if self.revocation_eff_date else None

        revocation_reason: Union[Unset, int] = UNSET
        if not isinstance(self.revocation_reason, Unset):
            revocation_reason = self.revocation_reason.value

        revocation_comment = self.revocation_comment
        certificate_authority_id = self.certificate_authority_id
        certificate_authority_name = self.certificate_authority_name
        template_name = self.template_name
        archived_key = self.archived_key
        has_private_key = self.has_private_key
        principal_name = self.principal_name
        cert_request_id = self.cert_request_id
        requester_name = self.requester_name
        content_bytes = self.content_bytes
        extended_key_usages: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extended_key_usages, Unset):
            if self.extended_key_usages is None:
                extended_key_usages = None
            else:
                extended_key_usages = []
                for extended_key_usages_item_data in self.extended_key_usages:
                    extended_key_usages_item = extended_key_usages_item_data.to_dict()

                    extended_key_usages.append(extended_key_usages_item)

        subject_alt_name_elements: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subject_alt_name_elements, Unset):
            if self.subject_alt_name_elements is None:
                subject_alt_name_elements = None
            else:
                subject_alt_name_elements = []
                for subject_alt_name_elements_item_data in self.subject_alt_name_elements:
                    subject_alt_name_elements_item = subject_alt_name_elements_item_data.to_dict()

                    subject_alt_name_elements.append(subject_alt_name_elements_item)

        crl_distribution_points: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.crl_distribution_points, Unset):
            if self.crl_distribution_points is None:
                crl_distribution_points = None
            else:
                crl_distribution_points = []
                for crl_distribution_points_item_data in self.crl_distribution_points:
                    crl_distribution_points_item = crl_distribution_points_item_data.to_dict()

                    crl_distribution_points.append(crl_distribution_points_item)

        locations_count: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations_count, Unset):
            if self.locations_count is None:
                locations_count = None
            else:
                locations_count = []
                for locations_count_item_data in self.locations_count:
                    locations_count_item = locations_count_item_data.to_dict()

                    locations_count.append(locations_count_item)

        ssl_locations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ssl_locations, Unset):
            if self.ssl_locations is None:
                ssl_locations = None
            else:
                ssl_locations = []
                for ssl_locations_item_data in self.ssl_locations:
                    ssl_locations_item = ssl_locations_item_data.to_dict()

                    ssl_locations.append(ssl_locations_item)

        locations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            if self.locations is None:
                locations = None
            else:
                locations = []
                for locations_item_data in self.locations:
                    locations_item = locations_item_data.to_dict()

                    locations.append(locations_item)

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        certificate_key_id = self.certificate_key_id
        ca_row_index = self.ca_row_index
        ca_record_id = self.ca_record_id
        detailed_key_usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.detailed_key_usage, Unset):
            detailed_key_usage = self.detailed_key_usage.to_dict()

        key_recoverable = self.key_recoverable
        curve = self.curve

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if issued_dn is not UNSET:
            field_dict["issuedDN"] = issued_dn
        if issued_cn is not UNSET:
            field_dict["issuedCN"] = issued_cn
        if import_date is not UNSET:
            field_dict["importDate"] = import_date
        if not_before is not UNSET:
            field_dict["notBefore"] = not_before
        if not_after is not UNSET:
            field_dict["notAfter"] = not_after
        if issuer_dn is not UNSET:
            field_dict["issuerDN"] = issuer_dn
        if principal_id is not UNSET:
            field_dict["principalId"] = principal_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if cert_state is not UNSET:
            field_dict["certState"] = cert_state
        if key_size_in_bits is not UNSET:
            field_dict["keySizeInBits"] = key_size_in_bits
        if key_type is not UNSET:
            field_dict["keyType"] = key_type
        if requester_id is not UNSET:
            field_dict["requesterId"] = requester_id
        if issued_ou is not UNSET:
            field_dict["issuedOU"] = issued_ou
        if issued_email is not UNSET:
            field_dict["issuedEmail"] = issued_email
        if key_usage is not UNSET:
            field_dict["keyUsage"] = key_usage
        if signing_algorithm is not UNSET:
            field_dict["signingAlgorithm"] = signing_algorithm
        if cert_state_string is not UNSET:
            field_dict["certStateString"] = cert_state_string
        if key_type_string is not UNSET:
            field_dict["keyTypeString"] = key_type_string
        if revocation_eff_date is not UNSET:
            field_dict["revocationEffDate"] = revocation_eff_date
        if revocation_reason is not UNSET:
            field_dict["revocationReason"] = revocation_reason
        if revocation_comment is not UNSET:
            field_dict["revocationComment"] = revocation_comment
        if certificate_authority_id is not UNSET:
            field_dict["certificateAuthorityId"] = certificate_authority_id
        if certificate_authority_name is not UNSET:
            field_dict["certificateAuthorityName"] = certificate_authority_name
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if archived_key is not UNSET:
            field_dict["archivedKey"] = archived_key
        if has_private_key is not UNSET:
            field_dict["hasPrivateKey"] = has_private_key
        if principal_name is not UNSET:
            field_dict["principalName"] = principal_name
        if cert_request_id is not UNSET:
            field_dict["certRequestId"] = cert_request_id
        if requester_name is not UNSET:
            field_dict["requesterName"] = requester_name
        if content_bytes is not UNSET:
            field_dict["contentBytes"] = content_bytes
        if extended_key_usages is not UNSET:
            field_dict["extendedKeyUsages"] = extended_key_usages
        if subject_alt_name_elements is not UNSET:
            field_dict["subjectAltNameElements"] = subject_alt_name_elements
        if crl_distribution_points is not UNSET:
            field_dict["crlDistributionPoints"] = crl_distribution_points
        if locations_count is not UNSET:
            field_dict["locationsCount"] = locations_count
        if ssl_locations is not UNSET:
            field_dict["sslLocations"] = ssl_locations
        if locations is not UNSET:
            field_dict["locations"] = locations
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if certificate_key_id is not UNSET:
            field_dict["certificateKeyId"] = certificate_key_id
        if ca_row_index is not UNSET:
            field_dict["caRowIndex"] = ca_row_index
        if ca_record_id is not UNSET:
            field_dict["caRecordId"] = ca_record_id
        if detailed_key_usage is not UNSET:
            field_dict["detailedKeyUsage"] = detailed_key_usage
        if key_recoverable is not UNSET:
            field_dict["keyRecoverable"] = key_recoverable
        if curve is not UNSET:
            field_dict["curve"] = curve

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_retrieval_response_certificate_store_inventory_item_model import (
            CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel,
        )
        from ..models.csscms_data_model_models_certificate_retrieval_response_certificate_store_location_detail_model import (
            CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel,
        )
        from ..models.csscms_data_model_models_certificate_retrieval_response_crl_distribution_point_model import (
            CSSCMSDataModelModelsCertificateRetrievalResponseCRLDistributionPointModel,
        )
        from ..models.csscms_data_model_models_certificate_retrieval_response_detailed_key_usage_model import (
            CSSCMSDataModelModelsCertificateRetrievalResponseDetailedKeyUsageModel,
        )
        from ..models.csscms_data_model_models_certificate_retrieval_response_extended_key_usage_model import (
            CSSCMSDataModelModelsCertificateRetrievalResponseExtendedKeyUsageModel,
        )
        from ..models.csscms_data_model_models_certificate_retrieval_response_location_count_model import (
            CSSCMSDataModelModelsCertificateRetrievalResponseLocationCountModel,
        )
        from ..models.csscms_data_model_models_certificate_retrieval_response_metadata import (
            CSSCMSDataModelModelsCertificateRetrievalResponseMetadata,
        )
        from ..models.csscms_data_model_models_certificate_retrieval_response_subject_alternative_name_model import (
            CSSCMSDataModelModelsCertificateRetrievalResponseSubjectAlternativeNameModel,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        thumbprint = d.pop("thumbprint", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        issued_dn = d.pop("issuedDN", UNSET)

        issued_cn = d.pop("issuedCN", UNSET)

        _import_date = d.pop("importDate", UNSET)
        import_date: Union[Unset, datetime.datetime]
        if isinstance(_import_date, Unset):
            import_date = UNSET
        else:
            import_date = isoparse(_import_date)

        _not_before = d.pop("notBefore", UNSET)
        not_before: Union[Unset, datetime.datetime]
        if isinstance(_not_before, Unset):
            not_before = UNSET
        else:
            not_before = isoparse(_not_before)

        _not_after = d.pop("notAfter", UNSET)
        not_after: Union[Unset, datetime.datetime]
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = isoparse(_not_after)

        issuer_dn = d.pop("issuerDN", UNSET)

        principal_id = d.pop("principalId", UNSET)

        template_id = d.pop("templateId", UNSET)

        _cert_state = d.pop("certState", UNSET)
        cert_state: Union[Unset, KeyfactorPKIEnumsCertificateState]
        if isinstance(_cert_state, Unset):
            cert_state = UNSET
        else:
            cert_state = KeyfactorPKIEnumsCertificateState(_cert_state)

        key_size_in_bits = d.pop("keySizeInBits", UNSET)

        _key_type = d.pop("keyType", UNSET)
        key_type: Union[Unset, CSSCMSCoreEnumsEncryptionKeyType]
        if isinstance(_key_type, Unset):
            key_type = UNSET
        else:
            key_type = CSSCMSCoreEnumsEncryptionKeyType(_key_type)

        requester_id = d.pop("requesterId", UNSET)

        issued_ou = d.pop("issuedOU", UNSET)

        issued_email = d.pop("issuedEmail", UNSET)

        key_usage = d.pop("keyUsage", UNSET)

        signing_algorithm = d.pop("signingAlgorithm", UNSET)

        cert_state_string = d.pop("certStateString", UNSET)

        key_type_string = d.pop("keyTypeString", UNSET)

        _revocation_eff_date = d.pop("revocationEffDate", UNSET)
        revocation_eff_date: Union[Unset, None, datetime.datetime]
        if _revocation_eff_date is None:
            revocation_eff_date = None
        elif isinstance(_revocation_eff_date, Unset):
            revocation_eff_date = UNSET
        else:
            revocation_eff_date = isoparse(_revocation_eff_date)

        _revocation_reason = d.pop("revocationReason", UNSET)
        revocation_reason: Union[Unset, KeyfactorPKIEnumsRevokeCode]
        if isinstance(_revocation_reason, Unset) or _revocation_reason is None:
            revocation_reason = UNSET
        else:
            revocation_reason = KeyfactorPKIEnumsRevokeCode(_revocation_reason)

        revocation_comment = d.pop("revocationComment", UNSET)

        certificate_authority_id = d.pop("certificateAuthorityId", UNSET)

        certificate_authority_name = d.pop("certificateAuthorityName", UNSET)

        template_name = d.pop("templateName", UNSET)

        archived_key = d.pop("archivedKey", UNSET)

        has_private_key = d.pop("hasPrivateKey", UNSET)

        principal_name = d.pop("principalName", UNSET)

        cert_request_id = d.pop("certRequestId", UNSET)

        requester_name = d.pop("requesterName", UNSET)

        content_bytes = d.pop("contentBytes", UNSET)

        extended_key_usages = []
        _extended_key_usages = d.pop("extendedKeyUsages", UNSET)
        for extended_key_usages_item_data in _extended_key_usages or []:
            extended_key_usages_item = CSSCMSDataModelModelsCertificateRetrievalResponseExtendedKeyUsageModel.from_dict(
                extended_key_usages_item_data
            )

            extended_key_usages.append(extended_key_usages_item)

        subject_alt_name_elements = []
        _subject_alt_name_elements = d.pop("subjectAltNameElements", UNSET)
        for subject_alt_name_elements_item_data in _subject_alt_name_elements or []:
            subject_alt_name_elements_item = (
                CSSCMSDataModelModelsCertificateRetrievalResponseSubjectAlternativeNameModel.from_dict(
                    subject_alt_name_elements_item_data
                )
            )

            subject_alt_name_elements.append(subject_alt_name_elements_item)

        crl_distribution_points = []
        _crl_distribution_points = d.pop("crlDistributionPoints", UNSET)
        for crl_distribution_points_item_data in _crl_distribution_points or []:
            crl_distribution_points_item = (
                CSSCMSDataModelModelsCertificateRetrievalResponseCRLDistributionPointModel.from_dict(
                    crl_distribution_points_item_data
                )
            )

            crl_distribution_points.append(crl_distribution_points_item)

        locations_count = []
        _locations_count = d.pop("locationsCount", UNSET)
        for locations_count_item_data in _locations_count or []:
            locations_count_item = CSSCMSDataModelModelsCertificateRetrievalResponseLocationCountModel.from_dict(
                locations_count_item_data
            )

            locations_count.append(locations_count_item)

        ssl_locations = []
        _ssl_locations = d.pop("sslLocations", UNSET)
        for ssl_locations_item_data in _ssl_locations or []:
            ssl_locations_item = (
                CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel.from_dict(
                    ssl_locations_item_data
                )
            )

            ssl_locations.append(ssl_locations_item)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = (
                CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel.from_dict(
                    locations_item_data
                )
            )

            locations.append(locations_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CSSCMSDataModelModelsCertificateRetrievalResponseMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CSSCMSDataModelModelsCertificateRetrievalResponseMetadata.from_dict(_metadata)

        certificate_key_id = d.pop("certificateKeyId", UNSET)

        ca_row_index = d.pop("caRowIndex", UNSET)

        ca_record_id = d.pop("caRecordId", UNSET)

        _detailed_key_usage = d.pop("detailedKeyUsage", UNSET)
        detailed_key_usage: Union[Unset, CSSCMSDataModelModelsCertificateRetrievalResponseDetailedKeyUsageModel]
        if isinstance(_detailed_key_usage, Unset):
            detailed_key_usage = UNSET
        else:
            detailed_key_usage = CSSCMSDataModelModelsCertificateRetrievalResponseDetailedKeyUsageModel.from_dict(
                _detailed_key_usage
            )

        key_recoverable = d.pop("keyRecoverable", UNSET)

        curve = d.pop("curve", UNSET)

        csscms_data_model_models_certificate_retrieval_response = cls(
            id=id,
            thumbprint=thumbprint,
            serial_number=serial_number,
            issued_dn=issued_dn,
            issued_cn=issued_cn,
            import_date=import_date,
            not_before=not_before,
            not_after=not_after,
            issuer_dn=issuer_dn,
            principal_id=principal_id,
            template_id=template_id,
            cert_state=cert_state,
            key_size_in_bits=key_size_in_bits,
            key_type=key_type,
            requester_id=requester_id,
            issued_ou=issued_ou,
            issued_email=issued_email,
            key_usage=key_usage,
            signing_algorithm=signing_algorithm,
            cert_state_string=cert_state_string,
            key_type_string=key_type_string,
            revocation_eff_date=revocation_eff_date,
            revocation_reason=revocation_reason,
            revocation_comment=revocation_comment,
            certificate_authority_id=certificate_authority_id,
            certificate_authority_name=certificate_authority_name,
            template_name=template_name,
            archived_key=archived_key,
            has_private_key=has_private_key,
            principal_name=principal_name,
            cert_request_id=cert_request_id,
            requester_name=requester_name,
            content_bytes=content_bytes,
            extended_key_usages=extended_key_usages,
            subject_alt_name_elements=subject_alt_name_elements,
            crl_distribution_points=crl_distribution_points,
            locations_count=locations_count,
            ssl_locations=ssl_locations,
            locations=locations,
            metadata=metadata,
            certificate_key_id=certificate_key_id,
            ca_row_index=ca_row_index,
            ca_record_id=ca_record_id,
            detailed_key_usage=detailed_key_usage,
            key_recoverable=key_recoverable,
            curve=curve,
        )

        return csscms_data_model_models_certificate_retrieval_response
