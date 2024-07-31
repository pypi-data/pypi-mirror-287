from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsSSLSslScanResult")


@_attrs_define
class CSSCMSDataModelModelsSSLSslScanResult:
    """
    Attributes:
        endpoint_id (Union[Unset, str]):
        reverse_dns (Union[Unset, None, str]):
        sni_name (Union[Unset, None, str]):
        ip_address (Union[Unset, None, str]):
        port (Union[Unset, int]):
        certificate_found (Union[Unset, bool]):
        agent_pool_name (Union[Unset, None, str]):
        network_name (Union[Unset, None, str]):
        monitor_status (Union[Unset, bool]):
        certificate_cn (Union[Unset, None, str]):
        reviewed (Union[Unset, bool]):
    """

    endpoint_id: Union[Unset, str] = UNSET
    reverse_dns: Union[Unset, None, str] = UNSET
    sni_name: Union[Unset, None, str] = UNSET
    ip_address: Union[Unset, None, str] = UNSET
    port: Union[Unset, int] = UNSET
    certificate_found: Union[Unset, bool] = UNSET
    agent_pool_name: Union[Unset, None, str] = UNSET
    network_name: Union[Unset, None, str] = UNSET
    monitor_status: Union[Unset, bool] = UNSET
    certificate_cn: Union[Unset, None, str] = UNSET
    reviewed: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        endpoint_id = self.endpoint_id
        reverse_dns = self.reverse_dns
        sni_name = self.sni_name
        ip_address = self.ip_address
        port = self.port
        certificate_found = self.certificate_found
        agent_pool_name = self.agent_pool_name
        network_name = self.network_name
        monitor_status = self.monitor_status
        certificate_cn = self.certificate_cn
        reviewed = self.reviewed

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if endpoint_id is not UNSET:
            field_dict["endpointId"] = endpoint_id
        if reverse_dns is not UNSET:
            field_dict["reverseDNS"] = reverse_dns
        if sni_name is not UNSET:
            field_dict["sniName"] = sni_name
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if port is not UNSET:
            field_dict["port"] = port
        if certificate_found is not UNSET:
            field_dict["certificateFound"] = certificate_found
        if agent_pool_name is not UNSET:
            field_dict["agentPoolName"] = agent_pool_name
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if monitor_status is not UNSET:
            field_dict["monitorStatus"] = monitor_status
        if certificate_cn is not UNSET:
            field_dict["certificateCN"] = certificate_cn
        if reviewed is not UNSET:
            field_dict["reviewed"] = reviewed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        endpoint_id = d.pop("endpointId", UNSET)

        reverse_dns = d.pop("reverseDNS", UNSET)

        sni_name = d.pop("sniName", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        port = d.pop("port", UNSET)

        certificate_found = d.pop("certificateFound", UNSET)

        agent_pool_name = d.pop("agentPoolName", UNSET)

        network_name = d.pop("networkName", UNSET)

        monitor_status = d.pop("monitorStatus", UNSET)

        certificate_cn = d.pop("certificateCN", UNSET)

        reviewed = d.pop("reviewed", UNSET)

        csscms_data_model_models_ssl_ssl_scan_result = cls(
            endpoint_id=endpoint_id,
            reverse_dns=reverse_dns,
            sni_name=sni_name,
            ip_address=ip_address,
            port=port,
            certificate_found=certificate_found,
            agent_pool_name=agent_pool_name,
            network_name=network_name,
            monitor_status=monitor_status,
            certificate_cn=certificate_cn,
            reviewed=reviewed,
        )

        return csscms_data_model_models_ssl_ssl_scan_result
