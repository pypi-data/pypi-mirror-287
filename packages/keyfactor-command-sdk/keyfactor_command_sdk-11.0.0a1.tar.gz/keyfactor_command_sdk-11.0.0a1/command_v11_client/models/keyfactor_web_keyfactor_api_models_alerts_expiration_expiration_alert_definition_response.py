from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_alerts_alert_certificate_query_alert_certificate_query_response import (
        KeyfactorWebKeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_event_handler_parameter_response import (
        KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse,
    )
    from ..models.keyfactor_web_keyfactor_api_models_event_handler_registered_event_handler_response import (
        KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertDefinitionResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsAlertsExpirationExpirationAlertDefinitionResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        subject (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        expiration_warning_days (Union[Unset, int]):
        recipients (Union[Unset, None, List[str]]):
        certificate_query (Union[Unset,
            KeyfactorWebKeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse]):
        registered_event_handler (Union[Unset,
            KeyfactorWebKeyfactorApiModelsEventHandlerRegisteredEventHandlerResponse]):
        event_handler_parameters (Union[Unset, None,
            List['KeyfactorWebKeyfactorApiModelsEventHandlerEventHandlerParameterResponse']]):
    """

    id: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    subject: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    expiration_warning_days: Union[Unset, int] = UNSET
    recipients: Union[Unset, None, List[str]] = UNSET
    certificate_query: Union[
        Unset, "KeyfactorWebKeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse"
    ] = UNSET
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
        expiration_warning_days = self.expiration_warning_days
        recipients: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            if self.recipients is None:
                recipients = None
            else:
                recipients = self.recipients

        certificate_query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.certificate_query, Unset):
            certificate_query = self.certificate_query.to_dict()

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
        if expiration_warning_days is not UNSET:
            field_dict["expirationWarningDays"] = expiration_warning_days
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if certificate_query is not UNSET:
            field_dict["certificateQuery"] = certificate_query
        if registered_event_handler is not UNSET:
            field_dict["registeredEventHandler"] = registered_event_handler
        if event_handler_parameters is not UNSET:
            field_dict["eventHandlerParameters"] = event_handler_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_alerts_alert_certificate_query_alert_certificate_query_response import (
            KeyfactorWebKeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse,
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

        expiration_warning_days = d.pop("expirationWarningDays", UNSET)

        recipients = cast(List[str], d.pop("recipients", UNSET))

        _certificate_query = d.pop("certificateQuery", UNSET)
        certificate_query: Union[
            Unset, KeyfactorWebKeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse
        ]
        if isinstance(_certificate_query, Unset):
            certificate_query = UNSET
        else:
            certificate_query = (
                KeyfactorWebKeyfactorApiModelsAlertsAlertCertificateQueryAlertCertificateQueryResponse.from_dict(
                    _certificate_query
                )
            )

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

        keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_definition_response = cls(
            id=id,
            display_name=display_name,
            subject=subject,
            message=message,
            expiration_warning_days=expiration_warning_days,
            recipients=recipients,
            certificate_query=certificate_query,
            registered_event_handler=registered_event_handler,
            event_handler_parameters=event_handler_parameters,
        )

        return keyfactor_web_keyfactor_api_models_alerts_expiration_expiration_alert_definition_response
