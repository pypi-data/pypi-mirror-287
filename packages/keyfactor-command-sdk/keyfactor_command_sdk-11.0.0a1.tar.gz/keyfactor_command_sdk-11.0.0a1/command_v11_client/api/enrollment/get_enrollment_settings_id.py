from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_templates_enrollment_template_enrollment_settings_response import (
    KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    return {
        "method": "get",
        "url": "/Enrollment/Settings/{id}".format(
            id=id,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse.from_dict(
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
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]]:
    """Gets the template settings to use during enrollment. The response will be the resolved values for
    the settings.
    If there is a template specific setting, the template specific setting will be used in the response.
    If there is not a template specific setting, the global setting will be used in the response.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]]:
    """Gets the template settings to use during enrollment. The response will be the resolved values for
    the settings.
    If there is a template specific setting, the template specific setting will be used in the response.
    If there is not a template specific setting, the global setting will be used in the response.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]]:
    """Gets the template settings to use during enrollment. The response will be the resolved values for
    the settings.
    If there is a template specific setting, the template specific setting will be used in the response.
    If there is not a template specific setting, the global setting will be used in the response.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]]:
    """Gets the template settings to use during enrollment. The response will be the resolved values for
    the settings.
    If there is a template specific setting, the template specific setting will be used in the response.
    If there is not a template specific setting, the global setting will be used in the response.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsTemplatesEnrollmentTemplateEnrollmentSettingsResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
