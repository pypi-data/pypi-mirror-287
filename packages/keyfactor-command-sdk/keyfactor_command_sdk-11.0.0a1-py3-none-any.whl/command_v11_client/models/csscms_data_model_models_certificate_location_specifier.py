from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_location_specifier_job_fields import (
        CSSCMSDataModelModelsCertificateLocationSpecifierJobFields,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateLocationSpecifier")


@_attrs_define
class CSSCMSDataModelModelsCertificateLocationSpecifier:
    """
    Attributes:
        alias (Union[Unset, None, str]):
        certificate_store_id (Union[Unset, str]):
        job_fields (Union[Unset, None, CSSCMSDataModelModelsCertificateLocationSpecifierJobFields]):
    """

    alias: Union[Unset, None, str] = UNSET
    certificate_store_id: Union[Unset, str] = UNSET
    job_fields: Union[Unset, None, "CSSCMSDataModelModelsCertificateLocationSpecifierJobFields"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        alias = self.alias
        certificate_store_id = self.certificate_store_id
        job_fields: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.job_fields, Unset):
            job_fields = self.job_fields.to_dict() if self.job_fields else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if certificate_store_id is not UNSET:
            field_dict["certificateStoreId"] = certificate_store_id
        if job_fields is not UNSET:
            field_dict["jobFields"] = job_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_location_specifier_job_fields import (
            CSSCMSDataModelModelsCertificateLocationSpecifierJobFields,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        alias = d.pop("alias", UNSET)

        certificate_store_id = d.pop("certificateStoreId", UNSET)

        _job_fields = d.pop("jobFields", UNSET)
        job_fields: Union[Unset, None, CSSCMSDataModelModelsCertificateLocationSpecifierJobFields]
        if _job_fields is None:
            job_fields = None
        elif isinstance(_job_fields, Unset):
            job_fields = UNSET
        else:
            job_fields = CSSCMSDataModelModelsCertificateLocationSpecifierJobFields.from_dict(_job_fields)

        csscms_data_model_models_certificate_location_specifier = cls(
            alias=alias,
            certificate_store_id=certificate_store_id,
            job_fields=job_fields,
        )

        return csscms_data_model_models_certificate_location_specifier
