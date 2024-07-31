from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.csscms_core_enums_orchestrator_auth_certificate_reenrollment import (
    CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentRequest"
)


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorsUpdateOrchestratorAuthCertificateReenrollmentRequest:
    """
    Attributes:
        status (str):
        orchestrator_ids (Union[Unset, None, List[str]]):
        status_enum (Union[Unset, CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment]):
    """

    status: str
    orchestrator_ids: Union[Unset, None, List[str]] = UNSET
    status_enum: Union[Unset, CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        orchestrator_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.orchestrator_ids, Unset):
            if self.orchestrator_ids is None:
                orchestrator_ids = None
            else:
                orchestrator_ids = self.orchestrator_ids

        status_enum: Union[Unset, int] = UNSET
        if not isinstance(self.status_enum, Unset):
            status_enum = self.status_enum.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "status": status,
            }
        )
        if orchestrator_ids is not UNSET:
            field_dict["orchestratorIds"] = orchestrator_ids
        if status_enum is not UNSET:
            field_dict["statusEnum"] = status_enum

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        status = d.pop("status")

        orchestrator_ids = cast(List[str], d.pop("orchestratorIds", UNSET))

        _status_enum = d.pop("statusEnum", UNSET)
        status_enum: Union[Unset, CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment]
        if isinstance(_status_enum, Unset):
            status_enum = UNSET
        else:
            status_enum = CSSCMSCoreEnumsOrchestratorAuthCertificateReenrollment(_status_enum)

        keyfactor_web_keyfactor_api_models_orchestrators_update_orchestrator_auth_certificate_reenrollment_request = (
            cls(
                status=status,
                orchestrator_ids=orchestrator_ids,
                status_enum=status_enum,
            )
        )

        return (
            keyfactor_web_keyfactor_api_models_orchestrators_update_orchestrator_auth_certificate_reenrollment_request
        )
