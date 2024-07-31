from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_certificate_stores_types_certificate_store_type_response import (
    KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    return {
        "method": "get",
        "url": "/CertificateStoreTypes/Name/{name}".format(
            name=name,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse.from_dict(
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
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse"]]]:
    """Returns a single certificate store type that matches the provided short name

    Args:
        name (str):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse']]]
    """

    kwargs = _get_kwargs(
        name=name,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse"]]]:
    """Returns a single certificate store type that matches the provided short name

    Args:
        name (str):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse']]
    """

    return sync_detailed(
        name=name,
        client=client,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse"]]]:
    """Returns a single certificate store type that matches the provided short name

    Args:
        name (str):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse']]]
    """

    kwargs = _get_kwargs(
        name=name,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse"]]]:
    """Returns a single certificate store type that matches the provided short name

    Args:
        name (str):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse']]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
