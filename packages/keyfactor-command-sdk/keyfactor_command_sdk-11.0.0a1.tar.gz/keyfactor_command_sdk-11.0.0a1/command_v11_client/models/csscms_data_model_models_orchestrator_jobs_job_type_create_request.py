from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_orchestrator_jobs_job_type_field_request import (
        CSSCMSDataModelModelsOrchestratorJobsJobTypeFieldRequest,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsOrchestratorJobsJobTypeCreateRequest")


@_attrs_define
class CSSCMSDataModelModelsOrchestratorJobsJobTypeCreateRequest:
    """
    Attributes:
        job_type_name (str):
        description (Union[Unset, None, str]):
        job_type_fields (Union[Unset, None, List['CSSCMSDataModelModelsOrchestratorJobsJobTypeFieldRequest']]):
    """

    job_type_name: str
    description: Union[Unset, None, str] = UNSET
    job_type_fields: Union[Unset, None, List["CSSCMSDataModelModelsOrchestratorJobsJobTypeFieldRequest"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        job_type_name = self.job_type_name
        description = self.description
        job_type_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_type_fields, Unset):
            if self.job_type_fields is None:
                job_type_fields = None
            else:
                job_type_fields = []
                for job_type_fields_item_data in self.job_type_fields:
                    job_type_fields_item = job_type_fields_item_data.to_dict()

                    job_type_fields.append(job_type_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "jobTypeName": job_type_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if job_type_fields is not UNSET:
            field_dict["jobTypeFields"] = job_type_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_orchestrator_jobs_job_type_field_request import (
            CSSCMSDataModelModelsOrchestratorJobsJobTypeFieldRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        job_type_name = d.pop("jobTypeName")

        description = d.pop("description", UNSET)

        job_type_fields = []
        _job_type_fields = d.pop("jobTypeFields", UNSET)
        for job_type_fields_item_data in _job_type_fields or []:
            job_type_fields_item = CSSCMSDataModelModelsOrchestratorJobsJobTypeFieldRequest.from_dict(
                job_type_fields_item_data
            )

            job_type_fields.append(job_type_fields_item)

        csscms_data_model_models_orchestrator_jobs_job_type_create_request = cls(
            job_type_name=job_type_name,
            description=description,
            job_type_fields=job_type_fields,
        )

        return csscms_data_model_models_orchestrator_jobs_job_type_create_request
