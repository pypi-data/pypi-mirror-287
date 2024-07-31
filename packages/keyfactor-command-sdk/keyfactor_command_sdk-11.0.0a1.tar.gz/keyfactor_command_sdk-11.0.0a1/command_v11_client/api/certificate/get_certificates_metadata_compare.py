from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    certificate_id: int,
    metadata_field_name: str,
    value: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    params: Dict[str, Any] = {}
    params["certificateId"] = certificate_id

    params["metadataFieldName"] = metadata_field_name

    params["value"] = value

    params["collectionId"] = collection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Certificates/Metadata/Compare",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, bool]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(bool, response.json())
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
) -> Response[Union[Any, bool]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    certificate_id: int,
    metadata_field_name: str,
    value: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, bool]]:
    """Compares the metadata value provided with the metadata value associated with the specified
    certificate

    Args:
        certificate_id (int):
        metadata_field_name (str):
        value (Union[Unset, None, str]):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, bool]]
    """

    kwargs = _get_kwargs(
        certificate_id=certificate_id,
        metadata_field_name=metadata_field_name,
        value=value,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    certificate_id: int,
    metadata_field_name: str,
    value: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, bool]]:
    """Compares the metadata value provided with the metadata value associated with the specified
    certificate

    Args:
        certificate_id (int):
        metadata_field_name (str):
        value (Union[Unset, None, str]):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, bool]
    """

    return sync_detailed(
        client=client,
        certificate_id=certificate_id,
        metadata_field_name=metadata_field_name,
        value=value,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    certificate_id: int,
    metadata_field_name: str,
    value: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, bool]]:
    """Compares the metadata value provided with the metadata value associated with the specified
    certificate

    Args:
        certificate_id (int):
        metadata_field_name (str):
        value (Union[Unset, None, str]):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, bool]]
    """

    kwargs = _get_kwargs(
        certificate_id=certificate_id,
        metadata_field_name=metadata_field_name,
        value=value,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    certificate_id: int,
    metadata_field_name: str,
    value: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, bool]]:
    """Compares the metadata value provided with the metadata value associated with the specified
    certificate

    Args:
        certificate_id (int):
        metadata_field_name (str):
        value (Union[Unset, None, str]):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, bool]
    """

    return (
        await asyncio_detailed(
            client=client,
            certificate_id=certificate_id,
            metadata_field_name=metadata_field_name,
            value=value,
            collection_id=collection_id,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
