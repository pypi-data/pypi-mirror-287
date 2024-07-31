import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.csscms_core_enums_agent_platform_type import CSSCMSCoreEnumsAgentPlatformType
from ..models.csscms_core_enums_agent_status_type import CSSCMSCoreEnumsAgentStatusType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorsAgentResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorsAgentResponse:
    """
    Attributes:
        agent_id (Union[Unset, str]):
        client_machine (Union[Unset, None, str]):
        username (Union[Unset, None, str]):
        agent_platform (Union[Unset, CSSCMSCoreEnumsAgentPlatformType]):
        version (Union[Unset, None, str]):
        status (Union[Unset, CSSCMSCoreEnumsAgentStatusType]):
        last_seen (Union[Unset, datetime.datetime]):
        capabilities (Union[Unset, None, List[str]]):
        blueprint (Union[Unset, None, str]):
        thumbprint (Union[Unset, None, str]):
        legacy_thumbprint (Union[Unset, None, str]):
        auth_certificate_reenrollment (Union[Unset, None, str]):
        last_thumbprint_used (Union[Unset, None, str]):
        last_error_code (Union[Unset, None, int]):
        last_error_message (Union[Unset, None, str]):
    """

    agent_id: Union[Unset, str] = UNSET
    client_machine: Union[Unset, None, str] = UNSET
    username: Union[Unset, None, str] = UNSET
    agent_platform: Union[Unset, CSSCMSCoreEnumsAgentPlatformType] = UNSET
    version: Union[Unset, None, str] = UNSET
    status: Union[Unset, CSSCMSCoreEnumsAgentStatusType] = UNSET
    last_seen: Union[Unset, datetime.datetime] = UNSET
    capabilities: Union[Unset, None, List[str]] = UNSET
    blueprint: Union[Unset, None, str] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET
    legacy_thumbprint: Union[Unset, None, str] = UNSET
    auth_certificate_reenrollment: Union[Unset, None, str] = UNSET
    last_thumbprint_used: Union[Unset, None, str] = UNSET
    last_error_code: Union[Unset, None, int] = UNSET
    last_error_message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id
        client_machine = self.client_machine
        username = self.username
        agent_platform: Union[Unset, int] = UNSET
        if not isinstance(self.agent_platform, Unset):
            agent_platform = self.agent_platform.value

        version = self.version
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_seen: Union[Unset, str] = UNSET
        if not isinstance(self.last_seen, Unset):
            last_seen = self.last_seen.isoformat()[:-6]+'Z'

        capabilities: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.capabilities, Unset):
            if self.capabilities is None:
                capabilities = None
            else:
                capabilities = self.capabilities

        blueprint = self.blueprint
        thumbprint = self.thumbprint
        legacy_thumbprint = self.legacy_thumbprint
        auth_certificate_reenrollment = self.auth_certificate_reenrollment
        last_thumbprint_used = self.last_thumbprint_used
        last_error_code = self.last_error_code
        last_error_message = self.last_error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine
        if username is not UNSET:
            field_dict["username"] = username
        if agent_platform is not UNSET:
            field_dict["agentPlatform"] = agent_platform
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if blueprint is not UNSET:
            field_dict["blueprint"] = blueprint
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if legacy_thumbprint is not UNSET:
            field_dict["legacyThumbprint"] = legacy_thumbprint
        if auth_certificate_reenrollment is not UNSET:
            field_dict["authCertificateReenrollment"] = auth_certificate_reenrollment
        if last_thumbprint_used is not UNSET:
            field_dict["lastThumbprintUsed"] = last_thumbprint_used
        if last_error_code is not UNSET:
            field_dict["lastErrorCode"] = last_error_code
        if last_error_message is not UNSET:
            field_dict["lastErrorMessage"] = last_error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        agent_id = d.pop("agentId", UNSET)

        client_machine = d.pop("clientMachine", UNSET)

        username = d.pop("username", UNSET)

        _agent_platform = d.pop("agentPlatform", UNSET)
        agent_platform: Union[Unset, CSSCMSCoreEnumsAgentPlatformType]
        if isinstance(_agent_platform, Unset):
            agent_platform = UNSET
        else:
            agent_platform = CSSCMSCoreEnumsAgentPlatformType(_agent_platform)

        version = d.pop("version", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CSSCMSCoreEnumsAgentStatusType]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CSSCMSCoreEnumsAgentStatusType(_status)

        _last_seen = d.pop("lastSeen", UNSET)
        last_seen: Union[Unset, datetime.datetime]
        if isinstance(_last_seen, Unset):
            last_seen = UNSET
        else:
            last_seen = isoparse(_last_seen)

        capabilities = cast(List[str], d.pop("capabilities", UNSET))

        blueprint = d.pop("blueprint", UNSET)

        thumbprint = d.pop("thumbprint", UNSET)

        legacy_thumbprint = d.pop("legacyThumbprint", UNSET)

        auth_certificate_reenrollment = d.pop("authCertificateReenrollment", UNSET)

        last_thumbprint_used = d.pop("lastThumbprintUsed", UNSET)

        last_error_code = d.pop("lastErrorCode", UNSET)

        last_error_message = d.pop("lastErrorMessage", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrators_agent_response = cls(
            agent_id=agent_id,
            client_machine=client_machine,
            username=username,
            agent_platform=agent_platform,
            version=version,
            status=status,
            last_seen=last_seen,
            capabilities=capabilities,
            blueprint=blueprint,
            thumbprint=thumbprint,
            legacy_thumbprint=legacy_thumbprint,
            auth_certificate_reenrollment=auth_certificate_reenrollment,
            last_thumbprint_used=last_thumbprint_used,
            last_error_code=last_error_code,
            last_error_message=last_error_message,
        )

        return keyfactor_web_keyfactor_api_models_orchestrators_agent_response
