from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_permission_sets_permission_set_create_request import (
    KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest,
)
from ...models.keyfactor_web_keyfactor_api_models_permission_sets_permission_set_response import (
    KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/PermissionSets",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse.from_dict(response.json())

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
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]]:
    """Creates a new permission set.

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]]
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
    json_body: KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]]:
    """Creates a new permission set.

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]]:
    """Creates a new permission set.

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]]
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
    json_body: KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]]:
    """Creates a new permission set.

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsPermissionSetsPermissionSetResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
