from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_response import (
        KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_response import (
        KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertDefinitionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        recipient (Union[Unset, None, str]):
        rotation_warning_days (Union[Unset, int]):
        registered_event_handler (Union[Unset,
            KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse]):
        event_handler_parameters (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse']]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    subject: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    recipient: Union[Unset, None, str] = UNSET
    rotation_warning_days: Union[Unset, int] = UNSET
    registered_event_handler: Union[
        Unset, "KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse"
    ] = UNSET
    event_handler_parameters: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        subject = self.subject
        message = self.message
        recipient = self.recipient
        rotation_warning_days = self.rotation_warning_days
        registered_event_handler: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.registered_event_handler, Unset):
            registered_event_handler = self.registered_event_handler.to_dict()

        event_handler_parameters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.event_handler_parameters, Unset):
            if self.event_handler_parameters is None:
                event_handler_parameters = None
            else:
                event_handler_parameters = []
                for event_handler_parameters_item_data in self.event_handler_parameters:
                    event_handler_parameters_item = event_handler_parameters_item_data.to_dict()

                    event_handler_parameters.append(event_handler_parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message is not UNSET:
            field_dict["message"] = message
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if rotation_warning_days is not UNSET:
            field_dict["rotationWarningDays"] = rotation_warning_days
        if registered_event_handler is not UNSET:
            field_dict["registeredEventHandler"] = registered_event_handler
        if event_handler_parameters is not UNSET:
            field_dict["eventHandlerParameters"] = event_handler_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_response import (
            KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse,
        )
        from ..models.keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_response import (
            KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        subject = d.pop("subject", UNSET)

        message = d.pop("message", UNSET)

        recipient = d.pop("recipient", UNSET)

        rotation_warning_days = d.pop("rotationWarningDays", UNSET)

        _registered_event_handler = d.pop("registeredEventHandler", UNSET)
        registered_event_handler: Union[Unset, KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse]
        if isinstance(_registered_event_handler, Unset):
            registered_event_handler = UNSET
        else:
            registered_event_handler = (
                KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse.from_dict(
                    _registered_event_handler
                )
            )

        event_handler_parameters = []
        _event_handler_parameters = d.pop("eventHandlerParameters", UNSET)
        for event_handler_parameters_item_data in _event_handler_parameters or []:
            event_handler_parameters_item = (
                KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse.from_dict(
                    event_handler_parameters_item_data
                )
            )

            event_handler_parameters.append(event_handler_parameters_item)

        keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_definition_response = cls(
            id=id,
            display_name=display_name,
            subject=subject,
            message=message,
            recipient=recipient,
            rotation_warning_days=rotation_warning_days,
            registered_event_handler=registered_event_handler,
            event_handler_parameters=event_handler_parameters,
        )

        return keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_definition_response
