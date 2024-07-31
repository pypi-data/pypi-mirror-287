from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_certificate_stores_reenrollment_request_job_properties import (
        KeyfactorWebKeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateStoresReenrollmentRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateStoresReenrollmentRequest:
    """
    Attributes:
        keystore_id (Union[Unset, str]):
        subject_name (Union[Unset, None, str]):
        agent_guid (Union[Unset, str]):
        alias (Union[Unset, None, str]):
        job_properties (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties]):
        certificate_authority (Union[Unset, None, str]):
        certificate_template (Union[Unset, None, str]):
    """

    keystore_id: Union[Unset, str] = UNSET
    subject_name: Union[Unset, None, str] = UNSET
    agent_guid: Union[Unset, str] = UNSET
    alias: Union[Unset, None, str] = UNSET
    job_properties: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties"
    ] = UNSET
    certificate_authority: Union[Unset, None, str] = UNSET
    certificate_template: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keystore_id = self.keystore_id
        subject_name = self.subject_name
        agent_guid = self.agent_guid
        alias = self.alias
        job_properties: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.job_properties, Unset):
            job_properties = self.job_properties.to_dict() if self.job_properties else None

        certificate_authority = self.certificate_authority
        certificate_template = self.certificate_template

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keystore_id is not UNSET:
            field_dict["keystoreId"] = keystore_id
        if subject_name is not UNSET:
            field_dict["subjectName"] = subject_name
        if agent_guid is not UNSET:
            field_dict["agentGuid"] = agent_guid
        if alias is not UNSET:
            field_dict["alias"] = alias
        if job_properties is not UNSET:
            field_dict["jobProperties"] = job_properties
        if certificate_authority is not UNSET:
            field_dict["certificateAuthority"] = certificate_authority
        if certificate_template is not UNSET:
            field_dict["certificateTemplate"] = certificate_template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_certificate_stores_reenrollment_request_job_properties import (
            KeyfactorWebKeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        keystore_id = d.pop("keystoreId", UNSET)

        subject_name = d.pop("subjectName", UNSET)

        agent_guid = d.pop("agentGuid", UNSET)

        alias = d.pop("alias", UNSET)

        _job_properties = d.pop("jobProperties", UNSET)
        job_properties: Union[
            Unset, None, KeyfactorWebKeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties
        ]
        if _job_properties is None:
            job_properties = None
        elif isinstance(_job_properties, Unset):
            job_properties = UNSET
        else:
            job_properties = KeyfactorWebKeyfactorApiModelsCertificateStoresReenrollmentRequestJobProperties.from_dict(
                _job_properties
            )

        certificate_authority = d.pop("certificateAuthority", UNSET)

        certificate_template = d.pop("certificateTemplate", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_stores_reenrollment_request = cls(
            keystore_id=keystore_id,
            subject_name=subject_name,
            agent_guid=agent_guid,
            alias=alias,
            job_properties=job_properties,
            certificate_authority=certificate_authority,
            certificate_template=certificate_template,
        )

        return keyfactor_web_keyfactor_api_models_certificate_stores_reenrollment_request
