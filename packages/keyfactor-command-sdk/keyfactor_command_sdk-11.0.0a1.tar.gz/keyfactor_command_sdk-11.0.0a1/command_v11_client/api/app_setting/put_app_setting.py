from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_app_settings_app_setting_response import (
    KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse,
)
from ...models.keyfactor_web_keyfactor_api_models_app_settings_app_setting_update_bulk_request import (
    KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "put",
        "url": "/AppSetting",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse"]]]:
    """Bulk update available application settings

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse']]]
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
    json_body: List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse"]]]:
    """Bulk update available application settings

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse']]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse"]]]:
    """Bulk update available application settings

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse']]]
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
    json_body: List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse"]]]:
    """Bulk update available application settings

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingUpdateBulkRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsAppSettingsAppSettingResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
