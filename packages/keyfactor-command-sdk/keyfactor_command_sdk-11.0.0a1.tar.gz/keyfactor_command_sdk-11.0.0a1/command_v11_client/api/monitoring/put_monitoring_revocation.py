from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_monitoring_revocation_monitoring_definition_response import (
    KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse,
)
from ...models.keyfactor_web_keyfactor_api_models_monitoring_revocation_monitoring_update_request import (
    KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/Monitoring/Revocation",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse.from_dict(
            response.json()
        )

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]]:
    """Edit a revocation monitoring endpoint

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]]:
    """Edit a revocation monitoring endpoint

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]]:
    """Edit a revocation monitoring endpoint

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]]:
    """Edit a revocation monitoring endpoint

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsMonitoringRevocationMonitoringDefinitionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
