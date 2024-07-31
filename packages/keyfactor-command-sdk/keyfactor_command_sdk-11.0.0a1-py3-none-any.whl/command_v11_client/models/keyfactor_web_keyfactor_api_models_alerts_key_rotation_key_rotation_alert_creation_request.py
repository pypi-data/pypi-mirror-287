from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_request import (
        KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest,
    )
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_request import (
        KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertCreationRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsKeyRotationKeyRotationAlertCreationRequest:
    """
    Attributes:
        display_name (str):
        subject (str):
        message (str):
        rotation_warning_days (int):
        registered_event_handler (Union[Unset,
            KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest]):
        event_handler_parameters (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest']]):
    """

    display_name: str
    subject: str
    message: str
    rotation_warning_days: int
    registered_event_handler: Union[
        Unset, "KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest"
    ] = UNSET
    event_handler_parameters: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        subject = self.subject
        message = self.message
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
        field_dict.update(
            {
                "displayName": display_name,
                "subject": subject,
                "message": message,
                "rotationWarningDays": rotation_warning_days,
            }
        )
        if registered_event_handler is not UNSET:
            field_dict["registeredEventHandler"] = registered_event_handler
        if event_handler_parameters is not UNSET:
            field_dict["eventHandlerParameters"] = event_handler_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_request import (
            KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest,
        )
        from ..models.keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_request import (
            KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        display_name = d.pop("displayName")

        subject = d.pop("subject")

        message = d.pop("message")

        rotation_warning_days = d.pop("rotationWarningDays")

        _registered_event_handler = d.pop("registeredEventHandler", UNSET)
        registered_event_handler: Union[Unset, KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest]
        if isinstance(_registered_event_handler, Unset):
            registered_event_handler = UNSET
        else:
            registered_event_handler = (
                KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest.from_dict(
                    _registered_event_handler
                )
            )

        event_handler_parameters = []
        _event_handler_parameters = d.pop("eventHandlerParameters", UNSET)
        for event_handler_parameters_item_data in _event_handler_parameters or []:
            event_handler_parameters_item = (
                KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest.from_dict(
                    event_handler_parameters_item_data
                )
            )

            event_handler_parameters.append(event_handler_parameters_item)

        keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_creation_request = cls(
            display_name=display_name,
            subject=subject,
            message=message,
            rotation_warning_days=rotation_warning_days,
            registered_event_handler=registered_event_handler,
            event_handler_parameters=event_handler_parameters,
        )

        return keyfactor_web_keyfactor_api_models_alerts_key_rotation_key_rotation_alert_creation_request
