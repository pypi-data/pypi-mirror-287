import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_workflows_workflow_instance_status import KeyfactorWorkflowsWorkflowInstanceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_instance_definition_response import (
        KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsInstanceQueryResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsInstanceQueryResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        status (Union[Unset, KeyfactorWorkflowsWorkflowInstanceStatus]):
        current_step_id (Union[Unset, str]):
        status_message (Union[Unset, None, str]):
        definition (Union[Unset, KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse]):
        current_step_display_name (Union[Unset, None, str]):
        current_step_unique_name (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        last_modified (Union[Unset, None, datetime.datetime]):
        start_date (Union[Unset, datetime.datetime]):
        reference_id (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, KeyfactorWorkflowsWorkflowInstanceStatus] = UNSET
    current_step_id: Union[Unset, str] = UNSET
    status_message: Union[Unset, None, str] = UNSET
    definition: Union[Unset, "KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse"] = UNSET
    current_step_display_name: Union[Unset, None, str] = UNSET
    current_step_unique_name: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    last_modified: Union[Unset, None, datetime.datetime] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    reference_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        current_step_id = self.current_step_id
        status_message = self.status_message
        definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

        current_step_display_name = self.current_step_display_name
        current_step_unique_name = self.current_step_unique_name
        title = self.title
        last_modified: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()[:-6]+'Z' if self.last_modified else None

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()[:-6]+'Z'

        reference_id = self.reference_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if current_step_id is not UNSET:
            field_dict["currentStepId"] = current_step_id
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if definition is not UNSET:
            field_dict["definition"] = definition
        if current_step_display_name is not UNSET:
            field_dict["currentStepDisplayName"] = current_step_display_name
        if current_step_unique_name is not UNSET:
            field_dict["currentStepUniqueName"] = current_step_unique_name
        if title is not UNSET:
            field_dict["title"] = title
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_instance_definition_response import (
            KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, KeyfactorWorkflowsWorkflowInstanceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = KeyfactorWorkflowsWorkflowInstanceStatus(_status)

        current_step_id = d.pop("currentStepId", UNSET)

        status_message = d.pop("statusMessage", UNSET)

        _definition = d.pop("definition", UNSET)
        definition: Union[Unset, KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse]
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse.from_dict(_definition)

        current_step_display_name = d.pop("currentStepDisplayName", UNSET)

        current_step_unique_name = d.pop("currentStepUniqueName", UNSET)

        title = d.pop("title", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, None, datetime.datetime]
        if _last_modified is None:
            last_modified = None
        elif isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        reference_id = d.pop("referenceId", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_instance_query_response = cls(
            id=id,
            status=status,
            current_step_id=current_step_id,
            status_message=status_message,
            definition=definition,
            current_step_display_name=current_step_display_name,
            current_step_unique_name=current_step_unique_name,
            title=title,
            last_modified=last_modified,
            start_date=start_date,
            reference_id=reference_id,
        )

        return keyfactor_web_keyfactor_api_models_workflows_instance_query_response
