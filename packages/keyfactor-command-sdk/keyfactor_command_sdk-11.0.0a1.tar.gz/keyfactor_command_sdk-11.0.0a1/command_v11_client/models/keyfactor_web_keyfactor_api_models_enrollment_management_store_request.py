from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_keyfactor_api_models_enrollment_management_store_request_properties import (
        KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequestProperties,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequest:
    """
    Attributes:
        store_id (Union[Unset, str]):
        alias (Union[Unset, None, str]):
        overwrite (Union[Unset, bool]):
        properties (Union[Unset, None, KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequestProperties]):
    """

    store_id: Union[Unset, str] = UNSET
    alias: Union[Unset, None, str] = UNSET
    overwrite: Union[Unset, bool] = UNSET
    properties: Union[Unset, None, "KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequestProperties"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_id = self.store_id
        alias = self.alias
        overwrite = self.overwrite
        properties: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict() if self.properties else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if store_id is not UNSET:
            field_dict["storeId"] = store_id
        if alias is not UNSET:
            field_dict["alias"] = alias
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_keyfactor_api_models_enrollment_management_store_request_properties import (
            KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequestProperties,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        store_id = d.pop("storeId", UNSET)

        alias = d.pop("alias", UNSET)

        overwrite = d.pop("overwrite", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, None, KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequestProperties]
        if _properties is None:
            properties = None
        elif isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = KeyfactorWebKeyfactorApiModelsEnrollmentManagementStoreRequestProperties.from_dict(_properties)

        keyfactor_web_keyfactor_api_models_enrollment_management_store_request = cls(
            store_id=store_id,
            alias=alias,
            overwrite=overwrite,
            properties=properties,
        )

        return keyfactor_web_keyfactor_api_models_enrollment_management_store_request
