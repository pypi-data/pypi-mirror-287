import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
    from ..models.keyfactor_web_keyfactor_api_models_orchestrators_agent_blueprint_stores_response import (
        KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintJobsResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintJobsResponse:
    """
    Attributes:
        agent_blueprint_job_id (Union[Unset, str]):
        agent_blueprint_store_id (Union[Unset, str]):
        agent_blueprint_id (Union[Unset, str]):
        job_type (Union[Unset, str]):
        job_type_name (Union[Unset, None, str]):
        operation_type (Union[Unset, None, int]):
        thumbprint (Union[Unset, None, str]):
        contents (Union[Unset, None, str]):
        alias (Union[Unset, None, str]):
        private_key_entry (Union[Unset, None, bool]):
        overwrite (Union[Unset, None, bool]):
        has_entry_password (Union[Unset, None, bool]):
        has_pfx_password (Union[Unset, None, bool]):
        request_timestamp (Union[Unset, None, datetime.datetime]):
        keyfactor_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        subject (Union[Unset, None, str]):
        directories (Union[Unset, None, str]):
        ignored_directories (Union[Unset, None, str]):
        sym_links (Union[Unset, None, bool]):
        compatibility (Union[Unset, None, bool]):
        file_extensions (Union[Unset, None, str]):
        file_name_patterns (Union[Unset, None, str]):
        agent_blueprint_stores (Union[Unset, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse]):
    """

    agent_blueprint_job_id: Union[Unset, str] = UNSET
    agent_blueprint_store_id: Union[Unset, str] = UNSET
    agent_blueprint_id: Union[Unset, str] = UNSET
    job_type: Union[Unset, str] = UNSET
    job_type_name: Union[Unset, None, str] = UNSET
    operation_type: Union[Unset, None, int] = UNSET
    thumbprint: Union[Unset, None, str] = UNSET
    contents: Union[Unset, None, str] = UNSET
    alias: Union[Unset, None, str] = UNSET
    private_key_entry: Union[Unset, None, bool] = UNSET
    overwrite: Union[Unset, None, bool] = UNSET
    has_entry_password: Union[Unset, None, bool] = UNSET
    has_pfx_password: Union[Unset, None, bool] = UNSET
    request_timestamp: Union[Unset, None, datetime.datetime] = UNSET
    keyfactor_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    subject: Union[Unset, None, str] = UNSET
    directories: Union[Unset, None, str] = UNSET
    ignored_directories: Union[Unset, None, str] = UNSET
    sym_links: Union[Unset, None, bool] = UNSET
    compatibility: Union[Unset, None, bool] = UNSET
    file_extensions: Union[Unset, None, str] = UNSET
    file_name_patterns: Union[Unset, None, str] = UNSET
    agent_blueprint_stores: Union[
        Unset, "KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse"
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_blueprint_job_id = self.agent_blueprint_job_id
        agent_blueprint_store_id = self.agent_blueprint_store_id
        agent_blueprint_id = self.agent_blueprint_id
        job_type = self.job_type
        job_type_name = self.job_type_name
        operation_type = self.operation_type
        thumbprint = self.thumbprint
        contents = self.contents
        alias = self.alias
        private_key_entry = self.private_key_entry
        overwrite = self.overwrite
        has_entry_password = self.has_entry_password
        has_pfx_password = self.has_pfx_password
        request_timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.request_timestamp, Unset):
            request_timestamp = self.request_timestamp.isoformat()[:-6]+'Z' if self.request_timestamp else None

        keyfactor_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.keyfactor_schedule, Unset):
            keyfactor_schedule = self.keyfactor_schedule.to_dict()

        subject = self.subject
        directories = self.directories
        ignored_directories = self.ignored_directories
        sym_links = self.sym_links
        compatibility = self.compatibility
        file_extensions = self.file_extensions
        file_name_patterns = self.file_name_patterns
        agent_blueprint_stores: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.agent_blueprint_stores, Unset):
            agent_blueprint_stores = self.agent_blueprint_stores.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agent_blueprint_job_id is not UNSET:
            field_dict["agentBlueprintJobId"] = agent_blueprint_job_id
        if agent_blueprint_store_id is not UNSET:
            field_dict["agentBlueprintStoreId"] = agent_blueprint_store_id
        if agent_blueprint_id is not UNSET:
            field_dict["agentBlueprintId"] = agent_blueprint_id
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if job_type_name is not UNSET:
            field_dict["jobTypeName"] = job_type_name
        if operation_type is not UNSET:
            field_dict["operationType"] = operation_type
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
        if contents is not UNSET:
            field_dict["contents"] = contents
        if alias is not UNSET:
            field_dict["alias"] = alias
        if private_key_entry is not UNSET:
            field_dict["privateKeyEntry"] = private_key_entry
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if has_entry_password is not UNSET:
            field_dict["hasEntryPassword"] = has_entry_password
        if has_pfx_password is not UNSET:
            field_dict["hasPfxPassword"] = has_pfx_password
        if request_timestamp is not UNSET:
            field_dict["requestTimestamp"] = request_timestamp
        if keyfactor_schedule is not UNSET:
            field_dict["keyfactorSchedule"] = keyfactor_schedule
        if subject is not UNSET:
            field_dict["subject"] = subject
        if directories is not UNSET:
            field_dict["directories"] = directories
        if ignored_directories is not UNSET:
            field_dict["ignoredDirectories"] = ignored_directories
        if sym_links is not UNSET:
            field_dict["symLinks"] = sym_links
        if compatibility is not UNSET:
            field_dict["compatibility"] = compatibility
        if file_extensions is not UNSET:
            field_dict["fileExtensions"] = file_extensions
        if file_name_patterns is not UNSET:
            field_dict["fileNamePatterns"] = file_name_patterns
        if agent_blueprint_stores is not UNSET:
            field_dict["agentBlueprintStores"] = agent_blueprint_stores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule
        from ..models.keyfactor_web_keyfactor_api_models_orchestrators_agent_blueprint_stores_response import (
            KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        agent_blueprint_job_id = d.pop("agentBlueprintJobId", UNSET)

        agent_blueprint_store_id = d.pop("agentBlueprintStoreId", UNSET)

        agent_blueprint_id = d.pop("agentBlueprintId", UNSET)

        job_type = d.pop("jobType", UNSET)

        job_type_name = d.pop("jobTypeName", UNSET)

        operation_type = d.pop("operationType", UNSET)

        thumbprint = d.pop("thumbprint", UNSET)

        contents = d.pop("contents", UNSET)

        alias = d.pop("alias", UNSET)

        private_key_entry = d.pop("privateKeyEntry", UNSET)

        overwrite = d.pop("overwrite", UNSET)

        has_entry_password = d.pop("hasEntryPassword", UNSET)

        has_pfx_password = d.pop("hasPfxPassword", UNSET)

        _request_timestamp = d.pop("requestTimestamp", UNSET)
        request_timestamp: Union[Unset, None, datetime.datetime]
        if _request_timestamp is None:
            request_timestamp = None
        elif isinstance(_request_timestamp, Unset):
            request_timestamp = UNSET
        else:
            request_timestamp = isoparse(_request_timestamp)

        _keyfactor_schedule = d.pop("keyfactorSchedule", UNSET)
        keyfactor_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_keyfactor_schedule, Unset):
            keyfactor_schedule = UNSET
        else:
            keyfactor_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_keyfactor_schedule)

        subject = d.pop("subject", UNSET)

        directories = d.pop("directories", UNSET)

        ignored_directories = d.pop("ignoredDirectories", UNSET)

        sym_links = d.pop("symLinks", UNSET)

        compatibility = d.pop("compatibility", UNSET)

        file_extensions = d.pop("fileExtensions", UNSET)

        file_name_patterns = d.pop("fileNamePatterns", UNSET)

        _agent_blueprint_stores = d.pop("agentBlueprintStores", UNSET)
        agent_blueprint_stores: Union[Unset, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse]
        if isinstance(_agent_blueprint_stores, Unset):
            agent_blueprint_stores = UNSET
        else:
            agent_blueprint_stores = KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse.from_dict(
                _agent_blueprint_stores
            )

        keyfactor_web_keyfactor_api_models_orchestrators_agent_blueprint_jobs_response = cls(
            agent_blueprint_job_id=agent_blueprint_job_id,
            agent_blueprint_store_id=agent_blueprint_store_id,
            agent_blueprint_id=agent_blueprint_id,
            job_type=job_type,
            job_type_name=job_type_name,
            operation_type=operation_type,
            thumbprint=thumbprint,
            contents=contents,
            alias=alias,
            private_key_entry=private_key_entry,
            overwrite=overwrite,
            has_entry_password=has_entry_password,
            has_pfx_password=has_pfx_password,
            request_timestamp=request_timestamp,
            keyfactor_schedule=keyfactor_schedule,
            subject=subject,
            directories=directories,
            ignored_directories=ignored_directories,
            sym_links=sym_links,
            compatibility=compatibility,
            file_extensions=file_extensions,
            file_name_patterns=file_name_patterns,
            agent_blueprint_stores=agent_blueprint_stores,
        )

        return keyfactor_web_keyfactor_api_models_orchestrators_agent_blueprint_jobs_response
