from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsWorkflowCertificateRequestCertStoreModel")


@_attrs_define
class CSSCMSDataModelModelsWorkflowCertificateRequestCertStoreModel:
    """
    Attributes:
        entry_name (Union[Unset, None, str]):
        client_machine (Union[Unset, None, str]):
        store_path (Union[Unset, None, str]):
    """

    entry_name: Union[Unset, None, str] = UNSET
    client_machine: Union[Unset, None, str] = UNSET
    store_path: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        entry_name = self.entry_name
        client_machine = self.client_machine
        store_path = self.store_path

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if entry_name is not UNSET:
            field_dict["entryName"] = entry_name
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine
        if store_path is not UNSET:
            field_dict["storePath"] = store_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        entry_name = d.pop("entryName", UNSET)

        client_machine = d.pop("clientMachine", UNSET)

        store_path = d.pop("storePath", UNSET)

        csscms_data_model_models_workflow_certificate_request_cert_store_model = cls(
            entry_name=entry_name,
            client_machine=client_machine,
            store_path=store_path,
        )

        return csscms_data_model_models_workflow_certificate_request_cert_store_model
