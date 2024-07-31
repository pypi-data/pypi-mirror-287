from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CSSCMSDataModelModelsSSLNetworkRangesRequest")


@_attrs_define
class CSSCMSDataModelModelsSSLNetworkRangesRequest:
    """
    Attributes:
        network_id (str):
        ranges (List[str]):
    """

    network_id: str
    ranges: List[str]

    def to_dict(self) -> Dict[str, Any]:
        network_id = self.network_id
        ranges = self.ranges

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "networkId": network_id,
                "ranges": ranges,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        network_id = d.pop("networkId")

        ranges = cast(List[str], d.pop("ranges"))

        csscms_data_model_models_ssl_network_ranges_request = cls(
            network_id=network_id,
            ranges=ranges,
        )

        return csscms_data_model_models_ssl_network_ranges_request
