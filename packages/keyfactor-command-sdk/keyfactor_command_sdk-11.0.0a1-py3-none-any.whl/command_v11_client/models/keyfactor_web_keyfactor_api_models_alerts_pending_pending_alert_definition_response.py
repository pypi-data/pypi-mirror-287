from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_alerts_alert_template_alert_template_response import (
        KeyfactorWebKeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_response import (
        KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_response import (
        KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        recipients (Union[Unset, None, List[str]]):
        template (Union[Unset, KeyfactorWebKeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse]):
        registered_event_handler (Union[Unset,
            KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse]):
        event_handler_parameters (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse']]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    subject: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    recipients: Union[Unset, None, List[str]] = UNSET
    template: Union[Unset, "KeyfactorWebKeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse"] = UNSET
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
        recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            if self.recipients is None:
                recipients = None
            else:
                recipients = self.recipients

        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

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
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if template is not UNSET:
            field_dict["template"] = template
        if registered_event_handler is not UNSET:
            field_dict["registeredEventHandler"] = registered_event_handler
        if event_handler_parameters is not UNSET:
            field_dict["eventHandlerParameters"] = event_handler_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_alerts_alert_template_alert_template_response import (
            KeyfactorWebKeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse,
        )
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

        recipients = cast(List[str], d.pop("recipients", UNSET))

        _template = d.pop("template", UNSET)
        template: Union[Unset, KeyfactorWebKeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = KeyfactorWebKeyfactorApiModelsAlertsAlertTemplateAlertTemplateResponse.from_dict(_template)

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

        keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_definition_response = cls(
            id=id,
            display_name=display_name,
            subject=subject,
            message=message,
            recipients=recipients,
            template=template,
            registered_event_handler=registered_event_handler,
            event_handler_parameters=event_handler_parameters,
        )

        return keyfactor_web_keyfactor_api_models_alerts_pending_pending_alert_definition_response
