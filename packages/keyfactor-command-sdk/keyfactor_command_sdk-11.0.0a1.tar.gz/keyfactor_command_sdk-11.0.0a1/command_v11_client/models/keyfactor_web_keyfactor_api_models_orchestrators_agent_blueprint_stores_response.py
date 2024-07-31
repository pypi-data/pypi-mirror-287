from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsOrchestratorsAgentBlueprintStoresResponse:
    """
    Attributes:
        agent_blueprint_store_id (Union[Unset, str]):
        agent_blueprint_id (Union[Unset, str]):
        store_path (Union[Unset, None, str]):
        container_id (Union[Unset, int]):
        cert_store_type (Union[Unset, int]):
        cert_store_type_name (Union[Unset, None, str]):
        approved (Union[Unset, bool]):
        create_if_missing (Union[Unset, bool]):
        properties (Union[Unset, None, str]):
    """

    agent_blueprint_store_id: Union[Unset, str] = UNSET
    agent_blueprint_id: Union[Unset, str] = UNSET
    store_path: Union[Unset, None, str] = UNSET
    container_id: Union[Unset, int] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    cert_store_type_name: Union[Unset, None, str] = UNSET
    approved: Union[Unset, bool] = UNSET
    create_if_missing: Union[Unset, bool] = UNSET
    properties: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agent_blueprint_store_id = self.agent_blueprint_store_id
        agent_blueprint_id = self.agent_blueprint_id
        store_path = self.store_path
        container_id = self.container_id
        cert_store_type = self.cert_store_type
        cert_store_type_name = self.cert_store_type_name
        approved = self.approved
        create_if_missing = self.create_if_missing
        properties = self.properties

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agent_blueprint_store_id is not UNSET:
            field_dict["agentBlueprintStoreId"] = agent_blueprint_store_id
        if agent_blueprint_id is not UNSET:
            field_dict["agentBlueprintId"] = agent_blueprint_id
        if store_path is not UNSET:
            field_dict["storePath"] = store_path
        if container_id is not UNSET:
            field_dict["containerId"] = container_id
        if cert_store_type is not UNSET:
            field_dict["certStoreType"] = cert_store_type
        if cert_store_type_name is not UNSET:
            field_dict["certStoreTypeName"] = cert_store_type_name
        if approved is not UNSET:
            field_dict["approved"] = approved
        if create_if_missing is not UNSET:
            field_dict["createIfMissing"] = create_if_missing
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        agent_blueprint_store_id = d.pop("agentBlueprintStoreId", UNSET)

        agent_blueprint_id = d.pop("agentBlueprintId", UNSET)

        store_path = d.pop("storePath", UNSET)

        container_id = d.pop("containerId", UNSET)

        cert_store_type = d.pop("certStoreType", UNSET)

        cert_store_type_name = d.pop("certStoreTypeName", UNSET)

        approved = d.pop("approved", UNSET)

        create_if_missing = d.pop("createIfMissing", UNSET)

        properties = d.pop("properties", UNSET)

        keyfactor_web_keyfactor_api_models_orchestrators_agent_blueprint_stores_response = cls(
            agent_blueprint_store_id=agent_blueprint_store_id,
            agent_blueprint_id=agent_blueprint_id,
            store_path=store_path,
            container_id=container_id,
            cert_store_type=cert_store_type,
            cert_store_type_name=cert_store_type_name,
            approved=approved,
            create_if_missing=create_if_missing,
            properties=properties,
        )

        return keyfactor_web_keyfactor_api_models_orchestrators_agent_blueprint_stores_response
