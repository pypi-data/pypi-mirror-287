from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.csscms_data_model_models_metadata_all_update_request import CSSCMSDataModelModelsMetadataAllUpdateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: CSSCMSDataModelModelsMetadataAllUpdateRequest,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    params: Dict[str, Any] = {}
    params["collectionId"] = collection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/Certificates/Metadata/All",
        "json": json_json_body,
        "params": params,
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
    json_body: CSSCMSDataModelModelsMetadataAllUpdateRequest,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Updates the metadata for certificates associated with the certificate identifiers or query provided

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsMetadataAllUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CSSCMSDataModelModelsMetadataAllUpdateRequest,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Updates the metadata for certificates associated with the certificate identifiers or query provided

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsMetadataAllUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
