import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsPendingCSRResponse")


@_attrs_define
class CSSCMSDataModelModelsPendingCSRResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        csr (Union[Unset, None, str]):
        request_time (Union[Unset, datetime.datetime]):
        subject (Union[Unset, None, List[str]]):
    """

    id: Union[Unset, int] = UNSET
    csr: Union[Unset, None, str] = UNSET
    request_time: Union[Unset, datetime.datetime] = UNSET
    subject: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        csr = self.csr
        request_time: Union[Unset, str] = UNSET
        if not isinstance(self.request_time, Unset):
            request_time = self.request_time.isoformat()[:-6]+'Z'

        subject: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.subject, Unset):
            if self.subject is None:
                subject = None
            else:
                subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if csr is not UNSET:
            field_dict["csr"] = csr
        if request_time is not UNSET:
            field_dict["requestTime"] = request_time
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        csr = d.pop("csr", UNSET)

        _request_time = d.pop("requestTime", UNSET)
        request_time: Union[Unset, datetime.datetime]
        if isinstance(_request_time, Unset):
            request_time = UNSET
        else:
            request_time = isoparse(_request_time)

        subject = cast(List[str], d.pop("subject", UNSET))

        csscms_data_model_models_pending_csr_response = cls(
            id=id,
            csr=csr,
            request_time=request_time,
            subject=subject,
        )

        return csscms_data_model_models_pending_csr_response
