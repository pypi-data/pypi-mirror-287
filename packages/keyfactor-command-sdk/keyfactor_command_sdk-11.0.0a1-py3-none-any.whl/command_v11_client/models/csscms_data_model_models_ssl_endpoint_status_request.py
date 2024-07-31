from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CSSCMSDataModelModelsSSLEndpointStatusRequest")


@_attrs_define
class CSSCMSDataModelModelsSSLEndpointStatusRequest:
    """
    Attributes:
        id (str):
        status (bool):
    """

    id: str
    status: bool

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id")

        status = d.pop("status")

        csscms_data_model_models_ssl_endpoint_status_request = cls(
            id=id,
            status=status,
        )

        return csscms_data_model_models_ssl_endpoint_status_request
