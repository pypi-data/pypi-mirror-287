from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_certificate_import_job_status import (
    CSSCMSDataModelEnumsCertificateImportJobStatus,
)
from ..models.csscms_data_model_enums_certificate_saved_state import CSSCMSDataModelEnumsCertificateSavedState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_invalid_keystore import CSSCMSDataModelModelsInvalidKeystore


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateImportResponseModel")


@_attrs_define
class CSSCMSDataModelModelsCertificateImportResponseModel:
    """
    Attributes:
        import_status (Union[Unset, CSSCMSDataModelEnumsCertificateSavedState]):
        job_status (Union[Unset, CSSCMSDataModelEnumsCertificateImportJobStatus]):
        invalid_keystores (Union[Unset, None, List['CSSCMSDataModelModelsInvalidKeystore']]):
        thumbprint (Union[Unset, None, str]):
    """

    import_status: Union[Unset, CSSCMSDataModelEnumsCertificateSavedState] = UNSET
    job_status: Union[Unset, CSSCMSDataModelEnumsCertificateImportJobStatus] = UNSET
    invalid_keystores: Union[Unset, None, List["CSSCMSDataModelModelsInvalidKeystore"]] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        import_status: Union[Unset, int] = UNSET
        if not isinstance(self.import_status, Unset):
            import_status = self.import_status.value

        job_status: Union[Unset, int] = UNSET
        if not isinstance(self.job_status, Unset):
            job_status = self.job_status.value

        invalid_keystores: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invalid_keystores, Unset):
            if self.invalid_keystores is None:
                invalid_keystores = None
            else:
                invalid_keystores = []
                for invalid_keystores_item_data in self.invalid_keystores:
                    invalid_keystores_item = invalid_keystores_item_data.to_dict()

                    invalid_keystores.append(invalid_keystores_item)

        thumbprint = self.thumbprint

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if import_status is not UNSET:
            field_dict["importStatus"] = import_status
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status
        if invalid_keystores is not UNSET:
            field_dict["invalidKeystores"] = invalid_keystores
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_invalid_keystore import CSSCMSDataModelModelsInvalidKeystore

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        _import_status = d.pop("importStatus", UNSET)
        import_status: Union[Unset, CSSCMSDataModelEnumsCertificateSavedState]
        if isinstance(_import_status, Unset):
            import_status = UNSET
        else:
            import_status = CSSCMSDataModelEnumsCertificateSavedState(_import_status)

        _job_status = d.pop("jobStatus", UNSET)
        job_status: Union[Unset, CSSCMSDataModelEnumsCertificateImportJobStatus]
        if isinstance(_job_status, Unset):
            job_status = UNSET
        else:
            job_status = CSSCMSDataModelEnumsCertificateImportJobStatus(_job_status)

        invalid_keystores = []
        _invalid_keystores = d.pop("invalidKeystores", UNSET)
        for invalid_keystores_item_data in _invalid_keystores or []:
            invalid_keystores_item = CSSCMSDataModelModelsInvalidKeystore.from_dict(invalid_keystores_item_data)

            invalid_keystores.append(invalid_keystores_item)

        thumbprint = d.pop("thumbprint", UNSET)

        csscms_data_model_models_certificate_import_response_model = cls(
            import_status=import_status,
            job_status=job_status,
            invalid_keystores=invalid_keystores,
            thumbprint=thumbprint,
        )

        return csscms_data_model_models_certificate_import_response_model
