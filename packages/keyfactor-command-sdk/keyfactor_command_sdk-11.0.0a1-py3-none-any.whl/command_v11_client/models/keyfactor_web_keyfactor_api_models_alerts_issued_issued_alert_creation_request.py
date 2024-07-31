from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_request import (
        KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest,
    )
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_request import (
        KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsIssuedIssuedAlertCreationRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsIssuedIssuedAlertCreationRequest:
    """
    Attributes:
        display_name (str):
        subject (str):
        message (str):
        template_id (Union[Unset, None, int]):
        registered_event_handler (Union[Unset,
            KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest]):
        recipients (Union[Unset, None, List[str]]):
        event_handler_parameters (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest']]):
    """

    display_name: str
    subject: str
    message: str
    template_id: Union[Unset, None, int] = UNSET
    registered_event_handler: Union[
        Unset, "KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerRequest"
    ] = UNSET
    recipients: Union[Unset, None, List[str]] = UNSET
    event_handler_parameters: Union[
        Unset, None, List["KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        subject = self.subject
        message = self.message
        template_id = self.template_id
        registered_event_handler: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.registered_event_handler, Unset):
            registered_event_handler = self.registered_event_handler.to_dict()

        recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            if self.recipients is None:
                recipients = None
            else:
                recipients = self.recipients

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
            }
        )
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if registered_event_handler is not UNSET:
            field_dict["registeredEventHandler"] = registered_event_handler
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
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

        template_id = d.pop("templateId", UNSET)

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

        recipients = cast(List[str], d.pop("recipients", UNSET))

        event_handler_parameters = []
        _event_handler_parameters = d.pop("eventHandlerParameters", UNSET)
        for event_handler_parameters_item_data in _event_handler_parameters or []:
            event_handler_parameters_item = (
                KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterRequest.from_dict(
                    event_handler_parameters_item_data
                )
            )

            event_handler_parameters.append(event_handler_parameters_item)

        keyfactor_web_keyfactor_api_models_alerts_issued_issued_alert_creation_request = cls(
            display_name=display_name,
            subject=subject,
            message=message,
            template_id=template_id,
            registered_event_handler=registered_event_handler,
            recipients=recipients,
            event_handler_parameters=event_handler_parameters,
        )

        return keyfactor_web_keyfactor_api_models_alerts_issued_issued_alert_creation_request
