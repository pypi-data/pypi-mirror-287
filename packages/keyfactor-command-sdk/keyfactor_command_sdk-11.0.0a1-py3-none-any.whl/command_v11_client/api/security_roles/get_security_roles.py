from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_common_queryable_extensions_sort_order import KeyfactorCommonQueryableExtensionsSortOrder
from ...models.keyfactor_web_keyfactor_api_models_security_legacy_security_roles_security_role_response import (
    KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    validate: Union[Unset, None, bool] = UNSET,
    query_string: Union[Unset, None, str] = UNSET,
    page_returned: Union[Unset, None, int] = UNSET,
    return_limit: Union[Unset, None, int] = UNSET,
    sort_field: Union[Unset, None, str] = UNSET,
    sort_ascending: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    params: Dict[str, Any] = {}
    params["Validate"] = validate

    params["QueryString"] = query_string

    params["PageReturned"] = page_returned

    params["ReturnLimit"] = return_limit

    params["SortField"] = sort_field

    json_sort_ascending: Union[Unset, None, int] = UNSET
    if not isinstance(sort_ascending, Unset):
        json_sort_ascending = sort_ascending.value if sort_ascending else None

    params["SortAscending"] = json_sort_ascending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/Security/Roles",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse.from_dict(
                response_200_item_data
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
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    validate: Union[Unset, None, bool] = UNSET,
    query_string: Union[Unset, None, str] = UNSET,
    page_returned: Union[Unset, None, int] = UNSET,
    return_limit: Union[Unset, None, int] = UNSET,
    sort_field: Union[Unset, None, str] = UNSET,
    sort_ascending: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse"]]]:
    """Returns all security roles according to the provided filter and output parameters.
    The v1 endpoints for Security Roles will only work against AD Identities.  Please use the v2
    endpoints instead.

    Args:
        validate (Union[Unset, None, bool]):
        query_string (Union[Unset, None, str]):
        page_returned (Union[Unset, None, int]):
        return_limit (Union[Unset, None, int]):
        sort_field (Union[Unset, None, str]):
        sort_ascending (Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse']]]
    """

    kwargs = _get_kwargs(
        validate=validate,
        query_string=query_string,
        page_returned=page_returned,
        return_limit=return_limit,
        sort_field=sort_field,
        sort_ascending=sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    validate: Union[Unset, None, bool] = UNSET,
    query_string: Union[Unset, None, str] = UNSET,
    page_returned: Union[Unset, None, int] = UNSET,
    return_limit: Union[Unset, None, int] = UNSET,
    sort_field: Union[Unset, None, str] = UNSET,
    sort_ascending: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse"]]]:
    """Returns all security roles according to the provided filter and output parameters.
    The v1 endpoints for Security Roles will only work against AD Identities.  Please use the v2
    endpoints instead.

    Args:
        validate (Union[Unset, None, bool]):
        query_string (Union[Unset, None, str]):
        page_returned (Union[Unset, None, int]):
        return_limit (Union[Unset, None, int]):
        sort_field (Union[Unset, None, str]):
        sort_ascending (Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse']]
    """

    return sync_detailed(
        client=client,
        validate=validate,
        query_string=query_string,
        page_returned=page_returned,
        return_limit=return_limit,
        sort_field=sort_field,
        sort_ascending=sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    validate: Union[Unset, None, bool] = UNSET,
    query_string: Union[Unset, None, str] = UNSET,
    page_returned: Union[Unset, None, int] = UNSET,
    return_limit: Union[Unset, None, int] = UNSET,
    sort_field: Union[Unset, None, str] = UNSET,
    sort_ascending: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse"]]]:
    """Returns all security roles according to the provided filter and output parameters.
    The v1 endpoints for Security Roles will only work against AD Identities.  Please use the v2
    endpoints instead.

    Args:
        validate (Union[Unset, None, bool]):
        query_string (Union[Unset, None, str]):
        page_returned (Union[Unset, None, int]):
        return_limit (Union[Unset, None, int]):
        sort_field (Union[Unset, None, str]):
        sort_ascending (Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse']]]
    """

    kwargs = _get_kwargs(
        validate=validate,
        query_string=query_string,
        page_returned=page_returned,
        return_limit=return_limit,
        sort_field=sort_field,
        sort_ascending=sort_ascending,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    validate: Union[Unset, None, bool] = UNSET,
    query_string: Union[Unset, None, str] = UNSET,
    page_returned: Union[Unset, None, int] = UNSET,
    return_limit: Union[Unset, None, int] = UNSET,
    sort_field: Union[Unset, None, str] = UNSET,
    sort_ascending: Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse"]]]:
    """Returns all security roles according to the provided filter and output parameters.
    The v1 endpoints for Security Roles will only work against AD Identities.  Please use the v2
    endpoints instead.

    Args:
        validate (Union[Unset, None, bool]):
        query_string (Union[Unset, None, str]):
        page_returned (Union[Unset, None, int]):
        return_limit (Union[Unset, None, int]):
        sort_field (Union[Unset, None, str]):
        sort_ascending (Union[Unset, None, KeyfactorCommonQueryableExtensionsSortOrder]):
        x_keyfactor_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsSecurityLegacySecurityRolesSecurityRoleResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            validate=validate,
            query_string=query_string,
            page_returned=page_returned,
            return_limit=return_limit,
            sort_field=sort_field,
            sort_ascending=sort_ascending,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
