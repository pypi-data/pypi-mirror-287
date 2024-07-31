from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_security_legacy_security_roles_role_identities_request import (
    KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest,
)
from ...models.keyfactor_web_keyfactor_api_models_security_legacy_security_roles_role_identities_response import (
    KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    json_body: KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/Security/Roles/{id}/Identities".format(
            id=id,
        ),
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse.from_dict(
                    response_200_item_data
                )
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
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse"]]]:
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
    json_body: KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse"]]]:
    """Updates the identities which have the security role that matches the id.
    The v1 endpoints for Security Roles will only work against AD Identities.  Please use the v2
    endpoints instead.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body
            (KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
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
    json_body: KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse"]]]:
    """Updates the identities which have the security role that matches the id.
    The v1 endpoints for Security Roles will only work against AD Identities.  Please use the v2
    endpoints instead.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body
            (KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse']]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse"]]]:
    """Updates the identities which have the security role that matches the id.
    The v1 endpoints for Security Roles will only work against AD Identities.  Please use the v2
    endpoints instead.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body
            (KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse"]]]:
    """Updates the identities which have the security role that matches the id.
    The v1 endpoints for Security Roles will only work against AD Identities.  Please use the v2
    endpoints instead.

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body
            (KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesRoleIdentitiesResponse']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
