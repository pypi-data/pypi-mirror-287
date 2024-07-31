from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsEnrollmentManagementStoreType")


@_attrs_define
class CSSCMSDataModelModelsEnrollmentManagementStoreType:
    """
    Attributes:
        store_type_id (Union[Unset, int]):
        alias (Union[Unset, None, str]):
        overwrite (Union[Unset, bool]):
        properties (Union[Unset, None, List[Any]]):
    """

    store_type_id: Union[Unset, int] = UNSET
    alias: Union[Unset, None, str] = UNSET
    overwrite: Union[Unset, bool] = UNSET
    properties: Union[Unset, None, List[Any]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_type_id = self.store_type_id
        alias = self.alias
        overwrite = self.overwrite
        properties: Union[Unset, None, List[Any]] = UNSET
        if not isinstance(self.properties, Unset):
            if self.properties is None:
                properties = None
            else:
                properties = self.properties

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if store_type_id is not UNSET:
            field_dict["storeTypeId"] = store_type_id
        if alias is not UNSET:
            field_dict["alias"] = alias
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        store_type_id = d.pop("storeTypeId", UNSET)

        alias = d.pop("alias", UNSET)

        overwrite = d.pop("overwrite", UNSET)

        properties = cast(List[Any], d.pop("properties", UNSET))

        csscms_data_model_models_enrollment_management_store_type = cls(
            store_type_id=store_type_id,
            alias=alias,
            overwrite=overwrite,
            properties=properties,
        )

        return csscms_data_model_models_enrollment_management_store_type
