from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_common_queryable_extensions_sort_order import KeyfactorCommonQueryableExtensionsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sort_name: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    params: Dict[str, Any] = {}
    params["SortName"] = sort_name

    json_sort_order: Union[Unset, None, int] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["SortOrder"] = json_sort_order

    params["Query"] = query

    params["CollectionId"] = collection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Certificates/CSV",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
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
) -> Response[Union[Any, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    sort_name: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, str]]:
    """Returns a comma-delimited CSV file containing all certificates in the database

    Args:
        sort_name (Union[Unset, None, str]):
        sort_order (Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder]):
        query (Union[Unset, None, str]):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        sort_name=sort_name,
        sort_order=sort_order,
        query=query,
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
    sort_name: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, str]]:
    """Returns a comma-delimited CSV file containing all certificates in the database

    Args:
        sort_name (Union[Unset, None, str]):
        sort_order (Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder]):
        query (Union[Unset, None, str]):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return sync_detailed(
        client=client,
        sort_name=sort_name,
        sort_order=sort_order,
        query=query,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sort_name: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, str]]:
    """Returns a comma-delimited CSV file containing all certificates in the database

    Args:
        sort_name (Union[Unset, None, str]):
        sort_order (Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder]):
        query (Union[Unset, None, str]):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        sort_name=sort_name,
        sort_order=sort_order,
        query=query,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sort_name: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, str]]:
    """Returns a comma-delimited CSV file containing all certificates in the database

    Args:
        sort_name (Union[Unset, None, str]):
        sort_order (Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder]):
        query (Union[Unset, None, str]):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            sort_name=sort_name,
            sort_order=sort_order,
            query=query,
            collection_id=collection_id,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
