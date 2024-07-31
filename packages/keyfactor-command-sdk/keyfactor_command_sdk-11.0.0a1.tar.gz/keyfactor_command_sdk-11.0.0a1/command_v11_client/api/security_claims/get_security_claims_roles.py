from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.csscms_core_enums_claim_type import CSSCMSCoreEnumsClaimType
from ...models.keyfactor_web_keyfactor_api_models_security_role_claim_definitions_security_role_for_claim_response import (
    KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    claim_type: CSSCMSCoreEnumsClaimType,
    claim_value: str,
    provider_authentication_scheme: str,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    params: Dict[str, Any] = {}
    json_claim_type = claim_type.value

    params["ClaimType"] = json_claim_type

    params["ClaimValue"] = claim_value

    params["ProviderAuthenticationScheme"] = provider_authentication_scheme

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Security/Claims/Roles",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse"]]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse.from_dict(
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
) -> Response[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse"]]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    claim_type: CSSCMSCoreEnumsClaimType,
    claim_value: str,
    provider_authentication_scheme: str,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse"]]
]:
    """Returns a list of roles granted by the claim with the provided id.

    Args:
        claim_type (CSSCMSCoreEnumsClaimType):
        claim_value (str):
        provider_authentication_scheme (str):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse']]]
    """

    kwargs = _get_kwargs(
        claim_type=claim_type,
        claim_value=claim_value,
        provider_authentication_scheme=provider_authentication_scheme,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    claim_type: CSSCMSCoreEnumsClaimType,
    claim_value: str,
    provider_authentication_scheme: str,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse"]]
]:
    """Returns a list of roles granted by the claim with the provided id.

    Args:
        claim_type (CSSCMSCoreEnumsClaimType):
        claim_value (str):
        provider_authentication_scheme (str):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse']]
    """

    return sync_detailed(
        client=client,
        claim_type=claim_type,
        claim_value=claim_value,
        provider_authentication_scheme=provider_authentication_scheme,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    claim_type: CSSCMSCoreEnumsClaimType,
    claim_value: str,
    provider_authentication_scheme: str,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse"]]
]:
    """Returns a list of roles granted by the claim with the provided id.

    Args:
        claim_type (CSSCMSCoreEnumsClaimType):
        claim_value (str):
        provider_authentication_scheme (str):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse']]]
    """

    kwargs = _get_kwargs(
        claim_type=claim_type,
        claim_value=claim_value,
        provider_authentication_scheme=provider_authentication_scheme,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    claim_type: CSSCMSCoreEnumsClaimType,
    claim_value: str,
    provider_authentication_scheme: str,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse"]]
]:
    """Returns a list of roles granted by the claim with the provided id.

    Args:
        claim_type (CSSCMSCoreEnumsClaimType):
        claim_value (str):
        provider_authentication_scheme (str):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityRoleClaimDefinitionsSecurityRoleForClaimResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            claim_type=claim_type,
            claim_value=claim_value,
            provider_authentication_scheme=provider_authentication_scheme,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
