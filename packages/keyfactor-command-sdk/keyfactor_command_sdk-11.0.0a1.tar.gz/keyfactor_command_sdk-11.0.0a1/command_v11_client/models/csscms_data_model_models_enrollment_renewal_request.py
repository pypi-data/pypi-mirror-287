import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentRenewalRequest")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentRenewalRequest:
    """
    Attributes:
        certificate_id (Union[Unset, None, int]):
        thumbprint (Union[Unset, None, str]):
        certificate_authority (Union[Unset, None, str]):
        template (Union[Unset, None, str]):
        timestamp (Union[Unset, datetime.datetime]):
    """

    certificate_id: Union[Unset, None, int] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET
    certificate_authority: Union[Unset, None, str] = UNSET
    template: Union[Unset, None, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate_id = self.certificate_id
        thumbprint = self.thumbprint
        certificate_authority = self.certificate_authority
        template = self.template
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()[:-6]+'Z'

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if certificate_id is not UNSET:
            field_dict["certificateId"] = certificate_id
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if certificate_authority is not UNSET:
            field_dict["certificateAuthority"] = certificate_authority
        if template is not UNSET:
            field_dict["template"] = template
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        certificate_id = d.pop("certificateId", UNSET)

        thumbprint = d.pop("thumbprint", UNSET)

        certificate_authority = d.pop("certificateAuthority", UNSET)

        template = d.pop("template", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        csscms_data_model_models_enrollment_renewal_request = cls(
            certificate_id=certificate_id,
            thumbprint=thumbprint,
            certificate_authority=certificate_authority,
            template=template,
            timestamp=timestamp,
        )

        return csscms_data_model_models_enrollment_renewal_request
