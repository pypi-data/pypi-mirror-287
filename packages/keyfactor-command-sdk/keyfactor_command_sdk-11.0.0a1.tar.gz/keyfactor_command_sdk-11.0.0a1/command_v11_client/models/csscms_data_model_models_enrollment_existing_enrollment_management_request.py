import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentExistingEnrollmentManagementRequest")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentExistingEnrollmentManagementRequest:
    """
    Attributes:
        certificate_id (Union[Unset, int]):
        request_id (Union[Unset, int]):
        password (Union[Unset, None, str]):
        job_time (Union[Unset, datetime.datetime]):
        existing_certificate_id (Union[Unset, int]):
    """

    certificate_id: Union[Unset, int] = UNSET
    request_id: Union[Unset, int] = UNSET
    password: Union[Unset, None, str] = UNSET
    job_time: Union[Unset, datetime.datetime] = UNSET
    existing_certificate_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate_id = self.certificate_id
        request_id = self.request_id
        password = self.password
        job_time: Union[Unset, str] = UNSET
        if not isinstance(self.job_time, Unset):
            job_time = self.job_time.isoformat()[:-6]+'Z'

        existing_certificate_id = self.existing_certificate_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if certificate_id is not UNSET:
            field_dict["certificateId"] = certificate_id
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if password is not UNSET:
            field_dict["password"] = password
        if job_time is not UNSET:
            field_dict["jobTime"] = job_time
        if existing_certificate_id is not UNSET:
            field_dict["existingCertificateId"] = existing_certificate_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        certificate_id = d.pop("certificateId", UNSET)

        request_id = d.pop("requestId", UNSET)

        password = d.pop("password", UNSET)

        _job_time = d.pop("jobTime", UNSET)
        job_time: Union[Unset, datetime.datetime]
        if isinstance(_job_time, Unset):
            job_time = UNSET
        else:
            job_time = isoparse(_job_time)

        existing_certificate_id = d.pop("existingCertificateId", UNSET)

        csscms_data_model_models_enrollment_existing_enrollment_management_request = cls(
            certificate_id=certificate_id,
            request_id=request_id,
            password=password,
            job_time=job_time,
            existing_certificate_id=existing_certificate_id,
        )

        return csscms_data_model_models_enrollment_existing_enrollment_management_request
