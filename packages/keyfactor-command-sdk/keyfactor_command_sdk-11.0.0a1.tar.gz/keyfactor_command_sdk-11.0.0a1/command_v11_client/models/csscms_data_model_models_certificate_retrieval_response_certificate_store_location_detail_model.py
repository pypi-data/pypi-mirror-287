from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel")


@_attrs_define
class CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreLocationDetailModel:
    """
    Attributes:
        store_path (Union[Unset, None, str]):
        agent_pool (Union[Unset, None, str]):
        ip_address (Union[Unset, None, str]):
        port (Union[Unset, None, int]):
        network_name (Union[Unset, None, str]):
    """

    store_path: Union[Unset, None, str] = UNSET
    agent_pool: Union[Unset, None, str] = UNSET
    ip_address: Union[Unset, None, str] = UNSET
    port: Union[Unset, None, int] = UNSET
    network_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_path = self.store_path
        agent_pool = self.agent_pool
        ip_address = self.ip_address
        port = self.port
        network_name = self.network_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if store_path is not UNSET:
            field_dict["storePath"] = store_path
        if agent_pool is not UNSET:
            field_dict["agentPool"] = agent_pool
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
        store_path = d.pop("storePath", UNSET)

        agent_pool = d.pop("agentPool", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        port = d.pop("port", UNSET)

        network_name = d.pop("networkName", UNSET)

        csscms_data_model_models_certificate_retrieval_response_certificate_store_location_detail_model = cls(
            store_path=store_path,
            agent_pool=agent_pool,
            ip_address=ip_address,
            port=port,
            network_name=network_name,
        )

        return csscms_data_model_models_certificate_retrieval_response_certificate_store_location_detail_model
