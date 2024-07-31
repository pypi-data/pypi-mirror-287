from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_workflows_definition_response import (
    KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse,
)
from ...models.keyfactor_web_keyfactor_api_models_workflows_definition_step_request import (
    KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    definition_id: str,
    *,
    json_body: List["KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest"],
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
        "method": "put",
        "url": "/Workflow/Definitions/{definitionId}/Steps".format(
            definitionId=definition_id,
        ),
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse.from_dict(response.json())

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
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    definition_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]]:
    """Sets the provided steps on the latest version of the definition.

     If the latest version is also the published version, a new version will be created and the steps
    will be set on that new version.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        definition_id=definition_id,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    definition_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]]:
    """Sets the provided steps on the latest version of the definition.

     If the latest version is also the published version, a new version will be created and the steps
    will be set on that new version.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    return sync_detailed(
        definition_id=definition_id,
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    definition_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]]:
    """Sets the provided steps on the latest version of the definition.

     If the latest version is also the published version, a new version will be created and the steps
    will be set on that new version.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        definition_id=definition_id,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    definition_id: str,
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]]:
    """Sets the provided steps on the latest version of the definition.

     If the latest version is also the published version, a new version will be created and the steps
    will be set on that new version.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionStepRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, KeyfactorWebKeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    return (
        await asyncio_detailed(
            definition_id=definition_id,
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
