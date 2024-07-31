import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_workflows_workflow_instance_status import KeyfactorWorkflowsWorkflowInstanceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_workflows_available_signal_response import (
        KeyfactorWebKeyfactorApiModelsWorkflowsAvailableSignalResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_workflows_instance_definition_response import (
        KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_workflows_instance_response_current_state_data import (
        KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData,
    )
    from ..models.keyfactor_web_keyfactor_api_models_workflows_instance_response_initial_data import (
        KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseInitialData,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        status (Union[Unset, KeyfactorWorkflowsWorkflowInstanceStatus]):
        current_step_id (Union[Unset, str]):
        status_message (Union[Unset, None, str]):
        signals (Union[Unset, None, List['KeyfactorWebKeyfactorApiModelsWorkflowsAvailableSignalResponse']]):
        definition (Union[Unset, KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse]):
        current_step_display_name (Union[Unset, None, str]):
        current_step_unique_name (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        last_modified (Union[Unset, None, datetime.datetime]):
        start_date (Union[Unset, datetime.datetime]):
        initial_data (Union[Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseInitialData]):
        current_state_data (Union[Unset, None,
            KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData]):
        reference_id (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, KeyfactorWorkflowsWorkflowInstanceStatus] = UNSET
    current_step_id: Union[Unset, str] = UNSET
    status_message: Union[Unset, None, str] = UNSET
    signals: Union[Unset, None, List["KeyfactorWebKeyfactorApiModelsWorkflowsAvailableSignalResponse"]] = UNSET
    definition: Union[Unset, "KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse"] = UNSET
    current_step_display_name: Union[Unset, None, str] = UNSET
    current_step_unique_name: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    last_modified: Union[Unset, None, datetime.datetime] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    initial_data: Union[Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseInitialData"] = UNSET
    current_state_data: Union[
        Unset, None, "KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData"
    ] = UNSET
    reference_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        current_step_id = self.current_step_id
        status_message = self.status_message
        signals: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.signals, Unset):
            if self.signals is None:
                signals = None
            else:
                signals = []
                for signals_item_data in self.signals:
                    signals_item = signals_item_data.to_dict()

                    signals.append(signals_item)

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

        initial_data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.initial_data, Unset):
            initial_data = self.initial_data.to_dict() if self.initial_data else None

        current_state_data: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.current_state_data, Unset):
            current_state_data = self.current_state_data.to_dict() if self.current_state_data else None

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
        if signals is not UNSET:
            field_dict["signals"] = signals
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
        if initial_data is not UNSET:
            field_dict["initialData"] = initial_data
        if current_state_data is not UNSET:
            field_dict["currentStateData"] = current_state_data
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_workflows_available_signal_response import (
            KeyfactorWebKeyfactorApiModelsWorkflowsAvailableSignalResponse,
        )
        from ..models.keyfactor_web_keyfactor_api_models_workflows_instance_definition_response import (
            KeyfactorWebKeyfactorApiModelsWorkflowsInstanceDefinitionResponse,
        )
        from ..models.keyfactor_web_keyfactor_api_models_workflows_instance_response_current_state_data import (
            KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData,
        )
        from ..models.keyfactor_web_keyfactor_api_models_workflows_instance_response_initial_data import (
            KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseInitialData,
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

        signals = []
        _signals = d.pop("signals", UNSET)
        for signals_item_data in _signals or []:
            signals_item = KeyfactorWebKeyfactorApiModelsWorkflowsAvailableSignalResponse.from_dict(signals_item_data)

            signals.append(signals_item)

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

        _initial_data = d.pop("initialData", UNSET)
        initial_data: Union[Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseInitialData]
        if _initial_data is None:
            initial_data = None
        elif isinstance(_initial_data, Unset):
            initial_data = UNSET
        else:
            initial_data = KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseInitialData.from_dict(_initial_data)

        _current_state_data = d.pop("currentStateData", UNSET)
        current_state_data: Union[Unset, None, KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData]
        if _current_state_data is None:
            current_state_data = None
        elif isinstance(_current_state_data, Unset):
            current_state_data = UNSET
        else:
            current_state_data = KeyfactorWebKeyfactorApiModelsWorkflowsInstanceResponseCurrentStateData.from_dict(
                _current_state_data
            )

        reference_id = d.pop("referenceId", UNSET)

        keyfactor_web_keyfactor_api_models_workflows_instance_response = cls(
            id=id,
            status=status,
            current_step_id=current_step_id,
            status_message=status_message,
            signals=signals,
            definition=definition,
            current_step_display_name=current_step_display_name,
            current_step_unique_name=current_step_unique_name,
            title=title,
            last_modified=last_modified,
            start_date=start_date,
            initial_data=initial_data,
            current_state_data=current_state_data,
            reference_id=reference_id,
        )

        return keyfactor_web_keyfactor_api_models_workflows_instance_response
