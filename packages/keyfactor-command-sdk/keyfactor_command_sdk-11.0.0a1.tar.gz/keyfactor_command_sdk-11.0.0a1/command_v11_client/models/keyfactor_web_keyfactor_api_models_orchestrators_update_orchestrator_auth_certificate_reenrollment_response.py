from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.csscms_core_enums_orchestrator_auth_certificate_reenrollment import (
    CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentResponse"
)


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentResponse:
    """
    Attributes:
        failed_orchestrator_ids (Union[Unset, None, List[str]]):
        status (Union[Unset, CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment]):
    """

    failed_orchestrator_ids: Union[Unset, None, List[str]] = UNSET
    status: Union[Unset, CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        failed_orchestrator_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.failed_orchestrator_ids, Unset):
            if self.failed_orchestrator_ids is None:
                failed_orchestrator_ids = None
            else:
                failed_orchestrator_ids = self.failed_orchestrator_ids

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if failed_orchestrator_ids is not UNSET:
            field_dict["failedOrchestratorIds"] = failed_orchestrator_ids
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        failed_orchestrator_ids = cast(List[str], d.pop("failedOrchestratorIds", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment(_status)

        keyfactor_web_keyfactor_api_models_orchestrators_update_orchestrator_auth_certificate_reenrollment_response = (
            cls(
                failed_orchestrator_ids=failed_orchestrator_ids,
                status=status,
            )
        )

        return (
            keyfactor_web_keyfactor_api_models_orchestrators_update_orchestrator_auth_certificate_reenrollment_response
        )
