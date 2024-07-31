from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.csscms_data_model_enums_failure_type import CSSCMSDataModelEnumsFailureType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsInvalidKeystore")


@_attrs_define
class CSSCMSDataModelModelsInvalidKeystore:
    """
    Attributes:
        keystore_id (Union[Unset, str]):
        client_machine (Union[Unset, None, str]):
        store_path (Union[Unset, None, str]):
        alias (Union[Unset, None, str]):
        reason (Union[Unset, CSSCMSDataModelEnumsFailureType]):
        explanation (Union[Unset, None, str]):
    """

    keystore_id: Union[Unset, str] = UNSET
    client_machine: Union[Unset, None, str] = UNSET
    store_path: Union[Unset, None, str] = UNSET
    alias: Union[Unset, None, str] = UNSET
    reason: Union[Unset, CSSCMSDataModelEnumsFailureType] = UNSET
    explanation: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keystore_id = self.keystore_id
        client_machine = self.client_machine
        store_path = self.store_path
        alias = self.alias
        reason: Union[Unset, int] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        explanation = self.explanation

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keystore_id is not UNSET:
            field_dict["keystoreId"] = keystore_id
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine
        if store_path is not UNSET:
            field_dict["storePath"] = store_path
        if alias is not UNSET:
            field_dict["alias"] = alias
        if reason is not UNSET:
            field_dict["reason"] = reason
        if explanation is not UNSET:
            field_dict["explanation"] = explanation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        keystore_id = d.pop("keystoreId", UNSET)

        client_machine = d.pop("clientMachine", UNSET)

        store_path = d.pop("storePath", UNSET)

        alias = d.pop("alias", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, CSSCMSDataModelEnumsFailureType]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = CSSCMSDataModelEnumsFailureType(_reason)

        explanation = d.pop("explanation", UNSET)

        csscms_data_model_models_invalid_keystore = cls(
            keystore_id=keystore_id,
            client_machine=client_machine,
            store_path=store_path,
            alias=alias,
            reason=reason,
            explanation=explanation,
        )

        return csscms_data_model_models_invalid_keystore
