from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_certificate_stores_certificate_store_approve_request import (
    KeyfactorWebKeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: List["KeyfactorWebKeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest"],
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
        "method": "post",
        "url": "/CertificateStores/Approve",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Approves the provided certificate stores to make them available for management

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body
            (List['KeyfactorWebKeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Approves the provided certificate stores to make them available for management

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body
            (List['KeyfactorWebKeyfactorApiModelsCertificateStoresCertificateStoreApproveRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
