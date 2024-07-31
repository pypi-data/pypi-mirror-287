from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertStoreLocationsCertificateStoreLocationsDetail")


@_attrs_define
class CSSCMSDataModelModelsCertStoreLocationsCertificateStoreLocationsDetail:
    """
    Attributes:
        store_type (Union[Unset, None, str]):
        certificate_id (Union[Unset, int]):
        store_id (Union[Unset, str]):
        store_type_id (Union[Unset, int]):
        client_machine (Union[Unset, None, str]):
        store_path (Union[Unset, None, str]):
        agent_pool (Union[Unset, None, str]):
        alias (Union[Unset, None, str]):
        ip_address (Union[Unset, None, str]):
        port (Union[Unset, None, int]):
        network_name (Union[Unset, None, str]):
    """

    store_type: Union[Unset, None, str] = UNSET
    certificate_id: Union[Unset, int] = UNSET
    store_id: Union[Unset, str] = UNSET
    store_type_id: Union[Unset, int] = UNSET
    client_machine: Union[Unset, None, str] = UNSET
    store_path: Union[Unset, None, str] = UNSET
    agent_pool: Union[Unset, None, str] = UNSET
    alias: Union[Unset, None, str] = UNSET
    ip_address: Union[Unset, None, str] = UNSET
    port: Union[Unset, None, int] = UNSET
    network_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_type = self.store_type
        certificate_id = self.certificate_id
        store_id = self.store_id
        store_type_id = self.store_type_id
        client_machine = self.client_machine
        store_path = self.store_path
        agent_pool = self.agent_pool
        alias = self.alias
        ip_address = self.ip_address
        port = self.port
        network_name = self.network_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if certificate_id is not UNSET:
            field_dict["certificateId"] = certificate_id
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if store_type_id is not UNSET:
            field_dict["storeTypeId"] = store_type_id
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine
        if store_path is not UNSET:
            field_dict["storePath"] = store_path
        if agent_pool is not UNSET:
            field_dict["agentPool"] = agent_pool
        if alias is not UNSET:
            field_dict["alias"] = alias
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if port is not UNSET:
            field_dict["port"] = port
        if network_name is not UNSET:
            field_dict["networkName"] = network_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        store_type = d.pop("storeType", UNSET)

        certificate_id = d.pop("certificateId", UNSET)

        store_id = d.pop("storeId", UNSET)

        store_type_id = d.pop("storeTypeId", UNSET)

        client_machine = d.pop("clientMachine", UNSET)

        store_path = d.pop("storePath", UNSET)

        agent_pool = d.pop("agentPool", UNSET)

        alias = d.pop("alias", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        port = d.pop("port", UNSET)

        network_name = d.pop("networkName", UNSET)

        csscms_data_model_models_cert_store_locations_certificate_store_locations_detail = cls(
            store_type=store_type,
            certificate_id=certificate_id,
            store_id=store_id,
            store_type_id=store_type_id,
            client_machine=client_machine,
            store_path=store_path,
            agent_pool=agent_pool,
            alias=alias,
            ip_address=ip_address,
            port=port,
            network_name=network_name,
        )

        return csscms_data_model_models_cert_store_locations_certificate_store_locations_detail
