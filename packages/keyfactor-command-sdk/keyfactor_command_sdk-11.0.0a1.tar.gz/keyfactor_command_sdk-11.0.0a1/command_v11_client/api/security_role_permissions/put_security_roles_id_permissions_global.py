from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.keyfactor_web_keyfactor_api_models_security_security_role_permissions_global_permission_request import (
    KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionRequest,
)
from ...models.keyfactor_web_keyfactor_api_models_security_security_role_permissions_global_permission_response import (
    KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    json_body: List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionRequest"],
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
        "url": "/Security/Roles/{id}/Permissions/Global".format(
            id=id,
        ),
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse"]]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse.from_dict(
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
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse"]]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse"]]
]:
    """Adds global permissions to the security role that matches the id.

     ### Valid Global Permissions ###
    | Area                          | Permission        |
    |-------------------------------|-------------------|
    | AdminPortal                   | Read              |
    | AgentAutoRegistration         | Read              |
    | AgentAutoRegistration         | Modify            |
    | AgentManagement               | Read              |
    | AgentManagement               | Modify            |
    | API                           | Read              |
    | ApplicationSettings           | Read              |
    | ApplicationSettings           | Modify            |
    | Auditing                      | Read              |
    | CertificateCollections        | Modify            |
    | CertificateEnrollment         | EnrollPFX         |
    | CertificateEnrollment         | EnrollCSR         |
    | CertificateEnrollment         | CsrGeneration     |
    | CertificateEnrollment         | PendingCsr        |
    | CertificateMetadataTypes      | Read              |
    | CertificateMetadataTypes      | Modify            |
    | Certificates                  | Read              |
    | Certificates                  | EditMetadata      |
    | Certificates                  | Import            |
    | Certificates                  | Recover           |
    | Certificates                  | Revoke            |
    | Certificates                  | Delete            |
    | Certificates                  | ImportPrivateKey  |
    | CertificateStoreManagement    | Read              |
    | CertificateStoreManagement    | Schedule          |
    | CertificateStoreManagement    | Modify            |
    | Dashboard                     | Read              |
    | Dashboard                     | RiskHeader        |
    | EventHandlerRegistration      | Read              |
    | EventHandlerRegistration      | Modify            |
    | MacAutoEnrollManagement       | Read              |
    | MacAutoEnrollManagement       | Modify            |
    | PkiManagement                 | Read              |
    | PkiManagement                 | Modify            |
    | PrivilegedAccessManagement    | Read              |
    | PrivilegedAccessManagement    | Modify            |
    | Reports                       | Read              |
    | Reports                       | Modify            |
    | SecuritySettings              | Read              |
    | SecuritySettings              | Modify            |
    | SSH                           | User              |
    | SSH                           | ServerAdmin       |
    | SSH                           | EnterpriseAdmin   |
    | SslManagement                 | Read              |
    | SslManagement                 | Modify            |
    | SystemSettings                | Read              |
    | SystemSettings                | Modify            |
    | WorkflowDefinitions           | Read              |
    | WorkflowDefinitions           | Modify            |
    | WorkflowInstances             | ReadAll           |
    | WorkflowInstances             | ReadAssignedToMe  |
    | WorkflowInstances             | ReadMy            |
    | WorkflowInstances             | Manage            |
    | WorkflowManagement            | Read              |
    | WorkflowManagement            | Modify            |
    | WorkflowManagement            | Test              |
    | WorkflowManagement            | Participate       |
    | WorkflowManagement            | Manage            |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermis
            sionRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse"]]
]:
    """Adds global permissions to the security role that matches the id.

     ### Valid Global Permissions ###
    | Area                          | Permission        |
    |-------------------------------|-------------------|
    | AdminPortal                   | Read              |
    | AgentAutoRegistration         | Read              |
    | AgentAutoRegistration         | Modify            |
    | AgentManagement               | Read              |
    | AgentManagement               | Modify            |
    | API                           | Read              |
    | ApplicationSettings           | Read              |
    | ApplicationSettings           | Modify            |
    | Auditing                      | Read              |
    | CertificateCollections        | Modify            |
    | CertificateEnrollment         | EnrollPFX         |
    | CertificateEnrollment         | EnrollCSR         |
    | CertificateEnrollment         | CsrGeneration     |
    | CertificateEnrollment         | PendingCsr        |
    | CertificateMetadataTypes      | Read              |
    | CertificateMetadataTypes      | Modify            |
    | Certificates                  | Read              |
    | Certificates                  | EditMetadata      |
    | Certificates                  | Import            |
    | Certificates                  | Recover           |
    | Certificates                  | Revoke            |
    | Certificates                  | Delete            |
    | Certificates                  | ImportPrivateKey  |
    | CertificateStoreManagement    | Read              |
    | CertificateStoreManagement    | Schedule          |
    | CertificateStoreManagement    | Modify            |
    | Dashboard                     | Read              |
    | Dashboard                     | RiskHeader        |
    | EventHandlerRegistration      | Read              |
    | EventHandlerRegistration      | Modify            |
    | MacAutoEnrollManagement       | Read              |
    | MacAutoEnrollManagement       | Modify            |
    | PkiManagement                 | Read              |
    | PkiManagement                 | Modify            |
    | PrivilegedAccessManagement    | Read              |
    | PrivilegedAccessManagement    | Modify            |
    | Reports                       | Read              |
    | Reports                       | Modify            |
    | SecuritySettings              | Read              |
    | SecuritySettings              | Modify            |
    | SSH                           | User              |
    | SSH                           | ServerAdmin       |
    | SSH                           | EnterpriseAdmin   |
    | SslManagement                 | Read              |
    | SslManagement                 | Modify            |
    | SystemSettings                | Read              |
    | SystemSettings                | Modify            |
    | WorkflowDefinitions           | Read              |
    | WorkflowDefinitions           | Modify            |
    | WorkflowInstances             | ReadAll           |
    | WorkflowInstances             | ReadAssignedToMe  |
    | WorkflowInstances             | ReadMy            |
    | WorkflowInstances             | Manage            |
    | WorkflowManagement            | Read              |
    | WorkflowManagement            | Modify            |
    | WorkflowManagement            | Test              |
    | WorkflowManagement            | Participate       |
    | WorkflowManagement            | Manage            |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermis
            sionRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse']]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Response[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse"]]
]:
    """Adds global permissions to the security role that matches the id.

     ### Valid Global Permissions ###
    | Area                          | Permission        |
    |-------------------------------|-------------------|
    | AdminPortal                   | Read              |
    | AgentAutoRegistration         | Read              |
    | AgentAutoRegistration         | Modify            |
    | AgentManagement               | Read              |
    | AgentManagement               | Modify            |
    | API                           | Read              |
    | ApplicationSettings           | Read              |
    | ApplicationSettings           | Modify            |
    | Auditing                      | Read              |
    | CertificateCollections        | Modify            |
    | CertificateEnrollment         | EnrollPFX         |
    | CertificateEnrollment         | EnrollCSR         |
    | CertificateEnrollment         | CsrGeneration     |
    | CertificateEnrollment         | PendingCsr        |
    | CertificateMetadataTypes      | Read              |
    | CertificateMetadataTypes      | Modify            |
    | Certificates                  | Read              |
    | Certificates                  | EditMetadata      |
    | Certificates                  | Import            |
    | Certificates                  | Recover           |
    | Certificates                  | Revoke            |
    | Certificates                  | Delete            |
    | Certificates                  | ImportPrivateKey  |
    | CertificateStoreManagement    | Read              |
    | CertificateStoreManagement    | Schedule          |
    | CertificateStoreManagement    | Modify            |
    | Dashboard                     | Read              |
    | Dashboard                     | RiskHeader        |
    | EventHandlerRegistration      | Read              |
    | EventHandlerRegistration      | Modify            |
    | MacAutoEnrollManagement       | Read              |
    | MacAutoEnrollManagement       | Modify            |
    | PkiManagement                 | Read              |
    | PkiManagement                 | Modify            |
    | PrivilegedAccessManagement    | Read              |
    | PrivilegedAccessManagement    | Modify            |
    | Reports                       | Read              |
    | Reports                       | Modify            |
    | SecuritySettings              | Read              |
    | SecuritySettings              | Modify            |
    | SSH                           | User              |
    | SSH                           | ServerAdmin       |
    | SSH                           | EnterpriseAdmin   |
    | SslManagement                 | Read              |
    | SslManagement                 | Modify            |
    | SystemSettings                | Read              |
    | SystemSettings                | Modify            |
    | WorkflowDefinitions           | Read              |
    | WorkflowDefinitions           | Modify            |
    | WorkflowInstances             | ReadAll           |
    | WorkflowInstances             | ReadAssignedToMe  |
    | WorkflowInstances             | ReadMy            |
    | WorkflowInstances             | Manage            |
    | WorkflowManagement            | Read              |
    | WorkflowManagement            | Modify            |
    | WorkflowManagement            | Test              |
    | WorkflowManagement            | Participate       |
    | WorkflowManagement            | Manage            |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermis
            sionRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionRequest"],
    x_keyfactor_api_version: Union[Unset, str] = UNSET,
) -> Optional[
    Union[Any, List["KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse"]]
]:
    """Adds global permissions to the security role that matches the id.

     ### Valid Global Permissions ###
    | Area                          | Permission        |
    |-------------------------------|-------------------|
    | AdminPortal                   | Read              |
    | AgentAutoRegistration         | Read              |
    | AgentAutoRegistration         | Modify            |
    | AgentManagement               | Read              |
    | AgentManagement               | Modify            |
    | API                           | Read              |
    | ApplicationSettings           | Read              |
    | ApplicationSettings           | Modify            |
    | Auditing                      | Read              |
    | CertificateCollections        | Modify            |
    | CertificateEnrollment         | EnrollPFX         |
    | CertificateEnrollment         | EnrollCSR         |
    | CertificateEnrollment         | CsrGeneration     |
    | CertificateEnrollment         | PendingCsr        |
    | CertificateMetadataTypes      | Read              |
    | CertificateMetadataTypes      | Modify            |
    | Certificates                  | Read              |
    | Certificates                  | EditMetadata      |
    | Certificates                  | Import            |
    | Certificates                  | Recover           |
    | Certificates                  | Revoke            |
    | Certificates                  | Delete            |
    | Certificates                  | ImportPrivateKey  |
    | CertificateStoreManagement    | Read              |
    | CertificateStoreManagement    | Schedule          |
    | CertificateStoreManagement    | Modify            |
    | Dashboard                     | Read              |
    | Dashboard                     | RiskHeader        |
    | EventHandlerRegistration      | Read              |
    | EventHandlerRegistration      | Modify            |
    | MacAutoEnrollManagement       | Read              |
    | MacAutoEnrollManagement       | Modify            |
    | PkiManagement                 | Read              |
    | PkiManagement                 | Modify            |
    | PrivilegedAccessManagement    | Read              |
    | PrivilegedAccessManagement    | Modify            |
    | Reports                       | Read              |
    | Reports                       | Modify            |
    | SecuritySettings              | Read              |
    | SecuritySettings              | Modify            |
    | SSH                           | User              |
    | SSH                           | ServerAdmin       |
    | SSH                           | EnterpriseAdmin   |
    | SslManagement                 | Read              |
    | SslManagement                 | Modify            |
    | SystemSettings                | Read              |
    | SystemSettings                | Modify            |
    | WorkflowDefinitions           | Read              |
    | WorkflowDefinitions           | Modify            |
    | WorkflowInstances             | ReadAll           |
    | WorkflowInstances             | ReadAssignedToMe  |
    | WorkflowInstances             | ReadMy            |
    | WorkflowInstances             | Manage            |
    | WorkflowManagement            | Read              |
    | WorkflowManagement            | Modify            |
    | WorkflowManagement            | Test              |
    | WorkflowManagement            | Participate       |
    | WorkflowManagement            | Manage            |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):
        json_body (List['KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermis
            sionRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['KeyfactorWebKeyfactorApiModelsSecuritySecurityRolePermissionsGlobalPermissionResponse']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
        )
    ).parsed
