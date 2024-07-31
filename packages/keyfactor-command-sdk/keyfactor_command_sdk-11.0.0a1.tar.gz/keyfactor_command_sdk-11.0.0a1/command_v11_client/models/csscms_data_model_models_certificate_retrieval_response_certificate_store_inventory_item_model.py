from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel")


@_attrs_define
class CSSCMSDataModelModelsCertificateRetrievalResponseCertificateStoreInventoryItemModel:
    """
    Attributes:
        store_machine (Union[Unset, None, str]):
        store_path (Union[Unset, None, str]):
        store_type (Union[Unset, int]):
        alias (Union[Unset, None, str]):
        chain_level (Union[Unset, int]):
        cert_store_id (Union[Unset, str]):
    """

    store_machine: Union[Unset, None, str] = UNSET
    store_path: Union[Unset, None, str] = UNSET
    store_type: Union[Unset, int] = UNSET
    alias: Union[Unset, None, str] = UNSET
    chain_level: Union[Unset, int] = UNSET
    cert_store_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_machine = self.store_machine
        store_path = self.store_path
        store_type = self.store_type
        alias = self.alias
        chain_level = self.chain_level
        cert_store_id = self.cert_store_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if store_machine is not UNSET:
            field_dict["storeMachine"] = store_machine
        if store_path is not UNSET:
            field_dict["storePath"] = store_path
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if alias is not UNSET:
            field_dict["alias"] = alias
        if chain_level is not UNSET:
            field_dict["chainLevel"] = chain_level
        if cert_store_id is not UNSET:
            field_dict["certStoreId"] = cert_store_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        store_machine = d.pop("storeMachine", UNSET)

        store_path = d.pop("storePath", UNSET)

        store_type = d.pop("storeType", UNSET)

        alias = d.pop("alias", UNSET)

        chain_level = d.pop("chainLevel", UNSET)

        cert_store_id = d.pop("certStoreId", UNSET)

        csscms_data_model_models_certificate_retrieval_response_certificate_store_inventory_item_model = cls(
            store_machine=store_machine,
            store_path=store_path,
            store_type=store_type,
            alias=alias,
            chain_level=chain_level,
            cert_store_id=cert_store_id,
        )

        return csscms_data_model_models_certificate_retrieval_response_certificate_store_inventory_item_model
