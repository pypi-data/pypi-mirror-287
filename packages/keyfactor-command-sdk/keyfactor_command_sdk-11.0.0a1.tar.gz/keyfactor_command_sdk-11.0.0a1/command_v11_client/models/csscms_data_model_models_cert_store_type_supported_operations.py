from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CSSCMSDataModelModelsCertStoreTypeSupportedOperations")


@_attrs_define
class CSSCMSDataModelModelsCertStoreTypeSupportedOperations:
    """
    Attributes:
        add (Union[Unset, bool]):
        create (Union[Unset, bool]):
        discovery (Union[Unset, bool]):
        enrollment (Union[Unset, bool]):
        remove (Union[Unset, bool]):
    """

    add: Union[Unset, bool] = UNSET
    create: Union[Unset, bool] = UNSET
    discovery: Union[Unset, bool] = UNSET
    enrollment: Union[Unset, bool] = UNSET
    remove: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        add = self.add
        create = self.create
        discovery = self.discovery
        enrollment = self.enrollment
        remove = self.remove

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if add is not UNSET:
            field_dict["add"] = add
        if create is not UNSET:
            field_dict["create"] = create
        if discovery is not UNSET:
            field_dict["discovery"] = discovery
        if enrollment is not UNSET:
            field_dict["enrollment"] = enrollment
        if remove is not UNSET:
            field_dict["remove"] = remove

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        add = d.pop("add", UNSET)

        create = d.pop("create", UNSET)

        discovery = d.pop("discovery", UNSET)

        enrollment = d.pop("enrollment", UNSET)

        remove = d.pop("remove", UNSET)

        csscms_data_model_models_cert_store_type_supported_operations = cls(
            add=add,
            create=create,
            discovery=discovery,
            enrollment=enrollment,
            remove=remove,
        )

        return csscms_data_model_models_cert_store_type_supported_operations
