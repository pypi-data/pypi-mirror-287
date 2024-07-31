from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_orchestrators_agent_blueprint_response import (
    KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    params: Dict[str, Any] = {}
    params["agentId"] = agent_id

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/AgentBluePrint/GenerateBluePrint",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse.from_dict(response.json())

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
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    agent_id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]]:
    """Generates an agent blueprint from the provided agents

    Args:
        agent_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        name=name,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    agent_id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]]:
    """Generates an agent blueprint from the provided agents

    Args:
        agent_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        name=name,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    agent_id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]]:
    """Generates an agent blueprint from the provided agents

    Args:
        agent_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        name=name,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    agent_id: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]]:
    """Generates an agent blueprint from the provided agents

    Args:
        agent_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            name=name,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
