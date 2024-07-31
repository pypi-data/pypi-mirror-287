from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.csscms_data_model_models_enrollment_csr_enrollment_request import (
    CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest,
)
from ...models.csscms_data_model_models_enrollment_csr_enrollment_response import (
    CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/Enrollment/CSR",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse.from_dict(response.json())

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
) -> Response[Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]]:
    """Performs a CSR Enrollment based upon the provided request

     ### Subject Alternative Name Flags ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | other              | OtherName                 |
    | rfc822             | RFC822Name                |
    | dns                | DNSName                   |
    | x400               | X400Address               |
    | directory          | DirectoryName             |
    | ediparty           | EdipartyName              |
    | uri                | UniformResourceIdentifier |
    | ip                 | IPAddress                 |
    | ip4                | IPv4Address               |
    | ip6                | IPv6Address               |
    | registeredid       | RegisteredId              |
    | ms_ntprincipalname | MS_NTPrincipalName        |
    | ms_ntdsreplication | MS_NTDSReplication        |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]]
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
    json_body: CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]]:
    """Performs a CSR Enrollment based upon the provided request

     ### Subject Alternative Name Flags ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | other              | OtherName                 |
    | rfc822             | RFC822Name                |
    | dns                | DNSName                   |
    | x400               | X400Address               |
    | directory          | DirectoryName             |
    | ediparty           | EdipartyName              |
    | uri                | UniformResourceIdentifier |
    | ip                 | IPAddress                 |
    | ip4                | IPv4Address               |
    | ip6                | IPv6Address               |
    | registeredid       | RegisteredId              |
    | ms_ntprincipalname | MS_NTPrincipalName        |
    | ms_ntdsreplication | MS_NTDSReplication        |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]]:
    """Performs a CSR Enrollment based upon the provided request

     ### Subject Alternative Name Flags ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | other              | OtherName                 |
    | rfc822             | RFC822Name                |
    | dns                | DNSName                   |
    | x400               | X400Address               |
    | directory          | DirectoryName             |
    | ediparty           | EdipartyName              |
    | uri                | UniformResourceIdentifier |
    | ip                 | IPAddress                 |
    | ip4                | IPv4Address               |
    | ip6                | IPv6Address               |
    | registeredid       | RegisteredId              |
    | ms_ntprincipalname | MS_NTPrincipalName        |
    | ms_ntdsreplication | MS_NTDSReplication        |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]]
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
    json_body: CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]]:
    """Performs a CSR Enrollment based upon the provided request

     ### Subject Alternative Name Flags ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | other              | OtherName                 |
    | rfc822             | RFC822Name                |
    | dns                | DNSName                   |
    | x400               | X400Address               |
    | directory          | DirectoryName             |
    | ediparty           | EdipartyName              |
    | uri                | UniformResourceIdentifier |
    | ip                 | IPAddress                 |
    | ip4                | IPv4Address               |
    | ip6                | IPv6Address               |
    | registeredid       | RegisteredId              |
    | ms_ntprincipalname | MS_NTPrincipalName        |
    | ms_ntdsreplication | MS_NTDSReplication        |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (CSSCMSDataModelModelsEnrollmentCSREnrollmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CSSCMSDataModelModelsEnrollmentCSREnrollmentResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
