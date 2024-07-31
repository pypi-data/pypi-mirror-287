from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSLEndpoint")


@_attrs_define
class CSSCMSDataModelModelsSSLEndpoint:
    """
    Attributes:
        endpoint_id (Union[Unset, str]):
        network_id (Union[Unset, str]):
        last_history_id (Union[Unset, None, str]):
        ip_address_bytes (Union[Unset, None, str]):
        port (Union[Unset, int]):
        sni_name (Union[Unset, None, str]):
        enable_monitor (Union[Unset, bool]):
        reviewed (Union[Unset, bool]):
    """

    endpoint_id: Union[Unset, str] = UNSET
    network_id: Union[Unset, str] = UNSET
    last_history_id: Union[Unset, None, str] = UNSET
    ip_address_bytes: Union[Unset, None, str] = UNSET
    port: Union[Unset, int] = UNSET
    sni_name: Union[Unset, None, str] = UNSET
    enable_monitor: Union[Unset, bool] = UNSET
    reviewed: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        endpoint_id = self.endpoint_id
        network_id = self.network_id
        last_history_id = self.last_history_id
        ip_address_bytes = self.ip_address_bytes
        port = self.port
        sni_name = self.sni_name
        enable_monitor = self.enable_monitor
        reviewed = self.reviewed

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if endpoint_id is not UNSET:
            field_dict["endpointId"] = endpoint_id
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if last_history_id is not UNSET:
            field_dict["lastHistoryId"] = last_history_id
        if ip_address_bytes is not UNSET:
            field_dict["ipAddressBytes"] = ip_address_bytes
        if port is not UNSET:
            field_dict["port"] = port
        if sni_name is not UNSET:
            field_dict["sniName"] = sni_name
        if enable_monitor is not UNSET:
            field_dict["enableMonitor"] = enable_monitor
        if reviewed is not UNSET:
            field_dict["reviewed"] = reviewed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        endpoint_id = d.pop("endpointId", UNSET)

        network_id = d.pop("networkId", UNSET)

        last_history_id = d.pop("lastHistoryId", UNSET)

        ip_address_bytes = d.pop("ipAddressBytes", UNSET)

        port = d.pop("port", UNSET)

        sni_name = d.pop("sniName", UNSET)

        enable_monitor = d.pop("enableMonitor", UNSET)

        reviewed = d.pop("reviewed", UNSET)

        csscms_data_model_models_ssl_endpoint = cls(
            endpoint_id=endpoint_id,
            network_id=network_id,
            last_history_id=last_history_id,
            ip_address_bytes=ip_address_bytes,
            port=port,
            sni_name=sni_name,
            enable_monitor=enable_monitor,
            reviewed=reviewed,
        )

        return csscms_data_model_models_ssl_endpoint
