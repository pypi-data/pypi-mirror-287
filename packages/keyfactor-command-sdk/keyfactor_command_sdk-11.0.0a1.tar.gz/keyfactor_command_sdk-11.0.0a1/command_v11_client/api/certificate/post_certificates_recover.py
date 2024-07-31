from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.csscms_data_model_models_recovery_response import CSSCMSDataModelModelsRecoveryResponse
from ...models.keyfactor_web_keyfactor_api_models_certificates_certificate_recovery_request import (
    KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    if not headers.get('x-certificateformat'):
        headers['x-certificateformat'] = 'PEM' # Default to recovered output PEM

    params: Dict[str, Any] = {}
    params["collectionId"] = collection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/Certificates/Recover",
        "json": json_json_body,
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CSSCMSDataModelModelsRecoveryResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CSSCMSDataModelModelsRecoveryResponse.from_dict(response.json())

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
) -> Response[Union[Any, CSSCMSDataModelModelsRecoveryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CSSCMSDataModelModelsRecoveryResponse]]:
    """Recovers the persisted certificate associated with the provided query

     *NOTE: At least one of the following criteria must be provided:
    1. Certificate ID
    2. Thumbprint
    3. Serial number AND Issuer DN (because Serial Number is CA-specific and so is not unique enough on
    its own)

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CSSCMSDataModelModelsRecoveryResponse]]
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


def sync(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CSSCMSDataModelModelsRecoveryResponse]]:
    """Recovers the persisted certificate associated with the provided query

     *NOTE: At least one of the following criteria must be provided:
    1. Certificate ID
    2. Thumbprint
    3. Serial number AND Issuer DN (because Serial Number is CA-specific and so is not unique enough on
    its own)

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CSSCMSDataModelModelsRecoveryResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CSSCMSDataModelModelsRecoveryResponse]]:
    """Recovers the persisted certificate associated with the provided query

     *NOTE: At least one of the following criteria must be provided:
    1. Certificate ID
    2. Thumbprint
    3. Serial number AND Issuer DN (because Serial Number is CA-specific and so is not unique enough on
    its own)

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CSSCMSDataModelModelsRecoveryResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest,
    collection_id: Union[Unset, None, int] = 0,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CSSCMSDataModelModelsRecoveryResponse]]:
    """Recovers the persisted certificate associated with the provided query

     *NOTE: At least one of the following criteria must be provided:
    1. Certificate ID
    2. Thumbprint
    3. Serial number AND Issuer DN (because Serial Number is CA-specific and so is not unique enough on
    its own)

    Args:
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CSSCMSDataModelModelsRecoveryResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            collection_id=collection_id,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
