from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsContainerAssignment")


@_attrs_define
class CSSCMSDataModelModelsContainerAssignment:
    """
    Attributes:
        keystore_ids (List[str]):
        cert_store_container_id (Union[Unset, int]):
        new_container_name (Union[Unset, None, str]):
        new_container_type (Union[Unset, int]):
    """

    keystore_ids: List[str]
    cert_store_container_id: Union[Unset, int] = UNSET
    new_container_name: Union[Unset, None, str] = UNSET
    new_container_type: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keystore_ids = self.keystore_ids

        cert_store_container_id = self.cert_store_container_id
        new_container_name = self.new_container_name
        new_container_type = self.new_container_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "keystoreIds": keystore_ids,
            }
        )
        if cert_store_container_id is not UNSET:
            field_dict["certStoreContainerId"] = cert_store_container_id
        if new_container_name is not UNSET:
            field_dict["newContainerName"] = new_container_name
        if new_container_type is not UNSET:
            field_dict["newContainerType"] = new_container_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        keystore_ids = cast(List[str], d.pop("keystoreIds"))

        cert_store_container_id = d.pop("certStoreContainerId", UNSET)

        new_container_name = d.pop("newContainerName", UNSET)

        new_container_type = d.pop("newContainerType", UNSET)

        csscms_data_model_models_container_assignment = cls(
            keystore_ids=keystore_ids,
            cert_store_container_id=cert_store_container_id,
            new_container_name=new_container_name,
            new_container_type=new_container_type,
        )

        return csscms_data_model_models_container_assignment
