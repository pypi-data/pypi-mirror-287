from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CSSCMSDataModelModelsSSLImmediateSslScanRequest")


@_attrs_define
class CSSCMSDataModelModelsSSLImmediateSslScanRequest:
    """
    Attributes:
        discovery (bool):
        monitoring (bool):
    """

    discovery: bool
    monitoring: bool

    def to_dict(self) -> Dict[str, Any]:
        discovery = self.discovery
        monitoring = self.monitoring

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "discovery": discovery,
                "monitoring": monitoring,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        discovery = d.pop("discovery")

        monitoring = d.pop("monitoring")

        csscms_data_model_models_ssl_immediate_ssl_scan_request = cls(
            discovery=discovery,
            monitoring=monitoring,
        )

        return csscms_data_model_models_ssl_immediate_ssl_scan_request
