from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_workflow_processed_certificate_request import (
        CSSCMSDataModelModelsWorkflowProcessedCertificateRequest,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsWorkflowApproveDenyResult")


@_attrs_define
class CSSCMSDataModelModelsWorkflowApproveDenyResult:
    """
    Attributes:
        failures (Union[Unset, None, List['CSSCMSDataModelModelsWorkflowProcessedCertificateRequest']]):
        denials (Union[Unset, None, List['CSSCMSDataModelModelsWorkflowProcessedCertificateRequest']]):
        successes (Union[Unset, None, List['CSSCMSDataModelModelsWorkflowProcessedCertificateRequest']]):
    """

    failures: Union[Unset, None, List["CSSCMSDataModelModelsWorkflowProcessedCertificateRequest"]] = UNSET
    denials: Union[Unset, None, List["CSSCMSDataModelModelsWorkflowProcessedCertificateRequest"]] = UNSET
    successes: Union[Unset, None, List["CSSCMSDataModelModelsWorkflowProcessedCertificateRequest"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        failures: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.failures, Unset):
            if self.failures is None:
                failures = None
            else:
                failures = []
                for failures_item_data in self.failures:
                    failures_item = failures_item_data.to_dict()

                    failures.append(failures_item)

        denials: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.denials, Unset):
            if self.denials is None:
                denials = None
            else:
                denials = []
                for denials_item_data in self.denials:
                    denials_item = denials_item_data.to_dict()

                    denials.append(denials_item)

        successes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.successes, Unset):
            if self.successes is None:
                successes = None
            else:
                successes = []
                for successes_item_data in self.successes:
                    successes_item = successes_item_data.to_dict()

                    successes.append(successes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if failures is not UNSET:
            field_dict["failures"] = failures
        if denials is not UNSET:
            field_dict["denials"] = denials
        if successes is not UNSET:
            field_dict["successes"] = successes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_workflow_processed_certificate_request import (
            CSSCMSDataModelModelsWorkflowProcessedCertificateRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        failures = []
        _failures = d.pop("failures", UNSET)
        for failures_item_data in _failures or []:
            failures_item = CSSCMSDataModelModelsWorkflowProcessedCertificateRequest.from_dict(failures_item_data)

            failures.append(failures_item)

        denials = []
        _denials = d.pop("denials", UNSET)
        for denials_item_data in _denials or []:
            denials_item = CSSCMSDataModelModelsWorkflowProcessedCertificateRequest.from_dict(denials_item_data)

            denials.append(denials_item)

        successes = []
        _successes = d.pop("successes", UNSET)
        for successes_item_data in _successes or []:
            successes_item = CSSCMSDataModelModelsWorkflowProcessedCertificateRequest.from_dict(successes_item_data)

            successes.append(successes_item)

        csscms_data_model_models_workflow_approve_deny_result = cls(
            failures=failures,
            denials=denials,
            successes=successes,
        )

        return csscms_data_model_models_workflow_approve_deny_result
