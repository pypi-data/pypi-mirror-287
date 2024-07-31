from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_store_entry_job_fields import (
        CSSCMSDataModelModelsCertificateStoreEntryJobFields,
    )
    from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoreEntry")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoreEntry:
    """
    Attributes:
        certificate_store_id (str):
        alias (Union[Unset, None, str]):
        job_fields (Union[Unset, None, CSSCMSDataModelModelsCertificateStoreEntryJobFields]):
        overwrite (Union[Unset, bool]):
        entry_password (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        pfx_password (Union[Unset, None, str]):
        include_private_key (Union[Unset, bool]):
    """

    certificate_store_id: str
    alias: Union[Unset, None, str] = UNSET
    job_fields: Union[Unset, None, "CSSCMSDataModelModelsCertificateStoreEntryJobFields"] = UNSET
    overwrite: Union[Unset, bool] = UNSET
    entry_password: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    pfx_password: Union[Unset, None, str] = UNSET
    include_private_key: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate_store_id = self.certificate_store_id
        alias = self.alias
        job_fields: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.job_fields, Unset):
            job_fields = self.job_fields.to_dict() if self.job_fields else None

        overwrite = self.overwrite
        entry_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entry_password, Unset):
            entry_password = self.entry_password.to_dict()

        pfx_password = self.pfx_password
        include_private_key = self.include_private_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "certificateStoreId": certificate_store_id,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if job_fields is not UNSET:
            field_dict["jobFields"] = job_fields
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if entry_password is not UNSET:
            field_dict["entryPassword"] = entry_password
        if pfx_password is not UNSET:
            field_dict["pfxPassword"] = pfx_password
        if include_private_key is not UNSET:
            field_dict["includePrivateKey"] = include_private_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_store_entry_job_fields import (
            CSSCMSDataModelModelsCertificateStoreEntryJobFields,
        )
        from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        certificate_store_id = d.pop("certificateStoreId")

        alias = d.pop("alias", UNSET)

        _job_fields = d.pop("jobFields", UNSET)
        job_fields: Union[Unset, None, CSSCMSDataModelModelsCertificateStoreEntryJobFields]
        if _job_fields is None:
            job_fields = None
        elif isinstance(_job_fields, Unset):
            job_fields = UNSET
        else:
            job_fields = CSSCMSDataModelModelsCertificateStoreEntryJobFields.from_dict(_job_fields)

        overwrite = d.pop("overwrite", UNSET)

        _entry_password = d.pop("entryPassword", UNSET)
        entry_password: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_entry_password, Unset):
            entry_password = UNSET
        else:
            entry_password = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_entry_password)

        pfx_password = d.pop("pfxPassword", UNSET)

        include_private_key = d.pop("includePrivateKey", UNSET)

        csscms_data_model_models_certificate_store_entry = cls(
            certificate_store_id=certificate_store_id,
            alias=alias,
            job_fields=job_fields,
            overwrite=overwrite,
            entry_password=entry_password,
            pfx_password=pfx_password,
            include_private_key=include_private_key,
        )

        return csscms_data_model_models_certificate_store_entry
