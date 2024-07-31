import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret


T = TypeVar("T", bound="CSSCMSDataModelModelsDiscoveryJobRequest")


@_attrs_define
class CSSCMSDataModelModelsDiscoveryJobRequest:
    """
    Attributes:
        type (int):
        client_machine (Union[Unset, None, str]):
        agent_id (Union[Unset, None, str]):
        job_execution_timestamp (Union[Unset, None, datetime.datetime]):
        dirs (Union[Unset, None, str]):
        ignored_dirs (Union[Unset, None, str]):
        extensions (Union[Unset, None, str]):
        name_patterns (Union[Unset, None, str]):
        sym_links (Union[Unset, bool]):
        compatibility (Union[Unset, bool]):
        server_username (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        server_password (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
        server_use_ssl (Union[Unset, bool]):
    """

    type: int
    client_machine: Union[Unset, None, str] = UNSET
    agent_id: Union[Unset, None, str] = UNSET
    job_execution_timestamp: Union[Unset, None, datetime.datetime] = UNSET
    dirs: Union[Unset, None, str] = UNSET
    ignored_dirs: Union[Unset, None, str] = UNSET
    extensions: Union[Unset, None, str] = UNSET
    name_patterns: Union[Unset, None, str] = UNSET
    sym_links: Union[Unset, bool] = UNSET
    compatibility: Union[Unset, bool] = UNSET
    server_username: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    server_password: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET
    server_use_ssl: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        client_machine = self.client_machine
        agent_id = self.agent_id
        job_execution_timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.job_execution_timestamp, Unset):
            job_execution_timestamp = self.job_execution_timestamp.isoformat()[:-6]+'Z' if self.job_execution_timestamp else None

        dirs = self.dirs
        ignored_dirs = self.ignored_dirs
        extensions = self.extensions
        name_patterns = self.name_patterns
        sym_links = self.sym_links
        compatibility = self.compatibility
        server_username: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_username, Unset):
            server_username = self.server_username.to_dict()

        server_password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_password, Unset):
            server_password = self.server_password.to_dict()

        server_use_ssl = self.server_use_ssl

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
            }
        )
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if job_execution_timestamp is not UNSET:
            field_dict["jobExecutionTimestamp"] = job_execution_timestamp
        if dirs is not UNSET:
            field_dict["dirs"] = dirs
        if ignored_dirs is not UNSET:
            field_dict["ignoredDirs"] = ignored_dirs
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if name_patterns is not UNSET:
            field_dict["namePatterns"] = name_patterns
        if sym_links is not UNSET:
            field_dict["symLinks"] = sym_links
        if compatibility is not UNSET:
            field_dict["compatibility"] = compatibility
        if server_username is not UNSET:
            field_dict["serverUsername"] = server_username
        if server_password is not UNSET:
            field_dict["serverPassword"] = server_password
        if server_use_ssl is not UNSET:
            field_dict["serverUseSsl"] = server_use_ssl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        type = d.pop("type")

        client_machine = d.pop("clientMachine", UNSET)

        agent_id = d.pop("agentId", UNSET)

        _job_execution_timestamp = d.pop("jobExecutionTimestamp", UNSET)
        job_execution_timestamp: Union[Unset, None, datetime.datetime]
        if _job_execution_timestamp is None:
            job_execution_timestamp = None
        elif isinstance(_job_execution_timestamp, Unset):
            job_execution_timestamp = UNSET
        else:
            job_execution_timestamp = isoparse(_job_execution_timestamp)

        dirs = d.pop("dirs", UNSET)

        ignored_dirs = d.pop("ignoredDirs", UNSET)

        extensions = d.pop("extensions", UNSET)

        name_patterns = d.pop("namePatterns", UNSET)

        sym_links = d.pop("symLinks", UNSET)

        compatibility = d.pop("compatibility", UNSET)

        _server_username = d.pop("serverUsername", UNSET)
        server_username: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_server_username, Unset):
            server_username = UNSET
        else:
            server_username = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_server_username)

        _server_password = d.pop("serverPassword", UNSET)
        server_password: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_server_password, Unset):
            server_password = UNSET
        else:
            server_password = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_server_password)

        server_use_ssl = d.pop("serverUseSsl", UNSET)

        csscms_data_model_models_discovery_job_request = cls(
            type=type,
            client_machine=client_machine,
            agent_id=agent_id,
            job_execution_timestamp=job_execution_timestamp,
            dirs=dirs,
            ignored_dirs=ignored_dirs,
            extensions=extensions,
            name_patterns=name_patterns,
            sym_links=sym_links,
            compatibility=compatibility,
            server_username=server_username,
            server_password=server_password,
            server_use_ssl=server_use_ssl,
        )

        return csscms_data_model_models_discovery_job_request
