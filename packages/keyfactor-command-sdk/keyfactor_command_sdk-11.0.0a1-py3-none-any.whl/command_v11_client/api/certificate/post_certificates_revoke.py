from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.csscms_data_model_models_revocation_revocation_response import (
    CSSCMSDataModelModelsRevocationRevocationResponse,
)
from ...models.csscms_data_model_models_revoke_certificate_request import CSSCMSDataModelModelsRevokeCertificateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: CSSCMSDataModelModelsRevokeCertificateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/Certificates/Revoke",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CSSCMSDataModelModelsRevocationRevocationResponse.from_dict(response.json())

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
) -> Response[Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CSSCMSDataModelModelsRevokeCertificateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]]:
    """Revokes the certificates associated with the provided identifiers and associates the provided data
    with the revocation

     ### Revocation Reason Codes for Microsoft CA ###
    | Value             | Description               |
    |-------------------|---------------------------|
    | -1                | Remove from hold          |
    | 0                 | Unspecified               |
    | 1                 | Key compromised           |
    | 2                 | CA compromised            |
    | 3                 | Affiliation changed       |
    | 4                 | Superceded                |
    | 5                 | Cessation of operation    |
    | 6                 | Certificate hold          |
    | 7                 | Remove from CRL           |
    | 999               | Unknown                   |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsRevokeCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]]
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
    json_body: CSSCMSDataModelModelsRevokeCertificateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]]:
    """Revokes the certificates associated with the provided identifiers and associates the provided data
    with the revocation

     ### Revocation Reason Codes for Microsoft CA ###
    | Value             | Description               |
    |-------------------|---------------------------|
    | -1                | Remove from hold          |
    | 0                 | Unspecified               |
    | 1                 | Key compromised           |
    | 2                 | CA compromised            |
    | 3                 | Affiliation changed       |
    | 4                 | Superceded                |
    | 5                 | Cessation of operation    |
    | 6                 | Certificate hold          |
    | 7                 | Remove from CRL           |
    | 999               | Unknown                   |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsRevokeCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CSSCMSDataModelModelsRevokeCertificateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]]:
    """Revokes the certificates associated with the provided identifiers and associates the provided data
    with the revocation

     ### Revocation Reason Codes for Microsoft CA ###
    | Value             | Description               |
    |-------------------|---------------------------|
    | -1                | Remove from hold          |
    | 0                 | Unspecified               |
    | 1                 | Key compromised           |
    | 2                 | CA compromised            |
    | 3                 | Affiliation changed       |
    | 4                 | Superceded                |
    | 5                 | Cessation of operation    |
    | 6                 | Certificate hold          |
    | 7                 | Remove from CRL           |
    | 999               | Unknown                   |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsRevokeCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]]
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
    json_body: CSSCMSDataModelModelsRevokeCertificateRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]]:
    """Revokes the certificates associated with the provided identifiers and associates the provided data
    with the revocation

     ### Revocation Reason Codes for Microsoft CA ###
    | Value             | Description               |
    |-------------------|---------------------------|
    | -1                | Remove from hold          |
    | 0                 | Unspecified               |
    | 1                 | Key compromised           |
    | 2                 | CA compromised            |
    | 3                 | Affiliation changed       |
    | 4                 | Superceded                |
    | 5                 | Cessation of operation    |
    | 6                 | Certificate hold          |
    | 7                 | Remove from CRL           |
    | 999               | Unknown                   |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsRevokeCertificateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CSSCMSDataModelModelsRevocationRevocationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
